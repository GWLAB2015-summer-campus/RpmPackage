Name: gridwiz
###install script input

Summary: gridwiz rpm

Version: 1.0.0
###install script input

License: GPL

Release: 1
###install script input

Group: Testing
Source: %{name}-%{version}.tar.gz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
gridwiz rpm package

%prep

%setup -q

%build

#configure
#make%{?_smp_mflags}

%install
sudo rm -rf $RPM_BUILD_ROOT
#make install DESTDIR=$RPM_BULLID_ROOT
sudo mkdir -p $RPM_BUILD_ROOT/usr/local/bin
sudo mkdir -p $RPM_BUILD_ROOT/usr/local/gridwiz
sudo mkdir -p $RPM_BUILD_ROOT/usr/local/gridwiz/bin
sudo mkdir -p $RPM_BUILD_ROOT/usr/local/gridwiz/config


sudo cp gridwiz $RPM_BUILD_ROOT/usr/local/gridwiz/bin
sudo cp config $RPM_BUILD_ROOT/usr/local/bin
sudo cp config.txt $RPM_BUILD_ROOT/usr/local/gridwiz/config


%clean
sudo rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
#%doc
%attr(0755,root,root)/usr/local/bin/config
%attr(0755,root,root) /usr/local/gridwiz/config/config.txt
%attr(0755,root,root)/usr/local/gridwiz/bin/gridwiz

%postun

%changelog
* Wed Aug 3 2016 <ghjf1278@naver.com>
- initial RPM

