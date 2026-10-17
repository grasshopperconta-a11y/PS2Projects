# Part 8 — Markdown Pages (READMEs etc.)

## IOPRP image generator

Page: <https://ps2dev.github.io/ps2sdk/md_ee_ioprpgen__r_e_a_d_m_e.html>

This library generates IOPRP images at runtime for usage with iopreboot.
#### Usage
See "ioprpgen" sample for usage example.

---

## PS2SDK - KERNEL LIBRARY

Page: <https://ps2dev.github.io/ps2sdk/md_ee_kernel__r_e_a_d_m_e.html>

#### SUMMARY
This folder creates the libkernel.a library, which contains all the references to the BIOS functionality embedded in the hardware of every single PS2.
Probably you've heard, that the PS2 BIOS is full of bugs, which totally accurate, however, these bugs aren't blocker you still could execute some program (with limited functionality) without any problem.
#### SOLVING BIOS ISSUES
In order to fix all these issues, we're patching the problematic functions by putting some wrappers in the middle before calling the actual BIOS function.
Some of these wrappers are set during the initialization process of the application _InitSys function. Additionally, we also use _InitSys to initialize some other functionality that the user may need.
#### CONSEQUENCES
All these functions are set during the initialization process of every single binary, this implies unfortunately having a bigger size binary.
Some apps require to have really tiny sizes, and also you may want to don't patch these BIOS functions, therefore we are offering the possibility to disable the functions called during the _InitSys function.
Let's first take a look at the current InitSys method:
```
void _InitSys(void)
{
    StartTimerSystemTime();
    InitTimerAlarm();
    InitAlarm();
    InitThread();
    InitExecPS2();
    InitTLBFunctions();
}
```
The nature of the functions called can be split into 2 different sections:
1. Patched functionality InitAlarm(); InitThread(); InitExecPS2(); InitTLBFunctions();
2. Additional timer utils StartTimerSystemTime(); InitTimerAlarm();
#### NO PATCHED BINARIES AND/OR TINY BINARIES
On the kernel.h file at the very end, we have a section where we defined some macros for making it super easy the disable these functions.
Let's put an example of how to disable the patched functionality:
```
.....
#include <kernel.h>
#include <stdio.h>

// With this line we disabled the patched functionalities
DISABLE_PATCHED_FUNCTIONS();

int main(int argc, char *argv[])
{
    printf("Hello world!\n");
    return 0;
}
```
Let's put another example where we disable the extra timer functionality:
```
.....
#include <kernel.h>
#include <stdio.h>

// With this line we disabled the extra functionalities for timers
DISABLE_EXTRA_TIMERS_FUNCTIONS();

int main(int argc, char *argv[])
{
    printf("Hello world!\n");
    return 0;
}
```
Therefore we can combine both:
```
.....
#include <kernel.h>
#include <stdio.h>

// With this line we disabled the patched functionalities
DISABLE_PATCHED_FUNCTIONS();
// With this line we disabled the extra functionalities for timers
DISABLE_EXTRA_TIMERS_FUNCTIONS();

int main(int argc, char *argv[])
{
    printf("Hello world!\n");
    return 0;
}
```
#### HOW IS THIS WORKING?
It honestly is quite easy. All these functions that we may want to disable are defined as __attribute__((weak)), so it means that if a "strong" implementation is defined, they will override. For this reason, the macros defined in the kernel.h are helpers that either does dummy implementations or bypass the patched wrappers.

---

## libcglue

Page: <https://ps2dev.github.io/ps2sdk/md_ee_libcglue__r_e_a_d_m_e.html>

This library provides functions to bridge the gap between newlib and libraries provided by ps2sdk.
#### About file descriptors
ps2sdk uses multiple libraries to interact with files and sockets. libcglue fdman unifies the file descriptors provided by these libraries into a single namespace:
```
flowchart LR

A["libkernel (fileio)"] --> G
B[libfileXio] --> G
C[libtcpip] --> G
D[libtcpips] --> G
G[libcglue] --> H[User code]
```

---

## remote

Page: <https://ps2dev.github.io/ps2sdk/md_ee_rpc_remote_remote.html>

