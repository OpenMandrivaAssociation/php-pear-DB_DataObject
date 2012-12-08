%define		_class		DB
%define		_subclass	DataObject
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.9.5
Release:	%mkrel 3
Summary:	An SQL builder, object interface to database tables
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/DB_DataObject/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The core class is designed to be extended for each of your tables so
that you put the data logic inside the data classes. Included is a
Generator to make your configuration files and your base classes.
DataObject performs 2 tasks:
- Builds SQL statements based on the objects vars and the builder
  methods,
- acts as a datastore for a table row.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests
rm -rf %{buildroot}%{_bindir}/DB

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/example.ini
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.9.5-2mdv2011.0
+ Revision: 667492
- mass rebuild

* Sat Aug 14 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.9.5-1mdv2011.0
+ Revision: 569594
- update to new version 1.9.5

* Mon Jan 25 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.9.3-1mdv2010.1
+ Revision: 495838
- update to new version 1.9.3

* Wed Jan 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.9.0-1mdv2010.1
+ Revision: 486960
- update to new version 1.9.0

* Wed Dec 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.8.12-2mdv2010.1
+ Revision: 479288
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Sep 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.8.12-1mdv2010.0
+ Revision: 446476
- update to new version 1.8.12

* Sun Jul 26 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.8.11-1mdv2010.0
+ Revision: 400319
- update to new version 1.8.11

* Sun Mar 22 2009 Funda Wang <fwang@mandriva.org> 1.8.10-1mdv2009.1
+ Revision: 360148
- update to new version 1.8.10

* Thu Mar 19 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.8.9-1mdv2009.1
+ Revision: 357907
- update to new version 1.8.9

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 1.8.8-2mdv2009.1
+ Revision: 321806
- rebuild

* Sat Aug 16 2008 Oden Eriksson <oeriksson@mandriva.com> 1.8.8-1mdv2009.0
+ Revision: 272583
- 1.8.8

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.8.7-2mdv2009.0
+ Revision: 224719
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Nov 09 2007 Adam Williamson <awilliamson@mandriva.org> 1.8.7-1mdv2008.1
+ Revision: 107089
- new release 1.8.7


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.7.15-5mdv2007.0
+ Revision: 81082
- Import php-pear-DB_DataObject

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.7.15-5mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.7.15-4mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.7.15-3mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.7.15-2mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.7.15-1mdk
- 1.7.15

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.7.13-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.7.13-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.7.13-1mdk
- initial Mandriva package (PLD import)

