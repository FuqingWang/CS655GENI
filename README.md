# CS655GENI Mini Project

## 1 Configurations

### 1.1 Proxy (cache) server ([Apache Traffic Server 7.1.2](https://docs.trafficserver.apache.org/en/7.1.x/))

1. Install ATS

   ```bash
   sudo apt-get update && sudo apt-get install trafficserver
   ```

2. Fix bugs ([link](https://serverfault.com/questions/917583/trafficserver-crashes-after-upgrade-to-ubuntu-bionic-segmentation-fault-address))

   ```bash
   sudo mkdir /var/run/trafficserver
   sudo chown -R trafficserver:trafficserver /var/run/trafficserver
   ```

3. Create Mapping Rules for HTTP Requests

   ```bash
   sudo vim /etc/trafficserver/remap.config
   ```

   Then add four mapping rules (make sure the IP address and port is correct):

   ```
   map http://10.10.1.1:8080/ http://10.10.2.2:80/
   reverse_map http://10.10.2.2:80/ http://10.10.1.1:8080/
   ```

4. Configure ATS to accept all request for caching:

   ```bash
   sudo vim /etc/trafficserver/records.config
   ```

   Modify the following line:

   ```
   CONFIG proxy.config.http.cache.required_headers INT 0
   ```

   Then save and quit vim

5. Filter URL for objects that are not to be cached

   ```bash
   sudo vim /etc/trafficserver/cache.config
   ```

   Add line: (this line means any object with suffix 'nocache' will never be cached by ATS)

   ```
   dest_domain=. suffix=nocache action=never-cache
   ```

6. Then reload configuration and restart ATS:

   ```bash
   sudo traffic_ctl config reload
   sudo traffic_ctl server restart
   ```

7. Set link delay

   ```bash
   sudo tc qdisc add dev eth1 root netem delay 10ms
   ```

   



