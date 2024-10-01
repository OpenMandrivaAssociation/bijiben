%define url_ver	%(echo %{version}|cut -d. -f1,2)
%define _disable_rebuild_configure 1

Summary:	Simple Note Viewer
Name:		bijiben
Version:	40.1
Release:	11
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		https://www.gnome.org
Source0:	https://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
# Upstream patch to fix compilation with meson 0.60+
Patch0:   https://gitlab.gnome.org/GNOME/gnome-notes/-/commit/994af76ce5144062d55d141129bf6bf5fab002ee.patch
Patch02:        https://src.fedoraproject.org/rpms/bijiben/blob/rawhide/f/webkitdep.patch

BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	yelp-tools
BuildRequires:	pkgconfig(clutter-gtk-1.0)
BuildRequires:	pkgconfig(goa-1.0)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(tinysparql-3.0)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(webkit2gtk-4.1)
BuildRequires:	pkgconfig(libecal-2.0)
BuildRequires:	pkgconfig(libedataserver-1.2)
BuildRequires:	pkgconfig(libedataserverui-1.2)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:	libxml2-utils
BuildRequires:	meson

Provides: gnome-notes

%description
Simple note editor which emphasis on visuals : quickly write
notes, quickly find it back.

%prep
%setup -q
%autopatch -p1

%build
%meson -Dupdate_mimedb=false
%meson_build

%install
%meson_install

#we don't want these
find %{buildroot} -name "*.la" -delete
find %{buildroot} -name "*.a" -delete

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc NEWS AUTHORS COPYING README.md
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.Notes.desktop
%{_datadir}/%{name}
%{_datadir}/dbus-1/services/org.gnome.Notes.SearchProvider.service
#{_datadir}/glib-2.0/schemas/org.gnome.bijiben.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.Notes.gschema.xml
%{_datadir}/gnome-shell/search-providers/org.gnome.Notes-search-provider.ini
%{_iconsdir}/*/*/*/org.gnome.Notes*.*
%{_libexecdir}/%{name}-shell-search-provider
%{_datadir}/metainfo/org.gnome.Notes.appdata.xml
%{_datadir}/mime/packages/org.gnome.Notes.xml
