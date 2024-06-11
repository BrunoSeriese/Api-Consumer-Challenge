import requests
import pytest
import httpx
from httpx import Response
from main import createGroup, deleteGroup, getGroup, rollback

hosts = [
    'node1.example.com',
    'node2.example.com',
    'node3.example.com'
]


@pytest.mark.parametrize('groupId', [1])
def test_createGroup(mocker, groupId):
    """test the creation of groups

    Args:
        mocker (obj):  mocks url
        groupId (int): integer which signifies the groupId
    """
    mocker.patch('httpx.post')
    httpx.post.return_value = Response(201)

    result = createGroup(groupId, hosts)
    expected_output = "201 CREATED"
    assert result == expected_output


@pytest.mark.parametrize('groupId', [1])
def test_deleteGroup(mocker, groupId):
    """test the deletion of groups

    Args:
        mocker (obj):  mocks url
        groupId (int): integer which signifies the groupId
    """
    mocker.patch('httpx.delete')
    httpx.delete.return_value = Response(204)

    result = deleteGroup(groupId, hosts)
    expected_output = "200 OK"
    assert result == expected_output


@pytest.mark.parametrize('groupId', [1])
def test_getGroup(mocker, groupId):
    """test getting specific groups

    Args:
        mocker (obj):  mocks url
        groupId (int): integer which signifies the groupId
    """
    mocker.patch('httpx.get')
    httpx.get.return_value = Response(200)

    result = getGroup(groupId, hosts)
    expected_output = {'groupId': groupId}
    assert result == expected_output


@pytest.mark.parametrize('groupId', [1])
def test_rollback(mocker, groupId):
    """test rolling back interrupted changes

    Args:
        mocker (obj):  mocks url
        groupId (int): integer which signifies the groupId
    """

    succeeded_hosts = ['node1', 'node2', 'node3']
    operation_type = "create"

    mocker.patch('httpx.post')

    if operation_type == "create":
        httpx.post.return_value = Response(200)

    result = rollback(groupId, succeeded_hosts, operation_type)
    expected_output = "Successful rollback"
    assert result == expected_output
