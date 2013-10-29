Name:	dextrose-updater	
Version:	5
Release:	1%{?dist}
Summary:	A yum based updater for sugar-dextrose. Updates the sugar-dextrose related packages automatically and emits dbus messages (for the sugar notification system, if installed)

Group:		Applications/Updating
License:	GPLv3
URL:		http://wiki.sugarlabs.org/go/Dextrose/Updater
Source0:	http://download.sugarlabs.org/sources/external/%{name}/%{name}-%{version}.tar.gz	
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch:	noarch

#BuildRequires:	
#Requires:	
Packager: Anish Mangal <anish@sugarlabs.org>

%description

A yum based updater for sugar-dextrose. Updates the sugar-dextrose related packages automatically and emits dbus messages (for the sugar notification system, if installed)

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=%{buildroot} REPO="dextrose dextrose-freeworld" install

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_DIR/%{name}-%{version}

%files
%defattr(-,root,root,-)
%doc 

/usr/sbin/dextrose-updater
/etc/sysconfig/dextrose-updater
/etc/cron.hourly/dextrose-updater

%changelog
* Tue Feb 15 2011 Anish Mangal <anish@sugarlabs.org> 5-1
- Bump version, fix Source0, download url

* Tue Feb 15 2011 Anish Mangal <anish@sugarlabs.org> 4-1
- Interpret check-update exit status correctly (alsroot)
- Remove stampfile at the beginning; touch it only successful exit (alsroot)
- More conveninet installer; install cron task (alsroot)
- Keep all metadata in Makefile

* Mon Feb 14 2011 Anish Mangal <anish@sugarlabs.org> 3-1
- Do not re-create logfile on checking update (alsroot)

* Thu Feb  3 2011 Anish Mangal <anish@sugarlabs.org> 2-1
- Keep trying every hour until yum returns an exit code (alsroot)

* Wed Jan 19 2011 Aleksey Lim <alsroot@member.fsf.org> 1-8
- Check daily updates hourly.

* Mon Jan 10 2011 Anish Mangal <anish@sugarlabs.org> 1-6
- Remove dextrose-py and change path of config file from /etc/default to /etc/sysconfig.

* Mon Jan 03 2011 Anish Mangal <anish@sugarlabs.org> 1-5
- Add dextrose-py to the list of repos to update from.

* Wed Dec 22 2010 Anish Mangal <anish@sugarlabs.org> 1-4
- Remove post, postun sections and handle symlink in install and file sections.

* Wed Dec 22 2010 Anish Mangal <anish@sugarlabs.org> 1-3
- Remove cron job after removing

* Wed Dec 22 2010 Anish Mangal <anish@sugarlabs.org> 1-2
- Add cron job

* Wed Dec 22 2010 Anish Mangal <anish@sugarlabs.org> 1-1
- Initial rpm version
