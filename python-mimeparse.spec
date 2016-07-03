#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-mimeparse
Version  : 1.5.2
Release  : 18
URL      : http://pypi.debian.net/python-mimeparse/python-mimeparse-1.5.2.tar.gz
Source0  : http://pypi.debian.net/python-mimeparse/python-mimeparse-1.5.2.tar.gz
Summary  : A module provides basic functions for parsing mime-type names and matching them against a list of media-ranges.
Group    : Development/Tools
License  : MIT
Requires: python-mimeparse-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
# Travis CI Build Status [![Build Status](https://travis-ci.org/dbtsai/python-mimeparse.svg?branch=master)](https://travis-ci.org/dbtsai/python-mimeparse)

%package python
Summary: python components for the python-mimeparse package.
Group: Default

%description python
python components for the python-mimeparse package.


%prep
%setup -q -n python-mimeparse-1.5.2

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python mimeparse_test.py
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