#librm.h notes
This is the EE RPC code to access the module RMMAN in my PS2.
RMMAN is in rom1 not rom0, to access it you must load the rom0:ADDDRV module, then you can load it manually. If the rom0:SIO2MAN has been loaded you MUST reboot the IOP and load rom1:SIO2MAN fresh else it will not work. The rom1:PADMAN looks to use the XPADMAN RPC interface so use the appropriate library from PS2SDK.
To use it is the same as using the PAD library.
Call RMMan_Init() to initialise the RPC interface. Call RMMan_Open(port, slot, data) to open the port with the remote in it. Data should be a 64byte aligned data structure of 256 bytes. Call RMMan_Read(port, slot) to read out the current status.
Check the status value equals either RM_READY or RM_KEYPRESSED to check its state. If (status == RM_KEYPRESSED) then the button is set to one of the RM keys defines in librm.h
The remote only has a concept of one keypress at a time, if you press more than one then neither is registered.
When you hold the button then this button value is returned, when you release the button RM_RELEASED will be returned.
When you press (or hold) any directional arrow button on the remote, 2 button values will be returned: first DVD section button, then PS2 section button, then the value that button was released. For example when you press UP, then RMMan_Read() will return
```
RM_DVD_UP
RM_PS2_UP
RM_RELEASED
```
Each 2 minutes with no action RMMAN will return RM_IDLE followed by RM_RELEASED value.
###### Sony Remote Theory
PS2 remote is from Sony20 remote family. That means that Remote sends a 20-bit length signal, which is then parsed and translated into hex. Input IR signal has some internal standards, in short, 20 bits are divided into 3 blocks (8-5-7 bits in each block). For example, the IR signal for RM_PS2_SQUARE will be
```
11011010-11010-1011111
```
The first block 11011010 in decimal will be 28, this block is identical on all Sony remotes. The second block 11010 in decimal will be 218, this block is responsible for a specific device. In our case 218 is the codename for PS2. PS2 also accepts block 26 for DVD side buttons. These 2 families are called: 28.218 and 28.26, both are supported by PS2. The third block is the actual button code (7 bits) in the range 0-127.
###### PS2 IR code conversion
PS2 will accept any 20 bit IR code and will convert it into its own format. For example RM_PS2_SQUARE IR 20-bit code will be in hex:
```
DAD5F
```
PS2 will add trailing Zeroes and change endian: DAD5F -> DAD5F000 -> 00 F0 D5 DA In short - 3 bytes can get only 2 values (0xDAD or 0x49D) for PS2 and DVD side. 2 bytes: button number (higher bit always zero)
###### RMMAN revision history
Firstly RMMAN was introduced in SCPH-18000 with DVD version 2.00. To get it to work in older models, you should install a DVD player update. The next revision was introduced when SCPH-5xxxx was released. The next revision was introduced when SCPH-7xxxx (slim) was released. Also in SCPH-5xxxx appeared new module RMMAN2 The next revision was introduced when SCPH-7xxxx (slim) was released.
Were released 2 remote revisions: SCPH-10170 and SCPH-10420. The first came with an external IR receiver, which can be plugged into the controller port. The latter one contains 2 additional buttons: EJECT and RESET and has no eternal IR reciever. These 2 buttons work only on SLIM models with a built-in IR receiver. The external IR receiver has no effect when plugged into Slim PS2.
###### Undocumented features
PS2 will accept additional IR commands which are not presented on its remote. Some standard DVD commands from the 28.26 family are supported. The most useful additional commands from the PS2 side (28.218 family) will be digital POWER_ON and POWER_OFF commands. These commands by default will work only on SLIM models.
###### SCMD
It seems that there are 2 SCMD commands for RMMAN: 0x1E - ReadSIRc - will return pressed button code and stat value: as an example: 0014 DAD1 6000, where 00 60 D1 DA - button code. 0x1F - IgnoreSIRc - seems that this will disable IR completely
SCMD command 0x1E is presented on PS3 Backward Compatible. On PS3 it just replicates each controller button press.
###### Programmable IR remotes
Lirc format will accept 20-bit code, you only need to reverse it and translate it into hex. Example: RM_PS2_SQUARE
```
11011010110101011111
in reverse
11111010101101011011
in hex
0x00000000000FAB5B
```
Other information about IR signal:
```
Frequency=40000
Time Base=600
One=2,-1
Zero=1,-1
Prefix=4,-1
Message Time=45000
```
##### Credits
Information about Sony remotes taken from http://www.hifi-remote.com/sony/Sony_ps2.htm

---

## Security manager RPC client

Page: <https://ps2dev.github.io/ps2sdk/md_ee_rpc_secr__r_e_a_d_m_e.html>

Remote procedure call client for the secrman module.
Requires secrsif IOP module to be loaded.
The source code for this module is based upon the source code from FMCB Installer v0.987.

---

## Arcade ATA/ATAPI driver

Page: <https://ps2dev.github.io/ps2sdk/md_iop_arcade_acata__r_e_a_d_m_e.html>

This module handles the ATA/ATAPI interface \ for Bandai Namco System 246/256 systems.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- acata -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## Arcade atad driver

Page: <https://ps2dev.github.io/ps2sdk/md_iop_arcade_acatad__r_e_a_d_m_e.html>

This module provides a shim for atad to acata so that libraries relying on it \ can be used.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- acatad -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## Arcade CD/DVD driver

