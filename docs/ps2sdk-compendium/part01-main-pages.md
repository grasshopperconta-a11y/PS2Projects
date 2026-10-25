# Part 1 — Main Pages

## PS2SDK - PS2DEV Open Source Project

Page: <https://ps2dev.github.io/ps2sdk/index.html>

CI CI-Docker
PS2SDK Documentation
Copyright 2001-2004, ps2dev - http://www.ps2dev.org All rights reserved.
#### **ATTENTION**
If you are confused on how to start developing for PS2, see the getting started section on the ps2dev main page.
#### Introduction
PS2SDK is a collection of Open Source libraries used for developing applications on Sony's PlayStation 2® (PS2). PS2SDK contains the work from a number of PS2 projects, which are now buildable in a single source tree. Review the history section for how ps2sdk came about.
At the time of writing, PS2SDK includes the following libraries and features, allowing:
- Access to PS2 internal OS functions.
- Access to PS2 control pad and multitap.
- Access to PS2 memory card.
- Access to USB mouse and keyboard.
- TCP/IP stack & DNS resolution compatible with PS2 Ethernet Adapter.
- Full PS2 compatible Hard Disk Drive file system.
- Access to CD and DVD.
- Required implementation by newlib, for fulfilling libc functionality.
- Access to sound library on all PS2 using freesd.
- HTTP client file system.
- Network File System to load files from HOST pc.
#### Standard Libraries
In a continuous effort to make PS2SDK and the whole PS2DEV a POSIX environment; there are some libraries needed to be included inside of the standard libraries, which means, libraries than by default are included in any compilation program. From PS2SDK we have:
- lkernel: Contains the calls to BIOS functions
- lcglue: Implements most of the required methods by newlib
- lcdvd: Implements ps2time function indirectly required by newlib
If you wanna compile a program without using the standard libraries take a look at the compiler flags (-nodefaultlibs, -nolibc and -nostdlib).
#### License
PS2SDK has been developed by a large number of individuals who have provided their time and effort. The AUTHORS file includes this list.
PS2SDK is licensed under the Academic Free License version 2.0. This is a very liberal license and allows both commercial and non-commercial usage of the SDK. Please read the LICENSE file for full details.
#### Binary Installation
ps2sdk provides a large number of the basic software libraries required to access the underlying PS2 system. As the PS2 has two independent CPUs - the Emotion Engine (EE) and the IO Processor (IOP), the source tree is split into two different major areas representing the functions available on each processor.
A binary release of PS2SDK will include the following directories:
- sdk/ee/include: EE include files.
- sdk/ee/lib: EE library files.
- sdk/ee/startup: Example crt0.o and linkfile.
- sdk/iop/include: IOP include files.
- sdk/iop/irx: IOP loadable modules.
- sdk/common/include: Common include files between EE and IOP.
- sdk/samples: Samples for both EE and IOP.
- sdk/tools: Tools used during development on host PC.
#### Source Installation
ps2sdk source tree is considerably different from the binary or release distribution. You should only use the binary release when using ps2sdk in your projects.
The source tree is built as a collection of separate projects; each with its Makefile. The file Defs.make provides the basic definitions required when building PS2SDK. The two main variables required are PS2SDKSRC, which points to the source base directory, and PS2SDK, which points to the release directory.
The main make file has three targets:
- all/default: compile each of the projects in the tree.
- clean: clean the tree of files created during the build.
- release: release the binaries to the target PS2SDK directory.
Each subproject has a tree structure which can include:
- src: source code
- include: include files that are exported
- samples: samples of using a project. Can include multiple directories
- doc: documentation files to be exported.
- test: Unit Testing or other testing code.
- obj: created during the build to store object files
- lib: created during the build to store library files
- bin: created during the build to store binary files
Please review the Makefiles to see how to create your subproject in the tree.
#### History
ps2sdk brings together several open-source projects developed for the Playstation 2®. These projects include ps2lib, ps2drv, libhdd, ps2ip and ps2hid. These projects are now all closed and have been migrated to ps2sdk.
ps2lib was the first library to be released. Created by Gustavo Scotti, the library was released in October 2001. Over the years a number of people have contributed to providing the base functionality required to access the internals of the PS2. ps2lib has gone through a number of versions and was last released as Version 2.1 in October 2003.
ps2drv was started by Marcus R. Brown to provide an area to look at more of the internals of the IO Processor and related hardware. It was started in June 2003 and over the last year (2004) has grown considerably. ps2drv is where the irx imports method was created used in ps2sdk. ps2drv was last released as Version 1.1 in February 2004.
ps2ip was started by David Ryan (Oobles) in late 2002 to provide a TCP/IP stack for open source development. Over the last two years (2003-2004), the stack has improved and matured. boman666 provided the last big improvement to the design and his changes are used in PS2SDK.
libhdd was started by Nick Van Veen (Sjeep) in 2003 to provide a Hard Disk Drive driver and file system that is compatible with the commercial Sony HDD and other non-Sony HDDs. The work was sponsored by DMS3, and the resulting code was kindly provided back to the ps2dev community. The last release before ps2sdk was version 1.2 released in February 2004.
ps2hid was started by Tyranid in October 2003 to provide USB mouse and keyboard drivers compatible with the Sony USB Driver.
AUTHORS
#### Community
Links for discussion and chat are available here.

