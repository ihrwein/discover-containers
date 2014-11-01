import os
import re
import yaml

ALIAS_RE = re.compile(".*_NAME$")
URL_RE = re.compile("(\w+)_PORT_([0-9]+)_([a-zA-Z0-9]+)$")

def read_environment_vars():
    return dict(os.environ)

def get_url_names(envvars):
    url_vars = filter(lambda key: URL_RE.match(key), envvars)
    # normalizing by their URL
    swapped_vars = dict((envvars[i], i) for i in url_vars)
    return dict((value, key) for key, value in swapped_vars.items())

def main():
    envvars = read_environment_vars()
    urls = get_url_names(envvars)

    containers = []
    for i in urls:
        m = URL_RE.match(i)
        d = {}
        d["name"] = m.group(1)
        d["port"] = m.group(2)
        d["proto"] = m.group(3)
        d["addr"] = os.getenv(i + "_ADDR")
        d["url"] = urls[i]
        containers.append(d)
    print(yaml.dump(data={'containers': containers},default_flow_style=False))

if __name__ == "__main__":
    main()
