Summary:	FM Radio plugin for xmms
Summary(pl):	Wtyczka sterowania radiem FM dla xmms
Name:		xmms-input-FMRadio
Version:	1.5
Release:	3
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://silicone.free.fr/xmms-FMRadio/xmms-FMRadio-%{version}.tgz
URL:		http://silicone.free.fr/xmms-FMRadio/
BuildRequires:	xmms-devel >= 1.2.3
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
FM Radio plugin for xmms.

%description -l pl
Wtyczka sterowania radiem FM dla xmms.

%prep
%setup -q -n xmms-FMRadio-%{version}

%build
%{__make} \
        COMMON_CFLAGS="%{rpmcflags} -ffast-math `glib-config --cflags`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/`%{_bindir}/xmms-config --input-plugin-dir`/

install libradio.so \
        $RPM_BUILD_ROOT/`%{_bindir}/xmms-config --input-plugin-dir`/libradio.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/xmms/*/*.so
