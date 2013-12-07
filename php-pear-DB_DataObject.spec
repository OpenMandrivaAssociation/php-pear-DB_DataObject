%define	_class		DB
%define	_subclass	DataObject
%define	modname	%{_class}_%{_subclass}

Summary:	An SQL builder, object interface to database tables
Name:		php-pear-%{modname}
Version:	1.11.2
Release:	5
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/DB_DataObject/
Source0:	http://download.pear.php.net/package/DB_DataObject-%{version}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear

%description
The core class is designed to be extended for each of your tables so
that you put the data logic inside the data classes. Included is a
Generator to make your configuration files and your base classes.
DataObject performs 2 tasks:
- Builds SQL statements based on the objects vars and the builder
  methods,
- acts as a datastore for a table row.

%prep
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests
rm -rf %{buildroot}%{_bindir}/DB

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%doc %{modname}-%{version}/docs/example.ini
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{modname}.xml

