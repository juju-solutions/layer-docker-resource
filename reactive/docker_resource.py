from charms.reactive import when

from charms import layer


@when('layer.docker-resource.pending')
def fetch():
    layer.docker_resource._fetch()
