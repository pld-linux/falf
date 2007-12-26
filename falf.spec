#
# TODO:
# - prepare patch to Makefile (install)

Summary:	Lightweight music player with multiplaylists for KDE
Summary(pl.UTF-8):	Lekki odtwarzacz muzyki z wieloma listami odtwarzania dla KDE
Name:		falf
Version:	1.0
Release:	0.5
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	d80056c9d7f91ce377eb5fd01043b700
URL:		http://falf.sf.net/
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	qmake >= 3.3.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	taglib-devel
BuildRequires:	xine-lib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FALF Player is based on foobar2000 music player for KDE.

Highlights:
- multiplaylist support
- lyrics support
- m3u support
- last.fm support
- HTTP streams support (radio)
- built-in tags' editor
- built-in equalizer
- easy transfer of tracks to removable device
- high stability
- low memory consumption

%description -l pl.UTF-8
FALF Player jest wzorowany na foobar2000 odtwarzaczem muzyki dla KDE.

Atuty:
- wsparcie dla wielu list odtwarzania
- wsparcie dla tekstow piosenek
- wsparcie dla plikow m3u
- wsparcie dla last.fm
- wsparcie dla strumieni HTTP (radio)
- wbudowany edytor tagow
- wbudowany korektor
- latwe przenoszenie danych do odtwarzaczy przenosnych
- wysoka stabilnosc
- niskie zuzycie pamieci

%prep
%setup -q

%build
export QTDIR=/usr
qmake
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_iconsdir}/hicolor,%{_desktopdir},%{_datadir}/apps/konqueror/servicemenus}

install bin/falf $RPM_BUILD_ROOT%{_bindir}

for i in pl it es nl zh_CN cs ru uk ;
do
	install -d $RPM_BUILD_ROOT%{_datadir}/locale/$i/LC_MESSAGES
	msgfmt po/$i/falf.po -o $RPM_BUILD_ROOT%{_datadir}/locale/$i/LC_MESSAGES/falf.mo
done

cp -Rf icons/* $RPM_BUILD_ROOT%{_iconsdir}/hicolor
install applnk/falf.desktop $RPM_BUILD_ROOT%{_desktopdir}
install applnk/falf_mnu.desktop $RPM_BUILD_ROOT%{_datadir}/apps/konqueror/servicemenus

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/falf
%{_datadir}/apps/konqueror/servicemenus/falf_mnu.desktop
%{_desktopdir}/falf.desktop
%{_iconsdir}/*/*/*/*.png
