# Add /root/bin
if [[ -d ~/bin ]]; then
  export PATH="$HOME/bin:$PATH"
fi

# Iterate over all /usr/local/etc/sh/*.sh files and source them
if [[ -d /usr/local/etc/sh ]]; then
  for file in /usr/local/etc/sh/*.sh; do
    if [[ -f $file ]]; then
      source "$file"
    fi
  done
fi