Page: <https://ps2dev.github.io/ps2sdk/md_iop_arcade_accdvd__r_e_a_d_m_e.html>

This module interfaces with acata to allow file-level access to ATAPI drives.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- accdvd -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## Arcade CD/DVD driver RPC

Page: <https://ps2dev.github.io/ps2sdk/md_iop_arcade_accdvde__r_e_a_d_m_e.html>

This module exposes the interfaces provided by accdvd \ to the EE using SIF RPC.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- accdvde -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## Arcade Core

Page: <https://ps2dev.github.io/ps2sdk/md_iop_arcade_accore__r_e_a_d_m_e.html>

This module is the core module for the arcade interface \ for Bandai Namco System 246/256 systems.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- accore -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## Arcade dev9 driver

Page: <https://ps2dev.github.io/ps2sdk/md_iop_arcade_acdev9__r_e_a_d_m_e.html>

This module provides a shim for dev9 for arcade hardware \ so that libraries relying on it can be used.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- acdev9 -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## Arcade Device

Page: <https://ps2dev.github.io/ps2sdk/md_iop_arcade_acdev__r_e_a_d_m_e.html>

This module is the device module for the arcade interface \ for Bandai Namco System 246/256 systems.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- acdev -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## Arcade Flash Memory driver

Page: <https://ps2dev.github.io/ps2sdk/md_iop_arcade_acflash__r_e_a_d_m_e.html>

This module allows flashing the flash ROM on the arcade interface \ for Bandai Namco System 246/256 systems. If ROMDIR compliant data is flashed, \ it will be accessible with acdev using rom1:.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- acflash -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## Arcade FPGA Bitstream Loader

Page: <https://ps2dev.github.io/ps2sdk/md_iop_arcade_acfpgald__r_e_a_d_m_e.html>

This module loads the Altera APEX EP20K100EQC208-2X FPGA bitstream \ on the arcade interface \ for Bandai Namco System 246/256 systems.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- acfpgald -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## Arcade JV Interface

Page: <https://ps2dev.github.io/ps2sdk/md_iop_arcade_acjv__r_e_a_d_m_e.html>

This module handles the JV interface \ for Bandai Namco System 246/256 systems.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- acjv -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## Arcade JV firmware loader

Page: <https://ps2dev.github.io/ps2sdk/md_iop_arcade_acjvld__r_e_a_d_m_e.html>

This module loads the JV firmware on the arcade interface \ for Bandai Namco System 246/256 systems.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- acjvld -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## Arcade Memory Interface

Page: <https://ps2dev.github.io/ps2sdk/md_iop_arcade_acmem__r_e_a_d_m_e.html>

This module allows access to the on-board volatile memory \ on the arcade interface \ for Bandai Namco System 246/256 systems.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- acmem -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## Arcade Memory Interface RPC

Page: <https://ps2dev.github.io/ps2sdk/md_iop_arcade_acmeme__r_e_a_d_m_e.html>

This module exposes the interfaces provided by acjv, acmem, acram, and acsram \ to the EE using SIF RPC.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- acmeme -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## Arcade Extended RAM Interface

Page: <https://ps2dev.github.io/ps2sdk/md_iop_arcade_acram__r_e_a_d_m_e.html>

This module allows access to the extended volatile memory on the arcade interface for Bandai Namco System 246/256 systems.
Originally, the ACRAM came as external boards, both RAM32 PCB and RAM64 PCB
- on System246A (at least on DRIVING version) the system has two slots for ACRAM boards. (only both wangan midnight games need two RAM64PCBs)
- on System246B and 246C 64MB of ACRAM are mounted directly on the motherboard
- on System256 the ACRAM is no longer part of the system
just like the ATA interface, it depends on the altera FPGA programmed by acfpgald.irx
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- acram -> The recommended version.
- acram_extended -> Supports up to 128mb of ACRAM, only on system246 Rack A
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## acrtc

Page: <https://ps2dev.github.io/ps2sdk/md_iop_arcade_acrtc__r_e_a_d_m_e.html>

This module exposes the real-time clock provided by cdvdman \ to the EE using SIF RPC.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- acrtc -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## Arcade SRAM Interface

Page: <https://ps2dev.github.io/ps2sdk/md_iop_arcade_acsram__r_e_a_d_m_e.html>

This module allows access to the non-volatile static memory \ on the arcade interface \ for Bandai Namco System 246/256 systems.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- acsram -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## Arcade Simple Timer Interface

Page: <https://ps2dev.github.io/ps2sdk/md_iop_arcade_actimer__r_e_a_d_m_e.html>

This module provides a simple interface to access the timers on the IOP.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- actimer -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## Arcade UART Interface

Page: <https://ps2dev.github.io/ps2sdk/md_iop_arcade_acuart__r_e_a_d_m_e.html>

