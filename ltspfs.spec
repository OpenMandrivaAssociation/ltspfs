Summary: 	Tool used to mount local media on an Xterminal from the terminals serveur
Name:		ltspfs
Version:	0.5.14
Release:	%mkrel 1
License:	GPL
Group:		System/Servers
URL:		http://wiki.ltsp.org/twiki/bin/view/Ltsp/LtspFS
Source:		http://ftp.fr.debian.org/debian/pool/main/l/ltspfs/%{name}_%{version}.orig.tar.gz
BuildRequires:	fuse-devel fuse libx11-devel glib2-devel
Requires:	fuse
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%package -n ltspfsd
Group:          System/Servers
Summary:        LTSP file system, userspace FUSE module that runs on a server
Requires:      x11-tools
Requires:      x11-util-cf-files
Requires:      x11-util-cf-files-debug
Requires:      x11-util-macros
Requires:      x11-util-modular

%description
ltspfs is a remote filesystem consisting of two parts:
  1) A network server daemon that runs on the LTSP terminal.
  2) A FUSE module that runs in user-space on the server, that connects with
     the daemon on the client.

The goals of ltspfs are:

   1. Provide a lightweight file access mechanism that will be feasable on
      lower end hardware.
   2. Provide a stateless file access method that will feature "atomic" reads
      and writes to minimize impact from client network disruptions.
   3. Provide a network filesystem that handles client reboots and
      disconnections in a manner that doesn't leave inaccesible, unmountable
      filesystems on the LTSP server.
   4. Provide a network filesystem that can easily handle the oddities of
      dealing with removable media, and integrate well with udev (LTSP's
      preferred device handling support).

%description -n ltspfsd
Fuse based remote filesystem daemon for LTSP thin clients
 LtspFS is a remote filesystem consisting of two parts:
 1) A network server daemon that runs on the LTSP terminal.
 2) A FUSE module that runs in userspace on the server, that connects with
 the daemon on the client.
 This package contains the daemon to be run on the LTSP thin client.

%prep

%setup -q

%build
%configure
%make

%install
rm -rf %{buildroot}
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/run/devices/
%make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING ChangeLog
%{_bindir}/ltspfs
%attr(4755,root,root) %{_bindir}/lbmount
%{_sbindir}/ltspfsmounter
%{_mandir}/man1/ltspfs.1*
%{_mandir}/man1/lbmount.1*
%{_mandir}/man1/ltspfsmounter.1*

%files -n ltspfsd
%defattr(-,root,root,-)
%{_bindir}/ltspfsd
%{_sbindir}/cdpinger
%{_sbindir}/ltspfs_mount
%{_sbindir}/ltspfs_umount
%{_sysconfdir}/udev/rules.d/88-ltsp.rules
/lib/udev/ltspfs_entry
%{_datadir}/ldm/
%{_datadir}/ltsp/xinitrc.d/I05-set-ltspfs_token
%{_mandir}/man1/ltspfsd.1*
%{_mandir}/man1/cdpinger.1*
%{_mandir}/man1/ltspfs_mount.1*
%{_mandir}/man1/ltspfs_umount.1*
%dir %{_localstatedir}/run/devices/
