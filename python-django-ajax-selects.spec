%define realname django-ajax-selects
%define name    python-%{realname}
%define version 1.0
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        jQuery-powered auto-complete fields for ForeignKey and ManyToMany fields
Group:          Development/Python
License:        BSD
URL:            http://code.google.com/p/django-ajax-selects/
Source:         %{realname}-svnr24.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch
BuildRequires:  python-devel python-setuptools
Requires:       python-django

%description
jQuery-powered auto-complete fields for ForeignKey and ManyToMany fields

%prep
%setup -q -n %{realname}-svnr24

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT/usr/templates

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{py_puresitedir}