This module allows access to the Maxim MAX232 UART hardware \ on the arcade interface \ for Bandai Namco System 246/256 systems.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- acuart -> default version. same behavior than original module.
- acuart-tty -> exactly the same than default. but will redirect stdout to the uart as soon as module boots
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.
#### Hardware Notes
The UART is easily accesible through the white JST 3 pin connector located on the frontal panel of the arcade board, just between JVS USB and the dip switches. From left to right, the pins are: RX, TX, GND.
An USB to RS232 (usually with DB9 connector) is recommended

---

## ROMWRITE

Page: <https://ps2dev.github.io/ps2sdk/md_iop_arcade_romwrite__r_e_a_d_m_e.html>

This module allows access to writing the NAND flash of System 147.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- romwrite -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with arguments.

---

## S147CTRL

Page: <https://ps2dev.github.io/ps2sdk/md_iop_arcade_s147ctrl__r_e_a_d_m_e.html>

This module provides access to the LED, watchdog, SRAM, RTC, and security of System 147.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- s147ctrl -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## S147LINK

Page: <https://ps2dev.github.io/ps2sdk/md_iop_arcade_s147link__r_e_a_d_m_e.html>

This module provides functions to access the CircLink of System 147 provided by the SMSC TMC2074 controller over RS485 medium.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- s147link -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## S147MDEV

Page: <https://ps2dev.github.io/ps2sdk/md_iop_arcade_s147mdev__r_e_a_d_m_e.html>

This module muxes together access to System 147 storage: NAND, USB, and HTTP.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- s147mdev -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## S147NAND

Page: <https://ps2dev.github.io/ps2sdk/md_iop_arcade_s147nand__r_e_a_d_m_e.html>

This module provides access to the NAND flash of System 147.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- s147nand -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## S147NETB

Page: <https://ps2dev.github.io/ps2sdk/md_iop_arcade_s147netb__r_e_a_d_m_e.html>

This module initializes the network/HTTP functionality of System 147.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- s147netb -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## Power off simulation

Page: <https://ps2dev.github.io/ps2sdk/md_iop_cdvd_poffsim__r_e_a_d_m_e.html>

This module simulates power off callbacks, equivalent to the POWEROFF module on DTL-T. This is useful for situations when debugging on systems that do not support power off callbacks, such as SCPH-10000.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- poffsim -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## DEV5 SPEED module for ATAPI

Page: <https://ps2dev.github.io/ps2sdk/md_iop_cdvd_xatapi__r_e_a_d_m_e.html>

This module allows access to the ATAPI CD/DVD drive connected to SPEED on DEV5. This module also contains support code for switching between the IDE/ATAPI and MechaCon/Dragon-connected CD/DVD drives.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- xatapi -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## PPC TTY

Page: <https://ps2dev.github.io/ps2sdk/md_iop_debug_ppctty__r_e_a_d_m_e.html>

IOP Module to redirect IOP Printf from stdout to PowerPC UART on DECKARD Models (SCPH-75xxx and up).
If the module detects the console is NOT a DECKARD model, it will abort its start process and unload from IOP.
Coded by @asmblur

---

## Simple Thread Monitor

Page: <https://ps2dev.github.io/ps2sdk/md_iop_debug_thmon__r_e_a_d_m_e.html>

This module provides an interface on tty9: (accessible from dsicons) to monitor threads on the IOP.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- thmon -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with, optionally, a single integer for added stack size.

---

## Additional ROM driver

Page: <https://ps2dev.github.io/ps2sdk/md_iop_fs_adddrv__r_e_a_d_m_e.html>

IOP module for handling the filesystem contained in the ROM chip attached to DEV1, usually containing the DVD player.
#### How to use this module in your program
In order to use this module in your program, you must integrate the module into an IOPRP image, then load the image with UDNL.\ Using LoadModule or LoadModuleBuffer directly will not work, because the module is already loaded at IOP boot.

---

## Additional ROM driver

Page: <https://ps2dev.github.io/ps2sdk/md_iop_fs_addrom2__r_e_a_d_m_e.html>

IOP module for handling the filesystem contained in the ROM chip attached to DEV1 at an offset, usually containing the Chinese font.
#### How to use this module in your program
In order to use this module in your program, you must integrate the module into an IOPRP image, then load the image with UDNL.\ Using LoadModule or LoadModuleBuffer directly will not work, because the module is already loaded at IOP boot.

---

## Encrypted ROM driver

Page: <https://ps2dev.github.io/ps2sdk/md_iop_fs_eromdrv__r_e_a_d_m_e.html>

IOP module for handling the encrypted filesystem contained in the ROM chip attached to DEV1.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- eromdrv -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## FILEIO server service module

Page: <https://ps2dev.github.io/ps2sdk/md_iop_fs_fileio__r_e_a_d_m_e.html>

