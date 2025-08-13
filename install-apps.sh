#!/bin/bash

ls apps | grep -v default | xargs ./gum_0.16.2_Linux_x86_64/gum choose --no-limit --selected=$(cat apps/default) | xargs -I{} sh "./apps/{}"