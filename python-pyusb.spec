%define	module	pyusb
Summary:	PyUSB provides USB access on the Python language
Summary(pl):	PyUSB - dostêp do USB z poziomu jêzyka Python
Name:		python-%{module}
Version:	0.1
Release:	1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/pyusb/%{module}-%{version}-src.tar.gz
# Source0-md5:	b86333284659f15986206413df61123e
URL:		http://pyusb.sourceforge.net/
BuildRequires:	libusb-devel
BuildRequires:	python-devel
BuildRequires:	unzip
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyUSB provides USB access on the Python language.

%description -l pl
PyUSB daje dostêp do USB z poziomu jêzyka Python.

%prep
%setup  -q -n %{module}

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
