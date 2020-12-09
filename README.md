# CS655GENI Mini Project

> Note: Please check the IP address for each node before configuration. For example, if the IP address for `cache` node is `10.10.1.1`, so you need to replace all `10.10.1.2` with `10.10.1.1` for any involved configuration below.

## 1 Configurations

### 1.1 Proxy (cache) server ([Apache Traffic Server 7.1.2](https://docs.trafficserver.apache.org/en/7.1.x/))

1. Install ATS (Install from source code is preferred, see [here](https://docs.trafficserver.apache.org/en/latest/getting-started/index.en.html#installation))

   ```bash
   sudo apt-get update && sudo apt-get install trafficserver
   ```

2. Fix bug ([link](https://serverfault.com/questions/917583/trafficserver-crashes-after-upgrade-to-ubuntu-bionic-segmentation-fault-address))

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
   map http://10.10.1.2:8080/ http://10.10.2.2:80/
   ```

   > Note: Please check if the IP address of cache node is `10.10.1.2`. If its `10.10.1.1`, replace `10.10.1.2` above with `10.10.1.1`

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

   Add line: (this line means any object with suffix `nocache` will never be cached by ATS)

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

   

### 1.2 Server ([Apache2 Web Server 2.4.29](https://httpd.apache.org/))

1. Install Apache2

   ```bash
   sudo apt-get update && sudo apt-get install apache2
   ```

2. **[Optional]** Configure static file path in VirtualHost setting file (here you can set another folder as static folder instead of `users/[your_path]/`)

   ```bash
   sudo vim /etc/apache2/sites-available/000-default.conf
   ```

   Add the following lines:

   ```
   Alias /static/ /users/[your_path]/
   <Directory /users/[your_path]/>
       Require all granted
   </Directory>
   ```

   Then restart apache2 web server:

   ```bash
   sudo service apache2 restart
   ```

   > You can skip this step, then all the file to be delivered should be under `/var/www/html/`

3. Set link delay

   ```bash
   sudo tc qdisc add dev eth1 root netem delay 30ms
   ```

4. Generate file for experiments

   ```bash
   wget pcvm1-19.genirack.nyu.edu/static/generateFile.sh
   sudo bash generateFile.sh
   ```

   > This step will download a script called `generateFile.sh`. Two folders - `cache/` and `nocache/` will be created with 20 files of size from 5MB to 100MB.

### 1.3 Client

1. Install pip3

   ```bash
   sudo add-apt-repository universe
   sudo apt-get update && sudo apt-get install python3-pip
   ```

2. Install matplotlib using pip3

   ```bash
   sudo pip3 install matplotlib
   ```

   > Library 'matplotlib' will be used to plot line charts.



---

## 2 Prepare for experiments

### 2.1 Retrieving scripts & codes

1. Login to `client` node, and direct to the folder you want to execute you experiments (e.g. `/users/[your_Path]/`).

2. Retrieve codes for experiments using `wget`:

   ```bash
   wget pcvm1-19.genirack.nyu.edu/static/experiments/exp1_timeWithCache.py
   wget pcvm1-19.genirack.nyu.edu/static/experiments/exp1_timeWithoutCache.py
   wget pcvm1-19.genirack.nyu.edu/static/experiments/exp1_plot.py
   wget pcvm1-19.genirack.nyu.edu/static/experiments/exp2_hitrate.py
   wget pcvm1-19.genirack.nyu.edu/static/experiments/exp2_plot.py
   ```

   > Note: Please check the IP address for 'cache' node. If the IP address for `cache` node is `10.10.1.1`, so you need to replace all `10.10.1.2` with `10.10.1.1` for any involved experiments retrieved above.

### 2.2 Check if ATS works

1. Login to `cache` node

2. Check status

   ```bash
   sudo /etc/init.d/trafficserver status
   ```



