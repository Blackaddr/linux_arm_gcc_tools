#!/bin/bash
# This script will zip up the linux tools then create the necessary binary cpp files
# for inclusion in a JUCE project
rm -f ./src/linuxTools.zip
rm -f ./target/BinaryToolsLinux*
pushd .
cd linux_tools
zip -r -y ../src/linuxTools.zip ./*
popd
BinaryBuilder src/ target/ BinaryToolsLinux
