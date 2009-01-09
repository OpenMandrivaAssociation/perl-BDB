%define realname   BDB
%define version    1.82
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Asynchronous Berkeley DB access
Source:     http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/BDB
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: db4.7-devel


%description
This is the Asynchronous Berkeley DB access API for Perl and DB 4.6.


%prep
%setup -q -n %{realname}-%{version} 

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

