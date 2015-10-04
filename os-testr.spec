#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : os-testr
Version  : 0.4.2
Release  : 6
URL      : https://pypi.python.org/packages/source/o/os-testr/os-testr-0.4.2.tar.gz
Source0  : https://pypi.python.org/packages/source/o/os-testr/os-testr-0.4.2.tar.gz
Summary  : A testr wrapper to provide functionality for OpenStack projects
Group    : Development/Tools
License  : Apache-2.0
Requires: os-testr-bin
Requires: os-testr-python
BuildRequires : Babel-python
BuildRequires : Jinja2
BuildRequires : Pygments
BuildRequires : Sphinx-python
BuildRequires : coverage-python
BuildRequires : discover-python
BuildRequires : docutils-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : fixtures-python
BuildRequires : flake8-python
BuildRequires : hacking
BuildRequires : linecache2-python
BuildRequires : markupsafe-python
BuildRequires : mccabe-python
BuildRequires : mock-python
BuildRequires : mox3-python
BuildRequires : os-testr
BuildRequires : oslosphinx-python
BuildRequires : oslotest-python
BuildRequires : pbr
BuildRequires : pep8
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pyflakes-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-mimeparse-python
BuildRequires : python3-dev
BuildRequires : requests-python
BuildRequires : setuptools
BuildRequires : six-python
BuildRequires : testrepository
BuildRequires : testrepository-python
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : tox
BuildRequires : traceback2-python
BuildRequires : unittest2-python
BuildRequires : virtualenv

%description
===============================
os-testr
===============================
A testr wrapper to provide functionality for OpenStack projects

%package bin
Summary: bin components for the os-testr package.
Group: Binaries

%description bin
bin components for the os-testr package.


%package python
Summary: python components for the os-testr package.
Group: Default
Requires: Babel-python
Requires: testrepository-python
Requires: testtools-python

%description python
python components for the os-testr package.


%prep
%setup -q -n os-testr-0.4.2

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ostestr
/usr/bin/subunit-trace
/usr/bin/subunit2html

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
