# wazo-c4

wazo-c4 provides a docker compose and test suite for wazo c4.

## Forcing pike off for stress testing purpose
```
docker exec -it wazo-c4_sbc_1 kamcmd pv.shvSet pike_off int 1
```
