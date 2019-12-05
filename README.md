# wazo-c4

This repository provides a docker compose and test suite for Wazo's C4 platform.

# Wazo Platform C4 overview

Wazo Platform allows you to build your own IP communication infrastructure and deliver innovative communication services. Fully open-source, API-centric, Cloud-native & multi-tenant, the project is designed around the famous open-source frameworks [Asterisk](https://www.asterisk.org/) & [Kamailio](https://www.kamailio.org/w/).

Wazo Platform aims to offer to service providers, entreprises and digital natives a coherent and complete reference platform for the design, deployment and management of a telecom infrastructure that can support very large volumes of simultaneous calls by interconnecting millions of users.

## What is a C4?

A C4 softswitch routes traffic between C5 softswitches.
The main characteristics of Wazo's C4 softswitch are:

* route large volume of calls
* protocol support and conversion
* transcoding
* billing interface
* security management
* call authentication

Wazo's C4 softswich provide intelligent call routing, which reduces congestion, latency, and costs while improving the quality of VoIP calls. Our C4 have several security features to protect the C5 switches.

We provide security functionalities such as SIP sanity checks, blocking the denial of service attacks and the SIP scanner. We handle normalization and SIP authentication.

## Run the development version

The development override `docker-compse.dev.yaml` allows you to edit the configuration files and get the changes reflected inside the contains using volume mounts.

```
$ docker-compose -f docker-compose.yaml -f docker-compose.dev.yaml up -d
```
## Tests

Running the tests once the C4 in docker compose is up and running is pretty simple:

```
$ docker exec wazo-c4_wazo-tester_1 pytest /tests/
```

Please refer to our testing tool called [wazo-tester](https://github.com/wazo-platform/wazo-tester) written in Python able to set up the Wazo environment, perform testing or stress testing with parallel sipp workers and custom scenarios for further info on how the tests work.

## Forcing pike off for stress testing purpose
```
docker exec -it wazo-c4_sbc_1 kamcmd pv.shvSet pike_off int 1
```