This module provides file and heap interfaces to the EE.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- fileio -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, you must integrate the module into an IOPRP image, then load the image with UDNL.\ Using LoadModule or LoadModuleBuffer directly will not work, because the module is already loaded at IOP boot.

---

## ROM/Flash Driver

Page: <https://ps2dev.github.io/ps2sdk/md_iop_fs_romdrv__r_e_a_d_m_e.html>

IOP module for handling the filesystem contained in the ROM chip attached to DEV2.
The source code for this module is based upon the source code from PS2Ident v0.835.
#### How to use this module in your program
In order to use this module in your program, you must integrate the module into an IOPRP image, then load the image with UDNL.\ Using LoadModule or LoadModuleBuffer directly will not work, because the module is already loaded at IOP boot.

---

## Subfile

Page: <https://ps2dev.github.io/ps2sdk/md_iop_fs_subfile__r_e_a_d_m_e.html>

IOP module for exposing a portion of a file (useful for loading an executable embedded in a APA partition).
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- subfile -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## AN986 USB Ethernet driver

Page: <https://ps2dev.github.io/ps2sdk/md_iop_network_an986__r_e_a_d_m_e.html>

This module allows interfacing with the ADMtek an986 USB Ethernet hardware.
#### Documentation
Datasheet: https://stuff.mit.edu/afs/sipb/contrib/doc/specs/ic/network/an986.pdf
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- an986 -> The recommended version.
- an986-uepcb -> Supports UEPCB intended for System 246C/256/147/148.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## Network configuration library

Page: <https://ps2dev.github.io/ps2sdk/md_iop_network_netcnf__r_e_a_d_m_e.html>

This module provides functions to access the "Your Network Configuration File" (YNCF) stored on the memory card, the hard drive, or other device.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- netcnf -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## Network configuration library interface

Page: <https://ps2dev.github.io/ps2sdk/md_iop_network_netcnfif__r_e_a_d_m_e.html>

This module provides a SIF RPC server for netcnf for accessing the library from the EE.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- netcnf -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## Daemon (aka: sec_checker)

Page: <https://ps2dev.github.io/ps2sdk/md_iop_security_daemon__r_e_a_d_m_e.html>

This module, found on the bootrom of the Arcade PS2s (COH-H models and derivative units) is in charge of checking the security dongle status.
Arcade SYSCON has a 3 to 5 minutes countdown (time may depend on the model) to reset the console.
Arcade Mechacon resets this countdown when the secrAuthDongle routine is successfully completed.
This module setups an IOP thread that calls mcdetectcard2 (DONGLEMAN EXPORT:21) once every minute. effectively keeping the watchdog at bay, but also making access to mc0:/ rather unstable.
This module is placed here just for hystorical purposes and preservation. there is (as of today) no reason to use a homebrew implementation in favor of rom0:DAEMON

---

## Security manager

Page: <https://ps2dev.github.io/ps2sdk/md_iop_security_secrman__r_e_a_d_m_e.html>

IOP module for security related functions.
Mainly related to memory card authentication and KELF binding.
The actual encryption/decryption is performed by the MechaCon processor. As such, this module does not include or require any encryption keys.
The source code for this module is based upon the source code from FMCB Installer v0.987.

---

## Security manager RPC server

Page: <https://ps2dev.github.io/ps2sdk/md_iop_security_secrsif__r_e_a_d_m_e.html>

Remote procedure call server for the secrman module.
Intended to be used with the libsecr EE RPC client library.
The source code for this module is based upon the source code from FMCB Installer v0.987.

---

## SIO2 Manager

Page: <https://ps2dev.github.io/ps2sdk/md_iop_sio_sio2man__r_e_a_d_m_e.html>

This module is an abstraction layer for the SIO2 interface used for memory card and controller ports. This implementation of the module has backwards compatibility features to allow different versions of e.g. mcman, padman, mcxman, mtapman, rmman, imodeman, sio2d, mc2_d, ds2u_d to link and operate correctly.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- sio2man -> The recommended version.
- sio2man-nano -> For memory savings.
- sio2log -> For debug and logging purposes.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## Clear SPU module

Page: <https://ps2dev.github.io/ps2sdk/md_iop_sound_clearspu__r_e_a_d_m_e.html>

This module clears the SPU2 to a known state.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- clearspu -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## Extended Sound Library for SPU2

Page: <https://ps2dev.github.io/ps2sdk/md_iop_sound_libsnd2__r_e_a_d_m_e.html>

This is a port of libsnd from PS1 to use the SPU2 processor.

---

## Basic Sound Library for SPU2

Page: <https://ps2dev.github.io/ps2sdk/md_iop_sound_libspu2__r_e_a_d_m_e.html>

This is a port of libspu from PS1 to use the SPU2 processor.

---

## Remote SPU2 Driver

