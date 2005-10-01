%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	RDDL
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - read RDDL (Resource Directory Description Language) documents
Summary(pl):	%{_pearname} - odczyt dokumentów RDDL (Resource Directory Description Language)
Name:		php-pear-%{_pearname}
Version:	0.9
Release:	2.1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	2319f1b75a6bca6e55a15d78f8973f91
URL:		http://pear.php.net/package/XML_RDDL/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class provides an easy-to-use interface to extract RDDL resources
from XML documents. More on RDDL can be found at http://www.rddl.org/

In PEAR status of this package is: %{_status}.

%description -l pl
Ta klasa dostarcza ³atwego w u¿yciu interfejsu do wydobywania danych
RDDL z dokumentów XML. Wiêcej informacji na temat RDDL mo¿na znale¼æ pod
adresem http://www.rddl.org/

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
