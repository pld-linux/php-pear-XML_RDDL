%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	RDDL
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - read RDDL (Resource Directory Description Language) documents
Summary(pl):	%{_pearname} - odczyt dokument�w RDDL (Resource Directory Description Language)
Name:		php-pear-%{_pearname}
Version:	0.9
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	2319f1b75a6bca6e55a15d78f8973f91
URL:		http://pear.php.net/package/XML_RDDL/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class provides an easy-to-use interface to extract RDDL resources
from XML documents. More on RDDL can be found at http://www.rddl.org/

This class has in PEAR status: %{_status}.

%description -l pl
Ta klasa dostarcza �atwego w u�yciu interfejstu do wydobywania danych
RDDL z dokument�w XML. Wi�cej informacji na temat RDDL mo�na znale�� pod
adresem http://www.rddl.org/

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/examples
%{php_pear_dir}/%{_class}/*.php