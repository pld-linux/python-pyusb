%define	module	pyusb
Summary:	PyUSB provides USB access on the Python language
Summary(pl.UTF-8):	PyUSB - dostęp do USB z poziomu języka Python
Name:		python-%{module}
Version:	0.4.1
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/pyusb/%{module}-%{version}.tar.gz
# Source0-md5:	9576c3e471e40e021fa44f36712bbd04
URL:		http://pyusb.sourceforge.net/
BuildRequires:	libusb-devel
BuildRequires:	python-devel
BuildRequires:	unzip
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyUSB provides USB access on the Python language.

%description -l pl.UTF-8
PyUSB daje dostęp do USB z poziomu języka Python.

%prep
%setup -q -n %{module}-%{version}

%build
python ./setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python ./setup.py install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{py_sitedir}/*.so
