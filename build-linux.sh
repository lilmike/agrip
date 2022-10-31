#!/bin/bash

# Cleanup Quake-Tools:
pushd giants/Quake-Tools &&
rm -rf qutils &&
git checkout "*" &&
popd
LDFLAGS="-lGL -lX11 -lGLU" ./build-all.py
