%define		plugin		s5
Summary:	S5 Slideshow Plugin
Name:		dokuwiki-plugin-%{plugin}
Version:	20070120
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://wiki.splitbrain.org/_media/plugin:s5-plugin-2007-01-20.tgz
# Source0-md5:	967ae23990aea7a2350e555fdb514940
Source1:	dokuwiki-find-lang.sh
URL:		http://wiki.splitbrain.org/plugin:s5
Requires:	dokuwiki >= 20061106
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
S5 is a slide show format based entirely on XHTML, CSS, and JavaScript. With
one file, you can run a complete slide show and have a printer-friendly version
as well. 

This plugin can create S5 slide show presentations from any DokuWiki page. 

%prep
%setup -q -n %{plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
rm -f %{name}.lang
cp -a . $RPM_BUILD_ROOT%{plugindir}
rm -f $RPM_BUILD_ROOT%{plugindir}/{COPYING,README,VERSION}

# find locales
sh %{SOURCE1} %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%dir %{plugindir}
%{plugindir}/*.gif
%{plugindir}/*.php
%{plugindir}/*.txt
%{plugindir}/conf
%{plugindir}/ui
