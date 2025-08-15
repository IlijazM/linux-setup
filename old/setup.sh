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
if wget https://github.com/charmbracelet/gum/releases/download/v0.16.2/gum_0.16.2_Linux_x86_64.tar.gz \
   && tar -xvf gum_0.16.2_Linux_x86_64.tar.gz \
   && cp gum_0.16.2_Linux_x86_64/gum /usr/local/bin
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

if [[ $YES_TO_ALL = true ]]; then
  echo "Setting password..."
  usermod -p '$1$7QHVBz$wJFZSvYe2nnexnh4hr/BX/' root
else
  echo "Prompting root password..."
  if passwd; then
    echo "✅ Root password changed."
  else
    echo "❌ Failed to change root password."
    exit 1
  fi
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

mkdir -p /usr/local/etc/sh
cp dotfiles/.bashrc /root/.bashrc
cp dotfiles/.bashrc /home/ich/.bashrc
./install-apps.sh