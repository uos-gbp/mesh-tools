%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-mesh-msgs-hdf5
Version:        1.1.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS mesh_msgs_hdf5 package

License:        BSD-3
URL:            http://wiki.ros.org/ros_mesh_tools/mesh_msgs_hdf5
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-hdf5-map-io
Requires:       ros-noetic-label-manager
Requires:       ros-noetic-mesh-msgs
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-hdf5-map-io
BuildRequires:  ros-noetic-label-manager
BuildRequires:  ros-noetic-mesh-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Read mesh_msgs from hdf5

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Wed Oct 27 2021 Sebastian Pütz <spuetz@uos.de> - 1.1.0-1
- Autogenerated by Bloom

* Fri Dec 18 2020 Sebastian Pütz <spuetz@uos.de> - 1.0.1-1
- Autogenerated by Bloom