Page: <https://ps2dev.github.io/ps2sdk/md_iop_sound_rspu2drv__r_e_a_d_m_e.html>

This module allows accessing the SPU2 remotely from the EE via SIF.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- rspu2drv -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## Sound data (HD file) access library

Page: <https://ps2dev.github.io/ps2sdk/md_iop_sound_sdhd__r_e_a_d_m_e.html>

This module provides functions to access sound banks stored in HD files.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- sdhd -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## Sound Device Remote Library

Page: <https://ps2dev.github.io/ps2sdk/md_iop_sound_sdrdrv__r_e_a_d_m_e.html>

This module is a IOP-side SIF RPC server for accessing libsd functions.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- sdrdrv -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## Sound data (SQ file) access library

Page: <https://ps2dev.github.io/ps2sdk/md_iop_sound_sdsq__r_e_a_d_m_e.html>

This module provides functions to access sequenced music stored in SQ files.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- sdsq -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## Board information module

Page: <https://ps2dev.github.io/ps2sdk/md_iop_system_boardinf__r_e_a_d_m_e.html>

This module registers boot modes 6 and 7 to values related to DTL-T boards.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- boardinf -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, you must integrate the module into an IOPRP image, then load the image with UDNL.\ Using LoadModule or LoadModuleBuffer directly will not work, because the module is already loaded at IOP boot.

---

## DMA Controller Manager

Page: <https://ps2dev.github.io/ps2sdk/md_iop_system_dmacman__r_e_a_d_m_e.html>

This module provides functions to manage the DMA controller (DMAC).
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- dmacman -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, you must integrate the module into an IOPRP image, then load the image with UDNL.\ Using LoadModule or LoadModuleBuffer directly will not work, because the module is already loaded at IOP boot.

---

## Dummy IOP Module

Page: <https://ps2dev.github.io/ps2sdk/md_iop_system_dummymod__r_e_a_d_m_e.html>

This module is a minimal module intended to be used where a module is used but a no-op is desired, such as a module in an IOPRP image.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- dummymod -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## EE Configuration Module

Page: <https://ps2dev.github.io/ps2sdk/md_iop_system_eeconf__r_e_a_d_m_e.html>

This module reads configuration data needed by EE, and also sets up DVE, DECKARD region/video mode/MAC address information, and an unknown device.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- eeconf -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## EE Synchronization Module

Page: <https://ps2dev.github.io/ps2sdk/md_iop_system_eesync__r_e_a_d_m_e.html>

This module will wait for SIF to be initialized.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- eesync -> The recommended version.
- eesync-nano -> For memory savings.
#### How to use this module in your program
In order to use this module in your program, you must integrate the module into an IOPRP image, then load the image with UDNL.\ Using LoadModule or LoadModuleBuffer directly will not work, because the module is already loaded at IOP boot.

---

## Exception manager

Page: <https://ps2dev.github.io/ps2sdk/md_iop_system_excepman__r_e_a_d_m_e.html>

This module provides functions to manage exceptions.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- excepman -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, you must integrate the module into an IOPRP image, then load the image with UDNL.\ Using LoadModule or LoadModuleBuffer directly will not work, because the module is already loaded at IOP boot.

---

## Heap library

Page: <https://ps2dev.github.io/ps2sdk/md_iop_system_heaplib__r_e_a_d_m_e.html>

This module provides functions related to heap management.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- heaplib -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, you must integrate the module into an IOPRP image, then load the image with UDNL.\ Using LoadModule or LoadModuleBuffer directly will not work, because the module is already loaded at IOP boot.

---

## IOP Greeting

Page: <https://ps2dev.github.io/ps2sdk/md_iop_system_igreeting__r_e_a_d_m_e.html>

This module will print the following information:
- Reboot type (hard reset boot/soft reboot/update reboot/update reboot complete)
- Board type (DTL-T only)
- Board info (DTL-T only)
- ROMGEN string
- CPUID value
- CACH_CONFIG value
- Memory size in MB
- Whether in PS or IOP mode (IOP only)
- Whether using Flash ROM or ROM (DTL-T only)
- EXTINFO comment
- DIP switches (DTL-T only)
- EE boot parameter (DTL-T only)
- IOP boot parameter (DTL-T only)
- DMA_WIDE_CH value (DTL-T only)
Additionally, it will enable SSBUS if DIP switch 5 is enabled (DTL-T only)
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- igreeting -> The recommended version.
- igreeting-dtlt -> For DTL-T systems.
#### How to use this module in your program
In order to use this module in your program, you must integrate the module into an IOPRP image, then load the image with UDNL.\ Using LoadModule or LoadModuleBuffer directly will not work, because the module is already loaded at IOP boot.

---

## Interrupt Manager

