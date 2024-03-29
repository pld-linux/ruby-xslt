Summary:	Ruby xslt bindings
Summary(pl.UTF-8):	Dowiązania xslt dla ruby'ego
Name:		ruby-xslt
Version:	0.9.3
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://gregoire.lejeune.free.fr/%{name}_%{version}.tar.gz
# Source0-md5:	f69bf3a70bedbd44f7dee25df20546fd
URL:		http://greg.rubyfr.net/pub/packages/ruby-xslt/
BuildRequires:	libgcrypt-devel >= 1.2.4
BuildRequires:	libgpg-error-devel >= 1.4-2
BuildRequires:	libxml2-devel >= 2.6.27
BuildRequires:	libxslt-devel >= 1.1.19
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
BuildRequires:	zlib-devel >= 1.2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby-xslt is a simple XSLT class based on libxml (xmlsoft.org) and
libxslt (xmlsoft.org/XSLT).

%description -l pl.UTF-8
Prosta klasa transformacji XSL oparta na libxml (xmlsoft.org) oraz
libxslt (xmlsoft.org/XSLT).

%prep
%setup -q -n %{name}

%build
ruby extconf.rb
%{__make}
%{__make} doc

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{ruby_rubylibdir}/xml
cp -af lib/xslt.rb $RPM_BUILD_ROOT%{ruby_rubylibdir}/xml

install -d $RPM_BUILD_ROOT%{ruby_archdir}/xml
install xslt_lib.so $RPM_BUILD_ROOT%{ruby_archdir}/xml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%dir %{ruby_rubylibdir}/xml
%{ruby_rubylibdir}/xml/xslt.rb
%dir %{ruby_archdir}/xml
%attr(755,root,root) %{ruby_archdir}/xml/xslt_lib.so
