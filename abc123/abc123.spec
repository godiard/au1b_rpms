%define name abc123

# nowdays most (all?) distributions seems to use this. Oh the joys of the FHS
%define ttmkfdir /usr/bin/ttmkfdir

%define fontdir /usr/share/fonts/%{name}

Source0: abc123-Bold.ttf
Source1: abc123-Regular.ttf

Summary: Abc123 fonts
Name: %{name}
Version: 1.0
Release: 1.olpcau
License: These fonts are licensed for use as part of the One Laptop per Child project, for other uses, contact http://www.schoolfonts.com.au
Group: User Interface/X
BuildArch: noarch
BuildRoot: /var/tmp/%{name}-root
BuildRequires: %{ttmkfdir}
Packager: Gonzalo Odiard <gonzalo@laptop.org>

%description
SchoolFonts fonts

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{fontdir}
cp %{SOURCE0} $RPM_BUILD_ROOT/%{fontdir}
cp %{SOURCE1} $RPM_BUILD_ROOT/%{fontdir}

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/sbin/chkfontpath -a $1 -eq 1 ]; then
	/usr/sbin/chkfontpath --add %{fontdir}
fi
# something has probably changed, update the font-config cache
if [ -x /usr/bin/fc-cache ]; then
	/usr/bin/fc-cache
fi

%preun
if [ -x /usr/sbin/chkfontpath -a $1 -eq 0 ]; then
	/usr/sbin/chkfontpath --remove %{fontdir}
fi

%files
%attr(-,root,root) %{fontdir}
%dir %{fontdir}

%changelog
