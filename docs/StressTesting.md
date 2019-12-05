# Stress Testing Wazo's C4
_Last update: December 5th 2019._

As per our definition of the Wazo Platform:

```
Wazo Platform aims to offer to service providers, entreprises and digital natives a coherent and complete reference platform for the design, deployment and management of a telecom infrastructure that can support very large volumes of simultaneous calls by interconnecting millions of users.
```

We need to be able to perform tests that guarantee that our infrastructure is able to handle large volumes of simultaneous calls and handle millions of users.

## Architectures used

Wazo's C4 is deployable on different architectures and platforms. We use ansible in order to install Wazo on dedicated servers or virtual machines. We have a docker compose to deploy Wazo's C4 in containers and We recently provided a Helm chart in order to deploy Wazo's C4 on Kubernetes.

So we decided to perform the tests on all the above mentioned platforms.

## Wazo-Tester

Please refer to our testing tool called [wazo-tester](https://github.com/wazo-platform/wazo-tester) written in Python able to set up the Wazo environment, perform testing or stress testing with parallel sipp workers and custom scenarios for further info on how the tests work.

## Forcing pike off for stress testing purpose

Our Session Border Controller (SBC) provides different secutiry features, one of them is using [Pike](https://kamailio.org/docs/modules/5.2.x/modules/pike.html).

The pike module keeps trace of all (or selected ones) incoming request's IP source and blocks the ones that exceed the limit. It works simultaneously for IPv4 and IPv6 addresses.

Prior to performing stress tests turning pike off is needed:
```
docker exec -it wazo-c4_sbc_1 kamcmd pv.shvSet pike_off int 1
```

## Testing parameters

We performed two runs of each test running 1.000 calls with a call duration of 30 seconds.
The tests are run with 10, 20, 30 and 40 calls per second (cps).

## Results

### Docker Compose
With docker compose and the configuration of 1 SBC, 2 Routers and 1 router-confd we observed the best performances
and zero failed calls up to 20 cps. On 30 cps we experienced some failed calls and 10% retransmission of packets. On 40cps the retransmissions reached 25% and we experienced 130 failed calls of 1.000.

| CPS        |  10   | 20    | 30  | 40  |
| -------    | ---   | ---   | --- | --- |
| successful | 1.000 | 1.000 | 979 | 870 |
| failed     | 0     | 0     | 21  | 130 |

### Kubernetes cluster
On Kubernetes we experienced the worst performance. The retransmissions were present even on 10cps. The calls were failing and we suppose it is due to networking issues.
We currently use Wave Net networking in our cluster. We will try other networking solutions and re run the tests.

### Virtual Machine
TBD
