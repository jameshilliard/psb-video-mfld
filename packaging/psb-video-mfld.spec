%define drimoduledir  /usr/lib/dri
%define configfiledir  /etc
%define debug_package %{nil}

Name:           psb-video-mfld
Version:        20130111.1.b96918
Release:        1
License:        Intel Free Distribution Binary License 
Source0:        psb-video-mfld-%{version}.tar.gz
Source2:        license.txt 
Source1001:     packaging/psb-video-mfld.manifest 
Group:          Development/Libraries
Summary:        User space video driver for mdfld
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  %{ix86}
Requires:   	pvr-bin-mdfld
AutoReqProv:    no  

%description
User space driver for video decode on mdfld

%prep
%setup -q -n %{name}-%{version}

%build
cp %{SOURCE1001} .

%install

mkdir -p %{buildroot}/%{drimoduledir}
mkdir -p %{buildroot}/%{configfiledir}
cp -arv  usr/lib/dri/* %{buildroot}/%{drimoduledir}
cp -arv  etc/psbvideo.conf %{buildroot}/%{configfiledir}
install -m 644 -D %{SOURCE2} %{buildroot}/%{_docdir}/%{name}-%{version}/license.txt

pushd $RPM_BUILD_ROOT%{drimoduledir}
ln -s pvr_drv_video.so psb_drv_video.so
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%manifest psb-video-mfld.manifest
%defattr(-,root,root,-)
%{_docdir}/%{name}-%{version}/license.txt
%{drimoduledir}/psb_drv_video.so
%{drimoduledir}/pvr_drv_video.so
%{configfiledir}/psbvideo.conf
