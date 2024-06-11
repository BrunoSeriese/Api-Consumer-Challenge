import httpx

hosts = [
    'node1.example.com',
    'node2.example.com',
    'node3.example.com'
]


def createGroup(groupId):
    for host in hosts:
        try:
            data = {'groupId': groupId}
            url = f"http://{host}/v1/group/"

            response = httpx.post(url,json=data)
            statusCode = response.status_code

            if statusCode == 201:
                print(f"group created with ID:{groupId}")
            else:
                print(f"group creation failed with statuscode:{statusCode}")
        except httpx.HTTPError as error:
            print(error)

def deleteGroup(groupId):
    for host in hosts:
        try:
            data = {'groupId': groupId}
            url = f"http://{host}/v1/group/"

            response = httpx.delete(url,json=data)
            statusCode = response.status_code

            if statusCode == 200:
                print(f"group deleted with ID:{groupId}")
            else:
                print(f"group deleten failed with statuscode:{statusCode}")
        except httpx.HTTPError as error:
            print(error)
            
def getGroup(groupId):
    for host in hosts:
        try:
         
            url = f"http://{host}/v1/group/{groupId}/"

            response = httpx.get(url)
            statusCode = response.status_code

            if statusCode == 200:
                print(f"group found with ID:{groupId}")
            else:
                print(f"group creation failed with statuscode:{statusCode}")
        except httpx.HTTPError as error:
            print(error)
