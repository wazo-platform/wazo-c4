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

The development override `docker-compose.dev.yaml` allows you to edit the configuration files and get the changes reflected inside the contains using volume mounts.

```ShellSession
$ docker-compose -f docker-compose.yaml -f docker-compose.dev.yaml up -d
```

## Run with wazo-auth for wazo portal integration

To run the plaform using wazo-auth :

```ShellSession
$ docker-compose -f docker-compose.yaml -f docker-compose.wazo-auth.yaml up -d --force-recreate -V
```

Using the C4 with Wazo's portal is easy in dev mode running the C4 repo with:
```ShellSession
$ make start-auth
```

When everything is up and running insert the required tenants with:
```ShellSession
$ make auth-setup
```

Now connect to the local C4 instance in the portal interface and you can insert the required routing data via the UI.

## Tests

Running the tests once the C4 in docker compose is up and running is pretty simple:

```ShellSession
$ docker-compose exec wazo-tester pytest -v /tests/
```

Please refer to our testing tool called [wazo-tester](https://github.com/wazo-platform/wazo-tester) written in Python able to set up the Wazo environment, perform testing or stress testing with parallel sipp workers and custom scenarios for further info on how the tests work.

If you want to test the all in one SBC (using `docker-compose-aio.yaml`), you need to add specific options to select tests like:

```ShellSession
$ docker-compose -f docker-compose-aio.yaml exec wazo-tester pytest -v pytest -v -k " not router and not failover" /tests/
```

## Forcing pike off for stress testing purpose

```ShellSession
$ docker-compose exec sbc kamcmd pv.shvSet pike_off int 1
```

## For new test in development platform, do not forget to clean postgresql db
To be sure do not have old data on db, remove in data/pgsql !
