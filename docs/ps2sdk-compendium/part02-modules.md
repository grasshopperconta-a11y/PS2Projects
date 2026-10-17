# Part 2 — Modules

## devfs: PS2 Device Filing System

Page: <https://ps2dev.github.io/ps2sdk/group__devfs.html>

##### Macros
| #define | DEVFS_MAX_SUBDEVS 16 |
| #define | DEVFS_MAX_DEVNAME_LENGTH 32 |
| #define | DEVFS_MAX_DESC_LENGTH 256 |
| #define | DEVFS_IOCTL_TYPE_1 1 |
| #define | DEVFS_IOCTL_TYPE_2 2 |
| #define | DEVFS_IOCTL_GETDESC 0 |
| #define | INVALID_HDEV -1 |
| #define | devfs_IMPORTS_start DECLARE_IMPORT_TABLE(devfs, 1, 1) |
| #define | devfs_IMPORTS_end END_IMPORT_TABLE |
| #define | I_DevFSAddDevice DECLARE_IMPORT(4, DevFSAddDevice) |
| #define | I_DevFSDelDevice DECLARE_IMPORT(5, DevFSDelDevice) |
| #define | I_DevFSAddSubDevice DECLARE_IMPORT(6, DevFSAddSubDevice) |
| #define | I_DevFSDelSubDevice DECLARE_IMPORT(7, DevFSDelSubDevice) |
##### Typedefs
| typedef s32 | HDEV |
| typedef s32(* | read_handler) (const devfs_info_t *dev, u8 *buf, s32 len) |
| typedef s32(* | write_handler) (const devfs_info_t *dev, u8 *buf, s32 len) |
| typedef s32(* | ioctl_handler) (const devfs_info_t *dev, int ioctl_type, int cmd, void *arg, size_t arglen, void *buf, size_t buflen) |
##### Enumerations
| enum | devfs_subdev_modes { DEVFS_MODE_EX = (1 << 0), DEVFS_MODE_W = (1 << 1), DEVFS_MODE_R = (1 << 2), DEVFS_MODE_RW = (DEVFS_MODE_R | DEVFS_MODE_W) } |
| enum | devfs_devtypes { DEVFS_DEVTYPE_CHAR = 1, DEVFS_DEVTYPE_BLOCK = 2, DEVFS_DEVTYPE_STREAM = 3 } |
##### Functions
| HDEV | DevFSAddDevice (const devfs_node_t *node) |
| int | DevFSDelDevice (HDEV hDev) |
| int | DevFSAddSubDevice (HDEV hDev, u32 subdev_no, s32 mode, devfs_loc_t extent, void *data) |
| int | DevFSDelSubDevice (HDEV hDev, u32 subdev_no) |
##### Detailed Description
##### Macro Definition Documentation
##### ◆ DEVFS_MAX_SUBDEVS
| #define DEVFS_MAX_SUBDEVS 16 |
#include <iop/fs/devfs/include/devfs.h>
Maximum number of sub devices per device
Definition at line 28 of file devfs.h.
##### ◆ DEVFS_MAX_DEVNAME_LENGTH
| #define DEVFS_MAX_DEVNAME_LENGTH 32 |
#include <iop/fs/devfs/include/devfs.h>
Maximum size of a device name
Definition at line 30 of file devfs.h.
##### ◆ DEVFS_MAX_DESC_LENGTH
| #define DEVFS_MAX_DESC_LENGTH 256 |
#include <iop/fs/devfs/include/devfs.h>
Maximum length of a description string
Definition at line 32 of file devfs.h.
##### ◆ DEVFS_IOCTL_TYPE_1
| #define DEVFS_IOCTL_TYPE_1 1 |
#include <iop/fs/devfs/include/devfs.h>
Specifies ioctl was called. No return value and the lengths are invalid
Definition at line 61 of file devfs.h.
##### ◆ DEVFS_IOCTL_TYPE_2
| #define DEVFS_IOCTL_TYPE_2 2 |
#include <iop/fs/devfs/include/devfs.h>
ioctl2 was called. Parameters should all be valid
Definition at line 63 of file devfs.h.
##### ◆ DEVFS_IOCTL_GETDESC
| #define DEVFS_IOCTL_GETDESC 0 |
#include <iop/fs/devfs/include/devfs.h>
ioctl command to return the description associated with a device
Definition at line 66 of file devfs.h.
##### ◆ INVALID_HDEV
| #define INVALID_HDEV -1 |
#include <iop/fs/devfs/include/devfs.h>
Defines an invalid HDEV value
Definition at line 152 of file devfs.h.
##### Typedef Documentation
##### ◆ HDEV
| typedef s32 HDEV |
#include <iop/fs/devfs/include/devfs.h>
Type to hold a handle to a device
Definition at line 26 of file devfs.h.
##### ◆ read_handler
| typedef s32(* read_handler) (const devfs_info_t *dev, u8 *buf, s32 len) |
#include <iop/fs/devfs/include/devfs.h>
Typedef of the read event handler
Definition at line 95 of file devfs.h.
##### ◆ write_handler
| typedef s32(* write_handler) (const devfs_info_t *dev, u8 *buf, s32 len) |
#include <iop/fs/devfs/include/devfs.h>
Typedef of the write event handler
Definition at line 97 of file devfs.h.
##### ◆ ioctl_handler
| typedef s32(* ioctl_handler) (const devfs_info_t *dev, int ioctl_type, int cmd, void *arg, size_t arglen, void *buf, size_t buflen) |
#include <iop/fs/devfs/include/devfs.h>
Typedef of the ioctl handler
Definition at line 99 of file devfs.h.
##### Enumeration Type Documentation
##### ◆ devfs_subdev_modes
| enum devfs_subdev_modes |
#include <iop/fs/devfs/include/devfs.h>
Enumeration of sub device access modes
| Enumerator |
| DEVFS_MODE_EX | Indicates a sub device can only be opened by one application at a time |
| DEVFS_MODE_W | Indicates a sub device can be opened for reading |
| DEVFS_MODE_R | Indicates a sub device can be opened for writing |
| DEVFS_MODE_RW | Indicates a sub device can be opened for reading and writing |
Definition at line 35 of file devfs.h.
##### ◆ devfs_devtypes
| enum devfs_devtypes |
#include <iop/fs/devfs/include/devfs.h>
Enumeration of device type.
**Note:** These are currently not used
| Enumerator |
| DEVFS_DEVTYPE_CHAR | Indicates a device is character device |
| DEVFS_DEVTYPE_BLOCK | Indicates a device is a block device |
| DEVFS_DEVTYPE_STREAM | Indicates a device is a stream device (no seek) |
Definition at line 50 of file devfs.h.
##### Function Documentation
##### ◆ DevFSAddDevice()
| HDEV DevFSAddDevice | ( | const devfs_node_t * | node | ) |  |
#include <iop/fs/devfs/include/devfs.h>
Adds a new device to the filing system
**Parameters:** nodePointer to a devfs_node_t structure
**Returns:** A device handle is returned if the device was added. On error INVALID_HDEV is returned
Definition at line 1109 of file devfs.c.
##### ◆ DevFSDelDevice()
| int DevFSDelDevice | ( | HDEV | hDev | ) |  |
#include <iop/fs/devfs/include/devfs.h>
Define to add DevFSAddDevice to the imports list Deletes an previously opened device.
**Parameters:** hDevHandle to the device to delete
**Returns:** 0 if device deleted, -1 on error
Definition at line 1162 of file devfs.c.
References devfs_find_deviceid(), DEVFS_MAX_SUBDEVS, and _devfs_device::forw.
##### ◆ DevFSAddSubDevice()
| int DevFSAddSubDevice | ( | HDEV | hDev, |
|  |  | u32 | subdev_no, |
|  |  | s32 | mode, |
|  |  | devfs_loc_t | extent, |
|  |  | void * | data |
|  | ) |  |  |
#include <iop/fs/devfs/include/devfs.h>
Adds a sub device to a previously opened device
**Parameters:** hDevHandle to an opened device subdev_noThe number of the subdevice. Can be 0 to DEVFS_MAX_SUBDEVS extentA 64bit extent which reflects the size of the underlying device dataPointer to some private data to associate with this sub device
**Returns:** 0 if sub device added, else -1
Definition at line 1213 of file devfs.c.
##### ◆ DevFSDelSubDevice()
| int DevFSDelSubDevice | ( | HDEV | hDev, |
|  |  | u32 | subdev_no |
|  | ) |  |  |
#include <iop/fs/devfs/include/devfs.h>
Deletes a sub device.
**Parameters:** hDevHandle to an opened device. subdev_noThe number of the subdevice to delete.
**Returns:** 0 if device deleted. -1 on error.
Definition at line 1251 of file devfs.c.
References devfs_find_deviceid().

---

## fakehost - host: to hdd driver

Page: <https://ps2dev.github.io/ps2sdk/group__fakehost.html>

##### Functions
| char * | fd_name (char *buffer, const char *name) |
| int | fd_save (int fd, iop_io_file_t *f) |
| int | realfd (iop_io_file_t *f) |
| int | fd_open (iop_io_file_t *f, const char *name, int mode) |
| int | fd_close (iop_io_file_t *f) |
| int | fd_read (iop_io_file_t *f, void *buffer, int size) |
| int | fd_write (iop_io_file_t *fd, void *buffer, int size) |
| int | fd_lseek (iop_io_file_t *fd, int offset, int whence) |
| int | _start (int argc, char *argv[]) |
| static void * | naplinkRpcHandler (int cmd, void *buffer, int size) |
| static void | napThread (void *arg) |
| int | naplinkRpcInit (void) |
##### Detailed Description
##### Function Documentation
##### ◆ fd_name()
| char* fd_name | ( | char * | buffer, |
|  |  | const char * | name |
|  | ) |  |  |
#include <iop/fs/fakehost/src/fakehost.c>
Make a full pathname string, adding base on.
**Parameters:** bufferbuffer to hold result. namename to add base to.
**Returns:** Pointer to buffer.
This function takes the name param and adds it to the basename for replacement, returning the destination full pathname.
Definition at line 75 of file fakehost.c.
##### ◆ fd_save()
| int fd_save | ( | int | fd, |
|  |  | iop_io_file_t * | f |
|  | ) |  |  |
#include <iop/fs/fakehost/src/fakehost.c>
Store filedescriptor and get client filedescriptor.
**Parameters:** fdfiledescriptor to store. fio_file pointer to store fd in .
**Returns:** client filedescriptor.
Definition at line 89 of file fakehost.c.
##### ◆ realfd()
| int realfd | ( | iop_io_file_t * | f | ) |  |
#include <iop/fs/fakehost/src/fakehost.c>
Get real filedescriptor.
**Parameters:** fio_file pointer to get fd from.
**Returns:** real filedescriptor.
Definition at line 102 of file fakehost.c.
References _iop_io_file::privdata.
##### ◆ fd_open()
| int fd_open | ( | iop_io_file_t * | f, |
|  |  | const char * | name, |
|  |  | int | mode |
|  | ) |  |  |
#include <iop/fs/fakehost/src/fakehost.c>
Handle open request.
**Parameters:** fPointer to io_device structure. namepathname. modeopen mode.
**Returns:** Status (as for fileio open).
Definition at line 115 of file fakehost.c.
##### ◆ fd_close()
| int fd_close | ( | iop_io_file_t * | f | ) |  |
#include <iop/fs/fakehost/src/fakehost.c>
Handle close request.
**Parameters:** fPointer to io_device structure.
**Returns:** Status (as for fileio close).
Definition at line 133 of file fakehost.c.
##### ◆ fd_read()
| int fd_read | ( | iop_io_file_t * | f, |
|  |  | void * | buffer, |
|  |  | int | size |
|  | ) |  |  |
#include <iop/fs/fakehost/src/fakehost.c>
Handle read request.
**Parameters:** fPointer to io_device structure. bufferPointer to read buffer. sizeSize of buffer.
**Returns:** Status (as for fileio read).
Definition at line 146 of file fakehost.c.
##### ◆ fd_write()
| int fd_write | ( | iop_io_file_t * | fd, |
|  |  | void * | buffer, |
|  |  | int | size |
|  | ) |  |  |
#include <iop/fs/fakehost/src/fakehost.c>
Handle write request.
**Parameters:** fPointer to io_device structure. bufferPointer to read buffer. sizeSize of buffer.
**Returns:** Status (as for fileio write).
Definition at line 159 of file fakehost.c.
##### ◆ fd_lseek()
| int fd_lseek | ( | iop_io_file_t * | fd, |
|  |  | int | offset, |
|  |  | int | whence |
|  | ) |  |  |
#include <iop/fs/fakehost/src/fakehost.c>
Handle lseek request.
**Parameters:** fPointer to io_device structure. offsetOffset for seek. whenceBase for seek.
**Returns:** Status (as for fileio lseek).
Definition at line 172 of file fakehost.c.
##### ◆ _start()
| int _start | ( | int | argc, |
|  |  | char * | argv[] |
|  | ) |  |  |
#include <iop/fs/fakehost/src/fakehost.c>
Entry point for IRX.
if argc != 2 , quit, as it needs parameter if argc == 2 , use arv[1] as basename.
**Parameters:** argcNumber of arguments. argvPointer to array of arguments.
**Returns:** Module Status on Exit.
This initialises the fakehost driver, setting up the 'host:' fs driver basename redirection, and naplink compatible rpc hander.
return values: MODULE_RESIDENT_END if loaded and registered as library. MODULE_NO_RESIDENT_END if just exiting normally.
Definition at line 227 of file fakehost.c.
##### ◆ naplinkRpcHandler()
| static void* naplinkRpcHandler ( int cmd, void * buffer, int size ) | static |
#include <iop/fs/fakehost/src/nprintf.c>
RPC handler function.
**Parameters:** cmdCommand. bufferPointer to buffer. sizeSize of buffer.
Definition at line 38 of file nprintf.c.
##### ◆ napThread()
| static void napThread ( void * arg) | static |
#include <iop/fs/fakehost/src/nprintf.c>
naplink compatbile RPC handler thread.
**Parameters:** argStartup parameters.
Definition at line 56 of file nprintf.c.
##### ◆ naplinkRpcInit()
| int naplinkRpcInit | ( | void |  | ) |  |
#include <iop/fs/fakehost/src/nprintf.c>
Setup naplink compatible RPC handler.
**Returns:** Status.
return values: 0 on success. -1 on error.
Definition at line 80 of file nprintf.c.

---

## iopmgr - IOP Manager

Page: <https://ps2dev.github.io/ps2sdk/group__iopmgr.html>

