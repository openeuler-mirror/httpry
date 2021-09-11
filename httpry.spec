Summary:             A specialized packet sniffer designed for displaying and logging HTTP traffic
Name:                httpry
Version:             0.1.8
Release:             1
License:             GPLv2 and BSD
URL:                 http://dumpsterventures.com/jason/httpry/
Source:              http://dumpsterventures.com/jason/httpry/httpry-%{version}.tar.gz
BuildRequires:       gcc libpcap-devel make
%description
httpry is a specialized packet sniffer designed for displaying and logging
HTTP traffic. It is not intended to perform analysis itself, but to capture,
parse, and log the traffic for later analysis. It can be run in real-time
displaying the traffic as it is parsed, or as a daemon process that logs to
an output file. It is written to be as lightweight and flexible as possible,
so that it can be easily adaptable to different applications.

%prep
%setup -q

%build
sed -i 's/^CCFLAGS.*$/CCFLAGS = \$(RPM_OPT_FLAGS) \$(RPM_LD_FLAGS) -I\/usr\/include\/pcap -I\/usr\/local\/include\/pcap/' Makefile
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p ${RPM_BUILD_ROOT}%{_sbindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
install -Dp -m 0755 httpry ${RPM_BUILD_ROOT}%{_sbindir}/httpry
install -Dp -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc doc/ChangeLog doc/COPYING doc/format-string doc/method-string doc/perl-tools doc/README
%{_sbindir}/httpry
%{_mandir}/man1/httpry.1*

%changelog
* Mon Sep 6 2021 wulei <wulei80@huawei.com> - 0.1.8-1
- package init
