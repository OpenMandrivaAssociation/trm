%define name    trm
%define version 0.2.1
%define release %mkrel 7

%define longtitle Application that generates Relatable TRM acoustic fingerprints

Summary:        %longtitle
Name:           %name
Version:        %version
Release:        %release
License:        GPL
Group:          Sound
URL:            http://www.musicbrainz.org/products/trmgen/download.html
Source0:        %name-%version.tar.bz2
Patch: trm-0.2.1-gcc4.patch
BuildRoot:      %_tmppath/%name-buildroot
Buildrequires: libmusicbrainz-devel 
Buildrequires: libvorbis-devel
Buildrequires: id3lib-devel
Buildrequires: libmad-devel

%description
The trm program will decode the first 30 seconds of audio file and
then spit out a TRM id (see http://www.relatable.com for details) on
stdout. If some error occurs, the error message is printed to stderr.

%prep

%setup -q
%patch -p1

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT/usr
mkdir $RPM_BUILD_ROOT/usr/bin
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS README
%_bindir/*


