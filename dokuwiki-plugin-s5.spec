%define		subver	2016-02-03
%define		ver		%(echo %{subver} | tr -d -)
%define		plugin		s5
%define		php_min_version 5.3.0
Summary:	S5 Slideshow Plugin
Name:		dokuwiki-plugin-%{plugin}
Version:	%{ver}
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	https://github.com/splitbrain/dokuwiki-plugin-s5/archive/%{subver}/%{plugin}-%{subver}.tar.gz
# Source0-md5:	97cb941d3e53cbccada7005dc7fde6d1
URL:		https://www.dokuwiki.org/plugin:s5
BuildRequires:	rpmbuild(macros) >= 1.553
Requires:	php(core) >= %{php_min_version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}
%define		find_lang 	%{_usrlibrpm}/dokuwiki-find-lang.sh %{buildroot}

%description
S5 is a slide show format based entirely on XHTML, CSS, and
JavaScript. With one file, you can run a complete slide show and have
a printer-friendly version as well.

This plugin can create S5 slide show presentations from any DokuWiki
page.

%prep
%setup -qc
mv *-%{plugin}-*/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
rm $RPM_BUILD_ROOT%{plugindir}/README

%find_lang %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
# force css cache refresh
if [ -f %{dokuconf}/local.php ]; then
	touch %{dokuconf}/local.php
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%dir %{plugindir}
%{plugindir}/*.gif
%{plugindir}/*.php
%{plugindir}/*.txt
%{plugindir}/conf
%{plugindir}/ui
