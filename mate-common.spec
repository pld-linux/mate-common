Summary:	Common scripts and macros for MATE desktop development
Summary(pl.UTF-8):	Skrypty i makra do rozwijania środowiska graficznego MATE
Name:		mate-common
Version:	1.5.0
Release:	1
License:	GPL v3+
Group:		Development/Tools
Source0:	http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz
# Source0-md5:	0a361d7dd40248674d39a92a9d050153
URL:		http://wiki.mate-desktop.org/mate-common
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.9
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains some common scripts and macros for development
with MATE desktop.

MATE is a fork of GNOME 2. It provides an intuitive and attractive
desktop to Linux users using traditional metaphors.

%description -l pl.UTF-8
Ten pakiet zawiera parę wspólnych skryptów i makr do rozwijania
oprogramowania związanego ze środowiskiem graficznym MATE.

MATE to odgałęzienie GNOME 2. Zapewnia intuicyjne i atrakcyjne
środowisko graficzne dla użytkowników Linuksa przy użyciu tradycyjnych
metafor.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/mate-autogen
%attr(755,root,root) %{_bindir}/mate-doc-common
%{_datadir}/mate-common
%{_aclocaldir}/mate-common.m4
%{_aclocaldir}/mate-compiler-flags.m4
%{_mandir}/man1/mate-autogen.1*
%{_mandir}/man1/mate-doc-common.1*