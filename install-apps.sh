#!/bin/bash

if $YES_TO_ALL; then
  ls apps | grep -v default | xargs -I{} sh "./apps/{}"
else
  ls apps | grep -v default | xargs gum choose --no-limit --selected=$(cat apps/default) | xargs -I{} sh "./apps/{}"
fi