from utils.expect import run, expect

def test_hello_world_service():
    run("mkdir -p /srv/services/hello-world")
    run("echo -e 'server {\\n    listen 80;\\n    server_name hello-world.ilijaz.example;\\n    location / {\\n        default_type text/plain;\\n        return 200 \"Hello World\";\\n    }\\n}' > /srv/services/hello-world/conf.nginx")
    expect("nginx")
    expect("nginx -s reload").to_not_fail()
    expect("curl localhost:8080 -H 'Host: hello-world.ilijaz.example'", container=None).to_return("Hello World")
