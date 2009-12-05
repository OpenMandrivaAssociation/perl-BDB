%define upstream_name    BDB
%define upstream_version 1.86

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Asynchronous Berkeley DB access
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/BDB
Source0:    http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: db4.7-devel
BuildRequires: perl(common::sense)
BuildRequires: perl-devel
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
This is the Asynchronous Berkeley DB access API for Perl and DB 4.6.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

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
