from utils.expect import expect, run

def test_ufw_installed():
    """Test that UFW is installed"""
    expect("ufw --version").to_contain("ufw", ignore_case=True)

def test_ufw_enabled():
    """Test that UFW is enabled and active"""
    expect("sudo ufw status").to_contain("Status: active")

def test_ufw_default_incoming_deny():
    """Test that UFW default policy for incoming is deny"""
    expect("sudo ufw status verbose").to_contain("Default: deny (incoming)")

def test_ufw_default_outgoing_allow():
    """Test that UFW default policy for outgoing is allow"""
    expect("sudo ufw status verbose").to_contain("Default: allow (outgoing)")

def test_ufw_allows_port_80():
    """Test that UFW allows port 80 (HTTP)"""
    expect("sudo ufw status numbered").to_contain("80/tcp")

def test_ufw_allows_port_443():
    """Test that UFW allows port 443 (HTTPS)"""
    expect("sudo ufw status numbered").to_contain("443/tcp")

def test_ufw_allows_port_4242():
    """Test that UFW allows port 4242 (SSH)"""
    expect("sudo ufw status numbered").to_contain("4242/tcp")

def test_ufw_port_80_rule_exists():
    """Test that port 80 has an ALLOW rule"""
    output = run("sudo ufw status numbered")
    assert "80/tcp" in output and "ALLOW IN" in output

def test_ufw_port_443_rule_exists():
    """Test that port 443 has an ALLOW rule"""
    output = run("sudo ufw status numbered")
    assert "443/tcp" in output and "ALLOW IN" in output

def test_ufw_port_4242_rule_exists():
    """Test that port 4242 has an ALLOW rule"""
    output = run("sudo ufw status numbered")
    assert "4242/tcp" in output and "ALLOW IN" in output
