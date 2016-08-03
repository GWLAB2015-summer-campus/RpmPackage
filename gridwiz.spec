Name: gridwiz
Summary: gridwiz rpm
Version: 1.0.0
License: GPL
Release: 1%{?dist}
Group: Testing
Source: %{name}-%{version}.tar.gz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: /bin/rm, /bin/mkdir, /bin/cp, /bin/sh
Requires: /bin/bash, /bin/sh


%description
gridwiz rpm package

%prep

%setup -q

%build

#configure
#make%{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
#make install DESTDIR=$RPM_BULLID_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/gridwiz
mkdir -p $RPM_BUILD_ROOT/usr/local/gridwiz/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/gridwiz/config

cp setup2 $RPM_BUILD_ROOT/usr/local/bin
cp config.txt $RPM_BUILD_ROOT/usr/local/gridwiz/config


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
#%doc
%attr(0755,root,root)/usr/local/bin/setup2
%attr(0755,root,root) /usr/local/gridwiz/config/config.txt

%postun
rm -rf /usr/local/bin/setup2
rm -rf /usr/local/gridwiz

%changelog
* Wed Aug 3 2016 <ghjf1278@naver.com>
- initial RPM

