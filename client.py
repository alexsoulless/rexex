import docker


serverURL = "tcp://127.0.0.1:2375"

desktop = docker.DockerClient(base_url=serverURL)

if desktop.ping():
    print("server available")

container = desktop.containers.run(
    image="rexelserv", ports={"10500": 10500}, detach=True
)
output = container.attach(stdout=True, stream=True, logs=True)

print(output)
