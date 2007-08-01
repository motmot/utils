#!/bin/bash

echo "= Dependency list ="
echo
echo -n "The following list of dependencies was generated automatically"
echo    "by the {{{motmot_utils/debian_show_depends.sh}}} script."
echo
echo -n "These were generated on an Ubuntu system, but will give you a"
echo    "rough feel for other systems, too."
echo
echo "== Dependencies for building motmot packages on Ubuntu =="

for srcpkg in camiface python-flymovieformat wxglvideo wxwrap wxvalidatedtext motmotutils fview
do
  echo -n " * $srcpkg "
  apt-cache showsrc $srcpkg | grep Version | head -n 1
  echo -n "  "
  apt-cache showsrc $srcpkg | grep Build-Depends | head -n 1
done

echo
echo "== Dependencies for running motmot packages on Ubuntu =="

for pkg in python-camiface python-flymovieformat python-wxglvideo python-wxwrap python-wxvalidatedtext python-motmotutils python-fview
do
  echo -n " * $pkg "
  apt-cache show --no-all-versions $pkg | grep '^Version'
  echo -n "  "
  apt-cache show --no-all-versions $pkg | grep Depends
done

