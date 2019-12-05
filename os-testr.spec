#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEB6CCA1483FA74EC (infra-root@openstack.org)
#
Name     : os-testr
Version  : 1.0.0
Release  : 31
URL      : http://tarballs.openstack.org/os-testr/os-testr-1.0.0.tar.gz
Source0  : http://tarballs.openstack.org/os-testr/os-testr-1.0.0.tar.gz
Source99 : http://tarballs.openstack.org/os-testr/os-testr-1.0.0.tar.gz.asc
Summary  : A testr wrapper to provide functionality for OpenStack projects
Group    : Development/Tools
License  : Apache-2.0
Requires: os-testr-bin
Requires: os-testr-python3
Requires: os-testr-license
Requires: os-testr-python
Requires: pbr
Requires: python-subunit
Requires: stestr
Requires: testtools
BuildRequires : buildreq-distutils3
BuildRequires : pbr

%description
os-testr
        ========

%package bin
Summary: bin components for the os-testr package.
Group: Binaries
Requires: os-testr-license

%description bin
bin components for the os-testr package.


%package license
Summary: license components for the os-testr package.
Group: Default

%description license
license components for the os-testr package.


%package python
Summary: python components for the os-testr package.
Group: Default
Requires: os-testr-python3

%description python
python components for the os-testr package.


%package python3
Summary: python3 components for the os-testr package.
Group: Default
Requires: python3-core

%description python3
python3 components for the os-testr package.


%prep
%setup -q -n os-testr-1.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533789343
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/os-testr
cp LICENSE %{buildroot}/usr/share/doc/os-testr/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/generate-subunit
/usr/bin/ostestr
/usr/bin/subunit-trace
/usr/bin/subunit2html

%files license
%defattr(-,root,root,-)
/usr/share/doc/os-testr/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
