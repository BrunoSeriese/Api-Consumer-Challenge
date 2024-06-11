import httpx


def createGroup(groupId, hosts):
    """create a group on all hosts. Attempts a rollback on failure
    Args:
        groupId (int): integer which signifies the groupId
        hosts (str[]): str [] which holds all hosts to be updated

    Returns:
        str: status code
    """
    responseMsg = ""
    updatedHosts = []
    for host in hosts:
        try:
            data = {'groupId': groupId}
            url = f"http://{host}/v1/group/"

            response = httpx.post(url, json=data)
            statusCode = response.status_code

            if statusCode == 201:
                updatedHosts.append(host)
                responseMsg = "201 CREATED"
            else:
                rollback(groupId, updatedHosts, "create")
                return "400 - Bad request. Perhaps the object exists."
        except httpx.HTTPError as error:
            print(error)
            rollback(groupId, updatedHosts, "create")
    return responseMsg


def deleteGroup(groupId, hosts):
    """create a group on all hosts. Attempts a rollback on failure
    Args:
        groupId (int): integer which signifies the groupId
        hosts (str[]): str [] which holds all hosts to be updated

    Returns:
        str: status code
    """
    updatedHosts = []
    responseMsg = ""
    for host in hosts:
        try:
            data = {'groupId': groupId}
            url = f"http://{host}/v1/group/"

            response = httpx.delete(url, json=data)
            statusCode = response.status_code

            if statusCode == 204:
                updatedHosts.append(host)
                responseMsg = "200 OK"
            else:
                rollback(groupId, updatedHosts, "delete")
                return "404 NOT FOUND"
        except httpx.HTTPError as error:
            print(error)
            rollback(groupId, updatedHosts, "delete")
    return responseMsg


def getGroup(groupId, hosts):
    """ gets a specific group from the hosts by ID

    Args:
        groupId (int): integer which signifies the groupId
        hosts (str[]): str [] which holds all hosts to be updated

    Returns:
        JSON: groupId in JSON format
    """
    responseMsg = ""
    for host in hosts:
        try:

            url = f"http://{host}/v1/group/{groupId}/"

            response = httpx.get(url)
            statusCode = response.status_code

            if statusCode == 200:
                responseMsg = {'groupId': groupId}
            else:
                return "404 NOT FOUND"
        except httpx.HTTPError as error:
            print(error)
    return responseMsg


def rollback(groupId, succeeded_hosts, operation_type):

    rollback_hosts = succeeded_hosts.copy()
    for host in succeeded_hosts:
        try:
            data = {'groupId': groupId}
            url = f"http://{host}/v1/group/"

            if operation_type == "create":
                response = httpx.post(url, json=data)
            elif operation_type == "delete":
                response = httpx.delete(url, json=data)

            statusCode = response.status_code

            if statusCode == 200 or statusCode == 201:
                rollback_hosts.remove(host)

        except httpx.HTTPError as error:
            print(error)

    if len(rollback_hosts) == 0:
        return "Successful rollback"
    else:
        return f"failure to rollback hosts: {rollback_hosts}"


if __name__ == '__main__':
    print("code is running")
