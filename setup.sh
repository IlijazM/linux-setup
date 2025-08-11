#!/bin/bash

#region Step 1. Setup:
echo ""
echo "Step 1. Setup:"
echo "--------------"

echo "Running update and upgrade..."
if apt update && apt upgrade -y; then
  echo "✅ Upgrade run successfully."
else
  echo "❌ Upgrade failed."
fi

echo "Installing useful packages..."
if apt install git curl wget net-tools nano sudo -y; then
  echo "✅ Useful packages installed."
else
  echo "❌ Failed to install useful packages."
  exit 1
fi

echo "Installing gum..."
if cd /tmp \
   && wget https://github.com/charmbracelet/gum/releases/download/v0.16.2/gum_0.16.2_Linux_x86_64.tar.gz \
   && tar -xvf gum_0.16.2_Linux_x86_64.tar.gz \
   && alias gum="/tmp/gum_0.16.2_Linux_x86_64/gum";
then
  echo "✅ Gum installed."
else
  echo "❌ Failed to install gum."
  exit 1
fi
#endregion

#region Step 2. Setup users:
echo ""
echo "Step 2. Setup users:"
echo "--------------------"

echo "Prompting root password..."
if passwd; then
  echo "✅ Root password changed."
else
  echo "❌ Failed to change root password."
  exit 1
fi

echo "Adding user 'ich'..."
if useradd -m ich && passwd -d ich && usermod -aG sudo ich && sudo -u ich whoami; then
  echo "✅ Added user 'ich'."
else
  echo "❌ Failed to add user 'ich'."
  exit 1
fi
#endregion

#region Step 3. Setup SSH:
echo ""
echo "Step 3. Setup SSH:"
echo "------------------"

echo "Generating SSH key..."
if ssh-keygen -t ed25519 -C "mehmedovic.ilijaz@gmail.com" -f ~/.ssh/id_ed25519 -N "" -q; then
  echo "✅ SSH key generated."
else
  echo "❌ Failed to generate SSH key."
  exit 1
fi

echo "Adding SSH keys to authorized_keys..."
if mkdir /home/ich/.ssh \
   && echo -e "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFk1Do6byK1ypZC5KuDR/dIqqPooycR7BqkGMghP/flD ilijaz@fedora.fritz.box\nssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDaBwDMkOF7SHfCrHbhfK9+6QSBbiEWnmXXGsh/zKOfoc6n5GvKPGYvGYy+yW7UNKYVKapgwgYxKJgTJ5/PisnSvuCNMzN3SRT47W6RNMaY3EcIUF5chJAsR/J3dA46F2LZJTZOZH+jD3POclIxq2bkEH5WVObv5SxqW3HTj2bck1JXAYlZqCAulV0brYnFWqMMiT3JQTENRY27EZAB6ctDk7siS/41af8XuC9ais7zQWKU1jUwm/BwRBhfN2/OpSW+zO66SdKcGCMt0e/eQtvcN7yEtam1RRk9IH93lE8V1iujCxk8H4/K7JhAG1wLT1KrlzHj12gfhY+beXysHUHRnNUhDjJ4w4T8sVSRwpvjWPCQrtRngqzMPpNoAH61+TCb315SC+rLYBDXora+pf02PLrYHA/NvuVl0ydaCgE2wgQ21QuOP81oD8joppCBfP0u0T5QLRMXZGp5eI6+NcOIsnSUP1bpBusCiu8mg4DQhMwGsEZxwLwOALxkp7NYtXU= azuread\ilijazmehmedovic@RIMIT020\nssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGf+R+0mu74RfSnDS7SmeqylPJaXqVAGA47tK758szm9 mehmedovic.ilijaz@gmail.com\nssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBj/CNNH44dlEU8Uu6U11SRG0op2mnP4ti/qb4vkzDO7 ilijazm@ilijaz\n" > /home/ich/.ssh/authorized_keys;
then
  echo "✅ SSH keys added to authorized_keys."
else
  echo "❌ Failed to add SSH keys to authorized_keys."
  exit 1
fi

echo "Updating SSH config..."
echo "Changing SSH port from 22 to 4242..."
if sed -i 's/#Port 22/Port 4242/' /etc/ssh/sshd_config; then
  if grep -q "Port 4242" /etc/ssh/sshd_config; then
    echo "✅ SSH port successfully changed."
  else
    echo "❌ Failed to change SSH port."
    exit 1
  fi
else
  echo "❌ An error occurred while running sed for SSH port."
  exit 1
fi

echo "Disallowing root login..."
if sed -i 's/PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config; then
  if grep -q "PermitRootLogin no" /etc/ssh/sshd_config; then
    echo "✅ Root login successfully disallowed."
  else
    echo "❌ Failed to disallow root login."
    exit 1
  fi