Page: <https://ps2dev.github.io/ps2sdk/md_iop_system_intrman__r_e_a_d_m_e.html>

This module provides functions to manage interrupts.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- intrman -> The recommended version.
- intrmanp -> The version supporting PS1 mode.
#### How to use this module in your program
In order to use this module in your program, you must integrate the module into an IOPRP image, then load the image with UDNL.\ Using LoadModule or LoadModuleBuffer directly will not work, because the module is already loaded at IOP boot.

---

## I/O Manager

Page: <https://ps2dev.github.io/ps2sdk/md_iop_system_ioman__r_e_a_d_m_e.html>

This is an implementation of ioman for reference purposes only. You probably want to use iomanx, which is an extended version of this module, instead.
#### How to use this module in your program
In order to use this module in your program, you must integrate the module into an IOPRP image, then load the image with UDNL.\ Using LoadModule or LoadModuleBuffer directly will not work, because the module is already loaded at IOP boot.

---

## Module Manager

Page: <https://ps2dev.github.io/ps2sdk/md_iop_system_loadcore__r_e_a_d_m_e.html>

This module provides functions to manage IRX modules.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- loadcore -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, you must integrate the module into an IOPRP image, then load the image with UDNL.\ Using LoadModule or LoadModuleBuffer directly will not work, because the module is already loaded at IOP boot.

---

## RPC server for executable loading management

Page: <https://ps2dev.github.io/ps2sdk/md_iop_system_loadfile__r_e_a_d_m_e.html>

This module provides a RPC server for managing and loading ELF and IRX files.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- loadfile -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, you must integrate the module into an IOPRP image, then load the image with UDNL.\ Using LoadModule or LoadModuleBuffer directly will not work, because the module is already loaded at IOP boot.

---

## IOP module loader

Page: <https://ps2dev.github.io/ps2sdk/md_iop_system_modload__r_e_a_d_m_e.html>

This module provides functions for managing and loading IOP executable files.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- modload -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, you must integrate the module into an IOPRP image, then load the image with UDNL.\ Using LoadModule or LoadModuleBuffer directly will not work, because the module is already loaded at IOP boot.

---

## Multi-threaded SIF service

Page: <https://ps2dev.github.io/ps2sdk/md_iop_system_msifrpc__r_e_a_d_m_e.html>

This module provides functions to allow multi-threaded SIF RPC operation.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- msifrpc -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## Reboot command server

Page: <https://ps2dev.github.io/ps2sdk/md_iop_system_reboot__r_e_a_d_m_e.html>

This module provides provides a server for calling the reboot function of modload.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- reboot -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, you must integrate the module into an IOPRP image, then load the image with UDNL.\ Using LoadModule or LoadModuleBuffer directly will not work, because the module is already loaded at IOP boot.

---

## Remote Reset

Page: <https://ps2dev.github.io/ps2sdk/md_iop_system_rmreset__r_e_a_d_m_e.html>

This module will reset the SCPH-10160 IR receiver to gamepad emulation mode.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- rmreset -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## SIF CMD

Page: <https://ps2dev.github.io/ps2sdk/md_iop_system_sifcmd__r_e_a_d_m_e.html>

This module provides functions to handle CoMmanDs and Remote Procedure Calls through Subsystem InterFace.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- sifcmd -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, you must integrate the module into an IOPRP image, then load the image with UDNL.\ Using LoadModule or LoadModuleBuffer directly will not work, because the module is already loaded at IOP boot.

---

## SIF Initialization

Page: <https://ps2dev.github.io/ps2sdk/md_iop_system_sifinit__r_e_a_d_m_e.html>

This module initializes SIF.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- sifinit -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, you must integrate the module into an IOPRP image, then load the image with UDNL.\ Using LoadModule or LoadModuleBuffer directly will not work, because the module is already loaded at IOP boot.

---

## SIF Manager

Page: <https://ps2dev.github.io/ps2sdk/md_iop_system_sifman__r_e_a_d_m_e.html>

This module provides functions to manage the Subsystem InterFace (SIF).
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- sifman -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, you must integrate the module into an IOPRP image, then load the image with UDNL.\ Using LoadModule or LoadModuleBuffer directly will not work, because the module is already loaded at IOP boot.

---

## SSBUSC manager

Page: <https://ps2dev.github.io/ps2sdk/md_iop_system_ssbusc__r_e_a_d_m_e.html>

This module provides functions to manage the SSBUSC chip.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- ssbusc -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, you must integrate the module into an IOPRP image, then load the image with UDNL.\ Using LoadModule or LoadModuleBuffer directly will not work, because the module is already loaded at IOP boot.

---

## Standard I/O module

Page: <https://ps2dev.github.io/ps2sdk/md_iop_system_stdio__r_e_a_d_m_e.html>

