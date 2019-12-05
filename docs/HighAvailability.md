# High Availability in Wazo Platform C4

## Introduction

Wazo Platform allows you to build your own IP communication infrastructure and deliver innovative communication services. Fully open-source, API-centric, Cloud-native & multi-tenant, the project is designed around the famous open-source frameworks [Asterisk](https://www.asterisk.org/) & [Kamailio](https://www.kamailio.org/w/). 

We're focused on delivering a cloud-native telecom solution with all the bells and whistles in the next months, scalability and high availability represent some of the fundamental features in our roadmap.

## Infrastructure

The platform consists of different boxes: Session Border Controller (SBC), Router, RTP Engine and router-confd API.

The routers are not accessed directly from carriers nor the termination IPBXs, as they are behind the SBC infrastructure. We assume then the routers are on an internal, non-externally accessible network segment and communicate with the SBC using the SIP protocol over UDP.

When a new SIP message reaches our SBC and satisfies our strict requirements regarding security and validation and thus it is ready to be forwarded to the routing layer, the target host is selected from a list managed using the [dispatcher module](https://kamailio.org/docs/modules/stable/modules/dispatcher.html).

This module offers SIP load balancer and SIP traffic dispatcher functionalities. It supports several different dispatching algorithms that you can choose from, for example: round-robin, weight based load balancing, call load distribution, and hashing over SIP message attributes. It also supports the auto-discovery of active/inactive gateways, which allows us to scale the routing layers and supporting health checks to detect dead routers.

## Dispatcher list

We use the `ds_select_dst` function from the `dispatcher` module to request up to two destination gateways for the SIP message being processed by the SBC. We store in a `dlg_var` the results in order to use them in case of failure while processing in-dialog messages. The failover itself is managed by the failure route in two different ways:

* Using the `ds_next_dst` function for failure while routing the first `INVITE` of a dialog; it uses the current state of the `ds_select_dst` function stored in the `xavp` variables.
* Using the previously stored address of the secondary router, recovering it from the dialog variables, for failure while routing the subsequent SIP messages within a dialog.

## Sharing dialogs and htables across the routers using DMQ

In order to be able to failover SIP messages and in-dialog messages across different SBCs and Routers running Kamailio we use htables which allows for key-value storage and in-dialog information.

Instead of using an external database to store these pieces of information to be shared between nodes, the [DMQ module](https://kamailio.org/docs/modules/stable/modules/dmq.html) is used. It implements a distributed message bus between Kamailio instances to enable the replication of data between them, allowing the DMQ nodes to communicate with each other by sending/receiving messages (either by broadcast or directly to a specific node). The system transparently deals with node discovery, consistency, retransmissions, etc.

## Auto discovery

All of our services use HTTP API requests towards Consul for registering and de registering. The data provided to Consul defines the type of the service, the IP and port, and also a Health-Check performed by Consul. We alse handle de-registration of services.

[Consul-template](HTTPs://github.com/hashicorp/consul-template) is a daemon that runs queries to and listens to events from the Consul cluster and updates different specified templates on the file system. It can optionally run commands after completing the update process.

For example it queries the consul API for services defined as `router` then lists them in a Kamailio dispatcher format. The format of the template is standard [GoLang templating](HTTPs://golang.org/pkg/text/template/) with the addition of several [functions](HTTPs://github.com/hashicorp/consul-template/blob/master/template/funcs.go). It also performs `kamcmd dispatcher.reload` to signal to Kamailio on our SBC to reload the dispatcher list.

## Conclusions

Wazo Platform C4 components are now easily scalable and auto-configure themselves thanks to Consul and `consul-template`. 
