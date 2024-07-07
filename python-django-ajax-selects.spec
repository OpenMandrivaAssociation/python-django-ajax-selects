%define realname django-ajax-selects

Name:           python-%{realname}
Version:        3.0.2
Release:        1
Summary:        JQuery-powered auto-complete fields for ForeignKey and ManyToMany fields

Group:          Development/Python
License:        MIT and GPLv3
URL:            https://pypi.python.org/pypi/django-ajax-selects
Source:         https://pypi.python.org/packages/source/d/django_ajax_selects/django_ajax_selects-%{version}.tar.gz
BuildArch:      noarch
Requires:       python-django
BuildSystem:	python

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
%autosetup -p1 -n django_ajax_selects-%{version}

%install -a
rm -rf %{buildroot}/usr/templates

%files
%doc  ajax_select/LICENSE.txt 
%{py_puresitedir}/ajax_select
%{py_puresitedir}/django_ajax_selects-%{version}*.*-info
