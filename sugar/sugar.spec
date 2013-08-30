%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Summary: Constructionist learning platform
Name:    sugar
Version: 0.99.2.git20130816
Release: 2.olpcau
URL:     http://sugarlabs.org/
License: GPLv2+
Group:   User Interface/Desktops
Source0: sugar-0.99.2.git20130816.tar
Patch0:  sugar-gnomekeyring.patch
Patch1:  0001-add-age-and-gender-to-intro-and-aboutme-section-of-c.patch
Patch2:  0001-add-dbus-method-to-update-favorites.patch
Patch3:  0001-Backup-and-Restore-to-a-mounted-device.patch
Patch4:  0002-Add-proxy-configuration-support-to-Network-Control-P.patch
Patch5:  0003-Control-Panel-Add-aoption-to-launch-the-network-mana.patch
Patch6:  0004-Add-model-information-in-the-about-computer-control-.patch
Patch7:  0005-Add-School-Fonts-license-in-control-panel.patch
Patch8:  0006-Add-last-updated-information-in-the-control-Panel.patch
Patch9:  0001-Add-5-GHz-frequency-channels-table-SL-4459.patch
Patch10: 0001-WPA-enterprise-feature.patch

BuildRequires: gettext
BuildRequires: GConf2-devel
BuildRequires: gobject-introspection
BuildRequires: gtk3-devel
BuildRequires: gtksourceview3-devel
BuildRequires: intltool
BuildRequires: perl-XML-Parser
BuildRequires: pkgconfig
BuildRequires: python

Requires: dbus-x11
Requires: ethtool
Requires: gnome-keyring-pam
Requires: gstreamer-plugins-espeak
Requires: gtksourceview3
Requires: gvfs
Requires: gwebsockets
Requires: libwnck3
Requires: metacity
Requires: NetworkManager
Requires: openssh
Requires: python-telepathy
Requires: sugar-artwork
Requires: sugar-toolkit-gtk3
Requires: telepathy-mission-control
Requires: upower
Requires: xdg-user-dirs
Requires: libxklavier

BuildArch: noarch

%description
Sugar provides simple yet powerful means of engaging young children in the 
world of learning that is opened up by computers and the Internet. With Sugar,
even the youngest learner will quickly become proficient in using the 
computer as a tool to engage in authentic problem-solving.  Sugar promotes 
sharing, collaborative learning, and reflection, developing skills that help 
them in all aspects of life. 

Sugar is also the learning environment for the One Laptop Per Child project. 
See http://www.laptop.org for more information on this project.

%package cp-all
Summary: All control panel modules 
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Requires: %{name}-cp-background %{name}-cp-datetime %{name}-cp-frame %{name}-cp-language
Requires: %{name}-cp-modemconfiguration %{name}-cp-network %{name}-cp-power %{name}-cp-keyboard
Requires: %{name}-cp-webaccount %{name}-cp-updater

%description cp-all
This is a meta package to install all Sugar Control Panel modules

%package cp-background
Summary: Sugar Background control panel
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}

%description cp-background
This is the Sugar control panel to change the background

%package cp-datetime
Summary: Sugar Date and Time control panel
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}

%description cp-datetime
This is the Sugar Date and Time settings control panel

%package cp-frame
Summary: Sugar Frame control panel
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}

%description cp-frame
This is the Sugar Frame settings control panel

%package cp-keyboard
Summary: Sugar Keyboard control panel
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}

%description cp-keyboard
This is the Sugar Keyboard settings control panel

%package cp-language
Summary: Sugar Language control panel
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}

%description cp-language
This is the Sugar Language settings control panel

%package cp-modemconfiguration
Summary: Sugar Modem configuration control panel
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}

%description cp-modemconfiguration
This is the Sugar Modem configuration control panel

%package cp-network
Summary: Sugar Network control panel
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}

%description cp-network
This is the Sugar Network settings control panel

%package cp-power
Summary: Sugar Power control panel
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}

%description cp-power
This is the Sugar Power settings control panel

%package cp-updater
Summary: Sugar Activity Update control panel
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}

%description cp-updater
This is the Sugar Activity Updates control panel

%package cp-webaccount
Summary: Sugar Web Account control panel
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}

%description cp-webaccount
This is the Sugar Web Account control panel


%prep
%setup -q
%patch0 -p1 -b .keyring

%patch1 -p1 -b .age_page
%patch2 -p1 -b .add_dbus_method
%patch3 -p1 -b .backup
%patch4 -p1 -b .proxy_support
%patch5 -p1 -b .add_nmce_launcher
%patch6 -p1 -b .model_info
%patch7 -p1 -b .schools_fonts_info
%patch8 -p1 -b .last_updated_info
%patch9 -p1 -b .add_5ghz
%patch10 -p1 -b .wpa

%build
# need run it again to include new files
./autogen.sh
%configure
make

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=%{buildroot}
mkdir %{buildroot}/%{_datadir}/sugar/activities
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

%find_lang %{name}

%post
if (update-mime-database -v &> /dev/null); then
  update-mime-database "%{_datadir}/mime" > /dev/null
fi

export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
	%{_sysconfdir}/gconf/schemas/sugar.schemas > /dev/null || :

