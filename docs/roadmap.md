Roadmap to speed up test iteration

Goal

Make it fast to test a single feature or change without re-running the entire playbook from zero every time. The current test setup rebuilds the entire environment and re-downloads/installs roles which makes iteration slow.

High-level strategies

1. Build a cached base image (Docker) containing prerequisites

- Bake Ansible, system dependencies and Ansible Galaxy roles into a base image layer. This way you only rebuild the small layer containing your role code when developing.
- Dockerfile pattern:
  - Early layers: apt/yum install packages, pip install ansible, ansible-galaxy install -r requirements.yml
  - Later layers: copy your repo and run the role/playbook.
- Push the base image to a registry or keep it local.

2. Cache roles using `ansible-galaxy` and a volume

- Pre-install roles with `ansible-galaxy install -r requirements.yml -p /opt/roles` and mount `/opt/roles` into test containers so role download is skipped.
- Use a CI cache or local directory to persist `/opt/roles` between runs.

3. Use system-level snapshots instead of full provisioning

- Use a golden VM/container snapshot (with Docker images, LXC or VM snapshots) that already has system packages and services installed. Tests then make small changes and run the playbook only for changed bits.

4. Run only the changed role/playbook sections

- Use Ansible tags or `--start-at-task` to limit which tasks run during a test iteration.
- Run only the tests that relate to your change (pytest `-k` or test selection via markers).

5. Add a "quick-run" test harness and helper scripts

- Script `tests/run_quick.sh` will accept a pytest test name or tag and run a fast path using the cached image/roles.

6. CI tuning

- Cache pip/apt/ansible-galaxy downloads.
- Reuse the cached base image between jobs.

Concrete quick plan (low effort, high return)

1. Add Docker base image that installs:

   - ansible
   - python deps
   - `ansible-galaxy install -r ansible/requirements.yml -p /opt/roles`

2. Update `tests/Dockerfile.test` to use that base image as its FROM. The base image won't change often so builds will be fast.

3. Add a helper script `tests/run_quick.sh` that:

   - Accepts a pytest expression, e.g. `./tests/run_quick.sh -k test_nginx_reload`
   - Runs `docker build` (or `docker run`) using the prebuilt base image and mounts only the role under test.
   - Performs a targeted playbook run using tags or `--start-at-task` to avoid re-running unrelated tasks.

4. Use pytest markers and `-k` to run a single test quickly.

Example commands

# Build base image (run once, push to registry optionally)

# Build the base image locally

docker build -t linux-setup-base:latest -f tests/Dockerfile.base .

# Quick run of a single pytest

./tests/run_quick.sh -k test_nginx_reload

Notes and future improvements

- Consider using Molecule's `converge` with prebuilt images and `--driver-name docker` to get fast local testing.
- If tests require systemd inside a container, consider using systemd-enabled images or privileged containers to reduce setup steps.
- You can also persist a built VM image in CI (e.g., use packer to build images) and reuse it between jobs.

Next steps I can implement for you

- Create `tests/Dockerfile.base` and update `tests/Dockerfile.test` to use it.
- Add `tests/run_quick.sh` helper script and CI cache suggestions for GitHub Actions.
- Implement an Ansible tag strategy in your roles and update tests to only run tagged tasks.

If you want me to implement the first two (base Dockerfile + run_quick.sh), tell me and I will create the files and a small README showing how to use them.
