#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define	module	pyusb
Summary:	PyUSB provides USB access on the Python language
Summary(pl.UTF-8):	PyUSB - dostęp do USB z poziomu języka Python
Name:		python-%{module}
# keep 1.1.x here for python2 support
Version:	1.1.0
Release:	3
License:	BSD
Group:		Development/Languages/Python
Source0:	https://downloads.sourceforge.net/pyusb/%{module}-%{version}.tar.gz
# Source0-md5:	3b2e38e9f697d2f90d86376bd10a9505
URL:		https://pyusb.github.io/pyusb/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-setuptools >= 1:30.3.0
BuildRequires:	python-setuptools_scm
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-setuptools >= 1:30.3.0
BuildRequires:	python3-setuptools_scm
%endif
Requires:	python-libs >= 1:2.5
Requires:	libusb >= 1.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyUSB provides USB access on the Python language.

%description -l pl.UTF-8
PyUSB daje dostęp do USB z poziomu języka Python.

%package -n python3-%{module}
Summary:	PyUSB provides USB access on the Python language
Summary(pl.UTF-8):	PyUSB - dostęp do USB z poziomu języka Python
Group:		Development/Languages/Python
Requires:	python3-libs >= 1:3.2
Requires:	libusb >= 1.0.0

%description -n python3-%{module}
PyUSB provides USB access on the Python language.

%description -n python3-%{module} -l pl.UTF-8
PyUSB daje dostęp do USB z poziomu języka Python.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc ACKNOWLEDGEMENTS LICENSE README.rst docs/*.rst
%{py_sitescriptdir}/usb
%{py_sitescriptdir}/pyusb-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc ACKNOWLEDGEMENTS LICENSE README.rst docs/*.rst
%{py3_sitescriptdir}/usb
%{py3_sitescriptdir}/pyusb-%{version}-py*.egg-info
%endif
