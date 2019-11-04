# wazo-c4

wazo-c4 provides a docker compose and test suite for wazo c4.

## Run the development version

The development override `docker-compse.dev.yaml` allows you to edit the configuration files and get the changes reflected inside the contains using volume mounts.

```
$ docker-compose -f docker-compose.yaml -f docker-compose.dev.yaml up -d
```

## Forcing pike off for stress testing purpose
```
docker exec -it wazo-c4_sbc_1 kamcmd pv.shvSet pike_off int 1
```
