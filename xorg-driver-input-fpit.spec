Summary:	X.org input driver for Fujitsu Stylistic Tablet PCs
Summary(pl):	Sterownik wej¶ciowy X.org dla komputerów Fujitsu Stylistic Tablet
Name:		xorg-driver-input-fpit
Version:	1.0.0.2
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC2/driver/xf86-input-fpit-%{version}.tar.bz2
# Source0-md5:	379c0c9116607e8b18c5005cf509572a
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-inputproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.1
BuildRequires:	xorg-xserver-server-devel >= 0.99.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org input driver for Fujitsu Stylistic Tablet PCs. This driver
supports the touchscreen of the Stylistic LT and (with special
options) of the Stylistic 500, 1000 and 2300.


%description -l pl
Sterownik wej¶ciowy X.org dla komputerów Fujitsu Stylistic Tablet. Ten
sterownik obs³uguje ekrany dotykowe Stylistic LT i (ze specjalnymi
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
	DESTDIR=$RPM_BUILD_ROOT \
	drivermandir=%{_mandir}/man4

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/xorg/modules/input/fpit_drv.so
%{_mandir}/man4/fpit.4x*
