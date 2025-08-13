#!/bin/bash

ls apps | grep -v default | xargs gum choose --no-limit --selected=$(cat apps/default) | xargs -I{} sh "./apps/{}"