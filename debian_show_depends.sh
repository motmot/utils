#!/bin/bash

echo "= Dependency list ="
echo
echo -n "The following list of dependencies was generated automatically "
echo    "by the {{{motmot_utils/debian_show_depends.sh}}} script."
echo
echo -n "These were generated on an Ubuntu system, but will give you a "
echo    "rough feel for other systems, too."
echo
echo "== Dependencies for building motmot packages on Ubuntu =="

# XXX Need to update this. Here are most of the binaries:

binpkgs="libcamiface python-motmot-utils python-posixsched python-motmot-fastimage python-motmot-flytrax python-motmot-fview python-motmot-fview-livehistogram python-motmot-fview-udplogger python-motmot-imops python-motmot-camiface python-motmot-realtimeimageanalysis python-motmot-trackem python-motmot-wxglvideo python-motmot-wxvalidatedtext python-motmot-wxvideo"

for binpkg in $binpkgs; do
    #echo $binpkg
    srcpkg=`apt-cache show --no-all-versions $binpkg | grep '^Source' | sed 's/Source: //g'`
    #echo $binpkg $srcpkg
#done
#exit 0

#for srcpkg in camiface python-flymovieformat wxglvideo wxvideo imops wxwrap wxvalidatedtext motmotutils fview
#do
  echo -n " * $srcpkg "
  apt-cache showsrc $srcpkg | grep Version | head -n 1
  echo -n "  "
  apt-cache showsrc $srcpkg | grep Build-Depends | head -n 1
done

echo
echo "== Dependencies for running motmot packages on Ubuntu =="

for binpkg in $binpkgs; do
  echo -n " * $binpkg "
  apt-cache show --no-all-versions $binpkg | grep '^Version'
  echo -n "  "
  apt-cache show --no-all-versions $binpkg | grep Depends
done

