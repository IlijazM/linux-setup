# Can't run tests because of docker in podman not setup

# from utils.expect import expect, run

# def ensure_nginx_running():
#     # start docker deamon
#     run("service docker start")
#     # ensure nginx container is running
#     run("docker compose -f /opt/nginx/docker-compose.yml up -d")


# # def test_hello_world_service():
# #     run("mkdir -p /srv/services/hello-world-nginx")
# #     run("echo -e 'server {\\n    listen 80;\\n    server_name hello-world-nginx.ilijaz.example;\\n    location / {\\n        default_type text/plain;\\n        return 200 \"Hello World from Nginx\";\\n    }\\n}' > /srv/services/hello-world-nginx/conf.nginx")
# #     ensure_nginx_running()
# #     expect("nginx -s reload").to_contain("signal process started", output="stderr")
# #     expect("curl localhost:8080 -H 'Host: hello-world-nginx.ilijaz.example'", container=None).to_return("Hello World from Nginx")

# # def test_nginx_installed():
# #     ensure_nginx_running()
# #     expect("nginx -v").to_contain("nginx", output="stderr")

# def test_nginx_config_syntax():
#     ensure_nginx_running()
#     expect("nginx -t").to_contain("syntax is ok", output="stderr")

# # def test_nginx_reload():
# #     expect("nginx -s reload").to_contain("signal process started", output="stderr")

