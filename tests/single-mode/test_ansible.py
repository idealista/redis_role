import pytest


@pytest.fixture()
def AnsibleDefaults(Ansible):
    return Ansible("include_vars", "defaults/main.yml")["ansible_facts"]


@pytest.fixture()
def AnsibleVars(Ansible):
    return Ansible("include_vars", "tests/group_vars/redis.yml")["ansible_facts"]


def test_redis_conf(File, AnsibleDefaults):
    conf_dir = File(AnsibleDefaults["redis_conf_path"])
    conf_file = File(AnsibleDefaults["redis_conf_path"] + "/redis.conf")
    assert conf_dir.exists
    assert conf_dir.is_directory
    assert conf_file.exists
    assert conf_file.is_file


def test_redis_service(File, Service, Socket, AnsibleDefaults):
    port = AnsibleDefaults["redis_port"]
    assert File("/lib/systemd/system/redis-server.service").exists
    assert Service("redis-server").is_enabled
    assert Service("redis-server").is_running
    assert Socket("tcp://" + ":::" + str(port)).is_listening
