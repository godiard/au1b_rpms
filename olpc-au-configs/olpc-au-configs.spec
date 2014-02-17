Summary: Configs needed by the olpc-au image
Name:    olpc-au-configs
Version: 0.1
Release: 3
URL:     https://www.laptop.org.au/
License: LGPL
Group:   User Interface/Desktops
Source0: olpc-au-configs-0.1.tar

Requires: GConf2
Requires: sugar

BuildArch: noarch

%description

This package provide configs needed by the olpc-au image, like:
* GConf settings
* Font configs
* Network profiles
* Font license file
* Boot animation customs

%prep
%setup -q

%install
rm -rf %{buildroot}
mkdir %{buildroot}
cp -r %{_builddir}/%{name}-%{version}/* %{buildroot}

%files
%{_sysconfdir}/*
%{_datadir}/sugar/licenses/*
%{_datadir}/plymouth/themes/olpc/custom.png

%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
# Use microformat back end for updater
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
    --type string --set /desktop/sugar/update/backend microformat.MicroformatUpdater

# microformat updater url to use.
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
    --type string --set /desktop/sugar/update/microformat_update_url \
    http://wiki.laptop.org/go/Activities/OLPCAU/ARM-test-addons/13.2.0

# Enable microformat updater.
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
    --type int --set /desktop/sugar/update/auto_update_frequency 1

# Set max activities open
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
    --type int --set /desktop/sugar/maximum_number_of_open_activities 4

# preset GSM
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
    --type=string --set /desktop/sugar/network/gsm/country au
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
    --type=string --set /desktop/sugar/network/gsm/provider Telstra
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
    --type int --set /desktop/sugar/network/gsm/plan 2
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
    --type=string --set /desktop/sugar/network/gsm/apn telstra.internet

# Set Write default font
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
    -s --type string /desktop/sugar/activities/write/font_face Sans
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
    -s --type int /desktop/sugar/activities/write/font_size 20

# enable control panel network hidden network section
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
    -s --type boolean /desktop/sugar/extensions/network/conf_hidden_ssid true

# Sugar font (AU use abc123)
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
    --type string --set /desktop/sugar/font/default_face abc123

# Harvest statistics service configuration
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
    --type string -s /desktop/sugar/collaboration/harvest_api_key V9iIS8EBC7Aho2EDeeKCg7K9QB8Ue9K4
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
    --type string -s /desktop/sugar/collaboration/harvest_hostname https://harvest.one-education.org
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
    --type boolean -s /desktop/sugar/collaboration/harvest_editable false

# hide Register menu in Sugar
gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults \
    -s -t bool /desktop/sugar/show_register false

%changelog
* Mon Dec 30 2013 Gonzalo Odiard <gonzalo@laptop.org> 0.1-0
- 0.1 devel release
