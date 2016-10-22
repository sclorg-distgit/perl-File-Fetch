%{?scl:%scl_package perl-File-Fetch}

Name:           %{?scl_prefix}perl-File-Fetch
Version:        0.52
Release:        1%{?dist}
Summary:        Generic file fetching mechanism
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/File-Fetch/
Source0:        http://www.cpan.org/authors/id/B/BI/BINGOS/File-Fetch-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(strict)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Cwd)
BuildRequires:  %{?scl_prefix}perl(File::Basename)
BuildRequires:  %{?scl_prefix}perl(File::Copy)
BuildRequires:  %{?scl_prefix}perl(File::Path)
BuildRequires:  %{?scl_prefix}perl(File::Spec) >= 0.82
BuildRequires:  %{?scl_prefix}perl(File::Spec::Unix)
BuildRequires:  %{?scl_prefix}perl(File::Temp)
BuildRequires:  %{?scl_prefix}perl(FileHandle)
BuildRequires:  %{?scl_prefix}perl(IPC::Cmd) >= 0.42
BuildRequires:  %{?scl_prefix}perl(Locale::Maketext::Simple)
BuildRequires:  %{?scl_prefix}perl(Module::Load::Conditional) >= 0.66
BuildRequires:  %{?scl_prefix}perl(Params::Check) >= 0.07
BuildRequires:  %{?scl_prefix}perl(vars)
# Keep all downaloaders optional (LWP, curl, rsync etc.).
# Tests:
BuildRequires:  %{?scl_prefix}perl(Data::Dumper)
BuildRequires:  %{?scl_prefix}perl(IO::Socket::INET)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(Test::More)
BuildRequires:  %{?scl_prefix}perl(warnings)
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(File::Spec) >= 0.82
Requires:       %{?scl_prefix}perl(IPC::Cmd) >= 0.42
Requires:       %{?scl_prefix}perl(Locale::Maketext::Simple)
Requires:       %{?scl_prefix}perl(Module::Load::Conditional) >= 0.66
Requires:       %{?scl_prefix}perl(Params::Check) >= 0.07

# Remove under-specified dependencies
%if 0%{?rhel} < 7
# RPM 4.8 style
%{?filter_setup:
%filter_from_requires /^%{?scl_prefix}perl(File::Spec)$/d
%filter_from_requires /^%{?scl_prefix}perl(IPC::Cmd)$/d
%filter_from_requires /^%{?scl_prefix}perl(Module::Load::Conditional)$/d
%filter_from_requires /^%{?scl_prefix}perl(Params::Check)$/d
%?perl_default_filter
}
%else
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^%{?scl_prefix}perl\\((File::Spec|IPC::Cmd|Module::Load::Conditional|Params::Check)\\)$
%endif

%description
File::Fetch allows you to fetch any file pointed to by a "ftp", "http",
"file", "git", or "rsync" URI by a number of different means.

%prep
%setup -q -n File-Fetch-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=$RPM_BUILD_ROOT%{?scl:'}
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Aug 22 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.52-1
- 0.52 bump

* Tue Aug 02 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.48-367
- Avoid loading optional modules from default . (CVE-2016-1238)

* Mon Jul 11 2016 Petr Pisar <ppisar@redhat.com> - 0.48-366
- SCL

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.48-365
- Increase release to favour standalone package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.48-347
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.48-346
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.48-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.48-311
- Perl 5.22 rebuild

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.48-310
- Increase release to favour standalone package

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.48-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.48-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 27 2014 Petr Pisar <ppisar@redhat.com> - 0.48-1
- 0.48 bump

* Thu Nov 28 2013 Petr Pisar <ppisar@redhat.com> - 0.46-1
- 0.46 bump

* Tue Oct 01 2013 Petr Pisar <ppisar@redhat.com> - 0.44-1
- 0.44 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 0.42-2
- Perl 5.18 rebuild

* Mon Apr 15 2013 Petr Pisar <ppisar@redhat.com> - 0.42-1
- 0.42 bump

* Fri Mar 15 2013 Petr Pisar <ppisar@redhat.com> 0.38-1
- Specfile autogenerated by cpanspec 1.78.
