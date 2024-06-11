import httpx

def createGroup(groupId,hosts):
    responseMsg = ""
    for host in hosts:
        try:
            data = {'groupId': groupId}
            url = f"http://{host}/v1/group/"

            response = httpx.post(url,json=data)
            statusCode = response.status_code

            if statusCode == 201:
                responseMsg = "201 CREATED"
            else:
                return "400 - Bad request. Perhaps the object exists."
        except httpx.HTTPError as error:
            print(error)
    return responseMsg

def deleteGroup(groupId,hosts):
    responseMsg = ""
    for host in hosts:
        try:
            data = {'groupId': groupId}
            url = f"http://{host}/v1/group/"

            response = httpx.delete(url,json=data)
            statusCode = response.status_code

            if statusCode == 204:
                responseMsg =  "200 OK"
            else:
                return "404 NOT FOUND"
        except httpx.HTTPError as error:
            print(error)
    return responseMsg
            
def getGroup(groupId,hosts):
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


if __name__ == '__main__':
    print("code is running")