%pre
if [ "$1" -gt 1 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
      %{_sysconfdir}/gconf/schemas/sugar.schemas > /dev/null || :
fi

%preun
if [ "$1" -eq 0 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
      %{_sysconfdir}/gconf/schemas/sugar.schemas > /dev/null || :
fi

%postun
if (update-mime-database -v &> /dev/null); then
  update-mime-database "%{_datadir}/mime" > /dev/null
fi

%files -f %{name}.lang
%doc COPYING

%config %{_sysconfdir}/dbus-1/system.d/nm-user-settings.conf
%config %{_sysconfdir}/gconf/schemas/sugar.schemas

%dir %{_datadir}/sugar
%dir %{_datadir}/sugar/activities
%{_datadir}/sugar/*

%{python_sitelib}/*

%{_datadir}/xsessions/sugar.desktop
%{_datadir}/icons/hicolor/scalable/apps/sugar-xo.svg

%{_bindir}/*
%exclude %{_bindir}/sugar-emulator
%config(noreplace) %{_datadir}/sugar/data/activities.defaults
%dir %{_datadir}/sugar/extensions/cpsection/
%exclude %{_datadir}/sugar/extensions/cpsection/[b-z]*
%{_datadir}/sugar/extensions/cpsection/aboutcomputer
%{_datadir}/sugar/extensions/cpsection/aboutme

%{_datadir}/mime/packages/sugar.xml

%files cp-all

%files cp-background
%{_datadir}/sugar/extensions/cpsection/background

%files cp-datetime
%{_datadir}/sugar/extensions/cpsection/datetime

%files cp-frame
%{_datadir}/sugar/extensions/cpsection/frame

%files cp-keyboard
%{_datadir}/sugar/extensions/cpsection/keyboard

%files cp-language
%{_datadir}/sugar/extensions/cpsection/language

%files cp-modemconfiguration
%{_datadir}/sugar/extensions/cpsection/modemconfiguration

%files cp-network
%{_datadir}/sugar/extensions/cpsection/network

%files cp-power
%{_datadir}/sugar/extensions/cpsection/power

%files cp-updater
%{_datadir}/sugar/extensions/cpsection/updater

%files cp-webaccount
%{_datadir}/sugar/extensions/cpsection/webaccount

%changelog
* Sat Aug 10 2013 Daniel Drake <dsd@laptop.org> 0.99.1-3
- Add dependency on libxklavier, used via gobject-introspection

* Mon Aug  5 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.99.1-2
- Add dependency on gwebsockets for webservices

* Wed Jul 31 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.99.1-1
- 0.99.1 devel release

* Thu Jul 11 2013 Daniel Drake <dsd@laptop.org> 0.99.0-2
- Remove dependencies not required by Sugar shell

* Fri Jun 28 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.99.0-1
- 0.99.0 devel release
- Trim changelog

* Sun May 26 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.8-2
- Update default control panels

* Fri May 24 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.8-1
- Sugar 0.98.8 stable release

* Fri Apr 12 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.7-1
- Sugar 0.98.7 stable release

* Fri Mar 22 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.6-1
- Sugar 0.98.6 stable release

* Fri Mar  8 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.5-1
- Sugar 0.98.5 stable release

* Sat Feb 16 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.4-1
- Sugar 0.98.4 stable release

* Fri Dec 21 2012 Simon Schampijer <simon@laptop.org> - 0.98.3-1
- Sugar 0.98.3 stable release

* Tue Dec 18 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.2-1
- Sugar 0.98.2 stable release

* Mon Dec 10 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.1-1
- Sugar 0.98.1 stable release

* Thu Nov 29 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.0-1
- Sugar 0.98.0 stable release

* Tue Nov 27 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.13-1
- 0.97.13 devel release

* Sat Nov 24 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.12-1
- 0.97.12 devel release 

* Sat Nov 10 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.11-1
- 0.97.11 devel release

* Wed Nov  7 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.10-1
- 0.97.10 devel release

* Thu Oct 25 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.9-1
- 0.97.9 devel release

* Tue Oct 16 2012 Daniel Drake <dsd@laptop.org> 0.97.8-1
- 0.97.8 devel release

* Thu Oct 11 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.7-1
- 0.97.7 devel release

* Fri Oct  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.6-1
- 0.97.6 devel release

* Thu Oct  4 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.97.5-2
- Split out Control Panels to sub packages
- Update gnome-keyring patch. RHBZ 862581
- Add patch to update build dependencies

* Thu Sep 27 2012 Daniel Drake <dsd@laptop.org> - 0.97.5-1
- New development release

* Thu Sep 20 2012 Daniel Drake <dsd@laptop.org> - 0.97.4-1
- New development release

* Thu Sep 13 2012 Daniel Drake <dsd@laptop.org> - 0.97.3-1
- New development release

* Tue Aug 28 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.97.2-1
- 0.97.2 devel release

* Tue Aug 21 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.97.1-1
- 0.97.1 devel release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.3-1
- 0.96.3 stable release

* Tue Jun  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.2-1
- 0.96.2 stable release

* Sat May  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.1-2
- Add patch to create gnome keyring if it doesn't exist

* Mon Apr 30 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.1-1
- 0.96.1 stable release

* Tue Apr 24 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.0-1
- 0.96.0 stable release

* Thu Apr 19 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.7-1
- devel release 0.95.7

* Mon Mar 26 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.6-1
- devel release 0.95.6

* Wed Mar 14 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.5-1
- devel release 0.95.5

* Tue Mar  6 2012 Daniel Drake <dsd@laptop.org> - 0.95.4-2
- Add dependency on sugar-toolkit-gtk3 (needed to launch activities)

* Thu Feb  2 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.4-1
- devel release 0.95.4

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jan  2 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.3-3
- Drop premature sugar-base obsoletion

* Thu Dec 22 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.3-2
- Obsolete sugar-base

* Wed Dec 21 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.3-1
- devel release 0.95.3

* Wed Nov 16 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.2-1
- devel release 0.95.2

* Tue Oct 25 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.1-1
- devel release 0.95.1
