#
# Conditional build:
%bcond_with	legacy	# enable the insecure legacy code (no avahi
			# dependency then)
%bcond_without	avahi	# disable avahi support
#
Summary:	mDNS Service Switch Module
Summary(pl.UTF-8):	Moduł NSS mDNS
Name:		nss_mdns
Version:	0.10
Release:	2
License:	LGPL v2.1
Group:		Base
Source0:	http://0pointer.de/lennart/projects/nss-mdns/nss-mdns-%{version}.tar.gz
# Source0-md5:	03938f17646efbb50aa70ba5f99f51d7
URL:		http://0pointer.de/lennart/projects/nss-mdns/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Requires(post):	/etc/nsswitch.conf
Requires(post): grep
Requires(post): sed
Requires(postun): sed
%{!?with_legacy:Requires:	avahi}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		/%{_lib}

%description
nss-mdns is a plugin for the GNU Name Service Switch (NSS)
functionality of the GNU C Library (glibc) providing host name
resolution via Multicast DNS (aka Zeroconf, aka Apple Rendezvous),
effectively allowing name resolution by common Unix/Linux programs in
the ad-hoc mDNS domain .local.

%description -l pl.UTF-8
nss-mdns to wtyczka dla funkcjonalności NSS (Name Service Switch) w
glibc dająca możliwość rozwiązywania nazw poprzez Multicast DNS (znany
także jako Zeroconf lub Apple Rendezvous), efektywnie umożliwiająca
rozwiązywanie nazw przez popularne programy uniksowe/linuksowe w
doraźnej domenie mDNS .local.

%prep
%setup -q -n nss-mdns-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--%{?with_legacy:en}%{!?with_legacy:dis}able-legacy \
	--%{?with_avahi:en}%{!?with_avahi:dis}able-avahi
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%post
if ! grep -q '^hosts:.*mdns' /etc/nsswitch.conf ; then
	%banner %{name} <<-EOF
	Adding Multicast-DNS resolver to /etc/nsswitch.conf
EOF
	sed -i -e's/^\(hosts:.*\)dns\(.*\)/\1mdns4_minimal [NOTFOUND=return] dns mdns4\2/' /etc/nsswitch.conf
fi

%postun
if [ "$1" = "0" ]; then
	sed -i -r -e's/mdns4(_minimal)?( \[NOTFOUND=return\])?( |$)//g' /etc/nsswitch.conf || :
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/{README.html,style.css}
%attr(755,root,root) %{_libdir}/libnss_mdns*.so.*
