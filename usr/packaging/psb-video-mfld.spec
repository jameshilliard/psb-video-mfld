%define drimoduledir  /usr/lib/dri
%define debug_package %{nil}

Name:           psb-video-mfld
Version:        20120625.1.40cca8
Release:        1
License:        Intel Free Distribution Binary License 
Source0:        psb-video-mfld-%{version}.tar.gz
Source2:        license.txt 
Group:          Development/Libraries
Summary:        User space video driver for mdfld
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  %{ix86}
Requires:   	pvr-bin-mdfld
AutoReqProv:    no  

%description
User space driver for video decode on mdfld

%prep
%setup -q -c -n %{name}-%{version}

%build

%install

mkdir -p $RPM_BUILD_ROOT%{drimoduledir}
cp -arv  %{name}-%{version}/usr/* %{buildroot}/usr
install -m 644 -D %{SOURCE2} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/license.txt

pushd $RPM_BUILD_ROOT%{drimoduledir}
ln -s pvr_drv_video.so psb_drv_video.so
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_docdir}/%{name}-%{version}/license.txt
%{drimoduledir}/psb_drv_video.so
%{drimoduledir}/pvr_drv_video.so
