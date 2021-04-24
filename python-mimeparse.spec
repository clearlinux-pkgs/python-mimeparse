#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-mimeparse
Version  : 1.6.0
Release  : 55
URL      : http://pypi.debian.net/python-mimeparse/python-mimeparse-1.6.0.tar.gz
Source0  : http://pypi.debian.net/python-mimeparse/python-mimeparse-1.6.0.tar.gz
Summary  : A module provides basic functions for parsing mime-type names and matching them against a list of media-ranges.
Group    : Development/Tools
License  : MIT
Requires: python-mimeparse-license = %{version}-%{release}
Requires: python-mimeparse-python = %{version}-%{release}
Requires: python-mimeparse-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
================

%package license
Summary: license components for the python-mimeparse package.
Group: Default

%description license
license components for the python-mimeparse package.


%package python
Summary: python components for the python-mimeparse package.
Group: Default
Requires: python-mimeparse-python3 = %{version}-%{release}

%description python
python components for the python-mimeparse package.


%package python3
Summary: python3 components for the python-mimeparse package.
Group: Default
Requires: python3-core
Provides: pypi(python_mimeparse)

%description python3
python3 components for the python-mimeparse package.


%prep
%setup -q -n python-mimeparse-1.6.0
cd %{_builddir}/python-mimeparse-1.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603402150
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python mimeparse_test.py
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-mimeparse
cp %{_builddir}/python-mimeparse-1.6.0/LICENSE %{buildroot}/usr/share/package-licenses/python-mimeparse/2807f3f1c4cb33b214defc4c7ab72f7e4e70a305
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-mimeparse/2807f3f1c4cb33b214defc4c7ab72f7e4e70a305

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