This module provides standard I/O functions.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- stdio -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, you must integrate the module into an IOPRP image, then load the image with UDNL.\ Using LoadModule or LoadModuleBuffer directly will not work, because the module is already loaded at IOP boot.

---

## System C Library

Page: <https://ps2dev.github.io/ps2sdk/md_iop_system_sysclib__r_e_a_d_m_e.html>

IOP System C library.\ This library is an open source implementation of the feature set of SYSCLIB in SCE SDK 3.1.0, compared to the feature set of SYSCLIB in ROM, which is based on SCE SDK 1.3.4.
#### Pulled sources
This library uses code from open source libraries, so their licenses apply.
embeddedartistry/libc bfa3d49: https://github.com/embeddedartistry/libc\ musl 1.2.2: https://musl.libc.org/\ eyalroz/printf 19a487c: https://github.com/eyalroz/printf\ newlib 4.1.0: https://sourceware.org/newlib/
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- sysclib -> The recommended version.\ Has the accelerated assembly versions of functions.
- sysclib-nano -> For memory savings.\ Smaller than the original SCE version.
- sysclib-full -> Based on sysclib, but its format series of functions\ supports long long and floating point. Around double the size.
#### How to use this module in your program
In order to use this module in your program, you must integrate the module into an IOPRP image, then load the image with UDNL.\ Using LoadModule or LoadModuleBuffer directly will work, but is not recommended because the old version of the module will remain in memory.

---

## System memory manager

Page: <https://ps2dev.github.io/ps2sdk/md_iop_system_sysmem__r_e_a_d_m_e.html>

This module provides functions to manage the system memory.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- sysmem -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, you must integrate the module into an IOPRP image, then load the image with UDNL.\ Using LoadModule or LoadModuleBuffer directly will not work, because the module is already loaded at IOP boot.

---

## Vertical blank service

Page: <https://ps2dev.github.io/ps2sdk/md_iop_system_vblank__r_e_a_d_m_e.html>

This module provides functions to allow callbacks to be called when a vertical blank event occurs.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- vblank -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, you must integrate the module into an IOPRP image, then load the image with UDNL.\ Using LoadModule or LoadModuleBuffer directly will not work, because the module is already loaded at IOP boot.

---

## USB Automatic Module Loader

Page: <https://ps2dev.github.io/ps2sdk/md_iop_usb_usbmload__r_e_a_d_m_e.html>

This module provides functions to allow IOP modules to be automatically loaded and unloaded when a USB device is plugged based on its characteristics.
#### Configurations
There are multiple configurations of this library, allowing the choice of balancing between size, speed, and features.
- usbmload -> The recommended version.
#### How to use this module in your program
In order to use this module in your program, use LoadModule or \ LoadModuleBuffer with no arguments.

---

## srxfixup

Page: <https://ps2dev.github.io/ps2sdk/md_tools_srxfixup__r_e_a_d_m_e.html>

This tool mainly handles generation of IRX and ERX files, mainly used as relocatable executables or libraries. This tool performs the following tasks on relocatable ELF files in order to ensure that loadcore can load it as a relocatable file:
- Sets the ELF header e_type to 0xFF80, 0xFF81, or 0xFF91, depending on the features and architecture used
- Creates the .iopmod or .eemod section and first program header, containing metadata about the file, such as name, version, and section sizes/offsets
- Rebuilds relocations
#### Aliases
This tool provides the following:
- iopfixup
- irx-strip
- eefixup
- erx-strip
#### Usage
To see usage and possible command line arguments that can be used with the program, run it without arguments.
#### Zero-.text symbol check
When processing a relocatable ELF (ET_REL), srxfixup checks for function or no-type symbols in the .text section whose st_value is exactly 0. Such symbols indicate that real code was placed first in .text by the linker. If an IOP export table has a zeroed or uninitialized entry, the dispatcher will issue a jal 0x0 — silently jumping into whatever function sits at .text offset 0 instead of faulting. The symbols _start and _ftext are excluded because they are entry points / linker labels that are never dispatched through an export table.
If any offending symbol is found, srxfixup prints an error like:
```
ERROR: foo.irx: symbol 'bar' (sym#3) is in .text with value 0 -- if this module has an export table, put exports.o first in IOP_OBJS and move _retonly after DECLARE_EXPORT_TABLE in exports.tab; otherwise use --allow-zero-text.
```
and exits with a non-zero status so the build fails.
For modules with an export table, the fix is to ensure exports.o is first in IOP_OBJS and that the _retonly definition appears after DECLARE_EXPORT_TABLE in exports.tab. This places the export-table struct (STT_OBJECT) at .text offset 0 instead of function code.
For modules without an export table, the jal 0x0 hazard does not apply. Use --allow-zero-text to suppress the check. The IOP Rules.make automatically passes this flag when exports.o is not present in IOP_OBJS.

---