else
  echo "❌ An error occurred while running sed for root login."
  exit 1
fi

echo "Restarting SSH service..."
if systemctl restart sshd; then
  echo "✅ SSH service restarted."
else
  echo "❌ Failed to restart SSH service."
  exit 1
fi
#endregion

#region Step 4. Setup firewall:
echo ""
echo "Step 4. Setup firewall:"
echo "-----------------------"

echo "Installing UFW..."

if gum spin --title "apt install ufw -y" -- apt install ufw -y; then
  echo "✅ UFW installed."
else
  echo "❌ Failed to install ufw."
  exit 1
fi

echo "Setting up UFW..."
if ufw default deny incoming \
   && ufw default allow outgoing \
   && ufw allow 4242/tcp \
   && ufw allow 443/tcp \
   && ufw allow 80/tcp;
then
  echo "✅ UFW setup."
else
  echo "❌ Failed to setup UFW".
  exit 1
fi
#endregion

#region Step 5. Setting up zsh:
echo ""
echo "Step 5. Setting up zsh:"
echo "-----------------------"

echo "Installing ZSH..."
if gum spin --title "apt install zsh -y" -- apt install zsh -y; then
  echo "✅ ZSH installed."
else
  echo "❌ Failed to install ZSH."
  exit 1
fi

echo "Installing zsh config..."
if cd /tmp
   && gum spin --title "git clone https://github.com/Bleuzen/linux-setup.git" -- git clone https://github.com/Bleuzen/linux-setup.git
   && cd linux-setup; then
  echo "✅ ZSH config installed."
else
  echo "❌ Failed to install ZSH config."
  exit 1
fi

echo "Configuring ZSH for root user..."
if gum spin --title "sh /tmp/linux-setup/setup-user-zsh.sh" -- sh /tmp/linux-setup/setup-user-zsh.sh
   && chsh -s $(which zsh); then
  echo "✅ ZSH configured for root user."
else
  echo "❌ Failed to configure ZSH for root user."
  exit 1
fi

echo "Configuring ZSH for user 'ich'..."
if gum spin --title "sudo -u ich sh /tmp/linux-setup/setup-user-zsh.sh" -- sudo -u ich sh /tmp/linux-setup/setup-user-zsh.sh
   && sudo -u ich chsh -s  $(which zsh); then
  echo "✅ ZSH configured for user 'ich'."
else
  echo "❌ Failed to configure ZSH for user 'ich'."
  exit 1
fi

echo "Define aliases for user 'ich'..."
if echo -e '\n\n# Aliases\n\nalias l="ls -l"\nalias ll="ls -lah"\nalias d="sudo docker"\nalias c="d compose"\nalias cu="c up --build -d"\nalias cr="c down && cu"\nalias cl="c logs -f"\nalias crl="cr && cl"\n\nalias nC="nano /root/apps/caddy/Caddyfile"\n\nalias nginx="d exec -it nginx-nginx-1 nginx"\n\nalias cval="docker exec caddy caddy validate --config /etc/caddy/Caddyfile"\nalias crel="docker exec caddy caddy reload --config /etc/caddy/Caddyfile"\nalias cfmt="docker exec caddy caddy fmt --overwrite /etc/caddy/Caddyfile"\nalias caddy="nC && cval && cfmt && crel"\n\n' >> /home/ich/.zshrc;
then
  echo "✅ Aliases defined for user 'ich'."
else
  echo "❌ Failed to define aliases for user 'ich'."
  exit 1
fi

echo "Define aliases for root user..."
if echo -e '\n\n# Aliases\n\nalias l="ls -l"\nalias ll="ls -lah"\nalias d="sudo docker"\nalias c="d compose"\nalias cu="c up --build -d"\nalias cr="c down && cu"\nalias cl="c logs -f"\nalias crl="cr && cl"\n\nalias nC="nano /root/apps/caddy/Caddyfile"\n\nalias nginx="d exec -it nginx-nginx-1 nginx"\n\nalias cval="docker exec caddy caddy validate --config /etc/caddy/Caddyfile"\nalias crel="docker exec caddy caddy reload --config /etc/caddy/Caddyfile"\nalias cfmt="docker exec caddy caddy fmt --overwrite /etc/caddy/Caddyfile"\nalias caddy="nC && cval && cfmt && crel"\n\n' >> /root/.zshrc;
then
  echo "✅ Aliases defined for root user."
else
  echo "❌ Failed to define aliases for root user."
  exit 1
fi
#endregion

gum choose --header "Select Software to install" --selected="docker,node" --no-limit "docker" "node" | xargs cat | sh