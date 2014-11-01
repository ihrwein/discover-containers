# Discover linked Docker containers

When you link containers to each others, Docker creates new environment
variables. These variables contains important information but it's hard
to handle them.

This Python module dumps the available data about linked
containers into stdout in YAML format. You can then use templates to
modify your application's configuration based on this file.

The [JinYAML](https://github.com/ihrwein/jinyaml) project can use a YAML
file and a Jinja2 template to create new files. 

## Installation
On Ubuntu 14.04 you will need `python3-setuptools` installed.

```
/usr/bin/easy_install3 https://github.com/ihrwein/discover-containers/archive/master.zip
```

## Usage
It will create a `discover-containers` scipt in your PATH. By running it in
your container you can get some useful information about the linked containers:
```
containers:
- addr: 172.17.0.50
  name: ADMINVIEW_APP_3
  port: '8000'
  proto: TCP
  url: tcp://172.17.0.50:8000
- addr: 172.17.0.48
  name: ADMINVIEW_APP_2
  port: '8000'
  proto: TCP
  url: tcp://172.17.0.48:8000
```

Now, you can use this file to generate configurations.
## Use case #1

You have and nginx reverse proxy container and some uWSGI vessel containers behind it.
You link the vessels to nginx, but you may want to scale them, increase their numbers.
You can do this with fig, by:
```
fig scale app=4
```
which will create 4 app container instances. That's cool, but nginx doesn't know about them!

With this little Python program you can create an nginx configuration file, which contains
the reference to all of your app instances.
