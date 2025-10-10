from utils.expect import expect, run

def test_hello_world_service():
    run("mkdir -p /srv/services/hello-world")
    run("echo -e 'server {\\n    listen 80;\\n    server_name hello-world.ilijaz.example;\\n    location / {\\n        default_type text/plain;\\n        return 200 \"Hello World\";\\n    }\\n}' > /srv/services/hello-world/conf.nginx")
    run("nginx")
    expect("nginx -s reload").to_contain("signal process started", output="stderr")
    expect("curl localhost:8080 -H 'Host: hello-world.ilijaz.example'", container=None).to_return("Hello World")

def test_nginx_installed():
    run("nginx")
    expect("nginx -v").to_contain("nginx", output="stderr")

def test_nginx_config_syntax():
    run("nginx")
    expect("nginx -t").to_contain("syntax is ok", output="stderr")

def test_nginx_reload():
    expect("nginx -s reload").to_contain("signal process started", output="stderr")

def test_nginx_ssl_certificates():
    # Check if default SSL cert exists in the container
    expect("test -f /etc/letsencrypt/live/default/fullchain.pem").to_not_fail()
    expect("test -f /etc/letsencrypt/live/default/privkey.pem").to_not_fail()

def test_nginx_custom_config():
    # Check if custom config is present
    expect("cat /etc/nginx/conf.d/srv-apps.conf").to_contain("server")
