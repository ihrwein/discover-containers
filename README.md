# Discover linked Docker containers

When you link containers to each others, Docker creates new environment
variables. These variables contains important information but it's hard
to handle them. This Python module dumps the available data about linked
containers into stdout in YAML format. You can then use templates to
modify your application's configuration.