##### Functions
| void | list_all_libraries () |
| void | list_all_modules () |
| void | list_devices_ioman () |
| void | list_devices_iomanx () |
| void | list_fs_devices (int mgrtype) |
| void | cmdline_handle (char *command, char *arg1) |
| iop_device_t * | iopmgr_get_iomandev (char *device) |
| iop_device_t * | iopmgr_get_iomanxdev (char *device) |
| int | iopmgr_get_devicelist (int man, int devtype, char *buffer) |
| iop_device_t * | iopmgr_get_device (char *device) |
| int | iopmgr_get_devicetype (char *device) |
| int | _start (int argc, char *argv[]) |
| int | shutdown () |
| iop_library_t * | slib_get_lib_by_name (const char *name) |
| void * | slib_get_exportlist_by_name (const char *name) |
| int | slib_get_version_by_name (const char *name) |
| int | slib_release_library (const char *name) |
| ModuleInfo_t * | smod_get_next_mod (ModuleInfo_t *cur_mod) |
| ModuleInfo_t * | smod_get_mod_by_name (const char *name) |
| int | smod_get_modcount_by_name (const char *name) |
| int | smod_get_modversion_by_name (const char *name) |
| int | smod_unload_module (const char *name) |
##### Detailed Description
##### Function Documentation
##### ◆ list_all_libraries()
| void list_all_libraries | ( |  | ) |  |
#include <iop/system/iopmgr/src/commandline.c>
Prints out a list of all currently registered libraries with their name and version.
Definition at line 28 of file commandline.c.
##### ◆ list_all_modules()
| void list_all_modules | ( |  | ) |  |
#include <iop/system/iopmgr/src/commandline.c>
Prints out a list of all currently loaded IRX modules with description and version number.
Definition at line 52 of file commandline.c.
##### ◆ list_devices_ioman()
| void list_devices_ioman | ( |  | ) |  |
#include <iop/system/iopmgr/src/commandline.c>
Print out all devices for ONLY ioman and shows which one they belong to.
Definition at line 69 of file commandline.c.
References smod_get_mod_by_name().
##### ◆ list_devices_iomanx()
| void list_devices_iomanx | ( |  | ) |  |
#include <iop/system/iopmgr/src/commandline.c>
Print out all devices for ONLY iomanx and shows which one they belong to.
Definition at line 99 of file commandline.c.
References smod_get_mod_by_name().
##### ◆ list_fs_devices()
| void list_fs_devices | ( | int | mgrtype | ) |  |
#include <iop/system/iopmgr/src/commandline.c>
Print out all devices for both ioman and iomanx and shows which one they belong to.
**Parameters:** mgrtypeDevice manager type search mask (IOPMGR_DEVTYPE_XXXX).
Definition at line 131 of file commandline.c.
References count.
##### ◆ cmdline_handle()
| void cmdline_handle | ( | char * | command, |
|  |  | char * | arg1 |
|  | ) |  |  |
#include <iop/system/iopmgr/src/commandline.c>
Handles basic parsing of commands, for command execution mode.
**Parameters:** commandPointer to command string.
Definition at line 161 of file commandline.c.
##### ◆ iopmgr_get_iomandev()
| iop_device_t* iopmgr_get_iomandev | ( | char * | device | ) |  |
#include <iop/system/iopmgr/src/devices.c>
Get a pointer to an ioman device handler.
**Parameters:** deviceStringname of device (eg "host").
**Returns:** Pointer to device structure.
return values: 0 if not found. pointer to device structure for named driver if found.
Definition at line 34 of file devices.c.
Referenced by iopmgr_get_device(), and iopmgr_get_devicetype().
##### ◆ iopmgr_get_iomanxdev()
| iop_device_t* iopmgr_get_iomanxdev | ( | char * | device | ) |  |
#include <iop/system/iopmgr/src/devices.c>
Get a pointer to an iomanx device handler.
**Parameters:** deviceStringname of device (eg "hdd").
**Returns:** Pointer to device structure.
return values: 0 if not found. pointer to device structure for named driver if found.
Definition at line 67 of file devices.c.
##### ◆ iopmgr_get_devicelist()
| int iopmgr_get_devicelist | ( | int | man, |
|  |  | int | devtype, |
|  |  | char * | buffer |
|  | ) |  |  |
#include <iop/system/iopmgr/src/devices.c>
Get a list of devices of a certain type
**Parameters:** manDevice manager mask (IOPMGR_DEVTYPE_IOMAN or IOPMGR_DEVTYPE_IOMANX). devtypeDevice type mask (0x10 for filesystems).
**Returns:** Number of devices found
return values: 0 if no matching devices found device count, if found, and buffer buffer filled with ascii serial string of device names.
Definition at line 102 of file devices.c.
##### ◆ iopmgr_get_device()
| iop_device_t* iopmgr_get_device | ( | char * | device | ) |  |
#include <iop/system/iopmgr/src/devices.c>
Get a pointer to a device of either type
**Parameters:** deviceStringname of device (eg "host).
**Returns:** Pointer to device structure.
return values: 0 if not found. pointer to device structure for named driver if found.
Definition at line 163 of file devices.c.
References iopmgr_get_iomandev().
##### ◆ iopmgr_get_devicetype()
| int iopmgr_get_devicetype | ( | char * | device | ) |  |
#include <iop/system/iopmgr/src/devices.c>
Returns which i/o manager handles the given device.
**Parameters:** deviceStringname of device (eg "host).
**Returns:** numeric value for i/o manager.
return values: IOPMGR_DEVTYPE_INVALID if not found, IOPMGR_DEVTYPE_IOMAN if found and ioman device, IOPMGR_DEVTYPE_IOMANX if found and iomanx device.
Definition at line 184 of file devices.c.
References iopmgr_get_iomandev().
##### ◆ _start()
| int _start | ( | int | argc, |
|  |  | char * | argv[] |
|  | ) |  |  |
#include <iop/system/iopmgr/src/main.c>
Entry point for IRX.
if argc <= 1 , install as library. if argc > 1 , run given command in argv[1].
**Parameters:** argcNumber of arguments. argvPointer to array of arguments.
**Returns:** Module Status on Exit.
return values: MODULE_RESIDENT_END if loaded and registered as library. MODULE_NO_RESIDENT_END if just exiting normally.
Definition at line 46 of file main.c.
##### ◆ shutdown()
| int shutdown | ( |  | ) |  |
#include <iop/system/iopmgr/src/main.c>
shutdown the IRX.
This checks if the library is registered, if it is then it unregisters it.
**Returns:** Module Status on Exit.
return values: MODULE_RESIDENT_END if loaded and registered as library. MODULE_NO_RESIDENT_END if just exiting normally.
Definition at line 99 of file main.c.
References slib_release_library().
##### ◆ slib_get_lib_by_name()
| iop_library_t* slib_get_lib_by_name | ( | const char * | name | ) |  |
#include <iop/system/iopmgr/src/slib.c>
Get pointer to system library structure for named library.
**Parameters:** nameStringname of library (eg "ioman").
**Returns:** Pointer to IOP library structure.
return values: 0 if not found. pointer to library structure for registered library if found.
Definition at line 37 of file slib.c.
##### ◆ slib_get_exportlist_by_name()
| void* slib_get_exportlist_by_name | ( | const char * | name | ) |  |
#include <iop/system/iopmgr/src/slib.c>
Get pointer to export list for named library.
**Parameters:** nameStringname of library (eg "ioman").
**Returns:** Pointer to export list.
return values: 0 if not found. pointer to export list for registered library if found.
Definition at line 62 of file slib.c.
##### ◆ slib_get_version_by_name()
| int slib_get_version_by_name | ( | const char * | name | ) |  |
#include <iop/system/iopmgr/src/slib.c>
Get version number for named library.
**Parameters:** nameStringname of library (eg "ioman").
**Returns:** version number.
return values: 0 if not found. Version number for registered library if found. (0xXXYY, XX=HIGH, YY=LOW)
Definition at line 82 of file slib.c.
##### ◆ slib_release_library()
| int slib_release_library | ( | const char * | name | ) |  |
#include <iop/system/iopmgr/src/slib.c>
Release (Unregister) a given named registered library.
**Parameters:** nameStringname of library (eg "ioman").
**Returns:** Status of operation.
return values: 0 if found and sucessfully unregistered. -1 if found, but failed to unregister. -2 if library was not found.
Definition at line 103 of file slib.c.
Referenced by shutdown().
##### ◆ smod_get_next_mod()
| ModuleInfo_t* smod_get_next_mod | ( | ModuleInfo_t * | cur_mod | ) |  |
#include <iop/system/iopmgr/src/smod.c>
Get pointer to head of module list, or next module in list.
**Parameters:** cur_modPointer to module structure, or 0 to return the head.
**Returns:** Pointer to module structure.
return values: 0 if end of list. pointer to head of module list if cur_mod=0. pointer to next module, if cur_mod!=0.
Definition at line 39 of file smod.c.
##### ◆ smod_get_mod_by_name()
| ModuleInfo_t* smod_get_mod_by_name | ( | const char * | name | ) |  |
#include <iop/system/iopmgr/src/smod.c>
Get pointer to module structure for named module.
**Parameters:** nameStringname of module (eg "atad_driver").
**Returns:** Pointer to module structure.
return values: 0 if not found. pointer to module structure for loaded module if found.
Definition at line 63 of file smod.c.
##### ◆ smod_get_modcount_by_name()
| int smod_get_modcount_by_name | ( | const char * | name | ) |  |
#include <iop/system/iopmgr/src/smod.c>
Get instance count for given module name.
**Parameters:** nameStringname of module (eg "atad_driver").
**Returns:** Number of instances loaded.
NOTE: if doing this to check for own module, the run being used to check automatically adds one to the count.. so ret=2 means another, instance loaded as well as current one.
Definition at line 88 of file smod.c.
##### ◆ smod_get_modversion_by_name()
| int smod_get_modversion_by_name | ( | const char * | name | ) |  |
#include <iop/system/iopmgr/src/smod.c>
Get version number for given module name.
**Parameters:** nameStringname of module (eg "atad_driver").
**Returns:** Version number.
return values: 0 if not found. Version number for module if found. (0xXXYY, XX=HIGH, YY=LOW)
Definition at line 115 of file smod.c.
##### ◆ smod_unload_module()
| int smod_unload_module | ( | const char * | name | ) |  |
#include <iop/system/iopmgr/src/smod.c>
Unload the named module.
**Parameters:** nameStringname of module (eg "atad_driver").
**Returns:** Status of operation.
return values: 0 if found and sucessfully unloaded. -1 if found, but failed to unload. -2 if module was not found.
Definition at line 136 of file smod.c.

---

## EE LOADFILE: ELF and IRX loader client library.

Page: <https://ps2dev.github.io/ps2sdk/group__loadfile.html>

##### Functions
| int | SifLoadFileInit (void) |
| void | SifLoadFileExit (void) |
| int | SifLoadModule (const char *path, int arg_len, const char *args) |
| int | SifLoadStartModule (const char *path, int arg_len, const char *args, int *mod_res) |
| int | SifLoadModuleEncrypted (const char *path, int arg_len, const char *args) |
| int | SifLoadModuleBuffer (void *ptr, int arg_len, const char *args) |
| int | SifLoadStartModuleBuffer (void *ptr, int arg_len, const char *args, int *mod_res) |
| int | SifLoadElfPart (const char *path, const char *secname, t_ExecData *data) |
| int | SifLoadElf (const char *path, t_ExecData *data) |
| int | SifLoadElfEncrypted (const char *path, t_ExecData *data) |
| int | SifIopSetVal (u32 iop_addr, int val, int type) |
| int | SifIopGetVal (u32 iop_addr, void *val, int type) |
| int | SifExecModuleBuffer (void *ptr, u32 size, u32 arg_len, const char *args, int *mod_res) |
| int | SifExecModuleFile (const char *path, u32 arg_len, const char *args, int *mod_res) |
| int | _SifLoadModule (const char *path, int arg_len, const char *args, int *modres, int fno, int dontwait) |
##### Detailed Description
##### Function Documentation
##### ◆ SifLoadFileInit()
| int SifLoadFileInit | ( | void |  | ) |  |
#include <ee/kernel/include/loadfile.h>
Initialize the LOADFILE library.
**Returns:** 0 on success, E_SIF_RPC_BIND if unable to connect to the server.
Initializes the LOADFILE API and binds to the remote LOADFILE RPC server.
##### ◆ SifLoadFileExit()
| void SifLoadFileExit | ( | void |  | ) |  |
#include <ee/kernel/include/loadfile.h>
Reset the LOADFILE library.
Deinitializes the LOADFILE library in preparation of an IOP reset.
##### ◆ SifLoadModule()
| int SifLoadModule | ( | const char * | path, |
|  |  | int | arg_len, |
|  |  | const char * | args |
|  | ) |  |  |
#include <ee/kernel/include/loadfile.h>
Load and execute an IRX module.
**Parameters:** pathPath to an IRX module arg_lenLength, in bytes, of the argument list argsList of arguments to pass to the IRX on startup
**Returns:** The ID of the loaded module on success, or an error if the module couldn't be loaded.
Loads an IRX module from the specified path, and executes it. The args parameter specifies a list of arguments that are passed to the loaded module as the argv[] array. Each argument string in args must be seperated by NUL ('\0'). Pass the length of the entire args list, including the NUL seperators in the args_len parameter.
**Note:** By default, modules cannot be loaded directly from the memory card. If you need to load modules from the memory card, you should use SifExecModuleFile or link with the sbv-lite library (http://www.0xd6.org).
**See also:** SifExecModuleFile
##### ◆ SifLoadStartModule()
| int SifLoadStartModule | ( | const char * | path, |
|  |  | int | arg_len, |
|  |  | const char * | args, |
|  |  | int * | mod_res |
|  | ) |  |  |
#include <ee/kernel/include/loadfile.h>
Load and execute and IRX module, and retrieve the module's load status.
**Parameters:** pathPath to an IRX module arg_lenLength, in bytes, of the argument list argsList of arguments to pass to the IRX on startup mod_resPointer to a variable that will store the return value from the IRX's _start() function
**Returns:** The ID of the loaded module on success, or an error if the module couldn't be loaded.
Loads an IRX module from the specified path, and executes it. See SifLoadModule for details on the arg_len and args parameters. If mod_res is non-NULL, the result code from the module's _start() function is stored here.
**See also:** SifLoadModule
##### ◆ SifLoadModuleEncrypted()
| int SifLoadModuleEncrypted | ( | const char * | path, |
|  |  | int | arg_len, |
|  |  | const char * | args |
|  | ) |  |  |
#include <ee/kernel/include/loadfile.h>
Load and execute an IRX module encrypted with MagicGate.
**Parameters:** pathPath to an IRX module arg_lenLength, in bytes, of the argument list argsList of arguments to pass to the IRX on startup
**Returns:** The ID of the loaded module on success, or an error if the module couldn't be loaded.
There is no real use for this function; it is only included in ps2lib for completeness.
**See also:** SifLoadModule
##### ◆ SifLoadModuleBuffer()
| int SifLoadModuleBuffer | ( | void * | ptr, |
|  |  | int | arg_len, |
|  |  | const char * | args |
|  | ) |  |  |
#include <ee/kernel/include/loadfile.h>
Load and execute an IRX module from a buffer in IOP RAM.
**Parameters:** ptrPointer to a buffer in IOP RAM where the IRX module will be loaded from arg_lenLength, in bytes, of the argument list argsList of arguments to pass to the IRX on startup
**Returns:** The ID of the loaded module on success, or an error if the module couldn't be loaded.
Loads an IRX module from a buffer located in IOP RAM. See SifLoadModule for details on the arg_len and args parameters.
**Note:** If you need to load an IRX module onto the IOP directly from a buffer in EE RAM, then use SifExecModuleBuffer.
**See also:** SifLoadModule, SifExecModuleBuffer
##### ◆ SifLoadStartModuleBuffer()
| int SifLoadStartModuleBuffer | ( | void * | ptr, |
|  |  | int | arg_len, |
|  |  | const char * | args, |
|  |  | int * | mod_res |
|  | ) |  |  |
#include <ee/kernel/include/loadfile.h>
Load and execute an IRX module from a buffer in IOP RAM, and retrieve the module's load status.
**Parameters:** ptrPointer to a buffer in IOP RAM where the IRX module will be loaded from arg_lenLength, in bytes, of the argument list argsList of arguments to pass to the IRX on startup mod_resPointer to a variable that will store the return value from the IRX's _start() function
**Returns:** The ID of the loaded module on success, or an error if the module couldn't be loaded.
Loads an IRX module from a buffer located in IOP RAM. See SifLoadModule for details on the arg_len and args parameters. If mod_res is non-NULL, the result code from the module's _start() function is stored here.
**Note:** If you need to load an IRX module onto the IOP directly from a buffer in EE RAM, then use SifExecModuleBuffer.
**See also:** SifLoadModule, SifExecModuleBuffer
##### ◆ SifLoadElfPart()
| int SifLoadElfPart | ( | const char * | path, |
|  |  | const char * | secname, |
|  |  | t_ExecData * | data |
|  | ) |  |  |
#include <ee/kernel/include/loadfile.h>
Load the specified section of an ELF executable into EE RAM.
**Parameters:** pathPath to an ELF executable secnameThe name of a single section to load from the ELF, or "all" to load all sections dataPointer to a variable that will store information about the loaded executable
**Returns:** 0 on success, or an error code if an error occurred.
Loads the section secname from the ELF file specified by path into EE RAM.
data points to a t_ExecData structure where information about the loaded section will be returned.
**Warning:** Don't ever use this function, it does not work as intended.
##### ◆ SifLoadElf()
| int SifLoadElf | ( | const char * | path, |
|  |  | t_ExecData * | data |
|  | ) |  |  |
#include <ee/kernel/include/loadfile.h>
Load an ELF executable into EE RAM.
**Parameters:** pathPath to an ELF executable dataPointer to a variable that will store information about the loaded executable
**Returns:** 0 on success, or an error code if an error occurred.
Loads the ELF executable specified by path into EE RAM. data points to a t_ExecData structure where information about the loaded executable will be returned.
**Warning:** It's possible to overwrite your program if the ELF that you're trying to load overlaps your program's memory space. Always ensure that the target ELF will load before or after your program's code and data addresses.
##### ◆ SifLoadElfEncrypted()
| int SifLoadElfEncrypted | ( | const char * | path, |
|  |  | t_ExecData * | data |
|  | ) |  |  |
#include <ee/kernel/include/loadfile.h>
Load a MagicGate-encrypted ELF executable into EE RAM.
**Parameters:** pathPath to an ELF executable dataPointer to a variable that will store information about the loaded executable
**Returns:** 0 on success, or an error code if an error occurred.
There is no real use for this function; it is only included in ps2lib for completeness.
**See also:** SifLoadElf
##### ◆ SifIopSetVal()
| int SifIopSetVal | ( | u32 | iop_addr, |
|  |  | int | val, |
|  |  | int | type |
|  | ) |  |  |
#include <ee/kernel/include/loadfile.h>
Write a value to an address within the IOP's memory space.
**Parameters:** iop_addrAddress to modify in the IOP's address space valData to write at iop_addr typeA type describing the size of the val argument
**Returns:** Previous value at iop_addr on success (?), or an error code if an error occurred.
Writes the data passed in val to the IOP address specified by iop_addr. Use the following types specify the size of data write:
- ::LF_VAL_BYTE to write an 8-bit value
- ::LF_VAL_SHORT to write a 16-bit value
- ::LF_VAL_LONG to write a 32-bit value
**Note:** Because iop_addr can be any address within the IOP's address space, it's possible to modify IOP hardware registers. However, in most cases the EE can modify the IOP's hardware registers directly so there is little use for this function.
**See also:** SifIopGetVal
##### ◆ SifIopGetVal()
| int SifIopGetVal | ( | u32 | iop_addr, |
|  |  | void * | val, |
|  |  | int | type |
|  | ) |  |  |
#include <ee/kernel/include/loadfile.h>
Read a value from an address within the IOP's memory space.
**Parameters:** iop_addrAddress within the IOP's address space to read from valPointer to a variable that stores the value read typeA type describing the size of the data to read
**Returns:** 0 on success, or an error code if an error occurred.
Reads data of the size specified by type from the IOP address specified by iop_addr. Use the following types to specify the size of the data to read:
- ::LF_VAL_BYTE to write an 8-bit value
- ::LF_VAL_SHORT to write a 16-bit value
- ::LF_VAL_LONG to write a 32-bit value
**Note:** Because iop_addr can be any address within the IOP's address space, it's possible to read from IOP hardware registers. However, in most cases the EE can read the IOP's hardware registers directly so there is little use for this function.
**See also:** SifIopSetVal
##### ◆ SifExecModuleBuffer()
| int SifExecModuleBuffer | ( | void * | ptr, |
|  |  | u32 | size, |
|  |  | u32 | arg_len, |
|  |  | const char * | args, |
|  |  | int * | mod_res |
|  | ) |  |  |
#include <ee/kernel/include/loadfile.h>
Transfer an IRX module from EE RAM to IOP RAM and execute it.
**Parameters:** ptrPointer to a buffer in EE RAM where the IRX module will be loaded from sizeSize of the buffer in EE RAM that contains the IRX module arg_lenLength, in bytes, of the argument list argsList of arguments to pass to the IRX on startup mod_resPointer to a variable that will store the return value from the IRX's _start() function
**Returns:** The ID of the loaded module on success, or an error if the module couldn't be loaded.
Transfers an IRX module stored in a buffer in EE RAM to the IOP, and calls SifLoadModuleBuffer to load and execute the module. See SifLoadModule for details on the arg_len and args parameters. If mod_res is non-NULL, the result code from the module's _start() function is stored here.
**See also:** SifLoadModule, SifLoadModuleBuffer
##### ◆ SifExecModuleFile()
| int SifExecModuleFile | ( | const char * | path, |
|  |  | u32 | arg_len, |
|  |  | const char * | args, |
|  |  | int * | mod_res |
|  | ) |  |  |
#include <ee/kernel/include/loadfile.h>
Read an IRX module from a file into IOP RAM and execute it.
**Parameters:** pathPath to an IRX module arg_lenLength, in bytes, of the argument list argsList of arguments to pass to the IRX on startup mod_resPointer to a variable that will store the return value from the IRX's _start() function
**Returns:** The ID of the loaded module on success, or an error if the module couldn't be loaded.
Loads an IRX module from the specified path into a buffer on the IOP, then calls SifLoadModuleBuffer to load and execute the module. See SifLoadModule for details on the arg_len and args parameters. This function is useful if you need to load an IRX module from a prohibited device, such as the memory card.
**See also:** SifLoadModule, SifLoadModuleBuffer
##### ◆ _SifLoadModule()
| int _SifLoadModule | ( | const char * | path, |
|  |  | int | arg_len, |
|  |  | const char * | args, |
|  |  | int * | modres, |
|  |  | int | fno, |
|  |  | int | dontwait |
|  | ) |  |  |
#include <ee/kernel/include/loadfile.h>
Low-level function for loading and executing an IRX module.
**Parameters:** pathPath to an IRX module arg_lenLength, in bytes, of the argument list argsList of arguments to pass to the IRX on startup *modresPointer to a variable that will store the return value from the IRX's _start() function fnoFunction number of function to execute. dontwaitWhether to wait for the module's _start function to finish executing.
**Returns:** The ID of the loaded module on success, or an error if the module couldn't be loaded.
Unless required, use the higher-level functions instead.
**See also:** SifLoadModule, SifLoadModuleBuffer, SifLoadModuleEncrypted

---

## Flags

Page: <https://ps2dev.github.io/ps2sdk/group__netif__flags.html>

##### Macros
| #define | NETIF_FLAG_UP 0x01U |
| #define | NETIF_FLAG_BROADCAST 0x02U |
| #define | NETIF_FLAG_LINK_UP 0x04U |
| #define | NETIF_FLAG_ETHARP 0x08U |
| #define | NETIF_FLAG_ETHERNET 0x10U |
| #define | NETIF_FLAG_IGMP 0x20U |
| #define | NETIF_FLAG_MLD6 0x40U |
##### Detailed Description
##### Macro Definition Documentation
##### ◆ NETIF_FLAG_UP
| #define NETIF_FLAG_UP 0x01U |
#include <common/include/tcpip.h>
Whether the network interface is 'up'. This is a software flag used to control whether this network interface is enabled and processes traffic. It must be set by the startup code before this netif can be used (also for dhcp/autoip).
Definition at line 1116 of file tcpip.h.
##### ◆ NETIF_FLAG_BROADCAST
| #define NETIF_FLAG_BROADCAST 0x02U |
#include <common/include/tcpip.h>
If set, the netif has broadcast capability. Set by the netif driver in its init function.
Definition at line 1119 of file tcpip.h.
##### ◆ NETIF_FLAG_LINK_UP
| #define NETIF_FLAG_LINK_UP 0x04U |
#include <common/include/tcpip.h>
If set, the interface has an active link (set by the network interface driver). Either set by the netif driver in its init function (if the link is up at that time) or at a later point once the link comes up (if link detection is supported by the hardware).
Definition at line 1125 of file tcpip.h.
##### ◆ NETIF_FLAG_ETHARP
| #define NETIF_FLAG_ETHARP 0x08U |
#include <common/include/tcpip.h>
If set, the netif is an ethernet device using ARP. Set by the netif driver in its init function. Used to check input packet types and use of DHCP.
Definition at line 1129 of file tcpip.h.
##### ◆ NETIF_FLAG_ETHERNET
| #define NETIF_FLAG_ETHERNET 0x10U |
#include <common/include/tcpip.h>
If set, the netif is an ethernet device. It might not use ARP or TCP/IP if it is used for PPPoE only.
Definition at line 1133 of file tcpip.h.
##### ◆ NETIF_FLAG_IGMP
| #define NETIF_FLAG_IGMP 0x20U |
#include <common/include/tcpip.h>
If set, the netif has IGMP capability. Set by the netif driver in its init function.
Definition at line 1136 of file tcpip.h.
##### ◆ NETIF_FLAG_MLD6
| #define NETIF_FLAG_MLD6 0x40U |
#include <common/include/tcpip.h>
If set, the netif has MLD6 capability. Set by the netif driver in its init function.
Definition at line 1139 of file tcpip.h.

---

## Packet2 library

Page: <https://ps2dev.github.io/ps2sdk/group__packet2.html>

Successor of packet_t. Main goal of this library is to create simple API for packet management. Library is splitted into several parts: More...
Collaboration diagram for Packet2 library:
##### Modules
|  | Chain |
|  | Chain mode related functions of libpacket2. |
|  | Types |
|  | Structures and enums used in libpacket2. |
|  | Utils |
|  | Useful functions and examples for libpacket2. |
|  | VIF |
|  | VIF related functions of libpacket2. |
##### Functions
| packet2_t * | packet2_create (u16 qwords, enum Packet2Type type, enum Packet2Mode mode, u8 tte) |
| packet2_t * | packet2_create_from (qword_t *base, qword_t *next, u16 qwords, enum Packet2Type type, enum Packet2Mode mode, u8 tte) |
| void | packet2_free (packet2_t *packet2) |
| void | packet2_reset (packet2_t *packet2, u8 clear_mem) |
| static void | packet2_update (packet2_t *packet2, qword_t *qw) |
| static void | packet2_advance_next (packet2_t *packet2, u32 i) |
| static void | packet2_add_u128 (packet2_t *packet2, const u128 val) |
| static void | packet2_add_s64 (packet2_t *packet2, const s64 val) |
| static void | packet2_add_2x_s64 (packet2_t *packet2, const s64 v1, const s64 v2) |
| static void | packet2_add_s128 (packet2_t *packet2, const s128 val) |
| static void | packet2_add_u64 (packet2_t *packet2, const u64 val) |
| static void | packet2_add_u32 (packet2_t *packet2, const u32 val) |
| static void | packet2_add_s32 (packet2_t *packet2, const s32 val) |
| static void | packet2_add_float (packet2_t *packet2, const float val) |
| static void | packet2_add_data (packet2_t *packet2, void *t_data, u32 t_size) |
| static void | packet2_pad96 (packet2_t *packet2, const u32 val) |
| static void | packet2_pad128 (packet2_t *packet2, const u32 val) |
| void | packet2_print (packet2_t *packet2, u32 qw_count) |
| void | packet2_print_qw_count (packet2_t *packet2) |
| void | packet2_add (packet2_t *a, packet2_t *b) |
| static u32 | packet2_get_qw_count (packet2_t *packet2) |
| static u8 | packet2_doesnt_have_even_number_of_quads (packet2_t *packet2) |
| static u8 | packet2_is_dma_tag_opened (packet2_t *packet2) |
| static u8 | packet2_is_vif_code_opened (packet2_t *packet2) |
##### Detailed Description
Successor of packet_t. Main goal of this library is to create simple API for packet management. Library is splitted into several parts:
- This - core functionality of libpacket2
- "_types" - Enums and structures used in libpacket2
- "_chain" - DMA tags
- "_vif" - VU related
- "_utils" - useful functions, and examples
##### Function Documentation
##### ◆ packet2_create()
| packet2_t* packet2_create | ( | u16 | qwords, |
|  |  | enum Packet2Type | type, |
|  |  | enum Packet2Mode | mode, |
|  |  | u8 | tte |
|  | ) |  |  |
#include <ee/packet2/include/packet2.h>
Allocate new packet2.
**Parameters:** qwordsMaximum data size in qwords (128bit). typeMemory mapping type. modePacket mode. Normal or chain. tteTag transfer enable. Used only for CHAIN mode! If >0 transfer tag is set during packet sending and add_dma_tag() (so also every open_tag()) will move buffer by DWORD, so remember to align memory!
**Returns:** Pointer to packet2 on success or NULL if memory allocation fail.
Definition at line 25 of file packet2.c.
##### ◆ packet2_create_from()
| packet2_t* packet2_create_from | ( | qword_t * | base, |
|  |  | qword_t * | next, |
|  |  | u16 | qwords, |
|  |  | enum Packet2Type | type, |
|  |  | enum Packet2Mode | mode, |
|  |  | u8 | tte |
|  | ) |  |  |
#include <ee/packet2/include/packet2.h>
Create new packet2 with given data pointer.
**Parameters:** basePointer to base (start of buffer). nextPointer to next (current position of buffer). qwordsMaximum data size in qwords (128bit). typeMemory mapping type. modePacket mode. Normal or chain (so also vif/vu). tteTag transfer enable. Used only for CHAIN mode! If >0 transfer tag is set during packet sending and add_dma_tag() (so also every open_tag()) will move buffer by DWORD, so remember to align memory!
**Returns:** Pointer to packet2 on success or NULL if memory allocation fail.
Definition at line 60 of file packet2.c.
##### ◆ packet2_free()
| void packet2_free | ( | packet2_t * | packet2 | ) |  |
#include <ee/packet2/include/packet2.h>
Free packet2 memory.
**Parameters:** packet2Pointer to packet2.
Definition at line 81 of file packet2.c.
##### ◆ packet2_reset()
| void packet2_reset | ( | packet2_t * | packet2, |
|  |  | u8 | clear_mem |
|  | ) |  |  |
#include <ee/packet2/include/packet2.h>
Reset packet. Move next pointer back to base pointer, Make all "openedAt" vars to NULL Do memset on data if required.
**Parameters:** packet2Pointer to packet. clear_memIf >0, data is cleared via memset(). SLOW!
Definition at line 88 of file packet2.c.
References packet2_t::next, and packet2_t::vif_code_opened_at.
##### ◆ packet2_update()
| static void packet2_update ( packet2_t * packet2, qword_t * qw ) | inlinestatic |
#include <ee/packet2/include/packet2.h>
Update current position of packet buffer. Useful with drawlib functions.
Definition at line 89 of file packet2.h.
References packet2_t::next.
##### ◆ packet2_advance_next()
| static void packet2_advance_next ( packet2_t * packet2, u32 i ) | inlinestatic |
#include <ee/packet2/include/packet2.h>
Move "next" pointer forward.
Definition at line 96 of file packet2.h.
References packet2_t::next.
##### ◆ packet2_add_s64()
| static void packet2_add_s64 ( packet2_t * packet2, const s64 val ) | inlinestatic |
#include <ee/packet2/include/packet2.h>
**Note:** Alignment alert. Size of dword (1/2)
Definition at line 108 of file packet2.h.
##### ◆ packet2_add_u64()
| static void packet2_add_u64 ( packet2_t * packet2, const u64 val ) | inlinestatic |
#include <ee/packet2/include/packet2.h>
**Note:** Alignment alert. Size of dword (1/2)
Definition at line 127 of file packet2.h.
##### ◆ packet2_add_u32()
| static void packet2_add_u32 ( packet2_t * packet2, const u32 val ) | inlinestatic |
#include <ee/packet2/include/packet2.h>
**Note:** Alignment alert. Size of word (1/4)
Definition at line 134 of file packet2.h.
##### ◆ packet2_add_s32()
| static void packet2_add_s32 ( packet2_t * packet2, const s32 val ) | inlinestatic |
#include <ee/packet2/include/packet2.h>
**Note:** Alignment alert. Size of word (1/4)
Definition at line 141 of file packet2.h.
##### ◆ packet2_add_float()
| static void packet2_add_float ( packet2_t * packet2, const float val ) | inlinestatic |
#include <ee/packet2/include/packet2.h>
**Note:** Alignment alert. Size of word (1/4)
Definition at line 148 of file packet2.h.
##### ◆ packet2_pad96()
| static void packet2_pad96 ( packet2_t * packet2, const u32 val ) | inlinestatic |
#include <ee/packet2/include/packet2.h>
Fill to align to 96bits
Definition at line 164 of file packet2.h.
Referenced by packet2_vif_pad96().
##### ◆ packet2_pad128()
| static void packet2_pad128 ( packet2_t * packet2, const u32 val ) | inlinestatic |
#include <ee/packet2/include/packet2.h>
Fill to align to 128bits
Definition at line 173 of file packet2.h.
Referenced by packet2_vif_pad128().
##### ◆ packet2_print()
| void packet2_print | ( | packet2_t * | packet2, |
|  |  | u32 | qw_count |
|  | ) |  |  |
#include <ee/packet2/include/packet2.h>
Print data of packet.
**Parameters:** packet2Pointer to packet. clear_memCount of qwords, type 0 for all.
Definition at line 108 of file packet2.c.
##### ◆ packet2_print_qw_count()
| void packet2_print_qw_count | ( | packet2_t * | packet2 | ) |  |
#include <ee/packet2/include/packet2.h>
Print amount of qwords of packet.
**Parameters:** packet2Pointer to packet.
Definition at line 127 of file packet2.c.
##### ◆ packet2_add()
| void packet2_add | ( | packet2_t * | a, |
|  |  | packet2_t * | b |
|  | ) |  |  |
#include <ee/packet2/include/packet2.h>
Copy data from b packet into a packet with memcpy()
Definition at line 101 of file packet2.c.
References packet2_t::max_qwords_count, and packet2_get_qw_count().
##### ◆ packet2_get_qw_count()
| static u32 packet2_get_qw_count ( packet2_t * packet2) | inlinestatic |
#include <ee/packet2/include/packet2.h>
Returns count of added qwords into packet.
Definition at line 200 of file packet2.h.
References packet2_t::next.
Referenced by packet2_add().
##### ◆ packet2_doesnt_have_even_number_of_quads()
| static u8 packet2_doesnt_have_even_number_of_quads ( packet2_t * packet2) | inlinestatic |
#include <ee/packet2/include/packet2.h>
True if packet doesnt have even number of quads.
Definition at line 203 of file packet2.h.
References packet2_t::next.
##### ◆ packet2_is_dma_tag_opened()
| static u8 packet2_is_dma_tag_opened ( packet2_t * packet2) | inlinestatic |
#include <ee/packet2/include/packet2.h>
True if dma tag is opened.
Definition at line 206 of file packet2.h.
References packet2_t::tag_opened_at.
##### ◆ packet2_is_vif_code_opened()
| static u8 packet2_is_vif_code_opened ( packet2_t * packet2) | inlinestatic |
#include <ee/packet2/include/packet2.h>
True if DIRECT/UNPACK is opened.
Definition at line 209 of file packet2.h.
References packet2_t::vif_code_opened_at.

---

## ChainPacket2 library

Page: <https://ps2dev.github.io/ps2sdk/group__packet2__chain.html>

Chain mode related functions of libpacket2. More...
Collaboration diagram for Chain:
##### Macros
| #define | PACKET2_COUNT_QWC 1 << 16 |
##### Functions
| static void | packet2_chain_set_dma_tag (dma_tag_t *tag, u32 qwc, u32 pce, u32 id, u8 irq, const u128 *addr, u8 spr) |
| static void | packet2_chain_add_dma_tag (packet2_t *packet2, u32 qwc, u32 pce, enum DmaTagType id, u8 irq, const u128 *addr, u8 spr) |
| static void | packet2_chain_close_tag (packet2_t *packet2) |
| static void | packet2_chain_open_cnt (packet2_t *packet2, u8 irq, u32 pce, u8 spr) |
| static void | packet2_chain_open_end (packet2_t *packet2, u8 irq, u32 pce) |
| static void | packet2_chain_ref (packet2_t *packet2, const void *ref_data, u32 qw_length, u8 irq, u8 spr, u32 pce) |
| static void | packet2_chain_next (packet2_t *packet2, const dma_tag_t *next_tag, u8 irq, u8 spr, u32 pce) |
| static void | packet2_chain_refs (packet2_t *packet2, const void *ref_data, u32 qw_length, u8 irq, u8 spr, u32 pce) |
| static void | packet2_chain_refe (packet2_t *packet2, const void *ref_data, u32 qw_length, u8 irq, u8 spr, u32 pce) |
| static void | packet2_chain_call (packet2_t *packet2, const void *next_tag, u8 irq, u8 spr, u32 pce) |
| static void | packet2_chain_ret (packet2_t *packet2, u8 irq, u32 pce) |
##### Detailed Description
Chain mode related functions of libpacket2.
##### Function Documentation
##### ◆ packet2_chain_set_dma_tag()
| static void packet2_chain_set_dma_tag ( dma_tag_t * tag, u32 qwc, u32 pce, u32 id, u8 irq, const u128 * addr, u8 spr ) | inlinestatic |
#include <ee/packet2/include/packet2_chain.h>
Set dma tag. For more details, check description of dma_tag_t.
**Parameters:** tagPointer to DMA tag to set. qwcQword count. pcePriority Control Enable. 0 by default. idTag ID. irqInterrupt Request. False by default. addrAddress. sprMemory/SPR Selection. False by default.
Definition at line 48 of file packet2_chain.h.
##### ◆ packet2_chain_add_dma_tag()
| static void packet2_chain_add_dma_tag ( packet2_t * packet2, u32 qwc, u32 pce, enum DmaTagType id, u8 irq, const u128 * addr, u8 spr ) | inlinestatic |
#include <ee/packet2/include/packet2_chain.h>
Add dma tag. For more details, check description of dma_tag_t. Will move current buffer position by: DWORD if packet->tte == true, QWORD if packet->tte == false
**Parameters:** packet2Pointer to packet. qwcQword count. If you want to use packet2_chain_close_tag(), and count qwords automatically, set value to PACKET2_COUNT_QWC. pcePriority Control Enable. 0 by default. idTag ID. irqInterrupt Request. False by default. addrAddress. sprMemory/SPR Selection. False by default.
Definition at line 74 of file packet2_chain.h.
##### ◆ packet2_chain_close_tag()
| static void packet2_chain_close_tag ( packet2_t * packet2) | inlinestatic |
#include <ee/packet2/include/packet2_chain.h>
Close dma tag. In reality, get back to pointer "tag_opened_at" and fix qwc value.
**Parameters:** packet2Pointer to packet.
Definition at line 100 of file packet2_chain.h.
References packet2_t::tag_opened_at.
Referenced by packet2_utils_vu_add_continue_program(), packet2_utils_vu_add_end_tag(), and packet2_utils_vu_close_unpack().
##### ◆ packet2_chain_open_cnt()
| static void packet2_chain_open_cnt ( packet2_t * packet2, u8 irq, u32 pce, u8 spr ) | inlinestatic |
#include <ee/packet2/include/packet2_chain.h>
Add CNT tag.
**Note:** packet2_chain_close_tag() required. Qwords are counted automatically. For more details, check description of dma_tag_t.
**Parameters:** packet2Pointer to packet. irqInterrupt Request. False by default. pcePriority Control Enable. 0 by default. sprMemory/SPR Selection. False by default.
Definition at line 122 of file packet2_chain.h.
Referenced by packet2_utils_vu_add_continue_program(), and packet2_utils_vu_open_unpack().
##### ◆ packet2_chain_open_end()
| static void packet2_chain_open_end ( packet2_t * packet2, u8 irq, u32 pce ) | inlinestatic |
#include <ee/packet2/include/packet2_chain.h>
Add END tag.
**Note:** packet2_chain_close_tag() required. Qwords are counted automatically. For more details, check description of dma_tag_t.
  Don't forget about close_tag()!
**Parameters:** packet2Pointer to packet. irqInterrupt Request. False by default. pcePriority Control Enable. 0 by default.
Definition at line 137 of file packet2_chain.h.
Referenced by packet2_utils_vu_add_end_tag().
##### ◆ packet2_chain_ref()
| static void packet2_chain_ref ( packet2_t * packet2, const void * ref_data, u32 qw_length, u8 irq, u8 spr, u32 pce ) | inlinestatic |
#include <ee/packet2/include/packet2_chain.h>
Add REF tag.
**Note:** Qwords are NOT counted automatically, so there is NO need to use packet2_chain_close_tag(); For more details, check description of dma_tag_t.
**Parameters:** packet2Pointer to packet. ref_dataPointer to data. qw_lengthSize of data in qwords. irqInterrupt Request. False by default. sprMemory/SPR Selection. False by default. pcePriority Control Enable. 0 by default.
Definition at line 154 of file packet2_chain.h.
Referenced by packet2_utils_vu_add_unpack_data(), and packet2_vif_add_micro_program().
##### ◆ packet2_chain_next()
| static void packet2_chain_next ( packet2_t * packet2, const dma_tag_t * next_tag, u8 irq, u8 spr, u32 pce ) | inlinestatic |
#include <ee/packet2/include/packet2_chain.h>
Add NEXT tag.
**Note:** packet2_chain_close_tag() required. Qwords are counted automatically. For more details, check description of dma_tag_t.
**Parameters:** next_tagPointer to next tag. irqInterrupt Request. False by default. sprMemory/SPR Selection. False by default. pcePriority Control Enable. 0 by default.
Definition at line 170 of file packet2_chain.h.
##### ◆ packet2_chain_refs()
| static void packet2_chain_refs ( packet2_t * packet2, const void * ref_data, u32 qw_length, u8 irq, u8 spr, u32 pce ) | inlinestatic |
#include <ee/packet2/include/packet2_chain.h>
Add REFS tag.
**Note:** Qwords are NOT counted automatically, so there is NO need to use packet2_chain_close_tag(); For more details, check description of dma_tag_t.
**Parameters:** packet2Pointer to packet. ref_dataPointer to data. qw_lengthSize of data in qwords. irqInterrupt Request. False by default. sprMemory/SPR Selection. False by default. pcePriority Control Enable. 0 by default.
Definition at line 188 of file packet2_chain.h.
##### ◆ packet2_chain_refe()
| static void packet2_chain_refe ( packet2_t * packet2, const void * ref_data, u32 qw_length, u8 irq, u8 spr, u32 pce ) | inlinestatic |
#include <ee/packet2/include/packet2_chain.h>
Add REFE tag.
**Note:** Qwords are NOT counted automatically, so there is NO need to use packet2_chain_close_tag(); For more details, check description of dma_tag_t.
**Parameters:** packet2Pointer to packet. ref_dataPointer to data. qw_lengthSize of data in qwords. irqInterrupt Request. False by default. sprMemory/SPR Selection. False by default. pcePriority Control Enable. 0 by default.
Definition at line 206 of file packet2_chain.h.
##### ◆ packet2_chain_call()
| static void packet2_chain_call ( packet2_t * packet2, const void * next_tag, u8 irq, u8 spr, u32 pce ) | inlinestatic |
#include <ee/packet2/include/packet2_chain.h>
Add CALL tag.
**Note:** packet2_chain_close_tag() required. Qwords are counted automatically. For more details, check description of dma_tag_t.
**Parameters:** packet2Pointer to packet. next_tagPointer to next tag. irqInterrupt Request. False by default. sprMemory/SPR Selection. False by default. pcePriority Control Enable. 0 by default.
Definition at line 223 of file packet2_chain.h.
##### ◆ packet2_chain_ret()
| static void packet2_chain_ret ( packet2_t * packet2, u8 irq, u32 pce ) | inlinestatic |
#include <ee/packet2/include/packet2_chain.h>
Add RET tag.
**Note:** packet2_chain_close_tag() required. Qwords are counted automatically. For more details, check description of dma_tag_t.
**Parameters:** packet2Pointer to packet. irqInterrupt Request. False by default. pcePriority Control Enable. 0 by default.
Definition at line 238 of file packet2_chain.h.

---

## TypesPacket2 library

Page: <https://ps2dev.github.io/ps2sdk/group__packet2__types.html>

Structures and enums used in libpacket2. More...
Collaboration diagram for Types:
##### Enumerations
| enum | Packet2Mode { P2_MODE_NORMAL = 0, P2_MODE_CHAIN = 1 } |
| enum | Packet2Type { P2_TYPE_NORMAL = 0x00000000, P2_TYPE_UNCACHED = 0x20000000, P2_TYPE_UNCACHED_ACCL = 0x30000000, P2_TYPE_SPRAM = 0x70000000 } |
| enum | DmaTagType { P2_DMA_TAG_REFE = 0, P2_DMA_TAG_CNT = 1, P2_DMA_TAG_NEXT = 2, P2_DMA_TAG_REF = 3, P2_DMA_TAG_REFS = 4, P2_DMA_TAG_CALL = 5, P2_DMA_TAG_RET = 6, P2_DMA_TAG_END = 7 } |
| enum | UnpackMode { P2_UNPACK_S_32 = 0x00, P2_UNPACK_S_16 = 0x01, P2_UNPACK_S_8 = 0x02, P2_UNPACK_V2_32 = 0x04, P2_UNPACK_V2_16 = 0x05, P2_UNPACK_V2_8 = 0x06, P2_UNPACK_V3_32 = 0x08, P2_UNPACK_V3_16 = 0x09, P2_UNPACK_V3_8 = 0x0A, P2_UNPACK_V4_32 = 0x0C, P2_UNPACK_V4_16 = 0x0D, P2_UNPACK_V4_8 = 0x0E, P2_UNPACK_V4_5 = 0x0F } |
| enum | VIFOpcode { P2_VIF_NOP = 0, P2_VIF_STCYCL = 1, P2_VIF_OFFSET = 2, P2_VIF_BASE = 3, P2_VIF_ITOP = 4, P2_VIF_STMOD = 5, P2_VIF_MSKPATH3 = 6, P2_VIF_MARK = 7, P2_VIF_FLUSHE = 16, P2_VIF_FLUSH = 17, P2_VIF_FLUSHA = 19, P2_VIF_MSCAL = 20, P2_VIF_MSCNT = 23, P2_VIF_MSCALF = 21, P2_VIF_STMASK = 32, P2_VIF_STROW = 48, P2_VIF_STCOL = 49, P2_VIF_MPG = 74, P2_VIF_DIRECT = 80, P2_VIF_DIRECTHL = 81 } |
##### Detailed Description
Structures and enums used in libpacket2.
##### Enumeration Type Documentation
##### ◆ Packet2Mode
| enum Packet2Mode |
#include <ee/packet2/include/packet2_types.h>
Two modes are commonly used with the DMA Controller (DMAC): normal mode and chain mode. In normal mode, transfers are issued one at a time. In chain mode, a series of transfers are issued simultaneously by initiating a transfer that contains "DMA Tags", which in turn contains instructions for further transfers. You will probably use chain mode for the majority of your transfers.
Definition at line 31 of file packet2_types.h.
##### ◆ Packet2Type
| enum Packet2Type |
#include <ee/packet2/include/packet2_types.h>
Types of memory mapping.
| Enumerator |
| P2_TYPE_NORMAL | Normal. |
| P2_TYPE_UNCACHED | Uncached. |
| P2_TYPE_UNCACHED_ACCL | Uncached accelerated. |
| P2_TYPE_SPRAM | Scratchpad memory. |
Definition at line 38 of file packet2_types.h.
##### ◆ DmaTagType
| enum DmaTagType |
#include <ee/packet2/include/packet2_types.h>
DMA tag types
| Enumerator |
| P2_DMA_TAG_REFE | Transfers the QWC qword from the ADDR field, clears the Dn_CHCR.STR to 0, and ends transfer. |
| P2_DMA_TAG_CNT | Transfers the QWC qword following the tag and reads the succeeding qword as the next tag. |
| P2_DMA_TAG_NEXT | Transfers the QWC qword following the tag and reads the qword of the ADDR field as the next tag. |
| P2_DMA_TAG_REF | Transfers the QWC qword from the ADDR field and reads the qword following the tag as the next tag. |
| P2_DMA_TAG_REFS | Transfers the QWC qword from the ADDR field while controlling stalls and reads the qword following the tag as the next tag. NoteEffective only on the VIF1, GIF, and SIF1 channels. |
| P2_DMA_TAG_CALL | Transfers the QWC qword following the tag, pushes the next field into the Dn_ASR register, and reads the qword of the ADDR field as the next tag. NoteEffective only on the VIF0, VIF1, and GIF channels. Addresses can be pushed up to 2 levels |
| P2_DMA_TAG_RET | Transfers the QWC qword following the tag and reads the qword of the field popped from the Dn_ASR register as the next tag. Transfers the QWC qword following the tag, clears the Dn_CHCR.STR to 0, and ends transfer when there is no pushed address. NoteEffective only on the VIF0, VIF1, and GIF channels. |
| P2_DMA_TAG_END | Transfers the QWC qword following the tag, clears the Dn_CHCR.STR to 0, and ends transfer. |
Definition at line 51 of file packet2_types.h.
##### ◆ UnpackMode
| enum UnpackMode |
#include <ee/packet2/include/packet2_types.h>
Unpack modes. V2 = 2 dimensions, S = Single = 1 dimension _32 = 32 bits of data length.
Definition at line 131 of file packet2_types.h.
##### ◆ VIFOpcode
| enum VIFOpcode |
#include <ee/packet2/include/packet2_types.h>
VIF opcodes.
| Enumerator |
| P2_VIF_NOP | No operation. No operation is performed. NOP is used to adjust the data alignment in the VIF packet. |
| P2_VIF_STCYCL | Sets write recycle. STCYCL writes the value of the IMMEDIATE field to the VIFn_CYCLE register. |
| P2_VIF_OFFSET | Sets the double buffer offset. OFFSET writes the lower 10 bits of the IMMEDIATE field to the VIF1_OFST register. At the same time, the DBF flag of the VIF1_STAT register is cleared to 0, and the VIF1_BASE register value is set to the VIF1_TOPS. That is, the pointer for the double buffer points to the BASE. |
| P2_VIF_BASE | Sets the base address of the double buffer. BASE writes the lower 10 bits of the IMMEDIATE field to the VIF1_BASE register. These bits become the base address of the double buffers. |
| P2_VIF_ITOP | Sets the data pointer. ITOP writes the lower 10 bits of the IMMEDIATE field to the VIFn_ITOPS register. This value is read from the VU by the XITOP instruction. |
| P2_VIF_STMOD | Sets the addition decompression mode. STMOD writes the lower 2 bits of the IMMEDIATE field to the VIFn_MODE register. This becomes the addition decompression mode setting. |
| P2_VIF_MSKPATH3 | Sets the PATH3 mask. MSKPATH3 enables/disables transfer processing via the GIF PATH3. The setting of this register applies to the next data block or later. |
| P2_VIF_MARK | Sets the MARK value. MARK writes the value of the IMMEDIATE field to the VIFn_MARK register. By properly setting the MARK value, it becomes possible to use this value for synchronization with the EE Core and debugging. |
| P2_VIF_FLUSHE | Waits for end of the microprogram. FLUSHE waits for the state in which the microprogram in VU0/VU1 has been ended. |
| P2_VIF_FLUSH | Waits for end of the microprogram. FLUSH waits for the state in which transfers to the GIF from PATH1 and PATH2 have been ended after end of microprogram in VU1. FLUSH does not wait for the end of the transfer via PATH1 by the XGKICK instruction with the E bit. |
| P2_VIF_FLUSHA | Waits for end of the microprogram. FLUSHA waits for the state in which there is no transfer request from PATH3 after the end of micro program in VU1 and end of transfer to the GIF from PATH1 and PATH2. |
| P2_VIF_MSCAL | Activates the microprogram. MSCAL waits for the end of the microprogram under execution and activates the micro program with the value of the IMMEDIATE field as the starting address. |
| P2_VIF_MSCNT | Activates the microprogram. MSCNT waits for the end of the microprogram under execution and executes the next microprogram from the address following the most recently ended one in the PC (program counter). |
| P2_VIF_MSCALF | Activates the microprogram. MSCALF waits for the end of both the microprogram and the GIF(PATH1/PATH2) transfer and executes the microprogram with the value of the IMMEDIATE field as the starting address. |
| P2_VIF_STMASK | Sets the data mask pattern. STMASK stores the next 1 word of data in the VIFn_MASK register. This data becomes the mask pattern of the write data. |
| P2_VIF_STROW | Sets the filling data. STROW stores the following 4 words of data in the VIFn_R0 - VIFn_R3 registers. These are used as filling data when decompressed by the VIFcode UNPACK. |
| P2_VIF_STCOL | Sets the filling data. STCOL stores the following 4 words of data in the VIFn_C0 - VIFn_C3 registers. These are used as filling data when decompressed by the VIFcode UNPACK. |
| P2_VIF_MPG | Transfers the microprogram. MPG waits for the end of the microprogram and transfers the following NUM pieces of 64-bit data. (microinstruction code) to the MicroMem address shown by the IMMEDIATE field. |
| P2_VIF_DIRECT | Transfers data to the GIF(GS). DIRECT transfers the following IMMEDIATE pieces of 128-bit data to the GS via GIF PATH2. It is necessary to put the appropriate GIFtag to the data. |
| P2_VIF_DIRECTHL | Transfers data to the GIF(GS). DIRECTHL transfers the following IMMEDIATE pieces of 128-bit data to the GS via GIF PATH2. The appropriate GIFtag must be attached to the data. Interruption of PATH3 IMAGE mode data does not occur during the data transfer via PATH2 by DIRECTHL. Moreover, when the IMAGE mode data is being transferred via PATH3, DIRECTHL stalls until the end of the transfer. |
Definition at line 149 of file packet2_types.h.

---

## UtilsPacket2 library

Page: <https://ps2dev.github.io/ps2sdk/group__packet2__utils.html>

Useful functions and examples for libpacket2. More...
Collaboration diagram for Utils:
##### Macros
| #define | VU_GS_PRIM(PRIM, IIP, TME, FGE, ABE, AA1, FST, CTXT, FIX) (u128)(((FIX << 10) | (CTXT << 9) | (FST << 8) | (AA1 << 7) | (ABE << 6) | (FGE << 5) | (TME << 4) | (IIP << 3) | (PRIM))) |
| #define | VU_GS_GIFTAG(NLOOP, EOP, PRE, PRIM, FLG, NREG) (((u64)(NREG) << 60) | ((u64)(FLG) << 58) | ((u64)(PRIM) << 47) | ((u64)(PRE) << 46) | (EOP << 15) | (NLOOP << 0)) |
##### Functions
| static void | packet2_utils_vu_add_double_buffer (packet2_t *packet2, u16 base, u16 offset) |
| static void | packet2_utils_vu_add_unpack_data (packet2_t *packet2, u32 t_dest_address, void *t_data, u32 t_size, u8 t_use_top) |
| static void | packet2_utils_vu_open_unpack (packet2_t *packet2, u32 t_dest_address, u8 t_use_top) |
| static u32 | packet2_utils_vu_close_unpack (packet2_t *packet2) |
| static void | packet2_utils_vu_add_continue_program (packet2_t *packet2) |
| static void | packet2_utils_vu_add_start_program (packet2_t *packet2, u32 addr) |
| static void | packet2_utils_vu_add_end_tag (packet2_t *packet2) |
| static u32 | packet2_utils_get_packet_size_for_program (u32 *start, u32 *end) |
| static void | packet2_utils_gif_add_set (packet2_t *packet2, u32 loops_count) |
| static void | packet2_utils_gs_add_lod (packet2_t *packet2, lod_t *lod) |
| static void | packet2_utils_gs_add_texbuff_clut (packet2_t *packet2, texbuffer_t *texbuff, clutbuffer_t *clut) |
| static void | packet2_utils_gs_add_draw_finish_giftag (packet2_t *packet2) |
| static void | packet2_utils_gs_add_prim_giftag (packet2_t *packet2, prim_t *prim, u32 loops_count, u32 nreg, u8 nreg_count, u8 context) |
##### Detailed Description
Useful functions and examples for libpacket2.
##### Function Documentation
##### ◆ packet2_utils_vu_add_double_buffer()
| static void packet2_utils_vu_add_double_buffer ( packet2_t * packet2, u16 base, u16 offset ) | inlinestatic |
#include <ee/packet2/include/packet2_utils.h>
Add VU buffers size settings.
**Parameters:** t_baseBase address (qw) t_offsetOffset address (qw)
Definition at line 49 of file packet2_utils.h.
##### ◆ packet2_utils_vu_add_unpack_data()
| static void packet2_utils_vu_add_unpack_data ( packet2_t * packet2, u32 t_dest_address, void * t_data, u32 t_size, u8 t_use_top ) | inlinestatic |
#include <ee/packet2/include/packet2_utils.h>
Add data via REF tag and UNPACK. Please be sure that data is aligned, and there is no any open UNPACK/DIRECT.
**Parameters:** packet2Pointer to packet2. t_dest_addressDestination address. t_dataData pointer. t_sizeSize in quadwords. t_use_topUnpack to current double buffer?
Definition at line 67 of file packet2_utils.h.
References packet2_chain_ref(), packet2_vif_open_unpack(), and packet2_vif_stcycl().
##### ◆ packet2_utils_vu_open_unpack()
| static void packet2_utils_vu_open_unpack ( packet2_t * packet2, u32 t_dest_address, u8 t_use_top ) | inlinestatic |
#include <ee/packet2/include/packet2_utils.h>
Open CNT tag + VU unpack.
**Parameters:** packet2Pointer to packet2. t_dest_addressDestination address. t_use_topUnpack to current double buffer?
Definition at line 81 of file packet2_utils.h.
References packet2_chain_open_cnt(), packet2_vif_open_unpack(), and packet2_vif_stcycl().
##### ◆ packet2_utils_vu_close_unpack()
| static u32 packet2_utils_vu_close_unpack ( packet2_t * packet2) | inlinestatic |
#include <ee/packet2/include/packet2_utils.h>
Close CNT tag + VU unpack.
**Returns:** Unpacked qwords count
Definition at line 92 of file packet2_utils.h.
References packet2_chain_close_tag(), packet2_vif_close_unpack_auto(), and packet2_vif_pad128().
##### ◆ packet2_utils_vu_add_continue_program()
| static void packet2_utils_vu_add_continue_program ( packet2_t * packet2) | inlinestatic |
#include <ee/packet2/include/packet2_utils.h>
Continue VU micro program (from –cont line). Adds FLUSH and MSCNT VIF opcodes.
Definition at line 103 of file packet2_utils.h.
References packet2_chain_close_tag(), packet2_chain_open_cnt(), packet2_vif_flush(), and packet2_vif_mscnt().
##### ◆ packet2_utils_vu_add_start_program()
| static void packet2_utils_vu_add_start_program ( packet2_t * packet2, u32 addr ) | inlinestatic |
#include <ee/packet2/include/packet2_utils.h>
Start VU micro program. Adds FLUSH and MSCAL VIF opcodes.
Definition at line 115 of file packet2_utils.h.
##### ◆ packet2_utils_vu_add_end_tag()
| static void packet2_utils_vu_add_end_tag ( packet2_t * packet2) | inlinestatic |
#include <ee/packet2/include/packet2_utils.h>
Add aligned END tag (with nops).
Definition at line 124 of file packet2_utils.h.
References packet2_chain_close_tag(), packet2_chain_open_end(), and packet2_vif_nop().
##### ◆ packet2_utils_get_packet_size_for_program()
| static u32 packet2_utils_get_packet_size_for_program ( u32 * start, u32 * end ) | inlinestatic |
#include <ee/packet2/include/packet2_utils.h>
Get program size in qws
**Parameters:** startStart address. endEnd address.
**Returns:** Packet size in qws for specified program (instructions/256 + 1qw for tolerance).
Definition at line 138 of file packet2_utils.h.
References count.
##### ◆ packet2_utils_gif_add_set()
| static void packet2_utils_gif_add_set ( packet2_t * packet2, u32 loops_count ) | inlinestatic |
#include <ee/packet2/include/packet2_utils.h>
Add set GIFTag which will be sent from VU1 via XGKICK instruction.
**Parameters:** packet2Pointer to packet2. loops_countHow many GIF tags there will be?
Definition at line 157 of file packet2_utils.h.
##### ◆ packet2_utils_gs_add_lod()
| static void packet2_utils_gs_add_lod ( packet2_t * packet2, lod_t * lod ) | inlinestatic |
#include <ee/packet2/include/packet2_utils.h>
Add lod GIFTag which will be sent from VU1 via XGKICK instruction.
**Parameters:** packet2Pointer to packet2. lodPointer to lod settings.
Definition at line 172 of file packet2_utils.h.
##### ◆ packet2_utils_gs_add_texbuff_clut()
| static void packet2_utils_gs_add_texbuff_clut ( packet2_t * packet2, texbuffer_t * texbuff, clutbuffer_t * clut ) | inlinestatic |
#include <ee/packet2/include/packet2_utils.h>
Add texture buffer / clut GIFTag which will be sent from VU1 via XGKICK instruction.
**Parameters:** packet2Pointer to packet2. texbuffPointer to texture buffer. clutPointer to clut buffer.
Definition at line 194 of file packet2_utils.h.
##### ◆ packet2_utils_gs_add_draw_finish_giftag()
| static void packet2_utils_gs_add_draw_finish_giftag ( packet2_t * packet2) | inlinestatic |
#include <ee/packet2/include/packet2_utils.h>
Add draw finish event GIFTag which will be sent from VU1 via XGKICK instruction. Used for synchronization via draw_wait_finish()
**Parameters:** packet2Pointer to packet2.
Definition at line 220 of file packet2_utils.h.
##### ◆ packet2_utils_gs_add_prim_giftag()
| static void packet2_utils_gs_add_prim_giftag ( packet2_t * packet2, prim_t * prim, u32 loops_count, u32 nreg, u8 nreg_count, u8 context ) | inlinestatic |
#include <ee/packet2/include/packet2_utils.h>
Add drawing (prim) GIFTag which will be sent from VU1 via XGKICK instruction.
**Parameters:** packet2Pointer to packet2. primPointer to prim settings. loops_countGIF tag loops count. nregWhat types of data we will use? nreg_countHow many types there are in nreg? contextDrawing context
Definition at line 235 of file packet2_utils.h.

---

## VIFPacket2 library

Page: <https://ps2dev.github.io/ps2sdk/group__packet2__vif.html>

VIF related functions of libpacket2. More...
Collaboration diagram for VIF:
##### Macros
| #define | MAKE_VIF_CODE(_immediate, _num, _cmd, _irq) ((u32)(_immediate) | ((u32)(_num) << 16) | ((u32)(_cmd) << 24) | ((u32)(_irq) << 31)) |
##### Functions
| static void | packet2_vif_open_unpack (packet2_t *packet2, enum UnpackMode mode, u32 vuAddr, u8 dblBuffered, u8 masked, u8 usigned, u8 irq) |
| static void | packet2_vif_close_unpack_manual (packet2_t *packet2, u32 unpack_num) |
| u32 | packet2_vif_close_unpack_auto (packet2_t *packet2, u32 wl, u32 cl) |
| static void | packet2_vif_open_direct (packet2_t *packet2, u8 irq) |
| static void | packet2_vif_close_direct_manual (packet2_t *packet2, u32 qwords) |
| static void | packet2_vif_close_direct_auto (packet2_t *packet2) |
| static void | packet2_vif_nop (packet2_t *packet2, u8 irq) |
| static void | packet2_vif_pad96 (packet2_t *packet2) |
| static void | packet2_vif_pad128 (packet2_t *packet2) |
| static void | packet2_vif_mpg (packet2_t *packet2, u32 num, u32 addr, u8 irq) |
| static void | packet2_vif_stcycl (packet2_t *packet2, u32 wl, u32 cl, u8 irq) |
| static void | packet2_vif_offset (packet2_t *packet2, u32 offset, u8 irq) |
| static void | packet2_vif_base (packet2_t *packet2, u32 base, u8 irq) |
| static void | packet2_vif_flush (packet2_t *packet2, u8 irq) |
| static void | packet2_vif_mscal (packet2_t *packet2, u32 addr, u8 irq) |
| static void | packet2_vif_mscnt (packet2_t *packet2, u8 irq) |
| static void | packet2_vif_itop (packet2_t *packet2, u32 itops, u8 irq) |
| static void | packet2_vif_stmod (packet2_t *packet2, u32 mode, u8 irq) |
| static void | packet2_vif_mskpath3 (packet2_t *packet2, u32 mask, u8 irq) |
| static void | packet2_vif_mark (packet2_t *packet2, u32 value, u8 irq) |
| static void | packet2_vif_flushe (packet2_t *packet2, u8 irq) |
| static void | packet2_vif_flusha (packet2_t *packet2, u8 irq) |
| static void | packet2_vif_mscalf (packet2_t *packet2, u32 addr, u8 irq) |
| static void | packet2_vif_stmask (packet2_t *packet2, Mask mask, u8 irq) |
| static void | packet2_vif_strow (packet2_t *packet2, const u32 *row_arr, u8 irq) |
| static void | packet2_vif_stcol (packet2_t *packet2, const u32 *col_arr, u8 irq) |
| void | packet2_vif_add_micro_program (packet2_t *packet2, u32 dest, u32 *start, u32 *end) |
##### Detailed Description
VIF related functions of libpacket2.
##### Function Documentation
##### ◆ packet2_vif_open_unpack()
| static void packet2_vif_open_unpack ( packet2_t * packet2, enum UnpackMode mode, u32 vuAddr, u8 dblBuffered, u8 masked, u8 usigned, u8 irq ) | inlinestatic |
#include <ee/packet2/include/packet2_vif.h>
Add UNPACK VIF opcode.
**Note:** packet2_vif_close_unpack() required. Qwords are counted automatically. For more details, check description of vif_code_t.
**Parameters:** packet2Pointer to packet. modeUnpack mode vuAddrMemory address (divided by 16). dblBuffered(VIF1 only) 1 - Adds VIF1_TOPS register to ADDR 0 - Does not use VIF1_TOPS register. maskedIs masked usigned1 - Unsigned - Decompress by padding 0 to the upper field 0 - Signed - Decompress by sign extension irqInterrupt Request. False by default.
Definition at line 50 of file packet2_vif.h.
Referenced by packet2_utils_vu_add_unpack_data(), and packet2_utils_vu_open_unpack().
##### ◆ packet2_vif_close_unpack_manual()
| static void packet2_vif_close_unpack_manual ( packet2_t * packet2, u32 unpack_num ) | inlinestatic |
#include <ee/packet2/include/packet2_vif.h>
Close UNPACK manually. In reality, get back to pointer "vif_code_opened_at" and fix num value with qwords counted from last packet2_vif_open_unpack().
**Parameters:** packet2Pointer to packet. unpack_numAmount of data written to the VU Mem (qwords) or MicroMem (dwords). 256 is max value!
Definition at line 68 of file packet2_vif.h.
References packet2_t::vif_code_opened_at.
##### ◆ packet2_vif_close_unpack_auto()
| u32 packet2_vif_close_unpack_auto | ( | packet2_t * | packet2, |
|  |  | u32 | wl, |
|  |  | u32 | cl |
|  | ) |  |  |
#include <ee/packet2/include/packet2_vif.h>
Close UNPACK automatically. In reality, get back to pointer "vif_code_opened_at" and fix num value with qwords counted from last packet2_vif_open_unpack().
**Parameters:** packet2Pointer to packet. wlWL Value (look at STCYCL) clCL Value (look at STCYCL)
**Returns:** Unpacked qwords count
Definition at line 34 of file packet2_vif.c.
References packet2_t::vif_code_opened_at.
Referenced by packet2_utils_vu_close_unpack().
##### ◆ packet2_vif_open_direct()
| static void packet2_vif_open_direct ( packet2_t * packet2, u8 irq ) | inlinestatic |
#include <ee/packet2/include/packet2_vif.h>
Add DIRECT VIF opcode.
**Note:** Direct must be closed via packet2_vif_close_direct_manual() or packet2_vif_close : "memory"
Definition at line 95 of file packet2_vif.h.
##### ◆ packet2_vif_close_direct_manual()
| static void packet2_vif_close_direct_manual ( packet2_t * packet2, u32 qwords ) | inlinestatic |
#include <ee/packet2/include/packet2_vif.h>
Close DIRECT manually. In reality, get back to pointer "vif_code_opened_at" and fix immediate value with given value.
**Parameters:** packet2Pointer to packet. qwordsQwords count.
Definition at line 109 of file packet2_vif.h.
References packet2_t::vif_code_opened_at.
Referenced by packet2_vif_close_direct_auto().
##### ◆ packet2_vif_close_direct_auto()
| static void packet2_vif_close_direct_auto ( packet2_t * packet2) | inlinestatic |
#include <ee/packet2/include/packet2_vif.h>
Close DIRECT automatically. In reality, get back to pointer "vif_code_opened_at" and fix immediate value with qwords counted from last packet2_vif_open_direct().
**Parameters:** packet2Pointer to packet.
Definition at line 123 of file packet2_vif.h.
References packet2_t::next, packet2_vif_close_direct_manual(), and packet2_t::vif_code_opened_at.
##### ◆ packet2_vif_nop()
| static void packet2_vif_nop ( packet2_t * packet2, u8 irq ) | inlinestatic |
#include <ee/packet2/include/packet2_vif.h>
Add NOP VIF opcode.
**Note:** Alignment alert. Size of word (1/4). For more details, check description of VIFOpcode.
**Parameters:** packet2Pointer to packet. irqInterrupt Request. False by default.
Definition at line 135 of file packet2_vif.h.
Referenced by packet2_utils_vu_add_end_tag(), and packet2_vif_add_micro_program().
##### ◆ packet2_vif_pad96()
| static void packet2_vif_pad96 ( packet2_t * packet2) | inlinestatic |
#include <ee/packet2/include/packet2_vif.h>
Fill with NOP VIF opcode to align to 96bits
**Parameters:** packet2Pointer to packet.
Definition at line 144 of file packet2_vif.h.
References packet2_pad96().
##### ◆ packet2_vif_pad128()
| static void packet2_vif_pad128 ( packet2_t * packet2) | inlinestatic |
#include <ee/packet2/include/packet2_vif.h>
Fill with NOP VIF opcode to align to 128bits
**Parameters:** packet2Pointer to packet.
Definition at line 153 of file packet2_vif.h.
References packet2_pad128().
Referenced by packet2_utils_vu_close_unpack().
##### ◆ packet2_vif_mpg()
| static void packet2_vif_mpg ( packet2_t * packet2, u32 num, u32 addr, u8 irq ) | inlinestatic |
#include <ee/packet2/include/packet2_vif.h>
Add MPG VIF opcode.
**Note:** Alignment alert. Size of word (1/4). For more details, check description of VIFOpcode.
**Parameters:** packet2Pointer to packet. numNumber of 64-bit data. addrAddress. irqInterrupt Request. False by default.
Definition at line 167 of file packet2_vif.h.
Referenced by packet2_vif_add_micro_program().
##### ◆ packet2_vif_stcycl()
| static void packet2_vif_stcycl ( packet2_t * packet2, u32 wl, u32 cl, u8 irq ) | inlinestatic |
#include <ee/packet2/include/packet2_vif.h>
Add STCYCL VIF opcode.
**Note:** Alignment alert. Size of word (1/4). For more details, check description of VIFOpcode.
**Parameters:** packet2Pointer to packet. wlWL field. clCL field. irqInterrupt Request. False by default.
Definition at line 181 of file packet2_vif.h.
Referenced by packet2_utils_vu_add_unpack_data(), and packet2_utils_vu_open_unpack().
##### ◆ packet2_vif_offset()
| static void packet2_vif_offset ( packet2_t * packet2, u32 offset, u8 irq ) | inlinestatic |
#include <ee/packet2/include/packet2_vif.h>
Add OFFSET VIF opcode.
**Note:** Alignment alert. Size of word (1/4). For more details, check description of VIFOpcode.
**Parameters:** packet2Pointer to packet. offsetOffset. BASE+OFFSET will be the address of second buffer. irqInterrupt Request. False by default.
Definition at line 194 of file packet2_vif.h.
##### ◆ packet2_vif_base()
| static void packet2_vif_base ( packet2_t * packet2, u32 base, u8 irq ) | inlinestatic |
#include <ee/packet2/include/packet2_vif.h>
Add BASE VIF opcode.
**Note:** Alignment alert. Size of word (1/4). For more details, check description of VIFOpcode.
**Parameters:** packet2Pointer to packet. baseBase address of double buffer. irqInterrupt Request. False by default.
Definition at line 207 of file packet2_vif.h.
##### ◆ packet2_vif_flush()
| static void packet2_vif_flush ( packet2_t * packet2, u8 irq ) | inlinestatic |
#include <ee/packet2/include/packet2_vif.h>
Add FLUSH VIF opcode.
**Note:** Alignment alert. Size of word (1/4). For more details, check description of VIFOpcode.
**Parameters:** packet2Pointer to packet. irqInterrupt Request. False by default.
Definition at line 219 of file packet2_vif.h.
Referenced by packet2_utils_vu_add_continue_program().
##### ◆ packet2_vif_mscal()
| static void packet2_vif_mscal ( packet2_t * packet2, u32 addr, u8 irq ) | inlinestatic |
#include <ee/packet2/include/packet2_vif.h>
Add MSCAL VIF opcode.
**Note:** Alignment alert. Size of word (1/4). For more details, check description of VIFOpcode.
**Parameters:** packet2Pointer to packet. addrStarting address. irqInterrupt Request. False by default.
Definition at line 232 of file packet2_vif.h.
##### ◆ packet2_vif_mscnt()
| static void packet2_vif_mscnt ( packet2_t * packet2, u8 irq ) | inlinestatic |
#include <ee/packet2/include/packet2_vif.h>
Add MSCNT VIF opcode.
**Note:** Alignment alert. Size of word (1/4). For more details, check description of VIFOpcode.
**Parameters:** packet2Pointer to packet. irqInterrupt Request. False by default.
Definition at line 244 of file packet2_vif.h.
Referenced by packet2_utils_vu_add_continue_program().
##### ◆ packet2_vif_itop()
| static void packet2_vif_itop ( packet2_t * packet2, u32 itops, u8 irq ) | inlinestatic |
#include <ee/packet2/include/packet2_vif.h>
Add ITOP VIF opcode.
**Note:** Alignment alert. Size of word (1/4). For more details, check description of VIFOpcode.
**Parameters:** packet2Pointer to packet. itopsValue for VU XITOP instruction. irqInterrupt Request. False by default.
Definition at line 257 of file packet2_vif.h.
##### ◆ packet2_vif_stmod()
| static void packet2_vif_stmod ( packet2_t * packet2, u32 mode, u8 irq ) | inlinestatic |
#include <ee/packet2/include/packet2_vif.h>
Add MSKPATH3 VIF opcode.
**Note:** Alignment alert. Size of word (1/4). For more details, check description of VIFOpcode.
**Parameters:** packet2Pointer to packet. modeDecompression mode. irqInterrupt Request. False by default.
Definition at line 270 of file packet2_vif.h.
##### ◆ packet2_vif_mskpath3()
| static void packet2_vif_mskpath3 ( packet2_t * packet2, u32 mask, u8 irq ) | inlinestatic |
#include <ee/packet2/include/packet2_vif.h>
Add MSKPATH3 VIF opcode.
**Note:** Alignment alert. Size of word (1/4). For more details, check description of VIFOpcode.
**Parameters:** packet2Pointer to packet. maskMask. irqInterrupt Request. False by default.
Definition at line 283 of file packet2_vif.h.
##### ◆ packet2_vif_mark()
| static void packet2_vif_mark ( packet2_t * packet2, u32 value, u8 irq ) | inlinestatic |
#include <ee/packet2/include/packet2_vif.h>
Add MARK VIF opcode.
**Note:** Alignment alert. Size of word (1/4). For more details, check description of VIFOpcode.
**Parameters:** packet2Pointer to packet. valueValue. irqInterrupt Request. False by default.
Definition at line 296 of file packet2_vif.h.
##### ◆ packet2_vif_flushe()
| static void packet2_vif_flushe ( packet2_t * packet2, u8 irq ) | inlinestatic |
#include <ee/packet2/include/packet2_vif.h>
Add FLUSHE VIF opcode.
**Note:** Alignment alert. Size of word (1/4). For more details, check description of VIFOpcode.
**Parameters:** packet2Pointer to packet. irqInterrupt Request. False by default.
Definition at line 308 of file packet2_vif.h.
##### ◆ packet2_vif_flusha()
| static void packet2_vif_flusha ( packet2_t * packet2, u8 irq ) | inlinestatic |
#include <ee/packet2/include/packet2_vif.h>
Add FLUSHA VIF opcode.
**Note:** Alignment alert. Size of word (1/4). For more details, check description of VIFOpcode.
**Parameters:** packet2Pointer to packet. irqInterrupt Request. False by default.
Definition at line 320 of file packet2_vif.h.
##### ◆ packet2_vif_mscalf()
| static void packet2_vif_mscalf ( packet2_t * packet2, u32 addr, u8 irq ) | inlinestatic |
#include <ee/packet2/include/packet2_vif.h>
Add MSCALF VIF opcode.
**Note:** Alignment alert. Size of word (1/4). For more details, check description of VIFOpcode.
**Parameters:** packet2Pointer to packet. addrAddress. irqInterrupt Request. False by default.
Definition at line 333 of file packet2_vif.h.
##### ◆ packet2_vif_stmask()
| static void packet2_vif_stmask ( packet2_t * packet2, Mask mask, u8 irq ) | inlinestatic |
#include <ee/packet2/include/packet2_vif.h>
Add STMASK VIF opcode.
**Note:** Alignment alert. Size of dword (1/2). For more details, check description of VIFOpcode.
**Parameters:** packet2Pointer to packet. maskMask. irqInterrupt Request. False by default.
Definition at line 346 of file packet2_vif.h.
##### ◆ packet2_vif_strow()
| static void packet2_vif_strow ( packet2_t * packet2, const u32 * row_arr, u8 irq ) | inlinestatic |
#include <ee/packet2/include/packet2_vif.h>
Add STROW VIF opcode.
**Note:** Alignment alert. Size of 5 x word (1+1/4). For more details, check description of VIFOpcode.
**Parameters:** packet2Pointer to packet. row_arrRow array. irqInterrupt Request. False by default.
Definition at line 360 of file packet2_vif.h.
##### ◆ packet2_vif_stcol()
| static void packet2_vif_stcol ( packet2_t * packet2, const u32 * col_arr, u8 irq ) | inlinestatic |
#include <ee/packet2/include/packet2_vif.h>
Add STCOL VIF opcode.
**Note:** Alignment alert. Size of 5 x word (1+1/4). For more details, check description of VIFOpcode.
**Parameters:** packet2Pointer to packet. col_arrColumn array. irqInterrupt Request. False by default.
Definition at line 377 of file packet2_vif.h.
##### ◆ packet2_vif_add_micro_program()
| void packet2_vif_add_micro_program | ( | packet2_t * | packet2, |
|  |  | u32 | dest, |
|  |  | u32 * | start, |
|  |  | u32 * | end |
|  | ) |  |  |
#include <ee/packet2/include/packet2_vif.h>
Add VU micro program into packet2. Packet2 MODE for micro program upload: Chain
**Parameters:** destVU destination address (divided by 16). startStart address. endEnd address.
Definition at line 14 of file packet2_vif.c.
References count, packet2_chain_ref(), packet2_vif_mpg(), and packet2_vif_nop().

---

## ps2netfs - TCP fs driver

Page: <https://ps2dev.github.io/ps2sdk/group__ps2netfs.html>

##### Macros
| #define | DEVSCAN_MAX (DEVSCAN_IOMAX+DEVSCAN_IOXMAX+1) |
| #define | DEVSCAN_MASK (IOP_DT_FS | IOP_DT_BLOCK) |
| #define | PFS_ZONE_SIZE 8192 |
##### Functions
| ModuleInfo_t * | devscan_getmodule (const char *name) |
| int | devscan_setup (int devtype) |
| int | devscan_gettype (char *name) |
| int | devscan_getdevlist (char *buffer) |
| static void | fdh_setup () |
| static int | fdh_getfd (int devtype, int fd) |
| static void | fdh_freefd (int fd) |
| static int | convmode_to_iomanx (int stat) |
| static int | convmode_from_iomanx (int stat) |
| int | ps2netfs_close_socket (void) |
| void | ps2netfs_close_fsys (void) |
| static int | ps2netfs_op_info (char *buf, int len) |
| static int | ps2netfs_op_fstype (char *buf, int len) |
| static int | ps2netfs_op_devlist (char *buf, int len) |
| static int | ps2netfs_op_open (char *buf, int len) |
| static int | ps2netfs_op_close (char *buf, int len) |
| static int | ps2netfs_op_read (char *buf, int len) |
| static int | ps2netfs_op_write (char *buf, int len) |
| static int | ps2netfs_op_lseek (char *buf, int len) |
| static int | ps2netfs_op_ioctl (char *buf, int len) |
| static int | ps2netfs_op_remove (char *buf, int len) |
| static int | ps2netfs_op_mkdir (char *buf, int len) |
| static int | ps2netfs_op_rmdir (char *buf, int len) |
| static int | ps2netfs_op_dopen (char *buf, int len) |
| static int | ps2netfs_op_dclose (char *buf, int len) |
| static int | ps2netfs_op_dread (char *buf, int len) |
| static int | ps2netfs_op_getstat (char *buf, int len) |
| static int | ps2netfs_op_chstat (char *buf, int len) |
| static int | ps2netfs_op_rename (char *buf, int len) |
| static int | ps2netfs_op_chdir (char *buf, int len) |
| static int | ps2netfs_op_sync (char *buf, int len) |
| static int | ps2netfs_op_mount (char *buf, int len) |
| static int | ps2netfs_op_umount (char *buf, int len) |
| static int | ps2netfs_op_lseek64 (char *buf, int len) |
| static int | ps2netfs_op_devctl (char *buf, int len) |
| static int | ps2netfs_op_symlink (char *buf, int len) |
| static int | ps2netfs_op_readlink (char *buf, int len) |
| static int | ps2netfs_op_ioctl2 (char *buf, int len) |
| static void | ps2netfs_Listener (int sock) |
| void | ps2netfs_serv (void *argv) |
| int | ps2netfs_Init (void) |
| int | ps2fs_Destroy (void) |
| int | _start (int argc, char *argv[]) |
##### Variables
| static dev_table_t | dev_info_list [DEVSCAN_MAX+1] |
##### Detailed Description
##### Macro Definition Documentation
##### ◆ DEVSCAN_MAX
| #define DEVSCAN_MAX (DEVSCAN_IOMAX+DEVSCAN_IOXMAX+1) |
#include <iop/fs/netfs/src/devscan.h>
Maximum number of devices handled.
Definition at line 21 of file devscan.h.
##### ◆ DEVSCAN_MASK
| #define DEVSCAN_MASK (IOP_DT_FS | IOP_DT_BLOCK) |
#include <iop/fs/netfs/src/devscan.h>
Device scan mask.
Definition at line 26 of file devscan.h.
##### ◆ PFS_ZONE_SIZE
| #define PFS_ZONE_SIZE 8192 |
#include <iop/fs/netfs/src/ps2_fio.c>
Handles a PS2NETFS_FORMAT_CMD request.
**Parameters:** bufPointer to packet data. lenLength of packet.
**Returns:** Status.
status returns: 0 if all request and response handled ok. -X if error.
return values for client: -19 (ENODEV) if device not found +X if handled ok, valid FD returned. -X if error.
Definition at line 1308 of file ps2_fio.c.
##### Function Documentation
##### ◆ devscan_getmodule()
| ModuleInfo_t* devscan_getmodule | ( | const char * | name | ) |  |
#include <iop/fs/netfs/src/devscan.c>
Get pointer to module structure for named module.
**Parameters:** nameStringname of module (eg "atad_driver").
**Returns:** Pointer to module structure.
return values: 0 if not found. pointer to module structure for loaded module if found.
Definition at line 47 of file devscan.c.
##### ◆ devscan_setup()
| int devscan_setup | ( | int | devtype | ) |  |
#include <iop/fs/netfs/src/devscan.c>
Initialise the devices table
**Parameters:** devtypeMask for device types to return (0x10 = FS drivers).
**Returns:** Number of devices found.
This scans ioman and iomanx for devices, then adds them to the internal list, with basename and the handler type.
Also used to re-init the devices table
Definition at line 73 of file devscan.c.
References count.
Referenced by ps2netfs_serv().
##### ◆ devscan_gettype()
| int devscan_gettype | ( | char * | name | ) |  |
#include <iop/fs/netfs/src/devscan.c>
Get device handler type for path.
**Parameters:** nameFull pathname to check.
**Returns:** Device handler type.
return values: MODULE_RESIDENT_END if loaded and registered as library. MODULE_NO_RESIDENT_END if just exiting normally.
Definition at line 141 of file devscan.c.
##### ◆ devscan_getdevlist()
| int devscan_getdevlist | ( | char * | buffer | ) |  |
#include <iop/fs/netfs/src/devscan.c>
Get device list.
**Parameters:** bufferPointer to dest buffer
**Returns:** number of devices returned.
Definition at line 162 of file devscan.c.
##### ◆ fdh_setup()
| static void fdh_setup ( ) | inlinestatic |
#include <iop/fs/netfs/src/ps2_fio.c>
Initialise the file descriptor table.
This initialises the file descriptor table that we use to translate to numbers passed to client, and to enable quick lookups on handler type.
Definition at line 79 of file ps2_fio.c.
Referenced by ps2netfs_serv().
##### ◆ fdh_getfd()
| static int fdh_getfd ( int devtype, int fd ) | inlinestatic |
#include <iop/fs/netfs/src/ps2_fio.c>
Get file descriptor for client.
**Parameters:** devtypeDevice Manager type. fdPS2 file descriptor.
**Returns:** FD to send to client.
return values: -1 if no space in list. FD if returning valid entry.
Definition at line 95 of file ps2_fio.c.
##### ◆ fdh_freefd()
| static void fdh_freefd ( int fd) | inlinestatic |
#include <iop/fs/netfs/src/ps2_fio.c>
Free file descriptor from client table.
**Parameters:** fdclient file descriptor.
Definition at line 117 of file ps2_fio.c.
##### ◆ convmode_to_iomanx()
| static int convmode_to_iomanx ( int stat) | inlinestatic |
#include <iop/fs/netfs/src/ps2_fio.c>
changes mode from ioman to iomanx format
Definition at line 140 of file ps2_fio.c.
##### ◆ convmode_from_iomanx()
| static int convmode_from_iomanx ( int stat) | inlinestatic |
#include <iop/fs/netfs/src/ps2_fio.c>
changes mode from iomanx to ioman format
Definition at line 161 of file ps2_fio.c.
##### ◆ ps2netfs_close_socket()
| int ps2netfs_close_socket | ( | void |  | ) |  |
#include <iop/fs/netfs/src/ps2_fio.c>
Shortcut to close the socket and cleanup.
**Returns:** disconnect return value.
Definition at line 171 of file ps2_fio.c.
##### ◆ ps2netfs_close_fsys()
| void ps2netfs_close_fsys | ( | void |  | ) |  |
#include <iop/fs/netfs/src/ps2_fio.c>
Shortcut to close the socket forcibly and set to exit (active=0).
This will close down the socket, and cause the server thread to exit.
**Returns:** disconnect return value.
Definition at line 189 of file ps2_fio.c.
##### ◆ ps2netfs_op_info()
| static int ps2netfs_op_info ( char * buf, int len ) | static |
#include <iop/fs/netfs/src/ps2_fio.c>
Handles a PS2NETFS_INFO_CMD request.
**Parameters:** bufPointer to packet data. lenLength of packet.
**Returns:** Status.
status returns: 0 if all request and response handled ok. -X if error.
return values for client: -1 if error. 0 if handled ok.
Definition at line 314 of file ps2_fio.c.
##### ◆ ps2netfs_op_fstype()
| static int ps2netfs_op_fstype ( char * buf, int len ) | static |
#include <iop/fs/netfs/src/ps2_fio.c>
Handles a PS2NETFS_FSTYPE_CMD request.
**Parameters:** bufPointer to packet data. lenLength of packet.
**Returns:** Status.
status returns: 0 if all request and response handled ok. -X if error.
return values for client: -1 if error. 0 if handled ok.
Definition at line 367 of file ps2_fio.c.
##### ◆ ps2netfs_op_devlist()
| static int ps2netfs_op_devlist ( char * buf, int len ) | static |
#include <iop/fs/netfs/src/ps2_fio.c>
Handles a PS2NETFS_DEVLIST_CMD request.
**Parameters:** bufPointer to packet data. lenLength of packet.
**Returns:** Status.
status returns: 0 if all request and response handled ok. -X if error.
return values for client: -1 if error. 0 if handled ok.
Definition at line 416 of file ps2_fio.c.
##### ◆ ps2netfs_op_open()
| static int ps2netfs_op_open ( char * buf, int len ) | static |
#include <iop/fs/netfs/src/ps2_fio.c>
Handles a PS2NETFS_OPEN_CMD request.
**Parameters:** bufPointer to packet data. lenLength of packet.
**Returns:** Status.
status returns: 0 if all request and response handled ok. -X if error.
return values for client: -19 (ENODEV) if device not found +X if handled ok, valid FD returned. -X if error.
Definition at line 484 of file ps2_fio.c.
##### ◆ ps2netfs_op_close()
| static int ps2netfs_op_close ( char * buf, int len ) | static |
#include <iop/fs/netfs/src/ps2_fio.c>
Handles a PS2NETFS_CLOSE_CMD request.
**Parameters:** bufPointer to packet data. lenLength of packet.
**Returns:** Status.
status returns: 0 if all request and response handled ok. -X if error.
return values for client: -19 (ENODEV) if device not found >=0 if handled ok. -X if error.
Definition at line 545 of file ps2_fio.c.
##### ◆ ps2netfs_op_read()
| static int ps2netfs_op_read ( char * buf, int len ) | static |
#include <iop/fs/netfs/src/ps2_fio.c>
Handles a PS2NETFS_READ_CMD request.
**Parameters:** bufPointer to packet data. lenLength of packet.
**Returns:** Status.
status returns: 0 if all request and response handled ok. -X if error.
return values for client: -19 (ENODEV) if device not found >=0 if handled ok , bytes read. -X if error.
Definition at line 605 of file ps2_fio.c.
##### ◆ ps2netfs_op_write()
| static int ps2netfs_op_write ( char * buf, int len ) | static |
#include <iop/fs/netfs/src/ps2_fio.c>
Handles a PS2NETFS_WRITE_CMD request.
**Parameters:** bufPointer to packet data. lenLength of packet.
**Returns:** Status.
status returns: 0 if all request and response handled ok. -X if error.
return values for client: -19 (ENODEV) if device not found >=0 if handled ok , bytes written. -X if error.
Definition at line 677 of file ps2_fio.c.
##### ◆ ps2netfs_op_lseek()
| static int ps2netfs_op_lseek ( char * buf, int len ) | static |
#include <iop/fs/netfs/src/ps2_fio.c>
Handles a PS2NETFS_LSEEK_CMD request.
**Parameters:** bufPointer to packet data. lenLength of packet.
**Returns:** Status.
status returns: 0 if all request and response handled ok. -X if error.
return values for client: -19 (ENODEV) if device not found >=0 if handled ok , position. -X if error.
Definition at line 751 of file ps2_fio.c.
##### ◆ ps2netfs_op_ioctl()
| static int ps2netfs_op_ioctl ( char * buf, int len ) | static |
#include <iop/fs/netfs/src/ps2_fio.c>
Handles a PS2NETFS_IOCTL_CMD request.
**Parameters:** bufPointer to packet data. lenLength of packet.
**Returns:** Status.
status returns: 0 if all request and response handled ok. -X if error.
return values for client: -19 (ENODEV) if device not found >=0 if handled ok. -X if error.
Definition at line 809 of file ps2_fio.c.
##### ◆ ps2netfs_op_remove()
| static int ps2netfs_op_remove ( char * buf, int len ) | static |
#include <iop/fs/netfs/src/ps2_fio.c>
Handles a PS2NETFS_REMOVE_CMD request.
**Parameters:** bufPointer to packet data. lenLength of packet.
**Returns:** Status.
status returns: 0 if all request and response handled ok. -X if error.
return values for client: -19 (ENODEV) if device not found >=0 if handled ok. -X if error.
Definition at line 867 of file ps2_fio.c.
##### ◆ ps2netfs_op_mkdir()
| static int ps2netfs_op_mkdir ( char * buf, int len ) | static |
#include <iop/fs/netfs/src/ps2_fio.c>
Handles a PS2NETFS_MKDIR_CMD request.
**Parameters:** bufPointer to packet data. lenLength of packet.
**Returns:** Status.
status returns: 0 if all request and response handled ok. -X if error.
return values for client: -19 (ENODEV) if device not found >=0 if handled ok. -X if error.
Definition at line 926 of file ps2_fio.c.
##### ◆ ps2netfs_op_rmdir()
| static int ps2netfs_op_rmdir ( char * buf, int len ) | static |
#include <iop/fs/netfs/src/ps2_fio.c>
Handles a PS2NETFS_RMDIR_CMD request.
**Parameters:** bufPointer to packet data. lenLength of packet.
**Returns:** Status.
status returns: 0 if all request and response handled ok. -X if error.
return values for client: -19 (ENODEV) if device not found >=0 if handled ok. -X if error.
Definition at line 985 of file ps2_fio.c.
##### ◆ ps2netfs_op_dopen()
| static int ps2netfs_op_dopen ( char * buf, int len ) | static |
#include <iop/fs/netfs/src/ps2_fio.c>
Handles a PS2NETFS_DOPEN_CMD request.
**Parameters:** bufPointer to packet data. lenLength of packet.
**Returns:** Status.
status returns: 0 if all request and response handled ok. -X if error.
return values for client: -19 (ENODEV) if device not found +X if handled ok, valid FD returned. -X if error.
Definition at line 1044 of file ps2_fio.c.
##### ◆ ps2netfs_op_dclose()
| static int ps2netfs_op_dclose ( char * buf, int len ) | static |
#include <iop/fs/netfs/src/ps2_fio.c>
Handles a PS2NETFS_DCLOSE_CMD request.
**Parameters:** bufPointer to packet data. lenLength of packet.
**Returns:** Status.
status returns: 0 if all request and response handled ok. -X if error.
return values for client: -19 (ENODEV) if device not found >=0 if handled ok. -X if error.
Definition at line 1105 of file ps2_fio.c.
##### ◆ ps2netfs_op_dread()
| static int ps2netfs_op_dread ( char * buf, int len ) | static |
#include <iop/fs/netfs/src/ps2_fio.c>
Handles a PS2NETFS_DREAD_CMD request.
**Parameters:** bufPointer to packet data. lenLength of packet.
**Returns:** Status.
status returns: 0 if all request and response handled ok. -X if error.
return values for client: -19 (ENODEV) if device not found >=0 if handled ok. -X if error.
Definition at line 1165 of file ps2_fio.c.
##### ◆ ps2netfs_op_getstat()
| static int ps2netfs_op_getstat ( char * buf, int len ) | static |
#include <iop/fs/netfs/src/ps2_fio.c>
Handles a PS2NETFS_GETSTAT_CMD request.
**Parameters:** bufPointer to packet data. lenLength of packet.
**Returns:** Status.
status returns: 0 if all request and response handled ok. -X if error.
return values for client: -19 (ENODEV) if device not found +X if handled ok, valid FD returned. -X if error.
Definition at line 1255 of file ps2_fio.c.
##### ◆ ps2netfs_op_chstat()
| static int ps2netfs_op_chstat ( char * buf, int len ) | static |
#include <iop/fs/netfs/src/ps2_fio.c>
Handles a PS2NETFS_CHSTAT_CMD request.
**Parameters:** bufPointer to packet data. lenLength of packet.
**Returns:** Status.
status returns: 0 if all request and response handled ok. -X if error.
return values for client: -19 (ENODEV) if device not found +X if handled ok, valid FD returned. -X if error.
Definition at line 1279 of file ps2_fio.c.
##### ◆ ps2netfs_op_rename()
| static int ps2netfs_op_rename ( char * buf, int len ) | static |
#include <iop/fs/netfs/src/ps2_fio.c>
Handles a PS2NETFS_RENAME_CMD request.
**Parameters:** bufPointer to packet data. lenLength of packet.
**Returns:** Status.
status returns: 0 if all request and response handled ok. -X if error.
return values for client: -19 (ENODEV) if device not found +X if handled ok, valid FD returned. -X if error.
Definition at line 1373 of file ps2_fio.c.
##### ◆ ps2netfs_op_chdir()
| static int ps2netfs_op_chdir ( char * buf, int len ) | static |
#include <iop/fs/netfs/src/ps2_fio.c>
Handles a PS2NETFS_CHDIR_CMD request.
**Parameters:** bufPointer to packet data. lenLength of packet.
**Returns:** Status.
status returns: 0 if all request and response handled ok. -X if error.
return values for client: -19 (ENODEV) if device not found +X if handled ok, valid FD returned. -X if error.
Definition at line 1431 of file ps2_fio.c.
##### ◆ ps2netfs_op_sync()
| static int ps2netfs_op_sync ( char * buf, int len ) | static |
#include <iop/fs/netfs/src/ps2_fio.c>
Handles a PS2NETFS_SYNC_CMD request.
**Parameters:** bufPointer to packet data. lenLength of packet.
**Returns:** Status.
status returns: 0 if all request and response handled ok. -X if error.
return values for client: -19 (ENODEV) if device not found +X if handled ok, valid FD returned. -X if error.
Definition at line 1485 of file ps2_fio.c.
##### ◆ ps2netfs_op_mount()
| static int ps2netfs_op_mount ( char * buf, int len ) | static |
#include <iop/fs/netfs/src/ps2_fio.c>
Handles a PS2NETFS_MOUNT_CMD request.
**Parameters:** bufPointer to packet data. lenLength of packet.
**Returns:** Status.
status returns: 0 if all request and response handled ok. -X if error.
return values for client: -19 (ENODEV) if device not found +X if handled ok, valid FD returned. -X if error.
Definition at line 1539 of file ps2_fio.c.
##### ◆ ps2netfs_op_umount()
| static int ps2netfs_op_umount ( char * buf, int len ) | static |
#include <iop/fs/netfs/src/ps2_fio.c>
Handles a PS2NETFS_UMOUNT_CMD request.
**Parameters:** bufPointer to packet data. lenLength of packet.
**Returns:** Status.
status returns: 0 if all request and response handled ok. -X if error.
return values for client: -19 (ENODEV) if device not found +X if handled ok, valid FD returned. -X if error.
Definition at line 1593 of file ps2_fio.c.
##### ◆ ps2netfs_op_lseek64()
| static int ps2netfs_op_lseek64 ( char * buf, int len ) | static |
#include <iop/fs/netfs/src/ps2_fio.c>
Handles a PS2NETFS_LSEEK64_CMD request.
**Parameters:** bufPointer to packet data. lenLength of packet.
**Returns:** Status.
status returns: 0 if all request and response handled ok. -X if error.
return values for client: -19 (ENODEV) if device not found +X if handled ok, valid FD returned. -X if error.
Definition at line 1647 of file ps2_fio.c.
##### ◆ ps2netfs_op_devctl()
| static int ps2netfs_op_devctl ( char * buf, int len ) | static |
#include <iop/fs/netfs/src/ps2_fio.c>
Handles a PS2NETFS_DEVCTL_CMD request.
**Parameters:** bufPointer to packet data. lenLength of packet.
**Returns:** Status.
status returns: 0 if all request and response handled ok. -X if error.
return values for client: -19 (ENODEV) if device not found +X if handled ok, valid FD returned. -X if error.
Definition at line 1671 of file ps2_fio.c.
##### ◆ ps2netfs_op_symlink()
| static int ps2netfs_op_symlink ( char * buf, int len ) | static |
#include <iop/fs/netfs/src/ps2_fio.c>
Handles a PS2NETFS_SYMLINK_CMD request.
**Parameters:** bufPointer to packet data. lenLength of packet.
**Returns:** Status.
status returns: 0 if all request and response handled ok. -X if error.
return values for client: -19 (ENODEV) if device not found +X if handled ok, valid FD returned. -X if error.
Definition at line 1695 of file ps2_fio.c.
##### ◆ ps2netfs_op_readlink()
| static int ps2netfs_op_readlink ( char * buf, int len ) | static |
#include <iop/fs/netfs/src/ps2_fio.c>
Handles a PS2NETFS_READLINK_CMD request.
**Parameters:** bufPointer to packet data. lenLength of packet.
**Returns:** Status.
status returns: 0 if all request and response handled ok. -X if error.
return values for client: -19 (ENODEV) if device not found +X if handled ok, valid FD returned. -X if error.
Definition at line 1753 of file ps2_fio.c.
##### ◆ ps2netfs_op_ioctl2()
| static int ps2netfs_op_ioctl2 ( char * buf, int len ) | static |
#include <iop/fs/netfs/src/ps2_fio.c>
Handles a PS2NETFS_IOCTL2_CMD request.
**Parameters:** bufPointer to packet data. lenLength of packet.
**Returns:** Status.
status returns: 0 if all request and response handled ok. -X if error.
return values for client: -19 (ENODEV) if device not found +X if handled ok, valid FD returned. -X if error.
Definition at line 1808 of file ps2_fio.c.
##### ◆ ps2netfs_Listener()
| static void ps2netfs_Listener ( int sock) | static |
#include <iop/fs/netfs/src/ps2_fio.c>
Listen for packets and handle them.
**Parameters:** sockSocket to receive on.
This function listens on the given socket for command packets. It loops until a socket error, or protocol error is found, then exits to the calling function, which should clean the socket up.
Definition at line 1825 of file ps2_fio.c.
References ps2netfs_accept_pktunknown().
##### ◆ ps2netfs_serv()
| void ps2netfs_serv | ( | void * | argv | ) |  |
#include <iop/fs/netfs/src/ps2_fio.c>
Main ps2netfs Thread.
**Parameters:** argvParameters to thread.
**Returns:** Status.
This is the main thread function for ps2netfs. It runs until 'ps2netfs_active' is set to 0. Handles accepting connections and passing them onto the listener function to handle them.
Definition at line 1963 of file ps2_fio.c.
References DEVSCAN_MASK, devscan_setup(), and fdh_setup().
##### ◆ ps2netfs_Init()
| int ps2netfs_Init | ( | void |  | ) |  |
#include <iop/fs/netfs/src/ps2_fio.c>
Init ps2netfs.
**Returns:** Status (0=success, -1 = failure).
This handles setting up the Thread, and starting it running.
Definition at line 2061 of file ps2_fio.c.
##### ◆ ps2fs_Destroy()
| int ps2fs_Destroy | ( | void |  | ) |  |
#include <iop/fs/netfs/src/ps2_fio.c>
Shutdown ps2netfs.
This handles Stopping the thread and disconnecting. All shutdown for ps2netfs.
Definition at line 2105 of file ps2_fio.c.
##### ◆ _start()
| int _start | ( | int | argc, |
|  |  | char * | argv[] |
|  | ) |  |  |
#include <iop/fs/netfs/src/ps2netfs.c>
Entry point for IRX.
argc and argv make no difference to runstate.
**Parameters:** argcNumber of arguments. argvPointer to array of arguments.
**Returns:** Module Status on Exit.
return values: MODULE_RESIDENT_END if loaded and registered as library. MODULE_NO_RESIDENT_END if just exiting normally.
Definition at line 47 of file ps2netfs.c.
##### Variable Documentation
##### ◆ dev_info_list
| dev_table_t dev_info_list[DEVSCAN_MAX+1] | static |
#include <iop/fs/netfs/src/devscan.c>
Device type structure.
Definition at line 35 of file devscan.c.

---

## Modules

Page: <https://ps2dev.github.io/ps2sdk/modules.html>

Here is a list of all modules:
[detail level
1
2
]
- Flags (group__netif__flags.html) |
- EE LOADFILE: ELF and IRX loader client library. (group__loadfile.html) |
- ▼Packet2 library (group__packet2.html) | Successor of packet_t (structpacket__t.html). Main goal of this library is to create simple API for packet management. Library is splitted into several parts:
- Chain (group__packet2__chain.html) | Chain mode related functions of libpacket2
- Types (group__packet2__types.html) | Structures and enums used in libpacket2
- Utils (group__packet2__utils.html) | Useful functions and examples for libpacket2
- VIF (group__packet2__vif.html) | VIF related functions of libpacket2
- fakehost - host: to hdd driver (group__fakehost.html) |
- ps2netfs - TCP fs driver (group__ps2netfs.html) |
- iopmgr - IOP Manager (group__iopmgr.html) |
- devfs: PS2 Device Filing System (group__devfs.html) |

---
