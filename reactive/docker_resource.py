from charmhelpers.core import hookenv
from charms.reactive import set_flag, when, when_not

from charms import layer


@when_not('layer.docker-resource.auto-fetched')
def auto_fetch():
    resources = hookenv.metadata().get('resources', {})
    for name, resource in resources.items():
        is_docker = resource.get('type') == 'docker'
        is_auto_fetch = resource.get('auto-fetch', False)
        if is_docker and is_auto_fetch:
            layer.docker_resource.fetch(name)
    set_flag('layer.docker-resource.auto-fetched')


@when('layer.docker-resource.pending')
def fetch():
    layer.docker_resource._fetch()
