Summary:	X.org input driver for Fujitsu Stylistic Tablet PCs
Summary(pl.UTF-8):	Sterownik wejściowy X.org dla komputerów Fujitsu Stylistic Tablet
Name:		xorg-driver-input-fpit
Version:	1.4.0
Release:	7
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-fpit-%{version}.tar.bz2
# Source0-md5:	042c95fec145d8b57ca62714131ff3f1
Patch0:		am.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-inputproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-util-util-macros >= 1.12
BuildRequires:	xorg-xserver-server-devel >= 1.10.0
BuildRequires:  rpmbuild(macros) >= 1.389
%{?requires_xorg_xserver_xinput}
Requires:	xorg-xserver-server >= 1.10.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org input driver for Fujitsu Stylistic Tablet PCs. This driver
supports the touchscreen of the Stylistic LT and (with special
options) of the Stylistic 500, 1000, 1200, 2300 and 3400. Modern
FinePoint MP800 devices will also work with this driver.

%description -l pl.UTF-8
Sterownik wejściowy X.org dla komputerów Fujitsu Stylistic Tablet. Ten
sterownik obsługuje ekrany dotykowe Stylistic LT i (ze specjalnymi
opcjami) Stylistic 500, 1000, 1200, 2300 i 3400. Nowe urządzenia
FinePoint MP800 także będą działać z tym sterownikiem.

%prep
%setup -q -n xf86-input-fpit-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README readme.txt
%attr(755,root,root) %{_libdir}/xorg/modules/input/fpit_drv.so
%{_datadir}/X11/xorg.conf.d/50-fpit.conf
%{_mandir}/man4/fpit.4*
