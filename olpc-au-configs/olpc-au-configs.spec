Summary: Configs needed by the olpc-au image
Name:    olpc-au-configs
Version: 0.102
Release: 2
URL:     https://www.laptop.org.au/
License: LGPL
Group:   User Interface/Desktops
Source0: olpc-au-configs-0.102.tar

Requires: GConf2
Requires: sugar >= 0.101

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
%{_datadir}/glib-2.0/schemas/sugar.gschema.override

%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
# Use microformat back end for updater
#gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
#    --type string --set /desktop/sugar/update/backend microformat.MicroformatUpdater

# microformat updater url to use.
#gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
#    --type string --set /desktop/sugar/update/microformat_update_url \
#    http://wiki.laptop.org/go/Activities/OLPCAU/ARM-test-addons/13.2.0

# Enable microformat updater.
#gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
#    --type int --set /desktop/sugar/update/auto_update_frequency 1

# Set max activities open
#gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
#    --type int --set /desktop/sugar/maximum_number_of_open_activities 4

# preset GSM
#gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
#    --type=string --set /desktop/sugar/network/gsm/country au
#gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
#    --type=string --set /desktop/sugar/network/gsm/provider Telstra
#gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
#    --type int --set /desktop/sugar/network/gsm/plan 2
#gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
#    --type=string --set /desktop/sugar/network/gsm/apn telstra.internet

# Set Write default font
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
    -s --type string /desktop/sugar/activities/write/font_face Sans
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
    -s --type int /desktop/sugar/activities/write/font_size 20

# enable control panel network hidden network section
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
    -s --type boolean /desktop/sugar/extensions/network/conf_hidden_ssid true

# Sugar font (AU use abc123)
#gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
#    --type string --set /desktop/sugar/font/default_face abc123

# Harvest statistics service configuration
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
    --type string -s /desktop/sugar/collaboration/harvest_api_key V9iIS8EBC7Aho2EDeeKCg7K9QB8Ue9K4
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
    --type string -s /desktop/sugar/collaboration/harvest_hostname https://harvest.one-education.org
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
    --type boolean -s /desktop/sugar/collaboration/harvest_editable false

# Training server configuration
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
    --type string -s /desktop/sugar/services/training/url https://training.one-education.org/training/report
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
    --type string -s /desktop/sugar/services/training/api_key SbCeK4nH8dpQJsHNn9djza9g

# Support server configuration
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
    --type=string -s /desktop/sugar/services/zendesk/url https://oneedu.zendesk.com
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
    --type=string -s /desktop/sugar/services/zendesk/token "eG8tc3VwcG9ydEBsYXB0b3Aub3JnLmF1L3Rva2VuOlZTaWM4TThZbjZBRTJkMWxYNkFGbFhkZzUxSjlJSHFUQ01DYzNjOHY="
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
    --type list --list-type string -s /desktop/sugar/services/zendesk/fields '[21891880,21729904,21729914,21808844]'

# hide Register menu in Sugar
#gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults \
#    -s -t bool /desktop/sugar/show_register false

glib-compile-schemas %{_datadir}/glib-2.0/schemas

%postun
glib-compile-schemas %{_datadir}/glib-2.0/schemas

%changelog
* Tue Apr 08 2014 Martin Abente Lahaye <tch@sugarlabs.org> 0.102-2
- set gsettings missing values

* Thu Mar 13 2014 Martin Abente Lahaye <tch@sugarlabs.org> 0.1-6
- add role id

* Fri Mar 07 2014 Martin Abente Lahaye <tch@sugarlabs.org> 0.1-5
- add support server configs

* Mon Feb 17 2014 Martin Abente Lahaye <tch@sugarlabs.org> 0.1-4
- add boot animation customs
- add training server configs

* Mon Dec 30 2013 Gonzalo Odiard <gonzalo@laptop.org> 0.1-0
- 0.1 devel release
