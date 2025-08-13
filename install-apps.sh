#!/bin/bash

if [[ $YES_TO_ALL = true ]]; then
  ls apps | grep -v default | xargs -I{} /bin/bash "./apps/{}"
else
  ls apps | grep -v default | xargs gum choose --no-limit --selected=$(cat apps/default) | xargs -I{} /bin/bash "./apps/{}"
fi