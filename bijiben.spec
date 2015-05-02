%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	Simple Note Viewer
Name:		bijiben
Version:	3.17.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://www.gnome.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
Patch1:		bijiben-string-literal.patch

BuildRequires:	intltool
BuildRequires:	pkgconfig(clutter-gtk-1.0)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(tracker-sparql-1.0)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(webkitgtk-3.0)
BuildRequires:	pkgconfig(libecal-1.2)
BuildRequires:	pkgconfig(libedataserver-1.2)
BuildRequires:	pkgconfig(libedataserverui-1.2)

%description
Simple note editor which emphasis on visuals : quickly write
notes, quickly find it back.

%prep
%setup -q
%apply_patches

%build
%configure \
	--disable-schemas-compile

%make

%install
%makeinstall_std

#we don't want these
find %{buildroot} -name "*.la" -delete
find %{buildroot} -name "*.a" -delete

# fix error
cp -r %{buildroot}/%{buildroot}/%{_datadir}/%{name}/Default.css %{buildroot}/%{_datadir}/%{name}/
rm -rf %{buildroot}/%{buildroot}/%{_datadir}/%{name}/Default.css
rm -f %{buildroot}/usr/doc/%{name}/*

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc NEWS AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/dbus-1/services/org.gnome.Bijiben.SearchProvider.service
%{_datadir}/glib-2.0/schemas/org.gnome.bijiben.gschema.xml
%{_datadir}/gnome-shell/search-providers/bijiben-search-provider.ini
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}.svg
%{_libdir}/%{name}/libgd.so
%{_libexecdir}/%{name}-shell-search-provider

