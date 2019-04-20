#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-mimeparse
Version  : 1.6.0
Release  : 43
URL      : http://pypi.debian.net/python-mimeparse/python-mimeparse-1.6.0.tar.gz
Source0  : http://pypi.debian.net/python-mimeparse/python-mimeparse-1.6.0.tar.gz
Summary  : A module provides basic functions for parsing mime-type names and matching them against a list of media-ranges.
Group    : Development/Tools
License  : MIT
Requires: python-mimeparse-python3
Requires: python-mimeparse-python
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : setuptools

%description
================

%package python
Summary: python components for the python-mimeparse package.
Group: Default
Requires: python-mimeparse-python3

%description python
python components for the python-mimeparse package.


%package python3
Summary: python3 components for the python-mimeparse package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-mimeparse package.


%prep
%setup -q -n python-mimeparse-1.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523299551
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python mimeparse_test.py
%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
