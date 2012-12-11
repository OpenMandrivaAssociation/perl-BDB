%define upstream_name    BDB
%define upstream_version 1.9

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	1

Summary:    Asynchronous Berkeley DB access
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/BDB
Source0:    http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: db-devel
BuildRequires: perl(common::sense)
BuildRequires: perl-devel

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

Requires: perl(common::sense)

%description
This is the Asynchronous Berkeley DB access API for Perl and DB 4.6.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes META.yml
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Mon May 14 2012 Crispin Boylan <crisb@mandriva.org> 1.900.0-1
+ Revision: 798858
- New release

* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.880.0-4
+ Revision: 768358
- mass rebuild of perl extensions against perl 5.14.2

* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.880.0-3
+ Revision: 680656
- mass rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.880.0-2mdv2011.0
+ Revision: 555682
- rebuild

* Wed Mar 31 2010 Jérôme Quelin <jquelin@mandriva.org> 1.880.0-1mdv2010.1
+ Revision: 530258
- update to 1.88

* Wed Feb 10 2010 Jérôme Quelin <jquelin@mandriva.org> 1.870.0-4mdv2010.1
+ Revision: 503943
- adding missing requires:

* Sat Jan 30 2010 Funda Wang <fwang@mandriva.org> 1.870.0-3mdv2010.1
+ Revision: 498573
- build with db4.8

* Wed Dec 30 2009 Jérôme Quelin <jquelin@mandriva.org> 1.870.0-2mdv2010.1
+ Revision: 483975
- rebuild

* Wed Dec 23 2009 Jérôme Quelin <jquelin@mandriva.org> 1.870.0-1mdv2010.1
+ Revision: 481706
- update to 1.87

* Sat Dec 05 2009 Jérôme Quelin <jquelin@mandriva.org> 1.860.0-1mdv2010.1
+ Revision: 473712
- update to 1.86

* Thu Nov 12 2009 Jérôme Quelin <jquelin@mandriva.org> 1.850.0-1mdv2010.1
+ Revision: 465165
- update to 1.85

* Tue Aug 11 2009 Jérôme Quelin <jquelin@mandriva.org> 1.840.0-1mdv2010.0
+ Revision: 415032
- adding missing buildrequires:
- update to 1.84

* Fri Jan 16 2009 Götz Waschk <waschk@mandriva.org> 1.83-1mdv2009.1
+ Revision: 330120
- update to new version 1.83

* Fri Jan 09 2009 Götz Waschk <waschk@mandriva.org> 1.82-1mdv2009.1
+ Revision: 327380
- update to new version 1.82

* Sun Nov 30 2008 Götz Waschk <waschk@mandriva.org> 1.81-1mdv2009.1
+ Revision: 308455
- new version
- fix source URL
- build with libdb 4.7

* Thu Aug 14 2008 Götz Waschk <waschk@mandriva.org> 1.71-1mdv2009.0
+ Revision: 271732
- new version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.5-2mdv2009.0
+ Revision: 268371
- rebuild early 2009.0 package (before pixel changes)

* Tue Jun 10 2008 Götz Waschk <waschk@mandriva.org> 1.5-1mdv2009.0
+ Revision: 217355
- new version

* Mon Jan 14 2008 Thierry Vignaud <tv@mandriva.org> 1.4-2mdv2008.1
+ Revision: 151846
- rebuild

* Wed Dec 19 2007 Götz Waschk <waschk@mandriva.org> 1.4-1mdv2008.1
+ Revision: 133736
- import perl-BDB

