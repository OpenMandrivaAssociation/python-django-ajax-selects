%define module django-ajax-selects
%define oname django_ajax_selects

Name:           python-django-ajax-selects
Version:        3.0.3
Release:        2
Summary:        JQuery-powered auto-complete fields for ForeignKey and ManyToMany fields
Group:          Development/Python
License:        MIT AND GPL-3.0-only
URL:            https://pypi.python.org/pypi/django-ajax-selects
Source:         https://pypi.python.org/packages/source/d/%{oname}/%{oname}-%{version}.tar.gz
BuildSystem:	python
BuildArch:      noarch
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
Requires:       python%{pyver}dist(django)

%description
Enables editing of `ForeignKey`, `ManyToMany` and simple text fields using the
Autocomplete - `jQuery` plugin.

django-ajax-selects will work in any normal form as well as in the admin.

The user is presented with a text field. They type a search term or a few
letters of a name they are looking for, an ajax request is sent to the server,
a search channel returns possible results. Results are displayed as a drop down
menu. When an item is selected it is added to a display area just below the
text field.

%prep
%autosetup -p1 -n %{oname}-%{version}

%install -a
rm -rf %{buildroot}/usr/templates

%files
%doc README.md
%license  LICENSE
%{python_sitelib}/ajax_select
%{python_sitelib}/%{oname}-%{version}.dist-info
