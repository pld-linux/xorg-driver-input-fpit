Summary:	X.org input driver for Fujitsu Stylistic Tablet PCs
Summary(pl.UTF-8):   Sterownik wejściowy X.org dla komputerów Fujitsu Stylistic Tablet
Name:		xorg-driver-input-fpit
Version:	1.1.0
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-fpit-%{version}.tar.bz2
# Source0-md5:	a31066a2076d18619ceaea67f6d89698
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-inputproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
Requires:	xorg-xserver-server >= 1.0.99.901
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org input driver for Fujitsu Stylistic Tablet PCs. This driver
supports the touchscreen of the Stylistic LT and (with special
options) of the Stylistic 500, 1000 and 2300.

%description -l pl.UTF-8
Sterownik wejściowy X.org dla komputerów Fujitsu Stylistic Tablet. Ten
sterownik obsługuje ekrany dotykowe Stylistic LT i (ze specjalnymi
opcjami) Stylistic 500, 1000 i 2300.

%prep
%setup -q -n xf86-input-fpit-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog readme.txt
%attr(755,root,root) %{_libdir}/xorg/modules/input/fpit_drv.so
%{_mandir}/man4/fpit.4*