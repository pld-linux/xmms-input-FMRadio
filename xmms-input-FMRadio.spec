Summary:	FM Radio plugin for XMMS
Summary(pl.UTF-8):	Wtyczka wejściowa dla XMMS-a sterująca radiem FM
Name:		xmms-input-FMRadio
Version:	1.5
Release:	5
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://silicone.free.fr/xmms-FMRadio/xmms-FMRadio-%{version}.tgz
# Source0-md5:	5a5cc64ca149ee03ff039d200c723b18
URL:		http://silicone.free.fr/xmms-FMRadio/
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel >= 1.2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FM Radio plugin for XMMS.

%description -l pl.UTF-8
Wtyczka wejściowa dla XMMS-a sterująca radiem FM.

%prep
%setup -q -n xmms-FMRadio-%{version}

%build
%{__make} \
	COMMON_CFLAGS="%{rpmcflags} -ffast-math `glib-config --cflags`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{xmms_input_plugindir}

install libradio.so $RPM_BUILD_ROOT%{xmms_input_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{xmms_input_plugindir}/*.so