---

## Related Pages

Page: <https://ps2dev.github.io/ps2sdk/pages.html>

Here is a list of all related documentation pages:
- IOPRP image generator (md_ee_ioprpgen__r_e_a_d_m_e.html) |
- PS2SDK - KERNEL LIBRARY (md_ee_kernel__r_e_a_d_m_e.html) |
- libcglue (md_ee_libcglue__r_e_a_d_m_e.html) |
- remote (md_ee_rpc_remote_remote.html) |
- Security manager RPC client (md_ee_rpc_secr__r_e_a_d_m_e.html) |
- Arcade ATA/ATAPI driver (md_iop_arcade_acata__r_e_a_d_m_e.html) |
- Arcade atad driver (md_iop_arcade_acatad__r_e_a_d_m_e.html) |
- Arcade CD/DVD driver (md_iop_arcade_accdvd__r_e_a_d_m_e.html) |
- Arcade CD/DVD driver RPC (md_iop_arcade_accdvde__r_e_a_d_m_e.html) |
- Arcade Core (md_iop_arcade_accore__r_e_a_d_m_e.html) |
- Arcade Device (md_iop_arcade_acdev__r_e_a_d_m_e.html) |
- Arcade dev9 driver (md_iop_arcade_acdev9__r_e_a_d_m_e.html) |
- Arcade Flash Memory driver (md_iop_arcade_acflash__r_e_a_d_m_e.html) |
- Arcade FPGA Bitstream Loader (md_iop_arcade_acfpgald__r_e_a_d_m_e.html) |
- Arcade JV Interface (md_iop_arcade_acjv__r_e_a_d_m_e.html) |
- Arcade JV firmware loader (md_iop_arcade_acjvld__r_e_a_d_m_e.html) |
- Arcade Memory Interface (md_iop_arcade_acmem__r_e_a_d_m_e.html) |
- Arcade Memory Interface RPC (md_iop_arcade_acmeme__r_e_a_d_m_e.html) |
- Arcade Extended RAM Interface (md_iop_arcade_acram__r_e_a_d_m_e.html) |
- acrtc (md_iop_arcade_acrtc__r_e_a_d_m_e.html) |
- Arcade SRAM Interface (md_iop_arcade_acsram__r_e_a_d_m_e.html) |
- Arcade Simple Timer Interface (md_iop_arcade_actimer__r_e_a_d_m_e.html) |
- Arcade UART Interface (md_iop_arcade_acuart__r_e_a_d_m_e.html) |
- ROMWRITE (md_iop_arcade_romwrite__r_e_a_d_m_e.html) |
- S147CTRL (md_iop_arcade_s147ctrl__r_e_a_d_m_e.html) |
- S147LINK (md_iop_arcade_s147link__r_e_a_d_m_e.html) |
- S147MDEV (md_iop_arcade_s147mdev__r_e_a_d_m_e.html) |
- S147NAND (md_iop_arcade_s147nand__r_e_a_d_m_e.html) |
- S147NETB (md_iop_arcade_s147netb__r_e_a_d_m_e.html) |
- Power off simulation (md_iop_cdvd_poffsim__r_e_a_d_m_e.html) |
- DEV5 SPEED module for ATAPI (md_iop_cdvd_xatapi__r_e_a_d_m_e.html) |
- PPC TTY (md_iop_debug_ppctty__r_e_a_d_m_e.html) |
- Simple Thread Monitor (md_iop_debug_thmon__r_e_a_d_m_e.html) |
- Additional ROM driver (md_iop_fs_adddrv__r_e_a_d_m_e.html) |
- Additional ROM driver (md_iop_fs_addrom2__r_e_a_d_m_e.html) |
- Encrypted ROM driver (md_iop_fs_eromdrv__r_e_a_d_m_e.html) |
- FILEIO server service module (md_iop_fs_fileio__r_e_a_d_m_e.html) |
- ROM/Flash Driver (md_iop_fs_romdrv__r_e_a_d_m_e.html) |
- Subfile (md_iop_fs_subfile__r_e_a_d_m_e.html) |
- AN986 USB Ethernet driver (md_iop_network_an986__r_e_a_d_m_e.html) |
- Network configuration library (md_iop_network_netcnf__r_e_a_d_m_e.html) |
- Network configuration library interface (md_iop_network_netcnfif__r_e_a_d_m_e.html) |
- Daemon (aka: sec_checker) (md_iop_security_daemon__r_e_a_d_m_e.html) |
- Security manager (md_iop_security_secrman__r_e_a_d_m_e.html) |
- Security manager RPC server (md_iop_security_secrsif__r_e_a_d_m_e.html) |
- SIO2 Manager (md_iop_sio_sio2man__r_e_a_d_m_e.html) |
- Clear SPU module (md_iop_sound_clearspu__r_e_a_d_m_e.html) |
- Extended Sound Library for SPU2 (md_iop_sound_libsnd2__r_e_a_d_m_e.html) |
- Basic Sound Library for SPU2 (md_iop_sound_libspu2__r_e_a_d_m_e.html) |
- Remote SPU2 Driver (md_iop_sound_rspu2drv__r_e_a_d_m_e.html) |
- Sound data (HD file) access library (md_iop_sound_sdhd__r_e_a_d_m_e.html) |
- Sound Device Remote Library (md_iop_sound_sdrdrv__r_e_a_d_m_e.html) |
- Sound data (SQ file) access library (md_iop_sound_sdsq__r_e_a_d_m_e.html) |
- Board information module (md_iop_system_boardinf__r_e_a_d_m_e.html) |
- DMA Controller Manager (md_iop_system_dmacman__r_e_a_d_m_e.html) |
- Dummy IOP Module (md_iop_system_dummymod__r_e_a_d_m_e.html) |
- EE Configuration Module (md_iop_system_eeconf__r_e_a_d_m_e.html) |
- EE Synchronization Module (md_iop_system_eesync__r_e_a_d_m_e.html) |
- Exception manager (md_iop_system_excepman__r_e_a_d_m_e.html) |
- Heap library (md_iop_system_heaplib__r_e_a_d_m_e.html) |
- IOP Greeting (md_iop_system_igreeting__r_e_a_d_m_e.html) |
- Interrupt Manager (md_iop_system_intrman__r_e_a_d_m_e.html) |
- I/O Manager (md_iop_system_ioman__r_e_a_d_m_e.html) |
- Module Manager (md_iop_system_loadcore__r_e_a_d_m_e.html) |
- RPC server for executable loading management (md_iop_system_loadfile__r_e_a_d_m_e.html) |
- IOP module loader (md_iop_system_modload__r_e_a_d_m_e.html) |
- Multi-threaded SIF service (md_iop_system_msifrpc__r_e_a_d_m_e.html) |
- Reboot command server (md_iop_system_reboot__r_e_a_d_m_e.html) |
- Remote Reset (md_iop_system_rmreset__r_e_a_d_m_e.html) |
- SIF CMD (md_iop_system_sifcmd__r_e_a_d_m_e.html) |
- SIF Initialization (md_iop_system_sifinit__r_e_a_d_m_e.html) |
- SIF Manager (md_iop_system_sifman__r_e_a_d_m_e.html) |
- SSBUSC manager (md_iop_system_ssbusc__r_e_a_d_m_e.html) |
- Standard I/O module (md_iop_system_stdio__r_e_a_d_m_e.html) |
- System C Library (md_iop_system_sysclib__r_e_a_d_m_e.html) |
- System memory manager (md_iop_system_sysmem__r_e_a_d_m_e.html) |
- Vertical blank service (md_iop_system_vblank__r_e_a_d_m_e.html) |
- USB Automatic Module Loader (md_iop_usb_usbmload__r_e_a_d_m_e.html) |
- srxfixup (md_tools_srxfixup__r_e_a_d_m_e.html) |

---
