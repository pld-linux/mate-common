Summary:	Common scripts and macros for MATE desktop development
Summary(pl.UTF-8):	Skrypty i makra do rozwijania środowiska graficznego MATE
Name:		mate-common
Version:	1.20.0
Release:	1
License:	GPL v3+
Group:		Development/Tools
Source0:	http://pub.mate-desktop.org/releases/1.20/%{name}-%{version}.tar.xz
# Source0-md5:	b92cae6bf3d82c9e5e4f501021d4fba6
URL:		http://wiki.mate-desktop.org/mate-common
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.9
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	autoconf >= 2.54
Requires:	automake >= 1:1.9
Requires:	gettext-tools >= 0.10.40
Requires:	glib2-devel >= 1:2.2.0
Requires:	gtk-doc >= 1.0
Requires:	intltool >= 0.25
Requires:	libtool >= 1:1.4.3
Requires:	pkgconfig >= 1:0.14.0
BuildArch:	noarch
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
%{_aclocaldir}/mate-code-coverage.m4
%{_aclocaldir}/mate-common.m4
%{_aclocaldir}/mate-compiler-flags.m4
%{_mandir}/man1/mate-autogen.1*
%{_mandir}/man1/mate-doc-common.1*
