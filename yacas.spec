%define major 0
%define libname %mklibname %{name} %{major}


Name:    yacas
Summary: A computer algebra language
Version: 1.9.1
Release: 1
Source0: https://github.com/grzegorzmazur/yacas/archive/v%{version}/%{name}-%{version}.tar.gz
Group: Development/Other
URL: http://yacas.sourceforge.net/
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: gsl-devel
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5WebEngine)
BuildRequires: pkgconfig(Qt5WebEngineWidgets)
License: GPLv2

%description
Yacas (Yet Another Computer Algebra System) is a small and highly
flexible computer algebra language. The syntax uses a infix-operator
grammar parser. The distribution contains a small library of
mathematical functions, but its real strength is in the language in
which you can easily write your own symbolic manipulation algorithms.
It supports arbitrary precision arithmetic.

%prep
%autosetup -p1

%build
%cmake

%make_build

%install
%make_install -C build

%files 
%defattr(-,root,root,0755)
%doc docs/*
%{_datadir}/yacas
%{_bindir}/*



%changelog
* Fri Mar 02 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.3.2-1
+ Revision: 781756
- version update 1.3.2

* Sun May 24 2009 Jérôme Brenier <incubusss@mandriva.org> 1.2.2-5mdv2010.0
+ Revision: 379337
- fix str fmt (1 patch)
- fix build with gcc 4.3 (1 patch)
- fix license (GPLv2)

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Dec 14 2007 Thierry Vignaud <tv@mandriva.org> 1.2.2-1mdv2008.1
+ Revision: 119981
- new release
- running make -k is just asking for problems
- new URL
- buildrequires gsl-devel
- use %%mkrel
- import yacas

