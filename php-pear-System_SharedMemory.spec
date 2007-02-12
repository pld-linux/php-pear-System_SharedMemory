%include	/usr/lib/rpm/macros.php
%define		_class		System
%define		_subclass	SharedMemory
%define		_status		beta
%define		_pearname	System_SharedMemory

Summary:	%{_pearname} - common OO-style shared memory API
Summary(pl.UTF-8):   %{_pearname} - wspólny, obiektowy interfejs do API pamięci współdzielonej
Name:		php-pear-%{_pearname}
Version:	0.9.0RC1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	0969d02662f4a7a1b67e7819bfc3f852
URL:		http://pear.php.net/package/System_SharedMemory/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OO-style shared memory API for several shared memory engines.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Zorientowane obiektowo API pamięci współdzielonej dla różnych
silników.

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
%doc install.log docs/%{_pearname}/docs/README.TXT
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/System/SharedMemory/
%{php_pear_dir}/System/SharedMemory.php
