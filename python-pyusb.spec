%define	module	pyusb
Summary:	PyUSB provides USB access on the Python language
Summary(pl.UTF-8):	PyUSB - dostęp do USB z poziomu języka Python
Name:		python-%{module}
Version:	0.4.2
Release:	2
License:	BSD
Group:		Development/Languages/Python
Source0:	http://downloads.sourceforge.net/pyusb/%{module}-%{version}.tar.gz
# Source0-md5:	5667a00af1ac0d5062103b4512e227f8
URL:		http://pyusb.sourceforge.net/
BuildRequires:	libusb-compat-devel
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyUSB provides USB access on the Python language.

%description -l pl.UTF-8
PyUSB daje dostęp do USB z poziomu języka Python.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/*.egg*
