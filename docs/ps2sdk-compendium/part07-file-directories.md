# Part 7 — File Directories

## PS2SDK: common -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000000_000006.html>

###### common → iop Relation
| File in common | Includes file in iop |
| include / iox_stat.h | kernel / include / sys / time.h |
| include / ps2ip_rpc.h | kernel / include / sys / time.h |
| sbus / src / iop_sbus.c | system / loadcore / include / loadcore.h |
| sbus / src / iop_sbus.c | system / stdio / include / stdio.h |
| sbus / src / iop_sbus.c | system / threadman / include / thbase.h |
| sbus / src / irx_imports.h | kernel / include / irx.h |
| sbus / src / irx_imports.h | cdvd / cdvdman / include / cdvdman.h |
| sbus / src / irx_imports.h | system / loadcore / include / loadcore.h |
| sbus / src / irx_imports.h | system / sifman / include / sifman.h |
| sbus / src / irx_imports.h | system / stdio / include / stdio.h |
| sbus / src / irx_imports.h | system / sysclib / include / sysclib.h |
| sbus / src / irx_imports.h | system / threadman / include / thbase.h |
| sbus / src / irx_imports.h | system / ioman / include / ioman.h |
| sbus / src / irx_imports.h | system / modload / include / modload.h |
| sbus / src / irx_imports.h | system / intrman / include / intrman.h |
| sbus / src / irx_imports.h | system / excepman / include / excepman.h |
| sbus / src / sbus_priv.h | system / intrman / include / intrman.h |
| sbus / src / sbus_priv.h | system / sysclib / include / sysclib.h |
| sbus / src / sif2cmd.c | system / sysclib / include / sysclib.h |

---

## PS2SDK: common -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000000_000056.html>

###### common → cdvd Relation
| File in common | Includes file in iop/cdvd |
| sbus / src / irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: common -&gt; cdvdman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000000_000061.html>

###### common → cdvdman Relation
| File in common | Includes file in iop/cdvd/cdvdman |
| sbus / src / irx_imports.h | include / cdvdman.h |

---

## PS2SDK: common -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000000_000223.html>

###### common → system Relation
| File in common | Includes file in iop/system |
| sbus / src / iop_sbus.c | loadcore / include / loadcore.h |
| sbus / src / iop_sbus.c | stdio / include / stdio.h |
| sbus / src / iop_sbus.c | threadman / include / thbase.h |
| sbus / src / irx_imports.h | loadcore / include / loadcore.h |
| sbus / src / irx_imports.h | sifman / include / sifman.h |
| sbus / src / irx_imports.h | stdio / include / stdio.h |
| sbus / src / irx_imports.h | sysclib / include / sysclib.h |
| sbus / src / irx_imports.h | threadman / include / thbase.h |
| sbus / src / irx_imports.h | ioman / include / ioman.h |
| sbus / src / irx_imports.h | modload / include / modload.h |
| sbus / src / irx_imports.h | intrman / include / intrman.h |
| sbus / src / irx_imports.h | excepman / include / excepman.h |
| sbus / src / sbus_priv.h | intrman / include / intrman.h |
| sbus / src / sbus_priv.h | sysclib / include / sysclib.h |
| sbus / src / sif2cmd.c | sysclib / include / sysclib.h |

---

## PS2SDK: common -&gt; excepman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000000_000234.html>

###### common → excepman Relation
| File in common | Includes file in iop/system/excepman |
| sbus / src / irx_imports.h | include / excepman.h |

---

## PS2SDK: common -&gt; intrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000000_000240.html>

###### common → intrman Relation
| File in common | Includes file in iop/system/intrman |
| sbus / src / irx_imports.h | include / intrman.h |
| sbus / src / sbus_priv.h | include / intrman.h |

---

## PS2SDK: common -&gt; ioman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000000_000242.html>

###### common → ioman Relation
| File in common | Includes file in iop/system/ioman |
| sbus / src / irx_imports.h | include / ioman.h |

---

## PS2SDK: common -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000000_000248.html>

###### common → loadcore Relation
| File in common | Includes file in iop/system/loadcore |
| sbus / src / iop_sbus.c | include / loadcore.h |
| sbus / src / irx_imports.h | include / loadcore.h |

---

## PS2SDK: common -&gt; modload Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000000_000252.html>

###### common → modload Relation
| File in common | Includes file in iop/system/modload |
| sbus / src / irx_imports.h | include / modload.h |

---

## PS2SDK: common -&gt; sifman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000000_000266.html>

###### common → sifman Relation
| File in common | Includes file in iop/system/sifman |
| sbus / src / irx_imports.h | include / sifman.h |

---

## PS2SDK: common -&gt; stdio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000000_000272.html>

###### common → stdio Relation
| File in common | Includes file in iop/system/stdio |
| sbus / src / iop_sbus.c | include / stdio.h |
| sbus / src / irx_imports.h | include / stdio.h |

---

## PS2SDK: common -&gt; sysclib Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000000_000274.html>

###### common → sysclib Relation
| File in common | Includes file in iop/system/sysclib |
| sbus / src / irx_imports.h | include / sysclib.h |
| sbus / src / sbus_priv.h | include / sysclib.h |
| sbus / src / sif2cmd.c | include / sysclib.h |

---

## PS2SDK: common -&gt; threadman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000000_000276.html>

###### common → threadman Relation
| File in common | Includes file in iop/system/threadman |
| sbus / src / iop_sbus.c | include / thbase.h |
| sbus / src / irx_imports.h | include / thbase.h |

---

## PS2SDK: common -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000000_000324.html>

###### common → kernel Relation
| File in common | Includes file in ee/kernel |
| sbus / src / ee_sbus.c | include / kernel.h |

---

## PS2SDK: common -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000000_000412.html>

###### common → include Relation
| File in common | Includes file in ee/kernel/include |
| sbus / src / ee_sbus.c | kernel.h |

---

## PS2SDK: common -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000000_000496.html>

###### common → include Relation
| File in common | Includes file in iop/cdvd/cdvdman/include |
| sbus / src / irx_imports.h | cdvdman.h |

---

## PS2SDK: common -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000000_000537.html>

###### common → kernel Relation
| File in common | Includes file in iop/kernel |
| include / iox_stat.h | include / sys / time.h |
| include / ps2ip_rpc.h | include / sys / time.h |
| sbus / src / irx_imports.h | include / irx.h |

---

## PS2SDK: common -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000000_000538.html>

###### common → include Relation
| File in common | Includes file in iop/kernel/include |
| include / iox_stat.h | sys / time.h |
| include / ps2ip_rpc.h | sys / time.h |
| sbus / src / irx_imports.h | irx.h |

---

## PS2SDK: common -&gt; sys Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000000_000539.html>

###### common → sys Relation
| File in common | Includes file in iop/kernel/include/sys |
| include / iox_stat.h | time.h |
| include / ps2ip_rpc.h | time.h |

---

## PS2SDK: common -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000000_000571.html>

###### common → include Relation
| File in common | Includes file in iop/system/intrman/include |
| sbus / src / irx_imports.h | intrman.h |
| sbus / src / sbus_priv.h | intrman.h |

---

## PS2SDK: common -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000000_000572.html>

###### common → include Relation
| File in common | Includes file in iop/system/ioman/include |
| sbus / src / irx_imports.h | ioman.h |

---

## PS2SDK: common -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000000_000576.html>

###### common → include Relation
| File in common | Includes file in iop/system/modload/include |
| sbus / src / irx_imports.h | modload.h |

---

## PS2SDK: common -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000000_000579.html>

###### common → include Relation
| File in common | Includes file in iop/system/sifman/include |
| sbus / src / irx_imports.h | sifman.h |

---

## PS2SDK: common -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000000_000583.html>

###### common → include Relation
| File in common | Includes file in iop/system/sysclib/include |
| sbus / src / irx_imports.h | sysclib.h |
| sbus / src / sbus_priv.h | sysclib.h |
| sbus / src / sif2cmd.c | sysclib.h |

---

## PS2SDK: common -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000000_000598.html>

###### common → include Relation
| File in common | Includes file in iop/system/threadman/include |
| sbus / src / iop_sbus.c | thbase.h |
| sbus / src / irx_imports.h | thbase.h |

---

## PS2SDK: common/include -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000001_000006.html>

###### include → iop Relation
| File in common/include | Includes file in iop |
| iox_stat.h | kernel / include / sys / time.h |
| ps2ip_rpc.h | kernel / include / sys / time.h |

---

## PS2SDK: common/sbus -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000003_000001.html>

###### sbus → include Relation
| File in common/sbus | Includes file in common/include |
| include / ps2_sbus.h | ps2_reg_defs.h |
| include / ps2_sbus.h | tamtypes.h |
| src / ee_sbus.c | ps2_reg_defs.h |
| src / ee_sbus.c | tamtypes.h |
| src / ee_sif2.c | tamtypes.h |
| src / ee_sif2.c | ps2_reg_defs.h |
| src / ee_sif2.c | ee_regs.h |
| src / iop_sbus.c | tamtypes.h |
| src / iop_sif2.c | tamtypes.h |
| src / iop_sif2.c | ps2_reg_defs.h |
| src / iop_sif2.c | iop_regs.h |
| src / ps2_dbg.c | tamtypes.h |
| src / ps2_sbus.c | tamtypes.h |
| src / ps2_sbus.c | ps2_reg_defs.h |
| src / ps2_sif.c | tamtypes.h |
| src / ps2_sif.c | ps2_reg_defs.h |
| src / sbus_priv.h | tamtypes.h |
| src / sbus_priv.h | ps2_reg_defs.h |
| src / sif2cmd.c | tamtypes.h |
| src / sif2cmd.c | ps2_reg_defs.h |

---

## PS2SDK: common/sbus -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000003_000006.html>

###### sbus → iop Relation
| File in common/sbus | Includes file in iop |
| src / iop_sbus.c | system / loadcore / include / loadcore.h |
| src / iop_sbus.c | system / stdio / include / stdio.h |
| src / iop_sbus.c | system / threadman / include / thbase.h |
| src / irx_imports.h | kernel / include / irx.h |
| src / irx_imports.h | cdvd / cdvdman / include / cdvdman.h |
| src / irx_imports.h | system / loadcore / include / loadcore.h |
| src / irx_imports.h | system / sifman / include / sifman.h |
| src / irx_imports.h | system / stdio / include / stdio.h |
| src / irx_imports.h | system / sysclib / include / sysclib.h |
| src / irx_imports.h | system / threadman / include / thbase.h |
| src / irx_imports.h | system / ioman / include / ioman.h |
| src / irx_imports.h | system / modload / include / modload.h |
| src / irx_imports.h | system / intrman / include / intrman.h |
| src / irx_imports.h | system / excepman / include / excepman.h |
| src / sbus_priv.h | system / intrman / include / intrman.h |
| src / sbus_priv.h | system / sysclib / include / sysclib.h |
| src / sif2cmd.c | system / sysclib / include / sysclib.h |

---

## PS2SDK: common/sbus -&gt; ee Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000003_000306.html>

###### sbus → ee Relation
| File in common/sbus | Includes file in ee |
| src / ee_sbus.c | kernel / include / kernel.h |

---

## PS2SDK: common/sbus/include -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000004_000001.html>

###### include → include Relation
| File in common/sbus/include | Includes file in common/include |
| ps2_sbus.h | ps2_reg_defs.h |
| ps2_sbus.h | tamtypes.h |

---

## PS2SDK: common/sbus/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000005_000001.html>

###### src → include Relation
| File in common/sbus/src | Includes file in common/include |
| ee_sbus.c | ps2_reg_defs.h |
| ee_sbus.c | tamtypes.h |
| ee_sif2.c | ee_regs.h |
| ee_sif2.c | ps2_reg_defs.h |
| ee_sif2.c | tamtypes.h |
| iop_sbus.c | tamtypes.h |
| iop_sif2.c | iop_regs.h |
| iop_sif2.c | ps2_reg_defs.h |
| iop_sif2.c | tamtypes.h |
| ps2_dbg.c | tamtypes.h |
| ps2_sbus.c | ps2_reg_defs.h |
| ps2_sbus.c | tamtypes.h |
| ps2_sif.c | ps2_reg_defs.h |
| ps2_sif.c | tamtypes.h |
| sbus_priv.h | ps2_reg_defs.h |
| sbus_priv.h | tamtypes.h |
| sif2cmd.c | ps2_reg_defs.h |
| sif2cmd.c | tamtypes.h |

---

## PS2SDK: common/sbus/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000005_000004.html>

###### src → include Relation
| File in common/sbus/src | Includes file in common/sbus/include |
| ee_sbus.c | ps2_sbus.h |
| ee_sif2.c | ps2_sbus.h |
| iop_sbus.c | ps2_sbus.h |
| iop_sif2.c | ps2_sbus.h |
| ps2_dbg.c | ps2_sbus.h |
| ps2_sbus.c | ps2_sbus.h |
| ps2_sif.c | ps2_sbus.h |
| sif2cmd.c | ps2_sbus.h |

---

## PS2SDK: common/sbus/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000005_000006.html>

###### src → iop Relation
| File in common/sbus/src | Includes file in iop |
| iop_sbus.c | system / loadcore / include / loadcore.h |
| iop_sbus.c | system / stdio / include / stdio.h |
| iop_sbus.c | system / threadman / include / thbase.h |
| irx_imports.h | cdvd / cdvdman / include / cdvdman.h |
| irx_imports.h | system / excepman / include / excepman.h |
| irx_imports.h | system / intrman / include / intrman.h |
| irx_imports.h | system / ioman / include / ioman.h |
| irx_imports.h | kernel / include / irx.h |
| irx_imports.h | system / loadcore / include / loadcore.h |
| irx_imports.h | system / modload / include / modload.h |
| irx_imports.h | system / sifman / include / sifman.h |
| irx_imports.h | system / stdio / include / stdio.h |
| irx_imports.h | system / sysclib / include / sysclib.h |
| irx_imports.h | system / threadman / include / thbase.h |
| sbus_priv.h | system / intrman / include / intrman.h |
| sbus_priv.h | system / sysclib / include / sysclib.h |
| sif2cmd.c | system / sysclib / include / sysclib.h |

---

## PS2SDK: common/sbus/src -&gt; ee Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000005_000306.html>

###### src → ee Relation
| File in common/sbus/src | Includes file in ee |
| ee_sbus.c | kernel / include / kernel.h |

---

## PS2SDK: iop -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000006_000000.html>

###### iop → common Relation
| File in iop | Includes file in common |
| arcade / accore / include / accore.h | include / tamtypes.h |
| arcade / acdev / include / acdev.h | include / tamtypes.h |
| dev9 / dev9 / include / aifdev9.h | include / aifregs.h |
| fs / libbdm / include / bd_cache.h | include / tamtypes.h |
| fs / libbdm / include / bd_defrag.h | include / tamtypes.h |
| fs / libbdm / include / bd_defrag.h | include / usbhdfsd-common.h |
| tcpip / tcpip-base / include / arch / cc.h | include / errno.h |
| cdvd / cdvdman / include / cdvdman.h | include / libcdvd-common.h |
| dev9 / dev9 / include / dev9.h | include / hdd-ioctl.h |
| system / ioman / include / ioman.h | include / io_common.h |
| system / ioman / include / ioman_mod.h | include / io_common.h |
| system / ioman / include / ioman_mod.h | include / iox_stat.h |
| system / iomanx / include / iomanX.h | include / io_common.h |
| system / iomanx / include / iomanX.h | include / iox_stat.h |
| debug / iop_sbusdbg / include / iop_sbusdbg.h | include / ps2_debug.h |
| debug / iopdebug / include / iopdebug.h | include / iop_cop0_defs.h |
| debug / iopdebug / include / iopdebug.h | include / ps2_debug.h |
| hdd / libapa / include / libapa.h | include / hdd-ioctl.h |
| sound / libsd / include / libsd.h | include / libsd-common.h |
| sound / libsnd2 / src / include / libsnd2_internal.h | include / tamtypes.h |
| sound / libspu2 / include / libspu2_internal.h | include / tamtypes.h |
| memorycard / mcman / include / mcman.h | include / libmc-common.h |
| network / netman / include / netdev.h | include / tamtypes.h |
| tcpip / tcpip / include / ps2ip.h | include / tcpip.h |
| input / rmman / include / rmman.h | include / librm-common.h |
| sound / rspu2drv / src / include / rs_i.h | include / tamtypes.h |
| arcade / s147nand / include / s147nand.h | include / tamtypes.h |
| iLink / IEEE1394_bd / src / include / sbp2_disk.h | include / tamtypes.h |
| sound / sdrdrv / include / sdrdrv.h | include / libsdr-common.h |
| security / secrman / include / secrman.h | include / libsecr-common.h |
| system / sysclib / include / setjmp.h | include / tamtypes.h |
| system / sifcmd / include / sifcmd.h | include / sifcmd-common.h |
| system / sifcmd / include / sifcmd.h | include / sifrpc-common.h |
| debug / sior / include / sior.h | include / sior-common.h |
| network / smap / include / smap_modular.h | include / tamtypes.h |
| system / threadman / src / include / thcommon.h | include / tamtypes.h |
| kernel / include / types.h | include / tamtypes.h |
| usb / usbhdfsd / include / usbhdfsd.h | include / usbhdfsd-common.h |
| cdvd / xatapi / include / xatapi.h | include / tamtypes.h |
| system / sysclib / src / newlib / libc / machine / mips / machine / fenv-softfloat.h | include / errno.h |
| network / spduart / src / spduart.c | include / speedregs.h |
| arcade / romwrite / src / romwrite.c | include / s147_mmio_hwport.h |
| debug / iop_sbusdbg / src / irx_imports.h | sbus / include / ps2_sbus.h |
| debug / iop_sbusdbg / src / main.c | include / tamtypes.h |
| debug / iop_sbusdbg / src / main.c | include / iop_cop0_defs.h |
| debug / iop_sbusdbg / src / main.c | sbus / include / ps2_sbus.h |
| debug / iop_sbusdbg / src / sbus_dbg.c | include / tamtypes.h |
| debug / iop_sbusdbg / src / sbus_dbg.c | include / ps2_debug.h |
| debug / iop_sbusdbg / src / sbus_dbg.c | sbus / include / ps2_sbus.h |
| debug / iop_sbusdbg / src / sbus_tty.c | include / tamtypes.h |
| debug / iop_sbusdbg / src / sbus_tty.c | include / errno.h |
| debug / iop_sbusdbg / src / sbus_tty.c | include / ps2_debug.h |
| debug / iop_sbusdbg / src / sbus_tty.c | sbus / include / ps2_sbus.h |
| debug / iop_sbusdbg / src / sbus_tty.h | include / tamtypes.h |
| network / udptty / src / udptty.c | include / tamtypes.h |
| network / udptty / src / udptty.c | include / errno.h |
| cdvd / cdvdman / src / cdvdman.c | include / cdvd-ioctl.h |
| cdvd / cdvdman / src / cdvdman.c | include / dev5_mmio_hwport.h |
| cdvd / cdvdman / src / cdvdman.c | include / errno.h |
| cdvd / cdvdman / src / cdvdman.c | include / hdd-ioctl.h |
| cdvd / cdvdman / src / cdvdman.c | include / iop_mmio_hwport.h |
| cdvd / cdvdman / src / cdvdman.c | include / mipscopaccess.h |
| fs / devfs / src / devfs.c | include / errno.h |
| system / modload / src / modload.c | include / mipscopaccess.h |
| system / loadfile / src / loadfile.c | include / loadfile-common.h |
| fs / eromdrv / src / eromdrv.c | include / errno.h |
| arcade / acatad / src / acatad.c | include / atahw.h |
| usb / keyboard / src / ps2kbd.c | include / errno.h |
| sio / mx4sio_bd / src / spi_sdcard_crc7.h | include / tamtypes.h |
| hdd / hdck / src / hdck.c | include / errno.h |
| hdd / hdck / src / hdck.c | include / hdd-ioctl.h |
| memorycard / mcman / src / mcman-internal.h | include / errno.h |
| cdvd / cdvdfsv / src / cdvdfsv.c | include / cdvd-ioctl.h |
| cdvd / cdvdfsv / src / cdvdfsv.c | include / libcdvd-rpc.h |
| arcade / s147mdev / src / s147mdev.c | include / errno.h |
| arcade / s147nand / src / s147nand.c | include / errno.h |
| arcade / s147nand / src / s147nand.c | include / iop_mmio_hwport.h |
| arcade / s147nand / src / s147nand.c | include / s147_mmio_hwport.h |
| arcade / accdvd / src / accdvd_internal.h | include / errno.h |
| arcade / accdvd / src / acd.c | include / atahw.h |
| dvrp / dvrfile / src / dvrfile.c | include / speedregs.h |
| dvrp / dvrfile / src / dvrfile.c | include / errno.h |
| arcade / acata / src / ata.c | include / atahw.h |
| arcade / acata / src / atacmd.c | include / atahw.h |
| arcade / acata / src / atapicmd.c | include / atahw.h |
| fs / filexio / src / fileXio_iop.c | include / errno.h |
| fs / filexio / src / fileXio_iop.c | include / fileXio.h |
| fs / bdmfs_fatfs / src / fs_driver.c | include / errno.h |
| fs / bdmfs_fatfs / src / fs_driver.c | include / usbhdfsd-common.h |
| tcpip / tcpip-netman / src / irx_imports.h | include / netman.h |
| tcpip / tcpip-netman / src / ps2ip.c | include / netman.h |
| cdvd / xatapi / src / xatapi.c | include / errno.h |
| cdvd / xatapi / src / xatapi.c | include / blkio-ioctl.h |
| fs / bdm / src / part_driver.c | include / errno.h |
| fs / bdm / src / part_driver_gpt.c | include / errno.h |
| fs / bdm / src / part_driver_mbr.c | include / errno.h |
| system / timrman / src / timrman.c | include / mipscopaccess.h |
| system / timrman / src / timrman.c | include / tamtypes.h |
| fs / romdrv / src / romdrv.c | include / errno.h |
| usb / usbmass_bd / src / scsi.c | include / errno.h |
| usb / usbmass_bd / src / usb_mass.c | include / errno.h |
| usb / usbmass_bd / src / usb_mass.c | include / usbhdfsd-common.h |
| cdvd / cdfs / src / cdfs_iop.c | include / libcdvd-common.h |
| cdvd / cdfs / src / main.c | include / iox_stat.h |
| cdvd / cdfs / src / main.c | include / errno.h |
| fs / subfile / src / subfile.c | include / errno.h |
| debug / sior / src / xprintf.c | include / tamtypes.h |
| debug / sior / src / xprintf.c | include / ps2lib_err.h |
| system / rmreset / src / rmreset.c | include / iop_mmio_hwport.h |
| network / netcnf / src / netcnf.c | include / errno.h |
| cdvd / cdvdstm / src / cdvdstm.c | include / cdvd-ioctl.h |
| cdvd / cdvdstm / src / cdvdstm.c | include / errno.h |
| deckard / xparam / src / xparam.c | include / tamtypes.h |
| deckard / xparam / src / xparam.c | include / iop_regs.h |
| usb / camera / src / ps2cam.c | include / tamtypes.h |
| tcpip / tcpips / src / ps2ips.c | include / ps2ip_rpc.h |
| system / eeconf / src / eeconf.c | include / dev5_mmio_hwport.h |
| system / eeconf / src / eeconf.c | include / iop_mmio_hwport.h |
| cdvd / xesdrv / src / xesdrv.c | include / errno.h |
| fs / vfat / src / fat_driver.c | include / errno.h |
| fs / vfat / src / fat_write.c | include / errno.h |
| fs / vfat / src / fs_driver.c | include / errno.h |
| fs / vfat / src / fs_driver.c | include / usbhdfsd-common.h |
| fs / vfat / src / part_driver.c | include / errno.h |
| fs / vfat / src / scache.c | include / tamtypes.h |
| dev9 / atad / src / ps2atad.c | include / atahw.h |
| iLink / IEEE1394_bd / src / sbp2_driver.c | include / usbhdfsd-common.h |
| iLink / IEEE1394_bd / src / scsi.c | include / errno.h |
| fs / fakehost / src / fakehost.c | include / errno.h |
| debug / iopdebug / src / iop_debug.c | include / tamtypes.h |
| debug / iopdebug / src / iop_debug.c | include / iop_cop0_defs.h |
| debug / iopdebug / src / iop_debug.c | include / ps2_debug.h |
| debug / iopdebug / src / iopdebug_priv.h | include / tamtypes.h |
| debug / iopdebug / src / main.c | include / tamtypes.h |
| system / boardinf / src / boardinf.c | include / iop_mmio_hwport.h |
| hdd / libapa / src / apa.c | include / errno.h |
| hdd / libapa / src / apa.c | include / hdd-ioctl.h |
| hdd / libapa / src / cache.c | include / errno.h |
| hdd / libapa / src / cache.c | include / hdd-ioctl.h |
| hdd / libapa / src / free.c | include / errno.h |
| hdd / libapa / src / free.c | include / hdd-ioctl.h |
| hdd / libapa / src / journal.c | include / errno.h |
| hdd / libapa / src / journal.c | include / hdd-ioctl.h |
| hdd / libapa / src / misc.c | include / errno.h |
| hdd / libapa / src / misc.c | include / hdd-ioctl.h |
| hdd / libapa / src / password.c | include / errno.h |
| hdd / libapa / src / password.c | include / hdd-ioctl.h |
| dvrp / dvrmisc / src / dvrmisc.c | include / speedregs.h |
| dvrp / dvrmisc / src / dvrmisc.c | include / errno.h |
| dvrp / dvripl / src / dvripl.c | include / speedregs.h |
| dvrp / dvripl / src / dvripl.c | include / errno.h |
| system / igreeting / src / igreeting.c | include / iop_mmio_hwport.h |
| system / igreeting / src / igreeting.c | include / tamtypes.h |
| system / igreeting / src / igreeting.c | include / mipscopaccess.h |
| hdd / libpfs / src / bitmap.c | include / errno.h |
| hdd / libpfs / src / block.c | include / errno.h |
| hdd / libpfs / src / blockWrite.c | include / errno.h |
| hdd / libpfs / src / cache.c | include / errno.h |
| hdd / libpfs / src / cache.c | include / hdd-ioctl.h |
| hdd / libpfs / src / dir.c | include / errno.h |
| hdd / libpfs / src / inode.c | include / errno.h |
| hdd / libpfs / src / journal.c | include / hdd-ioctl.h |
| hdd / libpfs / src / misc.c | include / errno.h |
| hdd / libpfs / src / misc.c | include / hdd-ioctl.h |
| hdd / libpfs / src / super.c | include / errno.h |
| hdd / libpfs / src / super.c | include / hdd-ioctl.h |
| hdd / libpfs / src / superWrite.c | include / errno.h |
| hdd / libpfs / src / superWrite.c | include / hdd-ioctl.h |
| sound / sdrdrv / src / sdr_i.h | include / libsdr-common.h |
| hdd / fsck / src / bitmap_fsck.c | include / errno.h |
| hdd / fsck / src / bitmap_fsck.c | include / hdd-ioctl.h |
| hdd / fsck / src / fsck.c | include / errno.h |
| hdd / fsck / src / fsck.c | include / hdd-ioctl.h |
| network / smap / src / smap.c | include / errno.h |
| network / smap / src / smap.c | include / smapregs.h |
| network / smap / src / smap.c | include / speedregs.h |
| network / smap / src / xfer.c | include / errno.h |
| network / smap / src / xfer.c | include / smapregs.h |
| network / smap / src / xfer.c | include / speedregs.h |
| network / smbman / src / smb.c | include / errno.h |
| network / smbman / src / smb.h | include / ps2smb.h |
| network / smbman / src / smb_fio.c | include / io_common.h |
| network / smbman / src / smb_fio.c | include / errno.h |
| network / smbman / src / smb_fio.c | include / ps2smb.h |
| dev9 / hdpro_atad / src / hdproatad.c | include / atahw.h |
| dev9 / poweroff / src / poweroff.c | include / pwroff_rpc.h |
| system / sifman / src / sifman.c | include / mipscopaccess.h |
| system / sifman / src / sifman.c | include / iop_mmio_hwport.h |
| system / sifman / src / sifman.c | include / sif_mmio_hwport.h |
| arcade / s147ctrl / src / s147ctrl.c | include / errno.h |
| arcade / s147ctrl / src / s147ctrl.c | include / s147_mmio_hwport.h |
| dev9 / pvrdrv / src / dvrdrv.c | include / tamtypes.h |
| dev9 / pvrdrv / src / dvrdrv.c | include / speedregs.h |
| usb / usbhdfsd / src / api.c | include / errno.h |
| usb / usbhdfsd / src / usb_driver.c | include / errno.h |
| system / ioman / src / ioman.c | include / errno.h |
| dvrp / dvrav / src / dvrav.c | include / speedregs.h |
| dvrp / dvrav / src / dvrav.c | include / errno.h |
| dvrp / dvrdv / src / dvrdv.c | include / speedregs.h |
| dvrp / dvrdv / src / dvrdv.c | include / errno.h |
| sound / ps2snd / src / adpcm-stream.c | include / ps2snd.h |
| sound / ps2snd / src / ps2snd.c | include / ps2snd.h |
| arcade / acuart / src / tty.c | include / errno.h |
| fs / fileio / src / fileio.c | include / fileio-common.h |
| fs / fileio / src / fileio.c | include / iopheap-common.h |
| fs / netfs / src / ps2_fio.c | include / errno.h |
| iLink / iLinkman / src / iLink.c | include / errno.h |
| debug / ppctty / src / main.c | include / tamtypes.h |
| debug / ppctty / src / main.c | include / iop_regs.h |
| debug / ppctty / src / tty.c | include / tamtypes.h |
| debug / ppctty / src / tty.c | include / errno.h |
| debug / ppctty / src / tty.h | include / tamtypes.h |
| hdd / fssk / src / fssk.c | include / errno.h |
| hdd / fssk / src / fssk.c | include / hdd-ioctl.h |
| hdd / hdsk / src / hdl.c | include / errno.h |
| hdd / hdsk / src / hdl.c | include / hdd-ioctl.h |
| hdd / hdsk / src / hdsk.c | include / errno.h |
| hdd / hdsk / src / hdsk.c | include / hdd-ioctl.h |
| hdd / hdsk / src / sim.c | include / hdd-ioctl.h |
| hdd / pfs / src / pfs.c | include / errno.h |
| hdd / pfs / src / pfs_fio.c | include / errno.h |
| hdd / pfs / src / pfs_fio.c | include / hdd-ioctl.h |
| hdd / pfs / src / pfs_fioctl.c | include / errno.h |
| hdd / pfs / src / pfs_fioctl.c | include / hdd-ioctl.h |
| dev9 / dev9 / src / ps2dev9.c | include / aifregs.h |
| dev9 / dev9 / src / ps2dev9.c | include / dev9regs.h |
| dev9 / dev9 / src / ps2dev9.c | include / speedregs.h |
| dev9 / dev9 / src / ps2dev9.c | include / smapregs.h |
| dev9 / extflash / src / extflash.c | include / dev9regs.h |
| dev9 / extflash / src / extflash.c | include / speedregs.h |
| system / intrman / src / intrman.c | include / mipscopaccess.h |
| system / intrman / src / intrman.c | include / iop_low_memory_globals.h |
| system / intrman / src / intrman.c | include / iop_mmio_hwport.h |
| dvrp / dvr / src / dvr.c | include / speedregs.h |
| dvrp / dvr / src / dvr.c | include / errno.h |
| network / netman / src / netdev.c | include / netman.h |
| network / netman / src / netman.c | include / errno.h |
| network / netman / src / netman.c | include / netman.h |
| network / netman / src / netman.c | include / netman_rpc.h |
| network / netman / src / rpc_client.c | include / errno.h |
| network / netman / src / rpc_client.c | include / netman.h |
| network / netman / src / rpc_client.c | include / netman_rpc.h |
| network / netman / src / rpc_server.c | include / errno.h |
| network / netman / src / rpc_server.c | include / netman.h |
| network / netman / src / rpc_server.c | include / netman_rpc.h |
| fs / http / src / ps2http.c | include / errno.h |
| arcade / s147link / src / s147link.c | include / s147_mmio_hwport.h |
| sio / sio2man / src / sio2man.c | include / iop_mmio_hwport.h |
| iLink / IEEE1394_disk / src / main.c | include / errno.h |
| iLink / IEEE1394_disk / src / scsi.c | include / errno.h |
| debug / ioptrap / src / breakpoint.c | include / mipscopaccess.h |
| system / iomanx / src / iomanX.c | include / errno.h |
| hdd / apa / src / hdd.c | include / errno.h |
| hdd / apa / src / hdd.c | include / hdd-ioctl.h |
| hdd / apa / src / hdd_fio.c | include / errno.h |
| hdd / apa / src / hdd_fio.c | include / hdd-ioctl.h |
| system / udnl / src / udnl.c | include / mipscopaccess.h |
| kernel / include / sys / types.h | include / tamtypes.h |

---

## PS2SDK: iop -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000006_000001.html>

###### iop → include Relation
| File in iop | Includes file in common/include |
| arcade / accore / include / accore.h | tamtypes.h |
| arcade / acdev / include / acdev.h | tamtypes.h |
| dev9 / dev9 / include / aifdev9.h | aifregs.h |
| fs / libbdm / include / bd_cache.h | tamtypes.h |
| fs / libbdm / include / bd_defrag.h | tamtypes.h |
| fs / libbdm / include / bd_defrag.h | usbhdfsd-common.h |
| tcpip / tcpip-base / include / arch / cc.h | errno.h |
| cdvd / cdvdman / include / cdvdman.h | libcdvd-common.h |
| dev9 / dev9 / include / dev9.h | hdd-ioctl.h |
| system / ioman / include / ioman.h | io_common.h |
| system / ioman / include / ioman_mod.h | io_common.h |
| system / ioman / include / ioman_mod.h | iox_stat.h |
| system / iomanx / include / iomanX.h | io_common.h |
| system / iomanx / include / iomanX.h | iox_stat.h |
| debug / iop_sbusdbg / include / iop_sbusdbg.h | ps2_debug.h |
| debug / iopdebug / include / iopdebug.h | iop_cop0_defs.h |
| debug / iopdebug / include / iopdebug.h | ps2_debug.h |
| hdd / libapa / include / libapa.h | hdd-ioctl.h |
| sound / libsd / include / libsd.h | libsd-common.h |
| sound / libsnd2 / src / include / libsnd2_internal.h | tamtypes.h |
| sound / libspu2 / include / libspu2_internal.h | tamtypes.h |
| memorycard / mcman / include / mcman.h | libmc-common.h |
| network / netman / include / netdev.h | tamtypes.h |
| tcpip / tcpip / include / ps2ip.h | tcpip.h |
| input / rmman / include / rmman.h | librm-common.h |
| sound / rspu2drv / src / include / rs_i.h | tamtypes.h |
| arcade / s147nand / include / s147nand.h | tamtypes.h |
| iLink / IEEE1394_bd / src / include / sbp2_disk.h | tamtypes.h |
| sound / sdrdrv / include / sdrdrv.h | libsdr-common.h |
| security / secrman / include / secrman.h | libsecr-common.h |
| system / sysclib / include / setjmp.h | tamtypes.h |
| system / sifcmd / include / sifcmd.h | sifcmd-common.h |
| system / sifcmd / include / sifcmd.h | sifrpc-common.h |
| debug / sior / include / sior.h | sior-common.h |
| network / smap / include / smap_modular.h | tamtypes.h |
| system / threadman / src / include / thcommon.h | tamtypes.h |
| kernel / include / types.h | tamtypes.h |
| usb / usbhdfsd / include / usbhdfsd.h | usbhdfsd-common.h |
| cdvd / xatapi / include / xatapi.h | tamtypes.h |
| system / sysclib / src / newlib / libc / machine / mips / machine / fenv-softfloat.h | errno.h |
| network / spduart / src / spduart.c | speedregs.h |
| arcade / romwrite / src / romwrite.c | s147_mmio_hwport.h |
| debug / iop_sbusdbg / src / main.c | tamtypes.h |
| debug / iop_sbusdbg / src / main.c | iop_cop0_defs.h |
| debug / iop_sbusdbg / src / sbus_dbg.c | tamtypes.h |
| debug / iop_sbusdbg / src / sbus_dbg.c | ps2_debug.h |
| debug / iop_sbusdbg / src / sbus_tty.c | tamtypes.h |
| debug / iop_sbusdbg / src / sbus_tty.c | errno.h |
| debug / iop_sbusdbg / src / sbus_tty.c | ps2_debug.h |
| debug / iop_sbusdbg / src / sbus_tty.h | tamtypes.h |
| network / udptty / src / udptty.c | tamtypes.h |
| network / udptty / src / udptty.c | errno.h |
| cdvd / cdvdman / src / cdvdman.c | cdvd-ioctl.h |
| cdvd / cdvdman / src / cdvdman.c | dev5_mmio_hwport.h |
| cdvd / cdvdman / src / cdvdman.c | errno.h |
| cdvd / cdvdman / src / cdvdman.c | hdd-ioctl.h |
| cdvd / cdvdman / src / cdvdman.c | iop_mmio_hwport.h |
| cdvd / cdvdman / src / cdvdman.c | mipscopaccess.h |
| fs / devfs / src / devfs.c | errno.h |
| system / modload / src / modload.c | mipscopaccess.h |
| system / loadfile / src / loadfile.c | loadfile-common.h |
| fs / eromdrv / src / eromdrv.c | errno.h |
| arcade / acatad / src / acatad.c | atahw.h |
| usb / keyboard / src / ps2kbd.c | errno.h |
| sio / mx4sio_bd / src / spi_sdcard_crc7.h | tamtypes.h |
| hdd / hdck / src / hdck.c | errno.h |
| hdd / hdck / src / hdck.c | hdd-ioctl.h |
| memorycard / mcman / src / mcman-internal.h | errno.h |
| cdvd / cdvdfsv / src / cdvdfsv.c | cdvd-ioctl.h |
| cdvd / cdvdfsv / src / cdvdfsv.c | libcdvd-rpc.h |
| arcade / s147mdev / src / s147mdev.c | errno.h |
| arcade / s147nand / src / s147nand.c | errno.h |
| arcade / s147nand / src / s147nand.c | iop_mmio_hwport.h |
| arcade / s147nand / src / s147nand.c | s147_mmio_hwport.h |
| arcade / accdvd / src / accdvd_internal.h | errno.h |
| arcade / accdvd / src / acd.c | atahw.h |
| dvrp / dvrfile / src / dvrfile.c | speedregs.h |
| dvrp / dvrfile / src / dvrfile.c | errno.h |
| arcade / acata / src / ata.c | atahw.h |
| arcade / acata / src / atacmd.c | atahw.h |
| arcade / acata / src / atapicmd.c | atahw.h |
| fs / filexio / src / fileXio_iop.c | errno.h |
| fs / filexio / src / fileXio_iop.c | fileXio.h |
| fs / bdmfs_fatfs / src / fs_driver.c | errno.h |
| fs / bdmfs_fatfs / src / fs_driver.c | usbhdfsd-common.h |
| tcpip / tcpip-netman / src / irx_imports.h | netman.h |
| tcpip / tcpip-netman / src / ps2ip.c | netman.h |
| cdvd / xatapi / src / xatapi.c | errno.h |
| cdvd / xatapi / src / xatapi.c | blkio-ioctl.h |
| fs / bdm / src / part_driver.c | errno.h |
| fs / bdm / src / part_driver_gpt.c | errno.h |
| fs / bdm / src / part_driver_mbr.c | errno.h |
| system / timrman / src / timrman.c | mipscopaccess.h |
| system / timrman / src / timrman.c | tamtypes.h |
| fs / romdrv / src / romdrv.c | errno.h |
| usb / usbmass_bd / src / scsi.c | errno.h |
| usb / usbmass_bd / src / usb_mass.c | errno.h |
| usb / usbmass_bd / src / usb_mass.c | usbhdfsd-common.h |
| cdvd / cdfs / src / cdfs_iop.c | libcdvd-common.h |
| cdvd / cdfs / src / main.c | iox_stat.h |
| cdvd / cdfs / src / main.c | errno.h |
| fs / subfile / src / subfile.c | errno.h |
| debug / sior / src / xprintf.c | tamtypes.h |
| debug / sior / src / xprintf.c | ps2lib_err.h |
| system / rmreset / src / rmreset.c | iop_mmio_hwport.h |
| network / netcnf / src / netcnf.c | errno.h |
| cdvd / cdvdstm / src / cdvdstm.c | cdvd-ioctl.h |
| cdvd / cdvdstm / src / cdvdstm.c | errno.h |
| deckard / xparam / src / xparam.c | tamtypes.h |
| deckard / xparam / src / xparam.c | iop_regs.h |
| usb / camera / src / ps2cam.c | tamtypes.h |
| tcpip / tcpips / src / ps2ips.c | ps2ip_rpc.h |
| system / eeconf / src / eeconf.c | dev5_mmio_hwport.h |
| system / eeconf / src / eeconf.c | iop_mmio_hwport.h |
| cdvd / xesdrv / src / xesdrv.c | errno.h |
| fs / vfat / src / fat_driver.c | errno.h |
| fs / vfat / src / fat_write.c | errno.h |
| fs / vfat / src / fs_driver.c | errno.h |
| fs / vfat / src / fs_driver.c | usbhdfsd-common.h |
| fs / vfat / src / part_driver.c | errno.h |
| fs / vfat / src / scache.c | tamtypes.h |
| dev9 / atad / src / ps2atad.c | atahw.h |
| iLink / IEEE1394_bd / src / sbp2_driver.c | usbhdfsd-common.h |
| iLink / IEEE1394_bd / src / scsi.c | errno.h |
| fs / fakehost / src / fakehost.c | errno.h |
| debug / iopdebug / src / iop_debug.c | tamtypes.h |
| debug / iopdebug / src / iop_debug.c | iop_cop0_defs.h |
| debug / iopdebug / src / iop_debug.c | ps2_debug.h |
| debug / iopdebug / src / iopdebug_priv.h | tamtypes.h |
| debug / iopdebug / src / main.c | tamtypes.h |
| system / boardinf / src / boardinf.c | iop_mmio_hwport.h |
| hdd / libapa / src / apa.c | errno.h |
| hdd / libapa / src / apa.c | hdd-ioctl.h |
| hdd / libapa / src / cache.c | errno.h |
| hdd / libapa / src / cache.c | hdd-ioctl.h |
| hdd / libapa / src / free.c | errno.h |
| hdd / libapa / src / free.c | hdd-ioctl.h |
| hdd / libapa / src / journal.c | errno.h |
| hdd / libapa / src / journal.c | hdd-ioctl.h |
| hdd / libapa / src / misc.c | errno.h |
| hdd / libapa / src / misc.c | hdd-ioctl.h |
| hdd / libapa / src / password.c | errno.h |
| hdd / libapa / src / password.c | hdd-ioctl.h |
| dvrp / dvrmisc / src / dvrmisc.c | speedregs.h |
| dvrp / dvrmisc / src / dvrmisc.c | errno.h |
| dvrp / dvripl / src / dvripl.c | speedregs.h |
| dvrp / dvripl / src / dvripl.c | errno.h |
| system / igreeting / src / igreeting.c | iop_mmio_hwport.h |
| system / igreeting / src / igreeting.c | tamtypes.h |
| system / igreeting / src / igreeting.c | mipscopaccess.h |
| hdd / libpfs / src / bitmap.c | errno.h |
| hdd / libpfs / src / block.c | errno.h |
| hdd / libpfs / src / blockWrite.c | errno.h |
| hdd / libpfs / src / cache.c | errno.h |
| hdd / libpfs / src / cache.c | hdd-ioctl.h |
| hdd / libpfs / src / dir.c | errno.h |
| hdd / libpfs / src / inode.c | errno.h |
| hdd / libpfs / src / journal.c | hdd-ioctl.h |
| hdd / libpfs / src / misc.c | errno.h |
| hdd / libpfs / src / misc.c | hdd-ioctl.h |
| hdd / libpfs / src / super.c | errno.h |
| hdd / libpfs / src / super.c | hdd-ioctl.h |
| hdd / libpfs / src / superWrite.c | errno.h |
| hdd / libpfs / src / superWrite.c | hdd-ioctl.h |
| sound / sdrdrv / src / sdr_i.h | libsdr-common.h |
| hdd / fsck / src / bitmap_fsck.c | errno.h |
| hdd / fsck / src / bitmap_fsck.c | hdd-ioctl.h |
| hdd / fsck / src / fsck.c | errno.h |
| hdd / fsck / src / fsck.c | hdd-ioctl.h |
| network / smap / src / smap.c | errno.h |
| network / smap / src / smap.c | smapregs.h |
| network / smap / src / smap.c | speedregs.h |
| network / smap / src / xfer.c | errno.h |
| network / smap / src / xfer.c | smapregs.h |
| network / smap / src / xfer.c | speedregs.h |
| network / smbman / src / smb.c | errno.h |
| network / smbman / src / smb.h | ps2smb.h |
| network / smbman / src / smb_fio.c | io_common.h |
| network / smbman / src / smb_fio.c | errno.h |
| network / smbman / src / smb_fio.c | ps2smb.h |
| dev9 / hdpro_atad / src / hdproatad.c | atahw.h |
| dev9 / poweroff / src / poweroff.c | pwroff_rpc.h |
| system / sifman / src / sifman.c | mipscopaccess.h |
| system / sifman / src / sifman.c | iop_mmio_hwport.h |
| system / sifman / src / sifman.c | sif_mmio_hwport.h |
| arcade / s147ctrl / src / s147ctrl.c | errno.h |
| arcade / s147ctrl / src / s147ctrl.c | s147_mmio_hwport.h |
| dev9 / pvrdrv / src / dvrdrv.c | tamtypes.h |
| dev9 / pvrdrv / src / dvrdrv.c | speedregs.h |
| usb / usbhdfsd / src / api.c | errno.h |
| usb / usbhdfsd / src / usb_driver.c | errno.h |
| system / ioman / src / ioman.c | errno.h |
| dvrp / dvrav / src / dvrav.c | speedregs.h |
| dvrp / dvrav / src / dvrav.c | errno.h |
| dvrp / dvrdv / src / dvrdv.c | speedregs.h |
| dvrp / dvrdv / src / dvrdv.c | errno.h |
| sound / ps2snd / src / adpcm-stream.c | ps2snd.h |
| sound / ps2snd / src / ps2snd.c | ps2snd.h |
| arcade / acuart / src / tty.c | errno.h |
| fs / fileio / src / fileio.c | fileio-common.h |
| fs / fileio / src / fileio.c | iopheap-common.h |
| fs / netfs / src / ps2_fio.c | errno.h |
| iLink / iLinkman / src / iLink.c | errno.h |
| debug / ppctty / src / main.c | tamtypes.h |
| debug / ppctty / src / main.c | iop_regs.h |
| debug / ppctty / src / tty.c | tamtypes.h |
| debug / ppctty / src / tty.c | errno.h |
| debug / ppctty / src / tty.h | tamtypes.h |
| hdd / fssk / src / fssk.c | errno.h |
| hdd / fssk / src / fssk.c | hdd-ioctl.h |
| hdd / hdsk / src / hdl.c | errno.h |
| hdd / hdsk / src / hdl.c | hdd-ioctl.h |
| hdd / hdsk / src / hdsk.c | errno.h |
| hdd / hdsk / src / hdsk.c | hdd-ioctl.h |
| hdd / hdsk / src / sim.c | hdd-ioctl.h |
| hdd / pfs / src / pfs.c | errno.h |
| hdd / pfs / src / pfs_fio.c | errno.h |
| hdd / pfs / src / pfs_fio.c | hdd-ioctl.h |
| hdd / pfs / src / pfs_fioctl.c | errno.h |
| hdd / pfs / src / pfs_fioctl.c | hdd-ioctl.h |
| dev9 / dev9 / src / ps2dev9.c | aifregs.h |
| dev9 / dev9 / src / ps2dev9.c | dev9regs.h |
| dev9 / dev9 / src / ps2dev9.c | speedregs.h |
| dev9 / dev9 / src / ps2dev9.c | smapregs.h |
| dev9 / extflash / src / extflash.c | dev9regs.h |
| dev9 / extflash / src / extflash.c | speedregs.h |
| system / intrman / src / intrman.c | mipscopaccess.h |
| system / intrman / src / intrman.c | iop_low_memory_globals.h |
| system / intrman / src / intrman.c | iop_mmio_hwport.h |
| dvrp / dvr / src / dvr.c | speedregs.h |
| dvrp / dvr / src / dvr.c | errno.h |
| network / netman / src / netdev.c | netman.h |
| network / netman / src / netman.c | errno.h |
| network / netman / src / netman.c | netman.h |
| network / netman / src / netman.c | netman_rpc.h |
| network / netman / src / rpc_client.c | errno.h |
| network / netman / src / rpc_client.c | netman.h |
| network / netman / src / rpc_client.c | netman_rpc.h |
| network / netman / src / rpc_server.c | errno.h |
| network / netman / src / rpc_server.c | netman.h |
| network / netman / src / rpc_server.c | netman_rpc.h |
| fs / http / src / ps2http.c | errno.h |
| arcade / s147link / src / s147link.c | s147_mmio_hwport.h |
| sio / sio2man / src / sio2man.c | iop_mmio_hwport.h |
| iLink / IEEE1394_disk / src / main.c | errno.h |
| iLink / IEEE1394_disk / src / scsi.c | errno.h |
| debug / ioptrap / src / breakpoint.c | mipscopaccess.h |
| system / iomanx / src / iomanX.c | errno.h |
| hdd / apa / src / hdd.c | errno.h |
| hdd / apa / src / hdd.c | hdd-ioctl.h |
| hdd / apa / src / hdd_fio.c | errno.h |
| hdd / apa / src / hdd_fio.c | hdd-ioctl.h |
| system / udnl / src / udnl.c | mipscopaccess.h |
| kernel / include / sys / types.h | tamtypes.h |

---

## PS2SDK: iop -&gt; sbus Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000006_000003.html>

###### iop → sbus Relation
| File in iop | Includes file in common/sbus |
| debug / iop_sbusdbg / src / irx_imports.h | include / ps2_sbus.h |
| debug / iop_sbusdbg / src / main.c | include / ps2_sbus.h |
| debug / iop_sbusdbg / src / sbus_dbg.c | include / ps2_sbus.h |
| debug / iop_sbusdbg / src / sbus_tty.c | include / ps2_sbus.h |

---

## PS2SDK: iop -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000006_000004.html>

###### iop → include Relation
| File in iop | Includes file in common/sbus/include |
| debug / iop_sbusdbg / src / irx_imports.h | ps2_sbus.h |
| debug / iop_sbusdbg / src / main.c | ps2_sbus.h |
| debug / iop_sbusdbg / src / sbus_dbg.c | ps2_sbus.h |
| debug / iop_sbusdbg / src / sbus_tty.c | ps2_sbus.h |

---

## PS2SDK: iop/arcade -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000007_000000.html>

###### arcade → common Relation
| File in iop/arcade | Includes file in common |
| acdev / include / acdev.h | include / tamtypes.h |
| accore / include / accore.h | include / tamtypes.h |
| s147nand / include / s147nand.h | include / tamtypes.h |
| romwrite / src / romwrite.c | include / s147_mmio_hwport.h |
| acatad / src / acatad.c | include / atahw.h |
| s147mdev / src / s147mdev.c | include / errno.h |
| s147nand / src / s147nand.c | include / errno.h |
| s147nand / src / s147nand.c | include / iop_mmio_hwport.h |
| s147nand / src / s147nand.c | include / s147_mmio_hwport.h |
| accdvd / src / accdvd_internal.h | include / errno.h |
| accdvd / src / acd.c | include / atahw.h |
| acata / src / ata.c | include / atahw.h |
| acata / src / atacmd.c | include / atahw.h |
| acata / src / atapicmd.c | include / atahw.h |
| s147ctrl / src / s147ctrl.c | include / errno.h |
| s147ctrl / src / s147ctrl.c | include / s147_mmio_hwport.h |
| acuart / src / tty.c | include / errno.h |
| s147link / src / s147link.c | include / s147_mmio_hwport.h |

---

## PS2SDK: iop/arcade -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000007_000056.html>

###### arcade → cdvd Relation
| File in iop/arcade | Includes file in iop/cdvd |
| accdvd / include / accdvd.h | cdvdman / include / cdvdman.h |
| acrtc / src / irx_imports.h | cdvdman / include / cdvdman.h |
| accdvde / src / irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/arcade -&gt; dev9 Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000007_000087.html>

###### arcade → dev9 Relation
| File in iop/arcade | Includes file in iop/dev9 |
| acatad / src / acatad.c | atad / include / atad.h |
| acdev9 / src / acdev9.c | dev9 / include / dev9.h |

---

## PS2SDK: iop/arcade -&gt; fs Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000007_000113.html>

###### arcade → fs Relation
| File in iop/arcade | Includes file in iop/fs |
| acdev / src / irx_imports.h | romdrv / include / romdrv.h |

---

## PS2SDK: iop/arcade -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000007_000223.html>

###### arcade → system Relation
| File in iop/arcade | Includes file in iop/system |
| s147mdev / include / s147mdev.h | ioman / include / ioman.h |
| romwrite / src / irx_imports.h | intrman / include / intrman.h |
| romwrite / src / irx_imports.h | ioman / include / ioman.h |
| romwrite / src / irx_imports.h | sysclib / include / sysclib.h |
| romwrite / src / irx_imports.h | threadman / include / thbase.h |
| romwrite / src / romwrite.c | loadcore / include / loadcore.h |
| acatad / src / irx_imports.h | loadcore / include / loadcore.h |
| acatad / src / irx_imports.h | stdio / include / stdio.h |
| acatad / src / irx_imports.h | sysclib / include / sysclib.h |
| acatad / src / irx_imports.h | threadman / include / thbase.h |
| acflash / src / irx_imports.h | loadcore / include / loadcore.h |
| acflash / src / irx_imports.h | stdio / include / stdio.h |
| acflash / src / irx_imports.h | threadman / include / thbase.h |
| s147mdev / src / irx_imports.h | ioman / include / ioman.h |
| s147mdev / src / irx_imports.h | loadcore / include / loadcore.h |
| s147mdev / src / irx_imports.h | sysclib / include / sysclib.h |
| acfpgald / src / irx_imports.h | ioman / include / ioman.h |
| acfpgald / src / irx_imports.h | stdio / include / stdio.h |
| acfpgald / src / irx_imports.h | sysclib / include / sysclib.h |
| acfpgald / src / irx_imports.h | threadman / include / thbase.h |
| s147nand / src / irx_imports.h | dmacman / include / dmacman.h |
| s147nand / src / irx_imports.h | intrman / include / intrman.h |
| s147nand / src / irx_imports.h | loadcore / include / loadcore.h |
| s147nand / src / irx_imports.h | stdio / include / stdio.h |
| s147nand / src / irx_imports.h | sysclib / include / sysclib.h |
| s147nand / src / irx_imports.h | threadman / include / thbase.h |
| s147nand / src / irx_imports.h | threadman / include / thsemap.h |
| accdvd / src / irx_imports.h | intrman / include / intrman.h |
| accdvd / src / irx_imports.h | ioman / include / ioman.h |
| accdvd / src / irx_imports.h | loadcore / include / loadcore.h |
| accdvd / src / irx_imports.h | stdio / include / stdio.h |
| accdvd / src / irx_imports.h | sysclib / include / sysclib.h |
| accdvd / src / irx_imports.h | threadman / include / thbase.h |
| accdvd / src / irx_imports.h | threadman / include / thevent.h |
| accdvd / src / irx_imports.h | threadman / include / thsemap.h |
| acata / src / irx_imports.h | intrman / include / intrman.h |
| acata / src / irx_imports.h | loadcore / include / loadcore.h |
| acata / src / irx_imports.h | stdio / include / stdio.h |
| acata / src / irx_imports.h | sysclib / include / sysclib.h |
| acata / src / irx_imports.h | threadman / include / thbase.h |
| acmeme / src / irx_imports.h | loadcore / include / loadcore.h |
| acmeme / src / irx_imports.h | stdio / include / stdio.h |
| acmeme / src / irx_imports.h | sysclib / include / sysclib.h |
| acmeme / src / irx_imports.h | threadman / include / thbase.h |
| acjvld / src / irx_imports.h | ioman / include / ioman.h |
| acjvld / src / irx_imports.h | stdio / include / stdio.h |
| acjvld / src / irx_imports.h | sysclib / include / sysclib.h |
| acsram / src / irx_imports.h | loadcore / include / loadcore.h |
| acdev / src / irx_imports.h | intrman / include / intrman.h |
| acdev / src / irx_imports.h | loadcore / include / loadcore.h |
| acdev / src / irx_imports.h | ssbusc / include / ssbusc.h |
| acram / src / irx_imports.h | intrman / include / intrman.h |
| acram / src / irx_imports.h | loadcore / include / loadcore.h |
| acram / src / irx_imports.h | stdio / include / stdio.h |
| acram / src / irx_imports.h | sysclib / include / sysclib.h |
| acram / src / irx_imports.h | threadman / include / thbase.h |
| accore / src / irx_imports.h | dmacman / include / dmacman.h |
| accore / src / irx_imports.h | intrman / include / intrman.h |
| accore / src / irx_imports.h | loadcore / include / loadcore.h |
| accore / src / irx_imports.h | stdio / include / stdio.h |
| s147netb / src / irx_imports.h | ioman / include / ioman.h |
| s147netb / src / irx_imports.h | modload / include / modload.h |
| s147netb / src / irx_imports.h | sysclib / include / sysclib.h |
| s147netb / src / irx_imports.h | threadman / include / thbase.h |
| s147netb / src / s147netb.c | loadcore / include / loadcore.h |
| actimer / src / irx_imports.h | intrman / include / intrman.h |
| actimer / src / irx_imports.h | loadcore / include / loadcore.h |
| actimer / src / irx_imports.h | sysclib / include / sysclib.h |
| actimer / src / irx_imports.h | threadman / include / thbase.h |
| s147ctrl / src / irx_imports.h | intrman / include / intrman.h |
| s147ctrl / src / irx_imports.h | ioman / include / ioman.h |
| s147ctrl / src / irx_imports.h | sifman / include / sifman.h |
| s147ctrl / src / irx_imports.h | sysclib / include / sysclib.h |
| s147ctrl / src / irx_imports.h | threadman / include / thbase.h |
| s147ctrl / src / irx_imports.h | threadman / include / thsemap.h |
| s147ctrl / src / irx_imports.h | timrman / include / timrman.h |
| s147ctrl / src / s147ctrl.c | loadcore / include / loadcore.h |
| acuart / src / irx_imports.h | intrman / include / intrman.h |
| acuart / src / irx_imports.h | loadcore / include / loadcore.h |
| acuart / src / irx_imports.h | stdio / include / stdio.h |
| acuart / src / irx_imports.h | sysclib / include / sysclib.h |
| acuart / src / irx_imports.h | threadman / include / thbase.h |
| acuart / src / irx_imports.h | threadman / include / thevent.h |
| acrtc / src / irx_imports.h | stdio / include / stdio.h |
| acrtc / src / irx_imports.h | threadman / include / thbase.h |
| accdvde / src / irx_imports.h | intrman / include / intrman.h |
| accdvde / src / irx_imports.h | loadcore / include / loadcore.h |
| accdvde / src / irx_imports.h | stdio / include / stdio.h |
| accdvde / src / irx_imports.h | sysclib / include / sysclib.h |
| accdvde / src / irx_imports.h | threadman / include / thbase.h |
| acmem / src / irx_imports.h | intrman / include / intrman.h |
| acmem / src / irx_imports.h | loadcore / include / loadcore.h |
| acmem / src / irx_imports.h | sifman / include / sifman.h |
| acmem / src / irx_imports.h | threadman / include / thbase.h |
| acdev9 / src / irx_imports.h | loadcore / include / loadcore.h |
| acdev9 / src / irx_imports.h | stdio / include / stdio.h |
| s147link / src / irx_imports.h | intrman / include / intrman.h |
| s147link / src / irx_imports.h | loadcore / include / loadcore.h |
| s147link / src / irx_imports.h | stdio / include / stdio.h |
| s147link / src / irx_imports.h | sysclib / include / sysclib.h |
| s147link / src / irx_imports.h | threadman / include / thbase.h |
| acjv / src / irx_imports.h | loadcore / include / loadcore.h |

---

## PS2SDK: iop/arcade -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000007_000537.html>

###### arcade → kernel Relation
| File in iop/arcade | Includes file in iop/kernel |
| acdev / include / acdev.h | include / irx.h |
| accore / include / accore.h | include / irx.h |
| romwrite / src / irx_imports.h | include / irx.h |
| acatad / src / irx_imports.h | include / irx.h |
| acflash / src / irx_imports.h | include / irx.h |
| s147mdev / src / irx_imports.h | include / irx.h |
| acfpgald / src / irx_imports.h | include / irx.h |
| s147nand / src / irx_imports.h | include / irx.h |
| accdvd / src / irx_imports.h | include / irx.h |
| acata / src / irx_imports.h | include / irx.h |
| acmeme / src / irx_imports.h | include / irx.h |
| acjvld / src / irx_imports.h | include / irx.h |
| acsram / src / irx_imports.h | include / irx.h |
| acdev / src / irx_imports.h | include / irx.h |
| acram / src / irx_imports.h | include / irx.h |
| accore / src / irx_imports.h | include / irx.h |
| s147netb / src / irx_imports.h | include / irx.h |
| actimer / src / irx_imports.h | include / irx.h |
| s147ctrl / src / irx_imports.h | include / irx.h |
| acuart / src / irx_imports.h | include / irx.h |
| acrtc / src / irx_imports.h | include / irx.h |
| accdvde / src / irx_imports.h | include / irx.h |
| acmem / src / irx_imports.h | include / irx.h |
| acdev9 / src / irx_imports.h | include / irx.h |
| s147link / src / irx_imports.h | include / irx.h |
| acjv / src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/acata -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000008_000000.html>

###### acata → common Relation
| File in iop/arcade/acata | Includes file in common |
| src / ata.c | include / atahw.h |
| src / atacmd.c | include / atahw.h |
| src / atapicmd.c | include / atahw.h |

---

## PS2SDK: iop/arcade/acata -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000008_000223.html>

###### acata → system Relation
| File in iop/arcade/acata | Includes file in iop/system |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |

---

## PS2SDK: iop/arcade/acata -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000008_000537.html>

###### acata → kernel Relation
| File in iop/arcade/acata | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/acata/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000009_000000.html>

###### src → common Relation
| File in iop/arcade/acata/src | Includes file in common |
| ata.c | include / atahw.h |
| atacmd.c | include / atahw.h |
| atapicmd.c | include / atahw.h |

---

## PS2SDK: iop/arcade/acata/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000009_000223.html>

###### src → system Relation
| File in iop/arcade/acata/src | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |

---

## PS2SDK: iop/arcade/acata/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000009_000537.html>

###### src → kernel Relation
| File in iop/arcade/acata/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/acatad -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000010_000000.html>

###### acatad → common Relation
| File in iop/arcade/acatad | Includes file in common |
| src / acatad.c | include / atahw.h |

---

## PS2SDK: iop/arcade/acatad -&gt; dev9 Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000010_000087.html>

###### acatad → dev9 Relation
| File in iop/arcade/acatad | Includes file in iop/dev9 |
| src / acatad.c | atad / include / atad.h |

---

## PS2SDK: iop/arcade/acatad -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000010_000223.html>

###### acatad → system Relation
| File in iop/arcade/acatad | Includes file in iop/system |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |

---

## PS2SDK: iop/arcade/acatad -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000010_000537.html>

###### acatad → kernel Relation
| File in iop/arcade/acatad | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/acatad/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000011_000000.html>

###### src → common Relation
| File in iop/arcade/acatad/src | Includes file in common |
| acatad.c | include / atahw.h |

---

## PS2SDK: iop/arcade/acatad/src -&gt; dev9 Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000011_000087.html>

###### src → dev9 Relation
| File in iop/arcade/acatad/src | Includes file in iop/dev9 |
| acatad.c | atad / include / atad.h |

---

## PS2SDK: iop/arcade/acatad/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000011_000223.html>

###### src → system Relation
| File in iop/arcade/acatad/src | Includes file in iop/system |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |

---

## PS2SDK: iop/arcade/acatad/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000011_000537.html>

###### src → kernel Relation
| File in iop/arcade/acatad/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/accdvd -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000012_000000.html>

###### accdvd → common Relation
| File in iop/arcade/accdvd | Includes file in common |
| src / accdvd_internal.h | include / errno.h |
| src / acd.c | include / atahw.h |

---

## PS2SDK: iop/arcade/accdvd -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000012_000056.html>

###### accdvd → cdvd Relation
| File in iop/arcade/accdvd | Includes file in iop/cdvd |
| include / accdvd.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/arcade/accdvd -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000012_000223.html>

###### accdvd → system Relation
| File in iop/arcade/accdvd | Includes file in iop/system |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | ioman / include / ioman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thevent.h |
| src / irx_imports.h | threadman / include / thsemap.h |

---

## PS2SDK: iop/arcade/accdvd -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000012_000537.html>

###### accdvd → kernel Relation
| File in iop/arcade/accdvd | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/accdvd/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000013_000000.html>

###### src → common Relation
| File in iop/arcade/accdvd/src | Includes file in common |
| accdvd_internal.h | include / errno.h |
| acd.c | include / atahw.h |

---

## PS2SDK: iop/arcade/accdvd/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000013_000223.html>

###### src → system Relation
| File in iop/arcade/accdvd/src | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | ioman / include / ioman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thevent.h |
| irx_imports.h | threadman / include / thsemap.h |

---

## PS2SDK: iop/arcade/accdvd/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000013_000537.html>

###### src → kernel Relation
| File in iop/arcade/accdvd/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/accdvde -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000014_000056.html>

###### accdvde → cdvd Relation
| File in iop/arcade/accdvde | Includes file in iop/cdvd |
| src / irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/arcade/accdvde -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000014_000223.html>

###### accdvde → system Relation
| File in iop/arcade/accdvde | Includes file in iop/system |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |

---

## PS2SDK: iop/arcade/accdvde -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000014_000537.html>

###### accdvde → kernel Relation
| File in iop/arcade/accdvde | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/accdvde/src -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000015_000056.html>

###### src → cdvd Relation
| File in iop/arcade/accdvde/src | Includes file in iop/cdvd |
| irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/arcade/accdvde/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000015_000223.html>

###### src → system Relation
| File in iop/arcade/accdvde/src | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |

---

## PS2SDK: iop/arcade/accdvde/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000015_000537.html>

###### src → kernel Relation
| File in iop/arcade/accdvde/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/accore -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000016_000000.html>

###### accore → common Relation
| File in iop/arcade/accore | Includes file in common |
| include / accore.h | include / tamtypes.h |

---

## PS2SDK: iop/arcade/accore -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000016_000223.html>

###### accore → system Relation
| File in iop/arcade/accore | Includes file in iop/system |
| src / irx_imports.h | dmacman / include / dmacman.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |

---

## PS2SDK: iop/arcade/accore -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000016_000537.html>

###### accore → kernel Relation
| File in iop/arcade/accore | Includes file in iop/kernel |
| include / accore.h | include / irx.h |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/accore/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000017_000223.html>

###### src → system Relation
| File in iop/arcade/accore/src | Includes file in iop/system |
| irx_imports.h | dmacman / include / dmacman.h |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |

---

## PS2SDK: iop/arcade/accore/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000017_000537.html>

###### src → kernel Relation
| File in iop/arcade/accore/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/acdev -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000018_000000.html>

###### acdev → common Relation
| File in iop/arcade/acdev | Includes file in common |
| include / acdev.h | include / tamtypes.h |

---

## PS2SDK: iop/arcade/acdev -&gt; fs Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000018_000113.html>

###### acdev → fs Relation
| File in iop/arcade/acdev | Includes file in iop/fs |
| src / irx_imports.h | romdrv / include / romdrv.h |

---

## PS2SDK: iop/arcade/acdev -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000018_000223.html>

###### acdev → system Relation
| File in iop/arcade/acdev | Includes file in iop/system |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | ssbusc / include / ssbusc.h |

---

## PS2SDK: iop/arcade/acdev -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000018_000537.html>

###### acdev → kernel Relation
| File in iop/arcade/acdev | Includes file in iop/kernel |
| include / acdev.h | include / irx.h |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/acdev/src -&gt; fs Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000019_000113.html>

###### src → fs Relation
| File in iop/arcade/acdev/src | Includes file in iop/fs |
| irx_imports.h | romdrv / include / romdrv.h |

---

## PS2SDK: iop/arcade/acdev/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000019_000223.html>

###### src → system Relation
| File in iop/arcade/acdev/src | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | ssbusc / include / ssbusc.h |

---

## PS2SDK: iop/arcade/acdev/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000019_000537.html>

###### src → kernel Relation
| File in iop/arcade/acdev/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/acdev9 -&gt; dev9 Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000020_000087.html>

###### acdev9 → dev9 Relation
| File in iop/arcade/acdev9 | Includes file in iop/dev9 |
| src / acdev9.c | dev9 / include / dev9.h |

---

## PS2SDK: iop/arcade/acdev9 -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000020_000223.html>

###### acdev9 → system Relation
| File in iop/arcade/acdev9 | Includes file in iop/system |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |

---

## PS2SDK: iop/arcade/acdev9 -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000020_000537.html>

###### acdev9 → kernel Relation
| File in iop/arcade/acdev9 | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/acdev9/src -&gt; dev9 Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000021_000087.html>

###### src → dev9 Relation
| File in iop/arcade/acdev9/src | Includes file in iop/dev9 |
| acdev9.c | dev9 / include / dev9.h |

---

## PS2SDK: iop/arcade/acdev9/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000021_000223.html>

###### src → system Relation
| File in iop/arcade/acdev9/src | Includes file in iop/system |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |

---

## PS2SDK: iop/arcade/acdev9/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000021_000537.html>

###### src → kernel Relation
| File in iop/arcade/acdev9/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/acflash -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000022_000223.html>

###### acflash → system Relation
| File in iop/arcade/acflash | Includes file in iop/system |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | threadman / include / thbase.h |

---

## PS2SDK: iop/arcade/acflash -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000022_000537.html>

###### acflash → kernel Relation
| File in iop/arcade/acflash | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/acflash/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000023_000223.html>

###### src → system Relation
| File in iop/arcade/acflash/src | Includes file in iop/system |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | threadman / include / thbase.h |

---

## PS2SDK: iop/arcade/acflash/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000023_000537.html>

###### src → kernel Relation
| File in iop/arcade/acflash/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/acfpgald -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000024_000223.html>

###### acfpgald → system Relation
| File in iop/arcade/acfpgald | Includes file in iop/system |
| src / irx_imports.h | ioman / include / ioman.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |

---

## PS2SDK: iop/arcade/acfpgald -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000024_000537.html>

###### acfpgald → kernel Relation
| File in iop/arcade/acfpgald | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/acfpgald/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000025_000223.html>

###### src → system Relation
| File in iop/arcade/acfpgald/src | Includes file in iop/system |
| irx_imports.h | ioman / include / ioman.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |

---

## PS2SDK: iop/arcade/acfpgald/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000025_000537.html>

###### src → kernel Relation
| File in iop/arcade/acfpgald/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/acjv -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000026_000223.html>

###### acjv → system Relation
| File in iop/arcade/acjv | Includes file in iop/system |
| src / irx_imports.h | loadcore / include / loadcore.h |

---

## PS2SDK: iop/arcade/acjv -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000026_000537.html>

###### acjv → kernel Relation
| File in iop/arcade/acjv | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/acjv/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000027_000223.html>

###### src → system Relation
| File in iop/arcade/acjv/src | Includes file in iop/system |
| irx_imports.h | loadcore / include / loadcore.h |

---

## PS2SDK: iop/arcade/acjv/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000027_000537.html>

###### src → kernel Relation
| File in iop/arcade/acjv/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/acjvld -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000028_000223.html>

###### acjvld → system Relation
| File in iop/arcade/acjvld | Includes file in iop/system |
| src / irx_imports.h | ioman / include / ioman.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |

---

## PS2SDK: iop/arcade/acjvld -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000028_000537.html>

###### acjvld → kernel Relation
| File in iop/arcade/acjvld | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/acjvld/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000029_000223.html>

###### src → system Relation
| File in iop/arcade/acjvld/src | Includes file in iop/system |
| irx_imports.h | ioman / include / ioman.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |

---

## PS2SDK: iop/arcade/acjvld/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000029_000537.html>

###### src → kernel Relation
| File in iop/arcade/acjvld/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/acmem -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000030_000223.html>

###### acmem → system Relation
| File in iop/arcade/acmem | Includes file in iop/system |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | sifman / include / sifman.h |
| src / irx_imports.h | threadman / include / thbase.h |

---

## PS2SDK: iop/arcade/acmem -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000030_000537.html>

###### acmem → kernel Relation
| File in iop/arcade/acmem | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/acmem/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000031_000223.html>

###### src → system Relation
| File in iop/arcade/acmem/src | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | sifman / include / sifman.h |
| irx_imports.h | threadman / include / thbase.h |

---

## PS2SDK: iop/arcade/acmem/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000031_000537.html>

###### src → kernel Relation
| File in iop/arcade/acmem/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/acmeme -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000032_000223.html>

###### acmeme → system Relation
| File in iop/arcade/acmeme | Includes file in iop/system |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |

---

## PS2SDK: iop/arcade/acmeme -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000032_000537.html>

###### acmeme → kernel Relation
| File in iop/arcade/acmeme | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/acmeme/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000033_000223.html>

###### src → system Relation
| File in iop/arcade/acmeme/src | Includes file in iop/system |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |

---

## PS2SDK: iop/arcade/acmeme/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000033_000537.html>

###### src → kernel Relation
| File in iop/arcade/acmeme/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/acram -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000034_000223.html>

###### acram → system Relation
| File in iop/arcade/acram | Includes file in iop/system |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |

---

## PS2SDK: iop/arcade/acram -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000034_000537.html>

###### acram → kernel Relation
| File in iop/arcade/acram | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/acram/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000035_000223.html>

###### src → system Relation
| File in iop/arcade/acram/src | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |

---

## PS2SDK: iop/arcade/acram/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000035_000537.html>

###### src → kernel Relation
| File in iop/arcade/acram/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/acrtc -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000036_000056.html>

###### acrtc → cdvd Relation
| File in iop/arcade/acrtc | Includes file in iop/cdvd |
| src / irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/arcade/acrtc -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000036_000223.html>

###### acrtc → system Relation
| File in iop/arcade/acrtc | Includes file in iop/system |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | threadman / include / thbase.h |

---

## PS2SDK: iop/arcade/acrtc -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000036_000537.html>

###### acrtc → kernel Relation
| File in iop/arcade/acrtc | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/acrtc/src -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000037_000056.html>

###### src → cdvd Relation
| File in iop/arcade/acrtc/src | Includes file in iop/cdvd |
| irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/arcade/acrtc/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000037_000223.html>

###### src → system Relation
| File in iop/arcade/acrtc/src | Includes file in iop/system |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | threadman / include / thbase.h |

---

## PS2SDK: iop/arcade/acrtc/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000037_000537.html>

###### src → kernel Relation
| File in iop/arcade/acrtc/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/acsram -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000038_000223.html>

###### acsram → system Relation
| File in iop/arcade/acsram | Includes file in iop/system |
| src / irx_imports.h | loadcore / include / loadcore.h |

---

## PS2SDK: iop/arcade/acsram -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000038_000537.html>

###### acsram → kernel Relation
| File in iop/arcade/acsram | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/acsram/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000039_000223.html>

###### src → system Relation
| File in iop/arcade/acsram/src | Includes file in iop/system |
| irx_imports.h | loadcore / include / loadcore.h |

---

## PS2SDK: iop/arcade/acsram/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000039_000537.html>

###### src → kernel Relation
| File in iop/arcade/acsram/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/actimer -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000040_000223.html>

###### actimer → system Relation
| File in iop/arcade/actimer | Includes file in iop/system |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |

---

## PS2SDK: iop/arcade/actimer -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000040_000537.html>

###### actimer → kernel Relation
| File in iop/arcade/actimer | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/actimer/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000041_000223.html>

###### src → system Relation
| File in iop/arcade/actimer/src | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |

---

## PS2SDK: iop/arcade/actimer/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000041_000537.html>

###### src → kernel Relation
| File in iop/arcade/actimer/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/acuart -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000042_000000.html>

###### acuart → common Relation
| File in iop/arcade/acuart | Includes file in common |
| src / tty.c | include / errno.h |

---

## PS2SDK: iop/arcade/acuart -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000042_000223.html>

###### acuart → system Relation
| File in iop/arcade/acuart | Includes file in iop/system |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thevent.h |

---

## PS2SDK: iop/arcade/acuart -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000042_000537.html>

###### acuart → kernel Relation
| File in iop/arcade/acuart | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/acuart/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000043_000000.html>

###### src → common Relation
| File in iop/arcade/acuart/src | Includes file in common |
| tty.c | include / errno.h |

---

## PS2SDK: iop/arcade/acuart/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000043_000223.html>

###### src → system Relation
| File in iop/arcade/acuart/src | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thevent.h |

---

## PS2SDK: iop/arcade/acuart/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000043_000537.html>

###### src → kernel Relation
| File in iop/arcade/acuart/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/romwrite -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000044_000000.html>

###### romwrite → common Relation
| File in iop/arcade/romwrite | Includes file in common |
| src / romwrite.c | include / s147_mmio_hwport.h |

---

## PS2SDK: iop/arcade/romwrite -&gt; s147nand Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000044_000052.html>

###### romwrite → s147nand Relation
| File in iop/arcade/romwrite | Includes file in iop/arcade/s147nand |
| src / irx_imports.h | include / s147nand.h |

---

## PS2SDK: iop/arcade/romwrite -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000044_000223.html>

###### romwrite → system Relation
| File in iop/arcade/romwrite | Includes file in iop/system |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | ioman / include / ioman.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / romwrite.c | loadcore / include / loadcore.h |

---

## PS2SDK: iop/arcade/romwrite -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000044_000537.html>

###### romwrite → kernel Relation
| File in iop/arcade/romwrite | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/romwrite/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000045_000000.html>

###### src → common Relation
| File in iop/arcade/romwrite/src | Includes file in common |
| romwrite.c | include / s147_mmio_hwport.h |

---

## PS2SDK: iop/arcade/romwrite/src -&gt; s147nand Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000045_000052.html>

###### src → s147nand Relation
| File in iop/arcade/romwrite/src | Includes file in iop/arcade/s147nand |
| irx_imports.h | include / s147nand.h |

---

## PS2SDK: iop/arcade/romwrite/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000045_000223.html>

###### src → system Relation
| File in iop/arcade/romwrite/src | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | ioman / include / ioman.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| romwrite.c | loadcore / include / loadcore.h |

---

## PS2SDK: iop/arcade/romwrite/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000045_000537.html>

###### src → kernel Relation
| File in iop/arcade/romwrite/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/s147ctrl -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000046_000000.html>

###### s147ctrl → common Relation
| File in iop/arcade/s147ctrl | Includes file in common |
| src / s147ctrl.c | include / errno.h |
| src / s147ctrl.c | include / s147_mmio_hwport.h |

---

## PS2SDK: iop/arcade/s147ctrl -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000046_000223.html>

###### s147ctrl → system Relation
| File in iop/arcade/s147ctrl | Includes file in iop/system |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | ioman / include / ioman.h |
| src / irx_imports.h | sifman / include / sifman.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thsemap.h |
| src / irx_imports.h | timrman / include / timrman.h |
| src / s147ctrl.c | loadcore / include / loadcore.h |

---

## PS2SDK: iop/arcade/s147ctrl -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000046_000537.html>

###### s147ctrl → kernel Relation
| File in iop/arcade/s147ctrl | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/s147ctrl/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000047_000000.html>

###### src → common Relation
| File in iop/arcade/s147ctrl/src | Includes file in common |
| s147ctrl.c | include / errno.h |
| s147ctrl.c | include / s147_mmio_hwport.h |

---

## PS2SDK: iop/arcade/s147ctrl/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000047_000223.html>

###### src → system Relation
| File in iop/arcade/s147ctrl/src | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | ioman / include / ioman.h |
| irx_imports.h | sifman / include / sifman.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thsemap.h |
| irx_imports.h | timrman / include / timrman.h |
| s147ctrl.c | loadcore / include / loadcore.h |

---

## PS2SDK: iop/arcade/s147ctrl/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000047_000537.html>

###### src → kernel Relation
| File in iop/arcade/s147ctrl/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/s147link -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000048_000000.html>

###### s147link → common Relation
| File in iop/arcade/s147link | Includes file in common |
| src / s147link.c | include / s147_mmio_hwport.h |

---

## PS2SDK: iop/arcade/s147link -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000048_000223.html>

###### s147link → system Relation
| File in iop/arcade/s147link | Includes file in iop/system |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |

---

## PS2SDK: iop/arcade/s147link -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000048_000537.html>

###### s147link → kernel Relation
| File in iop/arcade/s147link | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/s147link/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000049_000000.html>

###### src → common Relation
| File in iop/arcade/s147link/src | Includes file in common |
| s147link.c | include / s147_mmio_hwport.h |

---

## PS2SDK: iop/arcade/s147link/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000049_000223.html>

###### src → system Relation
| File in iop/arcade/s147link/src | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |

---

## PS2SDK: iop/arcade/s147link/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000049_000537.html>

###### src → kernel Relation
| File in iop/arcade/s147link/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/s147mdev -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000050_000000.html>

###### s147mdev → common Relation
| File in iop/arcade/s147mdev | Includes file in common |
| src / s147mdev.c | include / errno.h |

---

## PS2SDK: iop/arcade/s147mdev -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000050_000223.html>

###### s147mdev → system Relation
| File in iop/arcade/s147mdev | Includes file in iop/system |
| include / s147mdev.h | ioman / include / ioman.h |
| src / irx_imports.h | ioman / include / ioman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | sysclib / include / sysclib.h |

---

## PS2SDK: iop/arcade/s147mdev -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000050_000537.html>

###### s147mdev → kernel Relation
| File in iop/arcade/s147mdev | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/s147mdev/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000051_000000.html>

###### src → common Relation
| File in iop/arcade/s147mdev/src | Includes file in common |
| s147mdev.c | include / errno.h |

---

## PS2SDK: iop/arcade/s147mdev/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000051_000223.html>

###### src → system Relation
| File in iop/arcade/s147mdev/src | Includes file in iop/system |
| irx_imports.h | ioman / include / ioman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | sysclib / include / sysclib.h |

---

## PS2SDK: iop/arcade/s147mdev/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000051_000487.html>

###### src → include Relation
| File in iop/arcade/s147mdev/src | Includes file in iop/arcade/s147mdev/include |
| s147mdev.c | s147mdev.h |

---

## PS2SDK: iop/arcade/s147mdev/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000051_000537.html>

###### src → kernel Relation
| File in iop/arcade/s147mdev/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/s147nand -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000052_000000.html>

###### s147nand → common Relation
| File in iop/arcade/s147nand | Includes file in common |
| include / s147nand.h | include / tamtypes.h |
| src / s147nand.c | include / errno.h |
| src / s147nand.c | include / iop_mmio_hwport.h |
| src / s147nand.c | include / s147_mmio_hwport.h |

---

## PS2SDK: iop/arcade/s147nand -&gt; s147mdev Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000052_000050.html>

###### s147nand → s147mdev Relation
| File in iop/arcade/s147nand | Includes file in iop/arcade/s147mdev |
| src / irx_imports.h | include / s147mdev.h |

---

## PS2SDK: iop/arcade/s147nand -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000052_000223.html>

###### s147nand → system Relation
| File in iop/arcade/s147nand | Includes file in iop/system |
| src / irx_imports.h | dmacman / include / dmacman.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thsemap.h |

---

## PS2SDK: iop/arcade/s147nand -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000052_000537.html>

###### s147nand → kernel Relation
| File in iop/arcade/s147nand | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/s147nand/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000053_000000.html>

###### src → common Relation
| File in iop/arcade/s147nand/src | Includes file in common |
| s147nand.c | include / errno.h |
| s147nand.c | include / iop_mmio_hwport.h |
| s147nand.c | include / s147_mmio_hwport.h |

---

## PS2SDK: iop/arcade/s147nand/src -&gt; s147mdev Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000053_000050.html>

###### src → s147mdev Relation
| File in iop/arcade/s147nand/src | Includes file in iop/arcade/s147mdev |
| irx_imports.h | include / s147mdev.h |

---

## PS2SDK: iop/arcade/s147nand/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000053_000223.html>

###### src → system Relation
| File in iop/arcade/s147nand/src | Includes file in iop/system |
| irx_imports.h | dmacman / include / dmacman.h |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thsemap.h |

---

## PS2SDK: iop/arcade/s147nand/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000053_000488.html>

###### src → include Relation
| File in iop/arcade/s147nand/src | Includes file in iop/arcade/s147nand/include |
| s147nand.c | s147nand.h |

---

## PS2SDK: iop/arcade/s147nand/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000053_000537.html>

###### src → kernel Relation
| File in iop/arcade/s147nand/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/s147netb -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000054_000223.html>

###### s147netb → system Relation
| File in iop/arcade/s147netb | Includes file in iop/system |
| src / irx_imports.h | ioman / include / ioman.h |
| src / irx_imports.h | modload / include / modload.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / s147netb.c | loadcore / include / loadcore.h |

---

## PS2SDK: iop/arcade/s147netb -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000054_000537.html>

###### s147netb → kernel Relation
| File in iop/arcade/s147netb | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/arcade/s147netb/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000055_000223.html>

###### src → system Relation
| File in iop/arcade/s147netb/src | Includes file in iop/system |
| irx_imports.h | ioman / include / ioman.h |
| irx_imports.h | modload / include / modload.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| s147netb.c | loadcore / include / loadcore.h |

---

## PS2SDK: iop/arcade/s147netb/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000055_000537.html>

###### src → kernel Relation
| File in iop/arcade/s147netb/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/cdvd -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000056_000000.html>

###### cdvd → common Relation
| File in iop/cdvd | Includes file in common |
| cdvdman / include / cdvdman.h | include / libcdvd-common.h |
| xatapi / include / xatapi.h | include / tamtypes.h |
| cdvdman / src / cdvdman.c | include / cdvd-ioctl.h |
| cdvdman / src / cdvdman.c | include / dev5_mmio_hwport.h |
| cdvdman / src / cdvdman.c | include / errno.h |
| cdvdman / src / cdvdman.c | include / hdd-ioctl.h |
| cdvdman / src / cdvdman.c | include / iop_mmio_hwport.h |
| cdvdman / src / cdvdman.c | include / mipscopaccess.h |
| cdvdfsv / src / cdvdfsv.c | include / cdvd-ioctl.h |
| cdvdfsv / src / cdvdfsv.c | include / libcdvd-rpc.h |
| xatapi / src / xatapi.c | include / errno.h |
| xatapi / src / xatapi.c | include / blkio-ioctl.h |
| cdfs / src / cdfs_iop.c | include / libcdvd-common.h |
| cdfs / src / main.c | include / iox_stat.h |
| cdfs / src / main.c | include / errno.h |
| cdvdstm / src / cdvdstm.c | include / cdvd-ioctl.h |
| cdvdstm / src / cdvdstm.c | include / errno.h |
| xesdrv / src / xesdrv.c | include / errno.h |

---

## PS2SDK: iop/cdvd -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000056_000223.html>

###### cdvd → system Relation
| File in iop/cdvd | Includes file in iop/system |
| cdvdman / src / cdvdman.c | iomanx / include / iomanX.h |
| cdvdman / src / irx_imports.h | dmacman / include / dmacman.h |
| cdvdman / src / irx_imports.h | intrman / include / intrman.h |
| cdvdman / src / irx_imports.h | iomanx / include / iomanX.h |
| cdvdman / src / irx_imports.h | loadcore / include / loadcore.h |
| cdvdman / src / irx_imports.h | stdio / include / stdio.h |
| cdvdman / src / irx_imports.h | sysclib / include / sysclib.h |
| cdvdman / src / irx_imports.h | threadman / include / thbase.h |
| cdvdman / src / irx_imports.h | threadman / include / thevent.h |
| cdvdman / src / irx_imports.h | threadman / include / thsemap.h |
| cdvdfsv / src / irx_imports.h | dmacman / include / dmacman.h |
| cdvdfsv / src / irx_imports.h | intrman / include / intrman.h |
| cdvdfsv / src / irx_imports.h | iomanx / include / iomanX.h |
| cdvdfsv / src / irx_imports.h | loadcore / include / loadcore.h |
| cdvdfsv / src / irx_imports.h | sifman / include / sifman.h |
| cdvdfsv / src / irx_imports.h | stdio / include / stdio.h |
| cdvdfsv / src / irx_imports.h | sysclib / include / sysclib.h |
| cdvdfsv / src / irx_imports.h | threadman / include / thbase.h |
| cdvdfsv / src / irx_imports.h | threadman / include / thevent.h |
| xatapi / src / irx_imports.h | dmacman / include / dmacman.h |
| xatapi / src / irx_imports.h | intrman / include / intrman.h |
| xatapi / src / irx_imports.h | iomanx / include / iomanX.h |
| xatapi / src / irx_imports.h | loadcore / include / loadcore.h |
| xatapi / src / irx_imports.h | stdio / include / stdio.h |
| xatapi / src / irx_imports.h | sysclib / include / sysclib.h |
| xatapi / src / irx_imports.h | threadman / include / thbase.h |
| xatapi / src / irx_imports.h | threadman / include / thevent.h |
| xatapi / src / irx_imports.h | threadman / include / thsemap.h |
| cdfs / src / cdfs_iop.c | stdio / include / stdio.h |
| cdfs / src / cdfs_iop.c | sysclib / include / sysclib.h |
| cdfs / src / irx_imports.h | intrman / include / intrman.h |
| cdfs / src / irx_imports.h | ioman / include / ioman.h |
| cdfs / src / irx_imports.h | sifman / include / sifman.h |
| cdfs / src / irx_imports.h | stdio / include / stdio.h |
| cdfs / src / irx_imports.h | sysclib / include / sysclib.h |
| cdfs / src / irx_imports.h | threadman / include / thbase.h |
| cdfs / src / main.c | stdio / include / stdio.h |
| cdfs / src / main.c | ioman / include / ioman.h |
| cdfs / src / main.c | loadcore / include / loadcore.h |
| cdfs / src / main.c | sysclib / include / sysclib.h |
| cdvdstm / src / cdvdstm.c | iomanx / include / iomanX.h |
| cdvdstm / src / irx_imports.h | intrman / include / intrman.h |
| cdvdstm / src / irx_imports.h | iomanx / include / iomanX.h |
| cdvdstm / src / irx_imports.h | loadcore / include / loadcore.h |
| cdvdstm / src / irx_imports.h | sifman / include / sifman.h |
| cdvdstm / src / irx_imports.h | stdio / include / stdio.h |
| cdvdstm / src / irx_imports.h | sysclib / include / sysclib.h |
| cdvdstm / src / irx_imports.h | threadman / include / thbase.h |
| cdvdstm / src / irx_imports.h | threadman / include / thevent.h |
| cdvdstm / src / irx_imports.h | threadman / include / thsemap.h |
| xesdrv / src / irx_imports.h | iomanx / include / iomanX.h |
| xesdrv / src / irx_imports.h | threadman / include / thbase.h |
| xesdrv / src / irx_imports.h | threadman / include / thsemap.h |
| xesdrv / src / xesdrv.c | loadcore / include / loadcore.h |
| poffsim / src / irx_imports.h | threadman / include / thbase.h |
| poffsim / src / irx_imports.h | threadman / include / thevent.h |
| poffsim / src / irx_imports.h | threadman / include / thsemap.h |

---

## PS2SDK: iop/cdvd -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000056_000537.html>

###### cdvd → kernel Relation
| File in iop/cdvd | Includes file in iop/kernel |
| cdvdfsv / include / cdvdfsv.h | include / irx.h |
| cdvdman / include / cdvdman.h | include / irx.h |
| cdvdman / src / cdvdman.c | include / kerr.h |
| cdvdman / src / irx_imports.h | include / irx.h |
| cdvdfsv / src / cdvdfsv.c | include / kerr.h |
| cdvdfsv / src / irx_imports.h | include / irx.h |
| xatapi / src / irx_imports.h | include / irx.h |
| xatapi / src / xatapi.c | include / kerr.h |
| cdfs / src / irx_imports.h | include / irx.h |
| cdvdstm / src / cdvdstm.c | include / kerr.h |
| cdvdstm / src / irx_imports.h | include / irx.h |
| xesdrv / src / irx_imports.h | include / irx.h |
| poffsim / src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/cdvd/cdfs -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000057_000000.html>

###### cdfs → common Relation
| File in iop/cdvd/cdfs | Includes file in common |
| src / cdfs_iop.c | include / libcdvd-common.h |
| src / main.c | include / iox_stat.h |
| src / main.c | include / errno.h |

---

## PS2SDK: iop/cdvd/cdfs -&gt; cdvdman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000057_000061.html>

###### cdfs → cdvdman Relation
| File in iop/cdvd/cdfs | Includes file in iop/cdvd/cdvdman |
| src / irx_imports.h | include / cdvdman.h |

---

## PS2SDK: iop/cdvd/cdfs -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000057_000223.html>

###### cdfs → system Relation
| File in iop/cdvd/cdfs | Includes file in iop/system |
| src / cdfs_iop.c | stdio / include / stdio.h |
| src / cdfs_iop.c | sysclib / include / sysclib.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | ioman / include / ioman.h |
| src / irx_imports.h | sifman / include / sifman.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / main.c | stdio / include / stdio.h |
| src / main.c | ioman / include / ioman.h |
| src / main.c | loadcore / include / loadcore.h |
| src / main.c | sysclib / include / sysclib.h |

---

## PS2SDK: iop/cdvd/cdfs -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000057_000537.html>

###### cdfs → kernel Relation
| File in iop/cdvd/cdfs | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/cdvd/cdfs/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000058_000000.html>

###### src → common Relation
| File in iop/cdvd/cdfs/src | Includes file in common |
| cdfs_iop.c | include / libcdvd-common.h |
| main.c | include / errno.h |
| main.c | include / iox_stat.h |

---

## PS2SDK: iop/cdvd/cdfs/src -&gt; cdvdman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000058_000061.html>

###### src → cdvdman Relation
| File in iop/cdvd/cdfs/src | Includes file in iop/cdvd/cdvdman |
| irx_imports.h | include / cdvdman.h |

---

## PS2SDK: iop/cdvd/cdfs/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000058_000223.html>

###### src → system Relation
| File in iop/cdvd/cdfs/src | Includes file in iop/system |
| cdfs_iop.c | stdio / include / stdio.h |
| cdfs_iop.c | sysclib / include / sysclib.h |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | ioman / include / ioman.h |
| irx_imports.h | sifman / include / sifman.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| main.c | ioman / include / ioman.h |
| main.c | loadcore / include / loadcore.h |
| main.c | stdio / include / stdio.h |
| main.c | sysclib / include / sysclib.h |

---

## PS2SDK: iop/cdvd/cdfs/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000058_000537.html>

###### src → kernel Relation
| File in iop/cdvd/cdfs/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/cdvd/cdvdfsv -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000059_000000.html>

###### cdvdfsv → common Relation
| File in iop/cdvd/cdvdfsv | Includes file in common |
| src / cdvdfsv.c | include / cdvd-ioctl.h |
| src / cdvdfsv.c | include / libcdvd-rpc.h |

---

## PS2SDK: iop/cdvd/cdvdfsv -&gt; cdvdman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000059_000061.html>

###### cdvdfsv → cdvdman Relation
| File in iop/cdvd/cdvdfsv | Includes file in iop/cdvd/cdvdman |
| src / irx_imports.h | include / cdvdman.h |

---

## PS2SDK: iop/cdvd/cdvdfsv -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000059_000223.html>

###### cdvdfsv → system Relation
| File in iop/cdvd/cdvdfsv | Includes file in iop/system |
| src / irx_imports.h | dmacman / include / dmacman.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | iomanx / include / iomanX.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | sifman / include / sifman.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thevent.h |

---

## PS2SDK: iop/cdvd/cdvdfsv -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000059_000537.html>

###### cdvdfsv → kernel Relation
| File in iop/cdvd/cdvdfsv | Includes file in iop/kernel |
| include / cdvdfsv.h | include / irx.h |
| src / cdvdfsv.c | include / kerr.h |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/cdvd/cdvdfsv/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000060_000000.html>

###### src → common Relation
| File in iop/cdvd/cdvdfsv/src | Includes file in common |
| cdvdfsv.c | include / cdvd-ioctl.h |
| cdvdfsv.c | include / libcdvd-rpc.h |

---

## PS2SDK: iop/cdvd/cdvdfsv/src -&gt; cdvdman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000060_000061.html>

###### src → cdvdman Relation
| File in iop/cdvd/cdvdfsv/src | Includes file in iop/cdvd/cdvdman |
| irx_imports.h | include / cdvdman.h |

---

## PS2SDK: iop/cdvd/cdvdfsv/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000060_000223.html>

###### src → system Relation
| File in iop/cdvd/cdvdfsv/src | Includes file in iop/system |
| irx_imports.h | dmacman / include / dmacman.h |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | iomanx / include / iomanX.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | sifman / include / sifman.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thevent.h |

---

## PS2SDK: iop/cdvd/cdvdfsv/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000060_000537.html>

###### src → kernel Relation
| File in iop/cdvd/cdvdfsv/src | Includes file in iop/kernel |
| cdvdfsv.c | include / kerr.h |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/cdvd/cdvdman -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000061_000000.html>

###### cdvdman → common Relation
| File in iop/cdvd/cdvdman | Includes file in common |
| include / cdvdman.h | include / libcdvd-common.h |
| src / cdvdman.c | include / cdvd-ioctl.h |
| src / cdvdman.c | include / dev5_mmio_hwport.h |
| src / cdvdman.c | include / errno.h |
| src / cdvdman.c | include / hdd-ioctl.h |
| src / cdvdman.c | include / iop_mmio_hwport.h |
| src / cdvdman.c | include / mipscopaccess.h |

---

## PS2SDK: iop/cdvd/cdvdman -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000061_000223.html>

###### cdvdman → system Relation
| File in iop/cdvd/cdvdman | Includes file in iop/system |
| src / cdvdman.c | iomanx / include / iomanX.h |
| src / irx_imports.h | dmacman / include / dmacman.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | iomanx / include / iomanX.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thevent.h |
| src / irx_imports.h | threadman / include / thsemap.h |

---

## PS2SDK: iop/cdvd/cdvdman -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000061_000537.html>

###### cdvdman → kernel Relation
| File in iop/cdvd/cdvdman | Includes file in iop/kernel |
| include / cdvdman.h | include / irx.h |
| src / cdvdman.c | include / kerr.h |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/cdvd/cdvdman/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000062_000000.html>

###### src → common Relation
| File in iop/cdvd/cdvdman/src | Includes file in common |
| cdvdman.c | include / cdvd-ioctl.h |
| cdvdman.c | include / dev5_mmio_hwport.h |
| cdvdman.c | include / errno.h |
| cdvdman.c | include / hdd-ioctl.h |
| cdvdman.c | include / iop_mmio_hwport.h |
| cdvdman.c | include / mipscopaccess.h |

---

## PS2SDK: iop/cdvd/cdvdman/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000062_000223.html>

###### src → system Relation
| File in iop/cdvd/cdvdman/src | Includes file in iop/system |
| cdvdman.c | iomanx / include / iomanX.h |
| irx_imports.h | dmacman / include / dmacman.h |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | iomanx / include / iomanX.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thevent.h |
| irx_imports.h | threadman / include / thsemap.h |

---

## PS2SDK: iop/cdvd/cdvdman/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000062_000496.html>

###### src → include Relation
| File in iop/cdvd/cdvdman/src | Includes file in iop/cdvd/cdvdman/include |
| cdvdman.c | cdvdman.h |

---

## PS2SDK: iop/cdvd/cdvdman/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000062_000537.html>

###### src → kernel Relation
| File in iop/cdvd/cdvdman/src | Includes file in iop/kernel |
| cdvdman.c | include / kerr.h |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/cdvd/cdvdstm -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000063_000000.html>

###### cdvdstm → common Relation
| File in iop/cdvd/cdvdstm | Includes file in common |
| src / cdvdstm.c | include / cdvd-ioctl.h |
| src / cdvdstm.c | include / errno.h |

---

## PS2SDK: iop/cdvd/cdvdstm -&gt; cdvdman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000063_000061.html>

###### cdvdstm → cdvdman Relation
| File in iop/cdvd/cdvdstm | Includes file in iop/cdvd/cdvdman |
| src / irx_imports.h | include / cdvdman.h |

---

## PS2SDK: iop/cdvd/cdvdstm -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000063_000223.html>

###### cdvdstm → system Relation
| File in iop/cdvd/cdvdstm | Includes file in iop/system |
| src / cdvdstm.c | iomanx / include / iomanX.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | iomanx / include / iomanX.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | sifman / include / sifman.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thevent.h |
| src / irx_imports.h | threadman / include / thsemap.h |

---

## PS2SDK: iop/cdvd/cdvdstm -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000063_000537.html>

###### cdvdstm → kernel Relation
| File in iop/cdvd/cdvdstm | Includes file in iop/kernel |
| src / cdvdstm.c | include / kerr.h |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/cdvd/cdvdstm/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000064_000000.html>

###### src → common Relation
| File in iop/cdvd/cdvdstm/src | Includes file in common |
| cdvdstm.c | include / cdvd-ioctl.h |
| cdvdstm.c | include / errno.h |

---

## PS2SDK: iop/cdvd/cdvdstm/src -&gt; cdvdman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000064_000061.html>

###### src → cdvdman Relation
| File in iop/cdvd/cdvdstm/src | Includes file in iop/cdvd/cdvdman |
| irx_imports.h | include / cdvdman.h |

---

## PS2SDK: iop/cdvd/cdvdstm/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000064_000223.html>

###### src → system Relation
| File in iop/cdvd/cdvdstm/src | Includes file in iop/system |
| cdvdstm.c | iomanx / include / iomanX.h |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | iomanx / include / iomanX.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | sifman / include / sifman.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thevent.h |
| irx_imports.h | threadman / include / thsemap.h |

---

## PS2SDK: iop/cdvd/cdvdstm/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000064_000537.html>

###### src → kernel Relation
| File in iop/cdvd/cdvdstm/src | Includes file in iop/kernel |
| cdvdstm.c | include / kerr.h |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/cdvd/poffsim -&gt; cdvdman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000065_000061.html>

###### poffsim → cdvdman Relation
| File in iop/cdvd/poffsim | Includes file in iop/cdvd/cdvdman |
| src / irx_imports.h | include / cdvdman.h |

---

## PS2SDK: iop/cdvd/poffsim -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000065_000223.html>

###### poffsim → system Relation
| File in iop/cdvd/poffsim | Includes file in iop/system |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thevent.h |
| src / irx_imports.h | threadman / include / thsemap.h |

---

## PS2SDK: iop/cdvd/poffsim -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000065_000537.html>

###### poffsim → kernel Relation
| File in iop/cdvd/poffsim | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/cdvd/poffsim/src -&gt; cdvdman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000066_000061.html>

###### src → cdvdman Relation
| File in iop/cdvd/poffsim/src | Includes file in iop/cdvd/cdvdman |
| irx_imports.h | include / cdvdman.h |

---

## PS2SDK: iop/cdvd/poffsim/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000066_000223.html>

###### src → system Relation
| File in iop/cdvd/poffsim/src | Includes file in iop/system |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thevent.h |
| irx_imports.h | threadman / include / thsemap.h |

---

## PS2SDK: iop/cdvd/poffsim/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000066_000537.html>

###### src → kernel Relation
| File in iop/cdvd/poffsim/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/cdvd/xatapi -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000067_000000.html>

###### xatapi → common Relation
| File in iop/cdvd/xatapi | Includes file in common |
| src / xatapi.c | include / blkio-ioctl.h |
| src / xatapi.c | include / errno.h |
| include / xatapi.h | include / tamtypes.h |

---

## PS2SDK: iop/cdvd/xatapi -&gt; cdvdman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000067_000061.html>

###### xatapi → cdvdman Relation
| File in iop/cdvd/xatapi | Includes file in iop/cdvd/cdvdman |
| src / irx_imports.h | include / cdvdman.h |

---

## PS2SDK: iop/cdvd/xatapi -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000067_000223.html>

###### xatapi → system Relation
| File in iop/cdvd/xatapi | Includes file in iop/system |
| src / irx_imports.h | dmacman / include / dmacman.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | iomanx / include / iomanX.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thevent.h |
| src / irx_imports.h | threadman / include / thsemap.h |

---

## PS2SDK: iop/cdvd/xatapi -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000067_000537.html>

###### xatapi → kernel Relation
| File in iop/cdvd/xatapi | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |
| src / xatapi.c | include / kerr.h |

---

## PS2SDK: iop/cdvd/xatapi/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000068_000000.html>

###### src → common Relation
| File in iop/cdvd/xatapi/src | Includes file in common |
| xatapi.c | include / blkio-ioctl.h |
| xatapi.c | include / errno.h |

---

## PS2SDK: iop/cdvd/xatapi/src -&gt; cdvdman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000068_000061.html>

###### src → cdvdman Relation
| File in iop/cdvd/xatapi/src | Includes file in iop/cdvd/cdvdman |
| irx_imports.h | include / cdvdman.h |

---

## PS2SDK: iop/cdvd/xatapi/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000068_000223.html>

###### src → system Relation
| File in iop/cdvd/xatapi/src | Includes file in iop/system |
| irx_imports.h | dmacman / include / dmacman.h |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | iomanx / include / iomanX.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thevent.h |
| irx_imports.h | threadman / include / thsemap.h |

---

## PS2SDK: iop/cdvd/xatapi/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000068_000497.html>

###### src → include Relation
| File in iop/cdvd/xatapi/src | Includes file in iop/cdvd/xatapi/include |
| xatapi.c | xatapi.h |

---

## PS2SDK: iop/cdvd/xatapi/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000068_000537.html>

###### src → kernel Relation
| File in iop/cdvd/xatapi/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |
| xatapi.c | include / kerr.h |

---

## PS2SDK: iop/cdvd/xesdrv -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000069_000000.html>

###### xesdrv → common Relation
| File in iop/cdvd/xesdrv | Includes file in common |
| src / xesdrv.c | include / errno.h |

---

## PS2SDK: iop/cdvd/xesdrv -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000069_000223.html>

###### xesdrv → system Relation
| File in iop/cdvd/xesdrv | Includes file in iop/system |
| src / irx_imports.h | iomanx / include / iomanX.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thsemap.h |
| src / xesdrv.c | loadcore / include / loadcore.h |

---

## PS2SDK: iop/cdvd/xesdrv -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000069_000537.html>

###### xesdrv → kernel Relation
| File in iop/cdvd/xesdrv | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/cdvd/xesdrv/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000070_000000.html>

###### src → common Relation
| File in iop/cdvd/xesdrv/src | Includes file in common |
| xesdrv.c | include / errno.h |

---

## PS2SDK: iop/cdvd/xesdrv/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000070_000223.html>

###### src → system Relation
| File in iop/cdvd/xesdrv/src | Includes file in iop/system |
| irx_imports.h | iomanx / include / iomanX.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thsemap.h |
| xesdrv.c | loadcore / include / loadcore.h |

---

## PS2SDK: iop/cdvd/xesdrv/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000070_000537.html>

###### src → kernel Relation
| File in iop/cdvd/xesdrv/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/debug -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000071_000000.html>

###### debug → common Relation
| File in iop/debug | Includes file in common |
| iop_sbusdbg / include / iop_sbusdbg.h | include / ps2_debug.h |
| iopdebug / include / iopdebug.h | include / iop_cop0_defs.h |
| iopdebug / include / iopdebug.h | include / ps2_debug.h |
| sior / include / sior.h | include / sior-common.h |
| iop_sbusdbg / src / irx_imports.h | sbus / include / ps2_sbus.h |
| iop_sbusdbg / src / main.c | include / tamtypes.h |
| iop_sbusdbg / src / main.c | include / iop_cop0_defs.h |
| iop_sbusdbg / src / main.c | sbus / include / ps2_sbus.h |
| iop_sbusdbg / src / sbus_dbg.c | include / tamtypes.h |
| iop_sbusdbg / src / sbus_dbg.c | include / ps2_debug.h |
| iop_sbusdbg / src / sbus_dbg.c | sbus / include / ps2_sbus.h |
| iop_sbusdbg / src / sbus_tty.c | include / tamtypes.h |
| iop_sbusdbg / src / sbus_tty.c | include / errno.h |
| iop_sbusdbg / src / sbus_tty.c | include / ps2_debug.h |
| iop_sbusdbg / src / sbus_tty.c | sbus / include / ps2_sbus.h |
| iop_sbusdbg / src / sbus_tty.h | include / tamtypes.h |
| sior / src / xprintf.c | include / tamtypes.h |
| sior / src / xprintf.c | include / ps2lib_err.h |
| iopdebug / src / iop_debug.c | include / tamtypes.h |
| iopdebug / src / iop_debug.c | include / iop_cop0_defs.h |
| iopdebug / src / iop_debug.c | include / ps2_debug.h |
| iopdebug / src / iopdebug_priv.h | include / tamtypes.h |
| iopdebug / src / main.c | include / tamtypes.h |
| ppctty / src / main.c | include / tamtypes.h |
| ppctty / src / main.c | include / iop_regs.h |
| ppctty / src / tty.c | include / tamtypes.h |
| ppctty / src / tty.c | include / errno.h |
| ppctty / src / tty.h | include / tamtypes.h |
| ioptrap / src / breakpoint.c | include / mipscopaccess.h |

---

## PS2SDK: iop/debug -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000071_000056.html>

###### debug → cdvd Relation
| File in iop/debug | Includes file in iop/cdvd |
| iop_sbusdbg / src / irx_imports.h | cdvdman / include / cdvdman.h |
| iopdebug / src / irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/debug -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000071_000223.html>

###### debug → system Relation
| File in iop/debug | Includes file in iop/system |
| iop_sbusdbg / src / irx_imports.h | loadcore / include / loadcore.h |
| iop_sbusdbg / src / irx_imports.h | sifman / include / sifman.h |
| iop_sbusdbg / src / irx_imports.h | stdio / include / stdio.h |
| iop_sbusdbg / src / irx_imports.h | sysclib / include / sysclib.h |
| iop_sbusdbg / src / irx_imports.h | threadman / include / thbase.h |
| iop_sbusdbg / src / irx_imports.h | ioman / include / ioman.h |
| iop_sbusdbg / src / irx_imports.h | modload / include / modload.h |
| iop_sbusdbg / src / irx_imports.h | intrman / include / intrman.h |
| iop_sbusdbg / src / irx_imports.h | excepman / include / excepman.h |
| iop_sbusdbg / src / main.c | stdio / include / stdio.h |
| iop_sbusdbg / src / main.c | loadcore / include / loadcore.h |
| iop_sbusdbg / src / main.c | threadman / include / thbase.h |
| iop_sbusdbg / src / main.c | excepman / include / excepman.h |
| iop_sbusdbg / src / sbus_dbg.c | stdio / include / stdio.h |
| iop_sbusdbg / src / sbus_dbg.c | sysclib / include / sysclib.h |
| iop_sbusdbg / src / sbus_dbg.c | excepman / include / excepman.h |
| iop_sbusdbg / src / sbus_dbg.c | intrman / include / intrman.h |
| iop_sbusdbg / src / sbus_dbg.c | loadcore / include / loadcore.h |
| iop_sbusdbg / src / sbus_dbg.c | threadman / include / thbase.h |
| iop_sbusdbg / src / sbus_dbg.c | ioman / include / ioman.h |
| iop_sbusdbg / src / sbus_tty.c | stdio / include / stdio.h |
| iop_sbusdbg / src / sbus_tty.c | sysclib / include / sysclib.h |
| iop_sbusdbg / src / sbus_tty.c | excepman / include / excepman.h |
| iop_sbusdbg / src / sbus_tty.c | intrman / include / intrman.h |
| iop_sbusdbg / src / sbus_tty.c | ioman / include / ioman.h |
| sior / src / irx_imports.h | loadcore / include / loadcore.h |
| sior / src / irx_imports.h | stdio / include / stdio.h |
| sior / src / irx_imports.h | sysclib / include / sysclib.h |
| sior / src / irx_imports.h | threadman / include / thbase.h |
| sior / src / xprintf.c | stdio / include / stdio.h |
| sior / src / xprintf.c | sysclib / include / sysclib.h |
| sior / src / xprintf.c | sysclib / include / ctype.h |
| iopdebug / src / iop_debug.c | excepman / include / excepman.h |
| iopdebug / src / iopdebug_priv.h | intrman / include / intrman.h |
| iopdebug / src / irx_imports.h | loadcore / include / loadcore.h |
| iopdebug / src / irx_imports.h | sifman / include / sifman.h |
| iopdebug / src / irx_imports.h | stdio / include / stdio.h |
| iopdebug / src / irx_imports.h | sysclib / include / sysclib.h |
| iopdebug / src / irx_imports.h | threadman / include / thbase.h |
| iopdebug / src / irx_imports.h | ioman / include / ioman.h |
| iopdebug / src / irx_imports.h | modload / include / modload.h |
| iopdebug / src / irx_imports.h | intrman / include / intrman.h |
| iopdebug / src / irx_imports.h | excepman / include / excepman.h |
| iopdebug / src / main.c | stdio / include / stdio.h |
| iopdebug / src / main.c | loadcore / include / loadcore.h |
| iopdebug / src / main.c | threadman / include / thbase.h |
| ppctty / src / irx_imports.h | loadcore / include / loadcore.h |
| ppctty / src / irx_imports.h | stdio / include / stdio.h |
| ppctty / src / irx_imports.h | sysclib / include / sysclib.h |
| ppctty / src / irx_imports.h | ioman / include / ioman.h |
| ppctty / src / irx_imports.h | modload / include / modload.h |
| ppctty / src / irx_imports.h | threadman / include / thsemap.h |
| ppctty / src / main.c | stdio / include / stdio.h |
| ppctty / src / main.c | loadcore / include / loadcore.h |
| ppctty / src / main.c | excepman / include / excepman.h |
| ppctty / src / main.c | ioman / include / ioman.h |
| ppctty / src / tty.c | stdio / include / stdio.h |
| ppctty / src / tty.c | sysclib / include / sysclib.h |
| ppctty / src / tty.c | excepman / include / excepman.h |
| ppctty / src / tty.c | intrman / include / intrman.h |
| ppctty / src / tty.c | ioman / include / ioman.h |
| ppctty / src / tty.c | threadman / include / thsemap.h |
| thmon / src / irx_imports.h | intrman / include / intrman.h |
| thmon / src / irx_imports.h | ioman / include / ioman.h |
| thmon / src / irx_imports.h | loadcore / include / loadcore.h |
| thmon / src / irx_imports.h | stdio / include / stdio.h |
| thmon / src / irx_imports.h | sysclib / include / sysclib.h |
| thmon / src / irx_imports.h | threadman / include / thbase.h |
| thmon / src / irx_imports.h | threadman / include / thevent.h |
| thmon / src / irx_imports.h | threadman / include / thmsgbx.h |
| thmon / src / irx_imports.h | threadman / include / thsemap.h |
| ioptrap / src / ioptrap.c | excepman / include / excepman.h |
| ioptrap / src / ioptrap.c | loadcore / include / loadcore.h |
| ioptrap / src / ioptrap.c | sifman / include / sifman.h |
| ioptrap / src / ioptrap.c | stdio / include / stdio.h |
| ioptrap / src / ioptrap.c | sysclib / include / sysclib.h |
| ioptrap / src / ioptrap.c | threadman / include / thbase.h |
| ioptrap / src / irx_imports.h | excepman / include / excepman.h |
| ioptrap / src / irx_imports.h | loadcore / include / loadcore.h |
| ioptrap / src / irx_imports.h | sifman / include / sifman.h |
| ioptrap / src / irx_imports.h | stdio / include / stdio.h |
| ioptrap / src / irx_imports.h | sysclib / include / sysclib.h |

---

## PS2SDK: iop/debug -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000071_000537.html>

###### debug → kernel Relation
| File in iop/debug | Includes file in iop/kernel |
| iopdebug / include / iopdebug.h | include / irx.h |
| ioptrap / include / ioptrap.h | include / irx.h |
| sior / include / sior.h | include / irx.h |
| iop_sbusdbg / src / irx_imports.h | include / irx.h |
| sior / src / irx_imports.h | include / irx.h |
| sior / src / sior.c | include / defs.h |
| sior / src / sior.c | include / irx.h |
| iopdebug / src / irx_imports.h | include / irx.h |
| ppctty / src / irx_imports.h | include / irx.h |
| thmon / src / irx_imports.h | include / irx.h |
| ioptrap / src / ioptrap.c | include / defs.h |
| ioptrap / src / ioptrap.c | include / irx.h |
| ioptrap / src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/debug/iop_sbusdbg -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000072_000000.html>

###### iop_sbusdbg → common Relation
| File in iop/debug/iop_sbusdbg | Includes file in common |
| include / iop_sbusdbg.h | include / ps2_debug.h |
| src / irx_imports.h | sbus / include / ps2_sbus.h |
| src / main.c | include / tamtypes.h |
| src / main.c | include / iop_cop0_defs.h |
| src / main.c | sbus / include / ps2_sbus.h |
| src / sbus_dbg.c | include / tamtypes.h |
| src / sbus_dbg.c | include / ps2_debug.h |
| src / sbus_dbg.c | sbus / include / ps2_sbus.h |
| src / sbus_tty.c | include / tamtypes.h |
| src / sbus_tty.c | include / errno.h |
| src / sbus_tty.c | include / ps2_debug.h |
| src / sbus_tty.c | sbus / include / ps2_sbus.h |
| src / sbus_tty.h | include / tamtypes.h |

---

## PS2SDK: iop/debug/iop_sbusdbg -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000072_000056.html>

###### iop_sbusdbg → cdvd Relation
| File in iop/debug/iop_sbusdbg | Includes file in iop/cdvd |
| src / irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/debug/iop_sbusdbg -&gt; iopdebug Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000072_000074.html>

###### iop_sbusdbg → iopdebug Relation
| File in iop/debug/iop_sbusdbg | Includes file in iop/debug/iopdebug |
| src / irx_imports.h | include / iopdebug.h |
| src / main.c | include / iopdebug.h |
| src / sbus_dbg.c | include / iopdebug.h |
| src / sbus_tty.c | include / iopdebug.h |

---

## PS2SDK: iop/debug/iop_sbusdbg -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000072_000223.html>

###### iop_sbusdbg → system Relation
| File in iop/debug/iop_sbusdbg | Includes file in iop/system |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | sifman / include / sifman.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | ioman / include / ioman.h |
| src / irx_imports.h | modload / include / modload.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | excepman / include / excepman.h |
| src / main.c | stdio / include / stdio.h |
| src / main.c | loadcore / include / loadcore.h |
| src / main.c | threadman / include / thbase.h |
| src / main.c | excepman / include / excepman.h |
| src / sbus_dbg.c | stdio / include / stdio.h |
| src / sbus_dbg.c | sysclib / include / sysclib.h |
| src / sbus_dbg.c | excepman / include / excepman.h |
| src / sbus_dbg.c | intrman / include / intrman.h |
| src / sbus_dbg.c | loadcore / include / loadcore.h |
| src / sbus_dbg.c | threadman / include / thbase.h |
| src / sbus_dbg.c | ioman / include / ioman.h |
| src / sbus_tty.c | stdio / include / stdio.h |
| src / sbus_tty.c | sysclib / include / sysclib.h |
| src / sbus_tty.c | excepman / include / excepman.h |
| src / sbus_tty.c | intrman / include / intrman.h |
| src / sbus_tty.c | ioman / include / ioman.h |

---

## PS2SDK: iop/debug/iop_sbusdbg -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000072_000537.html>

###### iop_sbusdbg → kernel Relation
| File in iop/debug/iop_sbusdbg | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/debug/iop_sbusdbg/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000073_000000.html>

###### src → common Relation
| File in iop/debug/iop_sbusdbg/src | Includes file in common |
| irx_imports.h | sbus / include / ps2_sbus.h |
| main.c | include / iop_cop0_defs.h |
| main.c | sbus / include / ps2_sbus.h |
| main.c | include / tamtypes.h |
| sbus_dbg.c | include / ps2_debug.h |
| sbus_dbg.c | sbus / include / ps2_sbus.h |
| sbus_dbg.c | include / tamtypes.h |
| sbus_tty.c | include / errno.h |
| sbus_tty.c | include / ps2_debug.h |
| sbus_tty.c | sbus / include / ps2_sbus.h |
| sbus_tty.c | include / tamtypes.h |
| sbus_tty.h | include / tamtypes.h |

---

## PS2SDK: iop/debug/iop_sbusdbg/src -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000073_000056.html>

###### src → cdvd Relation
| File in iop/debug/iop_sbusdbg/src | Includes file in iop/cdvd |
| irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/debug/iop_sbusdbg/src -&gt; iopdebug Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000073_000074.html>

###### src → iopdebug Relation
| File in iop/debug/iop_sbusdbg/src | Includes file in iop/debug/iopdebug |
| irx_imports.h | include / iopdebug.h |
| main.c | include / iopdebug.h |
| sbus_dbg.c | include / iopdebug.h |
| sbus_tty.c | include / iopdebug.h |

---

## PS2SDK: iop/debug/iop_sbusdbg/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000073_000223.html>

###### src → system Relation
| File in iop/debug/iop_sbusdbg/src | Includes file in iop/system |
| irx_imports.h | excepman / include / excepman.h |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | ioman / include / ioman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | modload / include / modload.h |
| irx_imports.h | sifman / include / sifman.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| main.c | excepman / include / excepman.h |
| main.c | loadcore / include / loadcore.h |
| main.c | stdio / include / stdio.h |
| main.c | threadman / include / thbase.h |
| sbus_dbg.c | excepman / include / excepman.h |
| sbus_dbg.c | intrman / include / intrman.h |
| sbus_dbg.c | ioman / include / ioman.h |
| sbus_dbg.c | loadcore / include / loadcore.h |
| sbus_dbg.c | stdio / include / stdio.h |
| sbus_dbg.c | sysclib / include / sysclib.h |
| sbus_dbg.c | threadman / include / thbase.h |
| sbus_tty.c | excepman / include / excepman.h |
| sbus_tty.c | intrman / include / intrman.h |
| sbus_tty.c | ioman / include / ioman.h |
| sbus_tty.c | stdio / include / stdio.h |
| sbus_tty.c | sysclib / include / sysclib.h |

---

## PS2SDK: iop/debug/iop_sbusdbg/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000073_000537.html>

###### src → kernel Relation
| File in iop/debug/iop_sbusdbg/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/debug/iopdebug -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000074_000000.html>

###### iopdebug → common Relation
| File in iop/debug/iopdebug | Includes file in common |
| include / iopdebug.h | include / iop_cop0_defs.h |
| include / iopdebug.h | include / ps2_debug.h |
| src / iop_debug.c | include / tamtypes.h |
| src / iop_debug.c | include / iop_cop0_defs.h |
| src / iop_debug.c | include / ps2_debug.h |
| src / iopdebug_priv.h | include / tamtypes.h |
| src / main.c | include / tamtypes.h |

---

## PS2SDK: iop/debug/iopdebug -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000074_000056.html>

###### iopdebug → cdvd Relation
| File in iop/debug/iopdebug | Includes file in iop/cdvd |
| src / irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/debug/iopdebug -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000074_000223.html>

###### iopdebug → system Relation
| File in iop/debug/iopdebug | Includes file in iop/system |
| src / iop_debug.c | excepman / include / excepman.h |
| src / iopdebug_priv.h | intrman / include / intrman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | sifman / include / sifman.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | ioman / include / ioman.h |
| src / irx_imports.h | modload / include / modload.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | excepman / include / excepman.h |
| src / main.c | stdio / include / stdio.h |
| src / main.c | loadcore / include / loadcore.h |
| src / main.c | threadman / include / thbase.h |

---

## PS2SDK: iop/debug/iopdebug -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000074_000537.html>

###### iopdebug → kernel Relation
| File in iop/debug/iopdebug | Includes file in iop/kernel |
| include / iopdebug.h | include / irx.h |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/debug/iopdebug/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000075_000000.html>

###### src → common Relation
| File in iop/debug/iopdebug/src | Includes file in common |
| iop_debug.c | include / iop_cop0_defs.h |
| iop_debug.c | include / ps2_debug.h |
| iop_debug.c | include / tamtypes.h |
| iopdebug_priv.h | include / tamtypes.h |
| main.c | include / tamtypes.h |

---

## PS2SDK: iop/debug/iopdebug/src -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000075_000056.html>

###### src → cdvd Relation
| File in iop/debug/iopdebug/src | Includes file in iop/cdvd |
| irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/debug/iopdebug/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000075_000223.html>

###### src → system Relation
| File in iop/debug/iopdebug/src | Includes file in iop/system |
| iop_debug.c | excepman / include / excepman.h |
| iopdebug_priv.h | intrman / include / intrman.h |
| irx_imports.h | excepman / include / excepman.h |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | ioman / include / ioman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | modload / include / modload.h |
| irx_imports.h | sifman / include / sifman.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| main.c | loadcore / include / loadcore.h |
| main.c | stdio / include / stdio.h |
| main.c | threadman / include / thbase.h |

---

## PS2SDK: iop/debug/iopdebug/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000075_000499.html>

###### src → include Relation
| File in iop/debug/iopdebug/src | Includes file in iop/debug/iopdebug/include |
| iop_debug.c | iopdebug.h |
| main.c | iopdebug.h |

---

## PS2SDK: iop/debug/iopdebug/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000075_000537.html>

###### src → kernel Relation
| File in iop/debug/iopdebug/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/debug/ioptrap -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000076_000000.html>

###### ioptrap → common Relation
| File in iop/debug/ioptrap | Includes file in common |
| src / breakpoint.c | include / mipscopaccess.h |

---

## PS2SDK: iop/debug/ioptrap -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000076_000223.html>

###### ioptrap → system Relation
| File in iop/debug/ioptrap | Includes file in iop/system |
| src / ioptrap.c | excepman / include / excepman.h |
| src / ioptrap.c | loadcore / include / loadcore.h |
| src / ioptrap.c | sifman / include / sifman.h |
| src / ioptrap.c | stdio / include / stdio.h |
| src / ioptrap.c | sysclib / include / sysclib.h |
| src / ioptrap.c | threadman / include / thbase.h |
| src / irx_imports.h | excepman / include / excepman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | sifman / include / sifman.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |

---

## PS2SDK: iop/debug/ioptrap -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000076_000537.html>

###### ioptrap → kernel Relation
| File in iop/debug/ioptrap | Includes file in iop/kernel |
| include / ioptrap.h | include / irx.h |
| src / ioptrap.c | include / defs.h |
| src / ioptrap.c | include / irx.h |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/debug/ioptrap/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000077_000000.html>

###### src → common Relation
| File in iop/debug/ioptrap/src | Includes file in common |
| breakpoint.c | include / mipscopaccess.h |

---

## PS2SDK: iop/debug/ioptrap/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000077_000223.html>

###### src → system Relation
| File in iop/debug/ioptrap/src | Includes file in iop/system |
| ioptrap.c | excepman / include / excepman.h |
| ioptrap.c | loadcore / include / loadcore.h |
| ioptrap.c | sifman / include / sifman.h |
| ioptrap.c | stdio / include / stdio.h |
| ioptrap.c | sysclib / include / sysclib.h |
| ioptrap.c | threadman / include / thbase.h |
| irx_imports.h | excepman / include / excepman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | sifman / include / sifman.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |

---

## PS2SDK: iop/debug/ioptrap/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000077_000500.html>

###### src → include Relation
| File in iop/debug/ioptrap/src | Includes file in iop/debug/ioptrap/include |
| breakpoint.c | ioptrap.h |
| ioptrap.c | ioptrap.h |

---

## PS2SDK: iop/debug/ioptrap/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000077_000537.html>

###### src → kernel Relation
| File in iop/debug/ioptrap/src | Includes file in iop/kernel |
| ioptrap.c | include / defs.h |
| ioptrap.c | include / irx.h |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/debug/ppctty -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000078_000000.html>

###### ppctty → common Relation
| File in iop/debug/ppctty | Includes file in common |
| src / main.c | include / tamtypes.h |
| src / main.c | include / iop_regs.h |
| src / tty.c | include / tamtypes.h |
| src / tty.c | include / errno.h |
| src / tty.h | include / tamtypes.h |

---

## PS2SDK: iop/debug/ppctty -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000078_000223.html>

###### ppctty → system Relation
| File in iop/debug/ppctty | Includes file in iop/system |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | ioman / include / ioman.h |
| src / irx_imports.h | modload / include / modload.h |
| src / irx_imports.h | threadman / include / thsemap.h |
| src / main.c | stdio / include / stdio.h |
| src / main.c | loadcore / include / loadcore.h |
| src / main.c | excepman / include / excepman.h |
| src / main.c | ioman / include / ioman.h |
| src / tty.c | stdio / include / stdio.h |
| src / tty.c | sysclib / include / sysclib.h |
| src / tty.c | excepman / include / excepman.h |
| src / tty.c | intrman / include / intrman.h |
| src / tty.c | ioman / include / ioman.h |
| src / tty.c | threadman / include / thsemap.h |

---

## PS2SDK: iop/debug/ppctty -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000078_000537.html>

###### ppctty → kernel Relation
| File in iop/debug/ppctty | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/debug/ppctty/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000079_000000.html>

###### src → common Relation
| File in iop/debug/ppctty/src | Includes file in common |
| main.c | include / iop_regs.h |
| main.c | include / tamtypes.h |
| tty.c | include / errno.h |
| tty.c | include / tamtypes.h |
| tty.h | include / tamtypes.h |

---

## PS2SDK: iop/debug/ppctty/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000079_000223.html>

###### src → system Relation
| File in iop/debug/ppctty/src | Includes file in iop/system |
| irx_imports.h | ioman / include / ioman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | modload / include / modload.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thsemap.h |
| main.c | excepman / include / excepman.h |
| main.c | ioman / include / ioman.h |
| main.c | loadcore / include / loadcore.h |
| main.c | stdio / include / stdio.h |
| tty.c | excepman / include / excepman.h |
| tty.c | intrman / include / intrman.h |
| tty.c | ioman / include / ioman.h |
| tty.c | stdio / include / stdio.h |
| tty.c | sysclib / include / sysclib.h |
| tty.c | threadman / include / thsemap.h |

---

## PS2SDK: iop/debug/ppctty/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000079_000537.html>

###### src → kernel Relation
| File in iop/debug/ppctty/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/debug/sior -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000080_000000.html>

###### sior → common Relation
| File in iop/debug/sior | Includes file in common |
| include / sior.h | include / sior-common.h |
| src / xprintf.c | include / tamtypes.h |
| src / xprintf.c | include / ps2lib_err.h |

---

## PS2SDK: iop/debug/sior -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000080_000223.html>

###### sior → system Relation
| File in iop/debug/sior | Includes file in iop/system |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / xprintf.c | stdio / include / stdio.h |
| src / xprintf.c | sysclib / include / sysclib.h |
| src / xprintf.c | sysclib / include / ctype.h |

---

## PS2SDK: iop/debug/sior -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000080_000537.html>

###### sior → kernel Relation
| File in iop/debug/sior | Includes file in iop/kernel |
| include / sior.h | include / irx.h |
| src / irx_imports.h | include / irx.h |
| src / sior.c | include / defs.h |
| src / sior.c | include / irx.h |

---

## PS2SDK: iop/debug/sior/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000081_000000.html>

###### src → common Relation
| File in iop/debug/sior/src | Includes file in common |
| xprintf.c | include / ps2lib_err.h |
| xprintf.c | include / tamtypes.h |

---

## PS2SDK: iop/debug/sior/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000081_000223.html>

###### src → system Relation
| File in iop/debug/sior/src | Includes file in iop/system |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| xprintf.c | sysclib / include / ctype.h |
| xprintf.c | stdio / include / stdio.h |
| xprintf.c | sysclib / include / sysclib.h |

---

## PS2SDK: iop/debug/sior/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000081_000501.html>

###### src → include Relation
| File in iop/debug/sior/src | Includes file in iop/debug/sior/include |
| sior.c | sior.h |

---

## PS2SDK: iop/debug/sior/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000081_000537.html>

###### src → kernel Relation
| File in iop/debug/sior/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |
| sior.c | include / defs.h |
| sior.c | include / irx.h |

---

## PS2SDK: iop/debug/thmon -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000082_000223.html>

###### thmon → system Relation
| File in iop/debug/thmon | Includes file in iop/system |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | ioman / include / ioman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thevent.h |
| src / irx_imports.h | threadman / include / thmsgbx.h |
| src / irx_imports.h | threadman / include / thsemap.h |

---

## PS2SDK: iop/debug/thmon -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000082_000537.html>

###### thmon → kernel Relation
| File in iop/debug/thmon | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/debug/thmon/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000083_000223.html>

###### src → system Relation
| File in iop/debug/thmon/src | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | ioman / include / ioman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thevent.h |
| irx_imports.h | threadman / include / thmsgbx.h |
| irx_imports.h | threadman / include / thsemap.h |

---

## PS2SDK: iop/debug/thmon/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000083_000537.html>

###### src → kernel Relation
| File in iop/debug/thmon/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/deckard -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000084_000000.html>

###### deckard → common Relation
| File in iop/deckard | Includes file in common |
| xparam / src / xparam.c | include / tamtypes.h |
| xparam / src / xparam.c | include / iop_regs.h |

---

## PS2SDK: iop/deckard -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000084_000223.html>

###### deckard → system Relation
| File in iop/deckard | Includes file in iop/system |
| xparam / src / irx_imports.h | loadcore / include / loadcore.h |
| xparam / src / irx_imports.h | sysclib / include / sysclib.h |

---

## PS2SDK: iop/deckard -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000084_000537.html>

###### deckard → kernel Relation
| File in iop/deckard | Includes file in iop/kernel |
| xparam / src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/deckard/xparam -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000085_000000.html>

###### xparam → common Relation
| File in iop/deckard/xparam | Includes file in common |
| src / xparam.c | include / iop_regs.h |
| src / xparam.c | include / tamtypes.h |

---

## PS2SDK: iop/deckard/xparam -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000085_000223.html>

###### xparam → system Relation
| File in iop/deckard/xparam | Includes file in iop/system |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | sysclib / include / sysclib.h |

---

## PS2SDK: iop/deckard/xparam -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000085_000537.html>

###### xparam → kernel Relation
| File in iop/deckard/xparam | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/deckard/xparam/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000086_000000.html>

###### src → common Relation
| File in iop/deckard/xparam/src | Includes file in common |
| xparam.c | include / iop_regs.h |
| xparam.c | include / tamtypes.h |

---

## PS2SDK: iop/deckard/xparam/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000086_000223.html>

###### src → system Relation
| File in iop/deckard/xparam/src | Includes file in iop/system |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | sysclib / include / sysclib.h |

---

## PS2SDK: iop/deckard/xparam/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000086_000537.html>

###### src → kernel Relation
| File in iop/deckard/xparam/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/dev9 -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000087_000000.html>

###### dev9 → common Relation
| File in iop/dev9 | Includes file in common |
| dev9 / include / aifdev9.h | include / aifregs.h |
| dev9 / include / dev9.h | include / hdd-ioctl.h |
| atad / src / ps2atad.c | include / atahw.h |
| hdpro_atad / src / hdproatad.c | include / atahw.h |
| poweroff / src / poweroff.c | include / pwroff_rpc.h |
| pvrdrv / src / dvrdrv.c | include / tamtypes.h |
| pvrdrv / src / dvrdrv.c | include / speedregs.h |
| dev9 / src / ps2dev9.c | include / aifregs.h |
| dev9 / src / ps2dev9.c | include / dev9regs.h |
| dev9 / src / ps2dev9.c | include / speedregs.h |
| dev9 / src / ps2dev9.c | include / smapregs.h |
| extflash / src / extflash.c | include / dev9regs.h |
| extflash / src / extflash.c | include / speedregs.h |

---

## PS2SDK: iop/dev9 -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000087_000223.html>

###### dev9 → system Relation
| File in iop/dev9 | Includes file in iop/system |
| atad / src / irx_imports.h | loadcore / include / loadcore.h |
| atad / src / irx_imports.h | stdio / include / stdio.h |
| atad / src / irx_imports.h | sysclib / include / sysclib.h |
| atad / src / irx_imports.h | threadman / include / thbase.h |
| atad / src / irx_imports.h | threadman / include / thevent.h |
| atad / src / ps2atad.c | loadcore / include / loadcore.h |
| atad / src / ps2atad.c | threadman / include / thbase.h |
| atad / src / ps2atad.c | threadman / include / thevent.h |
| atad / src / ps2atad.c | stdio / include / stdio.h |
| atad / src / ps2atad.c | sysclib / include / sysclib.h |
| hdpro_atad / src / hdproatad.c | loadcore / include / loadcore.h |
| hdpro_atad / src / hdproatad.c | intrman / include / intrman.h |
| hdpro_atad / src / hdproatad.c | threadman / include / thbase.h |
| hdpro_atad / src / hdproatad.c | threadman / include / thevent.h |
| hdpro_atad / src / hdproatad.c | stdio / include / stdio.h |
| hdpro_atad / src / hdproatad.c | sysclib / include / sysclib.h |
| hdpro_atad / src / irx_imports.h | intrman / include / intrman.h |
| hdpro_atad / src / irx_imports.h | loadcore / include / loadcore.h |
| hdpro_atad / src / irx_imports.h | stdio / include / stdio.h |
| hdpro_atad / src / irx_imports.h | sysclib / include / sysclib.h |
| hdpro_atad / src / irx_imports.h | threadman / include / thbase.h |
| hdpro_atad / src / irx_imports.h | threadman / include / thevent.h |
| poweroff / src / irx_imports.h | loadcore / include / loadcore.h |
| poweroff / src / irx_imports.h | stdio / include / stdio.h |
| poweroff / src / irx_imports.h | sysclib / include / sysclib.h |
| poweroff / src / irx_imports.h | threadman / include / thbase.h |
| poweroff / src / poweroff.c | loadcore / include / loadcore.h |
| poweroff / src / poweroff.c | stdio / include / stdio.h |
| poweroff / src / poweroff.c | sysclib / include / sysclib.h |
| poweroff / src / poweroff.c | threadman / include / thbase.h |
| poweroff / src / poweroff.c | intrman / include / intrman.h |
| poweroff / src / poweroff.c | threadman / include / thsemap.h |
| pvrdrv / src / dvrdrv.c | intrman / include / intrman.h |
| pvrdrv / src / dvrdrv.c | loadcore / include / loadcore.h |
| pvrdrv / src / dvrdrv.c | stdio / include / stdio.h |
| pvrdrv / src / dvrdrv.c | threadman / include / thbase.h |
| pvrdrv / src / dvrdrv.c | threadman / include / thsemap.h |
| pvrdrv / src / irx_imports.h | intrman / include / intrman.h |
| pvrdrv / src / irx_imports.h | loadcore / include / loadcore.h |
| pvrdrv / src / irx_imports.h | stdio / include / stdio.h |
| pvrdrv / src / irx_imports.h | threadman / include / thbase.h |
| pvrdrv / src / irx_imports.h | threadman / include / thsemap.h |
| dev9 / src / irx_imports.h | dmacman / include / dmacman.h |
| dev9 / src / irx_imports.h | intrman / include / intrman.h |
| dev9 / src / irx_imports.h | ioman / include / ioman.h |
| dev9 / src / irx_imports.h | loadcore / include / loadcore.h |
| dev9 / src / irx_imports.h | stdio / include / stdio.h |
| dev9 / src / irx_imports.h | sysclib / include / sysclib.h |
| dev9 / src / irx_imports.h | threadman / include / thbase.h |
| dev9 / src / irx_imports.h | threadman / include / thsemap.h |
| dev9 / src / ps2dev9.c | loadcore / include / loadcore.h |
| dev9 / src / ps2dev9.c | intrman / include / intrman.h |
| dev9 / src / ps2dev9.c | iomanx / include / iomanX.h |
| dev9 / src / ps2dev9.c | dmacman / include / dmacman.h |
| dev9 / src / ps2dev9.c | threadman / include / thbase.h |
| dev9 / src / ps2dev9.c | threadman / include / thsemap.h |
| dev9 / src / ps2dev9.c | stdio / include / stdio.h |
| dev9 / src / ps2dev9.c | sysclib / include / sysclib.h |
| extflash / src / extflash.c | loadcore / include / loadcore.h |
| extflash / src / extflash.c | threadman / include / thbase.h |
| extflash / src / extflash.c | stdio / include / stdio.h |
| extflash / src / extflash.c | sysclib / include / sysclib.h |
| extflash / src / irx_imports.h | dmacman / include / dmacman.h |
| extflash / src / irx_imports.h | intrman / include / intrman.h |
| extflash / src / irx_imports.h | iomanx / include / iomanX.h |
| extflash / src / irx_imports.h | loadcore / include / loadcore.h |
| extflash / src / irx_imports.h | stdio / include / stdio.h |
| extflash / src / irx_imports.h | sysclib / include / sysclib.h |
| extflash / src / irx_imports.h | threadman / include / thbase.h |
| extflash / src / irx_imports.h | threadman / include / thevent.h |
| extflash / src / irx_imports.h | threadman / include / thmsgbx.h |
| extflash / src / irx_imports.h | threadman / include / thsemap.h |
| extflash / src / irx_imports.h | vblank / include / vblank.h |

---

## PS2SDK: iop/dev9 -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000087_000537.html>

###### dev9 → kernel Relation
| File in iop/dev9 | Includes file in iop/kernel |
| poweroff / include / poweroff.h | include / irx.h |
| atad / include / atad.h | include / irx.h |
| dev9 / include / aifdev9.h | include / irx.h |
| dev9 / include / dev9.h | include / irx.h |
| pvrdrv / include / pvrdrv.h | include / irx.h |
| atad / src / irx_imports.h | include / irx.h |
| atad / src / ps2atad.c | include / defs.h |
| atad / src / ps2atad.c | include / irx.h |
| hdpro_atad / src / hdproatad.c | include / defs.h |
| hdpro_atad / src / hdproatad.c | include / irx.h |
| hdpro_atad / src / irx_imports.h | include / irx.h |
| poweroff / src / irx_imports.h | include / irx.h |
| poweroff / src / poweroff.c | include / defs.h |
| poweroff / src / poweroff.c | include / irx.h |
| pvrdrv / src / dvrdrv.c | include / irx.h |
| pvrdrv / src / irx_imports.h | include / irx.h |
| dev9 / src / irx_imports.h | include / irx.h |
| dev9 / src / ps2dev9.c | include / defs.h |
| extflash / src / extflash.c | include / defs.h |
| extflash / src / extflash.c | include / irx.h |
| extflash / src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/dev9/atad -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000088_000000.html>

###### atad → common Relation
| File in iop/dev9/atad | Includes file in common |
| src / ps2atad.c | include / atahw.h |

---

## PS2SDK: iop/dev9/atad -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000088_000223.html>

###### atad → system Relation
| File in iop/dev9/atad | Includes file in iop/system |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thevent.h |
| src / ps2atad.c | loadcore / include / loadcore.h |
| src / ps2atad.c | threadman / include / thbase.h |
| src / ps2atad.c | threadman / include / thevent.h |
| src / ps2atad.c | stdio / include / stdio.h |
| src / ps2atad.c | sysclib / include / sysclib.h |

---

## PS2SDK: iop/dev9/atad -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000088_000537.html>

###### atad → kernel Relation
| File in iop/dev9/atad | Includes file in iop/kernel |
| include / atad.h | include / irx.h |
| src / irx_imports.h | include / irx.h |
| src / ps2atad.c | include / defs.h |
| src / ps2atad.c | include / irx.h |

---

## PS2SDK: iop/dev9/atad/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000089_000000.html>

###### src → common Relation
| File in iop/dev9/atad/src | Includes file in common |
| ps2atad.c | include / atahw.h |

---

## PS2SDK: iop/dev9/atad/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000089_000223.html>

###### src → system Relation
| File in iop/dev9/atad/src | Includes file in iop/system |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thevent.h |
| ps2atad.c | loadcore / include / loadcore.h |
| ps2atad.c | stdio / include / stdio.h |
| ps2atad.c | sysclib / include / sysclib.h |
| ps2atad.c | threadman / include / thbase.h |
| ps2atad.c | threadman / include / thevent.h |

---

## PS2SDK: iop/dev9/atad/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000089_000503.html>

###### src → include Relation
| File in iop/dev9/atad/src | Includes file in iop/dev9/atad/include |
| ps2atad.c | atad.h |

---

## PS2SDK: iop/dev9/atad/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000089_000537.html>

###### src → kernel Relation
| File in iop/dev9/atad/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |
| ps2atad.c | include / defs.h |
| ps2atad.c | include / irx.h |

---

## PS2SDK: iop/dev9/dev9 -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000090_000000.html>

###### dev9 → common Relation
| File in iop/dev9/dev9 | Includes file in common |
| include / aifdev9.h | include / aifregs.h |
| include / dev9.h | include / hdd-ioctl.h |
| src / ps2dev9.c | include / aifregs.h |
| src / ps2dev9.c | include / dev9regs.h |
| src / ps2dev9.c | include / speedregs.h |
| src / ps2dev9.c | include / smapregs.h |

---

## PS2SDK: iop/dev9/dev9 -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000090_000223.html>

###### dev9 → system Relation
| File in iop/dev9/dev9 | Includes file in iop/system |
| src / irx_imports.h | dmacman / include / dmacman.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | ioman / include / ioman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thsemap.h |
| src / ps2dev9.c | loadcore / include / loadcore.h |
| src / ps2dev9.c | intrman / include / intrman.h |
| src / ps2dev9.c | iomanx / include / iomanX.h |
| src / ps2dev9.c | dmacman / include / dmacman.h |
| src / ps2dev9.c | threadman / include / thbase.h |
| src / ps2dev9.c | threadman / include / thsemap.h |
| src / ps2dev9.c | stdio / include / stdio.h |
| src / ps2dev9.c | sysclib / include / sysclib.h |

---

## PS2SDK: iop/dev9/dev9 -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000090_000537.html>

###### dev9 → kernel Relation
| File in iop/dev9/dev9 | Includes file in iop/kernel |
| include / aifdev9.h | include / irx.h |
| include / dev9.h | include / irx.h |
| src / irx_imports.h | include / irx.h |
| src / ps2dev9.c | include / defs.h |

---

## PS2SDK: iop/dev9/dev9/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000091_000000.html>

###### src → common Relation
| File in iop/dev9/dev9/src | Includes file in common |
| ps2dev9.c | include / aifregs.h |
| ps2dev9.c | include / dev9regs.h |
| ps2dev9.c | include / smapregs.h |
| ps2dev9.c | include / speedregs.h |

---

## PS2SDK: iop/dev9/dev9/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000091_000223.html>

###### src → system Relation
| File in iop/dev9/dev9/src | Includes file in iop/system |
| irx_imports.h | dmacman / include / dmacman.h |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | ioman / include / ioman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thsemap.h |
| ps2dev9.c | dmacman / include / dmacman.h |
| ps2dev9.c | intrman / include / intrman.h |
| ps2dev9.c | iomanx / include / iomanX.h |
| ps2dev9.c | loadcore / include / loadcore.h |
| ps2dev9.c | stdio / include / stdio.h |
| ps2dev9.c | sysclib / include / sysclib.h |
| ps2dev9.c | threadman / include / thbase.h |
| ps2dev9.c | threadman / include / thsemap.h |

---

## PS2SDK: iop/dev9/dev9/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000091_000504.html>

###### src → include Relation
| File in iop/dev9/dev9/src | Includes file in iop/dev9/dev9/include |
| ps2dev9.c | dev9.h |

---

## PS2SDK: iop/dev9/dev9/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000091_000537.html>

###### src → kernel Relation
| File in iop/dev9/dev9/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |
| ps2dev9.c | include / defs.h |

---

## PS2SDK: iop/dev9/extflash -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000092_000000.html>

###### extflash → common Relation
| File in iop/dev9/extflash | Includes file in common |
| src / extflash.c | include / dev9regs.h |
| src / extflash.c | include / speedregs.h |

---

## PS2SDK: iop/dev9/extflash -&gt; dev9 Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000092_000090.html>

###### extflash → dev9 Relation
| File in iop/dev9/extflash | Includes file in iop/dev9/dev9 |
| src / irx_imports.h | include / dev9.h |

---

## PS2SDK: iop/dev9/extflash -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000092_000223.html>

###### extflash → system Relation
| File in iop/dev9/extflash | Includes file in iop/system |
| src / extflash.c | loadcore / include / loadcore.h |
| src / extflash.c | threadman / include / thbase.h |
| src / extflash.c | stdio / include / stdio.h |
| src / extflash.c | sysclib / include / sysclib.h |
| src / irx_imports.h | dmacman / include / dmacman.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | iomanx / include / iomanX.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thevent.h |
| src / irx_imports.h | threadman / include / thmsgbx.h |
| src / irx_imports.h | threadman / include / thsemap.h |
| src / irx_imports.h | vblank / include / vblank.h |

---

## PS2SDK: iop/dev9/extflash -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000092_000537.html>

###### extflash → kernel Relation
| File in iop/dev9/extflash | Includes file in iop/kernel |
| src / extflash.c | include / defs.h |
| src / extflash.c | include / irx.h |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/dev9/extflash/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000093_000000.html>

###### src → common Relation
| File in iop/dev9/extflash/src | Includes file in common |
| extflash.c | include / dev9regs.h |
| extflash.c | include / speedregs.h |

---

## PS2SDK: iop/dev9/extflash/src -&gt; dev9 Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000093_000090.html>

###### src → dev9 Relation
| File in iop/dev9/extflash/src | Includes file in iop/dev9/dev9 |
| irx_imports.h | include / dev9.h |

---

## PS2SDK: iop/dev9/extflash/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000093_000223.html>

###### src → system Relation
| File in iop/dev9/extflash/src | Includes file in iop/system |
| extflash.c | loadcore / include / loadcore.h |
| extflash.c | stdio / include / stdio.h |
| extflash.c | sysclib / include / sysclib.h |
| extflash.c | threadman / include / thbase.h |
| irx_imports.h | dmacman / include / dmacman.h |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | iomanx / include / iomanX.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thevent.h |
| irx_imports.h | threadman / include / thmsgbx.h |
| irx_imports.h | threadman / include / thsemap.h |
| irx_imports.h | vblank / include / vblank.h |

---

## PS2SDK: iop/dev9/extflash/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000093_000505.html>

###### src → include Relation
| File in iop/dev9/extflash/src | Includes file in iop/dev9/extflash/include |
| extflash.c | fls.h |

---

## PS2SDK: iop/dev9/extflash/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000093_000537.html>

###### src → kernel Relation
| File in iop/dev9/extflash/src | Includes file in iop/kernel |
| extflash.c | include / defs.h |
| extflash.c | include / irx.h |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/dev9/hdpro_atad -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000094_000000.html>

###### hdpro_atad → common Relation
| File in iop/dev9/hdpro_atad | Includes file in common |
| src / hdproatad.c | include / atahw.h |

---

## PS2SDK: iop/dev9/hdpro_atad -&gt; atad Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000094_000088.html>

###### hdpro_atad → atad Relation
| File in iop/dev9/hdpro_atad | Includes file in iop/dev9/atad |
| src / hdproatad.c | include / atad.h |

---

## PS2SDK: iop/dev9/hdpro_atad -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000094_000223.html>

###### hdpro_atad → system Relation
| File in iop/dev9/hdpro_atad | Includes file in iop/system |
| src / hdproatad.c | loadcore / include / loadcore.h |
| src / hdproatad.c | intrman / include / intrman.h |
| src / hdproatad.c | threadman / include / thbase.h |
| src / hdproatad.c | threadman / include / thevent.h |
| src / hdproatad.c | stdio / include / stdio.h |
| src / hdproatad.c | sysclib / include / sysclib.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thevent.h |

---

## PS2SDK: iop/dev9/hdpro_atad -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000094_000537.html>

###### hdpro_atad → kernel Relation
| File in iop/dev9/hdpro_atad | Includes file in iop/kernel |
| src / hdproatad.c | include / defs.h |
| src / hdproatad.c | include / irx.h |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/dev9/hdpro_atad/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000095_000000.html>

###### src → common Relation
| File in iop/dev9/hdpro_atad/src | Includes file in common |
| hdproatad.c | include / atahw.h |

---

## PS2SDK: iop/dev9/hdpro_atad/src -&gt; atad Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000095_000088.html>

###### src → atad Relation
| File in iop/dev9/hdpro_atad/src | Includes file in iop/dev9/atad |
| hdproatad.c | include / atad.h |

---

## PS2SDK: iop/dev9/hdpro_atad/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000095_000223.html>

###### src → system Relation
| File in iop/dev9/hdpro_atad/src | Includes file in iop/system |
| hdproatad.c | intrman / include / intrman.h |
| hdproatad.c | loadcore / include / loadcore.h |
| hdproatad.c | stdio / include / stdio.h |
| hdproatad.c | sysclib / include / sysclib.h |
| hdproatad.c | threadman / include / thbase.h |
| hdproatad.c | threadman / include / thevent.h |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thevent.h |

---

## PS2SDK: iop/dev9/hdpro_atad/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000095_000537.html>

###### src → kernel Relation
| File in iop/dev9/hdpro_atad/src | Includes file in iop/kernel |
| hdproatad.c | include / defs.h |
| hdproatad.c | include / irx.h |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/dev9/poweroff -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000096_000000.html>

###### poweroff → common Relation
| File in iop/dev9/poweroff | Includes file in common |
| src / poweroff.c | include / pwroff_rpc.h |

---

## PS2SDK: iop/dev9/poweroff -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000096_000223.html>

###### poweroff → system Relation
| File in iop/dev9/poweroff | Includes file in iop/system |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / poweroff.c | loadcore / include / loadcore.h |
| src / poweroff.c | stdio / include / stdio.h |
| src / poweroff.c | sysclib / include / sysclib.h |
| src / poweroff.c | threadman / include / thbase.h |
| src / poweroff.c | intrman / include / intrman.h |
| src / poweroff.c | threadman / include / thsemap.h |

---

## PS2SDK: iop/dev9/poweroff -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000096_000537.html>

###### poweroff → kernel Relation
| File in iop/dev9/poweroff | Includes file in iop/kernel |
| include / poweroff.h | include / irx.h |
| src / irx_imports.h | include / irx.h |
| src / poweroff.c | include / defs.h |
| src / poweroff.c | include / irx.h |

---

## PS2SDK: iop/dev9/poweroff/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000097_000000.html>

###### src → common Relation
| File in iop/dev9/poweroff/src | Includes file in common |
| poweroff.c | include / pwroff_rpc.h |

---

## PS2SDK: iop/dev9/poweroff/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000097_000223.html>

###### src → system Relation
| File in iop/dev9/poweroff/src | Includes file in iop/system |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| poweroff.c | intrman / include / intrman.h |
| poweroff.c | loadcore / include / loadcore.h |
| poweroff.c | stdio / include / stdio.h |
| poweroff.c | sysclib / include / sysclib.h |
| poweroff.c | threadman / include / thbase.h |
| poweroff.c | threadman / include / thsemap.h |

---

## PS2SDK: iop/dev9/poweroff/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000097_000506.html>

###### src → include Relation
| File in iop/dev9/poweroff/src | Includes file in iop/dev9/poweroff/include |
| poweroff.c | poweroff.h |

---

## PS2SDK: iop/dev9/poweroff/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000097_000537.html>

###### src → kernel Relation
| File in iop/dev9/poweroff/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |
| poweroff.c | include / defs.h |
| poweroff.c | include / irx.h |

---

## PS2SDK: iop/dev9/pvrdrv -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000098_000000.html>

###### pvrdrv → common Relation
| File in iop/dev9/pvrdrv | Includes file in common |
| src / dvrdrv.c | include / tamtypes.h |
| src / dvrdrv.c | include / speedregs.h |

---

## PS2SDK: iop/dev9/pvrdrv -&gt; dev9 Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000098_000090.html>

###### pvrdrv → dev9 Relation
| File in iop/dev9/pvrdrv | Includes file in iop/dev9/dev9 |
| src / dvrdrv.c | include / dev9.h |
| src / irx_imports.h | include / dev9.h |

---

## PS2SDK: iop/dev9/pvrdrv -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000098_000223.html>

###### pvrdrv → system Relation
| File in iop/dev9/pvrdrv | Includes file in iop/system |
| src / dvrdrv.c | intrman / include / intrman.h |
| src / dvrdrv.c | loadcore / include / loadcore.h |
| src / dvrdrv.c | stdio / include / stdio.h |
| src / dvrdrv.c | threadman / include / thbase.h |
| src / dvrdrv.c | threadman / include / thsemap.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thsemap.h |

---

## PS2SDK: iop/dev9/pvrdrv -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000098_000537.html>

###### pvrdrv → kernel Relation
| File in iop/dev9/pvrdrv | Includes file in iop/kernel |
| include / pvrdrv.h | include / irx.h |
| src / dvrdrv.c | include / irx.h |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/dev9/pvrdrv/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000099_000000.html>

###### src → common Relation
| File in iop/dev9/pvrdrv/src | Includes file in common |
| dvrdrv.c | include / speedregs.h |
| dvrdrv.c | include / tamtypes.h |

---

## PS2SDK: iop/dev9/pvrdrv/src -&gt; dev9 Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000099_000090.html>

###### src → dev9 Relation
| File in iop/dev9/pvrdrv/src | Includes file in iop/dev9/dev9 |
| dvrdrv.c | include / dev9.h |
| irx_imports.h | include / dev9.h |

---

## PS2SDK: iop/dev9/pvrdrv/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000099_000223.html>

###### src → system Relation
| File in iop/dev9/pvrdrv/src | Includes file in iop/system |
| dvrdrv.c | intrman / include / intrman.h |
| dvrdrv.c | loadcore / include / loadcore.h |
| dvrdrv.c | stdio / include / stdio.h |
| dvrdrv.c | threadman / include / thbase.h |
| dvrdrv.c | threadman / include / thsemap.h |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thsemap.h |

---

## PS2SDK: iop/dev9/pvrdrv/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000099_000507.html>

###### src → include Relation
| File in iop/dev9/pvrdrv/src | Includes file in iop/dev9/pvrdrv/include |
| dvrdrv.c | pvrdrv.h |

---

## PS2SDK: iop/dev9/pvrdrv/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000099_000537.html>

###### src → kernel Relation
| File in iop/dev9/pvrdrv/src | Includes file in iop/kernel |
| dvrdrv.c | include / irx.h |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/dvrp -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000100_000000.html>

###### dvrp → common Relation
| File in iop/dvrp | Includes file in common |
| dvrfile / src / dvrfile.c | include / speedregs.h |
| dvrfile / src / dvrfile.c | include / errno.h |
| dvrmisc / src / dvrmisc.c | include / speedregs.h |
| dvrmisc / src / dvrmisc.c | include / errno.h |
| dvripl / src / dvripl.c | include / speedregs.h |
| dvripl / src / dvripl.c | include / errno.h |
| dvrav / src / dvrav.c | include / speedregs.h |
| dvrav / src / dvrav.c | include / errno.h |
| dvrdv / src / dvrdv.c | include / speedregs.h |
| dvrdv / src / dvrdv.c | include / errno.h |
| dvr / src / dvr.c | include / speedregs.h |
| dvr / src / dvr.c | include / errno.h |

---

## PS2SDK: iop/dvrp -&gt; dev9 Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000100_000087.html>

###### dvrp → dev9 Relation
| File in iop/dvrp | Includes file in iop/dev9 |
| dvrfile / src / dvrfile.c | pvrdrv / include / pvrdrv.h |
| dvrfile / src / irx_imports.h | pvrdrv / include / pvrdrv.h |
| dvrmisc / src / dvrmisc.c | pvrdrv / include / pvrdrv.h |
| dvrmisc / src / irx_imports.h | pvrdrv / include / pvrdrv.h |
| dvripl / src / dvripl.c | pvrdrv / include / pvrdrv.h |
| dvripl / src / irx_imports.h | pvrdrv / include / pvrdrv.h |
| dvrav / src / dvrav.c | pvrdrv / include / pvrdrv.h |
| dvrav / src / irx_imports.h | pvrdrv / include / pvrdrv.h |
| dvrdv / src / dvrdv.c | pvrdrv / include / pvrdrv.h |
| dvrdv / src / irx_imports.h | pvrdrv / include / pvrdrv.h |
| dvr / src / dvr.c | pvrdrv / include / pvrdrv.h |
| dvr / src / irx_imports.h | pvrdrv / include / pvrdrv.h |

---

## PS2SDK: iop/dvrp -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000100_000223.html>

###### dvrp → system Relation
| File in iop/dvrp | Includes file in iop/system |
| dvrfile / src / dvrfile.c | iomanx / include / iomanX.h |
| dvrfile / src / dvrfile.c | loadcore / include / loadcore.h |
| dvrfile / src / dvrfile.c | stdio / include / stdio.h |
| dvrfile / src / dvrfile.c | sysclib / include / sysclib.h |
| dvrfile / src / dvrfile.c | threadman / include / thbase.h |
| dvrfile / src / dvrfile.c | threadman / include / thsemap.h |
| dvrfile / src / irx_imports.h | iomanx / include / iomanX.h |
| dvrfile / src / irx_imports.h | stdio / include / stdio.h |
| dvrfile / src / irx_imports.h | sysclib / include / sysclib.h |
| dvrfile / src / irx_imports.h | threadman / include / thbase.h |
| dvrfile / src / irx_imports.h | threadman / include / thsemap.h |
| dvrmisc / src / dvrmisc.c | iomanx / include / iomanX.h |
| dvrmisc / src / dvrmisc.c | loadcore / include / loadcore.h |
| dvrmisc / src / dvrmisc.c | stdio / include / stdio.h |
| dvrmisc / src / dvrmisc.c | sysclib / include / sysclib.h |
| dvrmisc / src / dvrmisc.c | threadman / include / thbase.h |
| dvrmisc / src / dvrmisc.c | threadman / include / thsemap.h |
| dvrmisc / src / irx_imports.h | iomanx / include / iomanX.h |
| dvrmisc / src / irx_imports.h | stdio / include / stdio.h |
| dvrmisc / src / irx_imports.h | sysclib / include / sysclib.h |
| dvrmisc / src / irx_imports.h | threadman / include / thbase.h |
| dvrmisc / src / irx_imports.h | threadman / include / thsemap.h |
| dvripl / src / dvripl.c | iomanx / include / iomanX.h |
| dvripl / src / dvripl.c | loadcore / include / loadcore.h |
| dvripl / src / dvripl.c | stdio / include / stdio.h |
| dvripl / src / dvripl.c | threadman / include / thbase.h |
| dvripl / src / dvripl.c | threadman / include / thsemap.h |
| dvripl / src / dvripl.c | timrman / include / timrman.h |
| dvripl / src / irx_imports.h | iomanx / include / iomanX.h |
| dvripl / src / irx_imports.h | stdio / include / stdio.h |
| dvripl / src / irx_imports.h | threadman / include / thbase.h |
| dvripl / src / irx_imports.h | threadman / include / thsemap.h |
| dvripl / src / irx_imports.h | timrman / include / timrman.h |
| dvrav / src / dvrav.c | iomanx / include / iomanX.h |
| dvrav / src / dvrav.c | loadcore / include / loadcore.h |
| dvrav / src / dvrav.c | stdio / include / stdio.h |
| dvrav / src / dvrav.c | threadman / include / thbase.h |
| dvrav / src / dvrav.c | threadman / include / thsemap.h |
| dvrav / src / irx_imports.h | iomanx / include / iomanX.h |
| dvrav / src / irx_imports.h | stdio / include / stdio.h |
| dvrav / src / irx_imports.h | sysclib / include / sysclib.h |
| dvrav / src / irx_imports.h | threadman / include / thbase.h |
| dvrav / src / irx_imports.h | threadman / include / thsemap.h |
| dvrdv / src / dvrdv.c | iomanx / include / iomanX.h |
| dvrdv / src / dvrdv.c | loadcore / include / loadcore.h |
| dvrdv / src / dvrdv.c | stdio / include / stdio.h |
| dvrdv / src / dvrdv.c | threadman / include / thbase.h |
| dvrdv / src / dvrdv.c | threadman / include / thsemap.h |
| dvrdv / src / irx_imports.h | iomanx / include / iomanX.h |
| dvrdv / src / irx_imports.h | stdio / include / stdio.h |
| dvrdv / src / irx_imports.h | threadman / include / thbase.h |
| dvrdv / src / irx_imports.h | threadman / include / thsemap.h |
| dvr / src / dvr.c | iomanx / include / iomanX.h |
| dvr / src / dvr.c | loadcore / include / loadcore.h |
| dvr / src / dvr.c | stdio / include / stdio.h |
| dvr / src / dvr.c | sysclib / include / sysclib.h |
| dvr / src / dvr.c | threadman / include / thbase.h |
| dvr / src / dvr.c | threadman / include / thsemap.h |
| dvr / src / irx_imports.h | iomanx / include / iomanX.h |
| dvr / src / irx_imports.h | stdio / include / stdio.h |
| dvr / src / irx_imports.h | sysclib / include / sysclib.h |
| dvr / src / irx_imports.h | threadman / include / thbase.h |
| dvr / src / irx_imports.h | threadman / include / thsemap.h |

---

## PS2SDK: iop/dvrp -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000100_000537.html>

###### dvrp → kernel Relation
| File in iop/dvrp | Includes file in iop/kernel |
| dvrfile / src / irx_imports.h | include / irx.h |
| dvrmisc / src / irx_imports.h | include / irx.h |
| dvripl / src / irx_imports.h | include / irx.h |
| dvrav / src / irx_imports.h | include / irx.h |
| dvrdv / src / irx_imports.h | include / irx.h |
| dvr / src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/dvrp/dvr -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000101_000000.html>

###### dvr → common Relation
| File in iop/dvrp/dvr | Includes file in common |
| src / dvr.c | include / speedregs.h |
| src / dvr.c | include / errno.h |

---

## PS2SDK: iop/dvrp/dvr -&gt; dev9 Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000101_000087.html>

###### dvr → dev9 Relation
| File in iop/dvrp/dvr | Includes file in iop/dev9 |
| src / dvr.c | pvrdrv / include / pvrdrv.h |
| src / irx_imports.h | pvrdrv / include / pvrdrv.h |

---

## PS2SDK: iop/dvrp/dvr -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000101_000223.html>

###### dvr → system Relation
| File in iop/dvrp/dvr | Includes file in iop/system |
| src / dvr.c | iomanx / include / iomanX.h |
| src / dvr.c | loadcore / include / loadcore.h |
| src / dvr.c | stdio / include / stdio.h |
| src / dvr.c | sysclib / include / sysclib.h |
| src / dvr.c | threadman / include / thbase.h |
| src / dvr.c | threadman / include / thsemap.h |
| src / irx_imports.h | iomanx / include / iomanX.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thsemap.h |

---

## PS2SDK: iop/dvrp/dvr -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000101_000537.html>

###### dvr → kernel Relation
| File in iop/dvrp/dvr | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/dvrp/dvr/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000102_000000.html>

###### src → common Relation
| File in iop/dvrp/dvr/src | Includes file in common |
| dvr.c | include / errno.h |
| dvr.c | include / speedregs.h |

---

## PS2SDK: iop/dvrp/dvr/src -&gt; dev9 Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000102_000087.html>

###### src → dev9 Relation
| File in iop/dvrp/dvr/src | Includes file in iop/dev9 |
| dvr.c | pvrdrv / include / pvrdrv.h |
| irx_imports.h | pvrdrv / include / pvrdrv.h |

---

## PS2SDK: iop/dvrp/dvr/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000102_000223.html>

###### src → system Relation
| File in iop/dvrp/dvr/src | Includes file in iop/system |
| dvr.c | iomanx / include / iomanX.h |
| dvr.c | loadcore / include / loadcore.h |
| dvr.c | stdio / include / stdio.h |
| dvr.c | sysclib / include / sysclib.h |
| dvr.c | threadman / include / thbase.h |
| dvr.c | threadman / include / thsemap.h |
| irx_imports.h | iomanx / include / iomanX.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thsemap.h |

---

## PS2SDK: iop/dvrp/dvr/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000102_000537.html>

###### src → kernel Relation
| File in iop/dvrp/dvr/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/dvrp/dvrav -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000103_000000.html>

###### dvrav → common Relation
| File in iop/dvrp/dvrav | Includes file in common |
| src / dvrav.c | include / speedregs.h |
| src / dvrav.c | include / errno.h |

---

## PS2SDK: iop/dvrp/dvrav -&gt; dev9 Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000103_000087.html>

###### dvrav → dev9 Relation
| File in iop/dvrp/dvrav | Includes file in iop/dev9 |
| src / dvrav.c | pvrdrv / include / pvrdrv.h |
| src / irx_imports.h | pvrdrv / include / pvrdrv.h |

---

## PS2SDK: iop/dvrp/dvrav -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000103_000223.html>

###### dvrav → system Relation
| File in iop/dvrp/dvrav | Includes file in iop/system |
| src / dvrav.c | iomanx / include / iomanX.h |
| src / dvrav.c | loadcore / include / loadcore.h |
| src / dvrav.c | stdio / include / stdio.h |
| src / dvrav.c | threadman / include / thbase.h |
| src / dvrav.c | threadman / include / thsemap.h |
| src / irx_imports.h | iomanx / include / iomanX.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thsemap.h |

---

## PS2SDK: iop/dvrp/dvrav -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000103_000537.html>

###### dvrav → kernel Relation
| File in iop/dvrp/dvrav | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/dvrp/dvrav/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000104_000000.html>

###### src → common Relation
| File in iop/dvrp/dvrav/src | Includes file in common |
| dvrav.c | include / errno.h |
| dvrav.c | include / speedregs.h |

---

## PS2SDK: iop/dvrp/dvrav/src -&gt; dev9 Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000104_000087.html>

###### src → dev9 Relation
| File in iop/dvrp/dvrav/src | Includes file in iop/dev9 |
| dvrav.c | pvrdrv / include / pvrdrv.h |
| irx_imports.h | pvrdrv / include / pvrdrv.h |

---

## PS2SDK: iop/dvrp/dvrav/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000104_000223.html>

###### src → system Relation
| File in iop/dvrp/dvrav/src | Includes file in iop/system |
| dvrav.c | iomanx / include / iomanX.h |
| dvrav.c | loadcore / include / loadcore.h |
| dvrav.c | stdio / include / stdio.h |
| dvrav.c | threadman / include / thbase.h |
| dvrav.c | threadman / include / thsemap.h |
| irx_imports.h | iomanx / include / iomanX.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thsemap.h |

---

## PS2SDK: iop/dvrp/dvrav/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000104_000537.html>

###### src → kernel Relation
| File in iop/dvrp/dvrav/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/dvrp/dvrdv -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000105_000000.html>

###### dvrdv → common Relation
| File in iop/dvrp/dvrdv | Includes file in common |
| src / dvrdv.c | include / speedregs.h |
| src / dvrdv.c | include / errno.h |

---

## PS2SDK: iop/dvrp/dvrdv -&gt; dev9 Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000105_000087.html>

###### dvrdv → dev9 Relation
| File in iop/dvrp/dvrdv | Includes file in iop/dev9 |
| src / dvrdv.c | pvrdrv / include / pvrdrv.h |
| src / irx_imports.h | pvrdrv / include / pvrdrv.h |

---

## PS2SDK: iop/dvrp/dvrdv -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000105_000223.html>

###### dvrdv → system Relation
| File in iop/dvrp/dvrdv | Includes file in iop/system |
| src / dvrdv.c | iomanx / include / iomanX.h |
| src / dvrdv.c | loadcore / include / loadcore.h |
| src / dvrdv.c | stdio / include / stdio.h |
| src / dvrdv.c | threadman / include / thbase.h |
| src / dvrdv.c | threadman / include / thsemap.h |
| src / irx_imports.h | iomanx / include / iomanX.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thsemap.h |

---

## PS2SDK: iop/dvrp/dvrdv -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000105_000537.html>

###### dvrdv → kernel Relation
| File in iop/dvrp/dvrdv | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/dvrp/dvrdv/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000106_000000.html>

###### src → common Relation
| File in iop/dvrp/dvrdv/src | Includes file in common |
| dvrdv.c | include / errno.h |
| dvrdv.c | include / speedregs.h |

---

## PS2SDK: iop/dvrp/dvrdv/src -&gt; dev9 Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000106_000087.html>

###### src → dev9 Relation
| File in iop/dvrp/dvrdv/src | Includes file in iop/dev9 |
| dvrdv.c | pvrdrv / include / pvrdrv.h |
| irx_imports.h | pvrdrv / include / pvrdrv.h |

---

## PS2SDK: iop/dvrp/dvrdv/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000106_000223.html>

###### src → system Relation
| File in iop/dvrp/dvrdv/src | Includes file in iop/system |
| dvrdv.c | iomanx / include / iomanX.h |
| dvrdv.c | loadcore / include / loadcore.h |
| dvrdv.c | stdio / include / stdio.h |
| dvrdv.c | threadman / include / thbase.h |
| dvrdv.c | threadman / include / thsemap.h |
| irx_imports.h | iomanx / include / iomanX.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thsemap.h |

---

## PS2SDK: iop/dvrp/dvrdv/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000106_000537.html>

###### src → kernel Relation
| File in iop/dvrp/dvrdv/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/dvrp/dvrfile -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000107_000000.html>

###### dvrfile → common Relation
| File in iop/dvrp/dvrfile | Includes file in common |
| src / dvrfile.c | include / speedregs.h |
| src / dvrfile.c | include / errno.h |

---

## PS2SDK: iop/dvrp/dvrfile -&gt; dev9 Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000107_000087.html>

###### dvrfile → dev9 Relation
| File in iop/dvrp/dvrfile | Includes file in iop/dev9 |
| src / dvrfile.c | pvrdrv / include / pvrdrv.h |
| src / irx_imports.h | pvrdrv / include / pvrdrv.h |

---

## PS2SDK: iop/dvrp/dvrfile -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000107_000223.html>

###### dvrfile → system Relation
| File in iop/dvrp/dvrfile | Includes file in iop/system |
| src / dvrfile.c | iomanx / include / iomanX.h |
| src / dvrfile.c | loadcore / include / loadcore.h |
| src / dvrfile.c | stdio / include / stdio.h |
| src / dvrfile.c | sysclib / include / sysclib.h |
| src / dvrfile.c | threadman / include / thbase.h |
| src / dvrfile.c | threadman / include / thsemap.h |
| src / irx_imports.h | iomanx / include / iomanX.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thsemap.h |

---

## PS2SDK: iop/dvrp/dvrfile -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000107_000537.html>

###### dvrfile → kernel Relation
| File in iop/dvrp/dvrfile | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/dvrp/dvrfile/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000108_000000.html>

###### src → common Relation
| File in iop/dvrp/dvrfile/src | Includes file in common |
| dvrfile.c | include / errno.h |
| dvrfile.c | include / speedregs.h |

---

## PS2SDK: iop/dvrp/dvrfile/src -&gt; dev9 Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000108_000087.html>

###### src → dev9 Relation
| File in iop/dvrp/dvrfile/src | Includes file in iop/dev9 |
| dvrfile.c | pvrdrv / include / pvrdrv.h |
| irx_imports.h | pvrdrv / include / pvrdrv.h |

---

## PS2SDK: iop/dvrp/dvrfile/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000108_000223.html>

###### src → system Relation
| File in iop/dvrp/dvrfile/src | Includes file in iop/system |
| dvrfile.c | iomanx / include / iomanX.h |
| dvrfile.c | loadcore / include / loadcore.h |
| dvrfile.c | stdio / include / stdio.h |
| dvrfile.c | sysclib / include / sysclib.h |
| dvrfile.c | threadman / include / thbase.h |
| dvrfile.c | threadman / include / thsemap.h |
| irx_imports.h | iomanx / include / iomanX.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thsemap.h |

---

## PS2SDK: iop/dvrp/dvrfile/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000108_000537.html>

###### src → kernel Relation
| File in iop/dvrp/dvrfile/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/dvrp/dvripl -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000109_000000.html>

###### dvripl → common Relation
| File in iop/dvrp/dvripl | Includes file in common |
| src / dvripl.c | include / speedregs.h |
| src / dvripl.c | include / errno.h |

---

## PS2SDK: iop/dvrp/dvripl -&gt; dev9 Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000109_000087.html>

###### dvripl → dev9 Relation
| File in iop/dvrp/dvripl | Includes file in iop/dev9 |
| src / dvripl.c | pvrdrv / include / pvrdrv.h |
| src / irx_imports.h | pvrdrv / include / pvrdrv.h |

---

## PS2SDK: iop/dvrp/dvripl -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000109_000223.html>

###### dvripl → system Relation
| File in iop/dvrp/dvripl | Includes file in iop/system |
| src / dvripl.c | iomanx / include / iomanX.h |
| src / dvripl.c | loadcore / include / loadcore.h |
| src / dvripl.c | stdio / include / stdio.h |
| src / dvripl.c | threadman / include / thbase.h |
| src / dvripl.c | threadman / include / thsemap.h |
| src / dvripl.c | timrman / include / timrman.h |
| src / irx_imports.h | iomanx / include / iomanX.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thsemap.h |
| src / irx_imports.h | timrman / include / timrman.h |

---

## PS2SDK: iop/dvrp/dvripl -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000109_000537.html>

###### dvripl → kernel Relation
| File in iop/dvrp/dvripl | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/dvrp/dvripl/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000110_000000.html>

###### src → common Relation
| File in iop/dvrp/dvripl/src | Includes file in common |
| dvripl.c | include / errno.h |
| dvripl.c | include / speedregs.h |

---

## PS2SDK: iop/dvrp/dvripl/src -&gt; dev9 Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000110_000087.html>

###### src → dev9 Relation
| File in iop/dvrp/dvripl/src | Includes file in iop/dev9 |
| dvripl.c | pvrdrv / include / pvrdrv.h |
| irx_imports.h | pvrdrv / include / pvrdrv.h |

---

## PS2SDK: iop/dvrp/dvripl/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000110_000223.html>

###### src → system Relation
| File in iop/dvrp/dvripl/src | Includes file in iop/system |
| dvripl.c | iomanx / include / iomanX.h |
| dvripl.c | loadcore / include / loadcore.h |
| dvripl.c | stdio / include / stdio.h |
| dvripl.c | threadman / include / thbase.h |
| dvripl.c | threadman / include / thsemap.h |
| dvripl.c | timrman / include / timrman.h |
| irx_imports.h | iomanx / include / iomanX.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thsemap.h |
| irx_imports.h | timrman / include / timrman.h |

---

## PS2SDK: iop/dvrp/dvripl/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000110_000537.html>

###### src → kernel Relation
| File in iop/dvrp/dvripl/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/dvrp/dvrmisc -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000111_000000.html>

###### dvrmisc → common Relation
| File in iop/dvrp/dvrmisc | Includes file in common |
| src / dvrmisc.c | include / speedregs.h |
| src / dvrmisc.c | include / errno.h |

---

## PS2SDK: iop/dvrp/dvrmisc -&gt; dev9 Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000111_000087.html>

###### dvrmisc → dev9 Relation
| File in iop/dvrp/dvrmisc | Includes file in iop/dev9 |
| src / dvrmisc.c | pvrdrv / include / pvrdrv.h |
| src / irx_imports.h | pvrdrv / include / pvrdrv.h |

---

## PS2SDK: iop/dvrp/dvrmisc -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000111_000223.html>

###### dvrmisc → system Relation
| File in iop/dvrp/dvrmisc | Includes file in iop/system |
| src / dvrmisc.c | iomanx / include / iomanX.h |
| src / dvrmisc.c | loadcore / include / loadcore.h |
| src / dvrmisc.c | stdio / include / stdio.h |
| src / dvrmisc.c | sysclib / include / sysclib.h |
| src / dvrmisc.c | threadman / include / thbase.h |
| src / dvrmisc.c | threadman / include / thsemap.h |
| src / irx_imports.h | iomanx / include / iomanX.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thsemap.h |

---

## PS2SDK: iop/dvrp/dvrmisc -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000111_000537.html>

###### dvrmisc → kernel Relation
| File in iop/dvrp/dvrmisc | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/dvrp/dvrmisc/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000112_000000.html>

###### src → common Relation
| File in iop/dvrp/dvrmisc/src | Includes file in common |
| dvrmisc.c | include / errno.h |
| dvrmisc.c | include / speedregs.h |

---

## PS2SDK: iop/dvrp/dvrmisc/src -&gt; dev9 Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000112_000087.html>

###### src → dev9 Relation
| File in iop/dvrp/dvrmisc/src | Includes file in iop/dev9 |
| dvrmisc.c | pvrdrv / include / pvrdrv.h |
| irx_imports.h | pvrdrv / include / pvrdrv.h |

---

## PS2SDK: iop/dvrp/dvrmisc/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000112_000223.html>

###### src → system Relation
| File in iop/dvrp/dvrmisc/src | Includes file in iop/system |
| dvrmisc.c | iomanx / include / iomanX.h |
| dvrmisc.c | loadcore / include / loadcore.h |
| dvrmisc.c | stdio / include / stdio.h |
| dvrmisc.c | sysclib / include / sysclib.h |
| dvrmisc.c | threadman / include / thbase.h |
| dvrmisc.c | threadman / include / thsemap.h |
| irx_imports.h | iomanx / include / iomanX.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thsemap.h |

---

## PS2SDK: iop/dvrp/dvrmisc/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000112_000537.html>

###### src → kernel Relation
| File in iop/dvrp/dvrmisc/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/fs -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000113_000000.html>

###### fs → common Relation
| File in iop/fs | Includes file in common |
| libbdm / include / bd_cache.h | include / tamtypes.h |
| libbdm / include / bd_defrag.h | include / tamtypes.h |
| libbdm / include / bd_defrag.h | include / usbhdfsd-common.h |
| devfs / src / devfs.c | include / errno.h |
| eromdrv / src / eromdrv.c | include / errno.h |
| filexio / src / fileXio_iop.c | include / errno.h |
| filexio / src / fileXio_iop.c | include / fileXio.h |
| bdmfs_fatfs / src / fs_driver.c | include / errno.h |
| bdmfs_fatfs / src / fs_driver.c | include / usbhdfsd-common.h |
| bdm / src / part_driver.c | include / errno.h |
| bdm / src / part_driver_gpt.c | include / errno.h |
| bdm / src / part_driver_mbr.c | include / errno.h |
| romdrv / src / romdrv.c | include / errno.h |
| subfile / src / subfile.c | include / errno.h |
| vfat / src / fat_driver.c | include / errno.h |
| vfat / src / fat_write.c | include / errno.h |
| vfat / src / fs_driver.c | include / errno.h |
| vfat / src / fs_driver.c | include / usbhdfsd-common.h |
| vfat / src / part_driver.c | include / errno.h |
| vfat / src / scache.c | include / tamtypes.h |
| fakehost / src / fakehost.c | include / errno.h |
| fileio / src / fileio.c | include / fileio-common.h |
| fileio / src / fileio.c | include / iopheap-common.h |
| netfs / src / ps2_fio.c | include / errno.h |
| http / src / ps2http.c | include / errno.h |

---

## PS2SDK: iop/fs -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000113_000056.html>

###### fs → cdvd Relation
| File in iop/fs | Includes file in iop/cdvd |
| bdmfs_vfat / src / irx_imports.h | cdvdman / include / cdvdman.h |
| bdmfs_fatfs / src / irx_imports.h | cdvdman / include / cdvdman.h |
| bdmfs_fatfs / src / main.c | cdvdman / include / cdvdman.h |
| vfat / src / fat_write.c | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/fs -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000113_000223.html>

###### fs → system Relation
| File in iop/fs | Includes file in iop/system |
| libbdm / src / include / module_debug.h | stdio / include / stdio.h |
| devfs / src / devfs.c | loadcore / include / loadcore.h |
| devfs / src / devfs.c | threadman / include / thbase.h |
| devfs / src / devfs.c | threadman / include / thevent.h |
| devfs / src / devfs.c | threadman / include / thsemap.h |
| devfs / src / devfs.c | intrman / include / intrman.h |
| devfs / src / devfs.c | stdio / include / stdio.h |
| devfs / src / devfs.c | sysclib / include / sysclib.h |
| devfs / src / devfs.c | iomanx / include / iomanX.h |
| devfs / src / irx_imports.h | iomanx / include / iomanX.h |
| devfs / src / irx_imports.h | loadcore / include / loadcore.h |
| devfs / src / irx_imports.h | stdio / include / stdio.h |
| devfs / src / irx_imports.h | sysclib / include / sysclib.h |
| eromdrv / src / eromdrv.c | loadcore / include / loadcore.h |
| eromdrv / src / irx_imports.h | intrman / include / intrman.h |
| eromdrv / src / irx_imports.h | ioman / include / ioman.h |
| eromdrv / src / irx_imports.h | sysclib / include / sysclib.h |
| addrom2 / src / addrom2.c | intrman / include / intrman.h |
| addrom2 / src / addrom2.c | ssbusc / include / ssbusc.h |
| addrom2 / src / addrom2.c | loadcore / include / loadcore.h |
| addrom2 / src / irx_imports.h | intrman / include / intrman.h |
| addrom2 / src / irx_imports.h | ssbusc / include / ssbusc.h |
| bdmfs_vfat / src / irx_imports.h | intrman / include / intrman.h |
| bdmfs_vfat / src / irx_imports.h | ioman / include / ioman.h |
| bdmfs_vfat / src / irx_imports.h | stdio / include / stdio.h |
| bdmfs_vfat / src / irx_imports.h | sysclib / include / sysclib.h |
| bdmfs_vfat / src / irx_imports.h | threadman / include / thsemap.h |
| bdmfs_vfat / src / main.c | intrman / include / intrman.h |
| bdmfs_vfat / src / main.c | loadcore / include / loadcore.h |
| bdmfs_vfat / src / main.c | stdio / include / stdio.h |
| filexio / src / fileXio_iop.c | stdio / include / stdio.h |
| filexio / src / fileXio_iop.c | sysclib / include / sysclib.h |
| filexio / src / fileXio_iop.c | threadman / include / thbase.h |
| filexio / src / fileXio_iop.c | intrman / include / intrman.h |
| filexio / src / fileXio_iop.c | iomanx / include / iomanX.h |
| filexio / src / fileXio_iop.c | loadcore / include / loadcore.h |
| filexio / src / fileXio_iop.c | sifman / include / sifman.h |
| filexio / src / irx_imports.h | intrman / include / intrman.h |
| filexio / src / irx_imports.h | iomanx / include / iomanX.h |
| filexio / src / irx_imports.h | sifman / include / sifman.h |
| filexio / src / irx_imports.h | stdio / include / stdio.h |
| filexio / src / irx_imports.h | sysclib / include / sysclib.h |
| filexio / src / irx_imports.h | threadman / include / thbase.h |
| bdmfs_fatfs / src / fs_driver.c | iomanx / include / iomanX.h |
| bdmfs_fatfs / src / fs_driver.c | stdio / include / stdio.h |
| bdmfs_fatfs / src / fs_driver.c | sysclib / include / sysclib.h |
| bdmfs_fatfs / src / fs_driver.c | threadman / include / thbase.h |
| bdmfs_fatfs / src / fs_driver.c | threadman / include / thsemap.h |
| bdmfs_fatfs / src / irx_imports.h | intrman / include / intrman.h |
| bdmfs_fatfs / src / irx_imports.h | ioman / include / ioman.h |
| bdmfs_fatfs / src / irx_imports.h | stdio / include / stdio.h |
| bdmfs_fatfs / src / irx_imports.h | sysclib / include / sysclib.h |
| bdmfs_fatfs / src / irx_imports.h | threadman / include / thsemap.h |
| bdmfs_fatfs / src / main.c | intrman / include / intrman.h |
| bdmfs_fatfs / src / main.c | loadcore / include / loadcore.h |
| bdmfs_fatfs / src / main.c | stdio / include / stdio.h |
| bdm / src / bdm.c | stdio / include / stdio.h |
| bdm / src / bdm.c | threadman / include / thbase.h |
| bdm / src / bdm.c | threadman / include / thevent.h |
| bdm / src / irx_imports.h | loadcore / include / loadcore.h |
| bdm / src / irx_imports.h | stdio / include / stdio.h |
| bdm / src / irx_imports.h | sysclib / include / sysclib.h |
| bdm / src / irx_imports.h | threadman / include / thbase.h |
| bdm / src / irx_imports.h | threadman / include / thevent.h |
| bdm / src / main.c | loadcore / include / loadcore.h |
| bdm / src / main.c | stdio / include / stdio.h |
| bdm / src / part_driver.c | stdio / include / stdio.h |
| bdm / src / part_driver_gpt.c | stdio / include / stdio.h |
| bdm / src / part_driver_mbr.c | stdio / include / stdio.h |
| romdrv / src / irx_imports.h | intrman / include / intrman.h |
| romdrv / src / irx_imports.h | ioman / include / ioman.h |
| romdrv / src / irx_imports.h | loadcore / include / loadcore.h |
| romdrv / src / irx_imports.h | sysclib / include / sysclib.h |
| romdrv / src / romdrv.c | intrman / include / intrman.h |
| romdrv / src / romdrv.c | ioman / include / ioman.h |
| romdrv / src / romdrv.c | loadcore / include / loadcore.h |
| romdrv / src / romdrv.c | sysclib / include / sysclib.h |
| subfile / src / irx_imports.h | intrman / include / intrman.h |
| subfile / src / irx_imports.h | ioman / include / ioman.h |
| subfile / src / irx_imports.h | sysclib / include / sysclib.h |
| subfile / src / subfile.c | loadcore / include / loadcore.h |
| adddrv / src / adddrv.c | intrman / include / intrman.h |
| adddrv / src / adddrv.c | ssbusc / include / ssbusc.h |
| adddrv / src / adddrv.c | loadcore / include / loadcore.h |
| adddrv / src / irx_imports.h | intrman / include / intrman.h |
| adddrv / src / irx_imports.h | ssbusc / include / ssbusc.h |
| vfat / src / fat_driver.c | stdio / include / stdio.h |
| vfat / src / fat_driver.c | sysclib / include / sysclib.h |
| vfat / src / fat_driver.c | threadman / include / thbase.h |
| vfat / src / fat_write.c | stdio / include / stdio.h |
| vfat / src / fat_write.c | sysclib / include / sysclib.h |
| vfat / src / fs_driver.c | stdio / include / stdio.h |
| vfat / src / fs_driver.c | iomanx / include / iomanX.h |
| vfat / src / fs_driver.c | sysclib / include / sysclib.h |
| vfat / src / fs_driver.c | threadman / include / thsemap.h |
| vfat / src / fs_driver.c | threadman / include / thbase.h |
| vfat / src / part_driver.c | stdio / include / stdio.h |
| vfat / src / scache.c | stdio / include / stdio.h |
| fakehost / src / fakehost.c | loadcore / include / loadcore.h |
| fakehost / src / fakehost.c | stdio / include / stdio.h |
| fakehost / src / fakehost.c | sysclib / include / sysclib.h |
| fakehost / src / fakehost.c | threadman / include / thbase.h |
| fakehost / src / fakehost.c | intrman / include / intrman.h |
| fakehost / src / fakehost.c | sifman / include / sifman.h |
| fakehost / src / fakehost.c | iomanx / include / iomanX.h |
| fakehost / src / fakehost.c | ioman / include / ioman_mod.h |
| fakehost / src / irx_imports.h | iomanx / include / iomanX.h |
| fakehost / src / irx_imports.h | ioman / include / ioman_mod.h |
| fakehost / src / irx_imports.h | loadcore / include / loadcore.h |
| fakehost / src / irx_imports.h | stdio / include / stdio.h |
| fakehost / src / irx_imports.h | sysclib / include / sysclib.h |
| fakehost / src / irx_imports.h | threadman / include / thbase.h |
| fakehost / src / nprintf.c | stdio / include / stdio.h |
| fakehost / src / nprintf.c | sysclib / include / sysclib.h |
| fakehost / src / nprintf.c | threadman / include / thbase.h |
| fakehost / src / nprintf.c | intrman / include / intrman.h |
| fakehost / src / nprintf.c | sifman / include / sifman.h |
| fileio / src / irx_imports.h | intrman / include / intrman.h |
| fileio / src / irx_imports.h | ioman / include / ioman_mod.h |
| fileio / src / irx_imports.h | loadcore / include / loadcore.h |
| fileio / src / irx_imports.h | sifman / include / sifman.h |
| fileio / src / irx_imports.h | stdio / include / stdio.h |
| fileio / src / irx_imports.h | threadman / include / thbase.h |
| netfs / src / devscan.c | loadcore / include / loadcore.h |
| netfs / src / devscan.c | ioman / include / ioman_mod.h |
| netfs / src / devscan.c | iomanx / include / iomanX.h |
| netfs / src / devscan.c | threadman / include / thbase.h |
| netfs / src / devscan.c | threadman / include / thsemap.h |
| netfs / src / devscan.c | stdio / include / stdio.h |
| netfs / src / devscan.c | sysclib / include / sysclib.h |
| netfs / src / devscan.c | iopmgr / include / iopmgr.h |
| netfs / src / irx_imports.h | ioman / include / ioman_mod.h |
| netfs / src / irx_imports.h | iomanx / include / iomanX.h |
| netfs / src / irx_imports.h | loadcore / include / loadcore.h |
| netfs / src / irx_imports.h | stdio / include / stdio.h |
| netfs / src / irx_imports.h | sysclib / include / sysclib.h |
| netfs / src / irx_imports.h | threadman / include / thbase.h |
| netfs / src / irx_imports.h | threadman / include / thsemap.h |
| netfs / src / ps2_fio.c | loadcore / include / loadcore.h |
| netfs / src / ps2_fio.c | ioman / include / ioman_mod.h |
| netfs / src / ps2_fio.c | iomanx / include / iomanX.h |
| netfs / src / ps2_fio.c | threadman / include / thbase.h |
| netfs / src / ps2_fio.c | threadman / include / thsemap.h |
| netfs / src / ps2_fio.c | stdio / include / stdio.h |
| netfs / src / ps2_fio.c | sysclib / include / sysclib.h |
| netfs / src / ps2_fio.c | iopmgr / include / iopmgr.h |
| netfs / src / ps2netfs.c | loadcore / include / loadcore.h |
| netfs / src / ps2netfs.c | ioman / include / ioman.h |
| netfs / src / ps2netfs.c | stdio / include / stdio.h |
| netfs / src / ps2netfs.c | iopmgr / include / iopmgr.h |
| http / src / irx_imports.h | intrman / include / intrman.h |
| http / src / irx_imports.h | iomanx / include / iomanX.h |
| http / src / irx_imports.h | sifman / include / sifman.h |
| http / src / irx_imports.h | stdio / include / stdio.h |
| http / src / irx_imports.h | sysclib / include / sysclib.h |
| http / src / irx_imports.h | threadman / include / thbase.h |
| http / src / irx_imports.h | ioman / include / ioman_mod.h |
| http / src / ps2http.c | loadcore / include / loadcore.h |
| http / src / ps2http.c | stdio / include / stdio.h |
| http / src / ps2http.c | threadman / include / thbase.h |
| http / src / ps2http.c | sysclib / include / sysclib.h |
| http / src / ps2http.c | ioman / include / ioman_mod.h |
| http / src / ps2http.c | ioman / include / ioman.h |
| libbdm / tests / test_bd_cache.c | stdio / include / stdio.h |

---

## PS2SDK: iop/fs -&gt; tcpip Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000113_000284.html>

###### fs → tcpip Relation
| File in iop/fs | Includes file in iop/tcpip |
| libbdm / tests / include / sysmem.h | tcpip-base / include / stdlib.h |

---

## PS2SDK: iop/fs -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000113_000537.html>

###### fs → kernel Relation
| File in iop/fs | Includes file in iop/kernel |
| devfs / include / devfs.h | include / irx.h |
| bdm / include / bdm.h | include / irx.h |
| devfs / src / devfs.c | include / defs.h |
| devfs / src / devfs.c | include / irx.h |
| devfs / src / irx_imports.h | include / irx.h |
| eromdrv / src / irx_imports.h | include / irx.h |
| addrom2 / src / irx_imports.h | include / irx.h |
| bdmfs_vfat / src / irx_imports.h | include / irx.h |
| bdmfs_vfat / src / main.c | include / irx.h |
| filexio / src / irx_imports.h | include / irx.h |
| bdmfs_fatfs / src / irx_imports.h | include / irx.h |
| bdmfs_fatfs / src / main.c | include / irx.h |
| bdm / src / irx_imports.h | include / irx.h |
| bdm / src / main.c | include / irx.h |
| romdrv / src / irx_imports.h | include / irx.h |
| romdrv / src / romdrv.c | include / irx.h |
| subfile / src / irx_imports.h | include / irx.h |
| adddrv / src / irx_imports.h | include / irx.h |
| fakehost / src / irx_imports.h | include / irx.h |
| fileio / src / irx_imports.h | include / irx.h |
| netfs / src / devscan.c | include / defs.h |
| netfs / src / devscan.c | include / irx.h |
| netfs / src / irx_imports.h | include / irx.h |
| netfs / src / ps2_fio.c | include / defs.h |
| netfs / src / ps2_fio.c | include / irx.h |
| netfs / src / ps2netfs.c | include / defs.h |
| netfs / src / ps2netfs.c | include / irx.h |
| http / src / irx_imports.h | include / irx.h |
| http / src / ps2http.c | include / irx.h |

---

## PS2SDK: iop/fs/adddrv -&gt; romdrv Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000114_000138.html>

###### adddrv → romdrv Relation
| File in iop/fs/adddrv | Includes file in iop/fs/romdrv |
| src / adddrv.c | include / romdrv.h |
| src / irx_imports.h | include / romdrv.h |

---

## PS2SDK: iop/fs/adddrv -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000114_000223.html>

###### adddrv → system Relation
| File in iop/fs/adddrv | Includes file in iop/system |
| src / adddrv.c | intrman / include / intrman.h |
| src / adddrv.c | ssbusc / include / ssbusc.h |
| src / adddrv.c | loadcore / include / loadcore.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | ssbusc / include / ssbusc.h |

---

## PS2SDK: iop/fs/adddrv -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000114_000537.html>

###### adddrv → kernel Relation
| File in iop/fs/adddrv | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/fs/adddrv/src -&gt; romdrv Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000115_000138.html>

###### src → romdrv Relation
| File in iop/fs/adddrv/src | Includes file in iop/fs/romdrv |
| adddrv.c | include / romdrv.h |
| irx_imports.h | include / romdrv.h |

---

## PS2SDK: iop/fs/adddrv/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000115_000223.html>

###### src → system Relation
| File in iop/fs/adddrv/src | Includes file in iop/system |
| adddrv.c | intrman / include / intrman.h |
| adddrv.c | loadcore / include / loadcore.h |
| adddrv.c | ssbusc / include / ssbusc.h |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | ssbusc / include / ssbusc.h |

---

## PS2SDK: iop/fs/adddrv/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000115_000537.html>

###### src → kernel Relation
| File in iop/fs/adddrv/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/fs/addrom2 -&gt; romdrv Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000116_000138.html>

###### addrom2 → romdrv Relation
| File in iop/fs/addrom2 | Includes file in iop/fs/romdrv |
| src / addrom2.c | include / romdrv.h |
| src / irx_imports.h | include / romdrv.h |

---

## PS2SDK: iop/fs/addrom2 -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000116_000223.html>

###### addrom2 → system Relation
| File in iop/fs/addrom2 | Includes file in iop/system |
| src / addrom2.c | intrman / include / intrman.h |
| src / addrom2.c | ssbusc / include / ssbusc.h |
| src / addrom2.c | loadcore / include / loadcore.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | ssbusc / include / ssbusc.h |

---

## PS2SDK: iop/fs/addrom2 -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000116_000537.html>

###### addrom2 → kernel Relation
| File in iop/fs/addrom2 | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/fs/addrom2/src -&gt; romdrv Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000117_000138.html>

###### src → romdrv Relation
| File in iop/fs/addrom2/src | Includes file in iop/fs/romdrv |
| addrom2.c | include / romdrv.h |
| irx_imports.h | include / romdrv.h |

---

## PS2SDK: iop/fs/addrom2/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000117_000223.html>

###### src → system Relation
| File in iop/fs/addrom2/src | Includes file in iop/system |
| addrom2.c | intrman / include / intrman.h |
| addrom2.c | loadcore / include / loadcore.h |
| addrom2.c | ssbusc / include / ssbusc.h |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | ssbusc / include / ssbusc.h |

---

## PS2SDK: iop/fs/addrom2/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000117_000537.html>

###### src → kernel Relation
| File in iop/fs/addrom2/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/fs/bdm -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000118_000000.html>

###### bdm → common Relation
| File in iop/fs/bdm | Includes file in common |
| src / part_driver.c | include / errno.h |
| src / part_driver_gpt.c | include / errno.h |
| src / part_driver_mbr.c | include / errno.h |

---

## PS2SDK: iop/fs/bdm -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000118_000223.html>

###### bdm → system Relation
| File in iop/fs/bdm | Includes file in iop/system |
| src / bdm.c | stdio / include / stdio.h |
| src / bdm.c | threadman / include / thbase.h |
| src / bdm.c | threadman / include / thevent.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thevent.h |
| src / main.c | loadcore / include / loadcore.h |
| src / main.c | stdio / include / stdio.h |
| src / part_driver.c | stdio / include / stdio.h |
| src / part_driver_gpt.c | stdio / include / stdio.h |
| src / part_driver_mbr.c | stdio / include / stdio.h |

---

## PS2SDK: iop/fs/bdm -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000118_000537.html>

###### bdm → kernel Relation
| File in iop/fs/bdm | Includes file in iop/kernel |
| include / bdm.h | include / irx.h |
| src / irx_imports.h | include / irx.h |
| src / main.c | include / irx.h |

---

## PS2SDK: iop/fs/bdm/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000119_000000.html>

###### src → common Relation
| File in iop/fs/bdm/src | Includes file in common |
| part_driver.c | include / errno.h |
| part_driver_gpt.c | include / errno.h |
| part_driver_mbr.c | include / errno.h |

---

## PS2SDK: iop/fs/bdm/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000119_000223.html>

###### src → system Relation
| File in iop/fs/bdm/src | Includes file in iop/system |
| bdm.c | stdio / include / stdio.h |
| bdm.c | threadman / include / thbase.h |
| bdm.c | threadman / include / thevent.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thevent.h |
| main.c | loadcore / include / loadcore.h |
| main.c | stdio / include / stdio.h |
| part_driver.c | stdio / include / stdio.h |
| part_driver_gpt.c | stdio / include / stdio.h |
| part_driver_mbr.c | stdio / include / stdio.h |

---

## PS2SDK: iop/fs/bdm/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000119_000508.html>

###### src → include Relation
| File in iop/fs/bdm/src | Includes file in iop/fs/bdm/include |
| bdm.c | bdm.h |
| irx_imports.h | bdm.h |
| main.c | bdm.h |
| part_driver.c | bdm.h |
| include / part_driver.h | bdm.h |
| part_driver_gpt.c | bdm.h |
| part_driver_mbr.c | bdm.h |

---

## PS2SDK: iop/fs/bdm/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000119_000509.html>

###### src → include Relation
| File in iop/fs/bdm/src | Includes file in iop/fs/bdm/src/include |
| part_driver.c | gpt_types.h |
| part_driver.c | mbr_types.h |
| part_driver_gpt.c | gpt_types.h |
| part_driver_mbr.c | mbr_types.h |

---

## PS2SDK: iop/fs/bdm/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000119_000537.html>

###### src → kernel Relation
| File in iop/fs/bdm/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |
| main.c | include / irx.h |

---

## PS2SDK: iop/fs/bdmfs_fatfs -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000120_000000.html>

###### bdmfs_fatfs → common Relation
| File in iop/fs/bdmfs_fatfs | Includes file in common |
| src / fs_driver.c | include / errno.h |
| src / fs_driver.c | include / usbhdfsd-common.h |

---

## PS2SDK: iop/fs/bdmfs_fatfs -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000120_000056.html>

###### bdmfs_fatfs → cdvd Relation
| File in iop/fs/bdmfs_fatfs | Includes file in iop/cdvd |
| src / irx_imports.h | cdvdman / include / cdvdman.h |
| src / main.c | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/fs/bdmfs_fatfs -&gt; bdm Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000120_000118.html>

###### bdmfs_fatfs → bdm Relation
| File in iop/fs/bdmfs_fatfs | Includes file in iop/fs/bdm |
| src / include / fs_driver.h | include / bdm.h |
| src / fs_driver.c | include / bdm.h |
| src / irx_imports.h | include / bdm.h |
| src / main.c | include / bdm.h |

---

## PS2SDK: iop/fs/bdmfs_fatfs -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000120_000223.html>

###### bdmfs_fatfs → system Relation
| File in iop/fs/bdmfs_fatfs | Includes file in iop/system |
| src / fs_driver.c | iomanx / include / iomanX.h |
| src / fs_driver.c | stdio / include / stdio.h |
| src / fs_driver.c | sysclib / include / sysclib.h |
| src / fs_driver.c | threadman / include / thbase.h |
| src / fs_driver.c | threadman / include / thsemap.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | ioman / include / ioman.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thsemap.h |
| src / main.c | intrman / include / intrman.h |
| src / main.c | loadcore / include / loadcore.h |
| src / main.c | stdio / include / stdio.h |

---

## PS2SDK: iop/fs/bdmfs_fatfs -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000120_000537.html>

###### bdmfs_fatfs → kernel Relation
| File in iop/fs/bdmfs_fatfs | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |
| src / main.c | include / irx.h |

---

## PS2SDK: iop/fs/bdmfs_fatfs/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000121_000000.html>

###### src → common Relation
| File in iop/fs/bdmfs_fatfs/src | Includes file in common |
| fs_driver.c | include / errno.h |
| fs_driver.c | include / usbhdfsd-common.h |

---

## PS2SDK: iop/fs/bdmfs_fatfs/src -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000121_000056.html>

###### src → cdvd Relation
| File in iop/fs/bdmfs_fatfs/src | Includes file in iop/cdvd |
| irx_imports.h | cdvdman / include / cdvdman.h |
| main.c | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/fs/bdmfs_fatfs/src -&gt; bdm Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000121_000118.html>

###### src → bdm Relation
| File in iop/fs/bdmfs_fatfs/src | Includes file in iop/fs/bdm |
| fs_driver.c | include / bdm.h |
| include / fs_driver.h | include / bdm.h |
| irx_imports.h | include / bdm.h |
| main.c | include / bdm.h |

---

## PS2SDK: iop/fs/bdmfs_fatfs/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000121_000223.html>

###### src → system Relation
| File in iop/fs/bdmfs_fatfs/src | Includes file in iop/system |
| fs_driver.c | iomanx / include / iomanX.h |
| fs_driver.c | stdio / include / stdio.h |
| fs_driver.c | sysclib / include / sysclib.h |
| fs_driver.c | threadman / include / thbase.h |
| fs_driver.c | threadman / include / thsemap.h |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | ioman / include / ioman.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thsemap.h |
| main.c | intrman / include / intrman.h |
| main.c | loadcore / include / loadcore.h |
| main.c | stdio / include / stdio.h |

---

## PS2SDK: iop/fs/bdmfs_fatfs/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000121_000537.html>

###### src → kernel Relation
| File in iop/fs/bdmfs_fatfs/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |
| main.c | include / irx.h |

---

## PS2SDK: iop/fs/bdmfs_vfat -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000122_000056.html>

###### bdmfs_vfat → cdvd Relation
| File in iop/fs/bdmfs_vfat | Includes file in iop/cdvd |
| src / irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/fs/bdmfs_vfat -&gt; bdm Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000122_000118.html>

###### bdmfs_vfat → bdm Relation
| File in iop/fs/bdmfs_vfat | Includes file in iop/fs/bdm |
| src / irx_imports.h | include / bdm.h |
| src / main.c | include / bdm.h |

---

## PS2SDK: iop/fs/bdmfs_vfat -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000122_000223.html>

###### bdmfs_vfat → system Relation
| File in iop/fs/bdmfs_vfat | Includes file in iop/system |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | ioman / include / ioman.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thsemap.h |
| src / main.c | intrman / include / intrman.h |
| src / main.c | loadcore / include / loadcore.h |
| src / main.c | stdio / include / stdio.h |

---

## PS2SDK: iop/fs/bdmfs_vfat -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000122_000537.html>

###### bdmfs_vfat → kernel Relation
| File in iop/fs/bdmfs_vfat | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |
| src / main.c | include / irx.h |

---

## PS2SDK: iop/fs/bdmfs_vfat/src -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000123_000056.html>

###### src → cdvd Relation
| File in iop/fs/bdmfs_vfat/src | Includes file in iop/cdvd |
| irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/fs/bdmfs_vfat/src -&gt; bdm Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000123_000118.html>

###### src → bdm Relation
| File in iop/fs/bdmfs_vfat/src | Includes file in iop/fs/bdm |
| irx_imports.h | include / bdm.h |
| main.c | include / bdm.h |

---

## PS2SDK: iop/fs/bdmfs_vfat/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000123_000223.html>

###### src → system Relation
| File in iop/fs/bdmfs_vfat/src | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | ioman / include / ioman.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thsemap.h |
| main.c | intrman / include / intrman.h |
| main.c | loadcore / include / loadcore.h |
| main.c | stdio / include / stdio.h |

---

## PS2SDK: iop/fs/bdmfs_vfat/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000123_000537.html>

###### src → kernel Relation
| File in iop/fs/bdmfs_vfat/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |
| main.c | include / irx.h |

---

## PS2SDK: iop/fs/devfs -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000124_000000.html>

###### devfs → common Relation
| File in iop/fs/devfs | Includes file in common |
| src / devfs.c | include / errno.h |

---

## PS2SDK: iop/fs/devfs -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000124_000223.html>

###### devfs → system Relation
| File in iop/fs/devfs | Includes file in iop/system |
| src / devfs.c | loadcore / include / loadcore.h |
| src / devfs.c | threadman / include / thbase.h |
| src / devfs.c | threadman / include / thevent.h |
| src / devfs.c | threadman / include / thsemap.h |
| src / devfs.c | intrman / include / intrman.h |
| src / devfs.c | stdio / include / stdio.h |
| src / devfs.c | sysclib / include / sysclib.h |
| src / devfs.c | iomanx / include / iomanX.h |
| src / irx_imports.h | iomanx / include / iomanX.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |

---

## PS2SDK: iop/fs/devfs -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000124_000537.html>

###### devfs → kernel Relation
| File in iop/fs/devfs | Includes file in iop/kernel |
| include / devfs.h | include / irx.h |
| src / devfs.c | include / defs.h |
| src / devfs.c | include / irx.h |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/fs/devfs/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000125_000000.html>

###### src → common Relation
| File in iop/fs/devfs/src | Includes file in common |
| devfs.c | include / errno.h |

---

## PS2SDK: iop/fs/devfs/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000125_000223.html>

###### src → system Relation
| File in iop/fs/devfs/src | Includes file in iop/system |
| devfs.c | intrman / include / intrman.h |
| devfs.c | iomanx / include / iomanX.h |
| devfs.c | loadcore / include / loadcore.h |
| devfs.c | stdio / include / stdio.h |
| devfs.c | sysclib / include / sysclib.h |
| devfs.c | threadman / include / thbase.h |
| devfs.c | threadman / include / thevent.h |
| devfs.c | threadman / include / thsemap.h |
| irx_imports.h | iomanx / include / iomanX.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |

---

## PS2SDK: iop/fs/devfs/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000125_000521.html>

###### src → include Relation
| File in iop/fs/devfs/src | Includes file in iop/fs/devfs/include |
| devfs.c | devfs.h |

---

## PS2SDK: iop/fs/devfs/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000125_000537.html>

###### src → kernel Relation
| File in iop/fs/devfs/src | Includes file in iop/kernel |
| devfs.c | include / defs.h |
| devfs.c | include / irx.h |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/fs/eromdrv -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000126_000000.html>

###### eromdrv → common Relation
| File in iop/fs/eromdrv | Includes file in common |
| src / eromdrv.c | include / errno.h |

---

## PS2SDK: iop/fs/eromdrv -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000126_000223.html>

###### eromdrv → system Relation
| File in iop/fs/eromdrv | Includes file in iop/system |
| src / eromdrv.c | loadcore / include / loadcore.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | ioman / include / ioman.h |
| src / irx_imports.h | sysclib / include / sysclib.h |

---

## PS2SDK: iop/fs/eromdrv -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000126_000537.html>

###### eromdrv → kernel Relation
| File in iop/fs/eromdrv | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/fs/eromdrv/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000127_000000.html>

###### src → common Relation
| File in iop/fs/eromdrv/src | Includes file in common |
| eromdrv.c | include / errno.h |

---

## PS2SDK: iop/fs/eromdrv/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000127_000223.html>

###### src → system Relation
| File in iop/fs/eromdrv/src | Includes file in iop/system |
| eromdrv.c | loadcore / include / loadcore.h |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | ioman / include / ioman.h |
| irx_imports.h | sysclib / include / sysclib.h |

---

## PS2SDK: iop/fs/eromdrv/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000127_000537.html>

###### src → kernel Relation
| File in iop/fs/eromdrv/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/fs/fakehost -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000128_000000.html>

###### fakehost → common Relation
| File in iop/fs/fakehost | Includes file in common |
| src / fakehost.c | include / errno.h |

---

## PS2SDK: iop/fs/fakehost -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000128_000223.html>

###### fakehost → system Relation
| File in iop/fs/fakehost | Includes file in iop/system |
| src / fakehost.c | loadcore / include / loadcore.h |
| src / fakehost.c | stdio / include / stdio.h |
| src / fakehost.c | sysclib / include / sysclib.h |
| src / fakehost.c | threadman / include / thbase.h |
| src / fakehost.c | intrman / include / intrman.h |
| src / fakehost.c | sifman / include / sifman.h |
| src / fakehost.c | iomanx / include / iomanX.h |
| src / fakehost.c | ioman / include / ioman_mod.h |
| src / irx_imports.h | iomanx / include / iomanX.h |
| src / irx_imports.h | ioman / include / ioman_mod.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / nprintf.c | stdio / include / stdio.h |
| src / nprintf.c | sysclib / include / sysclib.h |
| src / nprintf.c | threadman / include / thbase.h |
| src / nprintf.c | intrman / include / intrman.h |
| src / nprintf.c | sifman / include / sifman.h |

---

## PS2SDK: iop/fs/fakehost -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000128_000537.html>

###### fakehost → kernel Relation
| File in iop/fs/fakehost | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/fs/fakehost/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000129_000000.html>

###### src → common Relation
| File in iop/fs/fakehost/src | Includes file in common |
| fakehost.c | include / errno.h |

---

## PS2SDK: iop/fs/fakehost/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000129_000223.html>

###### src → system Relation
| File in iop/fs/fakehost/src | Includes file in iop/system |
| fakehost.c | intrman / include / intrman.h |
| fakehost.c | ioman / include / ioman_mod.h |
| fakehost.c | iomanx / include / iomanX.h |
| fakehost.c | loadcore / include / loadcore.h |
| fakehost.c | sifman / include / sifman.h |
| fakehost.c | stdio / include / stdio.h |
| fakehost.c | sysclib / include / sysclib.h |
| fakehost.c | threadman / include / thbase.h |
| irx_imports.h | ioman / include / ioman_mod.h |
| irx_imports.h | iomanx / include / iomanX.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| nprintf.c | intrman / include / intrman.h |
| nprintf.c | sifman / include / sifman.h |
| nprintf.c | stdio / include / stdio.h |
| nprintf.c | sysclib / include / sysclib.h |
| nprintf.c | threadman / include / thbase.h |

---

## PS2SDK: iop/fs/fakehost/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000129_000537.html>

###### src → kernel Relation
| File in iop/fs/fakehost/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/fs/fileio -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000130_000000.html>

###### fileio → common Relation
| File in iop/fs/fileio | Includes file in common |
| src / fileio.c | include / fileio-common.h |
| src / fileio.c | include / iopheap-common.h |

---

## PS2SDK: iop/fs/fileio -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000130_000223.html>

###### fileio → system Relation
| File in iop/fs/fileio | Includes file in iop/system |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | ioman / include / ioman_mod.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | sifman / include / sifman.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | threadman / include / thbase.h |

---

## PS2SDK: iop/fs/fileio -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000130_000537.html>

###### fileio → kernel Relation
| File in iop/fs/fileio | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/fs/fileio/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000131_000000.html>

###### src → common Relation
| File in iop/fs/fileio/src | Includes file in common |
| fileio.c | include / fileio-common.h |
| fileio.c | include / iopheap-common.h |

---

## PS2SDK: iop/fs/fileio/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000131_000223.html>

###### src → system Relation
| File in iop/fs/fileio/src | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | ioman / include / ioman_mod.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | sifman / include / sifman.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | threadman / include / thbase.h |

---

## PS2SDK: iop/fs/fileio/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000131_000537.html>

###### src → kernel Relation
| File in iop/fs/fileio/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/fs/filexio -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000132_000000.html>

###### filexio → common Relation
| File in iop/fs/filexio | Includes file in common |
| src / fileXio_iop.c | include / errno.h |
| src / fileXio_iop.c | include / fileXio.h |

---

## PS2SDK: iop/fs/filexio -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000132_000223.html>

###### filexio → system Relation
| File in iop/fs/filexio | Includes file in iop/system |
| src / fileXio_iop.c | stdio / include / stdio.h |
| src / fileXio_iop.c | sysclib / include / sysclib.h |
| src / fileXio_iop.c | threadman / include / thbase.h |
| src / fileXio_iop.c | intrman / include / intrman.h |
| src / fileXio_iop.c | iomanx / include / iomanX.h |
| src / fileXio_iop.c | loadcore / include / loadcore.h |
| src / fileXio_iop.c | sifman / include / sifman.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | iomanx / include / iomanX.h |
| src / irx_imports.h | sifman / include / sifman.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |

---

## PS2SDK: iop/fs/filexio -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000132_000537.html>

###### filexio → kernel Relation
| File in iop/fs/filexio | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/fs/filexio/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000133_000000.html>

###### src → common Relation
| File in iop/fs/filexio/src | Includes file in common |
| fileXio_iop.c | include / errno.h |
| fileXio_iop.c | include / fileXio.h |

---

## PS2SDK: iop/fs/filexio/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000133_000223.html>

###### src → system Relation
| File in iop/fs/filexio/src | Includes file in iop/system |
| fileXio_iop.c | intrman / include / intrman.h |
| fileXio_iop.c | iomanx / include / iomanX.h |
| fileXio_iop.c | loadcore / include / loadcore.h |
| fileXio_iop.c | sifman / include / sifman.h |
| fileXio_iop.c | stdio / include / stdio.h |
| fileXio_iop.c | sysclib / include / sysclib.h |
| fileXio_iop.c | threadman / include / thbase.h |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | iomanx / include / iomanX.h |
| irx_imports.h | sifman / include / sifman.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |

---

## PS2SDK: iop/fs/filexio/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000133_000537.html>

###### src → kernel Relation
| File in iop/fs/filexio/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/fs/http -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000134_000000.html>

###### http → common Relation
| File in iop/fs/http | Includes file in common |
| src / ps2http.c | include / errno.h |

---

## PS2SDK: iop/fs/http -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000134_000223.html>

###### http → system Relation
| File in iop/fs/http | Includes file in iop/system |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | iomanx / include / iomanX.h |
| src / irx_imports.h | sifman / include / sifman.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | ioman / include / ioman_mod.h |
| src / ps2http.c | loadcore / include / loadcore.h |
| src / ps2http.c | stdio / include / stdio.h |
| src / ps2http.c | threadman / include / thbase.h |
| src / ps2http.c | sysclib / include / sysclib.h |
| src / ps2http.c | ioman / include / ioman_mod.h |
| src / ps2http.c | ioman / include / ioman.h |

---

## PS2SDK: iop/fs/http -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000134_000537.html>

###### http → kernel Relation
| File in iop/fs/http | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |
| src / ps2http.c | include / irx.h |

---

## PS2SDK: iop/fs/http/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000135_000000.html>

###### src → common Relation
| File in iop/fs/http/src | Includes file in common |
| ps2http.c | include / errno.h |

---

## PS2SDK: iop/fs/http/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000135_000223.html>

###### src → system Relation
| File in iop/fs/http/src | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | ioman / include / ioman_mod.h |
| irx_imports.h | iomanx / include / iomanX.h |
| irx_imports.h | sifman / include / sifman.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| ps2http.c | ioman / include / ioman.h |
| ps2http.c | ioman / include / ioman_mod.h |
| ps2http.c | loadcore / include / loadcore.h |
| ps2http.c | stdio / include / stdio.h |
| ps2http.c | sysclib / include / sysclib.h |
| ps2http.c | threadman / include / thbase.h |

---

## PS2SDK: iop/fs/http/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000135_000537.html>

###### src → kernel Relation
| File in iop/fs/http/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |
| ps2http.c | include / irx.h |

---

## PS2SDK: iop/fs/netfs -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000136_000000.html>

###### netfs → common Relation
| File in iop/fs/netfs | Includes file in common |
| src / ps2_fio.c | include / errno.h |

---

## PS2SDK: iop/fs/netfs -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000136_000223.html>

###### netfs → system Relation
| File in iop/fs/netfs | Includes file in iop/system |
| src / devscan.c | loadcore / include / loadcore.h |
| src / devscan.c | ioman / include / ioman_mod.h |
| src / devscan.c | iomanx / include / iomanX.h |
| src / devscan.c | threadman / include / thbase.h |
| src / devscan.c | threadman / include / thsemap.h |
| src / devscan.c | stdio / include / stdio.h |
| src / devscan.c | sysclib / include / sysclib.h |
| src / devscan.c | iopmgr / include / iopmgr.h |
| src / irx_imports.h | ioman / include / ioman_mod.h |
| src / irx_imports.h | iomanx / include / iomanX.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thsemap.h |
| src / ps2_fio.c | loadcore / include / loadcore.h |
| src / ps2_fio.c | ioman / include / ioman_mod.h |
| src / ps2_fio.c | iomanx / include / iomanX.h |
| src / ps2_fio.c | threadman / include / thbase.h |
| src / ps2_fio.c | threadman / include / thsemap.h |
| src / ps2_fio.c | stdio / include / stdio.h |
| src / ps2_fio.c | sysclib / include / sysclib.h |
| src / ps2_fio.c | iopmgr / include / iopmgr.h |
| src / ps2netfs.c | loadcore / include / loadcore.h |
| src / ps2netfs.c | ioman / include / ioman.h |
| src / ps2netfs.c | stdio / include / stdio.h |
| src / ps2netfs.c | iopmgr / include / iopmgr.h |

---

## PS2SDK: iop/fs/netfs -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000136_000537.html>

###### netfs → kernel Relation
| File in iop/fs/netfs | Includes file in iop/kernel |
| src / devscan.c | include / defs.h |
| src / devscan.c | include / irx.h |
| src / irx_imports.h | include / irx.h |
| src / ps2_fio.c | include / defs.h |
| src / ps2_fio.c | include / irx.h |
| src / ps2netfs.c | include / defs.h |
| src / ps2netfs.c | include / irx.h |

---

## PS2SDK: iop/fs/netfs/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000137_000000.html>

###### src → common Relation
| File in iop/fs/netfs/src | Includes file in common |
| ps2_fio.c | include / errno.h |

---

## PS2SDK: iop/fs/netfs/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000137_000223.html>

###### src → system Relation
| File in iop/fs/netfs/src | Includes file in iop/system |
| devscan.c | ioman / include / ioman_mod.h |
| devscan.c | iomanx / include / iomanX.h |
| devscan.c | iopmgr / include / iopmgr.h |
| devscan.c | loadcore / include / loadcore.h |
| devscan.c | stdio / include / stdio.h |
| devscan.c | sysclib / include / sysclib.h |
| devscan.c | threadman / include / thbase.h |
| devscan.c | threadman / include / thsemap.h |
| irx_imports.h | ioman / include / ioman_mod.h |
| irx_imports.h | iomanx / include / iomanX.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thsemap.h |
| ps2_fio.c | ioman / include / ioman_mod.h |
| ps2_fio.c | iomanx / include / iomanX.h |
| ps2_fio.c | iopmgr / include / iopmgr.h |
| ps2_fio.c | loadcore / include / loadcore.h |
| ps2_fio.c | stdio / include / stdio.h |
| ps2_fio.c | sysclib / include / sysclib.h |
| ps2_fio.c | threadman / include / thbase.h |
| ps2_fio.c | threadman / include / thsemap.h |
| ps2netfs.c | ioman / include / ioman.h |
| ps2netfs.c | iopmgr / include / iopmgr.h |
| ps2netfs.c | loadcore / include / loadcore.h |
| ps2netfs.c | stdio / include / stdio.h |

---

## PS2SDK: iop/fs/netfs/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000137_000537.html>

###### src → kernel Relation
| File in iop/fs/netfs/src | Includes file in iop/kernel |
| devscan.c | include / defs.h |
| devscan.c | include / irx.h |
| irx_imports.h | include / irx.h |
| ps2_fio.c | include / defs.h |
| ps2_fio.c | include / irx.h |
| ps2netfs.c | include / defs.h |
| ps2netfs.c | include / irx.h |

---

## PS2SDK: iop/fs/romdrv -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000138_000000.html>

###### romdrv → common Relation
| File in iop/fs/romdrv | Includes file in common |
| src / romdrv.c | include / errno.h |

---

## PS2SDK: iop/fs/romdrv -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000138_000223.html>

###### romdrv → system Relation
| File in iop/fs/romdrv | Includes file in iop/system |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | ioman / include / ioman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / romdrv.c | intrman / include / intrman.h |
| src / romdrv.c | ioman / include / ioman.h |
| src / romdrv.c | loadcore / include / loadcore.h |
| src / romdrv.c | sysclib / include / sysclib.h |

---

## PS2SDK: iop/fs/romdrv -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000138_000537.html>

###### romdrv → kernel Relation
| File in iop/fs/romdrv | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |
| src / romdrv.c | include / irx.h |

---

## PS2SDK: iop/fs/romdrv/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000139_000000.html>

###### src → common Relation
| File in iop/fs/romdrv/src | Includes file in common |
| romdrv.c | include / errno.h |

---

## PS2SDK: iop/fs/romdrv/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000139_000223.html>

###### src → system Relation
| File in iop/fs/romdrv/src | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | ioman / include / ioman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | sysclib / include / sysclib.h |
| romdrv.c | intrman / include / intrman.h |
| romdrv.c | ioman / include / ioman.h |
| romdrv.c | loadcore / include / loadcore.h |
| romdrv.c | sysclib / include / sysclib.h |

---

## PS2SDK: iop/fs/romdrv/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000139_000525.html>

###### src → include Relation
| File in iop/fs/romdrv/src | Includes file in iop/fs/romdrv/include |
| romdrv.c | romdrv.h |

---

## PS2SDK: iop/fs/romdrv/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000139_000537.html>

###### src → kernel Relation
| File in iop/fs/romdrv/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |
| romdrv.c | include / irx.h |

---

## PS2SDK: iop/fs/subfile -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000140_000000.html>

###### subfile → common Relation
| File in iop/fs/subfile | Includes file in common |
| src / subfile.c | include / errno.h |

---

## PS2SDK: iop/fs/subfile -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000140_000223.html>

###### subfile → system Relation
| File in iop/fs/subfile | Includes file in iop/system |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | ioman / include / ioman.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / subfile.c | loadcore / include / loadcore.h |

---

## PS2SDK: iop/fs/subfile -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000140_000537.html>

###### subfile → kernel Relation
| File in iop/fs/subfile | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/fs/subfile/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000141_000000.html>

###### src → common Relation
| File in iop/fs/subfile/src | Includes file in common |
| subfile.c | include / errno.h |

---

## PS2SDK: iop/fs/subfile/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000141_000223.html>

###### src → system Relation
| File in iop/fs/subfile/src | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | ioman / include / ioman.h |
| irx_imports.h | sysclib / include / sysclib.h |
| subfile.c | loadcore / include / loadcore.h |

---

## PS2SDK: iop/fs/subfile/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000141_000537.html>

###### src → kernel Relation
| File in iop/fs/subfile/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/hdd -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000142_000000.html>

###### hdd → common Relation
| File in iop/hdd | Includes file in common |
| libapa / include / libapa.h | include / hdd-ioctl.h |
| hdck / src / hdck.c | include / errno.h |
| hdck / src / hdck.c | include / hdd-ioctl.h |
| libapa / src / apa.c | include / errno.h |
| libapa / src / apa.c | include / hdd-ioctl.h |
| libapa / src / cache.c | include / errno.h |
| libapa / src / cache.c | include / hdd-ioctl.h |
| libapa / src / free.c | include / errno.h |
| libapa / src / free.c | include / hdd-ioctl.h |
| libapa / src / journal.c | include / errno.h |
| libapa / src / journal.c | include / hdd-ioctl.h |
| libapa / src / misc.c | include / errno.h |
| libapa / src / misc.c | include / hdd-ioctl.h |
| libapa / src / password.c | include / errno.h |
| libapa / src / password.c | include / hdd-ioctl.h |
| libpfs / src / bitmap.c | include / errno.h |
| libpfs / src / block.c | include / errno.h |
| libpfs / src / blockWrite.c | include / errno.h |
| libpfs / src / cache.c | include / errno.h |
| libpfs / src / cache.c | include / hdd-ioctl.h |
| libpfs / src / dir.c | include / errno.h |
| libpfs / src / inode.c | include / errno.h |
| libpfs / src / journal.c | include / hdd-ioctl.h |
| libpfs / src / misc.c | include / errno.h |
| libpfs / src / misc.c | include / hdd-ioctl.h |
| libpfs / src / super.c | include / errno.h |
| libpfs / src / super.c | include / hdd-ioctl.h |
| libpfs / src / superWrite.c | include / errno.h |
| libpfs / src / superWrite.c | include / hdd-ioctl.h |
| fsck / src / bitmap_fsck.c | include / errno.h |
| fsck / src / bitmap_fsck.c | include / hdd-ioctl.h |
| fsck / src / fsck.c | include / errno.h |
| fsck / src / fsck.c | include / hdd-ioctl.h |
| fssk / src / fssk.c | include / errno.h |
| fssk / src / fssk.c | include / hdd-ioctl.h |
| hdsk / src / hdl.c | include / errno.h |
| hdsk / src / hdl.c | include / hdd-ioctl.h |
| hdsk / src / hdsk.c | include / errno.h |
| hdsk / src / hdsk.c | include / hdd-ioctl.h |
| hdsk / src / sim.c | include / hdd-ioctl.h |
| pfs / src / pfs.c | include / errno.h |
| pfs / src / pfs_fio.c | include / errno.h |
| pfs / src / pfs_fio.c | include / hdd-ioctl.h |
| pfs / src / pfs_fioctl.c | include / errno.h |
| pfs / src / pfs_fioctl.c | include / hdd-ioctl.h |
| apa / src / hdd.c | include / errno.h |
| apa / src / hdd.c | include / hdd-ioctl.h |
| apa / src / hdd_fio.c | include / errno.h |
| apa / src / hdd_fio.c | include / hdd-ioctl.h |

---

## PS2SDK: iop/hdd -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000142_000056.html>

###### hdd → cdvd Relation
| File in iop/hdd | Includes file in iop/cdvd |
| hdck / src / irx_imports.h | cdvdman / include / cdvdman.h |
| fsck / src / irx_imports.h | cdvdman / include / cdvdman.h |
| fssk / src / irx_imports.h | cdvdman / include / cdvdman.h |
| hdsk / src / irx_imports.h | cdvdman / include / cdvdman.h |
| pfs / src / irx_imports.h | cdvdman / include / cdvdman.h |
| apa / src / irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/hdd -&gt; dev9 Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000142_000087.html>

###### hdd → dev9 Relation
| File in iop/hdd | Includes file in iop/dev9 |
| hdck / src / hdck.c | atad / include / atad.h |
| hdck / src / hdd_blkio.h | atad / include / atad.h |
| hdck / src / irx_imports.h | atad / include / atad.h |
| hdck / src / misc_hdck.c | atad / include / atad.h |
| hdsk / src / hdd_blkio.h | atad / include / atad.h |
| hdsk / src / hdl.c | atad / include / atad.h |
| hdsk / src / hdsk.c | atad / include / atad.h |
| hdsk / src / irx_imports.h | atad / include / atad.h |
| hdsk / src / misc_hdsk.c | atad / include / atad.h |

---

## PS2SDK: iop/hdd -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000142_000223.html>

###### hdd → system Relation
| File in iop/hdd | Includes file in iop/system |
| hdck / src / hdck.c | iomanx / include / iomanX.h |
| hdck / src / hdck.c | loadcore / include / loadcore.h |
| hdck / src / hdck.c | stdio / include / stdio.h |
| hdck / src / hdck.c | sysclib / include / sysclib.h |
| hdck / src / irx_imports.h | intrman / include / intrman.h |
| hdck / src / irx_imports.h | iomanx / include / iomanX.h |
| hdck / src / irx_imports.h | stdio / include / stdio.h |
| hdck / src / irx_imports.h | sysclib / include / sysclib.h |
| hdck / src / irx_imports.h | threadman / include / thbase.h |
| libapa / src / apa.c | iomanx / include / iomanX.h |
| libapa / src / apa.c | stdio / include / stdio.h |
| libapa / src / cache.c | iomanx / include / iomanX.h |
| libapa / src / cache.c | stdio / include / stdio.h |
| libapa / src / free.c | iomanx / include / iomanX.h |
| libapa / src / free.c | stdio / include / stdio.h |
| libapa / src / journal.c | iomanx / include / iomanX.h |
| libapa / src / journal.c | stdio / include / stdio.h |
| libapa / src / misc.c | iomanx / include / iomanX.h |
| libapa / src / misc.c | stdio / include / stdio.h |
| libapa / src / password.c | iomanx / include / iomanX.h |
| libapa / src / password.c | stdio / include / stdio.h |
| libpfs / src / bitmap.c | stdio / include / stdio.h |
| libpfs / src / block.c | stdio / include / stdio.h |
| libpfs / src / blockWrite.c | stdio / include / stdio.h |
| libpfs / src / cache.c | stdio / include / stdio.h |
| libpfs / src / dir.c | stdio / include / stdio.h |
| libpfs / src / dir.c | iomanx / include / iomanX.h |
| libpfs / src / inode.c | stdio / include / stdio.h |
| libpfs / src / journal.c | stdio / include / stdio.h |
| libpfs / src / misc.c | stdio / include / stdio.h |
| libpfs / src / misc.c | iomanx / include / iomanX.h |
| libpfs / src / misc.c | sysclib / include / ctype.h |
| libpfs / src / super.c | stdio / include / stdio.h |
| libpfs / src / superWrite.c | stdio / include / stdio.h |
| fsck / src / bitmap_fsck.c | stdio / include / stdio.h |
| fsck / src / bitmap_fsck.c | sysclib / include / sysclib.h |
| fsck / src / bitmap_fsck.c | iomanx / include / iomanX.h |
| fsck / src / fsck.c | iomanx / include / iomanX.h |
| fsck / src / fsck.c | loadcore / include / loadcore.h |
| fsck / src / fsck.c | threadman / include / thbase.h |
| fsck / src / fsck.c | threadman / include / thevent.h |
| fsck / src / fsck.c | stdio / include / stdio.h |
| fsck / src / fsck.c | sysclib / include / sysclib.h |
| fsck / src / irx_imports.h | intrman / include / intrman.h |
| fsck / src / irx_imports.h | iomanx / include / iomanX.h |
| fsck / src / irx_imports.h | stdio / include / stdio.h |
| fsck / src / irx_imports.h | sysclib / include / sysclib.h |
| fsck / src / irx_imports.h | threadman / include / thbase.h |
| fsck / src / irx_imports.h | threadman / include / thevent.h |
| fsck / src / misc_fsck.c | threadman / include / thbase.h |
| fsck / src / misc_fsck.c | threadman / include / thevent.h |
| fssk / src / fssk.c | iomanx / include / iomanX.h |
| fssk / src / fssk.c | loadcore / include / loadcore.h |
| fssk / src / fssk.c | stdio / include / stdio.h |
| fssk / src / fssk.c | sysclib / include / sysclib.h |
| fssk / src / fssk.c | threadman / include / thbase.h |
| fssk / src / fssk.c | threadman / include / thevent.h |
| fssk / src / irx_imports.h | intrman / include / intrman.h |
| fssk / src / irx_imports.h | iomanx / include / iomanX.h |
| fssk / src / irx_imports.h | stdio / include / stdio.h |
| fssk / src / irx_imports.h | sysclib / include / sysclib.h |
| fssk / src / irx_imports.h | threadman / include / thbase.h |
| fssk / src / irx_imports.h | threadman / include / thevent.h |
| fssk / src / misc_fssk.c | threadman / include / thbase.h |
| fssk / src / misc_fssk.c | threadman / include / thevent.h |
| hdsk / src / hdl.c | iomanx / include / iomanX.h |
| hdsk / src / hdl.c | stdio / include / stdio.h |
| hdsk / src / hdl.c | sysclib / include / sysclib.h |
| hdsk / src / hdsk.c | iomanx / include / iomanX.h |
| hdsk / src / hdsk.c | loadcore / include / loadcore.h |
| hdsk / src / hdsk.c | stdio / include / stdio.h |
| hdsk / src / hdsk.c | sysclib / include / sysclib.h |
| hdsk / src / hdsk.c | threadman / include / thbase.h |
| hdsk / src / hdsk.c | threadman / include / thevent.h |
| hdsk / src / irx_imports.h | intrman / include / intrman.h |
| hdsk / src / irx_imports.h | iomanx / include / iomanX.h |
| hdsk / src / irx_imports.h | stdio / include / stdio.h |
| hdsk / src / irx_imports.h | sysclib / include / sysclib.h |
| hdsk / src / irx_imports.h | threadman / include / thbase.h |
| hdsk / src / irx_imports.h | threadman / include / thevent.h |
| hdsk / src / misc_hdsk.c | threadman / include / thbase.h |
| hdsk / src / misc_hdsk.c | threadman / include / thevent.h |
| hdsk / src / sim.c | stdio / include / stdio.h |
| hdsk / src / sim.c | sysclib / include / sysclib.h |
| pfs / src / irx_imports.h | intrman / include / intrman.h |
| pfs / src / irx_imports.h | iomanx / include / iomanX.h |
| pfs / src / irx_imports.h | stdio / include / stdio.h |
| pfs / src / irx_imports.h | sysclib / include / sysclib.h |
| pfs / src / irx_imports.h | threadman / include / thbase.h |
| pfs / src / irx_imports.h | threadman / include / thsemap.h |
| pfs / src / pfs.c | stdio / include / stdio.h |
| pfs / src / pfs.c | iomanx / include / iomanX.h |
| pfs / src / pfs.c | threadman / include / thsemap.h |
| pfs / src / pfs_fio.c | stdio / include / stdio.h |
| pfs / src / pfs_fio.c | iomanx / include / iomanX.h |
| pfs / src / pfs_fio.c | threadman / include / thsemap.h |
| pfs / src / pfs_fioctl.c | stdio / include / stdio.h |
| pfs / src / pfs_fioctl.c | iomanx / include / iomanX.h |
| pfs / src / pfs_fioctl.c | threadman / include / thsemap.h |
| apa / src / hdd.c | stdio / include / stdio.h |
| apa / src / hdd.c | iomanx / include / iomanX.h |
| apa / src / hdd_blkio.c | iomanx / include / iomanX.h |
| apa / src / hdd_fio.c | stdio / include / stdio.h |
| apa / src / hdd_fio.c | iomanx / include / iomanX.h |
| apa / src / hdd_fio.c | threadman / include / thsemap.h |
| apa / src / irx_imports.h | intrman / include / intrman.h |
| apa / src / irx_imports.h | iomanx / include / iomanX.h |
| apa / src / irx_imports.h | stdio / include / stdio.h |
| apa / src / irx_imports.h | sysclib / include / sysclib.h |
| apa / src / irx_imports.h | threadman / include / thbase.h |
| apa / src / irx_imports.h | threadman / include / thsemap.h |

---

## PS2SDK: iop/hdd -&gt; tcpip Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000142_000284.html>

###### hdd → tcpip Relation
| File in iop/hdd | Includes file in iop/tcpip |
| libapa / src / misc.c | tcpip-base / include / stdlib.h |
| libpfs / src / misc.c | tcpip-base / include / stdlib.h |
| pfs / src / pfs.c | tcpip-base / include / stdlib.h |
| apa / src / hdd.c | tcpip-base / include / stdlib.h |

---

## PS2SDK: iop/hdd -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000142_000537.html>

###### hdd → kernel Relation
| File in iop/hdd | Includes file in iop/kernel |
| hdck / src / hdck.c | include / irx.h |
| hdck / src / irx_imports.h | include / irx.h |
| libapa / src / misc.c | include / sys / time.h |
| libpfs / src / misc.c | include / sys / time.h |
| fsck / src / fsck.c | include / irx.h |
| fsck / src / fsck.c | include / kerr.h |
| fsck / src / irx_imports.h | include / irx.h |
| fssk / src / fssk.c | include / kerr.h |
| fssk / src / fssk.c | include / irx.h |
| fssk / src / irx_imports.h | include / irx.h |
| hdsk / src / hdl.c | include / irx.h |
| hdsk / src / hdsk.c | include / kerr.h |
| hdsk / src / hdsk.c | include / irx.h |
| hdsk / src / irx_imports.h | include / irx.h |
| pfs / src / irx_imports.h | include / irx.h |
| pfs / src / pfs.c | include / irx.h |
| apa / src / hdd.c | include / irx.h |
| apa / src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/hdd/apa -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000143_000000.html>

###### apa → common Relation
| File in iop/hdd/apa | Includes file in common |
| src / hdd.c | include / errno.h |
| src / hdd.c | include / hdd-ioctl.h |
| src / hdd_fio.c | include / errno.h |
| src / hdd_fio.c | include / hdd-ioctl.h |

---

## PS2SDK: iop/hdd/apa -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000143_000056.html>

###### apa → cdvd Relation
| File in iop/hdd/apa | Includes file in iop/cdvd |
| src / irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/hdd/apa -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000143_000223.html>

###### apa → system Relation
| File in iop/hdd/apa | Includes file in iop/system |
| src / hdd.c | stdio / include / stdio.h |
| src / hdd.c | iomanx / include / iomanX.h |
| src / hdd_blkio.c | iomanx / include / iomanX.h |
| src / hdd_fio.c | stdio / include / stdio.h |
| src / hdd_fio.c | iomanx / include / iomanX.h |
| src / hdd_fio.c | threadman / include / thsemap.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | iomanx / include / iomanX.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thsemap.h |

---

## PS2SDK: iop/hdd/apa -&gt; tcpip Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000143_000284.html>

###### apa → tcpip Relation
| File in iop/hdd/apa | Includes file in iop/tcpip |
| src / hdd.c | tcpip-base / include / stdlib.h |

---

## PS2SDK: iop/hdd/apa -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000143_000537.html>

###### apa → kernel Relation
| File in iop/hdd/apa | Includes file in iop/kernel |
| src / hdd.c | include / irx.h |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/hdd/apa/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000144_000000.html>

###### src → common Relation
| File in iop/hdd/apa/src | Includes file in common |
| hdd.c | include / errno.h |
| hdd.c | include / hdd-ioctl.h |
| hdd_fio.c | include / errno.h |
| hdd_fio.c | include / hdd-ioctl.h |

---

## PS2SDK: iop/hdd/apa/src -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000144_000056.html>

###### src → cdvd Relation
| File in iop/hdd/apa/src | Includes file in iop/cdvd |
| irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/hdd/apa/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000144_000223.html>

###### src → system Relation
| File in iop/hdd/apa/src | Includes file in iop/system |
| hdd.c | iomanx / include / iomanX.h |
| hdd.c | stdio / include / stdio.h |
| hdd_blkio.c | iomanx / include / iomanX.h |
| hdd_fio.c | iomanx / include / iomanX.h |
| hdd_fio.c | stdio / include / stdio.h |
| hdd_fio.c | threadman / include / thsemap.h |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | iomanx / include / iomanX.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thsemap.h |

---

## PS2SDK: iop/hdd/apa/src -&gt; tcpip Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000144_000284.html>

###### src → tcpip Relation
| File in iop/hdd/apa/src | Includes file in iop/tcpip |
| hdd.c | tcpip-base / include / stdlib.h |

---

## PS2SDK: iop/hdd/apa/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000144_000537.html>

###### src → kernel Relation
| File in iop/hdd/apa/src | Includes file in iop/kernel |
| hdd.c | include / irx.h |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/hdd/fsck -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000145_000000.html>

###### fsck → common Relation
| File in iop/hdd/fsck | Includes file in common |
| src / bitmap_fsck.c | include / errno.h |
| src / bitmap_fsck.c | include / hdd-ioctl.h |
| src / fsck.c | include / errno.h |
| src / fsck.c | include / hdd-ioctl.h |

---

## PS2SDK: iop/hdd/fsck -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000145_000056.html>

###### fsck → cdvd Relation
| File in iop/hdd/fsck | Includes file in iop/cdvd |
| src / irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/hdd/fsck -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000145_000223.html>

###### fsck → system Relation
| File in iop/hdd/fsck | Includes file in iop/system |
| src / bitmap_fsck.c | stdio / include / stdio.h |
| src / bitmap_fsck.c | sysclib / include / sysclib.h |
| src / bitmap_fsck.c | iomanx / include / iomanX.h |
| src / fsck.c | iomanx / include / iomanX.h |
| src / fsck.c | loadcore / include / loadcore.h |
| src / fsck.c | threadman / include / thbase.h |
| src / fsck.c | threadman / include / thevent.h |
| src / fsck.c | stdio / include / stdio.h |
| src / fsck.c | sysclib / include / sysclib.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | iomanx / include / iomanX.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thevent.h |
| src / misc_fsck.c | threadman / include / thbase.h |
| src / misc_fsck.c | threadman / include / thevent.h |

---

## PS2SDK: iop/hdd/fsck -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000145_000537.html>

###### fsck → kernel Relation
| File in iop/hdd/fsck | Includes file in iop/kernel |
| src / fsck.c | include / irx.h |
| src / fsck.c | include / kerr.h |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/hdd/fsck/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000146_000000.html>

###### src → common Relation
| File in iop/hdd/fsck/src | Includes file in common |
| bitmap_fsck.c | include / errno.h |
| bitmap_fsck.c | include / hdd-ioctl.h |
| fsck.c | include / errno.h |
| fsck.c | include / hdd-ioctl.h |

---

## PS2SDK: iop/hdd/fsck/src -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000146_000056.html>

###### src → cdvd Relation
| File in iop/hdd/fsck/src | Includes file in iop/cdvd |
| irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/hdd/fsck/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000146_000223.html>

###### src → system Relation
| File in iop/hdd/fsck/src | Includes file in iop/system |
| bitmap_fsck.c | iomanx / include / iomanX.h |
| bitmap_fsck.c | stdio / include / stdio.h |
| bitmap_fsck.c | sysclib / include / sysclib.h |
| fsck.c | iomanx / include / iomanX.h |
| fsck.c | loadcore / include / loadcore.h |
| fsck.c | stdio / include / stdio.h |
| fsck.c | sysclib / include / sysclib.h |
| fsck.c | threadman / include / thbase.h |
| fsck.c | threadman / include / thevent.h |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | iomanx / include / iomanX.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thevent.h |
| misc_fsck.c | threadman / include / thbase.h |
| misc_fsck.c | threadman / include / thevent.h |

---

## PS2SDK: iop/hdd/fsck/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000146_000537.html>

###### src → kernel Relation
| File in iop/hdd/fsck/src | Includes file in iop/kernel |
| fsck.c | include / irx.h |
| fsck.c | include / kerr.h |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/hdd/fssk -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000147_000000.html>

###### fssk → common Relation
| File in iop/hdd/fssk | Includes file in common |
| src / fssk.c | include / errno.h |
| src / fssk.c | include / hdd-ioctl.h |

---

## PS2SDK: iop/hdd/fssk -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000147_000056.html>

###### fssk → cdvd Relation
| File in iop/hdd/fssk | Includes file in iop/cdvd |
| src / irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/hdd/fssk -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000147_000223.html>

###### fssk → system Relation
| File in iop/hdd/fssk | Includes file in iop/system |
| src / fssk.c | iomanx / include / iomanX.h |
| src / fssk.c | loadcore / include / loadcore.h |
| src / fssk.c | stdio / include / stdio.h |
| src / fssk.c | sysclib / include / sysclib.h |
| src / fssk.c | threadman / include / thbase.h |
| src / fssk.c | threadman / include / thevent.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | iomanx / include / iomanX.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thevent.h |
| src / misc_fssk.c | threadman / include / thbase.h |
| src / misc_fssk.c | threadman / include / thevent.h |

---

## PS2SDK: iop/hdd/fssk -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000147_000537.html>

###### fssk → kernel Relation
| File in iop/hdd/fssk | Includes file in iop/kernel |
| src / fssk.c | include / kerr.h |
| src / fssk.c | include / irx.h |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/hdd/fssk/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000148_000000.html>

###### src → common Relation
| File in iop/hdd/fssk/src | Includes file in common |
| fssk.c | include / errno.h |
| fssk.c | include / hdd-ioctl.h |

---

## PS2SDK: iop/hdd/fssk/src -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000148_000056.html>

###### src → cdvd Relation
| File in iop/hdd/fssk/src | Includes file in iop/cdvd |
| irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/hdd/fssk/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000148_000223.html>

###### src → system Relation
| File in iop/hdd/fssk/src | Includes file in iop/system |
| fssk.c | iomanx / include / iomanX.h |
| fssk.c | loadcore / include / loadcore.h |
| fssk.c | stdio / include / stdio.h |
| fssk.c | sysclib / include / sysclib.h |
| fssk.c | threadman / include / thbase.h |
| fssk.c | threadman / include / thevent.h |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | iomanx / include / iomanX.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thevent.h |
| misc_fssk.c | threadman / include / thbase.h |
| misc_fssk.c | threadman / include / thevent.h |

---

## PS2SDK: iop/hdd/fssk/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000148_000537.html>

###### src → kernel Relation
| File in iop/hdd/fssk/src | Includes file in iop/kernel |
| fssk.c | include / irx.h |
| fssk.c | include / kerr.h |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/hdd/hdck -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000149_000000.html>

###### hdck → common Relation
| File in iop/hdd/hdck | Includes file in common |
| src / hdck.c | include / errno.h |
| src / hdck.c | include / hdd-ioctl.h |

---

## PS2SDK: iop/hdd/hdck -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000149_000056.html>

###### hdck → cdvd Relation
| File in iop/hdd/hdck | Includes file in iop/cdvd |
| src / irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/hdd/hdck -&gt; dev9 Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000149_000087.html>

###### hdck → dev9 Relation
| File in iop/hdd/hdck | Includes file in iop/dev9 |
| src / hdck.c | atad / include / atad.h |
| src / hdd_blkio.h | atad / include / atad.h |
| src / irx_imports.h | atad / include / atad.h |
| src / misc_hdck.c | atad / include / atad.h |

---

## PS2SDK: iop/hdd/hdck -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000149_000223.html>

###### hdck → system Relation
| File in iop/hdd/hdck | Includes file in iop/system |
| src / hdck.c | iomanx / include / iomanX.h |
| src / hdck.c | loadcore / include / loadcore.h |
| src / hdck.c | stdio / include / stdio.h |
| src / hdck.c | sysclib / include / sysclib.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | iomanx / include / iomanX.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |

---

## PS2SDK: iop/hdd/hdck -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000149_000537.html>

###### hdck → kernel Relation
| File in iop/hdd/hdck | Includes file in iop/kernel |
| src / hdck.c | include / irx.h |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/hdd/hdck/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000150_000000.html>

###### src → common Relation
| File in iop/hdd/hdck/src | Includes file in common |
| hdck.c | include / errno.h |
| hdck.c | include / hdd-ioctl.h |

---

## PS2SDK: iop/hdd/hdck/src -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000150_000056.html>

###### src → cdvd Relation
| File in iop/hdd/hdck/src | Includes file in iop/cdvd |
| irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/hdd/hdck/src -&gt; dev9 Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000150_000087.html>

###### src → dev9 Relation
| File in iop/hdd/hdck/src | Includes file in iop/dev9 |
| hdck.c | atad / include / atad.h |
| hdd_blkio.h | atad / include / atad.h |
| irx_imports.h | atad / include / atad.h |
| misc_hdck.c | atad / include / atad.h |

---

## PS2SDK: iop/hdd/hdck/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000150_000223.html>

###### src → system Relation
| File in iop/hdd/hdck/src | Includes file in iop/system |
| hdck.c | iomanx / include / iomanX.h |
| hdck.c | loadcore / include / loadcore.h |
| hdck.c | stdio / include / stdio.h |
| hdck.c | sysclib / include / sysclib.h |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | iomanx / include / iomanX.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |

---

## PS2SDK: iop/hdd/hdck/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000150_000537.html>

###### src → kernel Relation
| File in iop/hdd/hdck/src | Includes file in iop/kernel |
| hdck.c | include / irx.h |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/hdd/hdsk -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000151_000000.html>

###### hdsk → common Relation
| File in iop/hdd/hdsk | Includes file in common |
| src / hdl.c | include / errno.h |
| src / hdl.c | include / hdd-ioctl.h |
| src / hdsk.c | include / errno.h |
| src / hdsk.c | include / hdd-ioctl.h |
| src / sim.c | include / hdd-ioctl.h |

---

## PS2SDK: iop/hdd/hdsk -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000151_000056.html>

###### hdsk → cdvd Relation
| File in iop/hdd/hdsk | Includes file in iop/cdvd |
| src / irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/hdd/hdsk -&gt; dev9 Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000151_000087.html>

###### hdsk → dev9 Relation
| File in iop/hdd/hdsk | Includes file in iop/dev9 |
| src / hdd_blkio.h | atad / include / atad.h |
| src / hdl.c | atad / include / atad.h |
| src / hdsk.c | atad / include / atad.h |
| src / irx_imports.h | atad / include / atad.h |
| src / misc_hdsk.c | atad / include / atad.h |

---

## PS2SDK: iop/hdd/hdsk -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000151_000223.html>

###### hdsk → system Relation
| File in iop/hdd/hdsk | Includes file in iop/system |
| src / hdl.c | iomanx / include / iomanX.h |
| src / hdl.c | stdio / include / stdio.h |
| src / hdl.c | sysclib / include / sysclib.h |
| src / hdsk.c | iomanx / include / iomanX.h |
| src / hdsk.c | loadcore / include / loadcore.h |
| src / hdsk.c | stdio / include / stdio.h |
| src / hdsk.c | sysclib / include / sysclib.h |
| src / hdsk.c | threadman / include / thbase.h |
| src / hdsk.c | threadman / include / thevent.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | iomanx / include / iomanX.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thevent.h |
| src / misc_hdsk.c | threadman / include / thbase.h |
| src / misc_hdsk.c | threadman / include / thevent.h |
| src / sim.c | stdio / include / stdio.h |
| src / sim.c | sysclib / include / sysclib.h |

---

## PS2SDK: iop/hdd/hdsk -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000151_000537.html>

###### hdsk → kernel Relation
| File in iop/hdd/hdsk | Includes file in iop/kernel |
| src / hdl.c | include / irx.h |
| src / hdsk.c | include / kerr.h |
| src / hdsk.c | include / irx.h |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/hdd/hdsk/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000152_000000.html>

###### src → common Relation
| File in iop/hdd/hdsk/src | Includes file in common |
| hdl.c | include / errno.h |
| hdl.c | include / hdd-ioctl.h |
| hdsk.c | include / errno.h |
| hdsk.c | include / hdd-ioctl.h |
| sim.c | include / hdd-ioctl.h |

---

## PS2SDK: iop/hdd/hdsk/src -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000152_000056.html>

###### src → cdvd Relation
| File in iop/hdd/hdsk/src | Includes file in iop/cdvd |
| irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/hdd/hdsk/src -&gt; dev9 Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000152_000087.html>

###### src → dev9 Relation
| File in iop/hdd/hdsk/src | Includes file in iop/dev9 |
| hdd_blkio.h | atad / include / atad.h |
| hdl.c | atad / include / atad.h |
| hdsk.c | atad / include / atad.h |
| irx_imports.h | atad / include / atad.h |
| misc_hdsk.c | atad / include / atad.h |

---

## PS2SDK: iop/hdd/hdsk/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000152_000223.html>

###### src → system Relation
| File in iop/hdd/hdsk/src | Includes file in iop/system |
| hdl.c | iomanx / include / iomanX.h |
| hdl.c | stdio / include / stdio.h |
| hdl.c | sysclib / include / sysclib.h |
| hdsk.c | iomanx / include / iomanX.h |
| hdsk.c | loadcore / include / loadcore.h |
| hdsk.c | stdio / include / stdio.h |
| hdsk.c | sysclib / include / sysclib.h |
| hdsk.c | threadman / include / thbase.h |
| hdsk.c | threadman / include / thevent.h |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | iomanx / include / iomanX.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thevent.h |
| misc_hdsk.c | threadman / include / thbase.h |
| misc_hdsk.c | threadman / include / thevent.h |
| sim.c | stdio / include / stdio.h |
| sim.c | sysclib / include / sysclib.h |

---

## PS2SDK: iop/hdd/hdsk/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000152_000537.html>

###### src → kernel Relation
| File in iop/hdd/hdsk/src | Includes file in iop/kernel |
| hdl.c | include / irx.h |
| hdsk.c | include / irx.h |
| hdsk.c | include / kerr.h |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/hdd/pfs -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000153_000000.html>

###### pfs → common Relation
| File in iop/hdd/pfs | Includes file in common |
| src / pfs.c | include / errno.h |
| src / pfs_fio.c | include / errno.h |
| src / pfs_fio.c | include / hdd-ioctl.h |
| src / pfs_fioctl.c | include / errno.h |
| src / pfs_fioctl.c | include / hdd-ioctl.h |

---

## PS2SDK: iop/hdd/pfs -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000153_000056.html>

###### pfs → cdvd Relation
| File in iop/hdd/pfs | Includes file in iop/cdvd |
| src / irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/hdd/pfs -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000153_000223.html>

###### pfs → system Relation
| File in iop/hdd/pfs | Includes file in iop/system |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | iomanx / include / iomanX.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thsemap.h |
| src / pfs.c | stdio / include / stdio.h |
| src / pfs.c | iomanx / include / iomanX.h |
| src / pfs.c | threadman / include / thsemap.h |
| src / pfs_fio.c | stdio / include / stdio.h |
| src / pfs_fio.c | iomanx / include / iomanX.h |
| src / pfs_fio.c | threadman / include / thsemap.h |
| src / pfs_fioctl.c | stdio / include / stdio.h |
| src / pfs_fioctl.c | iomanx / include / iomanX.h |
| src / pfs_fioctl.c | threadman / include / thsemap.h |

---

## PS2SDK: iop/hdd/pfs -&gt; tcpip Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000153_000284.html>

###### pfs → tcpip Relation
| File in iop/hdd/pfs | Includes file in iop/tcpip |
| src / pfs.c | tcpip-base / include / stdlib.h |

---

## PS2SDK: iop/hdd/pfs -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000153_000537.html>

###### pfs → kernel Relation
| File in iop/hdd/pfs | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |
| src / pfs.c | include / irx.h |

---

## PS2SDK: iop/hdd/pfs/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000154_000000.html>

###### src → common Relation
| File in iop/hdd/pfs/src | Includes file in common |
| pfs.c | include / errno.h |
| pfs_fio.c | include / errno.h |
| pfs_fio.c | include / hdd-ioctl.h |
| pfs_fioctl.c | include / errno.h |
| pfs_fioctl.c | include / hdd-ioctl.h |

---

## PS2SDK: iop/hdd/pfs/src -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000154_000056.html>

###### src → cdvd Relation
| File in iop/hdd/pfs/src | Includes file in iop/cdvd |
| irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/hdd/pfs/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000154_000223.html>

###### src → system Relation
| File in iop/hdd/pfs/src | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | iomanx / include / iomanX.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thsemap.h |
| pfs.c | iomanx / include / iomanX.h |
| pfs.c | stdio / include / stdio.h |
| pfs.c | threadman / include / thsemap.h |
| pfs_fio.c | iomanx / include / iomanX.h |
| pfs_fio.c | stdio / include / stdio.h |
| pfs_fio.c | threadman / include / thsemap.h |
| pfs_fioctl.c | iomanx / include / iomanX.h |
| pfs_fioctl.c | stdio / include / stdio.h |
| pfs_fioctl.c | threadman / include / thsemap.h |

---

## PS2SDK: iop/hdd/pfs/src -&gt; tcpip Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000154_000284.html>

###### src → tcpip Relation
| File in iop/hdd/pfs/src | Includes file in iop/tcpip |
| pfs.c | tcpip-base / include / stdlib.h |

---

## PS2SDK: iop/hdd/pfs/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000154_000537.html>

###### src → kernel Relation
| File in iop/hdd/pfs/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |
| pfs.c | include / irx.h |

---

## PS2SDK: iop/iLink -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000155_000000.html>

###### iLink → common Relation
| File in iop/iLink | Includes file in common |
| IEEE1394_bd / src / include / sbp2_disk.h | include / tamtypes.h |
| IEEE1394_bd / src / sbp2_driver.c | include / usbhdfsd-common.h |
| IEEE1394_bd / src / scsi.c | include / errno.h |
| iLinkman / src / iLink.c | include / errno.h |
| IEEE1394_disk / src / main.c | include / errno.h |
| IEEE1394_disk / src / scsi.c | include / errno.h |

---

## PS2SDK: iop/iLink -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000155_000056.html>

###### iLink → cdvd Relation
| File in iop/iLink | Includes file in iop/cdvd |
| IEEE1394_bd / src / irx_imports.h | cdvdman / include / cdvdman.h |
| iLinkman / src / iLink_internal.c | cdvdman / include / cdvdman.h |
| iLinkman / src / irx_imports.h | cdvdman / include / cdvdman.h |
| IEEE1394_disk / src / irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/iLink -&gt; fs Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000155_000113.html>

###### iLink → fs Relation
| File in iop/iLink | Includes file in iop/fs |
| IEEE1394_bd / src / irx_imports.h | bdm / include / bdm.h |
| IEEE1394_bd / src / scsi.c | bdm / include / bdm.h |

---

## PS2SDK: iop/iLink -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000155_000223.html>

###### iLink → system Relation
| File in iop/iLink | Includes file in iop/system |
| IEEE1394_bd / src / irx_imports.h | intrman / include / intrman.h |
| IEEE1394_bd / src / irx_imports.h | ioman / include / ioman.h |
| IEEE1394_bd / src / irx_imports.h | loadcore / include / loadcore.h |
| IEEE1394_bd / src / irx_imports.h | stdio / include / stdio.h |
| IEEE1394_bd / src / irx_imports.h | sysclib / include / sysclib.h |
| IEEE1394_bd / src / irx_imports.h | threadman / include / thbase.h |
| IEEE1394_bd / src / irx_imports.h | threadman / include / thevent.h |
| IEEE1394_bd / src / irx_imports.h | threadman / include / thsemap.h |
| IEEE1394_bd / src / main.c | loadcore / include / loadcore.h |
| IEEE1394_bd / src / main.c | stdio / include / stdio.h |
| IEEE1394_bd / src / sbp2_driver.c | intrman / include / intrman.h |
| IEEE1394_bd / src / sbp2_driver.c | loadcore / include / loadcore.h |
| IEEE1394_bd / src / sbp2_driver.c | stdio / include / stdio.h |
| IEEE1394_bd / src / sbp2_driver.c | sysclib / include / sysclib.h |
| IEEE1394_bd / src / sbp2_driver.c | threadman / include / thbase.h |
| IEEE1394_bd / src / sbp2_driver.c | threadman / include / thevent.h |
| IEEE1394_bd / src / scsi.c | stdio / include / stdio.h |
| IEEE1394_bd / src / scsi.c | sysclib / include / sysclib.h |
| IEEE1394_bd / src / scsi.c | threadman / include / thsemap.h |
| iLinkman / src / iLink.c | dmacman / include / dmacman.h |
| iLinkman / src / iLink.c | ioman / include / ioman.h |
| iLinkman / src / iLink.c | intrman / include / intrman.h |
| iLinkman / src / iLink.c | loadcore / include / loadcore.h |
| iLinkman / src / iLink.c | stdio / include / stdio.h |
| iLinkman / src / iLink.c | threadman / include / thbase.h |
| iLinkman / src / iLink.c | threadman / include / thevent.h |
| iLinkman / src / iLink.c | threadman / include / thsemap.h |
| iLinkman / src / iLink.c | sysclib / include / sysclib.h |
| iLinkman / src / iLink_crom.c | stdio / include / stdio.h |
| iLinkman / src / iLink_crom.c | sysclib / include / sysclib.h |
| iLinkman / src / iLink_crom.c | threadman / include / thbase.h |
| iLinkman / src / iLink_DMA.c | dmacman / include / dmacman.h |
| iLinkman / src / iLink_DMA.c | stdio / include / stdio.h |
| iLinkman / src / iLink_DMA.c | threadman / include / thbase.h |
| iLinkman / src / iLink_DMA.c | threadman / include / thevent.h |
| iLinkman / src / iLink_internal.c | dmacman / include / dmacman.h |
| iLinkman / src / iLink_internal.c | intrman / include / intrman.h |
| iLinkman / src / iLink_internal.c | stdio / include / stdio.h |
| iLinkman / src / iLink_internal.c | sysclib / include / sysclib.h |
| iLinkman / src / iLink_internal.c | threadman / include / thbase.h |
| iLinkman / src / iLink_internal.c | threadman / include / thevent.h |
| iLinkman / src / iLink_intr.c | dmacman / include / dmacman.h |
| iLinkman / src / iLink_intr.c | stdio / include / stdio.h |
| iLinkman / src / iLink_intr.c | threadman / include / thevent.h |
| iLinkman / src / iLink_PHY.c | threadman / include / thbase.h |
| iLinkman / src / iLink_TxRx.c | intrman / include / intrman.h |
| iLinkman / src / iLink_TxRx.c | stdio / include / stdio.h |
| iLinkman / src / iLink_TxRx.c | threadman / include / thbase.h |
| iLinkman / src / iLink_TxRx.c | threadman / include / thevent.h |
| iLinkman / src / iLink_TxRx.c | threadman / include / thsemap.h |
| iLinkman / src / irx_imports.h | dmacman / include / dmacman.h |
| iLinkman / src / irx_imports.h | intrman / include / intrman.h |
| iLinkman / src / irx_imports.h | ioman / include / ioman.h |
| iLinkman / src / irx_imports.h | loadcore / include / loadcore.h |
| iLinkman / src / irx_imports.h | stdio / include / stdio.h |
| iLinkman / src / irx_imports.h | sysclib / include / sysclib.h |
| iLinkman / src / irx_imports.h | threadman / include / thbase.h |
| iLinkman / src / irx_imports.h | threadman / include / thevent.h |
| iLinkman / src / irx_imports.h | threadman / include / thsemap.h |
| IEEE1394_disk / src / irx_imports.h | intrman / include / intrman.h |
| IEEE1394_disk / src / irx_imports.h | ioman / include / ioman.h |
| IEEE1394_disk / src / irx_imports.h | loadcore / include / loadcore.h |
| IEEE1394_disk / src / irx_imports.h | stdio / include / stdio.h |
| IEEE1394_disk / src / irx_imports.h | sysclib / include / sysclib.h |
| IEEE1394_disk / src / irx_imports.h | threadman / include / thbase.h |
| IEEE1394_disk / src / irx_imports.h | threadman / include / thevent.h |
| IEEE1394_disk / src / irx_imports.h | threadman / include / thsemap.h |
| IEEE1394_disk / src / main.c | loadcore / include / loadcore.h |
| IEEE1394_disk / src / main.c | stdio / include / stdio.h |
| IEEE1394_disk / src / sbp2_driver.c | intrman / include / intrman.h |
| IEEE1394_disk / src / sbp2_driver.c | threadman / include / thbase.h |
| IEEE1394_disk / src / sbp2_driver.c | threadman / include / thevent.h |
| IEEE1394_disk / src / sbp2_driver.c | loadcore / include / loadcore.h |
| IEEE1394_disk / src / sbp2_driver.c | stdio / include / stdio.h |
| IEEE1394_disk / src / sbp2_driver.c | sysclib / include / sysclib.h |
| IEEE1394_disk / src / scsi.c | intrman / include / intrman.h |
| IEEE1394_disk / src / scsi.c | stdio / include / stdio.h |
| IEEE1394_disk / src / scsi.c | sysclib / include / sysclib.h |

---

## PS2SDK: iop/iLink -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000155_000537.html>

###### iLink → kernel Relation
| File in iop/iLink | Includes file in iop/kernel |
| iLinkman / include / iLinkman.h | include / irx.h |
| IEEE1394_bd / src / irx_imports.h | include / irx.h |
| IEEE1394_bd / src / main.c | include / irx.h |
| iLinkman / src / iLink.c | include / irx.h |
| iLinkman / src / irx_imports.h | include / irx.h |
| IEEE1394_disk / src / irx_imports.h | include / irx.h |
| IEEE1394_disk / src / main.c | include / irx.h |

---

## PS2SDK: iop/iLink/IEEE1394_bd -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000156_000000.html>

###### IEEE1394_bd → common Relation
| File in iop/iLink/IEEE1394_bd | Includes file in common |
| src / include / sbp2_disk.h | include / tamtypes.h |
| src / sbp2_driver.c | include / usbhdfsd-common.h |
| src / scsi.c | include / errno.h |

---

## PS2SDK: iop/iLink/IEEE1394_bd -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000156_000056.html>

###### IEEE1394_bd → cdvd Relation
| File in iop/iLink/IEEE1394_bd | Includes file in iop/cdvd |
| src / irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/iLink/IEEE1394_bd -&gt; fs Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000156_000113.html>

###### IEEE1394_bd → fs Relation
| File in iop/iLink/IEEE1394_bd | Includes file in iop/fs |
| src / irx_imports.h | bdm / include / bdm.h |
| src / scsi.c | bdm / include / bdm.h |

---

## PS2SDK: iop/iLink/IEEE1394_bd -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000156_000223.html>

###### IEEE1394_bd → system Relation
| File in iop/iLink/IEEE1394_bd | Includes file in iop/system |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | ioman / include / ioman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thevent.h |
| src / irx_imports.h | threadman / include / thsemap.h |
| src / main.c | loadcore / include / loadcore.h |
| src / main.c | stdio / include / stdio.h |
| src / sbp2_driver.c | intrman / include / intrman.h |
| src / sbp2_driver.c | loadcore / include / loadcore.h |
| src / sbp2_driver.c | stdio / include / stdio.h |
| src / sbp2_driver.c | sysclib / include / sysclib.h |
| src / sbp2_driver.c | threadman / include / thbase.h |
| src / sbp2_driver.c | threadman / include / thevent.h |
| src / scsi.c | stdio / include / stdio.h |
| src / scsi.c | sysclib / include / sysclib.h |
| src / scsi.c | threadman / include / thsemap.h |

---

## PS2SDK: iop/iLink/IEEE1394_bd -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000156_000537.html>

###### IEEE1394_bd → kernel Relation
| File in iop/iLink/IEEE1394_bd | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |
| src / main.c | include / irx.h |

---

## PS2SDK: iop/iLink/IEEE1394_bd/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000157_000000.html>

###### src → common Relation
| File in iop/iLink/IEEE1394_bd/src | Includes file in common |
| include / sbp2_disk.h | include / tamtypes.h |
| sbp2_driver.c | include / usbhdfsd-common.h |
| scsi.c | include / errno.h |

---

## PS2SDK: iop/iLink/IEEE1394_bd/src -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000157_000056.html>

###### src → cdvd Relation
| File in iop/iLink/IEEE1394_bd/src | Includes file in iop/cdvd |
| irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/iLink/IEEE1394_bd/src -&gt; fs Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000157_000113.html>

###### src → fs Relation
| File in iop/iLink/IEEE1394_bd/src | Includes file in iop/fs |
| irx_imports.h | bdm / include / bdm.h |
| scsi.c | bdm / include / bdm.h |

---

## PS2SDK: iop/iLink/IEEE1394_bd/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000157_000223.html>

###### src → system Relation
| File in iop/iLink/IEEE1394_bd/src | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | ioman / include / ioman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thevent.h |
| irx_imports.h | threadman / include / thsemap.h |
| main.c | loadcore / include / loadcore.h |
| main.c | stdio / include / stdio.h |
| sbp2_driver.c | intrman / include / intrman.h |
| sbp2_driver.c | loadcore / include / loadcore.h |
| sbp2_driver.c | stdio / include / stdio.h |
| sbp2_driver.c | sysclib / include / sysclib.h |
| sbp2_driver.c | threadman / include / thbase.h |
| sbp2_driver.c | threadman / include / thevent.h |
| scsi.c | stdio / include / stdio.h |
| scsi.c | sysclib / include / sysclib.h |
| scsi.c | threadman / include / thsemap.h |

---

## PS2SDK: iop/iLink/IEEE1394_bd/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000157_000537.html>

###### src → kernel Relation
| File in iop/iLink/IEEE1394_bd/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |
| main.c | include / irx.h |

---

## PS2SDK: iop/iLink/IEEE1394_disk -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000158_000000.html>

###### IEEE1394_disk → common Relation
| File in iop/iLink/IEEE1394_disk | Includes file in common |
| src / main.c | include / errno.h |
| src / scsi.c | include / errno.h |

---

## PS2SDK: iop/iLink/IEEE1394_disk -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000158_000056.html>

###### IEEE1394_disk → cdvd Relation
| File in iop/iLink/IEEE1394_disk | Includes file in iop/cdvd |
| src / irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/iLink/IEEE1394_disk -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000158_000223.html>

###### IEEE1394_disk → system Relation
| File in iop/iLink/IEEE1394_disk | Includes file in iop/system |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | ioman / include / ioman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thevent.h |
| src / irx_imports.h | threadman / include / thsemap.h |
| src / main.c | loadcore / include / loadcore.h |
| src / main.c | stdio / include / stdio.h |
| src / sbp2_driver.c | intrman / include / intrman.h |
| src / sbp2_driver.c | threadman / include / thbase.h |
| src / sbp2_driver.c | threadman / include / thevent.h |
| src / sbp2_driver.c | loadcore / include / loadcore.h |
| src / sbp2_driver.c | stdio / include / stdio.h |
| src / sbp2_driver.c | sysclib / include / sysclib.h |
| src / scsi.c | intrman / include / intrman.h |
| src / scsi.c | stdio / include / stdio.h |
| src / scsi.c | sysclib / include / sysclib.h |

---

## PS2SDK: iop/iLink/IEEE1394_disk -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000158_000537.html>

###### IEEE1394_disk → kernel Relation
| File in iop/iLink/IEEE1394_disk | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |
| src / main.c | include / irx.h |

---

## PS2SDK: iop/iLink/IEEE1394_disk/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000159_000000.html>

###### src → common Relation
| File in iop/iLink/IEEE1394_disk/src | Includes file in common |
| main.c | include / errno.h |
| scsi.c | include / errno.h |

---

## PS2SDK: iop/iLink/IEEE1394_disk/src -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000159_000056.html>

###### src → cdvd Relation
| File in iop/iLink/IEEE1394_disk/src | Includes file in iop/cdvd |
| irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/iLink/IEEE1394_disk/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000159_000223.html>

###### src → system Relation
| File in iop/iLink/IEEE1394_disk/src | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | ioman / include / ioman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thevent.h |
| irx_imports.h | threadman / include / thsemap.h |
| main.c | loadcore / include / loadcore.h |
| main.c | stdio / include / stdio.h |
| sbp2_driver.c | intrman / include / intrman.h |
| sbp2_driver.c | loadcore / include / loadcore.h |
| sbp2_driver.c | stdio / include / stdio.h |
| sbp2_driver.c | sysclib / include / sysclib.h |
| sbp2_driver.c | threadman / include / thbase.h |
| sbp2_driver.c | threadman / include / thevent.h |
| scsi.c | intrman / include / intrman.h |
| scsi.c | stdio / include / stdio.h |
| scsi.c | sysclib / include / sysclib.h |

---

## PS2SDK: iop/iLink/IEEE1394_disk/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000159_000537.html>

###### src → kernel Relation
| File in iop/iLink/IEEE1394_disk/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |
| main.c | include / irx.h |

---

## PS2SDK: iop/iLink/iLinkman -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000160_000000.html>

###### iLinkman → common Relation
| File in iop/iLink/iLinkman | Includes file in common |
| src / iLink.c | include / errno.h |

---

## PS2SDK: iop/iLink/iLinkman -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000160_000056.html>

###### iLinkman → cdvd Relation
| File in iop/iLink/iLinkman | Includes file in iop/cdvd |
| src / iLink_internal.c | cdvdman / include / cdvdman.h |
| src / irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/iLink/iLinkman -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000160_000223.html>

###### iLinkman → system Relation
| File in iop/iLink/iLinkman | Includes file in iop/system |
| src / iLink.c | dmacman / include / dmacman.h |
| src / iLink.c | ioman / include / ioman.h |
| src / iLink.c | intrman / include / intrman.h |
| src / iLink.c | loadcore / include / loadcore.h |
| src / iLink.c | stdio / include / stdio.h |
| src / iLink.c | threadman / include / thbase.h |
| src / iLink.c | threadman / include / thevent.h |
| src / iLink.c | threadman / include / thsemap.h |
| src / iLink.c | sysclib / include / sysclib.h |
| src / iLink_crom.c | stdio / include / stdio.h |
| src / iLink_crom.c | sysclib / include / sysclib.h |
| src / iLink_crom.c | threadman / include / thbase.h |
| src / iLink_DMA.c | dmacman / include / dmacman.h |
| src / iLink_DMA.c | stdio / include / stdio.h |
| src / iLink_DMA.c | threadman / include / thbase.h |
| src / iLink_DMA.c | threadman / include / thevent.h |
| src / iLink_internal.c | dmacman / include / dmacman.h |
| src / iLink_internal.c | intrman / include / intrman.h |
| src / iLink_internal.c | stdio / include / stdio.h |
| src / iLink_internal.c | sysclib / include / sysclib.h |
| src / iLink_internal.c | threadman / include / thbase.h |
| src / iLink_internal.c | threadman / include / thevent.h |
| src / iLink_intr.c | dmacman / include / dmacman.h |
| src / iLink_intr.c | stdio / include / stdio.h |
| src / iLink_intr.c | threadman / include / thevent.h |
| src / iLink_PHY.c | threadman / include / thbase.h |
| src / iLink_TxRx.c | intrman / include / intrman.h |
| src / iLink_TxRx.c | stdio / include / stdio.h |
| src / iLink_TxRx.c | threadman / include / thbase.h |
| src / iLink_TxRx.c | threadman / include / thevent.h |
| src / iLink_TxRx.c | threadman / include / thsemap.h |
| src / irx_imports.h | dmacman / include / dmacman.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | ioman / include / ioman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thevent.h |
| src / irx_imports.h | threadman / include / thsemap.h |

---

## PS2SDK: iop/iLink/iLinkman -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000160_000537.html>

###### iLinkman → kernel Relation
| File in iop/iLink/iLinkman | Includes file in iop/kernel |
| include / iLinkman.h | include / irx.h |
| src / iLink.c | include / irx.h |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/iLink/iLinkman/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000161_000000.html>

###### src → common Relation
| File in iop/iLink/iLinkman/src | Includes file in common |
| iLink.c | include / errno.h |

---

## PS2SDK: iop/iLink/iLinkman/src -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000161_000056.html>

###### src → cdvd Relation
| File in iop/iLink/iLinkman/src | Includes file in iop/cdvd |
| iLink_internal.c | cdvdman / include / cdvdman.h |
| irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/iLink/iLinkman/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000161_000223.html>

###### src → system Relation
| File in iop/iLink/iLinkman/src | Includes file in iop/system |
| iLink.c | dmacman / include / dmacman.h |
| iLink.c | intrman / include / intrman.h |
| iLink.c | ioman / include / ioman.h |
| iLink.c | loadcore / include / loadcore.h |
| iLink.c | stdio / include / stdio.h |
| iLink.c | sysclib / include / sysclib.h |
| iLink.c | threadman / include / thbase.h |
| iLink.c | threadman / include / thevent.h |
| iLink.c | threadman / include / thsemap.h |
| iLink_crom.c | stdio / include / stdio.h |
| iLink_crom.c | sysclib / include / sysclib.h |
| iLink_crom.c | threadman / include / thbase.h |
| iLink_DMA.c | dmacman / include / dmacman.h |
| iLink_DMA.c | stdio / include / stdio.h |
| iLink_DMA.c | threadman / include / thbase.h |
| iLink_DMA.c | threadman / include / thevent.h |
| iLink_internal.c | dmacman / include / dmacman.h |
| iLink_internal.c | intrman / include / intrman.h |
| iLink_internal.c | stdio / include / stdio.h |
| iLink_internal.c | sysclib / include / sysclib.h |
| iLink_internal.c | threadman / include / thbase.h |
| iLink_internal.c | threadman / include / thevent.h |
| iLink_intr.c | dmacman / include / dmacman.h |
| iLink_intr.c | stdio / include / stdio.h |
| iLink_intr.c | threadman / include / thevent.h |
| iLink_PHY.c | threadman / include / thbase.h |
| iLink_TxRx.c | intrman / include / intrman.h |
| iLink_TxRx.c | stdio / include / stdio.h |
| iLink_TxRx.c | threadman / include / thbase.h |
| iLink_TxRx.c | threadman / include / thevent.h |
| iLink_TxRx.c | threadman / include / thsemap.h |
| irx_imports.h | dmacman / include / dmacman.h |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | ioman / include / ioman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thevent.h |
| irx_imports.h | threadman / include / thsemap.h |

---

## PS2SDK: iop/iLink/iLinkman/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000161_000537.html>

###### src → kernel Relation
| File in iop/iLink/iLinkman/src | Includes file in iop/kernel |
| iLink.c | include / irx.h |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/input -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000162_000000.html>

###### input → common Relation
| File in iop/input | Includes file in common |
| rmman / include / rmman.h | include / librm-common.h |

---

## PS2SDK: iop/input -&gt; sio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000162_000197.html>

###### input → sio Relation
| File in iop/input | Includes file in iop/sio |
| padman / src / irx_imports.h | sio2man / include / sio2man.h |
| padman / src / padData.c | sio2man / include / sio2man.h |
| rmman / src / irx_imports.h | sio2man / include / rsio2man.h |
| rmman / src / rmman.c | sio2man / include / rsio2man.h |

---

## PS2SDK: iop/input -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000162_000223.html>

###### input → system Relation
| File in iop/input | Includes file in iop/system |
| padman / src / freepad.c | sysclib / include / ctype.h |
| padman / src / freepad.c | stdio / include / stdio.h |
| padman / src / freepad.c | loadcore / include / loadcore.h |
| padman / src / freepad.c | sysclib / include / sysclib.h |
| padman / src / freepad.c | threadman / include / thevent.h |
| padman / src / freepad.c | threadman / include / thbase.h |
| padman / src / irx_imports.h | intrman / include / intrman.h |
| padman / src / irx_imports.h | loadcore / include / loadcore.h |
| padman / src / irx_imports.h | sifman / include / sifman.h |
| padman / src / irx_imports.h | stdio / include / stdio.h |
| padman / src / irx_imports.h | sysclib / include / sysclib.h |
| padman / src / irx_imports.h | threadman / include / thbase.h |
| padman / src / irx_imports.h | threadman / include / thevent.h |
| padman / src / irx_imports.h | vblank / include / vblank.h |
| padman / src / padCmds.c | threadman / include / thevent.h |
| padman / src / padData.c | sifman / include / sifman.h |
| padman / src / padData.c | stdio / include / stdio.h |
| padman / src / padInit.c | stdio / include / stdio.h |
| padman / src / padInit.c | threadman / include / thevent.h |
| padman / src / padInit.c | threadman / include / thbase.h |
| padman / src / padInit.c | intrman / include / intrman.h |
| padman / src / padInit.c | vblank / include / vblank.h |
| padman / src / padInit.c | sifman / include / sifman.h |
| padman / src / padMiscFuncs.c | stdio / include / stdio.h |
| padman / src / padMiscFuncs.c | threadman / include / thevent.h |
| padman / src / padMiscFuncs.c | threadman / include / thbase.h |
| padman / src / padMiscFuncs.c | vblank / include / vblank.h |
| padman / src / padPortOpen.c | stdio / include / stdio.h |
| padman / src / padPortOpen.c | threadman / include / thevent.h |
| padman / src / padPortOpen.c | threadman / include / thbase.h |
| padman / src / rpcserver.c | threadman / include / thbase.h |
| padman / src / rpcserver.c | stdio / include / stdio.h |
| padman / src / rpcserver.c | sifman / include / sifman.h |
| rmman / src / irx_imports.h | intrman / include / intrman.h |
| rmman / src / irx_imports.h | loadcore / include / loadcore.h |
| rmman / src / irx_imports.h | sifman / include / sifman.h |
| rmman / src / irx_imports.h | stdio / include / stdio.h |
| rmman / src / irx_imports.h | threadman / include / thbase.h |
| rmman / src / irx_imports.h | threadman / include / thevent.h |
| rmman / src / irx_imports.h | vblank / include / vblank.h |
| rmman / src / rmman.c | intrman / include / intrman.h |
| rmman / src / rmman.c | loadcore / include / loadcore.h |
| rmman / src / rmman.c | sifman / include / sifman.h |
| rmman / src / rmman.c | stdio / include / stdio.h |
| rmman / src / rmman.c | threadman / include / thbase.h |
| rmman / src / rmman.c | threadman / include / thevent.h |
| rmman / src / rmman.c | vblank / include / vblank.h |

---

## PS2SDK: iop/input -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000162_000537.html>

###### input → kernel Relation
| File in iop/input | Includes file in iop/kernel |
| rmman / include / rmman.h | include / irx.h |
| padman / include / xpadman.h | include / defs.h |
| padman / src / freepad.c | include / irx.h |
| padman / src / freepad.h | include / irx.h |
| padman / src / irx_imports.h | include / irx.h |
| padman / src / padData.c | include / irx.h |
| padman / src / padMiscFuncs.c | include / irx.h |
| padman / src / sio2Cmds.c | include / irx.h |
| rmman / src / irx_imports.h | include / irx.h |
| rmman / src / rmman.c | include / irx.h |

---

## PS2SDK: iop/input/padman -&gt; sio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000163_000197.html>

###### padman → sio Relation
| File in iop/input/padman | Includes file in iop/sio |
| src / irx_imports.h | sio2man / include / sio2man.h |
| src / padData.c | sio2man / include / sio2man.h |

---

## PS2SDK: iop/input/padman -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000163_000223.html>

###### padman → system Relation
| File in iop/input/padman | Includes file in iop/system |
| src / freepad.c | sysclib / include / ctype.h |
| src / freepad.c | stdio / include / stdio.h |
| src / freepad.c | loadcore / include / loadcore.h |
| src / freepad.c | sysclib / include / sysclib.h |
| src / freepad.c | threadman / include / thevent.h |
| src / freepad.c | threadman / include / thbase.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | sifman / include / sifman.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thevent.h |
| src / irx_imports.h | vblank / include / vblank.h |
| src / padCmds.c | threadman / include / thevent.h |
| src / padData.c | sifman / include / sifman.h |
| src / padData.c | stdio / include / stdio.h |
| src / padInit.c | stdio / include / stdio.h |
| src / padInit.c | threadman / include / thevent.h |
| src / padInit.c | threadman / include / thbase.h |
| src / padInit.c | intrman / include / intrman.h |
| src / padInit.c | vblank / include / vblank.h |
| src / padInit.c | sifman / include / sifman.h |
| src / padMiscFuncs.c | stdio / include / stdio.h |
| src / padMiscFuncs.c | threadman / include / thevent.h |
| src / padMiscFuncs.c | threadman / include / thbase.h |
| src / padMiscFuncs.c | vblank / include / vblank.h |
| src / padPortOpen.c | stdio / include / stdio.h |
| src / padPortOpen.c | threadman / include / thevent.h |
| src / padPortOpen.c | threadman / include / thbase.h |
| src / rpcserver.c | threadman / include / thbase.h |
| src / rpcserver.c | stdio / include / stdio.h |
| src / rpcserver.c | sifman / include / sifman.h |

---

## PS2SDK: iop/input/padman -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000163_000537.html>

###### padman → kernel Relation
| File in iop/input/padman | Includes file in iop/kernel |
| include / xpadman.h | include / defs.h |
| src / freepad.c | include / irx.h |
| src / freepad.h | include / irx.h |
| src / irx_imports.h | include / irx.h |
| src / padData.c | include / irx.h |
| src / padMiscFuncs.c | include / irx.h |
| src / sio2Cmds.c | include / irx.h |

---

## PS2SDK: iop/input/padman/src -&gt; sio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000164_000197.html>

###### src → sio Relation
| File in iop/input/padman/src | Includes file in iop/sio |
| irx_imports.h | sio2man / include / sio2man.h |
| padData.c | sio2man / include / sio2man.h |

---

## PS2SDK: iop/input/padman/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000164_000223.html>

###### src → system Relation
| File in iop/input/padman/src | Includes file in iop/system |
| freepad.c | sysclib / include / ctype.h |
| freepad.c | loadcore / include / loadcore.h |
| freepad.c | stdio / include / stdio.h |
| freepad.c | sysclib / include / sysclib.h |
| freepad.c | threadman / include / thbase.h |
| freepad.c | threadman / include / thevent.h |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | sifman / include / sifman.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thevent.h |
| irx_imports.h | vblank / include / vblank.h |
| padCmds.c | threadman / include / thevent.h |
| padData.c | sifman / include / sifman.h |
| padData.c | stdio / include / stdio.h |
| padInit.c | intrman / include / intrman.h |
| padInit.c | sifman / include / sifman.h |
| padInit.c | stdio / include / stdio.h |
| padInit.c | threadman / include / thbase.h |
| padInit.c | threadman / include / thevent.h |
| padInit.c | vblank / include / vblank.h |
| padMiscFuncs.c | stdio / include / stdio.h |
| padMiscFuncs.c | threadman / include / thbase.h |
| padMiscFuncs.c | threadman / include / thevent.h |
| padMiscFuncs.c | vblank / include / vblank.h |
| padPortOpen.c | stdio / include / stdio.h |
| padPortOpen.c | threadman / include / thbase.h |
| padPortOpen.c | threadman / include / thevent.h |
| rpcserver.c | sifman / include / sifman.h |
| rpcserver.c | stdio / include / stdio.h |
| rpcserver.c | threadman / include / thbase.h |

---

## PS2SDK: iop/input/padman/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000164_000537.html>

###### src → kernel Relation
| File in iop/input/padman/src | Includes file in iop/kernel |
| freepad.c | include / irx.h |
| freepad.h | include / irx.h |
| irx_imports.h | include / irx.h |
| padData.c | include / irx.h |
| padMiscFuncs.c | include / irx.h |
| sio2Cmds.c | include / irx.h |

---

## PS2SDK: iop/input/rmman -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000165_000000.html>

###### rmman → common Relation
| File in iop/input/rmman | Includes file in common |
| include / rmman.h | include / librm-common.h |

---

## PS2SDK: iop/input/rmman -&gt; sio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000165_000197.html>

###### rmman → sio Relation
| File in iop/input/rmman | Includes file in iop/sio |
| src / irx_imports.h | sio2man / include / rsio2man.h |
| src / rmman.c | sio2man / include / rsio2man.h |

---

## PS2SDK: iop/input/rmman -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000165_000223.html>

###### rmman → system Relation
| File in iop/input/rmman | Includes file in iop/system |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | sifman / include / sifman.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thevent.h |
| src / irx_imports.h | vblank / include / vblank.h |
| src / rmman.c | intrman / include / intrman.h |
| src / rmman.c | loadcore / include / loadcore.h |
| src / rmman.c | sifman / include / sifman.h |
| src / rmman.c | stdio / include / stdio.h |
| src / rmman.c | threadman / include / thbase.h |
| src / rmman.c | threadman / include / thevent.h |
| src / rmman.c | vblank / include / vblank.h |

---

## PS2SDK: iop/input/rmman -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000165_000537.html>

###### rmman → kernel Relation
| File in iop/input/rmman | Includes file in iop/kernel |
| include / rmman.h | include / irx.h |
| src / irx_imports.h | include / irx.h |
| src / rmman.c | include / irx.h |

---

## PS2SDK: iop/input/rmman/src -&gt; sio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000166_000197.html>

###### src → sio Relation
| File in iop/input/rmman/src | Includes file in iop/sio |
| irx_imports.h | sio2man / include / rsio2man.h |
| rmman.c | sio2man / include / rsio2man.h |

---

## PS2SDK: iop/input/rmman/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000166_000223.html>

###### src → system Relation
| File in iop/input/rmman/src | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | sifman / include / sifman.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thevent.h |
| irx_imports.h | vblank / include / vblank.h |
| rmman.c | intrman / include / intrman.h |
| rmman.c | loadcore / include / loadcore.h |
| rmman.c | sifman / include / sifman.h |
| rmman.c | stdio / include / stdio.h |
| rmman.c | threadman / include / thbase.h |
| rmman.c | threadman / include / thevent.h |
| rmman.c | vblank / include / vblank.h |

---

## PS2SDK: iop/input/rmman/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000166_000536.html>

###### src → include Relation
| File in iop/input/rmman/src | Includes file in iop/input/rmman/include |
| rmman.c | rmman.h |

---

## PS2SDK: iop/input/rmman/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000166_000537.html>

###### src → kernel Relation
| File in iop/input/rmman/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |
| rmman.c | include / irx.h |

---

## PS2SDK: iop/memorycard -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000167_000000.html>

###### memorycard → common Relation
| File in iop/memorycard | Includes file in common |
| mcman / include / mcman.h | include / libmc-common.h |
| mcman / src / mcman-internal.h | include / errno.h |

---

## PS2SDK: iop/memorycard -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000167_000056.html>

###### memorycard → cdvd Relation
| File in iop/memorycard | Includes file in iop/cdvd |
| mcman / src / irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/memorycard -&gt; security Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000167_000190.html>

###### memorycard → security Relation
| File in iop/memorycard | Includes file in iop/security |
| mcman / src / irx_imports.h | secrman / include / secrman.h |
| mcman / src / mcman-internal.h | secrman / include / secrman.h |

---

## PS2SDK: iop/memorycard -&gt; secrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000167_000193.html>

###### memorycard → secrman Relation
| File in iop/memorycard | Includes file in iop/security/secrman |
| mcman / src / irx_imports.h | include / secrman.h |
| mcman / src / mcman-internal.h | include / secrman.h |

---

## PS2SDK: iop/memorycard -&gt; sio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000167_000197.html>

###### memorycard → sio Relation
| File in iop/memorycard | Includes file in iop/sio |
| mcman / src / irx_imports.h | sio2man / include / sio2man.h |
| mcman / src / mcman-internal.h | sio2man / include / sio2man.h |

---

## PS2SDK: iop/memorycard -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000167_000223.html>

###### memorycard → system Relation
| File in iop/memorycard | Includes file in iop/system |
| mcman / src / irx_imports.h | intrman / include / intrman.h |
| mcman / src / irx_imports.h | ioman / include / ioman.h |
| mcman / src / irx_imports.h | loadcore / include / loadcore.h |
| mcman / src / irx_imports.h | modload / include / modload.h |
| mcman / src / irx_imports.h | stdio / include / stdio.h |
| mcman / src / irx_imports.h | sysclib / include / sysclib.h |
| mcman / src / irx_imports.h | timrman / include / timrman.h |
| mcman / src / irx_imports.h | threadman / include / thbase.h |
| mcman / src / irx_imports.h | threadman / include / thsemap.h |
| mcman / src / mcman-internal.h | loadcore / include / loadcore.h |
| mcman / src / mcman-internal.h | intrman / include / intrman.h |
| mcman / src / mcman-internal.h | sysclib / include / sysclib.h |
| mcman / src / mcman-internal.h | threadman / include / thbase.h |
| mcman / src / mcman-internal.h | threadman / include / thsemap.h |
| mcman / src / mcman-internal.h | timrman / include / timrman.h |
| mcman / src / mcman-internal.h | modload / include / modload.h |
| mcman / src / mcman-internal.h | ioman / include / ioman.h |
| mcman / src / mcman-internal.h | stdio / include / stdio.h |
| mcserv / src / irx_imports.h | intrman / include / intrman.h |
| mcserv / src / irx_imports.h | loadcore / include / loadcore.h |
| mcserv / src / irx_imports.h | sifman / include / sifman.h |
| mcserv / src / irx_imports.h | stdio / include / stdio.h |
| mcserv / src / irx_imports.h | sysclib / include / sysclib.h |
| mcserv / src / irx_imports.h | threadman / include / thbase.h |
| mcserv / src / mcserv.h | loadcore / include / loadcore.h |
| mcserv / src / mcserv.h | intrman / include / intrman.h |
| mcserv / src / mcserv.h | sysclib / include / sysclib.h |
| mcserv / src / mcserv.h | sifman / include / sifman.h |
| mcserv / src / mcserv.h | threadman / include / thbase.h |
| mcserv / src / mcserv.h | stdio / include / stdio.h |

---

## PS2SDK: iop/memorycard -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000167_000537.html>

###### memorycard → kernel Relation
| File in iop/memorycard | Includes file in iop/kernel |
| mcman / include / mcman.h | include / irx.h |
| mcman / src / irx_imports.h | include / irx.h |
| mcman / src / mcman-internal.h | include / sys / time.h |
| mcserv / src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/memorycard/mcman -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000168_000000.html>

###### mcman → common Relation
| File in iop/memorycard/mcman | Includes file in common |
| include / mcman.h | include / libmc-common.h |
| src / mcman-internal.h | include / errno.h |

---

## PS2SDK: iop/memorycard/mcman -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000168_000056.html>

###### mcman → cdvd Relation
| File in iop/memorycard/mcman | Includes file in iop/cdvd |
| src / irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/memorycard/mcman -&gt; security Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000168_000190.html>

###### mcman → security Relation
| File in iop/memorycard/mcman | Includes file in iop/security |
| src / irx_imports.h | secrman / include / secrman.h |
| src / mcman-internal.h | secrman / include / secrman.h |

---

## PS2SDK: iop/memorycard/mcman -&gt; sio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000168_000197.html>

###### mcman → sio Relation
| File in iop/memorycard/mcman | Includes file in iop/sio |
| src / irx_imports.h | sio2man / include / sio2man.h |
| src / mcman-internal.h | sio2man / include / sio2man.h |

---

## PS2SDK: iop/memorycard/mcman -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000168_000223.html>

###### mcman → system Relation
| File in iop/memorycard/mcman | Includes file in iop/system |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | ioman / include / ioman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | modload / include / modload.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | timrman / include / timrman.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thsemap.h |
| src / mcman-internal.h | loadcore / include / loadcore.h |
| src / mcman-internal.h | intrman / include / intrman.h |
| src / mcman-internal.h | sysclib / include / sysclib.h |
| src / mcman-internal.h | threadman / include / thbase.h |
| src / mcman-internal.h | threadman / include / thsemap.h |
| src / mcman-internal.h | timrman / include / timrman.h |
| src / mcman-internal.h | modload / include / modload.h |
| src / mcman-internal.h | ioman / include / ioman.h |
| src / mcman-internal.h | stdio / include / stdio.h |

---

## PS2SDK: iop/memorycard/mcman -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000168_000537.html>

###### mcman → kernel Relation
| File in iop/memorycard/mcman | Includes file in iop/kernel |
| include / mcman.h | include / irx.h |
| src / irx_imports.h | include / irx.h |
| src / mcman-internal.h | include / sys / time.h |

---

## PS2SDK: iop/memorycard/mcman/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000169_000000.html>

###### src → common Relation
| File in iop/memorycard/mcman/src | Includes file in common |
| mcman-internal.h | include / errno.h |

---

## PS2SDK: iop/memorycard/mcman/src -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000169_000056.html>

###### src → cdvd Relation
| File in iop/memorycard/mcman/src | Includes file in iop/cdvd |
| irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/memorycard/mcman/src -&gt; security Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000169_000190.html>

###### src → security Relation
| File in iop/memorycard/mcman/src | Includes file in iop/security |
| irx_imports.h | secrman / include / secrman.h |
| mcman-internal.h | secrman / include / secrman.h |

---

## PS2SDK: iop/memorycard/mcman/src -&gt; sio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000169_000197.html>

###### src → sio Relation
| File in iop/memorycard/mcman/src | Includes file in iop/sio |
| irx_imports.h | sio2man / include / sio2man.h |
| mcman-internal.h | sio2man / include / sio2man.h |

---

## PS2SDK: iop/memorycard/mcman/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000169_000223.html>

###### src → system Relation
| File in iop/memorycard/mcman/src | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | ioman / include / ioman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | modload / include / modload.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thsemap.h |
| irx_imports.h | timrman / include / timrman.h |
| mcman-internal.h | intrman / include / intrman.h |
| mcman-internal.h | ioman / include / ioman.h |
| mcman-internal.h | loadcore / include / loadcore.h |
| mcman-internal.h | modload / include / modload.h |
| mcman-internal.h | stdio / include / stdio.h |
| mcman-internal.h | sysclib / include / sysclib.h |
| mcman-internal.h | threadman / include / thbase.h |
| mcman-internal.h | threadman / include / thsemap.h |
| mcman-internal.h | timrman / include / timrman.h |

---

## PS2SDK: iop/memorycard/mcman/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000169_000537.html>

###### src → kernel Relation
| File in iop/memorycard/mcman/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |
| mcman-internal.h | include / sys / time.h |

---

## PS2SDK: iop/memorycard/mcman/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000169_000542.html>

###### src → include Relation
| File in iop/memorycard/mcman/src | Includes file in iop/memorycard/mcman/include |
| main.c | mcman.h |
| mcdev.c | mcman.h |
| mciomanx_backing.c | mcman.h |
| mcsio2.c | mcman.h |
| ps1mc_fio.c | mcman.h |
| ps2mc_fio.c | mcman.h |

---

## PS2SDK: iop/memorycard/mcserv -&gt; mcman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000170_000168.html>

###### mcserv → mcman Relation
| File in iop/memorycard/mcserv | Includes file in iop/memorycard/mcman |
| src / irx_imports.h | include / mcman.h |
| src / mcserv.h | include / mcman.h |

---

## PS2SDK: iop/memorycard/mcserv -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000170_000223.html>

###### mcserv → system Relation
| File in iop/memorycard/mcserv | Includes file in iop/system |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | sifman / include / sifman.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / mcserv.h | loadcore / include / loadcore.h |
| src / mcserv.h | intrman / include / intrman.h |
| src / mcserv.h | sysclib / include / sysclib.h |
| src / mcserv.h | sifman / include / sifman.h |
| src / mcserv.h | threadman / include / thbase.h |
| src / mcserv.h | stdio / include / stdio.h |

---

## PS2SDK: iop/memorycard/mcserv -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000170_000537.html>

###### mcserv → kernel Relation
| File in iop/memorycard/mcserv | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/memorycard/mcserv/src -&gt; mcman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000171_000168.html>

###### src → mcman Relation
| File in iop/memorycard/mcserv/src | Includes file in iop/memorycard/mcman |
| irx_imports.h | include / mcman.h |
| mcserv.h | include / mcman.h |

---

## PS2SDK: iop/memorycard/mcserv/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000171_000223.html>

###### src → system Relation
| File in iop/memorycard/mcserv/src | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | sifman / include / sifman.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| mcserv.h | intrman / include / intrman.h |
| mcserv.h | loadcore / include / loadcore.h |
| mcserv.h | sifman / include / sifman.h |
| mcserv.h | stdio / include / stdio.h |
| mcserv.h | sysclib / include / sysclib.h |
| mcserv.h | threadman / include / thbase.h |

---

## PS2SDK: iop/memorycard/mcserv/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000171_000537.html>

###### src → kernel Relation
| File in iop/memorycard/mcserv/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/network -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000172_000000.html>

###### network → common Relation
| File in iop/network | Includes file in common |
| netman / include / netdev.h | include / tamtypes.h |
| smap / include / smap_modular.h | include / tamtypes.h |
| spduart / src / spduart.c | include / speedregs.h |
| udptty / src / udptty.c | include / tamtypes.h |
| udptty / src / udptty.c | include / errno.h |
| netcnf / src / netcnf.c | include / errno.h |
| smap / src / smap.c | include / errno.h |
| smap / src / smap.c | include / smapregs.h |
| smap / src / smap.c | include / speedregs.h |
| smap / src / xfer.c | include / errno.h |
| smap / src / xfer.c | include / smapregs.h |
| smap / src / xfer.c | include / speedregs.h |
| smbman / src / smb.c | include / errno.h |
| smbman / src / smb.h | include / ps2smb.h |
| smbman / src / smb_fio.c | include / io_common.h |
| smbman / src / smb_fio.c | include / errno.h |
| smbman / src / smb_fio.c | include / ps2smb.h |
| netman / src / netdev.c | include / netman.h |
| netman / src / netman.c | include / errno.h |
| netman / src / netman.c | include / netman.h |
| netman / src / netman.c | include / netman_rpc.h |
| netman / src / rpc_client.c | include / errno.h |
| netman / src / rpc_client.c | include / netman.h |
| netman / src / rpc_client.c | include / netman_rpc.h |
| netman / src / rpc_server.c | include / errno.h |
| netman / src / rpc_server.c | include / netman.h |
| netman / src / rpc_server.c | include / netman_rpc.h |

---

## PS2SDK: iop/network -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000172_000056.html>

###### network → cdvd Relation
| File in iop/network | Includes file in iop/cdvd |
| netcnf / src / irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/network -&gt; dev9 Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000172_000087.html>

###### network → dev9 Relation
| File in iop/network | Includes file in iop/dev9 |
| smap / src / include / irx_imports.h | dev9 / include / dev9.h |
| spduart / src / irx_imports.h | dev9 / include / dev9.h |
| smap / src / smap.c | dev9 / include / dev9.h |
| smap / src / xfer.c | dev9 / include / dev9.h |

---

## PS2SDK: iop/network -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000172_000223.html>

###### network → system Relation
| File in iop/network | Includes file in iop/system |
| smap / src / include / irx_imports.h | intrman / include / intrman.h |
| smap / src / include / irx_imports.h | loadcore / include / loadcore.h |
| smap / src / include / irx_imports.h | stdio / include / stdio.h |
| smap / src / include / irx_imports.h | sysclib / include / sysclib.h |
| smap / src / include / irx_imports.h | threadman / include / thbase.h |
| smap / src / include / irx_imports.h | threadman / include / thevent.h |
| smap / src / include / main.h | threadman / include / thbase.h |
| spduart / src / irx_imports.h | intrman / include / intrman.h |
| spduart / src / irx_imports.h | ioman / include / ioman.h |
| spduart / src / irx_imports.h | loadcore / include / loadcore.h |
| spduart / src / irx_imports.h | stdio / include / stdio.h |
| spduart / src / irx_imports.h | sysclib / include / sysclib.h |
| spduart / src / irx_imports.h | threadman / include / thbase.h |
| spduart / src / irx_imports.h | threadman / include / thevent.h |
| spduart / src / spduart.c | sysclib / include / ctype.h |
| udptty / src / irx_imports.h | ioman / include / ioman.h |
| udptty / src / irx_imports.h | intrman / include / intrman.h |
| udptty / src / irx_imports.h | loadcore / include / loadcore.h |
| udptty / src / irx_imports.h | stdio / include / stdio.h |
| udptty / src / irx_imports.h | sysclib / include / sysclib.h |
| udptty / src / irx_imports.h | threadman / include / thbase.h |
| udptty / src / irx_imports.h | threadman / include / thevent.h |
| udptty / src / irx_imports.h | threadman / include / thsemap.h |
| udptty / src / udptty.c | loadcore / include / loadcore.h |
| udptty / src / udptty.c | stdio / include / stdio.h |
| udptty / src / udptty.c | threadman / include / thsemap.h |
| udptty / src / udptty.c | ioman / include / ioman.h |
| udptty / src / udptty.c | intrman / include / intrman.h |
| udptty / src / udptty.c | sysclib / include / sysclib.h |
| udptty / src / udptty.c | threadman / include / thbase.h |
| udptty / src / udptty.c | threadman / include / thevent.h |
| netcnfif / src / irx_imports.h | heaplib / include / heaplib.h |
| netcnfif / src / irx_imports.h | intrman / include / intrman.h |
| netcnfif / src / irx_imports.h | loadcore / include / loadcore.h |
| netcnfif / src / irx_imports.h | sifman / include / sifman.h |
| netcnfif / src / irx_imports.h | stdio / include / stdio.h |
| netcnfif / src / irx_imports.h | sysclib / include / sysclib.h |
| netcnfif / src / irx_imports.h | threadman / include / thbase.h |
| netcnf / src / irx_imports.h | heaplib / include / heaplib.h |
| netcnf / src / irx_imports.h | iomanx / include / iomanX.h |
| netcnf / src / irx_imports.h | loadcore / include / loadcore.h |
| netcnf / src / irx_imports.h | stdio / include / stdio.h |
| netcnf / src / irx_imports.h | sysclib / include / sysclib.h |
| netcnf / src / irx_imports.h | threadman / include / thbase.h |
| netcnf / src / irx_imports.h | threadman / include / thsemap.h |
| netcnf / src / netcnf.c | sysclib / include / ctype.h |
| netcnf / src / netcnf.c | stdio / include / stdio.h |
| smap / src / main.c | stdio / include / stdio.h |
| smap / src / main.c | loadcore / include / loadcore.h |
| smap / src / main.c | threadman / include / thbase.h |
| smap / src / smap.c | stdio / include / stdio.h |
| smap / src / smap.c | dmacman / include / dmacman.h |
| smap / src / smap.c | intrman / include / intrman.h |
| smap / src / smap.c | loadcore / include / loadcore.h |
| smap / src / smap.c | modload / include / modload.h |
| smap / src / smap.c | sysclib / include / sysclib.h |
| smap / src / smap.c | sysclib / include / ctype.h |
| smap / src / smap.c | threadman / include / thbase.h |
| smap / src / smap.c | threadman / include / thevent.h |
| smap / src / smap.c | threadman / include / thsemap.h |
| smap / src / xfer.c | stdio / include / stdio.h |
| smap / src / xfer.c | dmacman / include / dmacman.h |
| smap / src / xfer.c | intrman / include / intrman.h |
| smap / src / xfer.c | loadcore / include / loadcore.h |
| smap / src / xfer.c | modload / include / modload.h |
| smap / src / xfer.c | sysclib / include / sysclib.h |
| smap / src / xfer.c | threadman / include / thbase.h |
| smap / src / xfer.c | threadman / include / thevent.h |
| smap / src / xfer.c | threadman / include / thsemap.h |
| smbman / src / auth.c | stdio / include / stdio.h |
| smbman / src / auth.c | sysclib / include / sysclib.h |
| smbman / src / irx_imports.h | intrman / include / intrman.h |
| smbman / src / irx_imports.h | ioman / include / ioman.h |
| smbman / src / irx_imports.h | sifman / include / sifman.h |
| smbman / src / irx_imports.h | stdio / include / stdio.h |
| smbman / src / irx_imports.h | sysclib / include / sysclib.h |
| smbman / src / irx_imports.h | threadman / include / thbase.h |
| smbman / src / irx_imports.h | threadman / include / thsemap.h |
| smbman / src / poll.c | stdio / include / stdio.h |
| smbman / src / poll.c | sysclib / include / sysclib.h |
| smbman / src / smb.c | stdio / include / stdio.h |
| smbman / src / smb.c | sysclib / include / sysclib.h |
| smbman / src / smb.c | ioman / include / ioman.h |
| smbman / src / smb_fio.c | intrman / include / intrman.h |
| smbman / src / smb_fio.c | iomanx / include / iomanX.h |
| smbman / src / smb_fio.c | sifman / include / sifman.h |
| smbman / src / smb_fio.c | stdio / include / stdio.h |
| smbman / src / smb_fio.c | sysclib / include / sysclib.h |
| smbman / src / smb_fio.c | threadman / include / thbase.h |
| smbman / src / smb_fio.c | threadman / include / thsemap.h |
| smbman / src / smbman.c | iomanx / include / iomanX.h |
| smbman / src / smbman.c | loadcore / include / loadcore.h |
| smbman / src / smbman.c | stdio / include / stdio.h |
| smbman / src / smbman.c | sysclib / include / sysclib.h |
| an986 / src / an986.c | sysclib / include / ctype.h |
| an986 / src / irx_imports.h | intrman / include / intrman.h |
| an986 / src / irx_imports.h | loadcore / include / loadcore.h |
| an986 / src / irx_imports.h | stdio / include / stdio.h |
| an986 / src / irx_imports.h | sysclib / include / sysclib.h |
| an986 / src / irx_imports.h | threadman / include / thbase.h |
| an986 / src / irx_imports.h | threadman / include / thevent.h |
| netman / src / irx_imports.h | intrman / include / intrman.h |
| netman / src / irx_imports.h | loadcore / include / loadcore.h |
| netman / src / irx_imports.h | sifman / include / sifman.h |
| netman / src / irx_imports.h | stdio / include / stdio.h |
| netman / src / irx_imports.h | sysclib / include / sysclib.h |
| netman / src / irx_imports.h | threadman / include / thbase.h |
| netman / src / irx_imports.h | threadman / include / thevent.h |
| netman / src / irx_imports.h | threadman / include / thsemap.h |
| netman / src / netman.c | intrman / include / intrman.h |
| netman / src / netman.c | loadcore / include / loadcore.h |
| netman / src / netman.c | sysclib / include / sysclib.h |
| netman / src / netman.c | sifman / include / sifman.h |
| netman / src / netman.c | threadman / include / thevent.h |
| netman / src / netman.c | threadman / include / thsemap.h |
| netman / src / rpc_client.c | intrman / include / intrman.h |
| netman / src / rpc_client.c | sifman / include / sifman.h |
| netman / src / rpc_client.c | sysclib / include / sysclib.h |
| netman / src / rpc_client.c | threadman / include / thbase.h |
| netman / src / rpc_client.c | threadman / include / thevent.h |
| netman / src / rpc_client.c | threadman / include / thsemap.h |
| netman / src / rpc_server.c | stdio / include / stdio.h |
| netman / src / rpc_server.c | sysclib / include / sysclib.h |
| netman / src / rpc_server.c | sifman / include / sifman.h |
| netman / src / rpc_server.c | loadcore / include / loadcore.h |
| netman / src / rpc_server.c | threadman / include / thbase.h |
| netman / src / rpc_server.c | threadman / include / thevent.h |
| netman / src / rpc_server.c | threadman / include / thsemap.h |
| netman / src / rpc_server.c | intrman / include / intrman.h |

---

## PS2SDK: iop/network -&gt; tcpip Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000172_000284.html>

###### network → tcpip Relation
| File in iop/network | Includes file in iop/tcpip |
| netcnf / src / netcnf.c | tcpip-base / include / stdlib.h |

---

## PS2SDK: iop/network -&gt; usb Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000172_000291.html>

###### network → usb Relation
| File in iop/network | Includes file in iop/usb |
| an986 / src / an986.c | usbd / include / usbd_macro.h |
| an986 / src / irx_imports.h | usbd / include / usbd.h |

---

## PS2SDK: iop/network -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000172_000537.html>

###### network → kernel Relation
| File in iop/network | Includes file in iop/kernel |
| smap / src / include / irx_imports.h | include / irx.h |
| spduart / include / modem.h | include / irx.h |
| spduart / src / irx_imports.h | include / irx.h |
| udptty / src / irx_imports.h | include / irx.h |
| netcnfif / src / irx_imports.h | include / irx.h |
| netcnf / src / irx_imports.h | include / irx.h |
| smap / src / main.c | include / defs.h |
| smap / src / smap.c | include / defs.h |
| smap / src / smap.c | include / irx.h |
| smap / src / xfer.c | include / irx.h |
| smbman / src / auth.c | include / defs.h |
| smbman / src / auth.c | include / irx.h |
| smbman / src / irx_imports.h | include / irx.h |
| smbman / src / md4.c | include / defs.h |
| smbman / src / md4.c | include / irx.h |
| smbman / src / poll.c | include / defs.h |
| smbman / src / poll.c | include / irx.h |
| smbman / src / smb.c | include / irx.h |
| smbman / src / smb_fio.c | include / defs.h |
| smbman / src / smb_fio.c | include / irx.h |
| smbman / src / smbman.c | include / defs.h |
| smbman / src / smbman.c | include / irx.h |
| an986 / src / an986.c | include / kerr.h |
| an986 / src / irx_imports.h | include / irx.h |
| netman / src / irx_imports.h | include / irx.h |
| netman / src / netman.c | include / irx.h |

---

## PS2SDK: iop/network/an986 -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000173_000223.html>

###### an986 → system Relation
| File in iop/network/an986 | Includes file in iop/system |
| src / an986.c | sysclib / include / ctype.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thevent.h |

---

## PS2SDK: iop/network/an986 -&gt; usb Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000173_000291.html>

###### an986 → usb Relation
| File in iop/network/an986 | Includes file in iop/usb |
| src / an986.c | usbd / include / usbd_macro.h |
| src / irx_imports.h | usbd / include / usbd.h |

---

## PS2SDK: iop/network/an986 -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000173_000537.html>

###### an986 → kernel Relation
| File in iop/network/an986 | Includes file in iop/kernel |
| src / an986.c | include / kerr.h |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/network/an986/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000174_000223.html>

###### src → system Relation
| File in iop/network/an986/src | Includes file in iop/system |
| an986.c | sysclib / include / ctype.h |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thevent.h |

---

## PS2SDK: iop/network/an986/src -&gt; usb Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000174_000291.html>

###### src → usb Relation
| File in iop/network/an986/src | Includes file in iop/usb |
| an986.c | usbd / include / usbd_macro.h |
| irx_imports.h | usbd / include / usbd.h |

---

## PS2SDK: iop/network/an986/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000174_000537.html>

###### src → kernel Relation
| File in iop/network/an986/src | Includes file in iop/kernel |
| an986.c | include / kerr.h |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/network/netcnf -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000175_000000.html>

###### netcnf → common Relation
| File in iop/network/netcnf | Includes file in common |
| src / netcnf.c | include / errno.h |

---

## PS2SDK: iop/network/netcnf -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000175_000056.html>

###### netcnf → cdvd Relation
| File in iop/network/netcnf | Includes file in iop/cdvd |
| src / irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/network/netcnf -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000175_000223.html>

###### netcnf → system Relation
| File in iop/network/netcnf | Includes file in iop/system |
| src / irx_imports.h | heaplib / include / heaplib.h |
| src / irx_imports.h | iomanx / include / iomanX.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thsemap.h |
| src / netcnf.c | sysclib / include / ctype.h |
| src / netcnf.c | stdio / include / stdio.h |

---

## PS2SDK: iop/network/netcnf -&gt; tcpip Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000175_000284.html>

###### netcnf → tcpip Relation
| File in iop/network/netcnf | Includes file in iop/tcpip |
| src / netcnf.c | tcpip-base / include / stdlib.h |

---

## PS2SDK: iop/network/netcnf -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000175_000537.html>

###### netcnf → kernel Relation
| File in iop/network/netcnf | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/network/netcnf/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000176_000000.html>

###### src → common Relation
| File in iop/network/netcnf/src | Includes file in common |
| netcnf.c | include / errno.h |

---

## PS2SDK: iop/network/netcnf/src -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000176_000056.html>

###### src → cdvd Relation
| File in iop/network/netcnf/src | Includes file in iop/cdvd |
| irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/network/netcnf/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000176_000223.html>

###### src → system Relation
| File in iop/network/netcnf/src | Includes file in iop/system |
| irx_imports.h | heaplib / include / heaplib.h |
| irx_imports.h | iomanx / include / iomanX.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thsemap.h |
| netcnf.c | sysclib / include / ctype.h |
| netcnf.c | stdio / include / stdio.h |

---

## PS2SDK: iop/network/netcnf/src -&gt; tcpip Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000176_000284.html>

###### src → tcpip Relation
| File in iop/network/netcnf/src | Includes file in iop/tcpip |
| netcnf.c | tcpip-base / include / stdlib.h |

---

## PS2SDK: iop/network/netcnf/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000176_000537.html>

###### src → kernel Relation
| File in iop/network/netcnf/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/network/netcnfif -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000177_000223.html>

###### netcnfif → system Relation
| File in iop/network/netcnfif | Includes file in iop/system |
| src / irx_imports.h | heaplib / include / heaplib.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | sifman / include / sifman.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |

---

## PS2SDK: iop/network/netcnfif -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000177_000537.html>

###### netcnfif → kernel Relation
| File in iop/network/netcnfif | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/network/netcnfif/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000178_000223.html>

###### src → system Relation
| File in iop/network/netcnfif/src | Includes file in iop/system |
| irx_imports.h | heaplib / include / heaplib.h |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | sifman / include / sifman.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |

---

## PS2SDK: iop/network/netcnfif/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000178_000537.html>

###### src → kernel Relation
| File in iop/network/netcnfif/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/network/netman -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000179_000000.html>

###### netman → common Relation
| File in iop/network/netman | Includes file in common |
| include / netdev.h | include / tamtypes.h |
| src / netdev.c | include / netman.h |
| src / netman.c | include / errno.h |
| src / netman.c | include / netman.h |
| src / netman.c | include / netman_rpc.h |
| src / rpc_client.c | include / errno.h |
| src / rpc_client.c | include / netman.h |
| src / rpc_client.c | include / netman_rpc.h |
| src / rpc_server.c | include / errno.h |
| src / rpc_server.c | include / netman.h |
| src / rpc_server.c | include / netman_rpc.h |

---

## PS2SDK: iop/network/netman -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000179_000223.html>

###### netman → system Relation
| File in iop/network/netman | Includes file in iop/system |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | sifman / include / sifman.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thevent.h |
| src / irx_imports.h | threadman / include / thsemap.h |
| src / netman.c | intrman / include / intrman.h |
| src / netman.c | loadcore / include / loadcore.h |
| src / netman.c | sysclib / include / sysclib.h |
| src / netman.c | sifman / include / sifman.h |
| src / netman.c | threadman / include / thevent.h |
| src / netman.c | threadman / include / thsemap.h |
| src / rpc_client.c | intrman / include / intrman.h |
| src / rpc_client.c | sifman / include / sifman.h |
| src / rpc_client.c | sysclib / include / sysclib.h |
| src / rpc_client.c | threadman / include / thbase.h |
| src / rpc_client.c | threadman / include / thevent.h |
| src / rpc_client.c | threadman / include / thsemap.h |
| src / rpc_server.c | stdio / include / stdio.h |
| src / rpc_server.c | sysclib / include / sysclib.h |
| src / rpc_server.c | sifman / include / sifman.h |
| src / rpc_server.c | loadcore / include / loadcore.h |
| src / rpc_server.c | threadman / include / thbase.h |
| src / rpc_server.c | threadman / include / thevent.h |
| src / rpc_server.c | threadman / include / thsemap.h |
| src / rpc_server.c | intrman / include / intrman.h |

---

## PS2SDK: iop/network/netman -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000179_000537.html>

###### netman → kernel Relation
| File in iop/network/netman | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |
| src / netman.c | include / irx.h |

---

## PS2SDK: iop/network/netman/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000180_000000.html>

###### src → common Relation
| File in iop/network/netman/src | Includes file in common |
| netdev.c | include / netman.h |
| netman.c | include / errno.h |
| netman.c | include / netman.h |
| netman.c | include / netman_rpc.h |
| rpc_client.c | include / errno.h |
| rpc_client.c | include / netman.h |
| rpc_client.c | include / netman_rpc.h |
| rpc_server.c | include / errno.h |
| rpc_server.c | include / netman.h |
| rpc_server.c | include / netman_rpc.h |

---

## PS2SDK: iop/network/netman/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000180_000223.html>

###### src → system Relation
| File in iop/network/netman/src | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | sifman / include / sifman.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thevent.h |
| irx_imports.h | threadman / include / thsemap.h |
| netman.c | intrman / include / intrman.h |
| netman.c | loadcore / include / loadcore.h |
| netman.c | sifman / include / sifman.h |
| netman.c | sysclib / include / sysclib.h |
| netman.c | threadman / include / thevent.h |
| netman.c | threadman / include / thsemap.h |
| rpc_client.c | intrman / include / intrman.h |
| rpc_client.c | sifman / include / sifman.h |
| rpc_client.c | sysclib / include / sysclib.h |
| rpc_client.c | threadman / include / thbase.h |
| rpc_client.c | threadman / include / thevent.h |
| rpc_client.c | threadman / include / thsemap.h |
| rpc_server.c | intrman / include / intrman.h |
| rpc_server.c | loadcore / include / loadcore.h |
| rpc_server.c | sifman / include / sifman.h |
| rpc_server.c | stdio / include / stdio.h |
| rpc_server.c | sysclib / include / sysclib.h |
| rpc_server.c | threadman / include / thbase.h |
| rpc_server.c | threadman / include / thevent.h |
| rpc_server.c | threadman / include / thsemap.h |

---

## PS2SDK: iop/network/netman/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000180_000537.html>

###### src → kernel Relation
| File in iop/network/netman/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |
| netman.c | include / irx.h |

---

## PS2SDK: iop/network/smap -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000181_000000.html>

###### smap → common Relation
| File in iop/network/smap | Includes file in common |
| include / smap_modular.h | include / tamtypes.h |
| src / smap.c | include / errno.h |
| src / smap.c | include / smapregs.h |
| src / smap.c | include / speedregs.h |
| src / xfer.c | include / errno.h |
| src / xfer.c | include / smapregs.h |
| src / xfer.c | include / speedregs.h |

---

## PS2SDK: iop/network/smap -&gt; dev9 Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000181_000087.html>

###### smap → dev9 Relation
| File in iop/network/smap | Includes file in iop/dev9 |
| src / include / irx_imports.h | dev9 / include / dev9.h |
| src / smap.c | dev9 / include / dev9.h |
| src / xfer.c | dev9 / include / dev9.h |

---

## PS2SDK: iop/network/smap -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000181_000223.html>

###### smap → system Relation
| File in iop/network/smap | Includes file in iop/system |
| src / include / irx_imports.h | intrman / include / intrman.h |
| src / include / irx_imports.h | loadcore / include / loadcore.h |
| src / include / irx_imports.h | stdio / include / stdio.h |
| src / include / irx_imports.h | sysclib / include / sysclib.h |
| src / include / irx_imports.h | threadman / include / thbase.h |
| src / include / irx_imports.h | threadman / include / thevent.h |
| src / include / main.h | threadman / include / thbase.h |
| src / main.c | stdio / include / stdio.h |
| src / main.c | loadcore / include / loadcore.h |
| src / main.c | threadman / include / thbase.h |
| src / smap.c | stdio / include / stdio.h |
| src / smap.c | dmacman / include / dmacman.h |
| src / smap.c | intrman / include / intrman.h |
| src / smap.c | loadcore / include / loadcore.h |
| src / smap.c | modload / include / modload.h |
| src / smap.c | sysclib / include / sysclib.h |
| src / smap.c | sysclib / include / ctype.h |
| src / smap.c | threadman / include / thbase.h |
| src / smap.c | threadman / include / thevent.h |
| src / smap.c | threadman / include / thsemap.h |
| src / xfer.c | stdio / include / stdio.h |
| src / xfer.c | dmacman / include / dmacman.h |
| src / xfer.c | intrman / include / intrman.h |
| src / xfer.c | loadcore / include / loadcore.h |
| src / xfer.c | modload / include / modload.h |
| src / xfer.c | sysclib / include / sysclib.h |
| src / xfer.c | threadman / include / thbase.h |
| src / xfer.c | threadman / include / thevent.h |
| src / xfer.c | threadman / include / thsemap.h |

---

## PS2SDK: iop/network/smap -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000181_000537.html>

###### smap → kernel Relation
| File in iop/network/smap | Includes file in iop/kernel |
| src / include / irx_imports.h | include / irx.h |
| src / main.c | include / defs.h |
| src / smap.c | include / defs.h |
| src / smap.c | include / irx.h |
| src / xfer.c | include / irx.h |

---

## PS2SDK: iop/network/smap/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000182_000000.html>

###### src → common Relation
| File in iop/network/smap/src | Includes file in common |
| smap.c | include / errno.h |
| smap.c | include / smapregs.h |
| smap.c | include / speedregs.h |
| xfer.c | include / errno.h |
| xfer.c | include / smapregs.h |
| xfer.c | include / speedregs.h |

---

## PS2SDK: iop/network/smap/src -&gt; dev9 Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000182_000087.html>

###### src → dev9 Relation
| File in iop/network/smap/src | Includes file in iop/dev9 |
| include / irx_imports.h | dev9 / include / dev9.h |
| smap.c | dev9 / include / dev9.h |
| xfer.c | dev9 / include / dev9.h |

---

## PS2SDK: iop/network/smap/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000182_000223.html>

###### src → system Relation
| File in iop/network/smap/src | Includes file in iop/system |
| include / irx_imports.h | intrman / include / intrman.h |
| include / irx_imports.h | loadcore / include / loadcore.h |
| include / irx_imports.h | stdio / include / stdio.h |
| include / irx_imports.h | sysclib / include / sysclib.h |
| include / irx_imports.h | threadman / include / thbase.h |
| include / irx_imports.h | threadman / include / thevent.h |
| main.c | loadcore / include / loadcore.h |
| main.c | stdio / include / stdio.h |
| main.c | threadman / include / thbase.h |
| include / main.h | threadman / include / thbase.h |
| smap.c | sysclib / include / ctype.h |
| smap.c | dmacman / include / dmacman.h |
| smap.c | intrman / include / intrman.h |
| smap.c | loadcore / include / loadcore.h |
| smap.c | modload / include / modload.h |
| smap.c | stdio / include / stdio.h |
| smap.c | sysclib / include / sysclib.h |
| smap.c | threadman / include / thbase.h |
| smap.c | threadman / include / thevent.h |
| smap.c | threadman / include / thsemap.h |
| xfer.c | dmacman / include / dmacman.h |
| xfer.c | intrman / include / intrman.h |
| xfer.c | loadcore / include / loadcore.h |
| xfer.c | modload / include / modload.h |
| xfer.c | stdio / include / stdio.h |
| xfer.c | sysclib / include / sysclib.h |
| xfer.c | threadman / include / thbase.h |
| xfer.c | threadman / include / thevent.h |
| xfer.c | threadman / include / thsemap.h |

---

## PS2SDK: iop/network/smap/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000182_000537.html>

###### src → kernel Relation
| File in iop/network/smap/src | Includes file in iop/kernel |
| include / irx_imports.h | include / irx.h |
| main.c | include / defs.h |
| smap.c | include / defs.h |
| smap.c | include / irx.h |
| xfer.c | include / irx.h |

---

## PS2SDK: iop/network/smap/src/include -&gt; dev9 Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000183_000087.html>

###### include → dev9 Relation
| File in iop/network/smap/src/include | Includes file in iop/dev9 |
| irx_imports.h | dev9 / include / dev9.h |

---

## PS2SDK: iop/network/smap/src/include -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000183_000223.html>

###### include → system Relation
| File in iop/network/smap/src/include | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thevent.h |
| main.h | threadman / include / thbase.h |

---

## PS2SDK: iop/network/smap/src/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000183_000537.html>

###### include → kernel Relation
| File in iop/network/smap/src/include | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/network/smbman -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000184_000000.html>

###### smbman → common Relation
| File in iop/network/smbman | Includes file in common |
| src / smb.c | include / errno.h |
| src / smb.h | include / ps2smb.h |
| src / smb_fio.c | include / io_common.h |
| src / smb_fio.c | include / errno.h |
| src / smb_fio.c | include / ps2smb.h |

---

## PS2SDK: iop/network/smbman -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000184_000223.html>

###### smbman → system Relation
| File in iop/network/smbman | Includes file in iop/system |
| src / auth.c | stdio / include / stdio.h |
| src / auth.c | sysclib / include / sysclib.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | ioman / include / ioman.h |
| src / irx_imports.h | sifman / include / sifman.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thsemap.h |
| src / poll.c | stdio / include / stdio.h |
| src / poll.c | sysclib / include / sysclib.h |
| src / smb.c | stdio / include / stdio.h |
| src / smb.c | sysclib / include / sysclib.h |
| src / smb.c | ioman / include / ioman.h |
| src / smb_fio.c | intrman / include / intrman.h |
| src / smb_fio.c | iomanx / include / iomanX.h |
| src / smb_fio.c | sifman / include / sifman.h |
| src / smb_fio.c | stdio / include / stdio.h |
| src / smb_fio.c | sysclib / include / sysclib.h |
| src / smb_fio.c | threadman / include / thbase.h |
| src / smb_fio.c | threadman / include / thsemap.h |
| src / smbman.c | iomanx / include / iomanX.h |
| src / smbman.c | loadcore / include / loadcore.h |
| src / smbman.c | stdio / include / stdio.h |
| src / smbman.c | sysclib / include / sysclib.h |

---

## PS2SDK: iop/network/smbman -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000184_000537.html>

###### smbman → kernel Relation
| File in iop/network/smbman | Includes file in iop/kernel |
| src / auth.c | include / defs.h |
| src / auth.c | include / irx.h |
| src / irx_imports.h | include / irx.h |
| src / md4.c | include / defs.h |
| src / md4.c | include / irx.h |
| src / poll.c | include / defs.h |
| src / poll.c | include / irx.h |
| src / smb.c | include / irx.h |
| src / smb_fio.c | include / defs.h |
| src / smb_fio.c | include / irx.h |
| src / smbman.c | include / defs.h |
| src / smbman.c | include / irx.h |

---

## PS2SDK: iop/network/smbman/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000185_000000.html>

###### src → common Relation
| File in iop/network/smbman/src | Includes file in common |
| smb.c | include / errno.h |
| smb.h | include / ps2smb.h |
| smb_fio.c | include / errno.h |
| smb_fio.c | include / io_common.h |
| smb_fio.c | include / ps2smb.h |

---

## PS2SDK: iop/network/smbman/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000185_000223.html>

###### src → system Relation
| File in iop/network/smbman/src | Includes file in iop/system |
| auth.c | stdio / include / stdio.h |
| auth.c | sysclib / include / sysclib.h |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | ioman / include / ioman.h |
| irx_imports.h | sifman / include / sifman.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thsemap.h |
| poll.c | stdio / include / stdio.h |
| poll.c | sysclib / include / sysclib.h |
| smb.c | ioman / include / ioman.h |
| smb.c | stdio / include / stdio.h |
| smb.c | sysclib / include / sysclib.h |
| smb_fio.c | intrman / include / intrman.h |
| smb_fio.c | iomanx / include / iomanX.h |
| smb_fio.c | sifman / include / sifman.h |
| smb_fio.c | stdio / include / stdio.h |
| smb_fio.c | sysclib / include / sysclib.h |
| smb_fio.c | threadman / include / thbase.h |
| smb_fio.c | threadman / include / thsemap.h |
| smbman.c | iomanx / include / iomanX.h |
| smbman.c | loadcore / include / loadcore.h |
| smbman.c | stdio / include / stdio.h |
| smbman.c | sysclib / include / sysclib.h |

---

## PS2SDK: iop/network/smbman/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000185_000537.html>

###### src → kernel Relation
| File in iop/network/smbman/src | Includes file in iop/kernel |
| auth.c | include / defs.h |
| auth.c | include / irx.h |
| irx_imports.h | include / irx.h |
| md4.c | include / defs.h |
| md4.c | include / irx.h |
| poll.c | include / defs.h |
| poll.c | include / irx.h |
| smb.c | include / irx.h |
| smb_fio.c | include / defs.h |
| smb_fio.c | include / irx.h |
| smbman.c | include / defs.h |
| smbman.c | include / irx.h |

---

## PS2SDK: iop/network/spduart -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000186_000000.html>

###### spduart → common Relation
| File in iop/network/spduart | Includes file in common |
| src / spduart.c | include / speedregs.h |

---

## PS2SDK: iop/network/spduart -&gt; dev9 Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000186_000087.html>

###### spduart → dev9 Relation
| File in iop/network/spduart | Includes file in iop/dev9 |
| src / irx_imports.h | dev9 / include / dev9.h |

---

## PS2SDK: iop/network/spduart -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000186_000223.html>

###### spduart → system Relation
| File in iop/network/spduart | Includes file in iop/system |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | ioman / include / ioman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thevent.h |
| src / spduart.c | sysclib / include / ctype.h |

---

## PS2SDK: iop/network/spduart -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000186_000537.html>

###### spduart → kernel Relation
| File in iop/network/spduart | Includes file in iop/kernel |
| include / modem.h | include / irx.h |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/network/spduart/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000187_000000.html>

###### src → common Relation
| File in iop/network/spduart/src | Includes file in common |
| spduart.c | include / speedregs.h |

---

## PS2SDK: iop/network/spduart/src -&gt; dev9 Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000187_000087.html>

###### src → dev9 Relation
| File in iop/network/spduart/src | Includes file in iop/dev9 |
| irx_imports.h | dev9 / include / dev9.h |

---

## PS2SDK: iop/network/spduart/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000187_000223.html>

###### src → system Relation
| File in iop/network/spduart/src | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | ioman / include / ioman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thevent.h |
| spduart.c | sysclib / include / ctype.h |

---

## PS2SDK: iop/network/spduart/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000187_000537.html>

###### src → kernel Relation
| File in iop/network/spduart/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/network/spduart/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000187_000546.html>

###### src → include Relation
| File in iop/network/spduart/src | Includes file in iop/network/spduart/include |
| irx_imports.h | modem.h |

---

## PS2SDK: iop/network/udptty -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000188_000000.html>

###### udptty → common Relation
| File in iop/network/udptty | Includes file in common |
| src / udptty.c | include / errno.h |
| src / udptty.c | include / tamtypes.h |

---

## PS2SDK: iop/network/udptty -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000188_000223.html>

###### udptty → system Relation
| File in iop/network/udptty | Includes file in iop/system |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | ioman / include / ioman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thevent.h |
| src / irx_imports.h | threadman / include / thsemap.h |
| src / udptty.c | intrman / include / intrman.h |
| src / udptty.c | ioman / include / ioman.h |
| src / udptty.c | loadcore / include / loadcore.h |
| src / udptty.c | stdio / include / stdio.h |
| src / udptty.c | sysclib / include / sysclib.h |
| src / udptty.c | threadman / include / thbase.h |
| src / udptty.c | threadman / include / thevent.h |
| src / udptty.c | threadman / include / thsemap.h |

---

## PS2SDK: iop/network/udptty -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000188_000537.html>

###### udptty → kernel Relation
| File in iop/network/udptty | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/network/udptty/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000189_000000.html>

###### src → common Relation
| File in iop/network/udptty/src | Includes file in common |
| udptty.c | include / errno.h |
| udptty.c | include / tamtypes.h |

---

## PS2SDK: iop/network/udptty/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000189_000223.html>

###### src → system Relation
| File in iop/network/udptty/src | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | ioman / include / ioman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thevent.h |
| irx_imports.h | threadman / include / thsemap.h |
| udptty.c | intrman / include / intrman.h |
| udptty.c | ioman / include / ioman.h |
| udptty.c | loadcore / include / loadcore.h |
| udptty.c | stdio / include / stdio.h |
| udptty.c | sysclib / include / sysclib.h |
| udptty.c | threadman / include / thbase.h |
| udptty.c | threadman / include / thevent.h |
| udptty.c | threadman / include / thsemap.h |

---

## PS2SDK: iop/network/udptty/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000189_000537.html>

###### src → kernel Relation
| File in iop/network/udptty/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/security -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000190_000000.html>

###### security → common Relation
| File in iop/security | Includes file in common |
| secrman / include / secrman.h | include / libsecr-common.h |

---

## PS2SDK: iop/security -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000190_000056.html>

###### security → cdvd Relation
| File in iop/security | Includes file in iop/cdvd |
| secrman / src / irx_imports.h | cdvdman / include / cdvdman.h |
| secrman / src / MechaAuth.c | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/security -&gt; memorycard Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000190_000167.html>

###### security → memorycard Relation
| File in iop/security | Includes file in iop/memorycard |
| daemon / src / irx_imports.h | mcman / include / mcman.h |

---

## PS2SDK: iop/security -&gt; mcman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000190_000168.html>

###### security → mcman Relation
| File in iop/security | Includes file in iop/memorycard/mcman |
| daemon / src / irx_imports.h | include / mcman.h |

---

## PS2SDK: iop/security -&gt; sio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000190_000197.html>

###### security → sio Relation
| File in iop/security | Includes file in iop/sio |
| secrman / include / secrman.h | sio2man / include / sio2man.h |
| secrman / src / secrman.c | sio2man / include / sio2man.h |

---

## PS2SDK: iop/security -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000190_000223.html>

###### security → system Relation
| File in iop/security | Includes file in iop/system |
| secrsif / src / irx_imports.h | loadcore / include / loadcore.h |
| secrsif / src / irx_imports.h | sifman / include / sifman.h |
| secrsif / src / irx_imports.h | stdio / include / stdio.h |
| secrsif / src / irx_imports.h | threadman / include / thbase.h |
| secrsif / src / secrsif.c | loadcore / include / loadcore.h |
| secrsif / src / secrsif.c | stdio / include / stdio.h |
| secrsif / src / secrsif.c | sysclib / include / sysclib.h |
| secrsif / src / secrsif.c | threadman / include / thbase.h |
| secrsif / src / secrsif.c | sifman / include / sifman.h |
| secrman / src / CardAuth.c | stdio / include / stdio.h |
| secrman / src / CardAuth.c | sysclib / include / sysclib.h |
| secrman / src / irx_imports.h | ioman / include / ioman.h |
| secrman / src / irx_imports.h | loadcore / include / loadcore.h |
| secrman / src / irx_imports.h | modload / include / modload.h |
| secrman / src / irx_imports.h | stdio / include / stdio.h |
| secrman / src / irx_imports.h | sysclib / include / sysclib.h |
| secrman / src / keyman.c | stdio / include / stdio.h |
| secrman / src / keyman.c | sysclib / include / sysclib.h |
| secrman / src / MechaAuth.c | stdio / include / stdio.h |
| secrman / src / MechaAuth.c | sysclib / include / sysclib.h |
| secrman / src / secrman.c | loadcore / include / loadcore.h |
| secrman / src / secrman.c | ioman / include / ioman.h |
| secrman / src / secrman.c | modload / include / modload.h |
| secrman / src / secrman.c | stdio / include / stdio.h |
| secrman / src / secrman.c | sysclib / include / sysclib.h |
| daemon / src / irx_imports.h | intrman / include / intrman.h |
| daemon / src / irx_imports.h | stdio / include / stdio.h |
| daemon / src / irx_imports.h | threadman / include / thbase.h |

---

## PS2SDK: iop/security -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000190_000537.html>

###### security → kernel Relation
| File in iop/security | Includes file in iop/kernel |
| secrman / include / secrman.h | include / irx.h |
| secrsif / src / irx_imports.h | include / irx.h |
| secrsif / src / secrsif.c | include / irx.h |
| secrman / src / irx_imports.h | include / irx.h |
| secrman / src / secrman.c | include / irx.h |
| daemon / src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/security -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000190_000542.html>

###### security → include Relation
| File in iop/security | Includes file in iop/memorycard/mcman/include |
| daemon / src / irx_imports.h | mcman.h |

---

## PS2SDK: iop/security/daemon -&gt; memorycard Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000191_000167.html>

###### daemon → memorycard Relation
| File in iop/security/daemon | Includes file in iop/memorycard |
| src / irx_imports.h | mcman / include / mcman.h |

---

## PS2SDK: iop/security/daemon -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000191_000223.html>

###### daemon → system Relation
| File in iop/security/daemon | Includes file in iop/system |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | threadman / include / thbase.h |

---

## PS2SDK: iop/security/daemon -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000191_000537.html>

###### daemon → kernel Relation
| File in iop/security/daemon | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/security/daemon/src -&gt; memorycard Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000192_000167.html>

###### src → memorycard Relation
| File in iop/security/daemon/src | Includes file in iop/memorycard |
| irx_imports.h | mcman / include / mcman.h |

---

## PS2SDK: iop/security/daemon/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000192_000223.html>

###### src → system Relation
| File in iop/security/daemon/src | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | threadman / include / thbase.h |

---

## PS2SDK: iop/security/daemon/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000192_000537.html>

###### src → kernel Relation
| File in iop/security/daemon/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/security/secrman -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000193_000000.html>

###### secrman → common Relation
| File in iop/security/secrman | Includes file in common |
| include / secrman.h | include / libsecr-common.h |

---

## PS2SDK: iop/security/secrman -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000193_000056.html>

###### secrman → cdvd Relation
| File in iop/security/secrman | Includes file in iop/cdvd |
| src / irx_imports.h | cdvdman / include / cdvdman.h |
| src / MechaAuth.c | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/security/secrman -&gt; sio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000193_000197.html>

###### secrman → sio Relation
| File in iop/security/secrman | Includes file in iop/sio |
| include / secrman.h | sio2man / include / sio2man.h |
| src / secrman.c | sio2man / include / sio2man.h |

---

## PS2SDK: iop/security/secrman -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000193_000223.html>

###### secrman → system Relation
| File in iop/security/secrman | Includes file in iop/system |
| src / CardAuth.c | stdio / include / stdio.h |
| src / CardAuth.c | sysclib / include / sysclib.h |
| src / irx_imports.h | ioman / include / ioman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | modload / include / modload.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / keyman.c | stdio / include / stdio.h |
| src / keyman.c | sysclib / include / sysclib.h |
| src / MechaAuth.c | stdio / include / stdio.h |
| src / MechaAuth.c | sysclib / include / sysclib.h |
| src / secrman.c | loadcore / include / loadcore.h |
| src / secrman.c | ioman / include / ioman.h |
| src / secrman.c | modload / include / modload.h |
| src / secrman.c | stdio / include / stdio.h |
| src / secrman.c | sysclib / include / sysclib.h |

---

## PS2SDK: iop/security/secrman -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000193_000537.html>

###### secrman → kernel Relation
| File in iop/security/secrman | Includes file in iop/kernel |
| include / secrman.h | include / irx.h |
| src / irx_imports.h | include / irx.h |
| src / secrman.c | include / irx.h |

---

## PS2SDK: iop/security/secrman/src -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000194_000056.html>

###### src → cdvd Relation
| File in iop/security/secrman/src | Includes file in iop/cdvd |
| irx_imports.h | cdvdman / include / cdvdman.h |
| MechaAuth.c | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/security/secrman/src -&gt; sio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000194_000197.html>

###### src → sio Relation
| File in iop/security/secrman/src | Includes file in iop/sio |
| secrman.c | sio2man / include / sio2man.h |

---

## PS2SDK: iop/security/secrman/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000194_000223.html>

###### src → system Relation
| File in iop/security/secrman/src | Includes file in iop/system |
| CardAuth.c | stdio / include / stdio.h |
| CardAuth.c | sysclib / include / sysclib.h |
| irx_imports.h | ioman / include / ioman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | modload / include / modload.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| keyman.c | stdio / include / stdio.h |
| keyman.c | sysclib / include / sysclib.h |
| MechaAuth.c | stdio / include / stdio.h |
| MechaAuth.c | sysclib / include / sysclib.h |
| secrman.c | ioman / include / ioman.h |
| secrman.c | loadcore / include / loadcore.h |
| secrman.c | modload / include / modload.h |
| secrman.c | stdio / include / stdio.h |
| secrman.c | sysclib / include / sysclib.h |

---

## PS2SDK: iop/security/secrman/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000194_000537.html>

###### src → kernel Relation
| File in iop/security/secrman/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |
| secrman.c | include / irx.h |

---

## PS2SDK: iop/security/secrman/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000194_000547.html>

###### src → include Relation
| File in iop/security/secrman/src | Includes file in iop/security/secrman/include |
| CardAuth.c | secrman.h |
| keyman.c | secrman.h |
| MechaAuth.c | secrman.h |
| secrman.c | secrman.h |

---

## PS2SDK: iop/security/secrsif -&gt; secrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000195_000193.html>

###### secrsif → secrman Relation
| File in iop/security/secrsif | Includes file in iop/security/secrman |
| src / irx_imports.h | include / secrman.h |
| src / secrsif.c | include / secrman.h |

---

## PS2SDK: iop/security/secrsif -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000195_000223.html>

###### secrsif → system Relation
| File in iop/security/secrsif | Includes file in iop/system |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | sifman / include / sifman.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / secrsif.c | loadcore / include / loadcore.h |
| src / secrsif.c | stdio / include / stdio.h |
| src / secrsif.c | sysclib / include / sysclib.h |
| src / secrsif.c | threadman / include / thbase.h |
| src / secrsif.c | sifman / include / sifman.h |

---

## PS2SDK: iop/security/secrsif -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000195_000537.html>

###### secrsif → kernel Relation
| File in iop/security/secrsif | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |
| src / secrsif.c | include / irx.h |

---

## PS2SDK: iop/security/secrsif/src -&gt; secrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000196_000193.html>

###### src → secrman Relation
| File in iop/security/secrsif/src | Includes file in iop/security/secrman |
| irx_imports.h | include / secrman.h |
| secrsif.c | include / secrman.h |

---

## PS2SDK: iop/security/secrsif/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000196_000223.html>

###### src → system Relation
| File in iop/security/secrsif/src | Includes file in iop/system |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | sifman / include / sifman.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | threadman / include / thbase.h |
| secrsif.c | loadcore / include / loadcore.h |
| secrsif.c | sifman / include / sifman.h |
| secrsif.c | stdio / include / stdio.h |
| secrsif.c | sysclib / include / sysclib.h |
| secrsif.c | threadman / include / thbase.h |

---

## PS2SDK: iop/security/secrsif/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000196_000537.html>

###### src → kernel Relation
| File in iop/security/secrsif/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |
| secrsif.c | include / irx.h |

---

## PS2SDK: iop/sio -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000197_000000.html>

###### sio → common Relation
| File in iop/sio | Includes file in common |
| mx4sio_bd / src / spi_sdcard_crc7.h | include / tamtypes.h |
| sio2man / src / sio2man.c | include / iop_mmio_hwport.h |

---

## PS2SDK: iop/sio -&gt; fs Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000197_000113.html>

###### sio → fs Relation
| File in iop/sio | Includes file in iop/fs |
| mx4sio_bd / src / irx_imports.h | bdm / include / bdm.h |
| mx4sio_bd / src / mx4sio.c | bdm / include / bdm.h |
| mx4sio_bd / src / spi_sdcard_driver.c | bdm / include / bdm.h |
| mx4sio_bd / src / spi_sdcard_driver.h | bdm / include / bdm.h |

---

## PS2SDK: iop/sio -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000197_000223.html>

###### sio → system Relation
| File in iop/sio | Includes file in iop/system |
| mx4sio_bd / src / ioplib.c | intrman / include / intrman.h |
| mx4sio_bd / src / ioplib.h | loadcore / include / loadcore.h |
| mx4sio_bd / src / irx_imports.h | dmacman / include / dmacman.h |
| mx4sio_bd / src / irx_imports.h | intrman / include / intrman.h |
| mx4sio_bd / src / irx_imports.h | loadcore / include / loadcore.h |
| mx4sio_bd / src / irx_imports.h | stdio / include / stdio.h |
| mx4sio_bd / src / irx_imports.h | sysclib / include / sysclib.h |
| mx4sio_bd / src / irx_imports.h | threadman / include / thbase.h |
| mx4sio_bd / src / irx_imports.h | threadman / include / thevent.h |
| mx4sio_bd / src / irx_imports.h | threadman / include / thsemap.h |
| mx4sio_bd / src / module_debug.h | stdio / include / stdio.h |
| mx4sio_bd / src / mx4sio.c | dmacman / include / dmacman.h |
| mx4sio_bd / src / mx4sio.c | intrman / include / intrman.h |
| mx4sio_bd / src / mx4sio.c | loadcore / include / loadcore.h |
| mx4sio_bd / src / mx4sio.c | threadman / include / thbase.h |
| mx4sio_bd / src / mx4sio.c | threadman / include / thevent.h |
| mx4sio_bd / src / mx4sio.c | threadman / include / thsemap.h |
| mx4sio_bd / src / sio2man_hook.c | stdio / include / stdio.h |
| mx4sio_bd / src / sio2man_hook.c | threadman / include / thsemap.h |
| mx4sio_bd / src / sio2man_hook.c | intrman / include / intrman.h |
| mx4sio_bd / src / spi_sdcard_driver.c | threadman / include / thevent.h |
| mx4sio_bd / src / spi_sdcard_driver.c | threadman / include / thbase.h |
| mx4sio_bd / src / spi_sdcard_driver_config.h | stdio / include / stdio.h |
| sio2man / src / irx_imports.h | dmacman / include / dmacman.h |
| sio2man / src / irx_imports.h | intrman / include / intrman.h |
| sio2man / src / irx_imports.h | loadcore / include / loadcore.h |
| sio2man / src / irx_imports.h | threadman / include / thsemap.h |
| mtapman / src / freemtap.c | stdio / include / stdio.h |
| mtapman / src / freemtap.c | loadcore / include / loadcore.h |
| mtapman / src / freemtap.c | threadman / include / thevent.h |
| mtapman / src / freemtap.c | threadman / include / thbase.h |
| mtapman / src / irx_imports.h | loadcore / include / loadcore.h |
| mtapman / src / irx_imports.h | sifman / include / sifman.h |
| mtapman / src / irx_imports.h | stdio / include / stdio.h |
| mtapman / src / irx_imports.h | threadman / include / thbase.h |
| mtapman / src / irx_imports.h | threadman / include / thevent.h |
| mtapman / src / rpcservers.c | stdio / include / stdio.h |
| mtapman / src / rpcservers.c | sifman / include / sifman.h |
| mtapman / src / rpcservers.c | threadman / include / thbase.h |

---

## PS2SDK: iop/sio -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000197_000537.html>

###### sio → kernel Relation
| File in iop/sio | Includes file in iop/kernel |
| sio2man / include / sio2man.h | include / irx.h |
| mtapman / include / xmtapman.h | include / irx.h |
| mx4sio_bd / src / irx_imports.h | include / irx.h |
| sio2man / src / irx_imports.h | include / irx.h |
| mtapman / src / freemtap.c | include / irx.h |
| mtapman / src / irx_imports.h | include / irx.h |
| mtapman / src / rpcservers.c | include / irx.h |

---

## PS2SDK: iop/sio/mtapman -&gt; sio2man Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000198_000202.html>

###### mtapman → sio2man Relation
| File in iop/sio/mtapman | Includes file in iop/sio/sio2man |
| src / freemtap.c | include / xsio2man.h |
| src / irx_imports.h | include / xsio2man.h |

---

## PS2SDK: iop/sio/mtapman -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000198_000223.html>

###### mtapman → system Relation
| File in iop/sio/mtapman | Includes file in iop/system |
| src / freemtap.c | stdio / include / stdio.h |
| src / freemtap.c | loadcore / include / loadcore.h |
| src / freemtap.c | threadman / include / thevent.h |
| src / freemtap.c | threadman / include / thbase.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | sifman / include / sifman.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thevent.h |
| src / rpcservers.c | stdio / include / stdio.h |
| src / rpcservers.c | sifman / include / sifman.h |
| src / rpcservers.c | threadman / include / thbase.h |

---

## PS2SDK: iop/sio/mtapman -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000198_000537.html>

###### mtapman → kernel Relation
| File in iop/sio/mtapman | Includes file in iop/kernel |
| include / xmtapman.h | include / irx.h |
| src / freemtap.c | include / irx.h |
| src / irx_imports.h | include / irx.h |
| src / rpcservers.c | include / irx.h |

---

## PS2SDK: iop/sio/mtapman/src -&gt; sio2man Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000199_000202.html>

###### src → sio2man Relation
| File in iop/sio/mtapman/src | Includes file in iop/sio/sio2man |
| freemtap.c | include / xsio2man.h |
| irx_imports.h | include / xsio2man.h |

---

## PS2SDK: iop/sio/mtapman/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000199_000223.html>

###### src → system Relation
| File in iop/sio/mtapman/src | Includes file in iop/system |
| freemtap.c | loadcore / include / loadcore.h |
| freemtap.c | stdio / include / stdio.h |
| freemtap.c | threadman / include / thbase.h |
| freemtap.c | threadman / include / thevent.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | sifman / include / sifman.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thevent.h |
| rpcservers.c | sifman / include / sifman.h |
| rpcservers.c | stdio / include / stdio.h |
| rpcservers.c | threadman / include / thbase.h |

---

## PS2SDK: iop/sio/mtapman/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000199_000537.html>

###### src → kernel Relation
| File in iop/sio/mtapman/src | Includes file in iop/kernel |
| freemtap.c | include / irx.h |
| irx_imports.h | include / irx.h |
| rpcservers.c | include / irx.h |

---

## PS2SDK: iop/sio/mx4sio_bd -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000200_000000.html>

###### mx4sio_bd → common Relation
| File in iop/sio/mx4sio_bd | Includes file in common |
| src / spi_sdcard_crc7.h | include / tamtypes.h |

---

## PS2SDK: iop/sio/mx4sio_bd -&gt; fs Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000200_000113.html>

###### mx4sio_bd → fs Relation
| File in iop/sio/mx4sio_bd | Includes file in iop/fs |
| src / irx_imports.h | bdm / include / bdm.h |
| src / mx4sio.c | bdm / include / bdm.h |
| src / spi_sdcard_driver.c | bdm / include / bdm.h |
| src / spi_sdcard_driver.h | bdm / include / bdm.h |

---

## PS2SDK: iop/sio/mx4sio_bd -&gt; sio2man Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000200_000202.html>

###### mx4sio_bd → sio2man Relation
| File in iop/sio/mx4sio_bd | Includes file in iop/sio/sio2man |
| src / mx4sio.c | include / xsio2man.h |
| src / sio2man_hook.c | include / sio2man.h |

---

## PS2SDK: iop/sio/mx4sio_bd -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000200_000223.html>

###### mx4sio_bd → system Relation
| File in iop/sio/mx4sio_bd | Includes file in iop/system |
| src / ioplib.c | intrman / include / intrman.h |
| src / ioplib.h | loadcore / include / loadcore.h |
| src / irx_imports.h | dmacman / include / dmacman.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thevent.h |
| src / irx_imports.h | threadman / include / thsemap.h |
| src / module_debug.h | stdio / include / stdio.h |
| src / mx4sio.c | dmacman / include / dmacman.h |
| src / mx4sio.c | intrman / include / intrman.h |
| src / mx4sio.c | loadcore / include / loadcore.h |
| src / mx4sio.c | threadman / include / thbase.h |
| src / mx4sio.c | threadman / include / thevent.h |
| src / mx4sio.c | threadman / include / thsemap.h |
| src / sio2man_hook.c | stdio / include / stdio.h |
| src / sio2man_hook.c | threadman / include / thsemap.h |
| src / sio2man_hook.c | intrman / include / intrman.h |
| src / spi_sdcard_driver.c | threadman / include / thevent.h |
| src / spi_sdcard_driver.c | threadman / include / thbase.h |
| src / spi_sdcard_driver_config.h | stdio / include / stdio.h |

---

## PS2SDK: iop/sio/mx4sio_bd -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000200_000537.html>

###### mx4sio_bd → kernel Relation
| File in iop/sio/mx4sio_bd | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/sio/mx4sio_bd/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000201_000000.html>

###### src → common Relation
| File in iop/sio/mx4sio_bd/src | Includes file in common |
| spi_sdcard_crc7.h | include / tamtypes.h |

---

## PS2SDK: iop/sio/mx4sio_bd/src -&gt; fs Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000201_000113.html>

###### src → fs Relation
| File in iop/sio/mx4sio_bd/src | Includes file in iop/fs |
| irx_imports.h | bdm / include / bdm.h |
| mx4sio.c | bdm / include / bdm.h |
| spi_sdcard_driver.c | bdm / include / bdm.h |
| spi_sdcard_driver.h | bdm / include / bdm.h |

---

## PS2SDK: iop/sio/mx4sio_bd/src -&gt; sio2man Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000201_000202.html>

###### src → sio2man Relation
| File in iop/sio/mx4sio_bd/src | Includes file in iop/sio/sio2man |
| mx4sio.c | include / xsio2man.h |
| sio2man_hook.c | include / sio2man.h |

---

## PS2SDK: iop/sio/mx4sio_bd/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000201_000223.html>

###### src → system Relation
| File in iop/sio/mx4sio_bd/src | Includes file in iop/system |
| ioplib.c | intrman / include / intrman.h |
| ioplib.h | loadcore / include / loadcore.h |
| irx_imports.h | dmacman / include / dmacman.h |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thevent.h |
| irx_imports.h | threadman / include / thsemap.h |
| module_debug.h | stdio / include / stdio.h |
| mx4sio.c | dmacman / include / dmacman.h |
| mx4sio.c | intrman / include / intrman.h |
| mx4sio.c | loadcore / include / loadcore.h |
| mx4sio.c | threadman / include / thbase.h |
| mx4sio.c | threadman / include / thevent.h |
| mx4sio.c | threadman / include / thsemap.h |
| sio2man_hook.c | intrman / include / intrman.h |
| sio2man_hook.c | stdio / include / stdio.h |
| sio2man_hook.c | threadman / include / thsemap.h |
| spi_sdcard_driver.c | threadman / include / thbase.h |
| spi_sdcard_driver.c | threadman / include / thevent.h |
| spi_sdcard_driver_config.h | stdio / include / stdio.h |

---

## PS2SDK: iop/sio/mx4sio_bd/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000201_000537.html>

###### src → kernel Relation
| File in iop/sio/mx4sio_bd/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/sio/sio2man -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000202_000000.html>

###### sio2man → common Relation
| File in iop/sio/sio2man | Includes file in common |
| src / sio2man.c | include / iop_mmio_hwport.h |

---

## PS2SDK: iop/sio/sio2man -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000202_000223.html>

###### sio2man → system Relation
| File in iop/sio/sio2man | Includes file in iop/system |
| src / irx_imports.h | dmacman / include / dmacman.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | threadman / include / thsemap.h |

---

## PS2SDK: iop/sio/sio2man -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000202_000537.html>

###### sio2man → kernel Relation
| File in iop/sio/sio2man | Includes file in iop/kernel |
| include / sio2man.h | include / irx.h |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/sio/sio2man/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000203_000000.html>

###### src → common Relation
| File in iop/sio/sio2man/src | Includes file in common |
| sio2man.c | include / iop_mmio_hwport.h |

---

## PS2SDK: iop/sio/sio2man/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000203_000223.html>

###### src → system Relation
| File in iop/sio/sio2man/src | Includes file in iop/system |
| irx_imports.h | dmacman / include / dmacman.h |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | threadman / include / thsemap.h |

---

## PS2SDK: iop/sio/sio2man/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000203_000537.html>

###### src → kernel Relation
| File in iop/sio/sio2man/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/sio/sio2man/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000203_000549.html>

###### src → include Relation
| File in iop/sio/sio2man/src | Includes file in iop/sio/sio2man/include |
| sio2man.c | rsio2man.h |

---

## PS2SDK: iop/sound -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000204_000000.html>

###### sound → common Relation
| File in iop/sound | Includes file in common |
| libsd / include / libsd.h | include / libsd-common.h |
| libsnd2 / src / include / libsnd2_internal.h | include / tamtypes.h |
| libspu2 / include / libspu2_internal.h | include / tamtypes.h |
| rspu2drv / src / include / rs_i.h | include / tamtypes.h |
| sdrdrv / include / sdrdrv.h | include / libsdr-common.h |
| sdrdrv / src / sdr_i.h | include / libsdr-common.h |
| ps2snd / src / adpcm-stream.c | include / ps2snd.h |
| ps2snd / src / ps2snd.c | include / ps2snd.h |

---

## PS2SDK: iop/sound -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000204_000056.html>

###### sound → cdvd Relation
| File in iop/sound | Includes file in iop/cdvd |
| audsrv / src / cdrom.c | cdvdman / include / cdvdman.h |
| audsrv / src / irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/sound -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000204_000223.html>

###### sound → system Relation
| File in iop/sound | Includes file in iop/system |
| libsnd2 / src / include / libsnd2_internal.h | intrman / include / intrman.h |
| libsnd2 / src / include / libsnd2_internal.h | stdio / include / stdio.h |
| libsnd2 / src / include / libsnd2_internal.h | sysclib / include / sysclib.h |
| libsnd2 / src / include / libsnd2_internal.h | threadman / include / thbase.h |
| libsnd2 / src / include / libsnd2_internal.h | timrman / include / timrman.h |
| libsnd2 / src / include / libsnd2_internal.h | vblank / include / vblank.h |
| libspu2 / include / libspu2_internal.h | intrman / include / intrman.h |
| libspu2 / include / libspu2_internal.h | loadcore / include / loadcore.h |
| libspu2 / include / libspu2_internal.h | stdio / include / stdio.h |
| rspu2drv / src / include / rs_i.h | intrman / include / intrman.h |
| rspu2drv / src / include / rs_i.h | loadcore / include / loadcore.h |
| rspu2drv / src / include / rs_i.h | sifman / include / sifman.h |
| rspu2drv / src / include / rs_i.h | threadman / include / thbase.h |
| rspu2drv / src / irx_imports.h | intrman / include / intrman.h |
| rspu2drv / src / irx_imports.h | loadcore / include / loadcore.h |
| rspu2drv / src / irx_imports.h | sifman / include / sifman.h |
| rspu2drv / src / irx_imports.h | stdio / include / stdio.h |
| rspu2drv / src / irx_imports.h | sysclib / include / sysclib.h |
| rspu2drv / src / irx_imports.h | threadman / include / thbase.h |
| rspu2drv / src / irx_imports.h | vblank / include / vblank.h |
| libsd / src / batch.c | sifman / include / sifman.h |
| libsd / src / batch.c | intrman / include / intrman.h |
| libsd / src / effect.c | sysclib / include / sysclib.h |
| libsd / src / freesd.c | loadcore / include / loadcore.h |
| libsd / src / freesd.c | stdio / include / stdio.h |
| libsd / src / freesd.c | intrman / include / intrman.h |
| libsd / src / irx_imports.h | intrman / include / intrman.h |
| libsd / src / irx_imports.h | loadcore / include / loadcore.h |
| libsd / src / irx_imports.h | sifman / include / sifman.h |
| libsd / src / irx_imports.h | stdio / include / stdio.h |
| libsd / src / irx_imports.h | sysclib / include / sysclib.h |
| libsd / src / voice.c | sifman / include / sifman.h |
| clearspu / src / irx_imports.h | loadcore / include / loadcore.h |
| clearspu / src / irx_imports.h | intrman / include / intrman.h |
| clearspu / src / irx_imports.h | stdio / include / stdio.h |
| clearspu / src / irx_imports.h | sysclib / include / sysclib.h |
| sdhd / src / irx_imports.h | intrman / include / intrman.h |
| sdhd / src / irx_imports.h | loadcore / include / loadcore.h |
| sdsq / src / irx_imports.h | intrman / include / intrman.h |
| sdsq / src / irx_imports.h | loadcore / include / loadcore.h |
| sdsq / src / irx_imports.h | sysclib / include / sysclib.h |
| sdrdrv / src / irx_imports.h | intrman / include / intrman.h |
| sdrdrv / src / irx_imports.h | loadcore / include / loadcore.h |
| sdrdrv / src / irx_imports.h | sysclib / include / sysclib.h |
| sdrdrv / src / irx_imports.h | threadman / include / thbase.h |
| audsrv / src / adpcm.c | stdio / include / stdio.h |
| audsrv / src / adpcm.c | threadman / include / thbase.h |
| audsrv / src / adpcm.c | threadman / include / thsemap.h |
| audsrv / src / adpcm.c | loadcore / include / loadcore.h |
| audsrv / src / adpcm.c | intrman / include / intrman.h |
| audsrv / src / adpcm.c | sysclib / include / sysclib.h |
| audsrv / src / audsrv.c | stdio / include / stdio.h |
| audsrv / src / audsrv.c | threadman / include / thbase.h |
| audsrv / src / audsrv.c | threadman / include / thsemap.h |
| audsrv / src / audsrv.c | loadcore / include / loadcore.h |
| audsrv / src / audsrv.c | intrman / include / intrman.h |
| audsrv / src / audsrv.c | sysclib / include / sysclib.h |
| audsrv / src / cdrom.c | stdio / include / stdio.h |
| audsrv / src / cdrom.c | threadman / include / thbase.h |
| audsrv / src / cdrom.c | threadman / include / thsemap.h |
| audsrv / src / cdrom.c | loadcore / include / loadcore.h |
| audsrv / src / cdrom.c | intrman / include / intrman.h |
| audsrv / src / cdrom.c | sysclib / include / sysclib.h |
| audsrv / src / common.c | stdio / include / stdio.h |
| audsrv / src / common.c | threadman / include / thbase.h |
| audsrv / src / common.c | threadman / include / thsemap.h |
| audsrv / src / common.c | loadcore / include / loadcore.h |
| audsrv / src / common.c | intrman / include / intrman.h |
| audsrv / src / common.c | sysclib / include / sysclib.h |
| audsrv / src / irx_imports.h | intrman / include / intrman.h |
| audsrv / src / irx_imports.h | loadcore / include / loadcore.h |
| audsrv / src / irx_imports.h | stdio / include / stdio.h |
| audsrv / src / irx_imports.h | sysclib / include / sysclib.h |
| audsrv / src / irx_imports.h | threadman / include / thbase.h |
| audsrv / src / irx_imports.h | threadman / include / thsemap.h |
| audsrv / src / rpc_client.c | stdio / include / stdio.h |
| audsrv / src / rpc_client.c | threadman / include / thbase.h |
| audsrv / src / rpc_client.c | threadman / include / thsemap.h |
| audsrv / src / rpc_client.c | loadcore / include / loadcore.h |
| audsrv / src / rpc_client.c | intrman / include / intrman.h |
| audsrv / src / rpc_client.c | sysclib / include / sysclib.h |
| audsrv / src / rpc_server.c | stdio / include / stdio.h |
| audsrv / src / rpc_server.c | threadman / include / thbase.h |
| audsrv / src / rpc_server.c | threadman / include / thsemap.h |
| audsrv / src / rpc_server.c | loadcore / include / loadcore.h |
| audsrv / src / rpc_server.c | intrman / include / intrman.h |
| audsrv / src / upsamplers.c | stdio / include / stdio.h |
| ahx / src / AHX.c | stdio / include / stdio.h |
| ahx / src / AHX.c | sysclib / include / sysclib.h |
| ahx / src / irx_imports.h | intrman / include / intrman.h |
| ahx / src / irx_imports.h | loadcore / include / loadcore.h |
| ahx / src / irx_imports.h | stdio / include / stdio.h |
| ahx / src / irx_imports.h | sysclib / include / sysclib.h |
| ahx / src / irx_imports.h | threadman / include / thbase.h |
| ahx / src / irx_imports.h | threadman / include / thsemap.h |
| ahx / src / spu2.c | threadman / include / thbase.h |
| ahx / src / spu2.c | intrman / include / intrman.h |
| ahx / src / spu2.c | loadcore / include / loadcore.h |
| ps2snd / src / adpcm-stream.c | loadcore / include / loadcore.h |
| ps2snd / src / adpcm-stream.c | stdio / include / stdio.h |
| ps2snd / src / adpcm-stream.c | threadman / include / thbase.h |
| ps2snd / src / adpcm-stream.c | intrman / include / intrman.h |
| ps2snd / src / adpcm-stream.c | ioman / include / ioman.h |
| ps2snd / src / adpcm-stream.c | threadman / include / thsemap.h |
| ps2snd / src / irx_imports.h | stdio / include / stdio.h |
| ps2snd / src / irx_imports.h | threadman / include / thbase.h |
| ps2snd / src / irx_imports.h | ioman / include / ioman.h |
| ps2snd / src / irx_imports.h | threadman / include / thsemap.h |
| ps2snd / src / irx_imports.h | intrman / include / intrman.h |
| ps2snd / src / irx_imports.h | loadcore / include / loadcore.h |
| ps2snd / src / ps2snd.c | loadcore / include / loadcore.h |
| ps2snd / src / ps2snd.c | stdio / include / stdio.h |
| ps2snd / src / ps2snd.c | threadman / include / thbase.h |
| ps2snd / src / ps2snd.c | intrman / include / intrman.h |
| ps2snd / src / ps2snd.c | threadman / include / thsemap.h |

---

## PS2SDK: iop/sound -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000204_000537.html>

###### sound → kernel Relation
| File in iop/sound | Includes file in iop/kernel |
| audsrv / include / audsrv.h | include / irx.h |
| libsd / include / libsd.h | include / irx.h |
| rspu2drv / src / irx_imports.h | include / irx.h |
| libsd / src / freesd.c | include / irx.h |
| libsd / src / irx_imports.h | include / irx.h |
| libsd / src / voice.c | include / irx.h |
| clearspu / src / irx_imports.h | include / irx.h |
| sdhd / src / irx_imports.h | include / irx.h |
| sdsq / src / irx_imports.h | include / irx.h |
| sdrdrv / src / irx_imports.h | include / irx.h |
| audsrv / src / irx_imports.h | include / irx.h |
| ahx / src / irx_imports.h | include / irx.h |
| ps2snd / src / adpcm-stream.c | include / irx.h |
| ps2snd / src / irx_imports.h | include / irx.h |
| ps2snd / src / ps2snd.c | include / irx.h |

---

## PS2SDK: iop/sound/ahx -&gt; libsd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000205_000211.html>

###### ahx → libsd Relation
| File in iop/sound/ahx | Includes file in iop/sound/libsd |
| src / spu2.c | include / spu2regs.h |

---

## PS2SDK: iop/sound/ahx -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000205_000223.html>

###### ahx → system Relation
| File in iop/sound/ahx | Includes file in iop/system |
| src / AHX.c | stdio / include / stdio.h |
| src / AHX.c | sysclib / include / sysclib.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thsemap.h |
| src / spu2.c | threadman / include / thbase.h |
| src / spu2.c | intrman / include / intrman.h |
| src / spu2.c | loadcore / include / loadcore.h |

---

## PS2SDK: iop/sound/ahx -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000205_000537.html>

###### ahx → kernel Relation
| File in iop/sound/ahx | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/sound/ahx/src -&gt; libsd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000206_000211.html>

###### src → libsd Relation
| File in iop/sound/ahx/src | Includes file in iop/sound/libsd |
| spu2.c | include / spu2regs.h |

---

## PS2SDK: iop/sound/ahx/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000206_000223.html>

###### src → system Relation
| File in iop/sound/ahx/src | Includes file in iop/system |
| AHX.c | stdio / include / stdio.h |
| AHX.c | sysclib / include / sysclib.h |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thsemap.h |
| spu2.c | intrman / include / intrman.h |
| spu2.c | loadcore / include / loadcore.h |
| spu2.c | threadman / include / thbase.h |

---

## PS2SDK: iop/sound/ahx/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000206_000537.html>

###### src → kernel Relation
| File in iop/sound/ahx/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/sound/ahx/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000206_000550.html>

###### src → include Relation
| File in iop/sound/ahx/src | Includes file in iop/sound/ahx/include |
| AHX.c | ahx.h |
| ahx_irx.c | ahx.h |

---

## PS2SDK: iop/sound/audsrv -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000207_000056.html>

###### audsrv → cdvd Relation
| File in iop/sound/audsrv | Includes file in iop/cdvd |
| src / cdrom.c | cdvdman / include / cdvdman.h |
| src / irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/sound/audsrv -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000207_000223.html>

###### audsrv → system Relation
| File in iop/sound/audsrv | Includes file in iop/system |
| src / adpcm.c | stdio / include / stdio.h |
| src / adpcm.c | threadman / include / thbase.h |
| src / adpcm.c | threadman / include / thsemap.h |
| src / adpcm.c | loadcore / include / loadcore.h |
| src / adpcm.c | intrman / include / intrman.h |
| src / adpcm.c | sysclib / include / sysclib.h |
| src / audsrv.c | stdio / include / stdio.h |
| src / audsrv.c | threadman / include / thbase.h |
| src / audsrv.c | threadman / include / thsemap.h |
| src / audsrv.c | loadcore / include / loadcore.h |
| src / audsrv.c | intrman / include / intrman.h |
| src / audsrv.c | sysclib / include / sysclib.h |
| src / cdrom.c | stdio / include / stdio.h |
| src / cdrom.c | threadman / include / thbase.h |
| src / cdrom.c | threadman / include / thsemap.h |
| src / cdrom.c | loadcore / include / loadcore.h |
| src / cdrom.c | intrman / include / intrman.h |
| src / cdrom.c | sysclib / include / sysclib.h |
| src / common.c | stdio / include / stdio.h |
| src / common.c | threadman / include / thbase.h |
| src / common.c | threadman / include / thsemap.h |
| src / common.c | loadcore / include / loadcore.h |
| src / common.c | intrman / include / intrman.h |
| src / common.c | sysclib / include / sysclib.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thsemap.h |
| src / rpc_client.c | stdio / include / stdio.h |
| src / rpc_client.c | threadman / include / thbase.h |
| src / rpc_client.c | threadman / include / thsemap.h |
| src / rpc_client.c | loadcore / include / loadcore.h |
| src / rpc_client.c | intrman / include / intrman.h |
| src / rpc_client.c | sysclib / include / sysclib.h |
| src / rpc_server.c | stdio / include / stdio.h |
| src / rpc_server.c | threadman / include / thbase.h |
| src / rpc_server.c | threadman / include / thsemap.h |
| src / rpc_server.c | loadcore / include / loadcore.h |
| src / rpc_server.c | intrman / include / intrman.h |
| src / upsamplers.c | stdio / include / stdio.h |

---

## PS2SDK: iop/sound/audsrv -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000207_000537.html>

###### audsrv → kernel Relation
| File in iop/sound/audsrv | Includes file in iop/kernel |
| include / audsrv.h | include / irx.h |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/sound/audsrv/src -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000208_000056.html>

###### src → cdvd Relation
| File in iop/sound/audsrv/src | Includes file in iop/cdvd |
| cdrom.c | cdvdman / include / cdvdman.h |
| irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/sound/audsrv/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000208_000223.html>

###### src → system Relation
| File in iop/sound/audsrv/src | Includes file in iop/system |
| adpcm.c | intrman / include / intrman.h |
| adpcm.c | loadcore / include / loadcore.h |
| adpcm.c | stdio / include / stdio.h |
| adpcm.c | sysclib / include / sysclib.h |
| adpcm.c | threadman / include / thbase.h |
| adpcm.c | threadman / include / thsemap.h |
| audsrv.c | intrman / include / intrman.h |
| audsrv.c | loadcore / include / loadcore.h |
| audsrv.c | stdio / include / stdio.h |
| audsrv.c | sysclib / include / sysclib.h |
| audsrv.c | threadman / include / thbase.h |
| audsrv.c | threadman / include / thsemap.h |
| cdrom.c | intrman / include / intrman.h |
| cdrom.c | loadcore / include / loadcore.h |
| cdrom.c | stdio / include / stdio.h |
| cdrom.c | sysclib / include / sysclib.h |
| cdrom.c | threadman / include / thbase.h |
| cdrom.c | threadman / include / thsemap.h |
| common.c | intrman / include / intrman.h |
| common.c | loadcore / include / loadcore.h |
| common.c | stdio / include / stdio.h |
| common.c | sysclib / include / sysclib.h |
| common.c | threadman / include / thbase.h |
| common.c | threadman / include / thsemap.h |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thsemap.h |
| rpc_client.c | intrman / include / intrman.h |
| rpc_client.c | loadcore / include / loadcore.h |
| rpc_client.c | stdio / include / stdio.h |
| rpc_client.c | sysclib / include / sysclib.h |
| rpc_client.c | threadman / include / thbase.h |
| rpc_client.c | threadman / include / thsemap.h |
| rpc_server.c | intrman / include / intrman.h |
| rpc_server.c | loadcore / include / loadcore.h |
| rpc_server.c | stdio / include / stdio.h |
| rpc_server.c | threadman / include / thbase.h |
| rpc_server.c | threadman / include / thsemap.h |
| upsamplers.c | stdio / include / stdio.h |

---

## PS2SDK: iop/sound/audsrv/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000208_000537.html>

###### src → kernel Relation
| File in iop/sound/audsrv/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/sound/clearspu -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000209_000223.html>

###### clearspu → system Relation
| File in iop/sound/clearspu | Includes file in iop/system |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |

---

## PS2SDK: iop/sound/clearspu -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000209_000537.html>

###### clearspu → kernel Relation
| File in iop/sound/clearspu | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/sound/clearspu/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000210_000223.html>

###### src → system Relation
| File in iop/sound/clearspu/src | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |

---

## PS2SDK: iop/sound/clearspu/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000210_000537.html>

###### src → kernel Relation
| File in iop/sound/clearspu/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/sound/libsd -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000211_000000.html>

###### libsd → common Relation
| File in iop/sound/libsd | Includes file in common |
| include / libsd.h | include / libsd-common.h |

---

## PS2SDK: iop/sound/libsd -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000211_000223.html>

###### libsd → system Relation
| File in iop/sound/libsd | Includes file in iop/system |
| src / batch.c | sifman / include / sifman.h |
| src / batch.c | intrman / include / intrman.h |
| src / effect.c | sysclib / include / sysclib.h |
| src / freesd.c | loadcore / include / loadcore.h |
| src / freesd.c | stdio / include / stdio.h |
| src / freesd.c | intrman / include / intrman.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | sifman / include / sifman.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / voice.c | sifman / include / sifman.h |

---

## PS2SDK: iop/sound/libsd -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000211_000537.html>

###### libsd → kernel Relation
| File in iop/sound/libsd | Includes file in iop/kernel |
| include / libsd.h | include / irx.h |
| src / freesd.c | include / irx.h |
| src / irx_imports.h | include / irx.h |
| src / voice.c | include / irx.h |

---

## PS2SDK: iop/sound/libsd/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000212_000223.html>

###### src → system Relation
| File in iop/sound/libsd/src | Includes file in iop/system |
| batch.c | intrman / include / intrman.h |
| batch.c | sifman / include / sifman.h |
| effect.c | sysclib / include / sysclib.h |
| freesd.c | intrman / include / intrman.h |
| freesd.c | loadcore / include / loadcore.h |
| freesd.c | stdio / include / stdio.h |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | sifman / include / sifman.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| voice.c | sifman / include / sifman.h |

---

## PS2SDK: iop/sound/libsd/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000212_000463.html>

###### src → include Relation
| File in iop/sound/libsd/src | Includes file in iop/sound/libsd/include |
| batch.c | spu2regs.h |
| block.c | spu2regs.h |
| effect.c | spu2regs.h |
| freesd.c | spu2regs.h |
| voice.c | spu2regs.h |

---

## PS2SDK: iop/sound/libsd/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000212_000537.html>

###### src → kernel Relation
| File in iop/sound/libsd/src | Includes file in iop/kernel |
| freesd.c | include / irx.h |
| irx_imports.h | include / irx.h |
| voice.c | include / irx.h |

---

## PS2SDK: iop/sound/ps2snd -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000213_000000.html>

###### ps2snd → common Relation
| File in iop/sound/ps2snd | Includes file in common |
| src / adpcm-stream.c | include / ps2snd.h |
| src / ps2snd.c | include / ps2snd.h |

---

## PS2SDK: iop/sound/ps2snd -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000213_000223.html>

###### ps2snd → system Relation
| File in iop/sound/ps2snd | Includes file in iop/system |
| src / adpcm-stream.c | loadcore / include / loadcore.h |
| src / adpcm-stream.c | stdio / include / stdio.h |
| src / adpcm-stream.c | threadman / include / thbase.h |
| src / adpcm-stream.c | intrman / include / intrman.h |
| src / adpcm-stream.c | ioman / include / ioman.h |
| src / adpcm-stream.c | threadman / include / thsemap.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | ioman / include / ioman.h |
| src / irx_imports.h | threadman / include / thsemap.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / ps2snd.c | loadcore / include / loadcore.h |
| src / ps2snd.c | stdio / include / stdio.h |
| src / ps2snd.c | threadman / include / thbase.h |
| src / ps2snd.c | intrman / include / intrman.h |
| src / ps2snd.c | threadman / include / thsemap.h |

---

## PS2SDK: iop/sound/ps2snd -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000213_000537.html>

###### ps2snd → kernel Relation
| File in iop/sound/ps2snd | Includes file in iop/kernel |
| src / adpcm-stream.c | include / irx.h |
| src / irx_imports.h | include / irx.h |
| src / ps2snd.c | include / irx.h |

---

## PS2SDK: iop/sound/ps2snd/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000214_000000.html>

###### src → common Relation
| File in iop/sound/ps2snd/src | Includes file in common |
| adpcm-stream.c | include / ps2snd.h |
| ps2snd.c | include / ps2snd.h |

---

## PS2SDK: iop/sound/ps2snd/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000214_000223.html>

###### src → system Relation
| File in iop/sound/ps2snd/src | Includes file in iop/system |
| adpcm-stream.c | intrman / include / intrman.h |
| adpcm-stream.c | ioman / include / ioman.h |
| adpcm-stream.c | loadcore / include / loadcore.h |
| adpcm-stream.c | stdio / include / stdio.h |
| adpcm-stream.c | threadman / include / thbase.h |
| adpcm-stream.c | threadman / include / thsemap.h |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | ioman / include / ioman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thsemap.h |
| ps2snd.c | intrman / include / intrman.h |
| ps2snd.c | loadcore / include / loadcore.h |
| ps2snd.c | stdio / include / stdio.h |
| ps2snd.c | threadman / include / thbase.h |
| ps2snd.c | threadman / include / thsemap.h |

---

## PS2SDK: iop/sound/ps2snd/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000214_000537.html>

###### src → kernel Relation
| File in iop/sound/ps2snd/src | Includes file in iop/kernel |
| adpcm-stream.c | include / irx.h |
| irx_imports.h | include / irx.h |
| ps2snd.c | include / irx.h |

---

## PS2SDK: iop/sound/rspu2drv -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000215_000000.html>

###### rspu2drv → common Relation
| File in iop/sound/rspu2drv | Includes file in common |
| src / include / rs_i.h | include / tamtypes.h |

---

## PS2SDK: iop/sound/rspu2drv -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000215_000223.html>

###### rspu2drv → system Relation
| File in iop/sound/rspu2drv | Includes file in iop/system |
| src / include / rs_i.h | intrman / include / intrman.h |
| src / include / rs_i.h | loadcore / include / loadcore.h |
| src / include / rs_i.h | sifman / include / sifman.h |
| src / include / rs_i.h | threadman / include / thbase.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | sifman / include / sifman.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | vblank / include / vblank.h |

---

## PS2SDK: iop/sound/rspu2drv -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000215_000537.html>

###### rspu2drv → kernel Relation
| File in iop/sound/rspu2drv | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/sound/rspu2drv/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000216_000000.html>

###### src → common Relation
| File in iop/sound/rspu2drv/src | Includes file in common |
| include / rs_i.h | include / tamtypes.h |

---

## PS2SDK: iop/sound/rspu2drv/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000216_000223.html>

###### src → system Relation
| File in iop/sound/rspu2drv/src | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | sifman / include / sifman.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | vblank / include / vblank.h |
| include / rs_i.h | intrman / include / intrman.h |
| include / rs_i.h | loadcore / include / loadcore.h |
| include / rs_i.h | sifman / include / sifman.h |
| include / rs_i.h | threadman / include / thbase.h |

---

## PS2SDK: iop/sound/rspu2drv/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000216_000537.html>

###### src → kernel Relation
| File in iop/sound/rspu2drv/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/sound/sdhd -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000217_000223.html>

###### sdhd → system Relation
| File in iop/sound/sdhd | Includes file in iop/system |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |

---

## PS2SDK: iop/sound/sdhd -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000217_000537.html>

###### sdhd → kernel Relation
| File in iop/sound/sdhd | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/sound/sdhd/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000218_000223.html>

###### src → system Relation
| File in iop/sound/sdhd/src | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | loadcore / include / loadcore.h |

---

## PS2SDK: iop/sound/sdhd/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000218_000537.html>

###### src → kernel Relation
| File in iop/sound/sdhd/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/sound/sdrdrv -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000219_000000.html>

###### sdrdrv → common Relation
| File in iop/sound/sdrdrv | Includes file in common |
| include / sdrdrv.h | include / libsdr-common.h |
| src / sdr_i.h | include / libsdr-common.h |

---

## PS2SDK: iop/sound/sdrdrv -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000219_000223.html>

###### sdrdrv → system Relation
| File in iop/sound/sdrdrv | Includes file in iop/system |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |

---

## PS2SDK: iop/sound/sdrdrv -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000219_000537.html>

###### sdrdrv → kernel Relation
| File in iop/sound/sdrdrv | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/sound/sdrdrv/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000220_000000.html>

###### src → common Relation
| File in iop/sound/sdrdrv/src | Includes file in common |
| sdr_i.h | include / libsdr-common.h |

---

## PS2SDK: iop/sound/sdrdrv/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000220_000223.html>

###### src → system Relation
| File in iop/sound/sdrdrv/src | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |

---

## PS2SDK: iop/sound/sdrdrv/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000220_000537.html>

###### src → kernel Relation
| File in iop/sound/sdrdrv/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/sound/sdsq -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000221_000223.html>

###### sdsq → system Relation
| File in iop/sound/sdsq | Includes file in iop/system |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | sysclib / include / sysclib.h |

---

## PS2SDK: iop/sound/sdsq -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000221_000537.html>

###### sdsq → kernel Relation
| File in iop/sound/sdsq | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/sound/sdsq/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000222_000223.html>

###### src → system Relation
| File in iop/sound/sdsq/src | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | sysclib / include / sysclib.h |

---

## PS2SDK: iop/sound/sdsq/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000222_000537.html>

###### src → kernel Relation
| File in iop/sound/sdsq/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/system -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000223_000000.html>

###### system → common Relation
| File in iop/system | Includes file in common |
| boardinf / src / boardinf.c | include / iop_mmio_hwport.h |
| eeconf / src / eeconf.c | include / dev5_mmio_hwport.h |
| eeconf / src / eeconf.c | include / iop_mmio_hwport.h |
| sysclib / src / newlib / libc / machine / mips / machine / fenv-softfloat.h | include / errno.h |
| igreeting / src / igreeting.c | include / iop_mmio_hwport.h |
| igreeting / src / igreeting.c | include / mipscopaccess.h |
| igreeting / src / igreeting.c | include / tamtypes.h |
| intrman / src / intrman.c | include / iop_low_memory_globals.h |
| intrman / src / intrman.c | include / iop_mmio_hwport.h |
| intrman / src / intrman.c | include / mipscopaccess.h |
| ioman / src / ioman.c | include / errno.h |
| ioman / include / ioman.h | include / io_common.h |
| ioman / include / ioman_mod.h | include / io_common.h |
| ioman / include / ioman_mod.h | include / iox_stat.h |
| iomanx / src / iomanX.c | include / errno.h |
| iomanx / include / iomanX.h | include / io_common.h |
| iomanx / include / iomanX.h | include / iox_stat.h |
| loadfile / src / loadfile.c | include / loadfile-common.h |
| modload / src / modload.c | include / mipscopaccess.h |
| rmreset / src / rmreset.c | include / iop_mmio_hwport.h |
| sysclib / include / setjmp.h | include / tamtypes.h |
| sifcmd / include / sifcmd.h | include / sifcmd-common.h |
| sifcmd / include / sifcmd.h | include / sifrpc-common.h |
| sifman / src / sifman.c | include / iop_mmio_hwport.h |
| sifman / src / sifman.c | include / mipscopaccess.h |
| sifman / src / sifman.c | include / sif_mmio_hwport.h |
| threadman / src / include / thcommon.h | include / tamtypes.h |
| timrman / src / timrman.c | include / mipscopaccess.h |
| timrman / src / timrman.c | include / tamtypes.h |
| udnl / src / udnl.c | include / mipscopaccess.h |

---

## PS2SDK: iop/system -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000223_000537.html>

###### system → kernel Relation
| File in iop/system | Includes file in iop/kernel |
| alloc / src / alloc.c | include / defs.h |
| alloc / include / alloc.h | include / irx.h |
| iopmgr / src / commandline.c | include / defs.h |
| iopmgr / src / devices.c | include / defs.h |
| dmacman / include / dmacman.h | include / irx.h |
| loadfile / src / eeelfloader.c | include / kerr.h |
| excepman / src / excepman.c | include / kerr.h |
| excepman / include / excepman.h | include / irx.h |
| heaplib / include / heaplib.h | include / irx.h |
| intrman / src / intrman.c | include / kerr.h |
| intrman / include / intrman.h | include / irx.h |
| ioman / include / ioman.h | include / irx.h |
| ioman / include / ioman_mod.h | include / irx.h |
| iopmgr / include / iopmgr.h | include / irx.h |
| excepman / src / irx_imports.h | include / irx.h |
| siftoo / src / irx_imports.h | include / irx.h |
| threadman / src / irx_imports.h | include / irx.h |
| stdio / src / irx_imports.h | include / irx.h |
| sysclib / src / irx_imports.h | include / irx.h |
| sifinit / src / irx_imports.h | include / irx.h |
| loadcore / src / irx_imports.h | include / irx.h |
| ioman / src / irx_imports.h | include / irx.h |
| eesync / src / irx_imports.h | include / irx.h |
| vblank / src / irx_imports.h | include / irx.h |
| msifrpc / src / irx_imports.h | include / irx.h |
| reboot / src / irx_imports.h | include / irx.h |
| iopmgr / src / irx_imports.h | include / irx.h |
| sifman / src / irx_imports.h | include / irx.h |
| intrman / src / irx_imports.h | include / irx.h |
| dmacman / src / irx_imports.h | include / irx.h |
| iomanx / src / irx_imports.h | include / irx.h |
| udnl / src / irx_imports.h | include / irx.h |
| ssbusc / src / irx_imports.h | include / irx.h |
| timrman / src / irx_imports.h | include / irx.h |
| heaplib / src / irx_imports.h | include / irx.h |
| rmreset / src / irx_imports.h | include / irx.h |
| modload / src / irx_imports.h | include / irx.h |
| alloc / src / irx_imports.h | include / irx.h |
| eeconf / src / irx_imports.h | include / irx.h |
| sbusintr / src / irx_imports.h | include / irx.h |
| sifcmd / src / irx_imports.h | include / irx.h |
| loadfile / src / irx_imports.h | include / irx.h |
| boardinf / src / irx_imports.h | include / irx.h |
| igreeting / src / irx_imports.h | include / irx.h |
| loadcore / src / loadcore.c | include / defs.h |
| loadcore / src / loadcore.c | include / kerr.h |
| loadcore / include / loadcore.h | include / irx.h |
| loadfile / src / loadfile.c | include / kerr.h |
| iopmgr / src / main.c | include / defs.h |
| iopmgr / src / main.c | include / irx.h |
| modload / src / modload.c | include / kerr.h |
| modload / include / modload.h | include / irx.h |
| msifrpc / src / msifrpc.c | include / kerr.h |
| siftoo / src / pipe.c | include / defs.h |
| sbusintr / src / sbusintr.c | include / defs.h |
| sbusintr / src / sbusintr.c | include / irx.h |
| sbusintr / include / sbusintr.h | include / irx.h |
| sifcmd / include / sifcmd.h | include / irx.h |
| sifman / include / sifman.h | include / irx.h |
| siftoo / src / siftoo.c | include / defs.h |
| siftoo / src / siftoo.c | include / irx.h |
| siftoo / include / siftoo.h | include / irx.h |
| iopmgr / src / slib.c | include / defs.h |
| iopmgr / src / slib.c | include / irx.h |
| iopmgr / src / smod.c | include / defs.h |
| iopmgr / src / smod.c | include / irx.h |
| ssbusc / include / ssbusc.h | include / irx.h |
| stdio / include / stdio.h | include / irx.h |
| sysclib / include / sysclib.h | include / irx.h |
| sysmem / include / sysmem.h | include / irx.h |
| threadman / src / thbase.c | include / defs.h |
| threadman / src / thbase.c | include / kerr.h |
| threadman / include / thbase.h | include / irx.h |
| threadman / src / thcommon.c | include / defs.h |
| threadman / src / thcommon.c | include / kerr.h |
| threadman / src / thevent.c | include / kerr.h |
| threadman / include / thevent.h | include / irx.h |
| threadman / src / thfpool.c | include / kerr.h |
| threadman / include / thfpool.h | include / irx.h |
| threadman / src / thmsgbx.c | include / kerr.h |
| threadman / include / thmsgbx.h | include / irx.h |
| threadman / src / thsemap.c | include / kerr.h |
| threadman / include / thsemap.h | include / irx.h |
| threadman / src / thvpool.c | include / kerr.h |
| threadman / include / thvpool.h | include / irx.h |
| timrman / src / timrman.c | include / kerr.h |
| timrman / include / timrman.h | include / irx.h |
| vblank / src / vblank.c | include / kerr.h |
| vblank / include / vblank.h | include / irx.h |

---

## PS2SDK: iop/system/alloc -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000224_000248.html>

###### alloc → loadcore Relation
| File in iop/system/alloc | Includes file in iop/system/loadcore |
| src / irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/alloc -&gt; sysclib Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000224_000274.html>

###### alloc → sysclib Relation
| File in iop/system/alloc | Includes file in iop/system/sysclib |
| src / irx_imports.h | include / sysclib.h |

---

## PS2SDK: iop/system/alloc -&gt; threadman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000224_000276.html>

###### alloc → threadman Relation
| File in iop/system/alloc | Includes file in iop/system/threadman |
| src / irx_imports.h | include / thsemap.h |

---

## PS2SDK: iop/system/alloc -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000224_000537.html>

###### alloc → kernel Relation
| File in iop/system/alloc | Includes file in iop/kernel |
| include / alloc.h | include / irx.h |
| src / alloc.c | include / defs.h |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/system/alloc/src -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000225_000248.html>

###### src → loadcore Relation
| File in iop/system/alloc/src | Includes file in iop/system/loadcore |
| irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/alloc/src -&gt; sysclib Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000225_000274.html>

###### src → sysclib Relation
| File in iop/system/alloc/src | Includes file in iop/system/sysclib |
| irx_imports.h | include / sysclib.h |

---

## PS2SDK: iop/system/alloc/src -&gt; threadman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000225_000276.html>

###### src → threadman Relation
| File in iop/system/alloc/src | Includes file in iop/system/threadman |
| irx_imports.h | include / thsemap.h |

---

## PS2SDK: iop/system/alloc/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000225_000537.html>

###### src → kernel Relation
| File in iop/system/alloc/src | Includes file in iop/kernel |
| alloc.c | include / defs.h |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/system/alloc/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000225_000565.html>

###### src → include Relation
| File in iop/system/alloc/src | Includes file in iop/system/alloc/include |
| alloc.c | alloc.h |

---

## PS2SDK: iop/system/boardinf -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000226_000000.html>

###### boardinf → common Relation
| File in iop/system/boardinf | Includes file in common |
| src / boardinf.c | include / iop_mmio_hwport.h |

---

## PS2SDK: iop/system/boardinf -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000226_000248.html>

###### boardinf → loadcore Relation
| File in iop/system/boardinf | Includes file in iop/system/loadcore |
| src / irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/boardinf -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000226_000537.html>

###### boardinf → kernel Relation
| File in iop/system/boardinf | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/system/boardinf/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000227_000000.html>

###### src → common Relation
| File in iop/system/boardinf/src | Includes file in common |
| boardinf.c | include / iop_mmio_hwport.h |

---

## PS2SDK: iop/system/boardinf/src -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000227_000248.html>

###### src → loadcore Relation
| File in iop/system/boardinf/src | Includes file in iop/system/loadcore |
| irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/boardinf/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000227_000537.html>

###### src → kernel Relation
| File in iop/system/boardinf/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/system/dmacman -&gt; intrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000228_000240.html>

###### dmacman → intrman Relation
| File in iop/system/dmacman | Includes file in iop/system/intrman |
| src / irx_imports.h | include / intrman.h |

---

## PS2SDK: iop/system/dmacman -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000228_000248.html>

###### dmacman → loadcore Relation
| File in iop/system/dmacman | Includes file in iop/system/loadcore |
| src / irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/dmacman -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000228_000537.html>

###### dmacman → kernel Relation
| File in iop/system/dmacman | Includes file in iop/kernel |
| include / dmacman.h | include / irx.h |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/system/dmacman/src -&gt; intrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000229_000240.html>

###### src → intrman Relation
| File in iop/system/dmacman/src | Includes file in iop/system/intrman |
| irx_imports.h | include / intrman.h |

---

## PS2SDK: iop/system/dmacman/src -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000229_000248.html>

###### src → loadcore Relation
| File in iop/system/dmacman/src | Includes file in iop/system/loadcore |
| irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/dmacman/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000229_000537.html>

###### src → kernel Relation
| File in iop/system/dmacman/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/system/dmacman/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000229_000566.html>

###### src → include Relation
| File in iop/system/dmacman/src | Includes file in iop/system/dmacman/include |
| dmacman.c | dmacman.h |

---

## PS2SDK: iop/system/eeconf -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000230_000000.html>

###### eeconf → common Relation
| File in iop/system/eeconf | Includes file in common |
| src / eeconf.c | include / dev5_mmio_hwport.h |
| src / eeconf.c | include / iop_mmio_hwport.h |

---

## PS2SDK: iop/system/eeconf -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000230_000248.html>

###### eeconf → loadcore Relation
| File in iop/system/eeconf | Includes file in iop/system/loadcore |
| src / irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/eeconf -&gt; sysclib Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000230_000274.html>

###### eeconf → sysclib Relation
| File in iop/system/eeconf | Includes file in iop/system/sysclib |
| src / irx_imports.h | include / sysclib.h |

---

## PS2SDK: iop/system/eeconf -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000230_000537.html>

###### eeconf → kernel Relation
| File in iop/system/eeconf | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/system/eeconf/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000231_000000.html>

###### src → common Relation
| File in iop/system/eeconf/src | Includes file in common |
| eeconf.c | include / dev5_mmio_hwport.h |
| eeconf.c | include / iop_mmio_hwport.h |

---

## PS2SDK: iop/system/eeconf/src -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000231_000248.html>

###### src → loadcore Relation
| File in iop/system/eeconf/src | Includes file in iop/system/loadcore |
| irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/eeconf/src -&gt; sysclib Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000231_000274.html>

###### src → sysclib Relation
| File in iop/system/eeconf/src | Includes file in iop/system/sysclib |
| irx_imports.h | include / sysclib.h |

---

## PS2SDK: iop/system/eeconf/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000231_000537.html>

###### src → kernel Relation
| File in iop/system/eeconf/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/system/eesync -&gt; intrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000232_000240.html>

###### eesync → intrman Relation
| File in iop/system/eesync | Includes file in iop/system/intrman |
| src / eesync.c | include / intrman.h |

---

## PS2SDK: iop/system/eesync -&gt; ioman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000232_000242.html>

###### eesync → ioman Relation
| File in iop/system/eesync | Includes file in iop/system/ioman |
| src / eesync.c | include / ioman.h |
| src / irx_imports.h | include / ioman.h |

---

## PS2SDK: iop/system/eesync -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000232_000248.html>

###### eesync → loadcore Relation
| File in iop/system/eesync | Includes file in iop/system/loadcore |
| src / eesync.c | include / loadcore.h |
| src / irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/eesync -&gt; sifman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000232_000266.html>

###### eesync → sifman Relation
| File in iop/system/eesync | Includes file in iop/system/sifman |
| src / eesync.c | include / sifman.h |
| src / irx_imports.h | include / sifman.h |

---

## PS2SDK: iop/system/eesync -&gt; sysclib Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000232_000274.html>

###### eesync → sysclib Relation
| File in iop/system/eesync | Includes file in iop/system/sysclib |
| src / eesync.c | include / sysclib.h |
| src / irx_imports.h | include / sysclib.h |

---

## PS2SDK: iop/system/eesync -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000232_000537.html>

###### eesync → kernel Relation
| File in iop/system/eesync | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/system/eesync/src -&gt; intrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000233_000240.html>

###### src → intrman Relation
| File in iop/system/eesync/src | Includes file in iop/system/intrman |
| eesync.c | include / intrman.h |

---

## PS2SDK: iop/system/eesync/src -&gt; ioman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000233_000242.html>

###### src → ioman Relation
| File in iop/system/eesync/src | Includes file in iop/system/ioman |
| eesync.c | include / ioman.h |
| irx_imports.h | include / ioman.h |

---

## PS2SDK: iop/system/eesync/src -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000233_000248.html>

###### src → loadcore Relation
| File in iop/system/eesync/src | Includes file in iop/system/loadcore |
| eesync.c | include / loadcore.h |
| irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/eesync/src -&gt; sifman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000233_000266.html>

###### src → sifman Relation
| File in iop/system/eesync/src | Includes file in iop/system/sifman |
| eesync.c | include / sifman.h |
| irx_imports.h | include / sifman.h |

---

## PS2SDK: iop/system/eesync/src -&gt; sysclib Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000233_000274.html>

###### src → sysclib Relation
| File in iop/system/eesync/src | Includes file in iop/system/sysclib |
| eesync.c | include / sysclib.h |
| irx_imports.h | include / sysclib.h |

---

## PS2SDK: iop/system/eesync/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000233_000537.html>

###### src → kernel Relation
| File in iop/system/eesync/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/system/excepman -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000234_000248.html>

###### excepman → loadcore Relation
| File in iop/system/excepman | Includes file in iop/system/loadcore |
| src / irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/excepman -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000234_000537.html>

###### excepman → kernel Relation
| File in iop/system/excepman | Includes file in iop/kernel |
| include / excepman.h | include / irx.h |
| src / excepman.c | include / kerr.h |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/system/excepman/src -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000235_000248.html>

###### src → loadcore Relation
| File in iop/system/excepman/src | Includes file in iop/system/loadcore |
| irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/excepman/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000235_000537.html>

###### src → kernel Relation
| File in iop/system/excepman/src | Includes file in iop/kernel |
| excepman.c | include / kerr.h |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/system/excepman/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000235_000569.html>

###### src → include Relation
| File in iop/system/excepman/src | Includes file in iop/system/excepman/include |
| excepman.c | excepman.h |

---

## PS2SDK: iop/system/heaplib -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000236_000248.html>

###### heaplib → loadcore Relation
| File in iop/system/heaplib | Includes file in iop/system/loadcore |
| src / irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/heaplib -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000236_000537.html>

###### heaplib → kernel Relation
| File in iop/system/heaplib | Includes file in iop/kernel |
| include / heaplib.h | include / irx.h |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/system/heaplib/src -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000237_000248.html>

###### src → loadcore Relation
| File in iop/system/heaplib/src | Includes file in iop/system/loadcore |
| irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/heaplib/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000237_000537.html>

###### src → kernel Relation
| File in iop/system/heaplib/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/system/heaplib/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000237_000570.html>

###### src → include Relation
| File in iop/system/heaplib/src | Includes file in iop/system/heaplib/include |
| heaplib.c | heaplib.h |

---

## PS2SDK: iop/system/igreeting -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000238_000000.html>

###### igreeting → common Relation
| File in iop/system/igreeting | Includes file in common |
| src / igreeting.c | include / iop_mmio_hwport.h |
| src / igreeting.c | include / tamtypes.h |
| src / igreeting.c | include / mipscopaccess.h |

---

## PS2SDK: iop/system/igreeting -&gt; intrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000238_000240.html>

###### igreeting → intrman Relation
| File in iop/system/igreeting | Includes file in iop/system/intrman |
| src / irx_imports.h | include / intrman.h |

---

## PS2SDK: iop/system/igreeting -&gt; ioman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000238_000242.html>

###### igreeting → ioman Relation
| File in iop/system/igreeting | Includes file in iop/system/ioman |
| src / irx_imports.h | include / ioman.h |

---

## PS2SDK: iop/system/igreeting -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000238_000248.html>

###### igreeting → loadcore Relation
| File in iop/system/igreeting | Includes file in iop/system/loadcore |
| src / irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/igreeting -&gt; stdio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000238_000272.html>

###### igreeting → stdio Relation
| File in iop/system/igreeting | Includes file in iop/system/stdio |
| src / irx_imports.h | include / stdio.h |

---

## PS2SDK: iop/system/igreeting -&gt; sysclib Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000238_000274.html>

###### igreeting → sysclib Relation
| File in iop/system/igreeting | Includes file in iop/system/sysclib |
| src / irx_imports.h | include / sysclib.h |

---

## PS2SDK: iop/system/igreeting -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000238_000537.html>

###### igreeting → kernel Relation
| File in iop/system/igreeting | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/system/igreeting/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000239_000000.html>

###### src → common Relation
| File in iop/system/igreeting/src | Includes file in common |
| igreeting.c | include / iop_mmio_hwport.h |
| igreeting.c | include / mipscopaccess.h |
| igreeting.c | include / tamtypes.h |

---

## PS2SDK: iop/system/igreeting/src -&gt; intrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000239_000240.html>

###### src → intrman Relation
| File in iop/system/igreeting/src | Includes file in iop/system/intrman |
| irx_imports.h | include / intrman.h |

---

## PS2SDK: iop/system/igreeting/src -&gt; ioman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000239_000242.html>

###### src → ioman Relation
| File in iop/system/igreeting/src | Includes file in iop/system/ioman |
| irx_imports.h | include / ioman.h |

---

## PS2SDK: iop/system/igreeting/src -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000239_000248.html>

###### src → loadcore Relation
| File in iop/system/igreeting/src | Includes file in iop/system/loadcore |
| irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/igreeting/src -&gt; stdio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000239_000272.html>

###### src → stdio Relation
| File in iop/system/igreeting/src | Includes file in iop/system/stdio |
| irx_imports.h | include / stdio.h |

---

## PS2SDK: iop/system/igreeting/src -&gt; sysclib Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000239_000274.html>

###### src → sysclib Relation
| File in iop/system/igreeting/src | Includes file in iop/system/sysclib |
| irx_imports.h | include / sysclib.h |

---

## PS2SDK: iop/system/igreeting/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000239_000537.html>

###### src → kernel Relation
| File in iop/system/igreeting/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/system/intrman -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000240_000000.html>

###### intrman → common Relation
| File in iop/system/intrman | Includes file in common |
| src / intrman.c | include / mipscopaccess.h |
| src / intrman.c | include / iop_low_memory_globals.h |
| src / intrman.c | include / iop_mmio_hwport.h |

---

## PS2SDK: iop/system/intrman -&gt; excepman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000240_000234.html>

###### intrman → excepman Relation
| File in iop/system/intrman | Includes file in iop/system/excepman |
| src / irx_imports.h | include / excepman.h |

---

## PS2SDK: iop/system/intrman -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000240_000248.html>

###### intrman → loadcore Relation
| File in iop/system/intrman | Includes file in iop/system/loadcore |
| src / irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/intrman -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000240_000537.html>

###### intrman → kernel Relation
| File in iop/system/intrman | Includes file in iop/kernel |
| include / intrman.h | include / irx.h |
| src / intrman.c | include / kerr.h |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/system/intrman/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000241_000000.html>

###### src → common Relation
| File in iop/system/intrman/src | Includes file in common |
| intrman.c | include / iop_low_memory_globals.h |
| intrman.c | include / iop_mmio_hwport.h |
| intrman.c | include / mipscopaccess.h |

---

## PS2SDK: iop/system/intrman/src -&gt; excepman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000241_000234.html>

###### src → excepman Relation
| File in iop/system/intrman/src | Includes file in iop/system/excepman |
| irx_imports.h | include / excepman.h |

---

## PS2SDK: iop/system/intrman/src -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000241_000248.html>

###### src → loadcore Relation
| File in iop/system/intrman/src | Includes file in iop/system/loadcore |
| irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/intrman/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000241_000537.html>

###### src → kernel Relation
| File in iop/system/intrman/src | Includes file in iop/kernel |
| intrman.c | include / kerr.h |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/system/intrman/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000241_000571.html>

###### src → include Relation
| File in iop/system/intrman/src | Includes file in iop/system/intrman/include |
| intrman.c | intrman.h |

---

## PS2SDK: iop/system/ioman -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000242_000000.html>

###### ioman → common Relation
| File in iop/system/ioman | Includes file in common |
| include / ioman.h | include / io_common.h |
| include / ioman_mod.h | include / io_common.h |
| include / ioman_mod.h | include / iox_stat.h |
| src / ioman.c | include / errno.h |

---

## PS2SDK: iop/system/ioman -&gt; intrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000242_000240.html>

###### ioman → intrman Relation
| File in iop/system/ioman | Includes file in iop/system/intrman |
| src / ioman.c | include / intrman.h |
| src / irx_imports.h | include / intrman.h |

---

## PS2SDK: iop/system/ioman -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000242_000248.html>

###### ioman → loadcore Relation
| File in iop/system/ioman | Includes file in iop/system/loadcore |
| src / irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/ioman -&gt; stdio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000242_000272.html>

###### ioman → stdio Relation
| File in iop/system/ioman | Includes file in iop/system/stdio |
| src / irx_imports.h | include / stdio.h |

---

## PS2SDK: iop/system/ioman -&gt; sysclib Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000242_000274.html>

###### ioman → sysclib Relation
| File in iop/system/ioman | Includes file in iop/system/sysclib |
| src / irx_imports.h | include / sysclib.h |

---

## PS2SDK: iop/system/ioman -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000242_000537.html>

###### ioman → kernel Relation
| File in iop/system/ioman | Includes file in iop/kernel |
| include / ioman.h | include / irx.h |
| include / ioman_mod.h | include / irx.h |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/system/ioman -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000242_000582.html>

###### ioman → include Relation
| File in iop/system/ioman | Includes file in iop/system/stdio/include |
| src / irx_imports.h | stdio.h |

---

## PS2SDK: iop/system/ioman/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000243_000000.html>

###### src → common Relation
| File in iop/system/ioman/src | Includes file in common |
| ioman.c | include / errno.h |

---

## PS2SDK: iop/system/ioman/src -&gt; intrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000243_000240.html>

###### src → intrman Relation
| File in iop/system/ioman/src | Includes file in iop/system/intrman |
| ioman.c | include / intrman.h |
| irx_imports.h | include / intrman.h |

---

## PS2SDK: iop/system/ioman/src -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000243_000248.html>

###### src → loadcore Relation
| File in iop/system/ioman/src | Includes file in iop/system/loadcore |
| irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/ioman/src -&gt; stdio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000243_000272.html>

###### src → stdio Relation
| File in iop/system/ioman/src | Includes file in iop/system/stdio |
| irx_imports.h | include / stdio.h |

---

## PS2SDK: iop/system/ioman/src -&gt; sysclib Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000243_000274.html>

###### src → sysclib Relation
| File in iop/system/ioman/src | Includes file in iop/system/sysclib |
| irx_imports.h | include / sysclib.h |

---

## PS2SDK: iop/system/ioman/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000243_000537.html>

###### src → kernel Relation
| File in iop/system/ioman/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/system/ioman/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000243_000572.html>

###### src → include Relation
| File in iop/system/ioman/src | Includes file in iop/system/ioman/include |
| ioman.c | ioman.h |
| ioman.c | ioman_mod.h |

---

## PS2SDK: iop/system/iomanx -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000244_000000.html>

###### iomanx → common Relation
| File in iop/system/iomanx | Includes file in common |
| include / iomanX.h | include / io_common.h |
| include / iomanX.h | include / iox_stat.h |
| src / iomanX.c | include / errno.h |

---

## PS2SDK: iop/system/iomanx -&gt; intrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000244_000240.html>

###### iomanx → intrman Relation
| File in iop/system/iomanx | Includes file in iop/system/intrman |
| src / iomanX.c | include / intrman.h |
| src / irx_imports.h | include / intrman.h |

---

## PS2SDK: iop/system/iomanx -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000244_000248.html>

###### iomanx → loadcore Relation
| File in iop/system/iomanx | Includes file in iop/system/loadcore |
| src / irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/iomanx -&gt; stdio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000244_000272.html>

###### iomanx → stdio Relation
| File in iop/system/iomanx | Includes file in iop/system/stdio |
| src / iomanX.c | include / stdio.h |
| src / irx_imports.h | include / stdio.h |

---

## PS2SDK: iop/system/iomanx -&gt; sysclib Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000244_000274.html>

###### iomanx → sysclib Relation
| File in iop/system/iomanx | Includes file in iop/system/sysclib |
| src / irx_imports.h | include / sysclib.h |

---

## PS2SDK: iop/system/iomanx -&gt; threadman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000244_000276.html>

###### iomanx → threadman Relation
| File in iop/system/iomanx | Includes file in iop/system/threadman |
| src / irx_imports.h | include / thbase.h |

---

## PS2SDK: iop/system/iomanx -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000244_000537.html>

###### iomanx → kernel Relation
| File in iop/system/iomanx | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/system/iomanx/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000245_000000.html>

###### src → common Relation
| File in iop/system/iomanx/src | Includes file in common |
| iomanX.c | include / errno.h |

---

## PS2SDK: iop/system/iomanx/src -&gt; intrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000245_000240.html>

###### src → intrman Relation
| File in iop/system/iomanx/src | Includes file in iop/system/intrman |
| iomanX.c | include / intrman.h |
| irx_imports.h | include / intrman.h |

---

## PS2SDK: iop/system/iomanx/src -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000245_000248.html>

###### src → loadcore Relation
| File in iop/system/iomanx/src | Includes file in iop/system/loadcore |
| irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/iomanx/src -&gt; stdio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000245_000272.html>

###### src → stdio Relation
| File in iop/system/iomanx/src | Includes file in iop/system/stdio |
| iomanX.c | include / stdio.h |
| irx_imports.h | include / stdio.h |

---

## PS2SDK: iop/system/iomanx/src -&gt; sysclib Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000245_000274.html>

###### src → sysclib Relation
| File in iop/system/iomanx/src | Includes file in iop/system/sysclib |
| irx_imports.h | include / sysclib.h |

---

## PS2SDK: iop/system/iomanx/src -&gt; threadman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000245_000276.html>

###### src → threadman Relation
| File in iop/system/iomanx/src | Includes file in iop/system/threadman |
| irx_imports.h | include / thbase.h |

---

## PS2SDK: iop/system/iomanx/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000245_000537.html>

###### src → kernel Relation
| File in iop/system/iomanx/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/system/iomanx/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000245_000573.html>

###### src → include Relation
| File in iop/system/iomanx/src | Includes file in iop/system/iomanx/include |
| iomanX.c | iomanX.h |

---

## PS2SDK: iop/system/iopmgr -&gt; ioman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000246_000242.html>

###### iopmgr → ioman Relation
| File in iop/system/iopmgr | Includes file in iop/system/ioman |
| include / iopmgr.h | include / ioman.h |
| src / slib.c | include / ioman.h |
| src / smod.c | include / ioman.h |

---

## PS2SDK: iop/system/iopmgr -&gt; iomanx Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000246_000244.html>

###### iopmgr → iomanx Relation
| File in iop/system/iopmgr | Includes file in iop/system/iomanx |
| src / commandline.c | include / iomanX.h |
| src / devices.c | include / iomanX.h |
| src / main.c | include / iomanX.h |

---

## PS2SDK: iop/system/iopmgr -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000246_000248.html>

###### iopmgr → loadcore Relation
| File in iop/system/iopmgr | Includes file in iop/system/loadcore |
| include / iopmgr.h | include / loadcore.h |
| src / irx_imports.h | include / loadcore.h |
| src / slib.c | include / loadcore.h |
| src / smod.c | include / loadcore.h |

---

## PS2SDK: iop/system/iopmgr -&gt; stdio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000246_000272.html>

###### iopmgr → stdio Relation
| File in iop/system/iopmgr | Includes file in iop/system/stdio |
| src / commandline.c | include / stdio.h |
| src / devices.c | include / stdio.h |
| src / irx_imports.h | include / stdio.h |
| src / main.c | include / stdio.h |
| src / slib.c | include / stdio.h |
| src / smod.c | include / stdio.h |

---

## PS2SDK: iop/system/iopmgr -&gt; sysclib Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000246_000274.html>

###### iopmgr → sysclib Relation
| File in iop/system/iopmgr | Includes file in iop/system/sysclib |
| src / commandline.c | include / sysclib.h |
| src / devices.c | include / sysclib.h |
| src / irx_imports.h | include / sysclib.h |
| src / slib.c | include / sysclib.h |
| src / smod.c | include / sysclib.h |

---

## PS2SDK: iop/system/iopmgr -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000246_000537.html>

###### iopmgr → kernel Relation
| File in iop/system/iopmgr | Includes file in iop/kernel |
| include / iopmgr.h | include / irx.h |
| src / commandline.c | include / defs.h |
| src / devices.c | include / defs.h |
| src / irx_imports.h | include / irx.h |
| src / main.c | include / defs.h |
| src / main.c | include / irx.h |
| src / slib.c | include / defs.h |
| src / slib.c | include / irx.h |
| src / smod.c | include / defs.h |
| src / smod.c | include / irx.h |

---

## PS2SDK: iop/system/iopmgr/src -&gt; ioman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000247_000242.html>

###### src → ioman Relation
| File in iop/system/iopmgr/src | Includes file in iop/system/ioman |
| slib.c | include / ioman.h |
| smod.c | include / ioman.h |

---

## PS2SDK: iop/system/iopmgr/src -&gt; iomanx Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000247_000244.html>

###### src → iomanx Relation
| File in iop/system/iopmgr/src | Includes file in iop/system/iomanx |
| commandline.c | include / iomanX.h |
| devices.c | include / iomanX.h |
| main.c | include / iomanX.h |

---

## PS2SDK: iop/system/iopmgr/src -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000247_000248.html>

###### src → loadcore Relation
| File in iop/system/iopmgr/src | Includes file in iop/system/loadcore |
| irx_imports.h | include / loadcore.h |
| slib.c | include / loadcore.h |
| smod.c | include / loadcore.h |

---

## PS2SDK: iop/system/iopmgr/src -&gt; stdio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000247_000272.html>

###### src → stdio Relation
| File in iop/system/iopmgr/src | Includes file in iop/system/stdio |
| commandline.c | include / stdio.h |
| devices.c | include / stdio.h |
| irx_imports.h | include / stdio.h |
| main.c | include / stdio.h |
| slib.c | include / stdio.h |
| smod.c | include / stdio.h |

---

## PS2SDK: iop/system/iopmgr/src -&gt; sysclib Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000247_000274.html>

###### src → sysclib Relation
| File in iop/system/iopmgr/src | Includes file in iop/system/sysclib |
| commandline.c | include / sysclib.h |
| devices.c | include / sysclib.h |
| irx_imports.h | include / sysclib.h |
| slib.c | include / sysclib.h |
| smod.c | include / sysclib.h |

---

## PS2SDK: iop/system/iopmgr/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000247_000537.html>

###### src → kernel Relation
| File in iop/system/iopmgr/src | Includes file in iop/kernel |
| commandline.c | include / defs.h |
| devices.c | include / defs.h |
| irx_imports.h | include / irx.h |
| main.c | include / defs.h |
| main.c | include / irx.h |
| slib.c | include / defs.h |
| slib.c | include / irx.h |
| smod.c | include / defs.h |
| smod.c | include / irx.h |

---

## PS2SDK: iop/system/iopmgr/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000247_000574.html>

###### src → include Relation
| File in iop/system/iopmgr/src | Includes file in iop/system/iopmgr/include |
| commandline.c | iopmgr.h |
| devices.c | iopmgr.h |
| main.c | iopmgr.h |
| slib.c | iopmgr.h |
| smod.c | iopmgr.h |

---

## PS2SDK: iop/system/loadcore -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000248_000537.html>

###### loadcore → kernel Relation
| File in iop/system/loadcore | Includes file in iop/kernel |
| include / loadcore.h | include / irx.h |
| src / irx_imports.h | include / irx.h |
| src / loadcore.c | include / kerr.h |
| src / loadcore.c | include / defs.h |

---

## PS2SDK: iop/system/loadcore/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000249_000537.html>

###### src → kernel Relation
| File in iop/system/loadcore/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |
| loadcore.c | include / defs.h |
| loadcore.c | include / kerr.h |

---

## PS2SDK: iop/system/loadcore/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000249_000575.html>

###### src → include Relation
| File in iop/system/loadcore/src | Includes file in iop/system/loadcore/include |
| loadcore.c | loadcore.h |
| loadcore.c | xloadcore.h |

---

## PS2SDK: iop/system/loadfile -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000250_000000.html>

###### loadfile → common Relation
| File in iop/system/loadfile | Includes file in common |
| src / loadfile.c | include / loadfile-common.h |

---

## PS2SDK: iop/system/loadfile -&gt; intrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000250_000240.html>

###### loadfile → intrman Relation
| File in iop/system/loadfile | Includes file in iop/system/intrman |
| src / irx_imports.h | include / intrman.h |

---

## PS2SDK: iop/system/loadfile -&gt; ioman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000250_000242.html>

###### loadfile → ioman Relation
| File in iop/system/loadfile | Includes file in iop/system/ioman |
| src / irx_imports.h | include / ioman.h |

---

## PS2SDK: iop/system/loadfile -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000250_000248.html>

###### loadfile → loadcore Relation
| File in iop/system/loadfile | Includes file in iop/system/loadcore |
| src / irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/loadfile -&gt; modload Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000250_000252.html>

###### loadfile → modload Relation
| File in iop/system/loadfile | Includes file in iop/system/modload |
| src / irx_imports.h | include / xmodload.h |

---

## PS2SDK: iop/system/loadfile -&gt; sifman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000250_000266.html>

###### loadfile → sifman Relation
| File in iop/system/loadfile | Includes file in iop/system/sifman |
| src / irx_imports.h | include / sifman.h |

---

## PS2SDK: iop/system/loadfile -&gt; stdio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000250_000272.html>

###### loadfile → stdio Relation
| File in iop/system/loadfile | Includes file in iop/system/stdio |
| src / irx_imports.h | include / stdio.h |

---

## PS2SDK: iop/system/loadfile -&gt; sysclib Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000250_000274.html>

###### loadfile → sysclib Relation
| File in iop/system/loadfile | Includes file in iop/system/sysclib |
| src / irx_imports.h | include / sysclib.h |

---

## PS2SDK: iop/system/loadfile -&gt; threadman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000250_000276.html>

###### loadfile → threadman Relation
| File in iop/system/loadfile | Includes file in iop/system/threadman |
| src / irx_imports.h | include / thbase.h |

---

## PS2SDK: iop/system/loadfile -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000250_000537.html>

###### loadfile → kernel Relation
| File in iop/system/loadfile | Includes file in iop/kernel |
| src / eeelfloader.c | include / kerr.h |
| src / irx_imports.h | include / irx.h |
| src / loadfile.c | include / kerr.h |

---

## PS2SDK: iop/system/loadfile/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000251_000000.html>

###### src → common Relation
| File in iop/system/loadfile/src | Includes file in common |
| loadfile.c | include / loadfile-common.h |

---

## PS2SDK: iop/system/loadfile/src -&gt; intrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000251_000240.html>

###### src → intrman Relation
| File in iop/system/loadfile/src | Includes file in iop/system/intrman |
| irx_imports.h | include / intrman.h |

---

## PS2SDK: iop/system/loadfile/src -&gt; ioman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000251_000242.html>

###### src → ioman Relation
| File in iop/system/loadfile/src | Includes file in iop/system/ioman |
| irx_imports.h | include / ioman.h |

---

## PS2SDK: iop/system/loadfile/src -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000251_000248.html>

###### src → loadcore Relation
| File in iop/system/loadfile/src | Includes file in iop/system/loadcore |
| irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/loadfile/src -&gt; modload Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000251_000252.html>

###### src → modload Relation
| File in iop/system/loadfile/src | Includes file in iop/system/modload |
| irx_imports.h | include / xmodload.h |

---

## PS2SDK: iop/system/loadfile/src -&gt; sifman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000251_000266.html>

###### src → sifman Relation
| File in iop/system/loadfile/src | Includes file in iop/system/sifman |
| irx_imports.h | include / sifman.h |

---

## PS2SDK: iop/system/loadfile/src -&gt; stdio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000251_000272.html>

###### src → stdio Relation
| File in iop/system/loadfile/src | Includes file in iop/system/stdio |
| irx_imports.h | include / stdio.h |

---

## PS2SDK: iop/system/loadfile/src -&gt; sysclib Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000251_000274.html>

###### src → sysclib Relation
| File in iop/system/loadfile/src | Includes file in iop/system/sysclib |
| irx_imports.h | include / sysclib.h |

---

## PS2SDK: iop/system/loadfile/src -&gt; threadman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000251_000276.html>

###### src → threadman Relation
| File in iop/system/loadfile/src | Includes file in iop/system/threadman |
| irx_imports.h | include / thbase.h |

---

## PS2SDK: iop/system/loadfile/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000251_000537.html>

###### src → kernel Relation
| File in iop/system/loadfile/src | Includes file in iop/kernel |
| eeelfloader.c | include / kerr.h |
| irx_imports.h | include / irx.h |
| loadfile.c | include / kerr.h |

---

## PS2SDK: iop/system/modload -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000252_000000.html>

###### modload → common Relation
| File in iop/system/modload | Includes file in common |
| src / modload.c | include / mipscopaccess.h |

---

## PS2SDK: iop/system/modload -&gt; intrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000252_000240.html>

###### modload → intrman Relation
| File in iop/system/modload | Includes file in iop/system/intrman |
| src / irx_imports.h | include / intrman.h |

---

## PS2SDK: iop/system/modload -&gt; ioman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000252_000242.html>

###### modload → ioman Relation
| File in iop/system/modload | Includes file in iop/system/ioman |
| src / irx_imports.h | include / ioman.h |

---

## PS2SDK: iop/system/modload -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000252_000248.html>

###### modload → loadcore Relation
| File in iop/system/modload | Includes file in iop/system/loadcore |
| src / irx_imports.h | include / xloadcore.h |

---

## PS2SDK: iop/system/modload -&gt; stdio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000252_000272.html>

###### modload → stdio Relation
| File in iop/system/modload | Includes file in iop/system/stdio |
| src / irx_imports.h | include / stdio.h |

---

## PS2SDK: iop/system/modload -&gt; sysclib Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000252_000274.html>

###### modload → sysclib Relation
| File in iop/system/modload | Includes file in iop/system/sysclib |
| src / irx_imports.h | include / sysclib.h |

---

## PS2SDK: iop/system/modload -&gt; threadman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000252_000276.html>

###### modload → threadman Relation
| File in iop/system/modload | Includes file in iop/system/threadman |
| src / irx_imports.h | include / thbase.h |
| src / irx_imports.h | include / thevent.h |
| src / irx_imports.h | include / thsemap.h |

---

## PS2SDK: iop/system/modload -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000252_000537.html>

###### modload → kernel Relation
| File in iop/system/modload | Includes file in iop/kernel |
| include / modload.h | include / irx.h |
| src / irx_imports.h | include / irx.h |
| src / modload.c | include / kerr.h |

---

## PS2SDK: iop/system/modload/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000253_000000.html>

###### src → common Relation
| File in iop/system/modload/src | Includes file in common |
| modload.c | include / mipscopaccess.h |

---

## PS2SDK: iop/system/modload/src -&gt; intrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000253_000240.html>

###### src → intrman Relation
| File in iop/system/modload/src | Includes file in iop/system/intrman |
| irx_imports.h | include / intrman.h |

---

## PS2SDK: iop/system/modload/src -&gt; ioman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000253_000242.html>

###### src → ioman Relation
| File in iop/system/modload/src | Includes file in iop/system/ioman |
| irx_imports.h | include / ioman.h |

---

## PS2SDK: iop/system/modload/src -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000253_000248.html>

###### src → loadcore Relation
| File in iop/system/modload/src | Includes file in iop/system/loadcore |
| irx_imports.h | include / xloadcore.h |

---

## PS2SDK: iop/system/modload/src -&gt; stdio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000253_000272.html>

###### src → stdio Relation
| File in iop/system/modload/src | Includes file in iop/system/stdio |
| irx_imports.h | include / stdio.h |

---

## PS2SDK: iop/system/modload/src -&gt; sysclib Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000253_000274.html>

###### src → sysclib Relation
| File in iop/system/modload/src | Includes file in iop/system/sysclib |
| irx_imports.h | include / sysclib.h |

---

## PS2SDK: iop/system/modload/src -&gt; threadman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000253_000276.html>

###### src → threadman Relation
| File in iop/system/modload/src | Includes file in iop/system/threadman |
| irx_imports.h | include / thbase.h |
| irx_imports.h | include / thevent.h |
| irx_imports.h | include / thsemap.h |

---

## PS2SDK: iop/system/modload/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000253_000537.html>

###### src → kernel Relation
| File in iop/system/modload/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |
| modload.c | include / kerr.h |

---

## PS2SDK: iop/system/modload/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000253_000576.html>

###### src → include Relation
| File in iop/system/modload/src | Includes file in iop/system/modload/include |
| modload.c | modload.h |
| modload.c | xmodload.h |

---

## PS2SDK: iop/system/msifrpc -&gt; intrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000254_000240.html>

###### msifrpc → intrman Relation
| File in iop/system/msifrpc | Includes file in iop/system/intrman |
| src / irx_imports.h | include / intrman.h |

---

## PS2SDK: iop/system/msifrpc -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000254_000248.html>

###### msifrpc → loadcore Relation
| File in iop/system/msifrpc | Includes file in iop/system/loadcore |
| src / irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/msifrpc -&gt; sifman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000254_000266.html>

###### msifrpc → sifman Relation
| File in iop/system/msifrpc | Includes file in iop/system/sifman |
| src / irx_imports.h | include / sifman.h |

---

## PS2SDK: iop/system/msifrpc -&gt; stdio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000254_000272.html>

###### msifrpc → stdio Relation
| File in iop/system/msifrpc | Includes file in iop/system/stdio |
| src / irx_imports.h | include / stdio.h |

---

## PS2SDK: iop/system/msifrpc -&gt; threadman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000254_000276.html>

###### msifrpc → threadman Relation
| File in iop/system/msifrpc | Includes file in iop/system/threadman |
| src / irx_imports.h | include / thbase.h |
| src / irx_imports.h | include / thmsgbx.h |

---

## PS2SDK: iop/system/msifrpc -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000254_000537.html>

###### msifrpc → kernel Relation
| File in iop/system/msifrpc | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |
| src / msifrpc.c | include / kerr.h |

---

## PS2SDK: iop/system/msifrpc/src -&gt; intrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000255_000240.html>

###### src → intrman Relation
| File in iop/system/msifrpc/src | Includes file in iop/system/intrman |
| irx_imports.h | include / intrman.h |

---

## PS2SDK: iop/system/msifrpc/src -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000255_000248.html>

###### src → loadcore Relation
| File in iop/system/msifrpc/src | Includes file in iop/system/loadcore |
| irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/msifrpc/src -&gt; sifman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000255_000266.html>

###### src → sifman Relation
| File in iop/system/msifrpc/src | Includes file in iop/system/sifman |
| irx_imports.h | include / sifman.h |

---

## PS2SDK: iop/system/msifrpc/src -&gt; stdio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000255_000272.html>

###### src → stdio Relation
| File in iop/system/msifrpc/src | Includes file in iop/system/stdio |
| irx_imports.h | include / stdio.h |

---

## PS2SDK: iop/system/msifrpc/src -&gt; threadman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000255_000276.html>

###### src → threadman Relation
| File in iop/system/msifrpc/src | Includes file in iop/system/threadman |
| irx_imports.h | include / thbase.h |
| irx_imports.h | include / thmsgbx.h |

---

## PS2SDK: iop/system/msifrpc/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000255_000537.html>

###### src → kernel Relation
| File in iop/system/msifrpc/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |
| msifrpc.c | include / kerr.h |

---

## PS2SDK: iop/system/reboot -&gt; intrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000256_000240.html>

###### reboot → intrman Relation
| File in iop/system/reboot | Includes file in iop/system/intrman |
| src / irx_imports.h | include / intrman.h |

---

## PS2SDK: iop/system/reboot -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000256_000248.html>

###### reboot → loadcore Relation
| File in iop/system/reboot | Includes file in iop/system/loadcore |
| src / irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/reboot -&gt; modload Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000256_000252.html>

###### reboot → modload Relation
| File in iop/system/reboot | Includes file in iop/system/modload |
| src / irx_imports.h | include / modload.h |

---

## PS2SDK: iop/system/reboot -&gt; sifman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000256_000266.html>

###### reboot → sifman Relation
| File in iop/system/reboot | Includes file in iop/system/sifman |
| src / irx_imports.h | include / sifman.h |

---

## PS2SDK: iop/system/reboot -&gt; stdio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000256_000272.html>

###### reboot → stdio Relation
| File in iop/system/reboot | Includes file in iop/system/stdio |
| src / irx_imports.h | include / stdio.h |

---

## PS2SDK: iop/system/reboot -&gt; threadman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000256_000276.html>

###### reboot → threadman Relation
| File in iop/system/reboot | Includes file in iop/system/threadman |
| src / irx_imports.h | include / thbase.h |
| src / irx_imports.h | include / thevent.h |

---

## PS2SDK: iop/system/reboot -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000256_000537.html>

###### reboot → kernel Relation
| File in iop/system/reboot | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/system/reboot/src -&gt; intrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000257_000240.html>

###### src → intrman Relation
| File in iop/system/reboot/src | Includes file in iop/system/intrman |
| irx_imports.h | include / intrman.h |

---

## PS2SDK: iop/system/reboot/src -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000257_000248.html>

###### src → loadcore Relation
| File in iop/system/reboot/src | Includes file in iop/system/loadcore |
| irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/reboot/src -&gt; modload Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000257_000252.html>

###### src → modload Relation
| File in iop/system/reboot/src | Includes file in iop/system/modload |
| irx_imports.h | include / modload.h |

---

## PS2SDK: iop/system/reboot/src -&gt; sifman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000257_000266.html>

###### src → sifman Relation
| File in iop/system/reboot/src | Includes file in iop/system/sifman |
| irx_imports.h | include / sifman.h |

---

## PS2SDK: iop/system/reboot/src -&gt; stdio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000257_000272.html>

###### src → stdio Relation
| File in iop/system/reboot/src | Includes file in iop/system/stdio |
| irx_imports.h | include / stdio.h |

---

## PS2SDK: iop/system/reboot/src -&gt; threadman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000257_000276.html>

###### src → threadman Relation
| File in iop/system/reboot/src | Includes file in iop/system/threadman |
| irx_imports.h | include / thbase.h |
| irx_imports.h | include / thevent.h |

---

## PS2SDK: iop/system/reboot/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000257_000537.html>

###### src → kernel Relation
| File in iop/system/reboot/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/system/rmreset -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000258_000000.html>

###### rmreset → common Relation
| File in iop/system/rmreset | Includes file in common |
| src / rmreset.c | include / iop_mmio_hwport.h |

---

## PS2SDK: iop/system/rmreset -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000258_000248.html>

###### rmreset → loadcore Relation
| File in iop/system/rmreset | Includes file in iop/system/loadcore |
| src / rmreset.c | include / loadcore.h |

---

## PS2SDK: iop/system/rmreset -&gt; stdio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000258_000272.html>

###### rmreset → stdio Relation
| File in iop/system/rmreset | Includes file in iop/system/stdio |
| src / irx_imports.h | include / stdio.h |

---

## PS2SDK: iop/system/rmreset -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000258_000537.html>

###### rmreset → kernel Relation
| File in iop/system/rmreset | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/system/rmreset/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000259_000000.html>

###### src → common Relation
| File in iop/system/rmreset/src | Includes file in common |
| rmreset.c | include / iop_mmio_hwport.h |

---

## PS2SDK: iop/system/rmreset/src -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000259_000248.html>

###### src → loadcore Relation
| File in iop/system/rmreset/src | Includes file in iop/system/loadcore |
| rmreset.c | include / loadcore.h |

---

## PS2SDK: iop/system/rmreset/src -&gt; stdio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000259_000272.html>

###### src → stdio Relation
| File in iop/system/rmreset/src | Includes file in iop/system/stdio |
| irx_imports.h | include / stdio.h |

---

## PS2SDK: iop/system/rmreset/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000259_000537.html>

###### src → kernel Relation
| File in iop/system/rmreset/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/system/sbusintr -&gt; intrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000260_000240.html>

###### sbusintr → intrman Relation
| File in iop/system/sbusintr | Includes file in iop/system/intrman |
| src / irx_imports.h | include / intrman.h |
| src / sbusintr.c | include / intrman.h |

---

## PS2SDK: iop/system/sbusintr -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000260_000248.html>

###### sbusintr → loadcore Relation
| File in iop/system/sbusintr | Includes file in iop/system/loadcore |
| src / irx_imports.h | include / loadcore.h |
| src / sbusintr.c | include / loadcore.h |

---

## PS2SDK: iop/system/sbusintr -&gt; sifman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000260_000266.html>

###### sbusintr → sifman Relation
| File in iop/system/sbusintr | Includes file in iop/system/sifman |
| src / irx_imports.h | include / sifman.h |
| src / sbusintr.c | include / sifman.h |

---

## PS2SDK: iop/system/sbusintr -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000260_000537.html>

###### sbusintr → kernel Relation
| File in iop/system/sbusintr | Includes file in iop/kernel |
| include / sbusintr.h | include / irx.h |
| src / irx_imports.h | include / irx.h |
| src / sbusintr.c | include / defs.h |
| src / sbusintr.c | include / irx.h |

---

## PS2SDK: iop/system/sbusintr/src -&gt; intrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000261_000240.html>

###### src → intrman Relation
| File in iop/system/sbusintr/src | Includes file in iop/system/intrman |
| irx_imports.h | include / intrman.h |
| sbusintr.c | include / intrman.h |

---

## PS2SDK: iop/system/sbusintr/src -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000261_000248.html>

###### src → loadcore Relation
| File in iop/system/sbusintr/src | Includes file in iop/system/loadcore |
| irx_imports.h | include / loadcore.h |
| sbusintr.c | include / loadcore.h |

---

## PS2SDK: iop/system/sbusintr/src -&gt; sifman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000261_000266.html>

###### src → sifman Relation
| File in iop/system/sbusintr/src | Includes file in iop/system/sifman |
| irx_imports.h | include / sifman.h |
| sbusintr.c | include / sifman.h |

---

## PS2SDK: iop/system/sbusintr/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000261_000537.html>

###### src → kernel Relation
| File in iop/system/sbusintr/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |
| sbusintr.c | include / defs.h |
| sbusintr.c | include / irx.h |

---

## PS2SDK: iop/system/sbusintr/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000261_000578.html>

###### src → include Relation
| File in iop/system/sbusintr/src | Includes file in iop/system/sbusintr/include |
| sbusintr.c | sbusintr.h |

---

## PS2SDK: iop/system/sifcmd -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000262_000000.html>

###### sifcmd → common Relation
| File in iop/system/sifcmd | Includes file in common |
| include / sifcmd.h | include / sifcmd-common.h |
| include / sifcmd.h | include / sifrpc-common.h |

---

## PS2SDK: iop/system/sifcmd -&gt; intrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000262_000240.html>

###### sifcmd → intrman Relation
| File in iop/system/sifcmd | Includes file in iop/system/intrman |
| src / irx_imports.h | include / intrman.h |

---

## PS2SDK: iop/system/sifcmd -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000262_000248.html>

###### sifcmd → loadcore Relation
| File in iop/system/sifcmd | Includes file in iop/system/loadcore |
| src / irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/sifcmd -&gt; sifman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000262_000266.html>

###### sifcmd → sifman Relation
| File in iop/system/sifcmd | Includes file in iop/system/sifman |
| src / irx_imports.h | include / sifman.h |

---

## PS2SDK: iop/system/sifcmd -&gt; stdio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000262_000272.html>

###### sifcmd → stdio Relation
| File in iop/system/sifcmd | Includes file in iop/system/stdio |
| src / irx_imports.h | include / stdio.h |

---

## PS2SDK: iop/system/sifcmd -&gt; threadman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000262_000276.html>

###### sifcmd → threadman Relation
| File in iop/system/sifcmd | Includes file in iop/system/threadman |
| src / irx_imports.h | include / thbase.h |
| src / irx_imports.h | include / thevent.h |

---

## PS2SDK: iop/system/sifcmd -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000262_000537.html>

###### sifcmd → kernel Relation
| File in iop/system/sifcmd | Includes file in iop/kernel |
| include / sifcmd.h | include / irx.h |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/system/sifcmd/src -&gt; intrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000263_000240.html>

###### src → intrman Relation
| File in iop/system/sifcmd/src | Includes file in iop/system/intrman |
| irx_imports.h | include / intrman.h |

---

## PS2SDK: iop/system/sifcmd/src -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000263_000248.html>

###### src → loadcore Relation
| File in iop/system/sifcmd/src | Includes file in iop/system/loadcore |
| irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/sifcmd/src -&gt; sifman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000263_000266.html>

###### src → sifman Relation
| File in iop/system/sifcmd/src | Includes file in iop/system/sifman |
| irx_imports.h | include / sifman.h |

---

## PS2SDK: iop/system/sifcmd/src -&gt; stdio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000263_000272.html>

###### src → stdio Relation
| File in iop/system/sifcmd/src | Includes file in iop/system/stdio |
| irx_imports.h | include / stdio.h |

---

## PS2SDK: iop/system/sifcmd/src -&gt; threadman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000263_000276.html>

###### src → threadman Relation
| File in iop/system/sifcmd/src | Includes file in iop/system/threadman |
| irx_imports.h | include / thbase.h |
| irx_imports.h | include / thevent.h |

---

## PS2SDK: iop/system/sifcmd/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000263_000537.html>

###### src → kernel Relation
| File in iop/system/sifcmd/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/system/sifinit -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000264_000248.html>

###### sifinit → loadcore Relation
| File in iop/system/sifinit | Includes file in iop/system/loadcore |
| src / irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/sifinit -&gt; sifman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000264_000266.html>

###### sifinit → sifman Relation
| File in iop/system/sifinit | Includes file in iop/system/sifman |
| src / irx_imports.h | include / sifman.h |

---

## PS2SDK: iop/system/sifinit -&gt; stdio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000264_000272.html>

###### sifinit → stdio Relation
| File in iop/system/sifinit | Includes file in iop/system/stdio |
| src / irx_imports.h | include / stdio.h |

---

## PS2SDK: iop/system/sifinit -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000264_000537.html>

###### sifinit → kernel Relation
| File in iop/system/sifinit | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/system/sifinit/src -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000265_000248.html>

###### src → loadcore Relation
| File in iop/system/sifinit/src | Includes file in iop/system/loadcore |
| irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/sifinit/src -&gt; sifman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000265_000266.html>

###### src → sifman Relation
| File in iop/system/sifinit/src | Includes file in iop/system/sifman |
| irx_imports.h | include / sifman.h |

---

## PS2SDK: iop/system/sifinit/src -&gt; stdio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000265_000272.html>

###### src → stdio Relation
| File in iop/system/sifinit/src | Includes file in iop/system/stdio |
| irx_imports.h | include / stdio.h |

---

## PS2SDK: iop/system/sifinit/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000265_000537.html>

###### src → kernel Relation
| File in iop/system/sifinit/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/system/sifman -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000266_000000.html>

###### sifman → common Relation
| File in iop/system/sifman | Includes file in common |
| src / sifman.c | include / mipscopaccess.h |
| src / sifman.c | include / iop_mmio_hwport.h |
| src / sifman.c | include / sif_mmio_hwport.h |

---

## PS2SDK: iop/system/sifman -&gt; intrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000266_000240.html>

###### sifman → intrman Relation
| File in iop/system/sifman | Includes file in iop/system/intrman |
| src / irx_imports.h | include / intrman.h |

---

## PS2SDK: iop/system/sifman -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000266_000248.html>

###### sifman → loadcore Relation
| File in iop/system/sifman | Includes file in iop/system/loadcore |
| src / irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/sifman -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000266_000537.html>

###### sifman → kernel Relation
| File in iop/system/sifman | Includes file in iop/kernel |
| include / sifman.h | include / irx.h |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/system/sifman/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000267_000000.html>

###### src → common Relation
| File in iop/system/sifman/src | Includes file in common |
| sifman.c | include / iop_mmio_hwport.h |
| sifman.c | include / mipscopaccess.h |
| sifman.c | include / sif_mmio_hwport.h |

---

## PS2SDK: iop/system/sifman/src -&gt; intrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000267_000240.html>

###### src → intrman Relation
| File in iop/system/sifman/src | Includes file in iop/system/intrman |
| irx_imports.h | include / intrman.h |

---

## PS2SDK: iop/system/sifman/src -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000267_000248.html>

###### src → loadcore Relation
| File in iop/system/sifman/src | Includes file in iop/system/loadcore |
| irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/sifman/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000267_000537.html>

###### src → kernel Relation
| File in iop/system/sifman/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/system/sifman/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000267_000579.html>

###### src → include Relation
| File in iop/system/sifman/src | Includes file in iop/system/sifman/include |
| sifman.c | sifman.h |

---

## PS2SDK: iop/system/siftoo -&gt; intrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000268_000240.html>

###### siftoo → intrman Relation
| File in iop/system/siftoo | Includes file in iop/system/intrman |
| src / irx_imports.h | include / intrman.h |
| src / siftoo.c | include / intrman.h |

---

## PS2SDK: iop/system/siftoo -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000268_000248.html>

###### siftoo → loadcore Relation
| File in iop/system/siftoo | Includes file in iop/system/loadcore |
| src / irx_imports.h | include / loadcore.h |
| src / siftoo.c | include / loadcore.h |

---

## PS2SDK: iop/system/siftoo -&gt; sbusintr Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000268_000260.html>

###### siftoo → sbusintr Relation
| File in iop/system/siftoo | Includes file in iop/system/sbusintr |
| src / irx_imports.h | include / sbusintr.h |
| src / pipe.c | include / sbusintr.h |
| src / siftoo.c | include / sbusintr.h |

---

## PS2SDK: iop/system/siftoo -&gt; sifman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000268_000266.html>

###### siftoo → sifman Relation
| File in iop/system/siftoo | Includes file in iop/system/sifman |
| src / irx_imports.h | include / sifman.h |
| src / siftoo.c | include / sifman.h |

---

## PS2SDK: iop/system/siftoo -&gt; stdio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000268_000272.html>

###### siftoo → stdio Relation
| File in iop/system/siftoo | Includes file in iop/system/stdio |
| src / irx_imports.h | include / stdio.h |
| src / siftoo.c | include / stdio.h |

---

## PS2SDK: iop/system/siftoo -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000268_000537.html>

###### siftoo → kernel Relation
| File in iop/system/siftoo | Includes file in iop/kernel |
| include / siftoo.h | include / irx.h |
| src / irx_imports.h | include / irx.h |
| src / pipe.c | include / defs.h |
| src / siftoo.c | include / defs.h |
| src / siftoo.c | include / irx.h |

---

## PS2SDK: iop/system/siftoo/src -&gt; intrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000269_000240.html>

###### src → intrman Relation
| File in iop/system/siftoo/src | Includes file in iop/system/intrman |
| irx_imports.h | include / intrman.h |
| siftoo.c | include / intrman.h |

---

## PS2SDK: iop/system/siftoo/src -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000269_000248.html>

###### src → loadcore Relation
| File in iop/system/siftoo/src | Includes file in iop/system/loadcore |
| irx_imports.h | include / loadcore.h |
| siftoo.c | include / loadcore.h |

---

## PS2SDK: iop/system/siftoo/src -&gt; sbusintr Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000269_000260.html>

###### src → sbusintr Relation
| File in iop/system/siftoo/src | Includes file in iop/system/sbusintr |
| irx_imports.h | include / sbusintr.h |
| pipe.c | include / sbusintr.h |
| siftoo.c | include / sbusintr.h |

---

## PS2SDK: iop/system/siftoo/src -&gt; sifman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000269_000266.html>

###### src → sifman Relation
| File in iop/system/siftoo/src | Includes file in iop/system/sifman |
| irx_imports.h | include / sifman.h |
| siftoo.c | include / sifman.h |

---

## PS2SDK: iop/system/siftoo/src -&gt; stdio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000269_000272.html>

###### src → stdio Relation
| File in iop/system/siftoo/src | Includes file in iop/system/stdio |
| irx_imports.h | include / stdio.h |
| siftoo.c | include / stdio.h |

---

## PS2SDK: iop/system/siftoo/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000269_000537.html>

###### src → kernel Relation
| File in iop/system/siftoo/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |
| pipe.c | include / defs.h |
| siftoo.c | include / defs.h |
| siftoo.c | include / irx.h |

---

## PS2SDK: iop/system/siftoo/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000269_000580.html>

###### src → include Relation
| File in iop/system/siftoo/src | Includes file in iop/system/siftoo/include |
| pipe.c | siftoo.h |
| siftoo.c | siftoo.h |

---

## PS2SDK: iop/system/ssbusc -&gt; intrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000270_000240.html>

###### ssbusc → intrman Relation
| File in iop/system/ssbusc | Includes file in iop/system/intrman |
| src / irx_imports.h | include / intrman.h |

---

## PS2SDK: iop/system/ssbusc -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000270_000248.html>

###### ssbusc → loadcore Relation
| File in iop/system/ssbusc | Includes file in iop/system/loadcore |
| src / irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/ssbusc -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000270_000537.html>

###### ssbusc → kernel Relation
| File in iop/system/ssbusc | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |
| include / ssbusc.h | include / irx.h |

---

## PS2SDK: iop/system/ssbusc/src -&gt; intrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000271_000240.html>

###### src → intrman Relation
| File in iop/system/ssbusc/src | Includes file in iop/system/intrman |
| irx_imports.h | include / intrman.h |

---

## PS2SDK: iop/system/ssbusc/src -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000271_000248.html>

###### src → loadcore Relation
| File in iop/system/ssbusc/src | Includes file in iop/system/loadcore |
| irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/ssbusc/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000271_000537.html>

###### src → kernel Relation
| File in iop/system/ssbusc/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/system/ssbusc/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000271_000581.html>

###### src → include Relation
| File in iop/system/ssbusc/src | Includes file in iop/system/ssbusc/include |
| ssbusc.c | ssbusc.h |

---

## PS2SDK: iop/system/stdio -&gt; ioman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000272_000242.html>

###### stdio → ioman Relation
| File in iop/system/stdio | Includes file in iop/system/ioman |
| src / irx_imports.h | include / ioman_mod.h |

---

## PS2SDK: iop/system/stdio -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000272_000248.html>

###### stdio → loadcore Relation
| File in iop/system/stdio | Includes file in iop/system/loadcore |
| src / irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/stdio -&gt; sysclib Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000272_000274.html>

###### stdio → sysclib Relation
| File in iop/system/stdio | Includes file in iop/system/sysclib |
| src / irx_imports.h | include / sysclib.h |

---

## PS2SDK: iop/system/stdio -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000272_000537.html>

###### stdio → kernel Relation
| File in iop/system/stdio | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |
| include / stdio.h | include / irx.h |

---

## PS2SDK: iop/system/stdio -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000272_000572.html>

###### stdio → include Relation
| File in iop/system/stdio | Includes file in iop/system/ioman/include |
| src / irx_imports.h | ioman_mod.h |

---

## PS2SDK: iop/system/stdio/src -&gt; ioman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000273_000242.html>

###### src → ioman Relation
| File in iop/system/stdio/src | Includes file in iop/system/ioman |
| irx_imports.h | include / ioman_mod.h |

---

## PS2SDK: iop/system/stdio/src -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000273_000248.html>

###### src → loadcore Relation
| File in iop/system/stdio/src | Includes file in iop/system/loadcore |
| irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/stdio/src -&gt; sysclib Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000273_000274.html>

###### src → sysclib Relation
| File in iop/system/stdio/src | Includes file in iop/system/sysclib |
| irx_imports.h | include / sysclib.h |

---

## PS2SDK: iop/system/stdio/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000273_000537.html>

###### src → kernel Relation
| File in iop/system/stdio/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/system/sysclib -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000274_000000.html>

###### sysclib → common Relation
| File in iop/system/sysclib | Includes file in common |
| src / newlib / libc / machine / mips / machine / fenv-softfloat.h | include / errno.h |
| include / setjmp.h | include / tamtypes.h |

---

## PS2SDK: iop/system/sysclib -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000274_000248.html>

###### sysclib → loadcore Relation
| File in iop/system/sysclib | Includes file in iop/system/loadcore |
| src / irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/sysclib -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000274_000537.html>

###### sysclib → kernel Relation
| File in iop/system/sysclib | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |
| include / sysclib.h | include / irx.h |

---

## PS2SDK: iop/system/sysclib/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000275_000000.html>

###### src → common Relation
| File in iop/system/sysclib/src | Includes file in common |
| newlib / libc / machine / mips / machine / fenv-softfloat.h | include / errno.h |

---

## PS2SDK: iop/system/sysclib/src -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000275_000248.html>

###### src → loadcore Relation
| File in iop/system/sysclib/src | Includes file in iop/system/loadcore |
| irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/sysclib/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000275_000537.html>

###### src → kernel Relation
| File in iop/system/sysclib/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/system/sysclib/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000275_000583.html>

###### src → include Relation
| File in iop/system/sysclib/src | Includes file in iop/system/sysclib/include |
| nonstd / _wmemcopy.c | sysclib.h |
| nonstd / _wmemset.c | sysclib.h |
| nonstd / atob.c | sysclib.h |
| nonstd / ctype.c | sysclib.h |
| size_optimized / memchr.c | sysclib.h |
| size_optimized / memcpy.c | sysclib.h |
| size_optimized / memmove.c | sysclib.h |
| size_optimized / memset.c | sysclib.h |
| eyalroz_printf / printf.c | sysclib.h |
| size_optimized / rindex.c | sysclib.h |
| size_optimized / strchr.c | sysclib.h |
| size_optimized / strcmp.c | sysclib.h |
| newlib / libc / machine / mips / strncpy.c | sysclib.h |
| size_optimized / strrchr.c | sysclib.h |
| size_optimized / strspn.c | sysclib.h |
| size_optimized / strstr.c | sysclib.h |
| size_optimized / strtok.c | sysclib.h |
| size_optimized / strtok_r.c | sysclib.h |
| size_optimized / strtol.c | sysclib.h |
| size_optimized / strtoul.c | sysclib.h |
| size_optimized / sysclib_determine_base.c | sysclib.h |
| musl / ctype / tolower.c | sysclib.h |
| musl / ctype / toupper.c | sysclib.h |
| embeddedartistry_libc / stdlib / strtol.c | ctype.h |
| embeddedartistry_libc / stdlib / strtol.c | sysclib.h |
| embeddedartistry_libc / stdlib / strtoul.c | ctype.h |
| embeddedartistry_libc / stdlib / strtoul.c | sysclib.h |
| musl / string / bcmp.c | sysclib.h |
| musl / string / bcopy.c | sysclib.h |
| musl / string / bzero.c | sysclib.h |
| musl / string / index.c | sysclib.h |
| musl / string / memchr.c | sysclib.h |
| musl / string / memcmp.c | sysclib.h |
| musl / string / memcpy.c | sysclib.h |
| musl / string / memmove.c | sysclib.h |
| musl / string / memrchr.c | sysclib.h |
| musl / string / memset.c | sysclib.h |
| musl / string / rindex.c | sysclib.h |
| musl / string / stpcpy.c | sysclib.h |
| musl / string / stpncpy.c | sysclib.h |
| musl / string / strcat.c | sysclib.h |
| musl / string / strchr.c | sysclib.h |
| musl / string / strchrnul.c | sysclib.h |
| musl / string / strcmp.c | sysclib.h |
| musl / string / strcpy.c | sysclib.h |
| musl / string / strcspn.c | sysclib.h |
| musl / string / strlen.c | sysclib.h |
| musl / string / strncat.c | sysclib.h |
| musl / string / strncmp.c | sysclib.h |
| musl / string / strncpy.c | sysclib.h |
| musl / string / strpbrk.c | sysclib.h |
| musl / string / strrchr.c | sysclib.h |
| musl / string / strspn.c | sysclib.h |
| musl / string / strstr.c | sysclib.h |
| musl / string / strtok.c | sysclib.h |

---

## PS2SDK: iop/system/threadman -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000276_000000.html>

###### threadman → common Relation
| File in iop/system/threadman | Includes file in common |
| src / include / thcommon.h | include / tamtypes.h |

---

## PS2SDK: iop/system/threadman -&gt; heaplib Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000276_000236.html>

###### threadman → heaplib Relation
| File in iop/system/threadman | Includes file in iop/system/heaplib |
| src / irx_imports.h | include / heaplib.h |

---

## PS2SDK: iop/system/threadman -&gt; intrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000276_000240.html>

###### threadman → intrman Relation
| File in iop/system/threadman | Includes file in iop/system/intrman |
| src / irx_imports.h | include / intrman.h |

---

## PS2SDK: iop/system/threadman -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000276_000248.html>

###### threadman → loadcore Relation
| File in iop/system/threadman | Includes file in iop/system/loadcore |
| src / irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/threadman -&gt; stdio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000276_000272.html>

###### threadman → stdio Relation
| File in iop/system/threadman | Includes file in iop/system/stdio |
| src / irx_imports.h | include / stdio.h |

---

## PS2SDK: iop/system/threadman -&gt; sysclib Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000276_000274.html>

###### threadman → sysclib Relation
| File in iop/system/threadman | Includes file in iop/system/sysclib |
| src / irx_imports.h | include / sysclib.h |

---

## PS2SDK: iop/system/threadman -&gt; timrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000276_000278.html>

###### threadman → timrman Relation
| File in iop/system/threadman | Includes file in iop/system/timrman |
| src / irx_imports.h | include / xtimrman.h |

---

## PS2SDK: iop/system/threadman -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000276_000537.html>

###### threadman → kernel Relation
| File in iop/system/threadman | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |
| src / thbase.c | include / defs.h |
| src / thbase.c | include / kerr.h |
| include / thbase.h | include / irx.h |
| src / thcommon.c | include / defs.h |
| src / thcommon.c | include / kerr.h |
| src / thevent.c | include / kerr.h |
| include / thevent.h | include / irx.h |
| src / thfpool.c | include / kerr.h |
| include / thfpool.h | include / irx.h |
| src / thmsgbx.c | include / kerr.h |
| include / thmsgbx.h | include / irx.h |
| src / thsemap.c | include / kerr.h |
| include / thsemap.h | include / irx.h |
| src / thvpool.c | include / kerr.h |
| include / thvpool.h | include / irx.h |

---

## PS2SDK: iop/system/threadman/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000277_000000.html>

###### src → common Relation
| File in iop/system/threadman/src | Includes file in common |
| include / thcommon.h | include / tamtypes.h |

---

## PS2SDK: iop/system/threadman/src -&gt; heaplib Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000277_000236.html>

###### src → heaplib Relation
| File in iop/system/threadman/src | Includes file in iop/system/heaplib |
| irx_imports.h | include / heaplib.h |

---

## PS2SDK: iop/system/threadman/src -&gt; intrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000277_000240.html>

###### src → intrman Relation
| File in iop/system/threadman/src | Includes file in iop/system/intrman |
| irx_imports.h | include / intrman.h |

---

## PS2SDK: iop/system/threadman/src -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000277_000248.html>

###### src → loadcore Relation
| File in iop/system/threadman/src | Includes file in iop/system/loadcore |
| irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/threadman/src -&gt; stdio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000277_000272.html>

###### src → stdio Relation
| File in iop/system/threadman/src | Includes file in iop/system/stdio |
| irx_imports.h | include / stdio.h |

---

## PS2SDK: iop/system/threadman/src -&gt; sysclib Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000277_000274.html>

###### src → sysclib Relation
| File in iop/system/threadman/src | Includes file in iop/system/sysclib |
| irx_imports.h | include / sysclib.h |

---

## PS2SDK: iop/system/threadman/src -&gt; timrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000277_000278.html>

###### src → timrman Relation
| File in iop/system/threadman/src | Includes file in iop/system/timrman |
| irx_imports.h | include / xtimrman.h |

---

## PS2SDK: iop/system/threadman/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000277_000537.html>

###### src → kernel Relation
| File in iop/system/threadman/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |
| thbase.c | include / defs.h |
| thbase.c | include / kerr.h |
| thcommon.c | include / defs.h |
| thcommon.c | include / kerr.h |
| thevent.c | include / kerr.h |
| thfpool.c | include / kerr.h |
| thmsgbx.c | include / kerr.h |
| thsemap.c | include / kerr.h |
| thvpool.c | include / kerr.h |

---

## PS2SDK: iop/system/threadman/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000277_000598.html>

###### src → include Relation
| File in iop/system/threadman/src | Includes file in iop/system/threadman/include |
| thbase.c | thbase.h |
| thbase.c | thsemap.h |
| thbase.c | xthbase.h |
| thcommon.c | thevent.h |
| include / thcommon.h | thbase.h |
| include / thcommon.h | thmsgbx.h |
| thevent.c | thevent.h |
| thmsgbx.c | thmsgbx.h |
| thsemap.c | thsemap.h |

---

## PS2SDK: iop/system/timrman -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000278_000000.html>

###### timrman → common Relation
| File in iop/system/timrman | Includes file in common |
| src / timrman.c | include / mipscopaccess.h |
| src / timrman.c | include / tamtypes.h |

---

## PS2SDK: iop/system/timrman -&gt; intrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000278_000240.html>

###### timrman → intrman Relation
| File in iop/system/timrman | Includes file in iop/system/intrman |
| src / irx_imports.h | include / intrman.h |

---

## PS2SDK: iop/system/timrman -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000278_000248.html>

###### timrman → loadcore Relation
| File in iop/system/timrman | Includes file in iop/system/loadcore |
| src / irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/timrman -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000278_000537.html>

###### timrman → kernel Relation
| File in iop/system/timrman | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |
| src / timrman.c | include / kerr.h |
| include / timrman.h | include / irx.h |

---

## PS2SDK: iop/system/timrman/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000279_000000.html>

###### src → common Relation
| File in iop/system/timrman/src | Includes file in common |
| timrman.c | include / mipscopaccess.h |
| timrman.c | include / tamtypes.h |

---

## PS2SDK: iop/system/timrman/src -&gt; intrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000279_000240.html>

###### src → intrman Relation
| File in iop/system/timrman/src | Includes file in iop/system/intrman |
| irx_imports.h | include / intrman.h |

---

## PS2SDK: iop/system/timrman/src -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000279_000248.html>

###### src → loadcore Relation
| File in iop/system/timrman/src | Includes file in iop/system/loadcore |
| irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/timrman/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000279_000537.html>

###### src → kernel Relation
| File in iop/system/timrman/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |
| timrman.c | include / kerr.h |

---

## PS2SDK: iop/system/timrman/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000279_000600.html>

###### src → include Relation
| File in iop/system/timrman/src | Includes file in iop/system/timrman/include |
| timrman.c | timrman.h |
| timrman.c | xtimrman.h |

---

## PS2SDK: iop/system/udnl -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000280_000000.html>

###### udnl → common Relation
| File in iop/system/udnl | Includes file in common |
| src / udnl.c | include / mipscopaccess.h |

---

## PS2SDK: iop/system/udnl -&gt; dmacman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000280_000228.html>

###### udnl → dmacman Relation
| File in iop/system/udnl | Includes file in iop/system/dmacman |
| src / irx_imports.h | include / dmacman.h |
| src / udnl.c | include / dmacman.h |

---

## PS2SDK: iop/system/udnl -&gt; intrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000280_000240.html>

###### udnl → intrman Relation
| File in iop/system/udnl | Includes file in iop/system/intrman |
| src / irx_imports.h | include / intrman.h |
| src / udnl.c | include / intrman.h |

---

## PS2SDK: iop/system/udnl -&gt; ioman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000280_000242.html>

###### udnl → ioman Relation
| File in iop/system/udnl | Includes file in iop/system/ioman |
| src / irx_imports.h | include / ioman.h |
| src / udnl.c | include / ioman.h |

---

## PS2SDK: iop/system/udnl -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000280_000248.html>

###### udnl → loadcore Relation
| File in iop/system/udnl | Includes file in iop/system/loadcore |
| src / irx_imports.h | include / loadcore.h |
| src / udnl.c | include / loadcore.h |

---

## PS2SDK: iop/system/udnl -&gt; stdio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000280_000272.html>

###### udnl → stdio Relation
| File in iop/system/udnl | Includes file in iop/system/stdio |
| src / irx_imports.h | include / stdio.h |
| src / udnl.c | include / stdio.h |

---

## PS2SDK: iop/system/udnl -&gt; sysclib Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000280_000274.html>

###### udnl → sysclib Relation
| File in iop/system/udnl | Includes file in iop/system/sysclib |
| src / irx_imports.h | include / sysclib.h |
| src / udnl.c | include / sysclib.h |

---

## PS2SDK: iop/system/udnl -&gt; threadman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000280_000276.html>

###### udnl → threadman Relation
| File in iop/system/udnl | Includes file in iop/system/threadman |
| src / irx_imports.h | include / thbase.h |
| src / udnl.c | include / thbase.h |

---

## PS2SDK: iop/system/udnl -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000280_000537.html>

###### udnl → kernel Relation
| File in iop/system/udnl | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/system/udnl/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000281_000000.html>

###### src → common Relation
| File in iop/system/udnl/src | Includes file in common |
| udnl.c | include / mipscopaccess.h |

---

## PS2SDK: iop/system/udnl/src -&gt; dmacman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000281_000228.html>

###### src → dmacman Relation
| File in iop/system/udnl/src | Includes file in iop/system/dmacman |
| irx_imports.h | include / dmacman.h |
| udnl.c | include / dmacman.h |

---

## PS2SDK: iop/system/udnl/src -&gt; intrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000281_000240.html>

###### src → intrman Relation
| File in iop/system/udnl/src | Includes file in iop/system/intrman |
| irx_imports.h | include / intrman.h |
| udnl.c | include / intrman.h |

---

## PS2SDK: iop/system/udnl/src -&gt; ioman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000281_000242.html>

###### src → ioman Relation
| File in iop/system/udnl/src | Includes file in iop/system/ioman |
| irx_imports.h | include / ioman.h |
| udnl.c | include / ioman.h |

---

## PS2SDK: iop/system/udnl/src -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000281_000248.html>

###### src → loadcore Relation
| File in iop/system/udnl/src | Includes file in iop/system/loadcore |
| irx_imports.h | include / loadcore.h |
| udnl.c | include / loadcore.h |

---

## PS2SDK: iop/system/udnl/src -&gt; stdio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000281_000272.html>

###### src → stdio Relation
| File in iop/system/udnl/src | Includes file in iop/system/stdio |
| irx_imports.h | include / stdio.h |
| udnl.c | include / stdio.h |

---

## PS2SDK: iop/system/udnl/src -&gt; sysclib Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000281_000274.html>

###### src → sysclib Relation
| File in iop/system/udnl/src | Includes file in iop/system/sysclib |
| irx_imports.h | include / sysclib.h |
| udnl.c | include / sysclib.h |

---

## PS2SDK: iop/system/udnl/src -&gt; threadman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000281_000276.html>

###### src → threadman Relation
| File in iop/system/udnl/src | Includes file in iop/system/threadman |
| irx_imports.h | include / thbase.h |
| udnl.c | include / thbase.h |

---

## PS2SDK: iop/system/udnl/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000281_000537.html>

###### src → kernel Relation
| File in iop/system/udnl/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/system/vblank -&gt; intrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000282_000240.html>

###### vblank → intrman Relation
| File in iop/system/vblank | Includes file in iop/system/intrman |
| src / irx_imports.h | include / intrman.h |

---

## PS2SDK: iop/system/vblank -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000282_000248.html>

###### vblank → loadcore Relation
| File in iop/system/vblank | Includes file in iop/system/loadcore |
| src / irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/vblank -&gt; sysclib Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000282_000274.html>

###### vblank → sysclib Relation
| File in iop/system/vblank | Includes file in iop/system/sysclib |
| src / irx_imports.h | include / sysclib.h |

---

## PS2SDK: iop/system/vblank -&gt; threadman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000282_000276.html>

###### vblank → threadman Relation
| File in iop/system/vblank | Includes file in iop/system/threadman |
| src / irx_imports.h | include / thbase.h |
| src / irx_imports.h | include / thevent.h |

---

## PS2SDK: iop/system/vblank -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000282_000537.html>

###### vblank → kernel Relation
| File in iop/system/vblank | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |
| src / vblank.c | include / kerr.h |
| include / vblank.h | include / irx.h |

---

## PS2SDK: iop/system/vblank/src -&gt; intrman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000283_000240.html>

###### src → intrman Relation
| File in iop/system/vblank/src | Includes file in iop/system/intrman |
| irx_imports.h | include / intrman.h |

---

## PS2SDK: iop/system/vblank/src -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000283_000248.html>

###### src → loadcore Relation
| File in iop/system/vblank/src | Includes file in iop/system/loadcore |
| irx_imports.h | include / loadcore.h |

---

## PS2SDK: iop/system/vblank/src -&gt; sysclib Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000283_000274.html>

###### src → sysclib Relation
| File in iop/system/vblank/src | Includes file in iop/system/sysclib |
| irx_imports.h | include / sysclib.h |

---

## PS2SDK: iop/system/vblank/src -&gt; threadman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000283_000276.html>

###### src → threadman Relation
| File in iop/system/vblank/src | Includes file in iop/system/threadman |
| irx_imports.h | include / thbase.h |
| irx_imports.h | include / thevent.h |

---

## PS2SDK: iop/system/vblank/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000283_000537.html>

###### src → kernel Relation
| File in iop/system/vblank/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |
| vblank.c | include / kerr.h |

---

## PS2SDK: iop/system/vblank/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000283_000601.html>

###### src → include Relation
| File in iop/system/vblank/src | Includes file in iop/system/vblank/include |
| vblank.c | vblank.h |

---

## PS2SDK: iop/tcpip -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000284_000000.html>

###### tcpip → common Relation
| File in iop/tcpip | Includes file in common |
| tcpip-base / include / arch / cc.h | include / errno.h |
| tcpip-netman / src / irx_imports.h | include / netman.h |
| tcpip-netman / src / ps2ip.c | include / netman.h |
| tcpip / include / ps2ip.h | include / tcpip.h |
| tcpips / src / ps2ips.c | include / ps2ip_rpc.h |

---

## PS2SDK: iop/tcpip -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000284_000223.html>

###### tcpip → system Relation
| File in iop/tcpip | Includes file in iop/system |
| tcpip-netman / src / irx_imports.h | intrman / include / intrman.h |
| tcpip / src / irx_imports.h | intrman / include / intrman.h |
| tcpips / src / irx_imports.h | intrman / include / intrman.h |
| tcpip-netman / src / irx_imports.h | loadcore / include / loadcore.h |
| tcpip / src / irx_imports.h | loadcore / include / loadcore.h |
| tcpips / src / irx_imports.h | sifman / include / sifman.h |
| tcpip / src / irx_imports.h | stdio / include / stdio.h |
| tcpips / src / irx_imports.h | stdio / include / stdio.h |
| tcpip-netman / src / irx_imports.h | stdio / include / stdio.h |
| tcpip-netman / src / irx_imports.h | sysclib / include / sysclib.h |
| tcpip / src / irx_imports.h | sysclib / include / sysclib.h |
| tcpips / src / irx_imports.h | sysclib / include / sysclib.h |
| tcpip / src / irx_imports.h | threadman / include / thbase.h |
| tcpip-netman / src / irx_imports.h | threadman / include / thbase.h |
| tcpips / src / irx_imports.h | threadman / include / thbase.h |
| tcpip / src / irx_imports.h | threadman / include / thmsgbx.h |
| tcpip-netman / src / irx_imports.h | threadman / include / thmsgbx.h |
| tcpip / src / irx_imports.h | threadman / include / thsemap.h |
| tcpip-netman / src / irx_imports.h | threadman / include / thsemap.h |
| tcpip-netman / src / ps2ip.c | intrman / include / intrman.h |
| tcpip / src / ps2ip.c | intrman / include / intrman.h |
| tcpip-netman / src / ps2ip.c | loadcore / include / loadcore.h |
| tcpip / src / ps2ip.c | loadcore / include / loadcore.h |
| tcpip / src / ps2ip.c | stdio / include / stdio.h |
| tcpip-netman / src / ps2ip.c | stdio / include / stdio.h |
| tcpip / src / ps2ip.c | sysclib / include / sysclib.h |
| tcpip-netman / src / ps2ip.c | sysclib / include / sysclib.h |
| tcpip-netman / src / ps2ip.c | threadman / include / thbase.h |
| tcpip / src / ps2ip.c | threadman / include / thbase.h |
| tcpip / src / ps2ip.c | threadman / include / thevent.h |
| tcpip-netman / src / ps2ip.c | threadman / include / thevent.h |
| tcpips / src / ps2ips.c | intrman / include / intrman.h |
| tcpips / src / ps2ips.c | loadcore / include / loadcore.h |
| tcpips / src / ps2ips.c | sifman / include / sifman.h |
| tcpips / src / ps2ips.c | stdio / include / stdio.h |
| tcpips / src / ps2ips.c | sysclib / include / sysclib.h |
| tcpips / src / ps2ips.c | threadman / include / thbase.h |
| tcpip-base / sys_arch.c | stdio / include / stdio.h |
| tcpip-base / sys_arch.c | threadman / include / thsemap.h |
| tcpip-base / sys_arch.c | threadman / include / thbase.h |
| tcpip-base / sys_arch.c | threadman / include / thmsgbx.h |
| tcpip-base / sys_arch.c | sysclib / include / sysclib.h |
| tcpip-base / sys_arch.c | intrman / include / intrman.h |

---

## PS2SDK: iop/tcpip -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000284_000537.html>

###### tcpip → kernel Relation
| File in iop/tcpip | Includes file in iop/kernel |
| tcpip-base / include / arch / cc.h | include / sys / time.h |
| tcpip-netman / src / irx_imports.h | include / irx.h |
| tcpip / src / irx_imports.h | include / irx.h |
| tcpips / src / irx_imports.h | include / irx.h |
| tcpip / include / ps2ip.h | include / irx.h |
| tcpip / include / ps2ip.h | include / sys / time.h |

---

## PS2SDK: iop/tcpip/tcpip -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000285_000000.html>

###### tcpip → common Relation
| File in iop/tcpip/tcpip | Includes file in common |
| include / ps2ip.h | include / tcpip.h |

---

## PS2SDK: iop/tcpip/tcpip -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000285_000223.html>

###### tcpip → system Relation
| File in iop/tcpip/tcpip | Includes file in iop/system |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thmsgbx.h |
| src / irx_imports.h | threadman / include / thsemap.h |
| src / ps2ip.c | intrman / include / intrman.h |
| src / ps2ip.c | loadcore / include / loadcore.h |
| src / ps2ip.c | stdio / include / stdio.h |
| src / ps2ip.c | sysclib / include / sysclib.h |
| src / ps2ip.c | threadman / include / thbase.h |
| src / ps2ip.c | threadman / include / thevent.h |

---

## PS2SDK: iop/tcpip/tcpip -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000285_000537.html>

###### tcpip → kernel Relation
| File in iop/tcpip/tcpip | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |
| include / ps2ip.h | include / irx.h |
| include / ps2ip.h | include / sys / time.h |

---

## PS2SDK: iop/tcpip/tcpip/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000286_000223.html>

###### src → system Relation
| File in iop/tcpip/tcpip/src | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thmsgbx.h |
| irx_imports.h | threadman / include / thsemap.h |
| ps2ip.c | intrman / include / intrman.h |
| ps2ip.c | loadcore / include / loadcore.h |
| ps2ip.c | stdio / include / stdio.h |
| ps2ip.c | sysclib / include / sysclib.h |
| ps2ip.c | threadman / include / thbase.h |
| ps2ip.c | threadman / include / thevent.h |

---

## PS2SDK: iop/tcpip/tcpip/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000286_000537.html>

###### src → kernel Relation
| File in iop/tcpip/tcpip/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/tcpip/tcpip-netman -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000287_000000.html>

###### tcpip-netman → common Relation
| File in iop/tcpip/tcpip-netman | Includes file in common |
| src / irx_imports.h | include / netman.h |
| src / ps2ip.c | include / netman.h |

---

## PS2SDK: iop/tcpip/tcpip-netman -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000287_000223.html>

###### tcpip-netman → system Relation
| File in iop/tcpip/tcpip-netman | Includes file in iop/system |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thmsgbx.h |
| src / irx_imports.h | threadman / include / thsemap.h |
| src / ps2ip.c | intrman / include / intrman.h |
| src / ps2ip.c | loadcore / include / loadcore.h |
| src / ps2ip.c | stdio / include / stdio.h |
| src / ps2ip.c | sysclib / include / sysclib.h |
| src / ps2ip.c | threadman / include / thbase.h |
| src / ps2ip.c | threadman / include / thevent.h |

---

## PS2SDK: iop/tcpip/tcpip-netman -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000287_000537.html>

###### tcpip-netman → kernel Relation
| File in iop/tcpip/tcpip-netman | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/tcpip/tcpip-netman/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000288_000000.html>

###### src → common Relation
| File in iop/tcpip/tcpip-netman/src | Includes file in common |
| irx_imports.h | include / netman.h |
| ps2ip.c | include / netman.h |

---

## PS2SDK: iop/tcpip/tcpip-netman/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000288_000223.html>

###### src → system Relation
| File in iop/tcpip/tcpip-netman/src | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thmsgbx.h |
| irx_imports.h | threadman / include / thsemap.h |
| ps2ip.c | intrman / include / intrman.h |
| ps2ip.c | loadcore / include / loadcore.h |
| ps2ip.c | stdio / include / stdio.h |
| ps2ip.c | sysclib / include / sysclib.h |
| ps2ip.c | threadman / include / thbase.h |
| ps2ip.c | threadman / include / thevent.h |

---

## PS2SDK: iop/tcpip/tcpip-netman/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000288_000537.html>

###### src → kernel Relation
| File in iop/tcpip/tcpip-netman/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/tcpip/tcpips -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000289_000000.html>

###### tcpips → common Relation
| File in iop/tcpip/tcpips | Includes file in common |
| src / ps2ips.c | include / ps2ip_rpc.h |

---

## PS2SDK: iop/tcpip/tcpips -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000289_000223.html>

###### tcpips → system Relation
| File in iop/tcpip/tcpips | Includes file in iop/system |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | sifman / include / sifman.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / ps2ips.c | intrman / include / intrman.h |
| src / ps2ips.c | loadcore / include / loadcore.h |
| src / ps2ips.c | sifman / include / sifman.h |
| src / ps2ips.c | stdio / include / stdio.h |
| src / ps2ips.c | sysclib / include / sysclib.h |
| src / ps2ips.c | threadman / include / thbase.h |

---

## PS2SDK: iop/tcpip/tcpips -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000289_000537.html>

###### tcpips → kernel Relation
| File in iop/tcpip/tcpips | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/tcpip/tcpips/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000290_000000.html>

###### src → common Relation
| File in iop/tcpip/tcpips/src | Includes file in common |
| ps2ips.c | include / ps2ip_rpc.h |

---

## PS2SDK: iop/tcpip/tcpips/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000290_000223.html>

###### src → system Relation
| File in iop/tcpip/tcpips/src | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | sifman / include / sifman.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| ps2ips.c | intrman / include / intrman.h |
| ps2ips.c | loadcore / include / loadcore.h |
| ps2ips.c | sifman / include / sifman.h |
| ps2ips.c | stdio / include / stdio.h |
| ps2ips.c | sysclib / include / sysclib.h |
| ps2ips.c | threadman / include / thbase.h |

---

## PS2SDK: iop/tcpip/tcpips/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000290_000537.html>

###### src → kernel Relation
| File in iop/tcpip/tcpips/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/usb -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000291_000000.html>

###### usb → common Relation
| File in iop/usb | Includes file in common |
| usbhdfsd / src / api.c | include / errno.h |
| camera / src / ps2cam.c | include / tamtypes.h |
| keyboard / src / ps2kbd.c | include / errno.h |
| usbmass_bd / src / scsi.c | include / errno.h |
| usbhdfsd / src / usb_driver.c | include / errno.h |
| usbmass_bd / src / usb_mass.c | include / errno.h |
| usbmass_bd / src / usb_mass.c | include / usbhdfsd-common.h |
| usbhdfsd / include / usbhdfsd.h | include / usbhdfsd-common.h |

---

## PS2SDK: iop/usb -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000291_000056.html>

###### usb → cdvd Relation
| File in iop/usb | Includes file in iop/cdvd |
| usbhdfsd / src / api.c | cdvdman / include / cdvdman.h |
| usbhdfsd / src / irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/usb -&gt; fs Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000291_000113.html>

###### usb → fs Relation
| File in iop/usb | Includes file in iop/fs |
| usbmass_bd / src / irx_imports.h | bdm / include / bdm.h |
| usbmass_bd / src / scsi.c | bdm / include / bdm.h |

---

## PS2SDK: iop/usb -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000291_000223.html>

###### usb → system Relation
| File in iop/usb | Includes file in iop/system |
| usbhdfsd / src / api.c | stdio / include / stdio.h |
| usbhdfsd / src / api.c | sysclib / include / sysclib.h |
| keyboard / src / irx_imports.h | dmacman / include / dmacman.h |
| camera / src / irx_imports.h | dmacman / include / dmacman.h |
| usbd / src / irx_imports.h | intrman / include / intrman.h |
| usbhdfsd / src / irx_imports.h | intrman / include / intrman.h |
| keyboard / src / irx_imports.h | intrman / include / intrman.h |
| camera / src / irx_imports.h | intrman / include / intrman.h |
| mouse / src / irx_imports.h | intrman / include / intrman.h |
| usbmload / src / irx_imports.h | intrman / include / intrman.h |
| usbhdfsd / src / irx_imports.h | ioman / include / ioman.h |
| camera / src / irx_imports.h | ioman / include / ioman.h |
| keyboard / src / irx_imports.h | ioman / include / ioman.h |
| usbmload / src / irx_imports.h | ioman / include / ioman.h |
| usbd / src / irx_imports.h | loadcore / include / loadcore.h |
| usbhdfsd / src / irx_imports.h | loadcore / include / loadcore.h |
| mouse / src / irx_imports.h | loadcore / include / loadcore.h |
| usbmload / src / irx_imports.h | loadcore / include / loadcore.h |
| mouse / src / irx_imports.h | stdio / include / stdio.h |
| usbmload / src / irx_imports.h | stdio / include / stdio.h |
| keyboard / src / irx_imports.h | stdio / include / stdio.h |
| usbmass_bd / src / irx_imports.h | stdio / include / stdio.h |
| usbd / src / irx_imports.h | stdio / include / stdio.h |
| usbhdfsd / src / irx_imports.h | stdio / include / stdio.h |
| camera / src / irx_imports.h | stdio / include / stdio.h |
| usbmload / src / irx_imports.h | sysclib / include / sysclib.h |
| mouse / src / irx_imports.h | sysclib / include / sysclib.h |
| usbd / src / irx_imports.h | sysclib / include / sysclib.h |
| usbmass_bd / src / irx_imports.h | sysclib / include / sysclib.h |
| usbhdfsd / src / irx_imports.h | sysclib / include / sysclib.h |
| keyboard / src / irx_imports.h | sysclib / include / sysclib.h |
| camera / src / irx_imports.h | sysclib / include / sysclib.h |
| usbmload / src / irx_imports.h | threadman / include / thbase.h |
| mouse / src / irx_imports.h | threadman / include / thbase.h |
| usbd / src / irx_imports.h | threadman / include / thbase.h |
| usbmass_bd / src / irx_imports.h | threadman / include / thbase.h |
| keyboard / src / irx_imports.h | threadman / include / thbase.h |
| camera / src / irx_imports.h | threadman / include / thbase.h |
| usbhdfsd / src / irx_imports.h | threadman / include / thbase.h |
| usbmload / src / irx_imports.h | threadman / include / thevent.h |
| mouse / src / irx_imports.h | threadman / include / thevent.h |
| usbd / src / irx_imports.h | threadman / include / thevent.h |
| usbhdfsd / src / irx_imports.h | threadman / include / thevent.h |
| camera / src / irx_imports.h | threadman / include / thevent.h |
| keyboard / src / irx_imports.h | threadman / include / thevent.h |
| keyboard / src / irx_imports.h | threadman / include / thmsgbx.h |
| mouse / src / irx_imports.h | threadman / include / thmsgbx.h |
| camera / src / irx_imports.h | threadman / include / thmsgbx.h |
| keyboard / src / irx_imports.h | threadman / include / thsemap.h |
| usbmass_bd / src / irx_imports.h | threadman / include / thsemap.h |
| mouse / src / irx_imports.h | threadman / include / thsemap.h |
| usbhdfsd / src / irx_imports.h | threadman / include / thsemap.h |
| usbd / src / irx_imports.h | threadman / include / thsemap.h |
| camera / src / irx_imports.h | threadman / include / thsemap.h |
| camera / src / irx_imports.h | vblank / include / vblank.h |
| usbmload / src / irx_imports.h | modload / include / xmodload.h |
| usbmass_bd / src / main.c | loadcore / include / loadcore.h |
| usbmass_bd / src / main.c | stdio / include / stdio.h |
| camera / src / ps2cam.c | ioman / include / ioman.h |
| camera / src / ps2cam.c | loadcore / include / loadcore.h |
| camera / src / ps2cam.c | stdio / include / stdio.h |
| camera / src / ps2cam.c | sysclib / include / sysclib.h |
| camera / src / ps2cam.c | threadman / include / thbase.h |
| camera / src / ps2cam.c | threadman / include / thsemap.h |
| keyboard / src / ps2kbd.c | ioman / include / ioman.h |
| keyboard / src / ps2kbd.c | loadcore / include / loadcore.h |
| keyboard / src / ps2kbd.c | stdio / include / stdio.h |
| keyboard / src / ps2kbd.c | sysclib / include / sysclib.h |
| keyboard / src / ps2kbd.c | threadman / include / thbase.h |
| keyboard / src / ps2kbd.c | threadman / include / thevent.h |
| keyboard / src / ps2kbd.c | threadman / include / thsemap.h |
| mouse / src / ps2mouse.c | iomanx / include / iomanX.h |
| mouse / src / ps2mouse.c | loadcore / include / loadcore.h |
| mouse / src / ps2mouse.c | stdio / include / stdio.h |
| mouse / src / ps2mouse.c | sysclib / include / sysclib.h |
| mouse / src / ps2mouse.c | threadman / include / thbase.h |
| mouse / src / ps2mouse.c | threadman / include / thevent.h |
| mouse / src / ps2mouse.c | threadman / include / thsemap.h |
| usbmass_bd / src / scsi.c | stdio / include / stdio.h |
| usbmass_bd / src / scsi.c | sysclib / include / sysclib.h |
| usbmass_bd / src / scsi.c | threadman / include / thsemap.h |
| usbhdfsd / src / usb_driver.c | stdio / include / stdio.h |
| usbhdfsd / src / usb_driver.c | sysclib / include / sysclib.h |
| usbhdfsd / src / usb_driver.c | threadman / include / thsemap.h |
| usbmass_bd / src / usb_mass.c | stdio / include / stdio.h |
| usbmass_bd / src / usb_mass.c | sysclib / include / sysclib.h |
| usbmass_bd / src / usb_mass.c | threadman / include / thbase.h |
| usbmass_bd / src / usb_mass.c | threadman / include / thsemap.h |
| usbhdfsd / src / usbhdfsd.c | intrman / include / intrman.h |
| usbhdfsd / src / usbhdfsd.c | loadcore / include / loadcore.h |
| usbhdfsd / src / usbhdfsd.c | stdio / include / stdio.h |

---

## PS2SDK: iop/usb -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000291_000537.html>

###### usb → kernel Relation
| File in iop/usb | Includes file in iop/kernel |
| keyboard / src / irx_imports.h | include / irx.h |
| usbmass_bd / src / irx_imports.h | include / irx.h |
| usbmload / src / irx_imports.h | include / irx.h |
| usbd / src / irx_imports.h | include / irx.h |
| usbhdfsd / src / irx_imports.h | include / irx.h |
| mouse / src / irx_imports.h | include / irx.h |
| camera / src / irx_imports.h | include / irx.h |
| usbmass_bd / src / main.c | include / irx.h |
| usbd / include / usbd.h | include / irx.h |
| usbd / src / usbdpriv.h | include / defs.h |
| usbhdfsd / src / usbhdfsd.c | include / irx.h |
| usbhdfsd / include / usbhdfsd.h | include / irx.h |

---

## PS2SDK: iop/usb/camera -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000292_000000.html>

###### camera → common Relation
| File in iop/usb/camera | Includes file in common |
| src / ps2cam.c | include / tamtypes.h |

---

## PS2SDK: iop/usb/camera -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000292_000223.html>

###### camera → system Relation
| File in iop/usb/camera | Includes file in iop/system |
| src / irx_imports.h | dmacman / include / dmacman.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | ioman / include / ioman.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thevent.h |
| src / irx_imports.h | threadman / include / thmsgbx.h |
| src / irx_imports.h | threadman / include / thsemap.h |
| src / irx_imports.h | vblank / include / vblank.h |
| src / ps2cam.c | stdio / include / stdio.h |
| src / ps2cam.c | sysclib / include / sysclib.h |
| src / ps2cam.c | threadman / include / thbase.h |
| src / ps2cam.c | loadcore / include / loadcore.h |
| src / ps2cam.c | ioman / include / ioman.h |
| src / ps2cam.c | threadman / include / thsemap.h |

---

## PS2SDK: iop/usb/camera -&gt; usbd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000292_000298.html>

###### camera → usbd Relation
| File in iop/usb/camera | Includes file in iop/usb/usbd |
| src / irx_imports.h | include / usbd.h |
| src / ps2cam.c | include / usbd.h |
| src / ps2cam.c | include / usbd_macro.h |

---

## PS2SDK: iop/usb/camera -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000292_000537.html>

###### camera → kernel Relation
| File in iop/usb/camera | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/usb/camera/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000293_000000.html>

###### src → common Relation
| File in iop/usb/camera/src | Includes file in common |
| ps2cam.c | include / tamtypes.h |

---

## PS2SDK: iop/usb/camera/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000293_000223.html>

###### src → system Relation
| File in iop/usb/camera/src | Includes file in iop/system |
| irx_imports.h | dmacman / include / dmacman.h |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | ioman / include / ioman.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thevent.h |
| irx_imports.h | threadman / include / thmsgbx.h |
| irx_imports.h | threadman / include / thsemap.h |
| irx_imports.h | vblank / include / vblank.h |
| ps2cam.c | ioman / include / ioman.h |
| ps2cam.c | loadcore / include / loadcore.h |
| ps2cam.c | stdio / include / stdio.h |
| ps2cam.c | sysclib / include / sysclib.h |
| ps2cam.c | threadman / include / thbase.h |
| ps2cam.c | threadman / include / thsemap.h |

---

## PS2SDK: iop/usb/camera/src -&gt; usbd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000293_000298.html>

###### src → usbd Relation
| File in iop/usb/camera/src | Includes file in iop/usb/usbd |
| irx_imports.h | include / usbd.h |
| ps2cam.c | include / usbd.h |
| ps2cam.c | include / usbd_macro.h |

---

## PS2SDK: iop/usb/camera/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000293_000537.html>

###### src → kernel Relation
| File in iop/usb/camera/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/usb/camera/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000293_000602.html>

###### src → include Relation
| File in iop/usb/camera/src | Includes file in iop/usb/camera/include |
| ps2cam.c | ps2cam.h |

---

## PS2SDK: iop/usb/keyboard -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000294_000000.html>

###### keyboard → common Relation
| File in iop/usb/keyboard | Includes file in common |
| src / ps2kbd.c | include / errno.h |

---

## PS2SDK: iop/usb/keyboard -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000294_000223.html>

###### keyboard → system Relation
| File in iop/usb/keyboard | Includes file in iop/system |
| src / irx_imports.h | dmacman / include / dmacman.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | ioman / include / ioman.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thevent.h |
| src / irx_imports.h | threadman / include / thmsgbx.h |
| src / irx_imports.h | threadman / include / thsemap.h |
| src / ps2kbd.c | ioman / include / ioman.h |
| src / ps2kbd.c | loadcore / include / loadcore.h |
| src / ps2kbd.c | stdio / include / stdio.h |
| src / ps2kbd.c | sysclib / include / sysclib.h |
| src / ps2kbd.c | threadman / include / thbase.h |
| src / ps2kbd.c | threadman / include / thevent.h |
| src / ps2kbd.c | threadman / include / thsemap.h |

---

## PS2SDK: iop/usb/keyboard -&gt; usbd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000294_000298.html>

###### keyboard → usbd Relation
| File in iop/usb/keyboard | Includes file in iop/usb/usbd |
| src / irx_imports.h | include / usbd.h |
| src / ps2kbd.c | include / usbd.h |
| src / ps2kbd.c | include / usbd_macro.h |

---

## PS2SDK: iop/usb/keyboard -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000294_000537.html>

###### keyboard → kernel Relation
| File in iop/usb/keyboard | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/usb/keyboard/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000295_000000.html>

###### src → common Relation
| File in iop/usb/keyboard/src | Includes file in common |
| ps2kbd.c | include / errno.h |

---

## PS2SDK: iop/usb/keyboard/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000295_000223.html>

###### src → system Relation
| File in iop/usb/keyboard/src | Includes file in iop/system |
| irx_imports.h | dmacman / include / dmacman.h |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | ioman / include / ioman.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thevent.h |
| irx_imports.h | threadman / include / thmsgbx.h |
| irx_imports.h | threadman / include / thsemap.h |
| ps2kbd.c | ioman / include / ioman.h |
| ps2kbd.c | loadcore / include / loadcore.h |
| ps2kbd.c | stdio / include / stdio.h |
| ps2kbd.c | sysclib / include / sysclib.h |
| ps2kbd.c | threadman / include / thbase.h |
| ps2kbd.c | threadman / include / thevent.h |
| ps2kbd.c | threadman / include / thsemap.h |

---

## PS2SDK: iop/usb/keyboard/src -&gt; usbd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000295_000298.html>

###### src → usbd Relation
| File in iop/usb/keyboard/src | Includes file in iop/usb/usbd |
| irx_imports.h | include / usbd.h |
| ps2kbd.c | include / usbd.h |
| ps2kbd.c | include / usbd_macro.h |

---

## PS2SDK: iop/usb/keyboard/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000295_000537.html>

###### src → kernel Relation
| File in iop/usb/keyboard/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/usb/mouse -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000296_000223.html>

###### mouse → system Relation
| File in iop/usb/mouse | Includes file in iop/system |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thevent.h |
| src / irx_imports.h | threadman / include / thmsgbx.h |
| src / irx_imports.h | threadman / include / thsemap.h |
| src / ps2mouse.c | iomanx / include / iomanX.h |
| src / ps2mouse.c | loadcore / include / loadcore.h |
| src / ps2mouse.c | stdio / include / stdio.h |
| src / ps2mouse.c | sysclib / include / sysclib.h |
| src / ps2mouse.c | threadman / include / thbase.h |
| src / ps2mouse.c | threadman / include / thevent.h |
| src / ps2mouse.c | threadman / include / thsemap.h |

---

## PS2SDK: iop/usb/mouse -&gt; usbd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000296_000298.html>

###### mouse → usbd Relation
| File in iop/usb/mouse | Includes file in iop/usb/usbd |
| src / irx_imports.h | include / usbd.h |
| src / ps2mouse.c | include / usbd.h |
| src / ps2mouse.c | include / usbd_macro.h |

---

## PS2SDK: iop/usb/mouse -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000296_000537.html>

###### mouse → kernel Relation
| File in iop/usb/mouse | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/usb/mouse/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000297_000223.html>

###### src → system Relation
| File in iop/usb/mouse/src | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thevent.h |
| irx_imports.h | threadman / include / thmsgbx.h |
| irx_imports.h | threadman / include / thsemap.h |
| ps2mouse.c | iomanx / include / iomanX.h |
| ps2mouse.c | loadcore / include / loadcore.h |
| ps2mouse.c | stdio / include / stdio.h |
| ps2mouse.c | sysclib / include / sysclib.h |
| ps2mouse.c | threadman / include / thbase.h |
| ps2mouse.c | threadman / include / thevent.h |
| ps2mouse.c | threadman / include / thsemap.h |

---

## PS2SDK: iop/usb/mouse/src -&gt; usbd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000297_000298.html>

###### src → usbd Relation
| File in iop/usb/mouse/src | Includes file in iop/usb/usbd |
| irx_imports.h | include / usbd.h |
| ps2mouse.c | include / usbd.h |
| ps2mouse.c | include / usbd_macro.h |

---

## PS2SDK: iop/usb/mouse/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000297_000537.html>

###### src → kernel Relation
| File in iop/usb/mouse/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: iop/usb/usbd -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000298_000223.html>

###### usbd → system Relation
| File in iop/usb/usbd | Includes file in iop/system |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thevent.h |
| src / irx_imports.h | threadman / include / thsemap.h |

---

## PS2SDK: iop/usb/usbd -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000298_000537.html>

###### usbd → kernel Relation
| File in iop/usb/usbd | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |
| include / usbd.h | include / irx.h |
| src / usbdpriv.h | include / defs.h |

---

## PS2SDK: iop/usb/usbd/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000299_000223.html>

###### src → system Relation
| File in iop/usb/usbd/src | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thevent.h |
| irx_imports.h | threadman / include / thsemap.h |

---

## PS2SDK: iop/usb/usbd/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000299_000537.html>

###### src → kernel Relation
| File in iop/usb/usbd/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |
| usbdpriv.h | include / defs.h |

---

## PS2SDK: iop/usb/usbd/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000299_000603.html>

###### src → include Relation
| File in iop/usb/usbd/src | Includes file in iop/usb/usbd/include |
| usbdpriv.h | usbd.h |

---

## PS2SDK: iop/usb/usbhdfsd -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000300_000000.html>

###### usbhdfsd → common Relation
| File in iop/usb/usbhdfsd | Includes file in common |
| src / api.c | include / errno.h |
| src / usb_driver.c | include / errno.h |
| include / usbhdfsd.h | include / usbhdfsd-common.h |

---

## PS2SDK: iop/usb/usbhdfsd -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000300_000056.html>

###### usbhdfsd → cdvd Relation
| File in iop/usb/usbhdfsd | Includes file in iop/cdvd |
| src / api.c | cdvdman / include / cdvdman.h |
| src / irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/usb/usbhdfsd -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000300_000223.html>

###### usbhdfsd → system Relation
| File in iop/usb/usbhdfsd | Includes file in iop/system |
| src / api.c | stdio / include / stdio.h |
| src / api.c | sysclib / include / sysclib.h |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | ioman / include / ioman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thevent.h |
| src / irx_imports.h | threadman / include / thsemap.h |
| src / usb_driver.c | stdio / include / stdio.h |
| src / usb_driver.c | sysclib / include / sysclib.h |
| src / usb_driver.c | threadman / include / thsemap.h |
| src / usbhdfsd.c | intrman / include / intrman.h |
| src / usbhdfsd.c | loadcore / include / loadcore.h |
| src / usbhdfsd.c | stdio / include / stdio.h |

---

## PS2SDK: iop/usb/usbhdfsd -&gt; usbd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000300_000298.html>

###### usbhdfsd → usbd Relation
| File in iop/usb/usbhdfsd | Includes file in iop/usb/usbd |
| src / irx_imports.h | include / usbd.h |
| src / usb_driver.c | include / usbd.h |
| src / usb_driver.c | include / usbd_macro.h |

---

## PS2SDK: iop/usb/usbhdfsd -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000300_000537.html>

###### usbhdfsd → kernel Relation
| File in iop/usb/usbhdfsd | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |
| src / usbhdfsd.c | include / irx.h |
| include / usbhdfsd.h | include / irx.h |

---

## PS2SDK: iop/usb/usbhdfsd/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000301_000000.html>

###### src → common Relation
| File in iop/usb/usbhdfsd/src | Includes file in common |
| api.c | include / errno.h |
| usb_driver.c | include / errno.h |

---

## PS2SDK: iop/usb/usbhdfsd/src -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000301_000056.html>

###### src → cdvd Relation
| File in iop/usb/usbhdfsd/src | Includes file in iop/cdvd |
| api.c | cdvdman / include / cdvdman.h |
| irx_imports.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/usb/usbhdfsd/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000301_000223.html>

###### src → system Relation
| File in iop/usb/usbhdfsd/src | Includes file in iop/system |
| api.c | stdio / include / stdio.h |
| api.c | sysclib / include / sysclib.h |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | ioman / include / ioman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thevent.h |
| irx_imports.h | threadman / include / thsemap.h |
| usb_driver.c | stdio / include / stdio.h |
| usb_driver.c | sysclib / include / sysclib.h |
| usb_driver.c | threadman / include / thsemap.h |
| usbhdfsd.c | intrman / include / intrman.h |
| usbhdfsd.c | loadcore / include / loadcore.h |
| usbhdfsd.c | stdio / include / stdio.h |

---

## PS2SDK: iop/usb/usbhdfsd/src -&gt; usbd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000301_000298.html>

###### src → usbd Relation
| File in iop/usb/usbhdfsd/src | Includes file in iop/usb/usbd |
| irx_imports.h | include / usbd.h |
| usb_driver.c | include / usbd.h |
| usb_driver.c | include / usbd_macro.h |

---

## PS2SDK: iop/usb/usbhdfsd/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000301_000537.html>

###### src → kernel Relation
| File in iop/usb/usbhdfsd/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |
| usbhdfsd.c | include / irx.h |

---

## PS2SDK: iop/usb/usbhdfsd/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000301_000604.html>

###### src → include Relation
| File in iop/usb/usbhdfsd/src | Includes file in iop/usb/usbhdfsd/include |
| api.c | usbhdfsd.h |
| usb_driver.c | usbhdfsd.h |
| usbhdfsd.c | usbhdfsd.h |

---

## PS2SDK: iop/usb/usbmass_bd -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000302_000000.html>

###### usbmass_bd → common Relation
| File in iop/usb/usbmass_bd | Includes file in common |
| src / scsi.c | include / errno.h |
| src / usb_mass.c | include / errno.h |
| src / usb_mass.c | include / usbhdfsd-common.h |

---

## PS2SDK: iop/usb/usbmass_bd -&gt; fs Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000302_000113.html>

###### usbmass_bd → fs Relation
| File in iop/usb/usbmass_bd | Includes file in iop/fs |
| src / irx_imports.h | bdm / include / bdm.h |
| src / scsi.c | bdm / include / bdm.h |

---

## PS2SDK: iop/usb/usbmass_bd -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000302_000223.html>

###### usbmass_bd → system Relation
| File in iop/usb/usbmass_bd | Includes file in iop/system |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thsemap.h |
| src / main.c | loadcore / include / loadcore.h |
| src / main.c | stdio / include / stdio.h |
| src / scsi.c | stdio / include / stdio.h |
| src / scsi.c | sysclib / include / sysclib.h |
| src / scsi.c | threadman / include / thsemap.h |
| src / usb_mass.c | stdio / include / stdio.h |
| src / usb_mass.c | sysclib / include / sysclib.h |
| src / usb_mass.c | threadman / include / thbase.h |
| src / usb_mass.c | threadman / include / thsemap.h |

---

## PS2SDK: iop/usb/usbmass_bd -&gt; usbd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000302_000298.html>

###### usbmass_bd → usbd Relation
| File in iop/usb/usbmass_bd | Includes file in iop/usb/usbd |
| src / irx_imports.h | include / usbd.h |
| src / usb_mass.c | include / usbd.h |
| src / usb_mass.c | include / usbd_macro.h |

---

## PS2SDK: iop/usb/usbmass_bd -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000302_000537.html>

###### usbmass_bd → kernel Relation
| File in iop/usb/usbmass_bd | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |
| src / main.c | include / irx.h |

---

## PS2SDK: iop/usb/usbmass_bd/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000303_000000.html>

###### src → common Relation
| File in iop/usb/usbmass_bd/src | Includes file in common |
| scsi.c | include / errno.h |
| usb_mass.c | include / errno.h |
| usb_mass.c | include / usbhdfsd-common.h |

---

## PS2SDK: iop/usb/usbmass_bd/src -&gt; fs Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000303_000113.html>

###### src → fs Relation
| File in iop/usb/usbmass_bd/src | Includes file in iop/fs |
| irx_imports.h | bdm / include / bdm.h |
| scsi.c | bdm / include / bdm.h |

---

## PS2SDK: iop/usb/usbmass_bd/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000303_000223.html>

###### src → system Relation
| File in iop/usb/usbmass_bd/src | Includes file in iop/system |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thsemap.h |
| main.c | loadcore / include / loadcore.h |
| main.c | stdio / include / stdio.h |
| scsi.c | stdio / include / stdio.h |
| scsi.c | sysclib / include / sysclib.h |
| scsi.c | threadman / include / thsemap.h |
| usb_mass.c | stdio / include / stdio.h |
| usb_mass.c | sysclib / include / sysclib.h |
| usb_mass.c | threadman / include / thbase.h |
| usb_mass.c | threadman / include / thsemap.h |

---

## PS2SDK: iop/usb/usbmass_bd/src -&gt; usbd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000303_000298.html>

###### src → usbd Relation
| File in iop/usb/usbmass_bd/src | Includes file in iop/usb/usbd |
| irx_imports.h | include / usbd.h |
| usb_mass.c | include / usbd.h |
| usb_mass.c | include / usbd_macro.h |

---

## PS2SDK: iop/usb/usbmass_bd/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000303_000537.html>

###### src → kernel Relation
| File in iop/usb/usbmass_bd/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |
| main.c | include / irx.h |

---

## PS2SDK: iop/usb/usbmload -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000304_000223.html>

###### usbmload → system Relation
| File in iop/usb/usbmload | Includes file in iop/system |
| src / irx_imports.h | intrman / include / intrman.h |
| src / irx_imports.h | ioman / include / ioman.h |
| src / irx_imports.h | loadcore / include / loadcore.h |
| src / irx_imports.h | stdio / include / stdio.h |
| src / irx_imports.h | sysclib / include / sysclib.h |
| src / irx_imports.h | threadman / include / thbase.h |
| src / irx_imports.h | threadman / include / thevent.h |
| src / irx_imports.h | modload / include / xmodload.h |

---

## PS2SDK: iop/usb/usbmload -&gt; usbd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000304_000298.html>

###### usbmload → usbd Relation
| File in iop/usb/usbmload | Includes file in iop/usb/usbd |
| src / irx_imports.h | include / usbd.h |

---

## PS2SDK: iop/usb/usbmload -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000304_000537.html>

###### usbmload → kernel Relation
| File in iop/usb/usbmload | Includes file in iop/kernel |
| src / irx_imports.h | include / irx.h |

---

## PS2SDK: iop/usb/usbmload/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000305_000223.html>

###### src → system Relation
| File in iop/usb/usbmload/src | Includes file in iop/system |
| irx_imports.h | intrman / include / intrman.h |
| irx_imports.h | ioman / include / ioman.h |
| irx_imports.h | loadcore / include / loadcore.h |
| irx_imports.h | stdio / include / stdio.h |
| irx_imports.h | sysclib / include / sysclib.h |
| irx_imports.h | threadman / include / thbase.h |
| irx_imports.h | threadman / include / thevent.h |
| irx_imports.h | modload / include / xmodload.h |

---

## PS2SDK: iop/usb/usbmload/src -&gt; usbd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000305_000298.html>

###### src → usbd Relation
| File in iop/usb/usbmload/src | Includes file in iop/usb/usbd |
| irx_imports.h | include / usbd.h |

---

## PS2SDK: iop/usb/usbmload/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000305_000537.html>

###### src → kernel Relation
| File in iop/usb/usbmload/src | Includes file in iop/kernel |
| irx_imports.h | include / irx.h |

---

## PS2SDK: ee -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000306_000001.html>

###### ee → include Relation
| File in ee | Includes file in common/include |
| network / tcpip / src / include / arch / cc.h | errno.h |
| libcglue / include / arpa / inet.h | tcpip.h |
| rpc / ps2snd / include / libsd.h | libsd-common.h |
| rpc / keyboard / include / ps2kbd.h | tamtypes.h |
| debug / include / debug.h | tamtypes.h |
| debug / include / hwbp.h | tamtypes.h |
| packet2 / include / packet2_types.h | tamtypes.h |
| packet2 / include / packet2_utils.h | tamtypes.h |
| packet2 / include / packet2_utils.h | gs_gp.h |
| dma / include / dma.h | tamtypes.h |
| dma / include / dma_registers.h | tamtypes.h |
| dma / include / dma_tags.h | tamtypes.h |
| draw / include / draw.h | tamtypes.h |
| draw / include / draw2d.h | tamtypes.h |
| draw / include / draw3d.h | tamtypes.h |
| draw / include / draw3d.h | gif_tags.h |
| draw / include / draw_blending.h | tamtypes.h |
| draw / include / draw_buffers.h | tamtypes.h |
| draw / include / draw_dithering.h | tamtypes.h |
| draw / include / draw_fog.h | tamtypes.h |
| draw / include / draw_masking.h | tamtypes.h |
| draw / include / draw_primitives.h | tamtypes.h |
| draw / include / draw_sampling.h | tamtypes.h |
| draw / include / draw_tests.h | tamtypes.h |
| eedebug / include / ee_debug.h | tamtypes.h |
| eedebug / include / ee_debug.h | ee_cop0_defs.h |
| eedebug / include / ee_debug.h | ps2_debug.h |
| elf-loader2 / src / include / elf_loader_common.h | tamtypes.h |
| erl / include / erl.h | tamtypes.h |
| font / include / font.h | tamtypes.h |
| ioprpgen / include / ioprpgen.h | tamtypes.h |
| kernel / include / delaythread.h | tamtypes.h |
| kernel / include / fileio.h | io_common.h |
| kernel / include / kernel.h | mipscopaccess.h |
| kernel / include / kernel_util.h | tamtypes.h |
| kernel / include / loadfile.h | tamtypes.h |
| kernel / include / loadfile.h | loadfile-common.h |
| kernel / include / osd_config.h | tamtypes.h |
| kernel / include / sifcmd.h | sifcmd-common.h |
| kernel / include / sifdma.h | tamtypes.h |
| kernel / include / sifrpc.h | sifrpc-common.h |
| kernel / include / sio.h | tamtypes.h |
| kernel / include / timer.h | tamtypes.h |
| kernel / include / timer_alarm.h | tamtypes.h |
| libcglue / include / netdb.h | tcpip.h |
| libcglue / include / ps2sdkapi.h | errno.h |
| libgs / include / libgs.h | tamtypes.h |
| math3d / include / math3d.h | tamtypes.h |
| mpeg / include / libmpeg.h | tamtypes.h |
| packet / include / packet.h | tamtypes.h |
| rpc / cdvd / include / libcdvd.h | libcdvd-common.h |
| rpc / filexio / include / fileXio_rpc.h | fileXio.h |
| rpc / hdd / include / libhdd.h | tamtypes.h |
| rpc / hdd / include / libhdd.h | hdd-ioctl.h |
| rpc / memorycard / include / libmc.h | libmc-common.h |
| rpc / mouse / include / ps2mouse.h | tamtypes.h |
| rpc / remote / include / librm.h | librm-common.h |
| rpc / sdr / include / libsdr.h | libsd-common.h |
| rpc / sdr / include / libsdr.h | libsdr-common.h |
| rpc / secr / include / libsecr.h | libsecr-common.h |
| sbv / include / slib.h | tamtypes.h |
| sbv / include / smem.h | tamtypes.h |
| sbv / include / smod.h | tamtypes.h |
| libcglue / include / netinet / in.h | tcpip.h |
| libcglue / include / netinet / tcp.h | tcpip.h |
| sbv / src / patch_disable_prefix_check.c | tamtypes.h |
| sbv / src / patch_enable_lmb.c | tamtypes.h |
| sbv / src / patch_fileio.c | tamtypes.h |
| sbv / src / patch_romdrv_set_rom1_info.c | tamtypes.h |
| sbv / src / patch_user_mem_clear.c | tamtypes.h |
| sbv / src / slib.c | tamtypes.h |
| sbv / src / smod.c | tamtypes.h |
| elf-loader / src / loader / src / loader.c | errno.h |
| elf-loader2 / src / ldrsrc / src / ldrsrc.c | tamtypes.h |
| rpc / memorycard / src / libmc.c | tamtypes.h |
| network / tcpip / src / ps2ip.c | netman.h |
| network / tcpip / src / ps2ip_ps2sdk.c | errno.h |
| kernel / src / tlbsrc / src / tlbsrc.c | ee_cop0_defs.h |
| kernel / src / tlbsrc / src / tlbsrc.c | mipscopaccess.h |
| kernel / src / osdsrc / src / osd.c | tamtypes.h |
| rpc / keyboard / src / libkbd.c | tamtypes.h |
| rpc / ahx / src / ahx_rpc.c | tamtypes.h |
| rpc / filexio / src / fileXio_ps2sdk.c | errno.h |
| rpc / filexio / src / fileXio_ps2sdk.c | iox_stat.h |
| rpc / filexio / src / fileXio_rpc.c | tamtypes.h |
| rpc / filexio / src / fileXio_rpc.c | errno.h |
| kernel / src / delaythread.c | mipscopaccess.h |
| kernel / src / fileio.c | tamtypes.h |
| kernel / src / fileio.c | ps2lib_err.h |
| kernel / src / fileio.c | fileio-common.h |
| kernel / src / glue.c | mipscopaccess.h |
| kernel / src / iopcontrol.c | tamtypes.h |
| kernel / src / iopheap.c | tamtypes.h |
| kernel / src / iopheap.c | ps2lib_err.h |
| kernel / src / iopheap.c | iopheap-common.h |
| kernel / src / loadfile.c | tamtypes.h |
| kernel / src / loadfile.c | ps2lib_err.h |
| kernel / src / osd_config.c | tamtypes.h |
| kernel / src / sifcmd.c | tamtypes.h |
| kernel / src / sifrpc.c | tamtypes.h |
| kernel / src / sifrpc.c | ps2lib_err.h |
| kernel / src / sio.c | tamtypes.h |
| kernel / src / timer.c | mipscopaccess.h |
| dma / src / dma.c | tamtypes.h |
| debug / src / font.c | tamtypes.h |
| debug / src / scr_printf.c | tamtypes.h |
| debug / src / scr_printf.c | ee_regs.h |
| debug / src / screenshot.c | tamtypes.h |
| math3d / src / math3d.c | tamtypes.h |
| font / src / fontx.c | gif_tags.h |
| font / src / fontx.c | gs_gp.h |
| rpc / ps2snd / src / ps2snd.c | ps2snd.h |
| rpc / pad / src / libpad.c | tamtypes.h |
| rpc / remote / src / librm.c | tamtypes.h |
| rpc / multitap / src / libmtap.c | tamtypes.h |
| rpc / tcpips / src / ps2ipc.c | tamtypes.h |
| rpc / tcpips / src / ps2ipc.c | ps2ip_rpc.h |
| rpc / tcpips / src / ps2ipc_ps2sdk.c | errno.h |
| network / netman / src / netman.c | errno.h |
| network / netman / src / netman.c | netman.h |
| network / netman / src / netman.c | netman_rpc.h |
| network / netman / src / rpc_client.c | errno.h |
| network / netman / src / rpc_client.c | netman.h |
| network / netman / src / rpc_client.c | netman_rpc.h |
| network / netman / src / rpc_server.c | errno.h |
| network / netman / src / rpc_server.c | netman.h |
| network / netman / src / rpc_server.c | netman_rpc.h |
| libcglue / src / cwd.c | errno.h |
| libcglue / src / fdman.c | errno.h |
| libcglue / src / glue.c | errno.h |
| libcglue / src / glue.c | tamtypes.h |
| libcglue / src / glue.c | io_common.h |
| libcglue / src / ps2sdkapi.c | errno.h |
| libcglue / src / ps2sdkapi.c | fileio-common.h |
| libcglue / src / ps2sdkapi.c | iox_stat.h |
| libcglue / src / select.c | errno.h |
| libcglue / src / sleep.c | errno.h |
| libcglue / src / socket.c | errno.h |
| draw / src / draw.c | gif_tags.h |
| draw / src / draw.c | gs_privileged.h |
| draw / src / draw.c | gs_gp.h |
| draw / src / draw.c | gs_psm.h |
| draw / src / draw2d.c | gif_tags.h |
| draw / src / draw2d.c | gs_gp.h |
| draw / src / draw3d.c | gif_tags.h |
| draw / src / draw3d.c | gs_gp.h |
| draw / src / draw3d.c | gs_privileged.h |
| draw / src / draw_environment.c | tamtypes.h |
| draw / src / draw_environment.c | gif_tags.h |
| draw / src / draw_environment.c | gs_gp.h |
| rpc / sior / src / sior_rpc.c | tamtypes.h |
| rpc / audsrv / src / audsrv_rpc.c | tamtypes.h |
| libgs / src / dma.c | errno.h |
| libgs / src / dma.c | ee_regs.h |
| libgs / src / DoubleBuff.c | errno.h |
| libgs / src / draw.c | errno.h |
| libgs / src / libgs.c | errno.h |
| libgs / src / lowlevel.c | errno.h |
| libgs / src / packets.c | errno.h |
| libgs / src / primitives.c | errno.h |
| libgs / src / sync.c | errno.h |
| libgs / src / texture.c | errno.h |
| libgs / src / Zbuffer.c | errno.h |
| mpeg / src / libmpeg.c | ee_regs.h |
| mpeg / src / libmpeg_core.c | ee_regs.h |
| graph / src / graph.c | gs_privileged.h |
| graph / src / graph_config.c | errno.h |
| graph / src / graph_mode.c | gs_privileged.h |
| graph / src / graph_vram.c | gs_psm.h |
| rpc / camera / src / ps2cam_rpc.c | tamtypes.h |
| rpc / cdvd / src / libcdvd.c | tamtypes.h |
| rpc / cdvd / src / ncmd.c | libcdvd-rpc.h |
| rpc / cdvd / src / scmd.c | libcdvd-rpc.h |
| rpc / poweroff / src / poweroff.c | errno.h |
| rpc / poweroff / src / poweroff.c | tamtypes.h |
| rpc / poweroff / src / poweroff.c | pwroff_rpc.h |
| rpc / mouse / src / libmouse.c | tamtypes.h |
| elf-loader / src / elf.h | tamtypes.h |
| kernel / src / srcfile / src / alarm.c | tamtypes.h |
| kernel / src / srcfile / src / alarm.c | ee_regs.h |
| rpc / hdd / src / libhdd.c | tamtypes.h |
| rpc / hdd / src / libhdd.c | errno.h |
| rpc / hdd / src / libhdd.c | sys / ioctl.h |
| rpc / hdd / src / libhdd.c | io_common.h |
| libcglue / include / sys / socket.h | tcpip.h |

---

## PS2SDK: ee -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000306_000006.html>

###### ee → iop Relation
| File in ee | Includes file in iop |
| network / tcpip / src / include / arch / cc.h | tcpip / tcpip-base / include / stdlib.h |
| network / tcpip / src / include / arch / cc.h | kernel / include / sys / time.h |
| network / tcpip / include / ps2ip.h | kernel / include / sys / time.h |
| libpthreadglue / src / include / ps2_osal.h | system / stdio / include / stdio.h |
| libpthreadglue / src / include / ps2_osal.h | tcpip / tcpip-base / include / stdlib.h |
| rpc / secr / src / libsecr.c | system / stdio / include / stdio.h |
| elf-loader / src / loader / src / loader.c | system / stdio / include / stdio.h |
| elf-loader / src / loader / src / loader.c | tcpip / tcpip-base / include / stdlib.h |
| erl / src / erl.c | tcpip / tcpip-base / include / stdlib.h |
| erl / src / erl.c | system / stdio / include / stdio.h |
| erl / src / hashtab.c | tcpip / tcpip-base / include / stdlib.h |
| erl / src / recycle.c | tcpip / tcpip-base / include / stdlib.h |
| input / src / input.c | system / stdio / include / stdio.h |
| network / tcpip / src / ps2ip.c | system / stdio / include / stdio.h |
| network / tcpip / src / sys_arch.c | tcpip / tcpip-base / include / stdlib.h |
| network / tcpip / src / sys_arch.c | system / stdio / include / stdio.h |
| network / tcpip / src / sys_arch.c | kernel / include / sys / time.h |
| libprofglue / src / prof.c | tcpip / tcpip-base / include / stdlib.h |
| libprofglue / src / prof.c | system / stdio / include / stdio.h |
| libpthreadglue / src / osal.c | kernel / include / sys / time.h |
| packet2 / src / packet2.c | system / stdio / include / stdio.h |
| startup / src / crt0.c | system / stdio / include / stdio.h |
| rpc / ahx / src / ahx_rpc.c | tcpip / tcpip-base / include / stdlib.h |
| rpc / ahx / src / ahx_rpc.c | system / stdio / include / stdio.h |
| rpc / filexio / src / fileXio_ps2sdk.c | system / stdio / include / stdio.h |
| rpc / filexio / src / fileXio_ps2sdk.c | tcpip / tcpip-base / include / stdlib.h |
| rpc / filexio / src / fileXio_rpc.c | system / stdio / include / stdio.h |
| rpc / filexio / src / fileXio_rpc.c | tcpip / tcpip-base / include / stdlib.h |
| kernel / src / alarm.c | system / stdio / include / stdio.h |
| kernel / src / iopcontrol.c | system / stdio / include / stdio.h |
| kernel / src / osd_config.c | system / stdio / include / stdio.h |
| kernel / src / sio.c | system / stdio / include / stdio.h |
| kernel / src / tlbfunc.c | system / stdio / include / stdio.h |
| dma / src / dma.c | tcpip / tcpip-base / include / stdlib.h |
| debug / src / scr_printf.c | system / sysclib / include / ctype.h |
| debug / src / scr_printf.c | system / stdio / include / stdio.h |
| libvux / src / vux.c | tcpip / tcpip-base / include / stdlib.h |
| font / src / fontx.c | system / stdio / include / stdio.h |
| font / src / fontx.c | tcpip / tcpip-base / include / stdlib.h |
| font / src / fsfont.c | system / stdio / include / stdio.h |
| font / src / fsfont.c | tcpip / tcpip-base / include / stdlib.h |
| rpc / ps2snd / src / ps2snd.c | system / stdio / include / stdio.h |
| rpc / pad / src / libpad.c | system / stdio / include / stdio.h |
| rpc / remote / src / librm.c | system / stdio / include / stdio.h |
| network / netman / src / rpc_client.c | system / stdio / include / stdio.h |
| network / netman / src / rpc_server.c | system / stdio / include / stdio.h |
| libcglue / src / cwd.c | system / stdio / include / stdio.h |
| libcglue / src / cwd.c | system / sysclib / include / ctype.h |
| libcglue / src / cwd.c | tcpip / tcpip-base / include / stdlib.h |
| libcglue / src / fdman.c | tcpip / tcpip-base / include / stdlib.h |
| libcglue / src / glue.c | system / stdio / include / stdio.h |
| libcglue / src / glue.c | tcpip / tcpip-base / include / stdlib.h |
| libcglue / src / glue.c | kernel / include / sys / time.h |
| libcglue / src / lock.c | system / stdio / include / stdio.h |
| libcglue / src / lock.c | tcpip / tcpip-base / include / stdlib.h |
| libcglue / src / ps2sdkapi.c | system / stdio / include / stdio.h |
| libcglue / src / ps2sdkapi.c | tcpip / tcpip-base / include / stdlib.h |
| libcglue / src / rtc.c | kernel / include / sys / time.h |
| libcglue / src / rtc.c | system / stdio / include / stdio.h |
| libcglue / src / rtc.c | tcpip / tcpip-base / include / stdlib.h |
| libcglue / src / sleep.c | kernel / include / sys / time.h |
| libcglue / src / timezone.c | kernel / include / sys / time.h |
| libcglue / src / timezone.c | system / stdio / include / stdio.h |
| libcglue / src / timezone.c | tcpip / tcpip-base / include / stdlib.h |
| rpc / sior / src / sior_rpc.c | tcpip / tcpip-base / include / stdlib.h |
| rpc / sior / src / sior_rpc.c | system / stdio / include / stdio.h |
| rpc / audsrv / src / audsrv_rpc.c | system / stdio / include / stdio.h |
| libgs / src / dma.c | system / stdio / include / stdio.h |
| libgs / src / DoubleBuff.c | system / stdio / include / stdio.h |
| libgs / src / draw.c | system / stdio / include / stdio.h |
| libgs / src / draw.c | tcpip / tcpip-base / include / stdlib.h |
| libgs / src / libgs.c | system / stdio / include / stdio.h |
| libgs / src / lowlevel.c | system / stdio / include / stdio.h |
| libgs / src / packets.c | system / stdio / include / stdio.h |
| libgs / src / primitives.c | system / stdio / include / stdio.h |
| libgs / src / sync.c | system / stdio / include / stdio.h |
| libgs / src / texture.c | system / stdio / include / stdio.h |
| libgs / src / Zbuffer.c | system / stdio / include / stdio.h |
| mpeg / src / libmpeg.c | system / stdio / include / stdio.h |
| mpeg / src / libmpeg_core.c | tcpip / tcpip-base / include / stdlib.h |
| mpeg / src / libmpeg_core.c | system / stdio / include / stdio.h |
| graph / src / graph_config.c | system / stdio / include / stdio.h |
| graph / src / graph_mode.c | tcpip / tcpip-base / include / stdlib.h |
| rpc / camera / src / ps2cam_rpc.c | system / stdio / include / stdio.h |
| rpc / cdvd / src / libcdvd.c | system / stdio / include / stdio.h |
| rpc / cdvd / src / ncmd.c | system / stdio / include / stdio.h |
| rpc / cdvd / src / scmd.c | system / stdio / include / stdio.h |
| rpc / cdvd / src / scmd.c | kernel / include / sys / time.h |
| rpc / poweroff / src / poweroff.c | system / stdio / include / stdio.h |
| rpc / mouse / src / libmouse.c | system / stdio / include / stdio.h |
| elf-loader2 / src / elf_loader_compat.c | tcpip / tcpip-base / include / stdlib.h |
| elf-loader2 / src / elf_loader_stdio.c | system / stdio / include / stdio.h |
| elf-loader2 / src / elf_loader_stdio.c | tcpip / tcpip-base / include / stdlib.h |
| elf-loader / src / elf.c | tcpip / tcpip-base / include / stdlib.h |
| packet / src / packet.c | tcpip / tcpip-base / include / stdlib.h |
| rpc / hdd / src / libhdd.c | system / stdio / include / stdio.h |
| rpc / hdd / src / libhdd.c | tcpip / tcpip-base / include / stdlib.h |
| libcglue / include / sys / utime.h | kernel / include / sys / time.h |

---

## PS2SDK: ee/debug -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000307_000000.html>

###### debug → common Relation
| File in ee/debug | Includes file in common |
| include / debug.h | include / tamtypes.h |
| include / hwbp.h | include / tamtypes.h |
| src / font.c | include / tamtypes.h |
| src / scr_printf.c | include / tamtypes.h |
| src / scr_printf.c | include / ee_regs.h |
| src / screenshot.c | include / tamtypes.h |

---

## PS2SDK: ee/debug -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000307_000006.html>

###### debug → iop Relation
| File in ee/debug | Includes file in iop |
| src / scr_printf.c | system / sysclib / include / ctype.h |
| src / scr_printf.c | system / stdio / include / stdio.h |

---

## PS2SDK: ee/debug -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000307_000324.html>

###### debug → kernel Relation
| File in ee/debug | Includes file in ee/kernel |
| src / scr_printf.c | include / kernel.h |
| src / scr_printf.c | include / rom0_info.h |
| src / screenshot.c | include / kernel.h |

---

## PS2SDK: ee/debug -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000307_000402.html>

###### debug → erl Relation
| File in ee/debug | Includes file in ee/erl |
| src / erl-support.c | include / erl.h |

---

## PS2SDK: ee/debug/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000308_000000.html>

###### include → common Relation
| File in ee/debug/include | Includes file in common |
| debug.h | include / tamtypes.h |
| hwbp.h | include / tamtypes.h |

---

## PS2SDK: ee/debug/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000309_000000.html>

###### src → common Relation
| File in ee/debug/src | Includes file in common |
| font.c | include / tamtypes.h |
| scr_printf.c | include / ee_regs.h |
| scr_printf.c | include / tamtypes.h |
| screenshot.c | include / tamtypes.h |

---

## PS2SDK: ee/debug/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000309_000006.html>

###### src → iop Relation
| File in ee/debug/src | Includes file in iop |
| scr_printf.c | system / sysclib / include / ctype.h |
| scr_printf.c | system / stdio / include / stdio.h |

---

## PS2SDK: ee/debug/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000309_000308.html>

###### src → include Relation
| File in ee/debug/src | Includes file in ee/debug/include |
| screenshot.c | screenshot.h |

---

## PS2SDK: ee/debug/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000309_000324.html>

###### src → kernel Relation
| File in ee/debug/src | Includes file in ee/kernel |
| scr_printf.c | include / kernel.h |
| scr_printf.c | include / rom0_info.h |
| screenshot.c | include / kernel.h |

---

## PS2SDK: ee/debug/src -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000309_000402.html>

###### src → erl Relation
| File in ee/debug/src | Includes file in ee/erl |
| erl-support.c | include / erl.h |

---

## PS2SDK: ee/dma -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000310_000000.html>

###### dma → common Relation
| File in ee/dma | Includes file in common |
| include / dma.h | include / tamtypes.h |
| include / dma_registers.h | include / tamtypes.h |
| include / dma_tags.h | include / tamtypes.h |
| src / dma.c | include / tamtypes.h |

---

## PS2SDK: ee/dma -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000310_000006.html>

###### dma → iop Relation
| File in ee/dma | Includes file in iop |
| src / dma.c | tcpip / tcpip-base / include / stdlib.h |

---

## PS2SDK: ee/dma -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000310_000324.html>

###### dma → kernel Relation
| File in ee/dma | Includes file in ee/kernel |
| src / dma.c | include / kernel.h |

---

## PS2SDK: ee/dma -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000310_000402.html>

###### dma → erl Relation
| File in ee/dma | Includes file in ee/erl |
| src / erl-support.c | include / erl.h |

---

## PS2SDK: ee/dma/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000311_000000.html>

###### src → common Relation
| File in ee/dma/src | Includes file in common |
| dma.c | include / tamtypes.h |

---

## PS2SDK: ee/dma/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000311_000006.html>

###### src → iop Relation
| File in ee/dma/src | Includes file in iop |
| dma.c | tcpip / tcpip-base / include / stdlib.h |

---

## PS2SDK: ee/dma/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000311_000324.html>

###### src → kernel Relation
| File in ee/dma/src | Includes file in ee/kernel |
| dma.c | include / kernel.h |

---

## PS2SDK: ee/dma/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000311_000382.html>

###### src → include Relation
| File in ee/dma/src | Includes file in ee/dma/include |
| dma.c | dma.h |
| dma.c | dma_registers.h |

---

## PS2SDK: ee/dma/src -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000311_000402.html>

###### src → erl Relation
| File in ee/dma/src | Includes file in ee/erl |
| erl-support.c | include / erl.h |

---

## PS2SDK: ee/draw -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000312_000000.html>

###### draw → common Relation
| File in ee/draw | Includes file in common |
| include / draw.h | include / tamtypes.h |
| include / draw2d.h | include / tamtypes.h |
| include / draw3d.h | include / tamtypes.h |
| include / draw3d.h | include / gif_tags.h |
| include / draw_blending.h | include / tamtypes.h |
| include / draw_buffers.h | include / tamtypes.h |
| include / draw_dithering.h | include / tamtypes.h |
| include / draw_fog.h | include / tamtypes.h |
| include / draw_masking.h | include / tamtypes.h |
| include / draw_primitives.h | include / tamtypes.h |
| include / draw_sampling.h | include / tamtypes.h |
| include / draw_tests.h | include / tamtypes.h |
| src / draw.c | include / gif_tags.h |
| src / draw.c | include / gs_privileged.h |
| src / draw.c | include / gs_gp.h |
| src / draw.c | include / gs_psm.h |
| src / draw2d.c | include / gif_tags.h |
| src / draw2d.c | include / gs_gp.h |
| src / draw3d.c | include / gif_tags.h |
| src / draw3d.c | include / gs_gp.h |
| src / draw3d.c | include / gs_privileged.h |
| src / draw_environment.c | include / tamtypes.h |
| src / draw_environment.c | include / gif_tags.h |
| src / draw_environment.c | include / gs_gp.h |

---

## PS2SDK: ee/draw -&gt; dma Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000312_000310.html>

###### draw → dma Relation
| File in ee/draw | Includes file in ee/dma |
| src / draw.c | include / dma_tags.h |

---

## PS2SDK: ee/draw -&gt; math3d Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000312_000330.html>

###### draw → math3d Relation
| File in ee/draw | Includes file in ee/math3d |
| include / draw_types.h | include / math3d.h |

---

## PS2SDK: ee/draw -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000312_000402.html>

###### draw → erl Relation
| File in ee/draw | Includes file in ee/erl |
| src / erl-support.c | include / erl.h |

---

## PS2SDK: ee/draw/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000313_000000.html>

###### src → common Relation
| File in ee/draw/src | Includes file in common |
| draw.c | include / gif_tags.h |
| draw.c | include / gs_gp.h |
| draw.c | include / gs_privileged.h |
| draw.c | include / gs_psm.h |
| draw2d.c | include / gif_tags.h |
| draw2d.c | include / gs_gp.h |
| draw3d.c | include / gif_tags.h |
| draw3d.c | include / gs_gp.h |
| draw3d.c | include / gs_privileged.h |
| draw_environment.c | include / gif_tags.h |
| draw_environment.c | include / gs_gp.h |
| draw_environment.c | include / tamtypes.h |

---

## PS2SDK: ee/draw/src -&gt; dma Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000313_000310.html>

###### src → dma Relation
| File in ee/draw/src | Includes file in ee/dma |
| draw.c | include / dma_tags.h |

---

## PS2SDK: ee/draw/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000313_000383.html>

###### src → include Relation
| File in ee/draw/src | Includes file in ee/draw/include |
| draw.c | draw.h |
| draw.c | draw2d.h |
| draw2d.c | draw.h |
| draw2d.c | draw2d.h |
| draw2d.c | draw3d.h |
| draw3d.c | draw.h |
| draw_environment.c | draw.h |

---

## PS2SDK: ee/draw/src -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000313_000402.html>

###### src → erl Relation
| File in ee/draw/src | Includes file in ee/erl |
| erl-support.c | include / erl.h |

---

## PS2SDK: ee/eedebug -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000314_000000.html>

###### eedebug → common Relation
| File in ee/eedebug | Includes file in common |
| include / ee_debug.h | include / tamtypes.h |
| include / ee_debug.h | include / ee_cop0_defs.h |
| include / ee_debug.h | include / ps2_debug.h |

---

## PS2SDK: ee/eedebug -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000314_000324.html>

###### eedebug → kernel Relation
| File in ee/eedebug | Includes file in ee/kernel |
| src / ee_debug.c | include / kernel.h |

---

## PS2SDK: ee/eedebug -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000314_000402.html>

###### eedebug → erl Relation
| File in ee/eedebug | Includes file in ee/erl |
| src / erl-support.c | include / erl.h |

---

## PS2SDK: ee/eedebug/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000315_000324.html>

###### src → kernel Relation
| File in ee/eedebug/src | Includes file in ee/kernel |
| ee_debug.c | include / kernel.h |

---

## PS2SDK: ee/eedebug/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000315_000384.html>

###### src → include Relation
| File in ee/eedebug/src | Includes file in ee/eedebug/include |
| ee_debug.c | ee_debug.h |

---

## PS2SDK: ee/eedebug/src -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000315_000402.html>

###### src → erl Relation
| File in ee/eedebug/src | Includes file in ee/erl |
| erl-support.c | include / erl.h |

---

## PS2SDK: ee/font -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000316_000000.html>

###### font → common Relation
| File in ee/font | Includes file in common |
| include / font.h | include / tamtypes.h |
| src / fontx.c | include / gif_tags.h |
| src / fontx.c | include / gs_gp.h |

---

## PS2SDK: ee/font -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000316_000006.html>

###### font → iop Relation
| File in ee/font | Includes file in iop |
| src / fontx.c | system / stdio / include / stdio.h |
| src / fontx.c | tcpip / tcpip-base / include / stdlib.h |
| src / fsfont.c | system / stdio / include / stdio.h |
| src / fsfont.c | tcpip / tcpip-base / include / stdlib.h |

---

## PS2SDK: ee/font -&gt; draw Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000316_000312.html>

###### font → draw Relation
| File in ee/font | Includes file in ee/draw |
| include / font.h | include / draw.h |
| src / fontx.c | include / draw.h |
| src / fontx.c | include / draw3d.h |
| src / fsfont.c | include / draw.h |
| src / fsfont.c | include / draw3d.h |

---

## PS2SDK: ee/font -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000316_000402.html>

###### font → erl Relation
| File in ee/font | Includes file in ee/erl |
| src / erl-support.c | include / erl.h |

---

## PS2SDK: ee/font/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000317_000000.html>

###### src → common Relation
| File in ee/font/src | Includes file in common |
| fontx.c | include / gif_tags.h |
| fontx.c | include / gs_gp.h |

---

## PS2SDK: ee/font/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000317_000006.html>

###### src → iop Relation
| File in ee/font/src | Includes file in iop |
| fontx.c | system / stdio / include / stdio.h |
| fontx.c | tcpip / tcpip-base / include / stdlib.h |
| fsfont.c | system / stdio / include / stdio.h |
| fsfont.c | tcpip / tcpip-base / include / stdlib.h |

---

## PS2SDK: ee/font/src -&gt; draw Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000317_000312.html>

###### src → draw Relation
| File in ee/font/src | Includes file in ee/draw |
| fontx.c | include / draw.h |
| fontx.c | include / draw3d.h |
| fsfont.c | include / draw.h |
| fsfont.c | include / draw3d.h |

---

## PS2SDK: ee/font/src -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000317_000402.html>

###### src → erl Relation
| File in ee/font/src | Includes file in ee/erl |
| erl-support.c | include / erl.h |

---

## PS2SDK: ee/font/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000317_000405.html>

###### src → include Relation
| File in ee/font/src | Includes file in ee/font/include |
| fontx.c | font.h |
| fsfont.c | font.h |

---

## PS2SDK: ee/graph -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000318_000000.html>

###### graph → common Relation
| File in ee/graph | Includes file in common |
| src / graph.c | include / gs_privileged.h |
| src / graph_config.c | include / errno.h |
| src / graph_mode.c | include / gs_privileged.h |
| src / graph_vram.c | include / gs_psm.h |

---

## PS2SDK: ee/graph -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000318_000006.html>

###### graph → iop Relation
| File in ee/graph | Includes file in iop |
| src / graph_config.c | system / stdio / include / stdio.h |
| src / graph_mode.c | tcpip / tcpip-base / include / stdlib.h |

---

## PS2SDK: ee/graph -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000318_000324.html>

###### graph → kernel Relation
| File in ee/graph | Includes file in ee/kernel |
| src / graph.c | include / kernel.h |
| src / graph_mode.c | include / kernel.h |
| src / graph_mode.c | include / osd_config.h |
| src / graph_mode.c | include / rom0_info.h |

---

## PS2SDK: ee/graph -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000318_000402.html>

###### graph → erl Relation
| File in ee/graph | Includes file in ee/erl |
| src / erl-support.c | include / erl.h |

---

## PS2SDK: ee/graph/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000319_000000.html>

###### src → common Relation
| File in ee/graph/src | Includes file in common |
| graph.c | include / gs_privileged.h |
| graph_config.c | include / errno.h |
| graph_mode.c | include / gs_privileged.h |
| graph_vram.c | include / gs_psm.h |

---

## PS2SDK: ee/graph/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000319_000006.html>

###### src → iop Relation
| File in ee/graph/src | Includes file in iop |
| graph_config.c | system / stdio / include / stdio.h |
| graph_mode.c | tcpip / tcpip-base / include / stdlib.h |

---

## PS2SDK: ee/graph/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000319_000324.html>

###### src → kernel Relation
| File in ee/graph/src | Includes file in ee/kernel |
| graph.c | include / kernel.h |
| graph_mode.c | include / kernel.h |
| graph_mode.c | include / osd_config.h |
| graph_mode.c | include / rom0_info.h |

---

## PS2SDK: ee/graph/src -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000319_000402.html>

###### src → erl Relation
| File in ee/graph/src | Includes file in ee/erl |
| erl-support.c | include / erl.h |

---

## PS2SDK: ee/graph/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000319_000406.html>

###### src → include Relation
| File in ee/graph/src | Includes file in ee/graph/include |
| graph.c | graph.h |
| graph_config.c | graph.h |
| graph_config.c | graph_config.h |
| graph_mode.c | graph.h |
| graph_mode.c | graph_config.h |
| graph_vram.c | graph_vram.h |

---

## PS2SDK: ee/input -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000320_000006.html>

###### input → iop Relation
| File in ee/input | Includes file in iop |
| src / input.c | system / stdio / include / stdio.h |

---

## PS2SDK: ee/input -&gt; rpc Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000320_000343.html>

###### input → rpc Relation
| File in ee/input | Includes file in ee/rpc |
| include / input.h | pad / include / libpad.h |
| src / input.c | pad / include / libpad.h |

---

## PS2SDK: ee/input -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000320_000402.html>

###### input → erl Relation
| File in ee/input | Includes file in ee/erl |
| src / erl-support.c | include / erl.h |

---

## PS2SDK: ee/input/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000321_000006.html>

###### src → iop Relation
| File in ee/input/src | Includes file in iop |
| input.c | system / stdio / include / stdio.h |

---

## PS2SDK: ee/input/src -&gt; rpc Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000321_000343.html>

###### src → rpc Relation
| File in ee/input/src | Includes file in ee/rpc |
| input.c | pad / include / libpad.h |

---

## PS2SDK: ee/input/src -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000321_000402.html>

###### src → erl Relation
| File in ee/input/src | Includes file in ee/erl |
| erl-support.c | include / erl.h |

---

## PS2SDK: ee/input/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000321_000407.html>

###### src → include Relation
| File in ee/input/src | Includes file in ee/input/include |
| input.c | input.h |

---

## PS2SDK: ee/iopreboot -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000322_000324.html>

###### iopreboot → kernel Relation
| File in ee/iopreboot | Includes file in ee/kernel |
| src / SifIopRebootBuffer.c | include / kernel.h |
| src / SifIopRebootBuffer.c | include / iopcontrol.h |
| src / SifIopRebootBuffer.c | include / loadfile.h |
| src / SifIopRebootBuffer.c | include / iopheap.h |
| src / SifIopRebootBuffer.c | include / sifdma.h |

---

## PS2SDK: ee/iopreboot -&gt; sbv Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000322_000380.html>

###### iopreboot → sbv Relation
| File in ee/iopreboot | Includes file in ee/sbv |
| src / SifIopRebootBuffer.c | include / sbv_patches.h |

---

## PS2SDK: ee/iopreboot -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000322_000402.html>

###### iopreboot → erl Relation
| File in ee/iopreboot | Includes file in ee/erl |
| src / erl-support.c | include / erl.h |

---

## PS2SDK: ee/iopreboot/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000323_000324.html>

###### src → kernel Relation
| File in ee/iopreboot/src | Includes file in ee/kernel |
| SifIopRebootBuffer.c | include / iopcontrol.h |
| SifIopRebootBuffer.c | include / iopheap.h |
| SifIopRebootBuffer.c | include / kernel.h |
| SifIopRebootBuffer.c | include / loadfile.h |
| SifIopRebootBuffer.c | include / sifdma.h |

---

## PS2SDK: ee/iopreboot/src -&gt; sbv Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000323_000380.html>

###### src → sbv Relation
| File in ee/iopreboot/src | Includes file in ee/sbv |
| SifIopRebootBuffer.c | include / sbv_patches.h |

---

## PS2SDK: ee/iopreboot/src -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000323_000402.html>

###### src → erl Relation
| File in ee/iopreboot/src | Includes file in ee/erl |
| erl-support.c | include / erl.h |

---

## PS2SDK: ee/iopreboot/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000323_000408.html>

###### src → include Relation
| File in ee/iopreboot/src | Includes file in ee/iopreboot/include |
| SifIopRebootBuffer.c | iopcontrol_special.h |

---

## PS2SDK: ee/kernel -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000324_000000.html>

###### kernel → common Relation
| File in ee/kernel | Includes file in common |
| include / delaythread.h | include / tamtypes.h |
| include / fileio.h | include / io_common.h |
| include / kernel.h | include / mipscopaccess.h |
| include / kernel_util.h | include / tamtypes.h |
| include / loadfile.h | include / loadfile-common.h |
| include / loadfile.h | include / tamtypes.h |
| include / osd_config.h | include / tamtypes.h |
| include / sifcmd.h | include / sifcmd-common.h |
| include / sifdma.h | include / tamtypes.h |
| include / sifrpc.h | include / sifrpc-common.h |
| include / sio.h | include / tamtypes.h |
| include / timer.h | include / tamtypes.h |
| include / timer_alarm.h | include / tamtypes.h |
| src / tlbsrc / src / tlbsrc.c | include / ee_cop0_defs.h |
| src / tlbsrc / src / tlbsrc.c | include / mipscopaccess.h |
| src / osdsrc / src / osd.c | include / tamtypes.h |
| src / delaythread.c | include / mipscopaccess.h |
| src / fileio.c | include / tamtypes.h |
| src / fileio.c | include / ps2lib_err.h |
| src / fileio.c | include / fileio-common.h |
| src / glue.c | include / mipscopaccess.h |
| src / iopcontrol.c | include / tamtypes.h |
| src / iopheap.c | include / tamtypes.h |
| src / iopheap.c | include / ps2lib_err.h |
| src / iopheap.c | include / iopheap-common.h |
| src / loadfile.c | include / tamtypes.h |
| src / loadfile.c | include / ps2lib_err.h |
| src / osd_config.c | include / tamtypes.h |
| src / sifcmd.c | include / tamtypes.h |
| src / sifrpc.c | include / tamtypes.h |
| src / sifrpc.c | include / ps2lib_err.h |
| src / sio.c | include / tamtypes.h |
| src / timer.c | include / mipscopaccess.h |
| src / srcfile / src / alarm.c | include / tamtypes.h |
| src / srcfile / src / alarm.c | include / ee_regs.h |

---

## PS2SDK: ee/kernel -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000324_000006.html>

###### kernel → iop Relation
| File in ee/kernel | Includes file in iop |
| src / alarm.c | system / stdio / include / stdio.h |
| src / iopcontrol.c | system / stdio / include / stdio.h |
| src / osd_config.c | system / stdio / include / stdio.h |
| src / sio.c | system / stdio / include / stdio.h |
| src / tlbfunc.c | system / stdio / include / stdio.h |

---

## PS2SDK: ee/kernel -&gt; rpc Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000324_000343.html>

###### kernel → rpc Relation
| File in ee/kernel | Includes file in ee/rpc |
| include / osd_config.h | cdvd / include / libcdvd.h |

---

## PS2SDK: ee/kernel -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000324_000350.html>

###### kernel → cdvd Relation
| File in ee/kernel | Includes file in ee/rpc/cdvd |
| include / osd_config.h | include / libcdvd.h |

---

## PS2SDK: ee/kernel -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000324_000402.html>

###### kernel → erl Relation
| File in ee/kernel | Includes file in ee/erl |
| src / erl-support.c | include / erl.h |

---

## PS2SDK: ee/kernel -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000324_000451.html>

###### kernel → include Relation
| File in ee/kernel | Includes file in ee/rpc/cdvd/include |
| include / osd_config.h | libcdvd.h |

---

## PS2SDK: ee/kernel/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000325_000000.html>

###### src → common Relation
| File in ee/kernel/src | Includes file in common |
| delaythread.c | include / mipscopaccess.h |
| fileio.c | include / fileio-common.h |
| fileio.c | include / ps2lib_err.h |
| fileio.c | include / tamtypes.h |
| glue.c | include / mipscopaccess.h |
| iopcontrol.c | include / tamtypes.h |
| iopheap.c | include / iopheap-common.h |
| iopheap.c | include / ps2lib_err.h |
| iopheap.c | include / tamtypes.h |
| loadfile.c | include / ps2lib_err.h |
| loadfile.c | include / tamtypes.h |
| osdsrc / src / osd.c | include / tamtypes.h |
| osd_config.c | include / tamtypes.h |
| sifcmd.c | include / tamtypes.h |
| sifrpc.c | include / ps2lib_err.h |
| sifrpc.c | include / tamtypes.h |
| sio.c | include / tamtypes.h |
| timer.c | include / mipscopaccess.h |
| tlbsrc / src / tlbsrc.c | include / ee_cop0_defs.h |
| tlbsrc / src / tlbsrc.c | include / mipscopaccess.h |
| srcfile / src / alarm.c | include / tamtypes.h |
| srcfile / src / alarm.c | include / ee_regs.h |

---

## PS2SDK: ee/kernel/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000325_000006.html>

###### src → iop Relation
| File in ee/kernel/src | Includes file in iop |
| alarm.c | system / stdio / include / stdio.h |
| iopcontrol.c | system / stdio / include / stdio.h |
| osd_config.c | system / stdio / include / stdio.h |
| sio.c | system / stdio / include / stdio.h |
| tlbfunc.c | system / stdio / include / stdio.h |

---

## PS2SDK: ee/kernel/src -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000325_000402.html>

###### src → erl Relation
| File in ee/kernel/src | Includes file in ee/erl |
| erl-support.c | include / erl.h |

---

## PS2SDK: ee/kernel/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000325_000412.html>

###### src → include Relation
| File in ee/kernel/src | Includes file in ee/kernel/include |
| alarm.c | kernel.h |
| alarm.c | timer.h |
| debug.c | kernel.h |
| debug.c | syscallnr.h |
| deci2.c | kernel.h |
| delaythread.c | kernel.h |
| delaythread.c | timer.h |
| osdsrc / src / ExecPS2.c | kernel.h |
| exit.c | kernel.h |
| fileio.c | fileio.h |
| fileio.c | iopcontrol.h |
| fileio.c | kernel.h |
| getkernel.c | kernel.h |
| glue.c | kernel.h |
| initsys.c | kernel.h |
| initsys.c | timer.h |
| iopcontrol.c | iopcontrol.h |
| iopcontrol.c | kernel.h |
| iopheap.c | iopcontrol.h |
| iopheap.c | iopheap.h |
| iopheap.c | kernel.h |
| kernel_util.c | kernel.h |
| kernel_util.c | kernel_util.h |
| libosd.c | kernel.h |
| libosd.c | osd_config.h |
| libosd.c | syscallnr.h |
| libosd_common.c | kernel.h |
| libosd_common.c | osd_config.h |
| libosd_common.c | syscallnr.h |
| libosd_full.c | kernel.h |
| libosd_full.c | osd_config.h |
| libosd_full.c | syscallnr.h |
| loadfile.c | iopcontrol.h |
| loadfile.c | iopheap.h |
| loadfile.c | kernel.h |
| loadfile.c | loadfile.h |
| osdsrc / src / osd.c | osd_config.h |
| osd_config.c | kernel.h |
| osd_config.c | osd_config.h |
| osd_config.c | rom0_info.h |
| osdsrc / src / osdsrc.c | osd_config.h |
| osdsrc / src / osdsrc.c | syscallnr.h |
| rom0_info.c | iopheap.h |
| rom0_info.c | kernel.h |
| rom0_info.c | rom0_info.h |
| rom0_info.c | syscallnr.h |
| setup.c | kernel.h |
| sifcmd.c | iopcontrol.h |
| sifcmd.c | kernel.h |
| sifrpc.c | iopcontrol.h |
| sifrpc.c | kernel.h |
| sio.c | kernel.h |
| sio.c | sio.h |
| thread.c | kernel.h |
| timer.c | kernel.h |
| timer.c | timer.h |
| timer_alarm.c | kernel.h |
| timer_alarm.c | timer.h |
| tlbfunc.c | kernel.h |
| tlbsrc / src / tlbsrc.c | kernel.h |
| tty.c | deci2.h |
| tty.c | kernel.h |
| srcfile / src / alarm.c | timer.h |
| srcfile / src / alarm.c | kernel.h |
| srcfile / src / srcfile.c | kernel.h |

---

## PS2SDK: ee/libgs -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000326_000000.html>

###### libgs → common Relation
| File in ee/libgs | Includes file in common |
| include / libgs.h | include / tamtypes.h |
| src / dma.c | include / errno.h |
| src / dma.c | include / ee_regs.h |
| src / DoubleBuff.c | include / errno.h |
| src / draw.c | include / errno.h |
| src / libgs.c | include / errno.h |
| src / lowlevel.c | include / errno.h |
| src / packets.c | include / errno.h |
| src / primitives.c | include / errno.h |
| src / sync.c | include / errno.h |
| src / texture.c | include / errno.h |
| src / Zbuffer.c | include / errno.h |

---

## PS2SDK: ee/libgs -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000326_000006.html>

###### libgs → iop Relation
| File in ee/libgs | Includes file in iop |
| src / dma.c | system / stdio / include / stdio.h |
| src / DoubleBuff.c | system / stdio / include / stdio.h |
| src / draw.c | system / stdio / include / stdio.h |
| src / draw.c | tcpip / tcpip-base / include / stdlib.h |
| src / libgs.c | system / stdio / include / stdio.h |
| src / lowlevel.c | system / stdio / include / stdio.h |
| src / packets.c | system / stdio / include / stdio.h |
| src / primitives.c | system / stdio / include / stdio.h |
| src / sync.c | system / stdio / include / stdio.h |
| src / texture.c | system / stdio / include / stdio.h |
| src / Zbuffer.c | system / stdio / include / stdio.h |

---

## PS2SDK: ee/libgs -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000326_000324.html>

###### libgs → kernel Relation
| File in ee/libgs | Includes file in ee/kernel |
| src / dma.c | include / kernel.h |
| src / DoubleBuff.c | include / kernel.h |
| src / draw.c | include / kernel.h |
| src / draw.c | include / syscallnr.h |
| src / libgs.c | include / kernel.h |
| src / lowlevel.c | include / kernel.h |
| src / packets.c | include / kernel.h |
| src / primitives.c | include / kernel.h |
| src / sync.c | include / kernel.h |
| src / texture.c | include / kernel.h |
| src / Zbuffer.c | include / kernel.h |

---

## PS2SDK: ee/libgs -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000326_000402.html>

###### libgs → erl Relation
| File in ee/libgs | Includes file in ee/erl |
| src / erl-support.c | include / erl.h |

---

## PS2SDK: ee/libgs/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000327_000000.html>

###### src → common Relation
| File in ee/libgs/src | Includes file in common |
| dma.c | include / ee_regs.h |
| dma.c | include / errno.h |
| DoubleBuff.c | include / errno.h |
| draw.c | include / errno.h |
| libgs.c | include / errno.h |
| lowlevel.c | include / errno.h |
| packets.c | include / errno.h |
| primitives.c | include / errno.h |
| sync.c | include / errno.h |
| texture.c | include / errno.h |
| Zbuffer.c | include / errno.h |

---

## PS2SDK: ee/libgs/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000327_000006.html>

###### src → iop Relation
| File in ee/libgs/src | Includes file in iop |
| dma.c | system / stdio / include / stdio.h |
| DoubleBuff.c | system / stdio / include / stdio.h |
| draw.c | system / stdio / include / stdio.h |
| draw.c | tcpip / tcpip-base / include / stdlib.h |
| libgs.c | system / stdio / include / stdio.h |
| lowlevel.c | system / stdio / include / stdio.h |
| packets.c | system / stdio / include / stdio.h |
| primitives.c | system / stdio / include / stdio.h |
| sync.c | system / stdio / include / stdio.h |
| texture.c | system / stdio / include / stdio.h |
| Zbuffer.c | system / stdio / include / stdio.h |

---

## PS2SDK: ee/libgs/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000327_000324.html>

###### src → kernel Relation
| File in ee/libgs/src | Includes file in ee/kernel |
| dma.c | include / kernel.h |
| DoubleBuff.c | include / kernel.h |
| draw.c | include / kernel.h |
| draw.c | include / syscallnr.h |
| libgs.c | include / kernel.h |
| lowlevel.c | include / kernel.h |
| packets.c | include / kernel.h |
| primitives.c | include / kernel.h |
| sync.c | include / kernel.h |
| texture.c | include / kernel.h |
| Zbuffer.c | include / kernel.h |

---

## PS2SDK: ee/libgs/src -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000327_000402.html>

###### src → erl Relation
| File in ee/libgs/src | Includes file in ee/erl |
| erl-support.c | include / erl.h |

---

## PS2SDK: ee/libgs/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000327_000428.html>

###### src → include Relation
| File in ee/libgs/src | Includes file in ee/libgs/include |
| dma.c | libgs.h |
| DoubleBuff.c | libgs.h |
| draw.c | libgs.h |
| libgs.c | libgs.h |
| lowlevel.c | libgs.h |
| packets.c | libgs.h |
| primitives.c | libgs.h |
| sync.c | libgs.h |
| texture.c | libgs.h |
| Zbuffer.c | libgs.h |

---

## PS2SDK: ee/libvux -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000328_000006.html>

###### libvux → iop Relation
| File in ee/libvux | Includes file in iop |
| src / vux.c | tcpip / tcpip-base / include / stdlib.h |

---

## PS2SDK: ee/libvux -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000328_000402.html>

###### libvux → erl Relation
| File in ee/libvux | Includes file in ee/erl |
| src / erl-support.c | include / erl.h |

---

## PS2SDK: ee/libvux/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000329_000006.html>

###### src → iop Relation
| File in ee/libvux/src | Includes file in iop |
| vux.c | tcpip / tcpip-base / include / stdlib.h |

---

## PS2SDK: ee/libvux/src -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000329_000402.html>

###### src → erl Relation
| File in ee/libvux/src | Includes file in ee/erl |
| erl-support.c | include / erl.h |

---

## PS2SDK: ee/libvux/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000329_000435.html>

###### src → include Relation
| File in ee/libvux/src | Includes file in ee/libvux/include |
| vuhw.c | libvux.h |
| vusw.c | libvux.h |
| vux.c | libvux.h |
| vux.h | libvux.h |

---

## PS2SDK: ee/math3d -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000330_000000.html>

###### math3d → common Relation
| File in ee/math3d | Includes file in common |
| include / math3d.h | include / tamtypes.h |
| src / math3d.c | include / tamtypes.h |

---

## PS2SDK: ee/math3d -&gt; graph Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000330_000318.html>

###### math3d → graph Relation
| File in ee/math3d | Includes file in ee/graph |
| src / math3d.c | include / graph.h |

---

## PS2SDK: ee/math3d -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000330_000402.html>

###### math3d → erl Relation
| File in ee/math3d | Includes file in ee/erl |
| src / erl-support.c | include / erl.h |

---

## PS2SDK: ee/math3d/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000331_000000.html>

###### src → common Relation
| File in ee/math3d/src | Includes file in common |
| math3d.c | include / tamtypes.h |

---

## PS2SDK: ee/math3d/src -&gt; graph Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000331_000318.html>

###### src → graph Relation
| File in ee/math3d/src | Includes file in ee/graph |
| math3d.c | include / graph.h |

---

## PS2SDK: ee/math3d/src -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000331_000402.html>

###### src → erl Relation
| File in ee/math3d/src | Includes file in ee/erl |
| erl-support.c | include / erl.h |

---

## PS2SDK: ee/math3d/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000331_000436.html>

###### src → include Relation
| File in ee/math3d/src | Includes file in ee/math3d/include |
| math3d.c | math3d.h |

---

## PS2SDK: ee/mpeg -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000332_000000.html>

###### mpeg → common Relation
| File in ee/mpeg | Includes file in common |
| include / libmpeg.h | include / tamtypes.h |
| src / libmpeg.c | include / ee_regs.h |
| src / libmpeg_core.c | include / ee_regs.h |

---

## PS2SDK: ee/mpeg -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000332_000006.html>

###### mpeg → iop Relation
| File in ee/mpeg | Includes file in iop |
| src / libmpeg.c | system / stdio / include / stdio.h |
| src / libmpeg_core.c | tcpip / tcpip-base / include / stdlib.h |
| src / libmpeg_core.c | system / stdio / include / stdio.h |

---

## PS2SDK: ee/mpeg -&gt; dma Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000332_000310.html>

###### mpeg → dma Relation
| File in ee/mpeg | Includes file in ee/dma |
| src / libmpeg_core.c | include / dma_tags.h |

---

## PS2SDK: ee/mpeg -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000332_000324.html>

###### mpeg → kernel Relation
| File in ee/mpeg | Includes file in ee/kernel |
| src / libmpeg.c | include / kernel.h |
| src / libmpeg_core.c | include / kernel.h |

---

## PS2SDK: ee/mpeg -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000332_000402.html>

###### mpeg → erl Relation
| File in ee/mpeg | Includes file in ee/erl |
| src / erl-support.c | include / erl.h |

---

## PS2SDK: ee/mpeg/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000333_000000.html>

###### src → common Relation
| File in ee/mpeg/src | Includes file in common |
| libmpeg.c | include / ee_regs.h |
| libmpeg_core.c | include / ee_regs.h |

---

## PS2SDK: ee/mpeg/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000333_000006.html>

###### src → iop Relation
| File in ee/mpeg/src | Includes file in iop |
| libmpeg.c | system / stdio / include / stdio.h |
| libmpeg_core.c | system / stdio / include / stdio.h |
| libmpeg_core.c | tcpip / tcpip-base / include / stdlib.h |

---

## PS2SDK: ee/mpeg/src -&gt; dma Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000333_000310.html>

###### src → dma Relation
| File in ee/mpeg/src | Includes file in ee/dma |
| libmpeg_core.c | include / dma_tags.h |

---

## PS2SDK: ee/mpeg/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000333_000324.html>

###### src → kernel Relation
| File in ee/mpeg/src | Includes file in ee/kernel |
| libmpeg.c | include / kernel.h |
| libmpeg_core.c | include / kernel.h |

---

## PS2SDK: ee/mpeg/src -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000333_000402.html>

###### src → erl Relation
| File in ee/mpeg/src | Includes file in ee/erl |
| erl-support.c | include / erl.h |

---

## PS2SDK: ee/mpeg/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000333_000437.html>

###### src → include Relation
| File in ee/mpeg/src | Includes file in ee/mpeg/include |
| libmpeg.c | libmpeg.h |
| libmpeg_core.c | libmpeg.h |
| libmpeg_internal.h | libmpeg.h |

---

## PS2SDK: ee/network -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000334_000000.html>

###### network → common Relation
| File in ee/network | Includes file in common |
| tcpip / src / include / arch / cc.h | include / errno.h |
| tcpip / src / ps2ip.c | include / netman.h |
| tcpip / src / ps2ip_ps2sdk.c | include / errno.h |
| netman / src / netman.c | include / errno.h |
| netman / src / netman.c | include / netman.h |
| netman / src / netman.c | include / netman_rpc.h |
| netman / src / rpc_client.c | include / errno.h |
| netman / src / rpc_client.c | include / netman.h |
| netman / src / rpc_client.c | include / netman_rpc.h |
| netman / src / rpc_server.c | include / errno.h |
| netman / src / rpc_server.c | include / netman.h |
| netman / src / rpc_server.c | include / netman_rpc.h |

---

## PS2SDK: ee/network -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000334_000006.html>

###### network → iop Relation
| File in ee/network | Includes file in iop |
| tcpip / src / include / arch / cc.h | tcpip / tcpip-base / include / stdlib.h |
| tcpip / src / include / arch / cc.h | kernel / include / sys / time.h |
| tcpip / include / ps2ip.h | kernel / include / sys / time.h |
| tcpip / src / ps2ip.c | system / stdio / include / stdio.h |
| tcpip / src / sys_arch.c | tcpip / tcpip-base / include / stdlib.h |
| tcpip / src / sys_arch.c | system / stdio / include / stdio.h |
| tcpip / src / sys_arch.c | kernel / include / sys / time.h |
| netman / src / rpc_client.c | system / stdio / include / stdio.h |
| netman / src / rpc_server.c | system / stdio / include / stdio.h |

---

## PS2SDK: ee/network -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000334_000324.html>

###### network → kernel Relation
| File in ee/network | Includes file in ee/kernel |
| tcpip / src / include / arch / sys_arch.h | include / kernel.h |
| tcpip / src / sys_arch.c | include / kernel.h |
| tcpip / src / sys_arch.c | include / kernel_util.h |
| netman / src / netman.c | include / kernel.h |
| netman / src / rpc_client.c | include / kernel.h |
| netman / src / rpc_client.c | include / iopcontrol.h |
| netman / src / rpc_server.c | include / kernel.h |

---

## PS2SDK: ee/network -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000334_000402.html>

###### network → erl Relation
| File in ee/network | Includes file in ee/erl |
| tcpip / src / erl-support.c | include / erl.h |
| netman / src / erl-support.c | include / erl.h |

---

## PS2SDK: ee/network/netman -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000335_000000.html>

###### netman → common Relation
| File in ee/network/netman | Includes file in common |
| src / netman.c | include / errno.h |
| src / netman.c | include / netman.h |
| src / netman.c | include / netman_rpc.h |
| src / rpc_client.c | include / errno.h |
| src / rpc_client.c | include / netman.h |
| src / rpc_client.c | include / netman_rpc.h |
| src / rpc_server.c | include / errno.h |
| src / rpc_server.c | include / netman.h |
| src / rpc_server.c | include / netman_rpc.h |

---

## PS2SDK: ee/network/netman -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000335_000006.html>

###### netman → iop Relation
| File in ee/network/netman | Includes file in iop |
| src / rpc_client.c | system / stdio / include / stdio.h |
| src / rpc_server.c | system / stdio / include / stdio.h |

---

## PS2SDK: ee/network/netman -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000335_000324.html>

###### netman → kernel Relation
| File in ee/network/netman | Includes file in ee/kernel |
| src / netman.c | include / kernel.h |
| src / rpc_client.c | include / kernel.h |
| src / rpc_client.c | include / iopcontrol.h |
| src / rpc_server.c | include / kernel.h |

---

## PS2SDK: ee/network/netman -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000335_000402.html>

###### netman → erl Relation
| File in ee/network/netman | Includes file in ee/erl |
| src / erl-support.c | include / erl.h |

---

## PS2SDK: ee/network/netman/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000336_000000.html>

###### src → common Relation
| File in ee/network/netman/src | Includes file in common |
| netman.c | include / errno.h |
| netman.c | include / netman.h |
| netman.c | include / netman_rpc.h |
| rpc_client.c | include / errno.h |
| rpc_client.c | include / netman.h |
| rpc_client.c | include / netman_rpc.h |
| rpc_server.c | include / errno.h |
| rpc_server.c | include / netman.h |
| rpc_server.c | include / netman_rpc.h |

---

## PS2SDK: ee/network/netman/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000336_000006.html>

###### src → iop Relation
| File in ee/network/netman/src | Includes file in iop |
| rpc_client.c | system / stdio / include / stdio.h |
| rpc_server.c | system / stdio / include / stdio.h |

---

## PS2SDK: ee/network/netman/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000336_000324.html>

###### src → kernel Relation
| File in ee/network/netman/src | Includes file in ee/kernel |
| netman.c | include / kernel.h |
| rpc_client.c | include / iopcontrol.h |
| rpc_client.c | include / kernel.h |
| rpc_server.c | include / kernel.h |

---

## PS2SDK: ee/network/netman/src -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000336_000402.html>

###### src → erl Relation
| File in ee/network/netman/src | Includes file in ee/erl |
| erl-support.c | include / erl.h |

---

## PS2SDK: ee/network/tcpip -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000337_000000.html>

###### tcpip → common Relation
| File in ee/network/tcpip | Includes file in common |
| src / include / arch / cc.h | include / errno.h |
| src / ps2ip.c | include / netman.h |
| src / ps2ip_ps2sdk.c | include / errno.h |

---

## PS2SDK: ee/network/tcpip -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000337_000006.html>

###### tcpip → iop Relation
| File in ee/network/tcpip | Includes file in iop |
| src / include / arch / cc.h | tcpip / tcpip-base / include / stdlib.h |
| src / include / arch / cc.h | kernel / include / sys / time.h |
| src / ps2ip.c | system / stdio / include / stdio.h |
| include / ps2ip.h | kernel / include / sys / time.h |
| src / sys_arch.c | system / stdio / include / stdio.h |
| src / sys_arch.c | tcpip / tcpip-base / include / stdlib.h |
| src / sys_arch.c | kernel / include / sys / time.h |

---

## PS2SDK: ee/network/tcpip -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000337_000324.html>

###### tcpip → kernel Relation
| File in ee/network/tcpip | Includes file in ee/kernel |
| src / sys_arch.c | include / kernel.h |
| src / sys_arch.c | include / kernel_util.h |
| src / include / arch / sys_arch.h | include / kernel.h |

---

## PS2SDK: ee/network/tcpip -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000337_000402.html>

###### tcpip → erl Relation
| File in ee/network/tcpip | Includes file in ee/erl |
| src / erl-support.c | include / erl.h |

---

## PS2SDK: ee/network/tcpip/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000338_000000.html>

###### src → common Relation
| File in ee/network/tcpip/src | Includes file in common |
| include / arch / cc.h | include / errno.h |
| ps2ip.c | include / netman.h |
| ps2ip_ps2sdk.c | include / errno.h |

---

## PS2SDK: ee/network/tcpip/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000338_000006.html>

###### src → iop Relation
| File in ee/network/tcpip/src | Includes file in iop |
| include / arch / cc.h | tcpip / tcpip-base / include / stdlib.h |
| include / arch / cc.h | kernel / include / sys / time.h |
| ps2ip.c | system / stdio / include / stdio.h |
| sys_arch.c | system / stdio / include / stdio.h |
| sys_arch.c | tcpip / tcpip-base / include / stdlib.h |
| sys_arch.c | kernel / include / sys / time.h |

---

## PS2SDK: ee/network/tcpip/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000338_000324.html>

###### src → kernel Relation
| File in ee/network/tcpip/src | Includes file in ee/kernel |
| sys_arch.c | include / kernel.h |
| sys_arch.c | include / kernel_util.h |
| include / arch / sys_arch.h | include / kernel.h |

---

## PS2SDK: ee/network/tcpip/src -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000338_000402.html>

###### src → erl Relation
| File in ee/network/tcpip/src | Includes file in ee/erl |
| erl-support.c | include / erl.h |

---

## PS2SDK: ee/packet -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000339_000000.html>

###### packet → common Relation
| File in ee/packet | Includes file in common |
| include / packet.h | include / tamtypes.h |

---

## PS2SDK: ee/packet -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000339_000006.html>

###### packet → iop Relation
| File in ee/packet | Includes file in iop |
| src / packet.c | tcpip / tcpip-base / include / stdlib.h |

---

## PS2SDK: ee/packet -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000339_000402.html>

###### packet → erl Relation
| File in ee/packet | Includes file in ee/erl |
| src / erl-support.c | include / erl.h |

---

## PS2SDK: ee/packet/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000340_000006.html>

###### src → iop Relation
| File in ee/packet/src | Includes file in iop |
| packet.c | tcpip / tcpip-base / include / stdlib.h |

---

## PS2SDK: ee/packet/src -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000340_000402.html>

###### src → erl Relation
| File in ee/packet/src | Includes file in ee/erl |
| erl-support.c | include / erl.h |

---

## PS2SDK: ee/packet/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000340_000445.html>

###### src → include Relation
| File in ee/packet/src | Includes file in ee/packet/include |
| packet.c | packet.h |

---

## PS2SDK: ee/packet2 -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000341_000000.html>

###### packet2 → common Relation
| File in ee/packet2 | Includes file in common |
| include / packet2_types.h | include / tamtypes.h |
| include / packet2_utils.h | include / gs_gp.h |
| include / packet2_utils.h | include / tamtypes.h |

---

## PS2SDK: ee/packet2 -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000341_000006.html>

###### packet2 → iop Relation
| File in ee/packet2 | Includes file in iop |
| src / packet2.c | system / stdio / include / stdio.h |

---

## PS2SDK: ee/packet2 -&gt; draw Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000341_000312.html>

###### packet2 → draw Relation
| File in ee/packet2 | Includes file in ee/draw |
| include / packet2_utils.h | include / draw3d.h |
| include / packet2_utils.h | include / draw_buffers.h |
| include / packet2_utils.h | include / draw_sampling.h |

---

## PS2SDK: ee/packet2 -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000341_000324.html>

###### packet2 → kernel Relation
| File in ee/packet2 | Includes file in ee/kernel |
| src / packet2.c | include / kernel.h |

---

## PS2SDK: ee/packet2 -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000341_000402.html>

###### packet2 → erl Relation
| File in ee/packet2 | Includes file in ee/erl |
| src / erl-support.c | include / erl.h |

---

## PS2SDK: ee/packet2/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000342_000006.html>

###### src → iop Relation
| File in ee/packet2/src | Includes file in iop |
| packet2.c | system / stdio / include / stdio.h |

---

## PS2SDK: ee/packet2/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000342_000324.html>

###### src → kernel Relation
| File in ee/packet2/src | Includes file in ee/kernel |
| packet2.c | include / kernel.h |

---

## PS2SDK: ee/packet2/src -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000342_000402.html>

###### src → erl Relation
| File in ee/packet2/src | Includes file in ee/erl |
| erl-support.c | include / erl.h |

---

## PS2SDK: ee/rpc -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000343_000000.html>

###### rpc → common Relation
| File in ee/rpc | Includes file in common |
| filexio / include / fileXio_rpc.h | include / fileXio.h |
| cdvd / include / libcdvd.h | include / libcdvd-common.h |
| hdd / include / libhdd.h | include / hdd-ioctl.h |
| hdd / include / libhdd.h | include / tamtypes.h |
| memorycard / include / libmc.h | include / libmc-common.h |
| remote / include / librm.h | include / librm-common.h |
| ps2snd / include / libsd.h | include / libsd-common.h |
| sdr / include / libsdr.h | include / libsd-common.h |
| sdr / include / libsdr.h | include / libsdr-common.h |
| secr / include / libsecr.h | include / libsecr-common.h |
| keyboard / include / ps2kbd.h | include / tamtypes.h |
| mouse / include / ps2mouse.h | include / tamtypes.h |
| memorycard / src / libmc.c | include / tamtypes.h |
| keyboard / src / libkbd.c | include / tamtypes.h |
| ahx / src / ahx_rpc.c | include / tamtypes.h |
| filexio / src / fileXio_ps2sdk.c | include / errno.h |
| filexio / src / fileXio_ps2sdk.c | include / iox_stat.h |
| filexio / src / fileXio_rpc.c | include / tamtypes.h |
| filexio / src / fileXio_rpc.c | include / errno.h |
| ps2snd / src / ps2snd.c | include / ps2snd.h |
| pad / src / libpad.c | include / tamtypes.h |
| remote / src / librm.c | include / tamtypes.h |
| multitap / src / libmtap.c | include / tamtypes.h |
| tcpips / src / ps2ipc.c | include / tamtypes.h |
| tcpips / src / ps2ipc.c | include / ps2ip_rpc.h |
| tcpips / src / ps2ipc_ps2sdk.c | include / errno.h |
| sior / src / sior_rpc.c | include / tamtypes.h |
| audsrv / src / audsrv_rpc.c | include / tamtypes.h |
| camera / src / ps2cam_rpc.c | include / tamtypes.h |
| cdvd / src / libcdvd.c | include / tamtypes.h |
| cdvd / src / ncmd.c | include / libcdvd-rpc.h |
| cdvd / src / scmd.c | include / libcdvd-rpc.h |
| poweroff / src / poweroff.c | include / errno.h |
| poweroff / src / poweroff.c | include / tamtypes.h |
| poweroff / src / poweroff.c | include / pwroff_rpc.h |
| mouse / src / libmouse.c | include / tamtypes.h |
| hdd / src / libhdd.c | include / tamtypes.h |
| hdd / src / libhdd.c | include / errno.h |
| hdd / src / libhdd.c | include / sys / ioctl.h |
| hdd / src / libhdd.c | include / io_common.h |

---

## PS2SDK: ee/rpc -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000343_000006.html>

###### rpc → iop Relation
| File in ee/rpc | Includes file in iop |
| secr / src / libsecr.c | system / stdio / include / stdio.h |
| ahx / src / ahx_rpc.c | tcpip / tcpip-base / include / stdlib.h |
| ahx / src / ahx_rpc.c | system / stdio / include / stdio.h |
| filexio / src / fileXio_ps2sdk.c | system / stdio / include / stdio.h |
| filexio / src / fileXio_ps2sdk.c | tcpip / tcpip-base / include / stdlib.h |
| filexio / src / fileXio_rpc.c | system / stdio / include / stdio.h |
| filexio / src / fileXio_rpc.c | tcpip / tcpip-base / include / stdlib.h |
| ps2snd / src / ps2snd.c | system / stdio / include / stdio.h |
| pad / src / libpad.c | system / stdio / include / stdio.h |
| remote / src / librm.c | system / stdio / include / stdio.h |
| sior / src / sior_rpc.c | tcpip / tcpip-base / include / stdlib.h |
| sior / src / sior_rpc.c | system / stdio / include / stdio.h |
| audsrv / src / audsrv_rpc.c | system / stdio / include / stdio.h |
| camera / src / ps2cam_rpc.c | system / stdio / include / stdio.h |
| cdvd / src / libcdvd.c | system / stdio / include / stdio.h |
| cdvd / src / ncmd.c | system / stdio / include / stdio.h |
| cdvd / src / scmd.c | system / stdio / include / stdio.h |
| cdvd / src / scmd.c | kernel / include / sys / time.h |
| poweroff / src / poweroff.c | system / stdio / include / stdio.h |
| mouse / src / libmouse.c | system / stdio / include / stdio.h |
| hdd / src / libhdd.c | system / stdio / include / stdio.h |
| hdd / src / libhdd.c | tcpip / tcpip-base / include / stdlib.h |

---

## PS2SDK: ee/rpc -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000343_000324.html>

###### rpc → kernel Relation
| File in ee/rpc | Includes file in ee/kernel |
| secr / src / libsecr.c | include / kernel.h |
| secr / src / libsecr.c | include / iopcontrol.h |
| memorycard / src / libmc.c | include / kernel.h |
| memorycard / src / libmc.c | include / iopcontrol.h |
| keyboard / src / libkbd.c | include / iopcontrol.h |
| ahx / src / ahx_rpc.c | include / kernel.h |
| ahx / src / ahx_rpc.c | include / iopcontrol.h |
| filexio / src / fileXio_ps2sdk.c | include / fileio.h |
| filexio / src / fileXio_rpc.c | include / kernel.h |
| filexio / src / fileXio_rpc.c | include / iopcontrol.h |
| ps2snd / src / ps2snd.c | include / kernel.h |
| ps2snd / src / ps2snd.c | include / iopheap.h |
| ps2snd / src / ps2snd.c | include / iopcontrol.h |
| pad / src / libpad.c | include / kernel.h |
| pad / src / libpad.c | include / iopcontrol.h |
| remote / src / librm.c | include / kernel.h |
| remote / src / librm.c | include / iopcontrol.h |
| multitap / src / libmtap.c | include / kernel.h |
| multitap / src / libmtap.c | include / iopcontrol.h |
| tcpips / src / ps2ipc.c | include / kernel.h |
| tcpips / src / ps2ipc.c | include / iopcontrol.h |
| sior / src / sior_rpc.c | include / kernel.h |
| sior / src / sior_rpc.c | include / sio.h |
| audsrv / src / audsrv_rpc.c | include / kernel.h |
| audsrv / src / audsrv_rpc.c | include / iopheap.h |
| audsrv / src / audsrv_rpc.c | include / iopcontrol.h |
| camera / src / ps2cam_rpc.c | include / kernel.h |
| camera / src / ps2cam_rpc.c | include / iopcontrol.h |
| cdvd / src / libcdvd.c | include / kernel.h |
| cdvd / src / libcdvd.c | include / iopcontrol.h |
| cdvd / src / ncmd.c | include / kernel.h |
| cdvd / src / ncmd.c | include / iopcontrol.h |
| cdvd / src / scmd.c | include / kernel.h |
| cdvd / src / scmd.c | include / osd_config.h |
| cdvd / src / scmd.c | include / iopcontrol.h |
| poweroff / src / poweroff.c | include / kernel.h |
| poweroff / src / poweroff.c | include / iopcontrol.h |
| sdr / src / sdr_i.h | include / kernel.h |
| sdr / src / sdr_i.h | include / iopcontrol.h |
| mouse / src / libmouse.c | include / kernel.h |
| mouse / src / libmouse.c | include / iopcontrol.h |
| hdd / src / libhdd.c | include / kernel.h |
| hdd / src / libhdd.c | include / loadfile.h |
| hdd / src / libhdd.c | include / iopheap.h |

---

## PS2SDK: ee/rpc -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000343_000402.html>

###### rpc → erl Relation
| File in ee/rpc | Includes file in ee/erl |
| secr / src / erl-support.c | include / erl.h |
| memorycard / src / erl-support.c | include / erl.h |
| keyboard / src / erl-support.c | include / erl.h |
| ahx / src / erl-support.c | include / erl.h |
| filexio / src / erl-support.c | include / erl.h |
| ps2snd / src / erl-support.c | include / erl.h |
| pad / src / erl-support.c | include / erl.h |
| remote / src / erl-support.c | include / erl.h |
| multitap / src / erl-support.c | include / erl.h |
| tcpips / src / erl-support.c | include / erl.h |
| sior / src / erl-support.c | include / erl.h |
| audsrv / src / erl-support.c | include / erl.h |
| camera / src / erl-support.c | include / erl.h |
| cdvd / src / erl-support.c | include / erl.h |
| poweroff / src / erl-support.c | include / erl.h |
| sdr / src / erl-support.c | include / erl.h |
| mouse / src / erl-support.c | include / erl.h |
| hdd / src / erl-support.c | include / erl.h |

---

## PS2SDK: ee/rpc -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000343_000412.html>

###### rpc → include Relation
| File in ee/rpc | Includes file in ee/kernel/include |
| secr / src / libsecr.c | kernel.h |
| secr / src / libsecr.c | iopcontrol.h |
| memorycard / src / libmc.c | kernel.h |
| memorycard / src / libmc.c | iopcontrol.h |
| keyboard / src / libkbd.c | iopcontrol.h |
| ahx / src / ahx_rpc.c | kernel.h |
| ahx / src / ahx_rpc.c | iopcontrol.h |
| filexio / src / fileXio_ps2sdk.c | fileio.h |
| filexio / src / fileXio_rpc.c | kernel.h |
| filexio / src / fileXio_rpc.c | iopcontrol.h |
| ps2snd / src / ps2snd.c | kernel.h |
| ps2snd / src / ps2snd.c | iopheap.h |
| ps2snd / src / ps2snd.c | iopcontrol.h |
| pad / src / libpad.c | kernel.h |
| pad / src / libpad.c | iopcontrol.h |
| remote / src / librm.c | kernel.h |
| remote / src / librm.c | iopcontrol.h |
| multitap / src / libmtap.c | kernel.h |
| multitap / src / libmtap.c | iopcontrol.h |
| tcpips / src / ps2ipc.c | kernel.h |
| tcpips / src / ps2ipc.c | iopcontrol.h |
| sior / src / sior_rpc.c | kernel.h |
| sior / src / sior_rpc.c | sio.h |
| audsrv / src / audsrv_rpc.c | kernel.h |
| audsrv / src / audsrv_rpc.c | iopheap.h |
| audsrv / src / audsrv_rpc.c | iopcontrol.h |
| camera / src / ps2cam_rpc.c | kernel.h |
| camera / src / ps2cam_rpc.c | iopcontrol.h |
| cdvd / src / libcdvd.c | kernel.h |
| cdvd / src / libcdvd.c | iopcontrol.h |
| cdvd / src / ncmd.c | kernel.h |
| cdvd / src / ncmd.c | iopcontrol.h |
| cdvd / src / scmd.c | kernel.h |
| cdvd / src / scmd.c | osd_config.h |
| cdvd / src / scmd.c | iopcontrol.h |
| poweroff / src / poweroff.c | kernel.h |
| poweroff / src / poweroff.c | iopcontrol.h |
| sdr / src / sdr_i.h | kernel.h |
| sdr / src / sdr_i.h | iopcontrol.h |
| mouse / src / libmouse.c | kernel.h |
| mouse / src / libmouse.c | iopcontrol.h |
| hdd / src / libhdd.c | kernel.h |
| hdd / src / libhdd.c | loadfile.h |
| hdd / src / libhdd.c | iopheap.h |

---

## PS2SDK: ee/rpc/ahx -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000344_000000.html>

###### ahx → common Relation
| File in ee/rpc/ahx | Includes file in common |
| src / ahx_rpc.c | include / tamtypes.h |

---

## PS2SDK: ee/rpc/ahx -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000344_000006.html>

###### ahx → iop Relation
| File in ee/rpc/ahx | Includes file in iop |
| src / ahx_rpc.c | tcpip / tcpip-base / include / stdlib.h |
| src / ahx_rpc.c | system / stdio / include / stdio.h |

---

## PS2SDK: ee/rpc/ahx -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000344_000324.html>

###### ahx → kernel Relation
| File in ee/rpc/ahx | Includes file in ee/kernel |
| src / ahx_rpc.c | include / kernel.h |
| src / ahx_rpc.c | include / iopcontrol.h |

---

## PS2SDK: ee/rpc/ahx -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000344_000402.html>

###### ahx → erl Relation
| File in ee/rpc/ahx | Includes file in ee/erl |
| src / erl-support.c | include / erl.h |

---

## PS2SDK: ee/rpc/ahx/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000345_000000.html>

###### src → common Relation
| File in ee/rpc/ahx/src | Includes file in common |
| ahx_rpc.c | include / tamtypes.h |

---

## PS2SDK: ee/rpc/ahx/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000345_000006.html>

###### src → iop Relation
| File in ee/rpc/ahx/src | Includes file in iop |
| ahx_rpc.c | system / stdio / include / stdio.h |
| ahx_rpc.c | tcpip / tcpip-base / include / stdlib.h |

---

## PS2SDK: ee/rpc/ahx/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000345_000324.html>

###### src → kernel Relation
| File in ee/rpc/ahx/src | Includes file in ee/kernel |
| ahx_rpc.c | include / iopcontrol.h |
| ahx_rpc.c | include / kernel.h |

---

## PS2SDK: ee/rpc/ahx/src -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000345_000402.html>

###### src → erl Relation
| File in ee/rpc/ahx/src | Includes file in ee/erl |
| erl-support.c | include / erl.h |

---

## PS2SDK: ee/rpc/ahx/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000345_000447.html>

###### src → include Relation
| File in ee/rpc/ahx/src | Includes file in ee/rpc/ahx/include |
| ahx_rpc.c | ahx_rpc.h |

---

## PS2SDK: ee/rpc/audsrv -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000346_000000.html>

###### audsrv → common Relation
| File in ee/rpc/audsrv | Includes file in common |
| src / audsrv_rpc.c | include / tamtypes.h |

---

## PS2SDK: ee/rpc/audsrv -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000346_000006.html>

###### audsrv → iop Relation
| File in ee/rpc/audsrv | Includes file in iop |
| src / audsrv_rpc.c | system / stdio / include / stdio.h |

---

## PS2SDK: ee/rpc/audsrv -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000346_000324.html>

###### audsrv → kernel Relation
| File in ee/rpc/audsrv | Includes file in ee/kernel |
| src / audsrv_rpc.c | include / kernel.h |
| src / audsrv_rpc.c | include / iopheap.h |
| src / audsrv_rpc.c | include / iopcontrol.h |

---

## PS2SDK: ee/rpc/audsrv -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000346_000402.html>

###### audsrv → erl Relation
| File in ee/rpc/audsrv | Includes file in ee/erl |
| src / erl-support.c | include / erl.h |

---

## PS2SDK: ee/rpc/audsrv/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000347_000000.html>

###### src → common Relation
| File in ee/rpc/audsrv/src | Includes file in common |
| audsrv_rpc.c | include / tamtypes.h |

---

## PS2SDK: ee/rpc/audsrv/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000347_000006.html>

###### src → iop Relation
| File in ee/rpc/audsrv/src | Includes file in iop |
| audsrv_rpc.c | system / stdio / include / stdio.h |

---

## PS2SDK: ee/rpc/audsrv/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000347_000324.html>

###### src → kernel Relation
| File in ee/rpc/audsrv/src | Includes file in ee/kernel |
| audsrv_rpc.c | include / iopcontrol.h |
| audsrv_rpc.c | include / iopheap.h |
| audsrv_rpc.c | include / kernel.h |

---

## PS2SDK: ee/rpc/audsrv/src -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000347_000402.html>

###### src → erl Relation
| File in ee/rpc/audsrv/src | Includes file in ee/erl |
| erl-support.c | include / erl.h |

---

## PS2SDK: ee/rpc/camera -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000348_000000.html>

###### camera → common Relation
| File in ee/rpc/camera | Includes file in common |
| src / ps2cam_rpc.c | include / tamtypes.h |

---

## PS2SDK: ee/rpc/camera -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000348_000006.html>

###### camera → iop Relation
| File in ee/rpc/camera | Includes file in iop |
| src / ps2cam_rpc.c | system / stdio / include / stdio.h |

---

## PS2SDK: ee/rpc/camera -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000348_000324.html>

###### camera → kernel Relation
| File in ee/rpc/camera | Includes file in ee/kernel |
| src / ps2cam_rpc.c | include / kernel.h |
| src / ps2cam_rpc.c | include / iopcontrol.h |

---

## PS2SDK: ee/rpc/camera -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000348_000402.html>

###### camera → erl Relation
| File in ee/rpc/camera | Includes file in ee/erl |
| src / erl-support.c | include / erl.h |

---

## PS2SDK: ee/rpc/camera/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000349_000000.html>

###### src → common Relation
| File in ee/rpc/camera/src | Includes file in common |
| ps2cam_rpc.c | include / tamtypes.h |

---

## PS2SDK: ee/rpc/camera/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000349_000006.html>

###### src → iop Relation
| File in ee/rpc/camera/src | Includes file in iop |
| ps2cam_rpc.c | system / stdio / include / stdio.h |

---

## PS2SDK: ee/rpc/camera/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000349_000324.html>

###### src → kernel Relation
| File in ee/rpc/camera/src | Includes file in ee/kernel |
| ps2cam_rpc.c | include / iopcontrol.h |
| ps2cam_rpc.c | include / kernel.h |

---

## PS2SDK: ee/rpc/camera/src -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000349_000402.html>

###### src → erl Relation
| File in ee/rpc/camera/src | Includes file in ee/erl |
| erl-support.c | include / erl.h |

---

## PS2SDK: ee/rpc/camera/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000349_000450.html>

###### src → include Relation
| File in ee/rpc/camera/src | Includes file in ee/rpc/camera/include |
| ps2cam_rpc.c | ps2cam_rpc.h |

---

## PS2SDK: ee/rpc/cdvd -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000350_000000.html>

###### cdvd → common Relation
| File in ee/rpc/cdvd | Includes file in common |
| include / libcdvd.h | include / libcdvd-common.h |
| src / libcdvd.c | include / tamtypes.h |
| src / ncmd.c | include / libcdvd-rpc.h |
| src / scmd.c | include / libcdvd-rpc.h |

---

## PS2SDK: ee/rpc/cdvd -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000350_000006.html>

###### cdvd → iop Relation
| File in ee/rpc/cdvd | Includes file in iop |
| src / libcdvd.c | system / stdio / include / stdio.h |
| src / ncmd.c | system / stdio / include / stdio.h |
| src / scmd.c | system / stdio / include / stdio.h |
| src / scmd.c | kernel / include / sys / time.h |

---

## PS2SDK: ee/rpc/cdvd -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000350_000324.html>

###### cdvd → kernel Relation
| File in ee/rpc/cdvd | Includes file in ee/kernel |
| src / libcdvd.c | include / kernel.h |
| src / libcdvd.c | include / iopcontrol.h |
| src / ncmd.c | include / kernel.h |
| src / ncmd.c | include / iopcontrol.h |
| src / scmd.c | include / kernel.h |
| src / scmd.c | include / osd_config.h |
| src / scmd.c | include / iopcontrol.h |

---

## PS2SDK: ee/rpc/cdvd -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000350_000402.html>

###### cdvd → erl Relation
| File in ee/rpc/cdvd | Includes file in ee/erl |
| src / erl-support.c | include / erl.h |

---

## PS2SDK: ee/rpc/cdvd/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000351_000000.html>

###### src → common Relation
| File in ee/rpc/cdvd/src | Includes file in common |
| libcdvd.c | include / tamtypes.h |
| ncmd.c | include / libcdvd-rpc.h |
| scmd.c | include / libcdvd-rpc.h |

---

## PS2SDK: ee/rpc/cdvd/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000351_000006.html>

###### src → iop Relation
| File in ee/rpc/cdvd/src | Includes file in iop |
| libcdvd.c | system / stdio / include / stdio.h |
| ncmd.c | system / stdio / include / stdio.h |
| scmd.c | system / stdio / include / stdio.h |
| scmd.c | kernel / include / sys / time.h |

---

## PS2SDK: ee/rpc/cdvd/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000351_000324.html>

###### src → kernel Relation
| File in ee/rpc/cdvd/src | Includes file in ee/kernel |
| libcdvd.c | include / iopcontrol.h |
| libcdvd.c | include / kernel.h |
| ncmd.c | include / iopcontrol.h |
| ncmd.c | include / kernel.h |
| scmd.c | include / iopcontrol.h |
| scmd.c | include / kernel.h |
| scmd.c | include / osd_config.h |

---

## PS2SDK: ee/rpc/cdvd/src -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000351_000402.html>

###### src → erl Relation
| File in ee/rpc/cdvd/src | Includes file in ee/erl |
| erl-support.c | include / erl.h |

---

## PS2SDK: ee/rpc/cdvd/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000351_000451.html>

###### src → include Relation
| File in ee/rpc/cdvd/src | Includes file in ee/rpc/cdvd/include |
| libcdvd.c | libcdvd.h |
| ncmd.c | libcdvd.h |
| scmd.c | libcdvd.h |

---

## PS2SDK: ee/rpc/filexio -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000352_000000.html>

###### filexio → common Relation
| File in ee/rpc/filexio | Includes file in common |
| include / fileXio_rpc.h | include / fileXio.h |
| src / fileXio_ps2sdk.c | include / errno.h |
| src / fileXio_ps2sdk.c | include / iox_stat.h |
| src / fileXio_rpc.c | include / tamtypes.h |
| src / fileXio_rpc.c | include / errno.h |

---

## PS2SDK: ee/rpc/filexio -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000352_000006.html>

###### filexio → iop Relation
| File in ee/rpc/filexio | Includes file in iop |
| src / fileXio_ps2sdk.c | system / stdio / include / stdio.h |
| src / fileXio_ps2sdk.c | tcpip / tcpip-base / include / stdlib.h |
| src / fileXio_rpc.c | system / stdio / include / stdio.h |
| src / fileXio_rpc.c | tcpip / tcpip-base / include / stdlib.h |

---

## PS2SDK: ee/rpc/filexio -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000352_000324.html>

###### filexio → kernel Relation
| File in ee/rpc/filexio | Includes file in ee/kernel |
| src / fileXio_ps2sdk.c | include / fileio.h |
| src / fileXio_rpc.c | include / kernel.h |
| src / fileXio_rpc.c | include / iopcontrol.h |

---

## PS2SDK: ee/rpc/filexio -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000352_000402.html>

###### filexio → erl Relation
| File in ee/rpc/filexio | Includes file in ee/erl |
| src / erl-support.c | include / erl.h |

---

## PS2SDK: ee/rpc/filexio/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000353_000000.html>

###### src → common Relation
| File in ee/rpc/filexio/src | Includes file in common |
| fileXio_ps2sdk.c | include / errno.h |
| fileXio_ps2sdk.c | include / iox_stat.h |
| fileXio_rpc.c | include / errno.h |
| fileXio_rpc.c | include / tamtypes.h |

---

## PS2SDK: ee/rpc/filexio/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000353_000006.html>

###### src → iop Relation
| File in ee/rpc/filexio/src | Includes file in iop |
| fileXio_ps2sdk.c | system / stdio / include / stdio.h |
| fileXio_ps2sdk.c | tcpip / tcpip-base / include / stdlib.h |
| fileXio_rpc.c | system / stdio / include / stdio.h |
| fileXio_rpc.c | tcpip / tcpip-base / include / stdlib.h |

---

## PS2SDK: ee/rpc/filexio/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000353_000324.html>

###### src → kernel Relation
| File in ee/rpc/filexio/src | Includes file in ee/kernel |
| fileXio_ps2sdk.c | include / fileio.h |
| fileXio_rpc.c | include / iopcontrol.h |
| fileXio_rpc.c | include / kernel.h |

---

## PS2SDK: ee/rpc/filexio/src -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000353_000402.html>

###### src → erl Relation
| File in ee/rpc/filexio/src | Includes file in ee/erl |
| erl-support.c | include / erl.h |

---

## PS2SDK: ee/rpc/filexio/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000353_000452.html>

###### src → include Relation
| File in ee/rpc/filexio/src | Includes file in ee/rpc/filexio/include |
| fileXio_ps2sdk.c | fileXio_rpc.h |
| fileXio_rpc.c | fileXio_rpc.h |

---

## PS2SDK: ee/rpc/hdd -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000354_000000.html>

###### hdd → common Relation
| File in ee/rpc/hdd | Includes file in common |
| include / libhdd.h | include / tamtypes.h |
| include / libhdd.h | include / hdd-ioctl.h |
| src / libhdd.c | include / tamtypes.h |
| src / libhdd.c | include / errno.h |
| src / libhdd.c | include / sys / ioctl.h |
| src / libhdd.c | include / io_common.h |

---

## PS2SDK: ee/rpc/hdd -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000354_000006.html>

###### hdd → iop Relation
| File in ee/rpc/hdd | Includes file in iop |
| src / libhdd.c | system / stdio / include / stdio.h |
| src / libhdd.c | tcpip / tcpip-base / include / stdlib.h |

---

## PS2SDK: ee/rpc/hdd -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000354_000324.html>

###### hdd → kernel Relation
| File in ee/rpc/hdd | Includes file in ee/kernel |
| src / libhdd.c | include / kernel.h |
| src / libhdd.c | include / loadfile.h |
| src / libhdd.c | include / iopheap.h |

---

## PS2SDK: ee/rpc/hdd -&gt; filexio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000354_000352.html>

###### hdd → filexio Relation
| File in ee/rpc/hdd | Includes file in ee/rpc/filexio |
| src / libhdd.c | include / fileXio_rpc.h |

---

## PS2SDK: ee/rpc/hdd -&gt; poweroff Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000354_000366.html>

###### hdd → poweroff Relation
| File in ee/rpc/hdd | Includes file in ee/rpc/poweroff |
| include / libhdd.h | include / libpwroff.h |

---

## PS2SDK: ee/rpc/hdd -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000354_000402.html>

###### hdd → erl Relation
| File in ee/rpc/hdd | Includes file in ee/erl |
| src / erl-support.c | include / erl.h |

---

## PS2SDK: ee/rpc/hdd/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000355_000000.html>

###### src → common Relation
| File in ee/rpc/hdd/src | Includes file in common |
| libhdd.c | include / errno.h |
| libhdd.c | include / io_common.h |
| libhdd.c | include / sys / ioctl.h |
| libhdd.c | include / tamtypes.h |

---

## PS2SDK: ee/rpc/hdd/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000355_000006.html>

###### src → iop Relation
| File in ee/rpc/hdd/src | Includes file in iop |
| libhdd.c | system / stdio / include / stdio.h |
| libhdd.c | tcpip / tcpip-base / include / stdlib.h |

---

## PS2SDK: ee/rpc/hdd/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000355_000324.html>

###### src → kernel Relation
| File in ee/rpc/hdd/src | Includes file in ee/kernel |
| libhdd.c | include / iopheap.h |
| libhdd.c | include / kernel.h |
| libhdd.c | include / loadfile.h |

---

## PS2SDK: ee/rpc/hdd/src -&gt; filexio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000355_000352.html>

###### src → filexio Relation
| File in ee/rpc/hdd/src | Includes file in ee/rpc/filexio |
| libhdd.c | include / fileXio_rpc.h |

---

## PS2SDK: ee/rpc/hdd/src -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000355_000402.html>

###### src → erl Relation
| File in ee/rpc/hdd/src | Includes file in ee/erl |
| erl-support.c | include / erl.h |

---

## PS2SDK: ee/rpc/hdd/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000355_000453.html>

###### src → include Relation
| File in ee/rpc/hdd/src | Includes file in ee/rpc/hdd/include |
| libhdd.c | libhdd.h |

---

## PS2SDK: ee/rpc/keyboard -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000356_000000.html>

###### keyboard → common Relation
| File in ee/rpc/keyboard | Includes file in common |
| include / ps2kbd.h | include / tamtypes.h |
| src / libkbd.c | include / tamtypes.h |

---

## PS2SDK: ee/rpc/keyboard -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000356_000324.html>

###### keyboard → kernel Relation
| File in ee/rpc/keyboard | Includes file in ee/kernel |
| src / libkbd.c | include / iopcontrol.h |

---

## PS2SDK: ee/rpc/keyboard -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000356_000402.html>

###### keyboard → erl Relation
| File in ee/rpc/keyboard | Includes file in ee/erl |
| src / erl-support.c | include / erl.h |

---

## PS2SDK: ee/rpc/keyboard/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000357_000000.html>

###### src → common Relation
| File in ee/rpc/keyboard/src | Includes file in common |
| libkbd.c | include / tamtypes.h |

---

## PS2SDK: ee/rpc/keyboard/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000357_000324.html>

###### src → kernel Relation
| File in ee/rpc/keyboard/src | Includes file in ee/kernel |
| libkbd.c | include / iopcontrol.h |

---

## PS2SDK: ee/rpc/keyboard/src -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000357_000402.html>

###### src → erl Relation
| File in ee/rpc/keyboard/src | Includes file in ee/erl |
| erl-support.c | include / erl.h |

---

## PS2SDK: ee/rpc/keyboard/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000357_000454.html>

###### src → include Relation
| File in ee/rpc/keyboard/src | Includes file in ee/rpc/keyboard/include |
| libkbd.c | libkbd.h |

---

## PS2SDK: ee/rpc/memorycard -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000358_000000.html>

###### memorycard → common Relation
| File in ee/rpc/memorycard | Includes file in common |
| include / libmc.h | include / libmc-common.h |
| src / libmc.c | include / tamtypes.h |

---

## PS2SDK: ee/rpc/memorycard -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000358_000324.html>

###### memorycard → kernel Relation
| File in ee/rpc/memorycard | Includes file in ee/kernel |
| src / libmc.c | include / kernel.h |
| src / libmc.c | include / iopcontrol.h |

---

## PS2SDK: ee/rpc/memorycard -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000358_000402.html>

###### memorycard → erl Relation
| File in ee/rpc/memorycard | Includes file in ee/erl |
| src / erl-support.c | include / erl.h |

---

## PS2SDK: ee/rpc/memorycard/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000359_000000.html>

###### src → common Relation
| File in ee/rpc/memorycard/src | Includes file in common |
| libmc.c | include / tamtypes.h |

---

## PS2SDK: ee/rpc/memorycard/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000359_000324.html>

###### src → kernel Relation
| File in ee/rpc/memorycard/src | Includes file in ee/kernel |
| libmc.c | include / iopcontrol.h |
| libmc.c | include / kernel.h |

---

## PS2SDK: ee/rpc/memorycard/src -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000359_000402.html>

###### src → erl Relation
| File in ee/rpc/memorycard/src | Includes file in ee/erl |
| erl-support.c | include / erl.h |

---

## PS2SDK: ee/rpc/memorycard/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000359_000456.html>

###### src → include Relation
| File in ee/rpc/memorycard/src | Includes file in ee/rpc/memorycard/include |
| libmc.c | libmc.h |

---

## PS2SDK: ee/rpc/mouse -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000360_000000.html>

###### mouse → common Relation
| File in ee/rpc/mouse | Includes file in common |
| include / ps2mouse.h | include / tamtypes.h |
| src / libmouse.c | include / tamtypes.h |

---

## PS2SDK: ee/rpc/mouse -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000360_000006.html>

###### mouse → iop Relation
| File in ee/rpc/mouse | Includes file in iop |
| src / libmouse.c | system / stdio / include / stdio.h |

---

## PS2SDK: ee/rpc/mouse -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000360_000324.html>

###### mouse → kernel Relation
| File in ee/rpc/mouse | Includes file in ee/kernel |
| src / libmouse.c | include / kernel.h |
| src / libmouse.c | include / iopcontrol.h |

---

## PS2SDK: ee/rpc/mouse -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000360_000402.html>

###### mouse → erl Relation
| File in ee/rpc/mouse | Includes file in ee/erl |
| src / erl-support.c | include / erl.h |

---

## PS2SDK: ee/rpc/mouse/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000361_000000.html>

###### src → common Relation
| File in ee/rpc/mouse/src | Includes file in common |
| libmouse.c | include / tamtypes.h |

---

## PS2SDK: ee/rpc/mouse/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000361_000006.html>

###### src → iop Relation
| File in ee/rpc/mouse/src | Includes file in iop |
| libmouse.c | system / stdio / include / stdio.h |

---

## PS2SDK: ee/rpc/mouse/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000361_000324.html>

###### src → kernel Relation
| File in ee/rpc/mouse/src | Includes file in ee/kernel |
| libmouse.c | include / iopcontrol.h |
| libmouse.c | include / kernel.h |

---

## PS2SDK: ee/rpc/mouse/src -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000361_000402.html>

###### src → erl Relation
| File in ee/rpc/mouse/src | Includes file in ee/erl |
| erl-support.c | include / erl.h |

---

## PS2SDK: ee/rpc/mouse/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000361_000457.html>

###### src → include Relation
| File in ee/rpc/mouse/src | Includes file in ee/rpc/mouse/include |
| libmouse.c | libmouse.h |

---

## PS2SDK: ee/rpc/multitap -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000362_000000.html>

###### multitap → common Relation
| File in ee/rpc/multitap | Includes file in common |
| src / libmtap.c | include / tamtypes.h |

---

## PS2SDK: ee/rpc/multitap -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000362_000324.html>

###### multitap → kernel Relation
| File in ee/rpc/multitap | Includes file in ee/kernel |
| src / libmtap.c | include / kernel.h |
| src / libmtap.c | include / iopcontrol.h |

---

## PS2SDK: ee/rpc/multitap -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000362_000402.html>

###### multitap → erl Relation
| File in ee/rpc/multitap | Includes file in ee/erl |
| src / erl-support.c | include / erl.h |

---

## PS2SDK: ee/rpc/multitap/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000363_000000.html>

###### src → common Relation
| File in ee/rpc/multitap/src | Includes file in common |
| libmtap.c | include / tamtypes.h |

---

## PS2SDK: ee/rpc/multitap/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000363_000324.html>

###### src → kernel Relation
| File in ee/rpc/multitap/src | Includes file in ee/kernel |
| libmtap.c | include / iopcontrol.h |
| libmtap.c | include / kernel.h |

---

## PS2SDK: ee/rpc/multitap/src -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000363_000402.html>

###### src → erl Relation
| File in ee/rpc/multitap/src | Includes file in ee/erl |
| erl-support.c | include / erl.h |

---

## PS2SDK: ee/rpc/multitap/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000363_000459.html>

###### src → include Relation
| File in ee/rpc/multitap/src | Includes file in ee/rpc/multitap/include |
| libmtap.c | libmtap.h |

---

## PS2SDK: ee/rpc/pad -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000364_000000.html>

###### pad → common Relation
| File in ee/rpc/pad | Includes file in common |
| src / libpad.c | include / tamtypes.h |

---

## PS2SDK: ee/rpc/pad -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000364_000006.html>

###### pad → iop Relation
| File in ee/rpc/pad | Includes file in iop |
| src / libpad.c | system / stdio / include / stdio.h |

---

## PS2SDK: ee/rpc/pad -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000364_000324.html>

###### pad → kernel Relation
| File in ee/rpc/pad | Includes file in ee/kernel |
| src / libpad.c | include / kernel.h |
| src / libpad.c | include / iopcontrol.h |

---

## PS2SDK: ee/rpc/pad -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000364_000402.html>

###### pad → erl Relation
| File in ee/rpc/pad | Includes file in ee/erl |
| src / erl-support.c | include / erl.h |

---

## PS2SDK: ee/rpc/pad/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000365_000000.html>

###### src → common Relation
| File in ee/rpc/pad/src | Includes file in common |
| libpad.c | include / tamtypes.h |

---

## PS2SDK: ee/rpc/pad/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000365_000006.html>

###### src → iop Relation
| File in ee/rpc/pad/src | Includes file in iop |
| libpad.c | system / stdio / include / stdio.h |

---

## PS2SDK: ee/rpc/pad/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000365_000324.html>

###### src → kernel Relation
| File in ee/rpc/pad/src | Includes file in ee/kernel |
| libpad.c | include / iopcontrol.h |
| libpad.c | include / kernel.h |

---

## PS2SDK: ee/rpc/pad/src -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000365_000402.html>

###### src → erl Relation
| File in ee/rpc/pad/src | Includes file in ee/erl |
| erl-support.c | include / erl.h |

---

## PS2SDK: ee/rpc/pad/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000365_000460.html>

###### src → include Relation
| File in ee/rpc/pad/src | Includes file in ee/rpc/pad/include |
| libpad.c | libpad.h |

---

## PS2SDK: ee/rpc/poweroff -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000366_000000.html>

###### poweroff → common Relation
| File in ee/rpc/poweroff | Includes file in common |
| src / poweroff.c | include / errno.h |
| src / poweroff.c | include / tamtypes.h |
| src / poweroff.c | include / pwroff_rpc.h |

---

## PS2SDK: ee/rpc/poweroff -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000366_000006.html>

###### poweroff → iop Relation
| File in ee/rpc/poweroff | Includes file in iop |
| src / poweroff.c | system / stdio / include / stdio.h |

---

## PS2SDK: ee/rpc/poweroff -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000366_000324.html>

###### poweroff → kernel Relation
| File in ee/rpc/poweroff | Includes file in ee/kernel |
| src / poweroff.c | include / kernel.h |
| src / poweroff.c | include / iopcontrol.h |

---

## PS2SDK: ee/rpc/poweroff -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000366_000402.html>

###### poweroff → erl Relation
| File in ee/rpc/poweroff | Includes file in ee/erl |
| src / erl-support.c | include / erl.h |

---

## PS2SDK: ee/rpc/poweroff/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000367_000000.html>

###### src → common Relation
| File in ee/rpc/poweroff/src | Includes file in common |
| poweroff.c | include / errno.h |
| poweroff.c | include / pwroff_rpc.h |
| poweroff.c | include / tamtypes.h |

---

## PS2SDK: ee/rpc/poweroff/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000367_000006.html>

###### src → iop Relation
| File in ee/rpc/poweroff/src | Includes file in iop |
| poweroff.c | system / stdio / include / stdio.h |

---

## PS2SDK: ee/rpc/poweroff/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000367_000324.html>

###### src → kernel Relation
| File in ee/rpc/poweroff/src | Includes file in ee/kernel |
| poweroff.c | include / iopcontrol.h |
| poweroff.c | include / kernel.h |

---

## PS2SDK: ee/rpc/poweroff/src -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000367_000402.html>

###### src → erl Relation
| File in ee/rpc/poweroff/src | Includes file in ee/erl |
| erl-support.c | include / erl.h |

---

## PS2SDK: ee/rpc/poweroff/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000367_000461.html>

###### src → include Relation
| File in ee/rpc/poweroff/src | Includes file in ee/rpc/poweroff/include |
| poweroff.c | libpwroff.h |

---

## PS2SDK: ee/rpc/ps2snd -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000368_000000.html>

###### ps2snd → common Relation
| File in ee/rpc/ps2snd | Includes file in common |
| include / libsd.h | include / libsd-common.h |
| src / ps2snd.c | include / ps2snd.h |

---

## PS2SDK: ee/rpc/ps2snd -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000368_000006.html>

###### ps2snd → iop Relation
| File in ee/rpc/ps2snd | Includes file in iop |
| src / ps2snd.c | system / stdio / include / stdio.h |

---

## PS2SDK: ee/rpc/ps2snd -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000368_000324.html>

###### ps2snd → kernel Relation
| File in ee/rpc/ps2snd | Includes file in ee/kernel |
| src / ps2snd.c | include / kernel.h |
| src / ps2snd.c | include / iopheap.h |
| src / ps2snd.c | include / iopcontrol.h |

---

## PS2SDK: ee/rpc/ps2snd -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000368_000402.html>

###### ps2snd → erl Relation
| File in ee/rpc/ps2snd | Includes file in ee/erl |
| src / erl-support.c | include / erl.h |

---

## PS2SDK: ee/rpc/ps2snd/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000369_000000.html>

###### src → common Relation
| File in ee/rpc/ps2snd/src | Includes file in common |
| ps2snd.c | include / ps2snd.h |

---

## PS2SDK: ee/rpc/ps2snd/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000369_000006.html>

###### src → iop Relation
| File in ee/rpc/ps2snd/src | Includes file in iop |
| ps2snd.c | system / stdio / include / stdio.h |

---

## PS2SDK: ee/rpc/ps2snd/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000369_000324.html>

###### src → kernel Relation
| File in ee/rpc/ps2snd/src | Includes file in ee/kernel |
| ps2snd.c | include / iopcontrol.h |
| ps2snd.c | include / iopheap.h |
| ps2snd.c | include / kernel.h |

---

## PS2SDK: ee/rpc/ps2snd/src -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000369_000402.html>

###### src → erl Relation
| File in ee/rpc/ps2snd/src | Includes file in ee/erl |
| erl-support.c | include / erl.h |

---

## PS2SDK: ee/rpc/remote -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000370_000000.html>

###### remote → common Relation
| File in ee/rpc/remote | Includes file in common |
| include / librm.h | include / librm-common.h |
| src / librm.c | include / tamtypes.h |

---

## PS2SDK: ee/rpc/remote -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000370_000006.html>

###### remote → iop Relation
| File in ee/rpc/remote | Includes file in iop |
| src / librm.c | system / stdio / include / stdio.h |

---

## PS2SDK: ee/rpc/remote -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000370_000324.html>

###### remote → kernel Relation
| File in ee/rpc/remote | Includes file in ee/kernel |
| src / librm.c | include / kernel.h |
| src / librm.c | include / iopcontrol.h |

---

## PS2SDK: ee/rpc/remote -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000370_000402.html>

###### remote → erl Relation
| File in ee/rpc/remote | Includes file in ee/erl |
| src / erl-support.c | include / erl.h |

---

## PS2SDK: ee/rpc/remote/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000371_000000.html>

###### src → common Relation
| File in ee/rpc/remote/src | Includes file in common |
| librm.c | include / tamtypes.h |

---

## PS2SDK: ee/rpc/remote/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000371_000006.html>

###### src → iop Relation
| File in ee/rpc/remote/src | Includes file in iop |
| librm.c | system / stdio / include / stdio.h |

---

## PS2SDK: ee/rpc/remote/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000371_000324.html>

###### src → kernel Relation
| File in ee/rpc/remote/src | Includes file in ee/kernel |
| librm.c | include / iopcontrol.h |
| librm.c | include / kernel.h |

---

## PS2SDK: ee/rpc/remote/src -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000371_000402.html>

###### src → erl Relation
| File in ee/rpc/remote/src | Includes file in ee/erl |
| erl-support.c | include / erl.h |

---

## PS2SDK: ee/rpc/remote/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000371_000464.html>

###### src → include Relation
| File in ee/rpc/remote/src | Includes file in ee/rpc/remote/include |
| librm.c | librm.h |

---

## PS2SDK: ee/rpc/sdr -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000372_000000.html>

###### sdr → common Relation
| File in ee/rpc/sdr | Includes file in common |
| include / libsdr.h | include / libsd-common.h |
| include / libsdr.h | include / libsdr-common.h |

---

## PS2SDK: ee/rpc/sdr -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000372_000324.html>

###### sdr → kernel Relation
| File in ee/rpc/sdr | Includes file in ee/kernel |
| src / sdr_i.h | include / kernel.h |
| src / sdr_i.h | include / iopcontrol.h |

---

## PS2SDK: ee/rpc/sdr -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000372_000402.html>

###### sdr → erl Relation
| File in ee/rpc/sdr | Includes file in ee/erl |
| src / erl-support.c | include / erl.h |

---

## PS2SDK: ee/rpc/sdr/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000373_000324.html>

###### src → kernel Relation
| File in ee/rpc/sdr/src | Includes file in ee/kernel |
| sdr_i.h | include / iopcontrol.h |
| sdr_i.h | include / kernel.h |

---

## PS2SDK: ee/rpc/sdr/src -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000373_000402.html>

###### src → erl Relation
| File in ee/rpc/sdr/src | Includes file in ee/erl |
| erl-support.c | include / erl.h |

---

## PS2SDK: ee/rpc/sdr/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000373_000465.html>

###### src → include Relation
| File in ee/rpc/sdr/src | Includes file in ee/rpc/sdr/include |
| sdr_i.h | libsdr.h |

---

## PS2SDK: ee/rpc/secr -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000374_000000.html>

###### secr → common Relation
| File in ee/rpc/secr | Includes file in common |
| include / libsecr.h | include / libsecr-common.h |

---

## PS2SDK: ee/rpc/secr -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000374_000006.html>

###### secr → iop Relation
| File in ee/rpc/secr | Includes file in iop |
| src / libsecr.c | system / stdio / include / stdio.h |

---

## PS2SDK: ee/rpc/secr -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000374_000324.html>

###### secr → kernel Relation
| File in ee/rpc/secr | Includes file in ee/kernel |
| src / libsecr.c | include / kernel.h |
| src / libsecr.c | include / iopcontrol.h |

---

## PS2SDK: ee/rpc/secr -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000374_000402.html>

###### secr → erl Relation
| File in ee/rpc/secr | Includes file in ee/erl |
| src / erl-support.c | include / erl.h |

---

## PS2SDK: ee/rpc/secr/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000375_000006.html>

###### src → iop Relation
| File in ee/rpc/secr/src | Includes file in iop |
| libsecr.c | system / stdio / include / stdio.h |

---

## PS2SDK: ee/rpc/secr/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000375_000324.html>

###### src → kernel Relation
| File in ee/rpc/secr/src | Includes file in ee/kernel |
| libsecr.c | include / iopcontrol.h |
| libsecr.c | include / kernel.h |

---

## PS2SDK: ee/rpc/secr/src -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000375_000402.html>

###### src → erl Relation
| File in ee/rpc/secr/src | Includes file in ee/erl |
| erl-support.c | include / erl.h |

---

## PS2SDK: ee/rpc/sior -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000376_000000.html>

###### sior → common Relation
| File in ee/rpc/sior | Includes file in common |
| src / sior_rpc.c | include / tamtypes.h |

---

## PS2SDK: ee/rpc/sior -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000376_000006.html>

###### sior → iop Relation
| File in ee/rpc/sior | Includes file in iop |
| src / sior_rpc.c | tcpip / tcpip-base / include / stdlib.h |
| src / sior_rpc.c | system / stdio / include / stdio.h |

---

## PS2SDK: ee/rpc/sior -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000376_000324.html>

###### sior → kernel Relation
| File in ee/rpc/sior | Includes file in ee/kernel |
| src / sior_rpc.c | include / kernel.h |
| src / sior_rpc.c | include / sio.h |

---

## PS2SDK: ee/rpc/sior -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000376_000402.html>

###### sior → erl Relation
| File in ee/rpc/sior | Includes file in ee/erl |
| src / erl-support.c | include / erl.h |

---

## PS2SDK: ee/rpc/sior/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000377_000000.html>

###### src → common Relation
| File in ee/rpc/sior/src | Includes file in common |
| sior_rpc.c | include / tamtypes.h |

---

## PS2SDK: ee/rpc/sior/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000377_000006.html>

###### src → iop Relation
| File in ee/rpc/sior/src | Includes file in iop |
| sior_rpc.c | system / stdio / include / stdio.h |
| sior_rpc.c | tcpip / tcpip-base / include / stdlib.h |

---

## PS2SDK: ee/rpc/sior/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000377_000324.html>

###### src → kernel Relation
| File in ee/rpc/sior/src | Includes file in ee/kernel |
| sior_rpc.c | include / kernel.h |
| sior_rpc.c | include / sio.h |

---

## PS2SDK: ee/rpc/sior/src -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000377_000402.html>

###### src → erl Relation
| File in ee/rpc/sior/src | Includes file in ee/erl |
| erl-support.c | include / erl.h |

---

## PS2SDK: ee/rpc/sior/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000377_000467.html>

###### src → include Relation
| File in ee/rpc/sior/src | Includes file in ee/rpc/sior/include |
| sior_rpc.c | sior_rpc.h |

---

## PS2SDK: ee/rpc/tcpips -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000378_000000.html>

###### tcpips → common Relation
| File in ee/rpc/tcpips | Includes file in common |
| src / ps2ipc.c | include / ps2ip_rpc.h |
| src / ps2ipc.c | include / tamtypes.h |
| src / ps2ipc_ps2sdk.c | include / errno.h |

---

## PS2SDK: ee/rpc/tcpips -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000378_000324.html>

###### tcpips → kernel Relation
| File in ee/rpc/tcpips | Includes file in ee/kernel |
| src / ps2ipc.c | include / iopcontrol.h |
| src / ps2ipc.c | include / kernel.h |

---

## PS2SDK: ee/rpc/tcpips -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000378_000402.html>

###### tcpips → erl Relation
| File in ee/rpc/tcpips | Includes file in ee/erl |
| src / erl-support.c | include / erl.h |

---

## PS2SDK: ee/rpc/tcpips/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000379_000000.html>

###### src → common Relation
| File in ee/rpc/tcpips/src | Includes file in common |
| ps2ipc.c | include / ps2ip_rpc.h |
| ps2ipc.c | include / tamtypes.h |
| ps2ipc_ps2sdk.c | include / errno.h |

---

## PS2SDK: ee/rpc/tcpips/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000379_000324.html>

###### src → kernel Relation
| File in ee/rpc/tcpips/src | Includes file in ee/kernel |
| ps2ipc.c | include / iopcontrol.h |
| ps2ipc.c | include / kernel.h |

---

## PS2SDK: ee/rpc/tcpips/src -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000379_000402.html>

###### src → erl Relation
| File in ee/rpc/tcpips/src | Includes file in ee/erl |
| erl-support.c | include / erl.h |

---

## PS2SDK: ee/rpc/tcpips/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000379_000468.html>

###### src → include Relation
| File in ee/rpc/tcpips/src | Includes file in ee/rpc/tcpips/include |
| ps2ipc.c | ps2ips.h |
| ps2ipc.h | ps2ips.h |

---

## PS2SDK: ee/sbv -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000380_000000.html>

###### sbv → common Relation
| File in ee/sbv | Includes file in common |
| include / slib.h | include / tamtypes.h |
| include / smem.h | include / tamtypes.h |
| include / smod.h | include / tamtypes.h |
| src / patch_disable_prefix_check.c | include / tamtypes.h |
| src / patch_enable_lmb.c | include / tamtypes.h |
| src / patch_fileio.c | include / tamtypes.h |
| src / patch_romdrv_set_rom1_info.c | include / tamtypes.h |
| src / patch_user_mem_clear.c | include / tamtypes.h |
| src / slib.c | include / tamtypes.h |
| src / smod.c | include / tamtypes.h |

---

## PS2SDK: ee/sbv -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000380_000324.html>

###### sbv → kernel Relation
| File in ee/sbv | Includes file in ee/kernel |
| src / common.c | include / kernel.h |
| src / patch_disable_prefix_check.c | include / kernel.h |
| src / patch_enable_lmb.c | include / kernel.h |
| src / patch_enable_lmb.c | include / iopheap.h |
| src / patch_fileio.c | include / kernel.h |
| src / patch_fileio.c | include / iopheap.h |
| src / patch_romdrv_set_rom1_info.c | include / kernel.h |
| src / patch_romdrv_set_rom1_info.c | include / sifdma.h |
| src / patch_user_mem_clear.c | include / kernel.h |
| src / slib.c | include / kernel.h |
| src / smem.c | include / kernel.h |
| src / smod.c | include / kernel.h |

---

## PS2SDK: ee/sbv -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000380_000402.html>

###### sbv → erl Relation
| File in ee/sbv | Includes file in ee/erl |
| src / erl-support.c | include / erl.h |

---

## PS2SDK: ee/sbv/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000381_000000.html>

###### src → common Relation
| File in ee/sbv/src | Includes file in common |
| patch_disable_prefix_check.c | include / tamtypes.h |
| patch_enable_lmb.c | include / tamtypes.h |
| patch_fileio.c | include / tamtypes.h |
| patch_romdrv_set_rom1_info.c | include / tamtypes.h |
| patch_user_mem_clear.c | include / tamtypes.h |
| slib.c | include / tamtypes.h |
| smod.c | include / tamtypes.h |

---

## PS2SDK: ee/sbv/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000381_000324.html>

###### src → kernel Relation
| File in ee/sbv/src | Includes file in ee/kernel |
| common.c | include / kernel.h |
| patch_disable_prefix_check.c | include / kernel.h |
| patch_enable_lmb.c | include / iopheap.h |
| patch_enable_lmb.c | include / kernel.h |
| patch_fileio.c | include / iopheap.h |
| patch_fileio.c | include / kernel.h |
| patch_romdrv_set_rom1_info.c | include / kernel.h |
| patch_romdrv_set_rom1_info.c | include / sifdma.h |
| patch_user_mem_clear.c | include / kernel.h |
| slib.c | include / kernel.h |
| smem.c | include / kernel.h |
| smod.c | include / kernel.h |

---

## PS2SDK: ee/sbv/src -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000381_000402.html>

###### src → erl Relation
| File in ee/sbv/src | Includes file in ee/erl |
| erl-support.c | include / erl.h |

---

## PS2SDK: ee/sbv/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000381_000469.html>

###### src → include Relation
| File in ee/sbv/src | Includes file in ee/sbv/include |
| common.c | slib.h |
| common.c | smod.h |
| patch_disable_prefix_check.c | slib.h |
| patch_enable_lmb.c | slib.h |
| patch_enable_lmb.c | smem.h |
| patch_enable_lmb.c | smod.h |
| patch_fileio.c | slib.h |
| patch_fileio.c | smod.h |
| patch_romdrv_set_rom1_info.c | slib.h |
| patch_romdrv_set_rom1_info.c | smod.h |
| slib.c | slib.h |
| slib.c | smod.h |
| smem.c | smem.h |
| smod.c | slib.h |
| smod.c | smem.h |
| smod.c | smod.h |

---

## PS2SDK: ee/dma/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000382_000000.html>

###### include → common Relation
| File in ee/dma/include | Includes file in common |
| dma.h | include / tamtypes.h |
| dma_registers.h | include / tamtypes.h |
| dma_tags.h | include / tamtypes.h |

---

## PS2SDK: ee/draw/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000383_000000.html>

###### include → common Relation
| File in ee/draw/include | Includes file in common |
| draw.h | include / tamtypes.h |
| draw2d.h | include / tamtypes.h |
| draw3d.h | include / gif_tags.h |
| draw3d.h | include / tamtypes.h |
| draw_blending.h | include / tamtypes.h |
| draw_buffers.h | include / tamtypes.h |
| draw_dithering.h | include / tamtypes.h |
| draw_fog.h | include / tamtypes.h |
| draw_masking.h | include / tamtypes.h |
| draw_primitives.h | include / tamtypes.h |
| draw_sampling.h | include / tamtypes.h |
| draw_tests.h | include / tamtypes.h |

---

## PS2SDK: ee/draw/include -&gt; math3d Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000383_000330.html>

###### include → math3d Relation
| File in ee/draw/include | Includes file in ee/math3d |
| draw_types.h | include / math3d.h |

---

## PS2SDK: ee/eedebug/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000384_000000.html>

###### include → common Relation
| File in ee/eedebug/include | Includes file in common |
| ee_debug.h | include / ee_cop0_defs.h |
| ee_debug.h | include / ps2_debug.h |
| ee_debug.h | include / tamtypes.h |

---

## PS2SDK: ee/elf-loader -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000385_000000.html>

###### elf-loader → common Relation
| File in ee/elf-loader | Includes file in common |
| src / loader / src / loader.c | include / errno.h |
| src / elf.h | include / tamtypes.h |

---

## PS2SDK: ee/elf-loader -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000385_000006.html>

###### elf-loader → iop Relation
| File in ee/elf-loader | Includes file in iop |
| src / loader / src / loader.c | system / stdio / include / stdio.h |
| src / loader / src / loader.c | tcpip / tcpip-base / include / stdlib.h |
| src / elf.c | tcpip / tcpip-base / include / stdlib.h |

---

## PS2SDK: ee/elf-loader -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000385_000324.html>

###### elf-loader → kernel Relation
| File in ee/elf-loader | Includes file in ee/kernel |
| src / loader / src / loader.c | include / kernel.h |
| src / loader / src / loader.c | include / loadfile.h |
| src / loader / src / loader.c | include / iopcontrol.h |
| src / elf.c | include / kernel.h |

---

## PS2SDK: ee/elf-loader2 -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000387_000000.html>

###### elf-loader2 → common Relation
| File in ee/elf-loader2 | Includes file in common |
| src / include / elf_loader_common.h | include / tamtypes.h |
| src / ldrsrc / src / ldrsrc.c | include / tamtypes.h |

---

## PS2SDK: ee/elf-loader2 -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000387_000006.html>

###### elf-loader2 → iop Relation
| File in ee/elf-loader2 | Includes file in iop |
| src / elf_loader_compat.c | tcpip / tcpip-base / include / stdlib.h |
| src / elf_loader_stdio.c | system / stdio / include / stdio.h |
| src / elf_loader_stdio.c | tcpip / tcpip-base / include / stdlib.h |

---

## PS2SDK: ee/elf-loader2 -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000387_000324.html>

###### elf-loader2 → kernel Relation
| File in ee/elf-loader2 | Includes file in ee/kernel |
| src / ldrsrc / src / ldrsrc.c | include / kernel.h |
| src / elf.c | include / kernel.h |
| src / elf_loader_compat.c | include / iopcontrol.h |
| src / elf_loader_compat.c | include / loadfile.h |

---

## PS2SDK: ee/elf-loader/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000389_000000.html>

###### src → common Relation
| File in ee/elf-loader/src | Includes file in common |
| elf.h | include / tamtypes.h |
| loader / src / loader.c | include / errno.h |

---

## PS2SDK: ee/elf-loader/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000389_000006.html>

###### src → iop Relation
| File in ee/elf-loader/src | Includes file in iop |
| elf.c | tcpip / tcpip-base / include / stdlib.h |
| loader / src / loader.c | system / stdio / include / stdio.h |
| loader / src / loader.c | tcpip / tcpip-base / include / stdlib.h |

---

## PS2SDK: ee/elf-loader/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000389_000324.html>

###### src → kernel Relation
| File in ee/elf-loader/src | Includes file in ee/kernel |
| elf.c | include / kernel.h |
| loader / src / loader.c | include / iopcontrol.h |
| loader / src / loader.c | include / kernel.h |
| loader / src / loader.c | include / loadfile.h |

---

## PS2SDK: ee/elf-loader2/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000390_000000.html>

###### src → common Relation
| File in ee/elf-loader2/src | Includes file in common |
| include / elf_loader_common.h | include / tamtypes.h |
| ldrsrc / src / ldrsrc.c | include / tamtypes.h |

---

## PS2SDK: ee/elf-loader2/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000390_000006.html>

###### src → iop Relation
| File in ee/elf-loader2/src | Includes file in iop |
| elf_loader_compat.c | tcpip / tcpip-base / include / stdlib.h |
| elf_loader_stdio.c | system / stdio / include / stdio.h |
| elf_loader_stdio.c | tcpip / tcpip-base / include / stdlib.h |

---

## PS2SDK: ee/elf-loader2/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000390_000324.html>

###### src → kernel Relation
| File in ee/elf-loader2/src | Includes file in ee/kernel |
| elf.c | include / kernel.h |
| elf_loader_compat.c | include / iopcontrol.h |
| elf_loader_compat.c | include / loadfile.h |
| ldrsrc / src / ldrsrc.c | include / kernel.h |

---

## PS2SDK: tools/romimg -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000393_000000.html>

###### romimg → common Relation
| File in tools/romimg | Includes file in common |
| src / main.c | include / errno.h |
| src / platform.c | include / errno.h |
| src / romimg.c | include / errno.h |
| src / SonyRX.c | include / errno.h |

---

## PS2SDK: tools/romimg -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000393_000006.html>

###### romimg → iop Relation
| File in tools/romimg | Includes file in iop |
| src / dprintf.h | system / stdio / include / stdio.h |
| src / main.c | system / stdio / include / stdio.h |
| src / main.c | system / sysclib / include / ctype.h |
| src / platform.c | tcpip / tcpip-base / include / stdlib.h |
| src / platform.c | system / sysclib / include / ctype.h |
| src / platform.c | kernel / include / sys / time.h |
| src / romimg.c | system / stdio / include / stdio.h |
| src / romimg.c | tcpip / tcpip-base / include / stdlib.h |
| src / SonyRX.c | system / stdio / include / stdio.h |
| src / SonyRX.c | tcpip / tcpip-base / include / stdlib.h |

---

## PS2SDK: tools/romimg/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000394_000000.html>

###### src → common Relation
| File in tools/romimg/src | Includes file in common |
| main.c | include / errno.h |
| platform.c | include / errno.h |
| romimg.c | include / errno.h |
| SonyRX.c | include / errno.h |

---

## PS2SDK: tools/romimg/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000394_000006.html>

###### src → iop Relation
| File in tools/romimg/src | Includes file in iop |
| dprintf.h | system / stdio / include / stdio.h |
| main.c | system / sysclib / include / ctype.h |
| main.c | system / stdio / include / stdio.h |
| platform.c | system / sysclib / include / ctype.h |
| platform.c | tcpip / tcpip-base / include / stdlib.h |
| platform.c | kernel / include / sys / time.h |
| romimg.c | system / stdio / include / stdio.h |
| romimg.c | tcpip / tcpip-base / include / stdlib.h |
| SonyRX.c | system / stdio / include / stdio.h |
| SonyRX.c | tcpip / tcpip-base / include / stdlib.h |

---

## PS2SDK: ee/elf-loader/src/loader -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000395_000000.html>

###### loader → common Relation
| File in ee/elf-loader/src/loader | Includes file in common |
| src / loader.c | include / errno.h |

---

## PS2SDK: ee/elf-loader/src/loader -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000395_000006.html>

###### loader → iop Relation
| File in ee/elf-loader/src/loader | Includes file in iop |
| src / loader.c | system / stdio / include / stdio.h |
| src / loader.c | tcpip / tcpip-base / include / stdlib.h |

---

## PS2SDK: ee/elf-loader/src/loader -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000395_000324.html>

###### loader → kernel Relation
| File in ee/elf-loader/src/loader | Includes file in ee/kernel |
| src / loader.c | include / kernel.h |
| src / loader.c | include / loadfile.h |
| src / loader.c | include / iopcontrol.h |

---

## PS2SDK: ee/elf-loader/src/loader/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000396_000000.html>

###### src → common Relation
| File in ee/elf-loader/src/loader/src | Includes file in common |
| loader.c | include / errno.h |

---

## PS2SDK: ee/elf-loader/src/loader/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000396_000006.html>

###### src → iop Relation
| File in ee/elf-loader/src/loader/src | Includes file in iop |
| loader.c | system / stdio / include / stdio.h |
| loader.c | tcpip / tcpip-base / include / stdlib.h |

---

## PS2SDK: ee/elf-loader/src/loader/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000396_000324.html>

###### src → kernel Relation
| File in ee/elf-loader/src/loader/src | Includes file in ee/kernel |
| loader.c | include / iopcontrol.h |
| loader.c | include / kernel.h |
| loader.c | include / loadfile.h |

---

## PS2SDK: ee/elf-loader2/src/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000397_000000.html>

###### include → common Relation
| File in ee/elf-loader2/src/include | Includes file in common |
| elf_loader_common.h | include / tamtypes.h |

---

## PS2SDK: ee/elf-loader2/src/ldrsrc -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000398_000000.html>

###### ldrsrc → common Relation
| File in ee/elf-loader2/src/ldrsrc | Includes file in common |
| src / ldrsrc.c | include / tamtypes.h |

---

## PS2SDK: ee/elf-loader2/src/ldrsrc -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000398_000324.html>

###### ldrsrc → kernel Relation
| File in ee/elf-loader2/src/ldrsrc | Includes file in ee/kernel |
| src / ldrsrc.c | include / kernel.h |

---

## PS2SDK: ee/elf-loader2/src/ldrsrc/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000399_000000.html>

###### src → common Relation
| File in ee/elf-loader2/src/ldrsrc/src | Includes file in common |
| ldrsrc.c | include / tamtypes.h |

---

## PS2SDK: ee/elf-loader2/src/ldrsrc/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000399_000324.html>

###### src → kernel Relation
| File in ee/elf-loader2/src/ldrsrc/src | Includes file in ee/kernel |
| ldrsrc.c | include / kernel.h |

---

## PS2SDK: ee/erl-loader -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000400_000402.html>

###### erl-loader → erl Relation
| File in ee/erl-loader | Includes file in ee/erl |
| src / erl-loader.c | include / erl.h |

---

## PS2SDK: ee/erl-loader/src -&gt; erl Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000401_000402.html>

###### src → erl Relation
| File in ee/erl-loader/src | Includes file in ee/erl |
| erl-loader.c | include / erl.h |

---

## PS2SDK: ee/erl -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000402_000000.html>

###### erl → common Relation
| File in ee/erl | Includes file in common |
| include / erl.h | include / tamtypes.h |

---

## PS2SDK: ee/erl -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000402_000006.html>

###### erl → iop Relation
| File in ee/erl | Includes file in iop |
| src / erl.c | tcpip / tcpip-base / include / stdlib.h |
| src / erl.c | system / stdio / include / stdio.h |
| src / hashtab.c | tcpip / tcpip-base / include / stdlib.h |
| src / recycle.c | tcpip / tcpip-base / include / stdlib.h |

---

## PS2SDK: ee/erl/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000403_000000.html>

###### include → common Relation
| File in ee/erl/include | Includes file in common |
| erl.h | include / tamtypes.h |

---

## PS2SDK: ee/erl/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000404_000006.html>

###### src → iop Relation
| File in ee/erl/src | Includes file in iop |
| erl.c | system / stdio / include / stdio.h |
| erl.c | tcpip / tcpip-base / include / stdlib.h |
| hashtab.c | tcpip / tcpip-base / include / stdlib.h |
| recycle.c | tcpip / tcpip-base / include / stdlib.h |

---

## PS2SDK: ee/erl/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000404_000403.html>

###### src → include Relation
| File in ee/erl/src | Includes file in ee/erl/include |
| erl.c | erl.h |

---

## PS2SDK: ee/font/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000405_000000.html>

###### include → common Relation
| File in ee/font/include | Includes file in common |
| font.h | include / tamtypes.h |

---

## PS2SDK: ee/font/include -&gt; draw Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000405_000312.html>

###### include → draw Relation
| File in ee/font/include | Includes file in ee/draw |
| font.h | include / draw.h |

---

## PS2SDK: ee/input/include -&gt; rpc Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000407_000343.html>

###### include → rpc Relation
| File in ee/input/include | Includes file in ee/rpc |
| input.h | pad / include / libpad.h |

---

## PS2SDK: ee/ioprpgen -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000409_000000.html>

###### ioprpgen → common Relation
| File in ee/ioprpgen | Includes file in common |
| include / ioprpgen.h | include / tamtypes.h |

---

## PS2SDK: ee/ioprpgen/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000410_000000.html>

###### include → common Relation
| File in ee/ioprpgen/include | Includes file in common |
| ioprpgen.h | include / tamtypes.h |

---

## PS2SDK: ee/ioprpgen/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000411_000410.html>

###### src → include Relation
| File in ee/ioprpgen/src | Includes file in ee/ioprpgen/include |
| ioprpgen.c | ioprpgen.h |

---

## PS2SDK: ee/kernel/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000412_000000.html>

###### include → common Relation
| File in ee/kernel/include | Includes file in common |
| delaythread.h | include / tamtypes.h |
| fileio.h | include / io_common.h |
| kernel.h | include / mipscopaccess.h |
| kernel_util.h | include / tamtypes.h |
| loadfile.h | include / loadfile-common.h |
| loadfile.h | include / tamtypes.h |
| osd_config.h | include / tamtypes.h |
| sifcmd.h | include / sifcmd-common.h |
| sifdma.h | include / tamtypes.h |
| sifrpc.h | include / sifrpc-common.h |
| sio.h | include / tamtypes.h |
| timer.h | include / tamtypes.h |
| timer_alarm.h | include / tamtypes.h |

---

## PS2SDK: ee/kernel/include -&gt; rpc Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000412_000343.html>

###### include → rpc Relation
| File in ee/kernel/include | Includes file in ee/rpc |
| osd_config.h | cdvd / include / libcdvd.h |

---

## PS2SDK: iop/system/sifcmd/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000413_000000.html>

###### include → common Relation
| File in iop/system/sifcmd/include | Includes file in common |
| sifcmd.h | include / sifcmd-common.h |
| sifcmd.h | include / sifrpc-common.h |

---

## PS2SDK: iop/system/sifcmd/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000413_000537.html>

###### include → kernel Relation
| File in iop/system/sifcmd/include | Includes file in iop/kernel |
| sifcmd.h | include / irx.h |

---

## PS2SDK: ee/kernel/src/srcfile -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000414_000000.html>

###### srcfile → common Relation
| File in ee/kernel/src/srcfile | Includes file in common |
| src / alarm.c | include / ee_regs.h |
| src / alarm.c | include / tamtypes.h |

---

## PS2SDK: ee/kernel/src/srcfile -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000414_000412.html>

###### srcfile → include Relation
| File in ee/kernel/src/srcfile | Includes file in ee/kernel/include |
| src / alarm.c | kernel.h |
| src / alarm.c | timer.h |
| src / srcfile.c | kernel.h |

---

## PS2SDK: ee/kernel/src/srcfile/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000415_000000.html>

###### src → common Relation
| File in ee/kernel/src/srcfile/src | Includes file in common |
| alarm.c | include / ee_regs.h |
| alarm.c | include / tamtypes.h |

---

## PS2SDK: ee/kernel/src/srcfile/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000415_000412.html>

###### src → include Relation
| File in ee/kernel/src/srcfile/src | Includes file in ee/kernel/include |
| alarm.c | kernel.h |
| alarm.c | timer.h |
| srcfile.c | kernel.h |

---

## PS2SDK: ee/libcglue -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000416_000000.html>

###### libcglue → common Relation
| File in ee/libcglue | Includes file in common |
| include / arpa / inet.h | include / tcpip.h |
| include / netdb.h | include / tcpip.h |
| include / ps2sdkapi.h | include / errno.h |
| include / netinet / in.h | include / tcpip.h |
| include / netinet / tcp.h | include / tcpip.h |
| src / cwd.c | include / errno.h |
| src / fdman.c | include / errno.h |
| src / glue.c | include / errno.h |
| src / glue.c | include / tamtypes.h |
| src / glue.c | include / io_common.h |
| src / ps2sdkapi.c | include / errno.h |
| src / ps2sdkapi.c | include / fileio-common.h |
| src / ps2sdkapi.c | include / iox_stat.h |
| src / select.c | include / errno.h |
| src / sleep.c | include / errno.h |
| src / socket.c | include / errno.h |
| include / sys / socket.h | include / tcpip.h |

---

## PS2SDK: ee/libcglue -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000416_000006.html>

###### libcglue → iop Relation
| File in ee/libcglue | Includes file in iop |
| src / cwd.c | system / stdio / include / stdio.h |
| src / cwd.c | system / sysclib / include / ctype.h |
| src / cwd.c | tcpip / tcpip-base / include / stdlib.h |
| src / fdman.c | tcpip / tcpip-base / include / stdlib.h |
| src / glue.c | system / stdio / include / stdio.h |
| src / glue.c | tcpip / tcpip-base / include / stdlib.h |
| src / glue.c | kernel / include / sys / time.h |
| src / lock.c | system / stdio / include / stdio.h |
| src / lock.c | tcpip / tcpip-base / include / stdlib.h |
| src / ps2sdkapi.c | system / stdio / include / stdio.h |
| src / ps2sdkapi.c | tcpip / tcpip-base / include / stdlib.h |
| src / rtc.c | kernel / include / sys / time.h |
| src / rtc.c | system / stdio / include / stdio.h |
| src / rtc.c | tcpip / tcpip-base / include / stdlib.h |
| src / sleep.c | kernel / include / sys / time.h |
| src / timezone.c | kernel / include / sys / time.h |
| src / timezone.c | system / stdio / include / stdio.h |
| src / timezone.c | tcpip / tcpip-base / include / stdlib.h |
| include / sys / utime.h | kernel / include / sys / time.h |

---

## PS2SDK: ee/libcglue -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000416_000324.html>

###### libcglue → kernel Relation
| File in ee/libcglue | Includes file in ee/kernel |
| include / ps2sdkapi.h | include / timer.h |
| src / fdman.c | include / kernel.h |
| src / glue.c | include / kernel.h |
| src / glue.c | include / timer.h |
| src / glue.c | include / sio.h |
| src / lock.c | include / kernel.h |
| src / ps2sdkapi.c | include / fileio.h |
| src / rtc.c | include / osd_config.h |
| src / sleep.c | include / kernel.h |
| src / timezone.c | include / osd_config.h |

---

## PS2SDK: ee/libcglue/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000417_000000.html>

###### src → common Relation
| File in ee/libcglue/src | Includes file in common |
| cwd.c | include / errno.h |
| fdman.c | include / errno.h |
| glue.c | include / errno.h |
| glue.c | include / io_common.h |
| glue.c | include / tamtypes.h |
| ps2sdkapi.c | include / errno.h |
| ps2sdkapi.c | include / fileio-common.h |
| ps2sdkapi.c | include / iox_stat.h |
| select.c | include / errno.h |
| sleep.c | include / errno.h |
| socket.c | include / errno.h |

---

## PS2SDK: ee/libcglue/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000417_000006.html>

###### src → iop Relation
| File in ee/libcglue/src | Includes file in iop |
| cwd.c | system / sysclib / include / ctype.h |
| cwd.c | system / stdio / include / stdio.h |
| cwd.c | tcpip / tcpip-base / include / stdlib.h |
| fdman.c | tcpip / tcpip-base / include / stdlib.h |
| glue.c | system / stdio / include / stdio.h |
| glue.c | tcpip / tcpip-base / include / stdlib.h |
| glue.c | kernel / include / sys / time.h |
| lock.c | system / stdio / include / stdio.h |
| lock.c | tcpip / tcpip-base / include / stdlib.h |
| ps2sdkapi.c | system / stdio / include / stdio.h |
| ps2sdkapi.c | tcpip / tcpip-base / include / stdlib.h |
| rtc.c | system / stdio / include / stdio.h |
| rtc.c | tcpip / tcpip-base / include / stdlib.h |
| rtc.c | kernel / include / sys / time.h |
| sleep.c | kernel / include / sys / time.h |
| timezone.c | system / stdio / include / stdio.h |
| timezone.c | tcpip / tcpip-base / include / stdlib.h |
| timezone.c | kernel / include / sys / time.h |

---

## PS2SDK: ee/libcglue/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000417_000324.html>

###### src → kernel Relation
| File in ee/libcglue/src | Includes file in ee/kernel |
| fdman.c | include / kernel.h |
| glue.c | include / kernel.h |
| glue.c | include / sio.h |
| glue.c | include / timer.h |
| lock.c | include / kernel.h |
| ps2sdkapi.c | include / fileio.h |
| rtc.c | include / osd_config.h |
| sleep.c | include / kernel.h |
| timezone.c | include / osd_config.h |

---

## PS2SDK: ee/libcglue/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000417_000424.html>

###### src → include Relation
| File in ee/libcglue/src | Includes file in ee/libcglue/include |
| glue.c | sys / termios.h |
| sjis.c | sjis.h |

---

## PS2SDK: ee/kernel/src/osdsrc -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000418_000000.html>

###### osdsrc → common Relation
| File in ee/kernel/src/osdsrc | Includes file in common |
| src / osd.c | include / tamtypes.h |

---

## PS2SDK: ee/kernel/src/osdsrc -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000418_000412.html>

###### osdsrc → include Relation
| File in ee/kernel/src/osdsrc | Includes file in ee/kernel/include |
| src / ExecPS2.c | kernel.h |
| src / osd.c | osd_config.h |
| src / osdsrc.c | syscallnr.h |
| src / osdsrc.c | osd_config.h |

---

## PS2SDK: ee/kernel/src/osdsrc/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000419_000000.html>

###### src → common Relation
| File in ee/kernel/src/osdsrc/src | Includes file in common |
| osd.c | include / tamtypes.h |

---

## PS2SDK: ee/kernel/src/osdsrc/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000419_000412.html>

###### src → include Relation
| File in ee/kernel/src/osdsrc/src | Includes file in ee/kernel/include |
| ExecPS2.c | kernel.h |
| osd.c | osd_config.h |
| osdsrc.c | osd_config.h |
| osdsrc.c | syscallnr.h |

---

## PS2SDK: ee/kernel/src/tlbsrc -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000422_000000.html>

###### tlbsrc → common Relation
| File in ee/kernel/src/tlbsrc | Includes file in common |
| src / tlbsrc.c | include / ee_cop0_defs.h |
| src / tlbsrc.c | include / mipscopaccess.h |

---

## PS2SDK: ee/kernel/src/tlbsrc -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000422_000412.html>

###### tlbsrc → include Relation
| File in ee/kernel/src/tlbsrc | Includes file in ee/kernel/include |
| src / tlbsrc.c | kernel.h |

---

## PS2SDK: ee/kernel/src/tlbsrc/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000423_000000.html>

###### src → common Relation
| File in ee/kernel/src/tlbsrc/src | Includes file in common |
| tlbsrc.c | include / ee_cop0_defs.h |
| tlbsrc.c | include / mipscopaccess.h |

---

## PS2SDK: ee/kernel/src/tlbsrc/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000423_000412.html>

###### src → include Relation
| File in ee/kernel/src/tlbsrc/src | Includes file in ee/kernel/include |
| tlbsrc.c | kernel.h |

---

## PS2SDK: ee/libcglue/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000424_000000.html>

###### include → common Relation
| File in ee/libcglue/include | Includes file in common |
| arpa / inet.h | include / tcpip.h |
| netdb.h | include / tcpip.h |
| ps2sdkapi.h | include / errno.h |
| netinet / in.h | include / tcpip.h |
| netinet / tcp.h | include / tcpip.h |
| sys / socket.h | include / tcpip.h |

---

## PS2SDK: ee/libcglue/include -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000424_000006.html>

###### include → iop Relation
| File in ee/libcglue/include | Includes file in iop |
| sys / utime.h | kernel / include / sys / time.h |

---

## PS2SDK: ee/libcglue/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000424_000324.html>

###### include → kernel Relation
| File in ee/libcglue/include | Includes file in ee/kernel |
| ps2sdkapi.h | include / timer.h |

---

## PS2SDK: ee/libcglue/include/arpa -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000425_000000.html>

###### arpa → common Relation
| File in ee/libcglue/include/arpa | Includes file in common |
| inet.h | include / tcpip.h |

---

## PS2SDK: ee/libcglue/include/netinet -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000426_000000.html>

###### netinet → common Relation
| File in ee/libcglue/include/netinet | Includes file in common |
| in.h | include / tcpip.h |
| tcp.h | include / tcpip.h |

---

## PS2SDK: ee/libcglue/include/sys -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000427_000000.html>

###### sys → common Relation
| File in ee/libcglue/include/sys | Includes file in common |
| socket.h | include / tcpip.h |

---

## PS2SDK: ee/libcglue/include/sys -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000427_000006.html>

###### sys → iop Relation
| File in ee/libcglue/include/sys | Includes file in iop |
| utime.h | kernel / include / sys / time.h |

---

## PS2SDK: ee/libgs/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000428_000000.html>

###### include → common Relation
| File in ee/libgs/include | Includes file in common |
| libgs.h | include / tamtypes.h |

---

## PS2SDK: ee/libprofglue -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000429_000006.html>

###### libprofglue → iop Relation
| File in ee/libprofglue | Includes file in iop |
| src / prof.c | tcpip / tcpip-base / include / stdlib.h |
| src / prof.c | system / stdio / include / stdio.h |

---

## PS2SDK: ee/libprofglue -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000429_000324.html>

###### libprofglue → kernel Relation
| File in ee/libprofglue | Includes file in ee/kernel |
| src / prof.c | include / kernel.h |

---

## PS2SDK: ee/libprofglue/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000431_000006.html>

###### src → iop Relation
| File in ee/libprofglue/src | Includes file in iop |
| prof.c | system / stdio / include / stdio.h |
| prof.c | tcpip / tcpip-base / include / stdlib.h |

---

## PS2SDK: ee/libprofglue/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000431_000324.html>

###### src → kernel Relation
| File in ee/libprofglue/src | Includes file in ee/kernel |
| prof.c | include / kernel.h |

---

## PS2SDK: ee/libpthreadglue -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000432_000006.html>

###### libpthreadglue → iop Relation
| File in ee/libpthreadglue | Includes file in iop |
| src / include / ps2_osal.h | system / stdio / include / stdio.h |
| src / include / ps2_osal.h | tcpip / tcpip-base / include / stdlib.h |
| src / osal.c | kernel / include / sys / time.h |

---

## PS2SDK: ee/libpthreadglue -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000432_000324.html>

###### libpthreadglue → kernel Relation
| File in ee/libpthreadglue | Includes file in ee/kernel |
| src / include / ps2_osal.h | include / kernel.h |
| src / include / ps2_osal.h | include / kernel_util.h |
| src / osal.c | include / kernel_util.h |

---

## PS2SDK: ee/libpthreadglue/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000433_000006.html>

###### src → iop Relation
| File in ee/libpthreadglue/src | Includes file in iop |
| osal.c | kernel / include / sys / time.h |
| include / ps2_osal.h | system / stdio / include / stdio.h |
| include / ps2_osal.h | tcpip / tcpip-base / include / stdlib.h |

---

## PS2SDK: ee/libpthreadglue/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000433_000324.html>

###### src → kernel Relation
| File in ee/libpthreadglue/src | Includes file in ee/kernel |
| osal.c | include / kernel_util.h |
| include / ps2_osal.h | include / kernel.h |
| include / ps2_osal.h | include / kernel_util.h |

---

## PS2SDK: ee/libpthreadglue/src/include -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000434_000006.html>

###### include → iop Relation
| File in ee/libpthreadglue/src/include | Includes file in iop |
| ps2_osal.h | system / stdio / include / stdio.h |
| ps2_osal.h | tcpip / tcpip-base / include / stdlib.h |

---

## PS2SDK: ee/libpthreadglue/src/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000434_000324.html>

###### include → kernel Relation
| File in ee/libpthreadglue/src/include | Includes file in ee/kernel |
| ps2_osal.h | include / kernel.h |
| ps2_osal.h | include / kernel_util.h |

---

## PS2SDK: ee/math3d/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000436_000000.html>

###### include → common Relation
| File in ee/math3d/include | Includes file in common |
| math3d.h | include / tamtypes.h |

---

## PS2SDK: ee/mpeg/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000437_000000.html>

###### include → common Relation
| File in ee/mpeg/include | Includes file in common |
| libmpeg.h | include / tamtypes.h |

---

## PS2SDK: ee/network/tcpip/include -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000438_000006.html>

###### include → iop Relation
| File in ee/network/tcpip/include | Includes file in iop |
| ps2ip.h | kernel / include / sys / time.h |

---

## PS2SDK: iop/tcpip/tcpip/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000439_000000.html>

###### include → common Relation
| File in iop/tcpip/tcpip/include | Includes file in common |
| ps2ip.h | include / tcpip.h |

---

## PS2SDK: iop/tcpip/tcpip/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000439_000537.html>

###### include → kernel Relation
| File in iop/tcpip/tcpip/include | Includes file in iop/kernel |
| ps2ip.h | include / irx.h |
| ps2ip.h | include / sys / time.h |

---

## PS2SDK: ee/network/tcpip/src/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000440_000000.html>

###### include → common Relation
| File in ee/network/tcpip/src/include | Includes file in common |
| arch / cc.h | include / errno.h |

---

## PS2SDK: ee/network/tcpip/src/include -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000440_000006.html>

###### include → iop Relation
| File in ee/network/tcpip/src/include | Includes file in iop |
| arch / cc.h | tcpip / tcpip-base / include / stdlib.h |
| arch / cc.h | kernel / include / sys / time.h |

---

## PS2SDK: ee/network/tcpip/src/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000440_000324.html>

###### include → kernel Relation
| File in ee/network/tcpip/src/include | Includes file in ee/kernel |
| arch / sys_arch.h | include / kernel.h |

---

## PS2SDK: ee/network/tcpip/src/include/arch -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000441_000000.html>

###### arch → common Relation
| File in ee/network/tcpip/src/include/arch | Includes file in common |
| cc.h | include / errno.h |

---

## PS2SDK: ee/network/tcpip/src/include/arch -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000441_000006.html>

###### arch → iop Relation
| File in ee/network/tcpip/src/include/arch | Includes file in iop |
| cc.h | tcpip / tcpip-base / include / stdlib.h |
| cc.h | kernel / include / sys / time.h |

---

## PS2SDK: ee/network/tcpip/src/include/arch -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000441_000324.html>

###### arch → kernel Relation
| File in ee/network/tcpip/src/include/arch | Includes file in ee/kernel |
| sys_arch.h | include / kernel.h |

---

## PS2SDK: iop/tcpip/tcpip-base -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000442_000000.html>

###### tcpip-base → common Relation
| File in iop/tcpip/tcpip-base | Includes file in common |
| include / arch / cc.h | include / errno.h |

---

## PS2SDK: iop/tcpip/tcpip-base -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000442_000223.html>

###### tcpip-base → system Relation
| File in iop/tcpip/tcpip-base | Includes file in iop/system |
| sys_arch.c | intrman / include / intrman.h |
| sys_arch.c | stdio / include / stdio.h |
| sys_arch.c | sysclib / include / sysclib.h |
| sys_arch.c | threadman / include / thbase.h |
| sys_arch.c | threadman / include / thmsgbx.h |
| sys_arch.c | threadman / include / thsemap.h |

---

## PS2SDK: iop/tcpip/tcpip-base -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000442_000537.html>

###### tcpip-base → kernel Relation
| File in iop/tcpip/tcpip-base | Includes file in iop/kernel |
| include / arch / cc.h | include / sys / time.h |

---

## PS2SDK: iop/tcpip/tcpip-base/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000443_000000.html>

###### include → common Relation
| File in iop/tcpip/tcpip-base/include | Includes file in common |
| arch / cc.h | include / errno.h |

---

## PS2SDK: iop/tcpip/tcpip-base/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000443_000537.html>

###### include → kernel Relation
| File in iop/tcpip/tcpip-base/include | Includes file in iop/kernel |
| arch / cc.h | include / sys / time.h |

---

## PS2SDK: iop/tcpip/tcpip-base/include/arch -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000444_000000.html>

###### arch → common Relation
| File in iop/tcpip/tcpip-base/include/arch | Includes file in common |
| cc.h | include / errno.h |

---

## PS2SDK: iop/tcpip/tcpip-base/include/arch -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000444_000537.html>

###### arch → kernel Relation
| File in iop/tcpip/tcpip-base/include/arch | Includes file in iop/kernel |
| cc.h | include / sys / time.h |

---

## PS2SDK: ee/packet/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000445_000000.html>

###### include → common Relation
| File in ee/packet/include | Includes file in common |
| packet.h | include / tamtypes.h |

---

## PS2SDK: ee/packet2/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000446_000000.html>

###### include → common Relation
| File in ee/packet2/include | Includes file in common |
| packet2_types.h | include / tamtypes.h |
| packet2_utils.h | include / gs_gp.h |
| packet2_utils.h | include / tamtypes.h |

---

## PS2SDK: ee/packet2/include -&gt; draw Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000446_000312.html>

###### include → draw Relation
| File in ee/packet2/include | Includes file in ee/draw |
| packet2_utils.h | include / draw3d.h |
| packet2_utils.h | include / draw_buffers.h |
| packet2_utils.h | include / draw_sampling.h |

---

## PS2SDK: iop/sound/audsrv/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000449_000537.html>

###### include → kernel Relation
| File in iop/sound/audsrv/include | Includes file in iop/kernel |
| audsrv.h | include / irx.h |

---

## PS2SDK: ee/rpc/cdvd/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000451_000000.html>

###### include → common Relation
| File in ee/rpc/cdvd/include | Includes file in common |
| libcdvd.h | include / libcdvd-common.h |

---

## PS2SDK: ee/rpc/filexio/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000452_000000.html>

###### include → common Relation
| File in ee/rpc/filexio/include | Includes file in common |
| fileXio_rpc.h | include / fileXio.h |

---

## PS2SDK: ee/rpc/hdd/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000453_000000.html>

###### include → common Relation
| File in ee/rpc/hdd/include | Includes file in common |
| libhdd.h | include / hdd-ioctl.h |
| libhdd.h | include / tamtypes.h |

---

## PS2SDK: ee/rpc/hdd/include -&gt; poweroff Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000453_000366.html>

###### include → poweroff Relation
| File in ee/rpc/hdd/include | Includes file in ee/rpc/poweroff |
| libhdd.h | include / libpwroff.h |

---

## PS2SDK: ee/rpc/keyboard/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000454_000000.html>

###### include → common Relation
| File in ee/rpc/keyboard/include | Includes file in common |
| ps2kbd.h | include / tamtypes.h |

---

## PS2SDK: ee/rpc/memorycard/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000456_000000.html>

###### include → common Relation
| File in ee/rpc/memorycard/include | Includes file in common |
| libmc.h | include / libmc-common.h |

---

## PS2SDK: ee/rpc/mouse/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000457_000000.html>

###### include → common Relation
| File in ee/rpc/mouse/include | Includes file in common |
| ps2mouse.h | include / tamtypes.h |

---

## PS2SDK: ee/rpc/ps2snd/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000462_000000.html>

###### include → common Relation
| File in ee/rpc/ps2snd/include | Includes file in common |
| libsd.h | include / libsd-common.h |

---

## PS2SDK: iop/sound/libsd/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000463_000000.html>

###### include → common Relation
| File in iop/sound/libsd/include | Includes file in common |
| libsd.h | include / libsd-common.h |

---

## PS2SDK: iop/sound/libsd/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000463_000537.html>

###### include → kernel Relation
| File in iop/sound/libsd/include | Includes file in iop/kernel |
| libsd.h | include / irx.h |

---

## PS2SDK: ee/rpc/remote/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000464_000000.html>

###### include → common Relation
| File in ee/rpc/remote/include | Includes file in common |
| librm.h | include / librm-common.h |

---

## PS2SDK: ee/rpc/sdr/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000465_000000.html>

###### include → common Relation
| File in ee/rpc/sdr/include | Includes file in common |
| libsdr.h | include / libsd-common.h |
| libsdr.h | include / libsdr-common.h |

---

## PS2SDK: ee/rpc/secr/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000466_000000.html>

###### include → common Relation
| File in ee/rpc/secr/include | Includes file in common |
| libsecr.h | include / libsecr-common.h |

---

## PS2SDK: ee/sbv/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000469_000000.html>

###### include → common Relation
| File in ee/sbv/include | Includes file in common |
| slib.h | include / tamtypes.h |
| smem.h | include / tamtypes.h |
| smod.h | include / tamtypes.h |

---

## PS2SDK: ee/startup -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000470_000006.html>

###### startup → iop Relation
| File in ee/startup | Includes file in iop |
| src / crt0.c | system / stdio / include / stdio.h |

---

## PS2SDK: ee/startup -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000470_000324.html>

###### startup → kernel Relation
| File in ee/startup | Includes file in ee/kernel |
| src / crt0.c | include / kernel.h |

---

## PS2SDK: ee/startup/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000472_000006.html>

###### src → iop Relation
| File in ee/startup/src | Includes file in iop |
| crt0.c | system / stdio / include / stdio.h |

---

## PS2SDK: ee/startup/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000472_000324.html>

###### src → kernel Relation
| File in ee/startup/src | Includes file in ee/kernel |
| crt0.c | include / kernel.h |

---

## PS2SDK: ee/startup/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000472_000471.html>

###### src → include Relation
| File in ee/startup/src | Includes file in ee/startup/include |
| crt0.c | startup.h |

---

## PS2SDK: iop/startup -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000473_000223.html>

###### startup → system Relation
| File in iop/startup | Includes file in iop/system |
| src / crt0.c | stdio / include / stdio.h |

---

## PS2SDK: iop/startup/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000474_000223.html>

###### src → system Relation
| File in iop/startup/src | Includes file in iop/system |
| crt0.c | stdio / include / stdio.h |

---

## PS2SDK: iop/arcade/accdvd/include -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000476_000056.html>

###### include → cdvd Relation
| File in iop/arcade/accdvd/include | Includes file in iop/cdvd |
| accdvd.h | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/arcade/accore/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000477_000000.html>

###### include → common Relation
| File in iop/arcade/accore/include | Includes file in common |
| accore.h | include / tamtypes.h |

---

## PS2SDK: iop/arcade/accore/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000477_000537.html>

###### include → kernel Relation
| File in iop/arcade/accore/include | Includes file in iop/kernel |
| accore.h | include / irx.h |

---

## PS2SDK: iop/arcade/acdev/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000478_000000.html>

###### include → common Relation
| File in iop/arcade/acdev/include | Includes file in common |
| acdev.h | include / tamtypes.h |

---

## PS2SDK: iop/arcade/acdev/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000478_000537.html>

###### include → kernel Relation
| File in iop/arcade/acdev/include | Includes file in iop/kernel |
| acdev.h | include / irx.h |

---

## PS2SDK: iop/arcade/s147mdev/include -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000487_000223.html>

###### include → system Relation
| File in iop/arcade/s147mdev/include | Includes file in iop/system |
| s147mdev.h | ioman / include / ioman.h |

---

## PS2SDK: iop/arcade/s147nand/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000488_000000.html>

###### include → common Relation
| File in iop/arcade/s147nand/include | Includes file in common |
| s147nand.h | include / tamtypes.h |

---

## PS2SDK: tools/adpenc -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000489_000000.html>

###### adpenc → common Relation
| File in tools/adpenc | Includes file in common |
| src / adpcm.c | include / errno.h |
| src / main.c | include / errno.h |

---

## PS2SDK: tools/adpenc -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000489_000006.html>

###### adpenc → iop Relation
| File in tools/adpenc | Includes file in iop |
| src / adpcm.c | system / stdio / include / stdio.h |
| src / adpcm.c | system / sysclib / include / ctype.h |
| src / main.c | system / stdio / include / stdio.h |
| src / main.c | system / sysclib / include / ctype.h |

---

## PS2SDK: tools/adpenc/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000490_000000.html>

###### src → common Relation
| File in tools/adpenc/src | Includes file in common |
| adpcm.c | include / errno.h |
| main.c | include / errno.h |

---

## PS2SDK: tools/adpenc/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000490_000006.html>

###### src → iop Relation
| File in tools/adpenc/src | Includes file in iop |
| adpcm.c | system / sysclib / include / ctype.h |
| adpcm.c | system / stdio / include / stdio.h |
| main.c | system / sysclib / include / ctype.h |
| main.c | system / stdio / include / stdio.h |

---

## PS2SDK: tools/gensymtab -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000491_000000.html>

###### gensymtab → common Relation
| File in tools/gensymtab | Includes file in common |
| src / main.c | include / errno.h |

---

## PS2SDK: tools/gensymtab -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000491_000006.html>

###### gensymtab → iop Relation
| File in tools/gensymtab | Includes file in iop |
| src / main.c | system / stdio / include / stdio.h |
| src / main.c | tcpip / tcpip-base / include / stdlib.h |

---

## PS2SDK: tools/gensymtab/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000492_000000.html>

###### src → common Relation
| File in tools/gensymtab/src | Includes file in common |
| main.c | include / errno.h |

---

## PS2SDK: tools/gensymtab/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000492_000006.html>

###### src → iop Relation
| File in tools/gensymtab/src | Includes file in iop |
| main.c | system / stdio / include / stdio.h |
| main.c | tcpip / tcpip-base / include / stdlib.h |

---

## PS2SDK: tools/ps2adpcm -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000493_000000.html>

###### ps2adpcm → common Relation
| File in tools/ps2adpcm | Includes file in common |
| src / main.c | include / errno.h |

---

## PS2SDK: tools/ps2adpcm -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000493_000006.html>

###### ps2adpcm → iop Relation
| File in tools/ps2adpcm | Includes file in iop |
| src / adpcm.c | tcpip / tcpip-base / include / stdlib.h |
| src / adpcm.c | system / stdio / include / stdio.h |
| src / main.c | system / stdio / include / stdio.h |
| src / main.c | tcpip / tcpip-base / include / stdlib.h |

---

## PS2SDK: tools/ps2adpcm/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000494_000000.html>

###### src → common Relation
| File in tools/ps2adpcm/src | Includes file in common |
| main.c | include / errno.h |

---

## PS2SDK: tools/ps2adpcm/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000494_000006.html>

###### src → iop Relation
| File in tools/ps2adpcm/src | Includes file in iop |
| adpcm.c | system / stdio / include / stdio.h |
| adpcm.c | tcpip / tcpip-base / include / stdlib.h |
| main.c | system / stdio / include / stdio.h |
| main.c | tcpip / tcpip-base / include / stdlib.h |

---

## PS2SDK: iop/cdvd/cdvdfsv/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000495_000537.html>

###### include → kernel Relation
| File in iop/cdvd/cdvdfsv/include | Includes file in iop/kernel |
| cdvdfsv.h | include / irx.h |

---

## PS2SDK: iop/cdvd/cdvdman/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000496_000000.html>

###### include → common Relation
| File in iop/cdvd/cdvdman/include | Includes file in common |
| cdvdman.h | include / libcdvd-common.h |

---

## PS2SDK: iop/cdvd/cdvdman/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000496_000537.html>

###### include → kernel Relation
| File in iop/cdvd/cdvdman/include | Includes file in iop/kernel |
| cdvdman.h | include / irx.h |

---

## PS2SDK: iop/cdvd/xatapi/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000497_000000.html>

###### include → common Relation
| File in iop/cdvd/xatapi/include | Includes file in common |
| xatapi.h | include / tamtypes.h |

---

## PS2SDK: iop/debug/iop_sbusdbg/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000498_000000.html>

###### include → common Relation
| File in iop/debug/iop_sbusdbg/include | Includes file in common |
| iop_sbusdbg.h | include / ps2_debug.h |

---

## PS2SDK: iop/debug/iopdebug/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000499_000000.html>

###### include → common Relation
| File in iop/debug/iopdebug/include | Includes file in common |
| iopdebug.h | include / iop_cop0_defs.h |
| iopdebug.h | include / ps2_debug.h |

---

## PS2SDK: iop/debug/iopdebug/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000499_000537.html>

###### include → kernel Relation
| File in iop/debug/iopdebug/include | Includes file in iop/kernel |
| iopdebug.h | include / irx.h |

---

## PS2SDK: iop/debug/ioptrap/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000500_000537.html>

###### include → kernel Relation
| File in iop/debug/ioptrap/include | Includes file in iop/kernel |
| ioptrap.h | include / irx.h |

---

## PS2SDK: iop/debug/sior/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000501_000000.html>

###### include → common Relation
| File in iop/debug/sior/include | Includes file in common |
| sior.h | include / sior-common.h |

---

## PS2SDK: iop/debug/sior/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000501_000537.html>

###### include → kernel Relation
| File in iop/debug/sior/include | Includes file in iop/kernel |
| sior.h | include / irx.h |

---

## PS2SDK: iop/dev9/atad/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000503_000537.html>

###### include → kernel Relation
| File in iop/dev9/atad/include | Includes file in iop/kernel |
| atad.h | include / irx.h |

---

## PS2SDK: iop/dev9/dev9/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000504_000000.html>

###### include → common Relation
| File in iop/dev9/dev9/include | Includes file in common |
| aifdev9.h | include / aifregs.h |
| dev9.h | include / hdd-ioctl.h |

---

## PS2SDK: iop/dev9/dev9/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000504_000537.html>

###### include → kernel Relation
| File in iop/dev9/dev9/include | Includes file in iop/kernel |
| aifdev9.h | include / irx.h |
| dev9.h | include / irx.h |

---

## PS2SDK: iop/dev9/poweroff/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000506_000537.html>

###### include → kernel Relation
| File in iop/dev9/poweroff/include | Includes file in iop/kernel |
| poweroff.h | include / irx.h |

---

## PS2SDK: iop/dev9/pvrdrv/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000507_000537.html>

###### include → kernel Relation
| File in iop/dev9/pvrdrv/include | Includes file in iop/kernel |
| pvrdrv.h | include / irx.h |

---

## PS2SDK: iop/fs/bdm/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000508_000537.html>

###### include → kernel Relation
| File in iop/fs/bdm/include | Includes file in iop/kernel |
| bdm.h | include / irx.h |

---

## PS2SDK: iop/fs/bdm/src/include -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000509_000508.html>

###### include → include Relation
| File in iop/fs/bdm/src/include | Includes file in iop/fs/bdm/include |
| part_driver.h | bdm.h |

---

## PS2SDK: iop/fs/bdmfs_fatfs/src/include -&gt; bdm Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000510_000118.html>

###### include → bdm Relation
| File in iop/fs/bdmfs_fatfs/src/include | Includes file in iop/fs/bdm |
| fs_driver.h | include / bdm.h |

---

## PS2SDK: iop/fs/libbdm -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000511_000000.html>

###### libbdm → common Relation
| File in iop/fs/libbdm | Includes file in common |
| include / bd_cache.h | include / tamtypes.h |
| include / bd_defrag.h | include / tamtypes.h |
| include / bd_defrag.h | include / usbhdfsd-common.h |

---

## PS2SDK: iop/fs/libbdm -&gt; bdm Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000511_000118.html>

###### libbdm → bdm Relation
| File in iop/fs/libbdm | Includes file in iop/fs/bdm |
| include / bd_cache.h | include / bdm.h |
| include / bd_defrag.h | include / bdm.h |

---

## PS2SDK: iop/fs/libbdm -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000511_000223.html>

###### libbdm → system Relation
| File in iop/fs/libbdm | Includes file in iop/system |
| src / include / module_debug.h | stdio / include / stdio.h |
| tests / test_bd_cache.c | stdio / include / stdio.h |

---

## PS2SDK: iop/fs/libbdm -&gt; tcpip Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000511_000284.html>

###### libbdm → tcpip Relation
| File in iop/fs/libbdm | Includes file in iop/tcpip |
| tests / include / sysmem.h | tcpip-base / include / stdlib.h |

---

## PS2SDK: iop/fs/libbdm/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000512_000223.html>

###### src → system Relation
| File in iop/fs/libbdm/src | Includes file in iop/system |
| include / module_debug.h | stdio / include / stdio.h |

---

## PS2SDK: iop/fs/libbdm/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000512_000522.html>

###### src → include Relation
| File in iop/fs/libbdm/src | Includes file in iop/fs/libbdm/include |
| bd_defrag.c | bd_defrag.h |

---

## PS2SDK: iop/fs/libbdm/src/include -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000513_000223.html>

###### include → system Relation
| File in iop/fs/libbdm/src/include | Includes file in iop/system |
| module_debug.h | stdio / include / stdio.h |

---

## PS2SDK: iop/fs/libbdm/tests -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000514_000223.html>

###### tests → system Relation
| File in iop/fs/libbdm/tests | Includes file in iop/system |
| test_bd_cache.c | stdio / include / stdio.h |

---

## PS2SDK: iop/fs/libbdm/tests -&gt; tcpip Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000514_000284.html>

###### tests → tcpip Relation
| File in iop/fs/libbdm/tests | Includes file in iop/tcpip |
| include / sysmem.h | tcpip-base / include / stdlib.h |

---

## PS2SDK: iop/fs/libbdm/tests/include -&gt; tcpip Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000515_000284.html>

###### include → tcpip Relation
| File in iop/fs/libbdm/tests/include | Includes file in iop/tcpip |
| sysmem.h | tcpip-base / include / stdlib.h |

---

## PS2SDK: iop/iLink/IEEE1394_bd/src/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000516_000000.html>

###### include → common Relation
| File in iop/iLink/IEEE1394_bd/src/include | Includes file in common |
| sbp2_disk.h | include / tamtypes.h |

---

## PS2SDK: iop/fs/vfat -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000518_000000.html>

###### vfat → common Relation
| File in iop/fs/vfat | Includes file in common |
| src / fat_driver.c | include / errno.h |
| src / fat_write.c | include / errno.h |
| src / fs_driver.c | include / errno.h |
| src / fs_driver.c | include / usbhdfsd-common.h |
| src / part_driver.c | include / errno.h |
| src / scache.c | include / tamtypes.h |

---

## PS2SDK: iop/fs/vfat -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000518_000056.html>

###### vfat → cdvd Relation
| File in iop/fs/vfat | Includes file in iop/cdvd |
| src / fat_write.c | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/fs/vfat -&gt; bdm Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000518_000118.html>

###### vfat → bdm Relation
| File in iop/fs/vfat | Includes file in iop/fs/bdm |
| src / include / fat_driver.h | include / bdm.h |
| src / scache.c | include / bdm.h |

---

## PS2SDK: iop/fs/vfat -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000518_000223.html>

###### vfat → system Relation
| File in iop/fs/vfat | Includes file in iop/system |
| src / fat_driver.c | stdio / include / stdio.h |
| src / fat_driver.c | sysclib / include / sysclib.h |
| src / fat_driver.c | threadman / include / thbase.h |
| src / fat_write.c | stdio / include / stdio.h |
| src / fat_write.c | sysclib / include / sysclib.h |
| src / fs_driver.c | iomanx / include / iomanX.h |
| src / fs_driver.c | stdio / include / stdio.h |
| src / fs_driver.c | sysclib / include / sysclib.h |
| src / fs_driver.c | threadman / include / thbase.h |
| src / fs_driver.c | threadman / include / thsemap.h |
| src / part_driver.c | stdio / include / stdio.h |
| src / scache.c | stdio / include / stdio.h |

---

## PS2SDK: iop/fs/vfat/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000519_000000.html>

###### src → common Relation
| File in iop/fs/vfat/src | Includes file in common |
| fat_driver.c | include / errno.h |
| fat_write.c | include / errno.h |
| fs_driver.c | include / errno.h |
| fs_driver.c | include / usbhdfsd-common.h |
| part_driver.c | include / errno.h |
| scache.c | include / tamtypes.h |

---

## PS2SDK: iop/fs/vfat/src -&gt; cdvd Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000519_000056.html>

###### src → cdvd Relation
| File in iop/fs/vfat/src | Includes file in iop/cdvd |
| fat_write.c | cdvdman / include / cdvdman.h |

---

## PS2SDK: iop/fs/vfat/src -&gt; bdm Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000519_000118.html>

###### src → bdm Relation
| File in iop/fs/vfat/src | Includes file in iop/fs/bdm |
| include / fat_driver.h | include / bdm.h |
| scache.c | include / bdm.h |

---

## PS2SDK: iop/fs/vfat/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000519_000223.html>

###### src → system Relation
| File in iop/fs/vfat/src | Includes file in iop/system |
| fat_driver.c | stdio / include / stdio.h |
| fat_driver.c | sysclib / include / sysclib.h |
| fat_driver.c | threadman / include / thbase.h |
| fat_write.c | stdio / include / stdio.h |
| fat_write.c | sysclib / include / sysclib.h |
| fs_driver.c | iomanx / include / iomanX.h |
| fs_driver.c | stdio / include / stdio.h |
| fs_driver.c | sysclib / include / sysclib.h |
| fs_driver.c | threadman / include / thbase.h |
| fs_driver.c | threadman / include / thsemap.h |
| part_driver.c | stdio / include / stdio.h |
| scache.c | stdio / include / stdio.h |

---

## PS2SDK: iop/fs/vfat/src/include -&gt; bdm Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000520_000118.html>

###### include → bdm Relation
| File in iop/fs/vfat/src/include | Includes file in iop/fs/bdm |
| fat_driver.h | include / bdm.h |

---

## PS2SDK: iop/fs/devfs/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000521_000537.html>

###### include → kernel Relation
| File in iop/fs/devfs/include | Includes file in iop/kernel |
| devfs.h | include / irx.h |

---

## PS2SDK: iop/fs/libbdm/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000522_000000.html>

###### include → common Relation
| File in iop/fs/libbdm/include | Includes file in common |
| bd_cache.h | include / tamtypes.h |
| bd_defrag.h | include / tamtypes.h |
| bd_defrag.h | include / usbhdfsd-common.h |

---

## PS2SDK: iop/fs/libbdm/include -&gt; bdm Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000522_000118.html>

###### include → bdm Relation
| File in iop/fs/libbdm/include | Includes file in iop/fs/bdm |
| bd_cache.h | include / bdm.h |
| bd_defrag.h | include / bdm.h |

---

## PS2SDK: iop/system/sysmem -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000523_000537.html>

###### sysmem → kernel Relation
| File in iop/system/sysmem | Includes file in iop/kernel |
| include / sysmem.h | include / irx.h |

---

## PS2SDK: iop/system/sysmem/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000524_000537.html>

###### include → kernel Relation
| File in iop/system/sysmem/include | Includes file in iop/kernel |
| sysmem.h | include / irx.h |

---

## PS2SDK: iop/hdd/libapa -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000526_000000.html>

###### libapa → common Relation
| File in iop/hdd/libapa | Includes file in common |
| include / libapa.h | include / hdd-ioctl.h |
| src / apa.c | include / errno.h |
| src / apa.c | include / hdd-ioctl.h |
| src / cache.c | include / errno.h |
| src / cache.c | include / hdd-ioctl.h |
| src / free.c | include / errno.h |
| src / free.c | include / hdd-ioctl.h |
| src / journal.c | include / errno.h |
| src / journal.c | include / hdd-ioctl.h |
| src / misc.c | include / errno.h |
| src / misc.c | include / hdd-ioctl.h |
| src / password.c | include / errno.h |
| src / password.c | include / hdd-ioctl.h |

---

## PS2SDK: iop/hdd/libapa -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000526_000223.html>

###### libapa → system Relation
| File in iop/hdd/libapa | Includes file in iop/system |
| src / apa.c | iomanx / include / iomanX.h |
| src / apa.c | stdio / include / stdio.h |
| src / cache.c | iomanx / include / iomanX.h |
| src / cache.c | stdio / include / stdio.h |
| src / free.c | iomanx / include / iomanX.h |
| src / free.c | stdio / include / stdio.h |
| src / journal.c | iomanx / include / iomanX.h |
| src / journal.c | stdio / include / stdio.h |
| src / misc.c | iomanx / include / iomanX.h |
| src / misc.c | stdio / include / stdio.h |
| src / password.c | iomanx / include / iomanX.h |
| src / password.c | stdio / include / stdio.h |

---

## PS2SDK: iop/hdd/libapa -&gt; tcpip Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000526_000284.html>

###### libapa → tcpip Relation
| File in iop/hdd/libapa | Includes file in iop/tcpip |
| src / misc.c | tcpip-base / include / stdlib.h |

---

## PS2SDK: iop/hdd/libapa -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000526_000537.html>

###### libapa → kernel Relation
| File in iop/hdd/libapa | Includes file in iop/kernel |
| src / misc.c | include / sys / time.h |

---

## PS2SDK: iop/hdd/libapa/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000527_000000.html>

###### include → common Relation
| File in iop/hdd/libapa/include | Includes file in common |
| libapa.h | include / hdd-ioctl.h |

---

## PS2SDK: iop/hdd/libapa/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000528_000000.html>

###### src → common Relation
| File in iop/hdd/libapa/src | Includes file in common |
| apa.c | include / errno.h |
| apa.c | include / hdd-ioctl.h |
| cache.c | include / errno.h |
| cache.c | include / hdd-ioctl.h |
| free.c | include / errno.h |
| free.c | include / hdd-ioctl.h |
| journal.c | include / errno.h |
| journal.c | include / hdd-ioctl.h |
| misc.c | include / errno.h |
| misc.c | include / hdd-ioctl.h |
| password.c | include / errno.h |
| password.c | include / hdd-ioctl.h |

---

## PS2SDK: iop/hdd/libapa/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000528_000223.html>

###### src → system Relation
| File in iop/hdd/libapa/src | Includes file in iop/system |
| apa.c | iomanx / include / iomanX.h |
| apa.c | stdio / include / stdio.h |
| cache.c | iomanx / include / iomanX.h |
| cache.c | stdio / include / stdio.h |
| free.c | iomanx / include / iomanX.h |
| free.c | stdio / include / stdio.h |
| journal.c | iomanx / include / iomanX.h |
| journal.c | stdio / include / stdio.h |
| misc.c | iomanx / include / iomanX.h |
| misc.c | stdio / include / stdio.h |
| password.c | iomanx / include / iomanX.h |
| password.c | stdio / include / stdio.h |

---

## PS2SDK: iop/hdd/libapa/src -&gt; tcpip Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000528_000284.html>

###### src → tcpip Relation
| File in iop/hdd/libapa/src | Includes file in iop/tcpip |
| misc.c | tcpip-base / include / stdlib.h |

---

## PS2SDK: iop/hdd/libapa/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000528_000537.html>

###### src → kernel Relation
| File in iop/hdd/libapa/src | Includes file in iop/kernel |
| misc.c | include / sys / time.h |

---

## PS2SDK: iop/hdd/libpfs -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000529_000000.html>

###### libpfs → common Relation
| File in iop/hdd/libpfs | Includes file in common |
| src / bitmap.c | include / errno.h |
| src / block.c | include / errno.h |
| src / blockWrite.c | include / errno.h |
| src / cache.c | include / errno.h |
| src / cache.c | include / hdd-ioctl.h |
| src / dir.c | include / errno.h |
| src / inode.c | include / errno.h |
| src / journal.c | include / hdd-ioctl.h |
| src / misc.c | include / errno.h |
| src / misc.c | include / hdd-ioctl.h |
| src / super.c | include / errno.h |
| src / super.c | include / hdd-ioctl.h |
| src / superWrite.c | include / errno.h |
| src / superWrite.c | include / hdd-ioctl.h |

---

## PS2SDK: iop/hdd/libpfs -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000529_000223.html>

###### libpfs → system Relation
| File in iop/hdd/libpfs | Includes file in iop/system |
| src / bitmap.c | stdio / include / stdio.h |
| src / block.c | stdio / include / stdio.h |
| src / blockWrite.c | stdio / include / stdio.h |
| src / cache.c | stdio / include / stdio.h |
| src / dir.c | stdio / include / stdio.h |
| src / dir.c | iomanx / include / iomanX.h |
| src / inode.c | stdio / include / stdio.h |
| src / journal.c | stdio / include / stdio.h |
| src / misc.c | stdio / include / stdio.h |
| src / misc.c | iomanx / include / iomanX.h |
| src / misc.c | sysclib / include / ctype.h |
| src / super.c | stdio / include / stdio.h |
| src / superWrite.c | stdio / include / stdio.h |

---

## PS2SDK: iop/hdd/libpfs -&gt; tcpip Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000529_000284.html>

###### libpfs → tcpip Relation
| File in iop/hdd/libpfs | Includes file in iop/tcpip |
| src / misc.c | tcpip-base / include / stdlib.h |

---

## PS2SDK: iop/hdd/libpfs -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000529_000537.html>

###### libpfs → kernel Relation
| File in iop/hdd/libpfs | Includes file in iop/kernel |
| src / misc.c | include / sys / time.h |

---

## PS2SDK: iop/hdd/libpfs/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000530_000000.html>

###### src → common Relation
| File in iop/hdd/libpfs/src | Includes file in common |
| bitmap.c | include / errno.h |
| block.c | include / errno.h |
| blockWrite.c | include / errno.h |
| cache.c | include / errno.h |
| cache.c | include / hdd-ioctl.h |
| dir.c | include / errno.h |
| inode.c | include / errno.h |
| journal.c | include / hdd-ioctl.h |
| misc.c | include / errno.h |
| misc.c | include / hdd-ioctl.h |
| super.c | include / errno.h |
| super.c | include / hdd-ioctl.h |
| superWrite.c | include / errno.h |
| superWrite.c | include / hdd-ioctl.h |

---

## PS2SDK: iop/hdd/libpfs/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000530_000223.html>

###### src → system Relation
| File in iop/hdd/libpfs/src | Includes file in iop/system |
| bitmap.c | stdio / include / stdio.h |
| block.c | stdio / include / stdio.h |
| blockWrite.c | stdio / include / stdio.h |
| cache.c | stdio / include / stdio.h |
| dir.c | iomanx / include / iomanX.h |
| dir.c | stdio / include / stdio.h |
| inode.c | stdio / include / stdio.h |
| journal.c | stdio / include / stdio.h |
| misc.c | sysclib / include / ctype.h |
| misc.c | iomanx / include / iomanX.h |
| misc.c | stdio / include / stdio.h |
| super.c | stdio / include / stdio.h |
| superWrite.c | stdio / include / stdio.h |

---

## PS2SDK: iop/hdd/libpfs/src -&gt; tcpip Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000530_000284.html>

###### src → tcpip Relation
| File in iop/hdd/libpfs/src | Includes file in iop/tcpip |
| misc.c | tcpip-base / include / stdlib.h |

---

## PS2SDK: iop/hdd/libpfs/src -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000530_000537.html>

###### src → kernel Relation
| File in iop/hdd/libpfs/src | Includes file in iop/kernel |
| misc.c | include / sys / time.h |

---

## PS2SDK: iop/iLink/iLinkman/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000533_000537.html>

###### include → kernel Relation
| File in iop/iLink/iLinkman/include | Includes file in iop/kernel |
| iLinkman.h | include / irx.h |

---

## PS2SDK: iop/input/padman/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000535_000537.html>

###### include → kernel Relation
| File in iop/input/padman/include | Includes file in iop/kernel |
| xpadman.h | include / defs.h |

---

## PS2SDK: iop/input/rmman/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000536_000000.html>

###### include → common Relation
| File in iop/input/rmman/include | Includes file in common |
| rmman.h | include / librm-common.h |

---

## PS2SDK: iop/input/rmman/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000536_000537.html>

###### include → kernel Relation
| File in iop/input/rmman/include | Includes file in iop/kernel |
| rmman.h | include / irx.h |

---

## PS2SDK: iop/kernel -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000537_000000.html>

###### kernel → common Relation
| File in iop/kernel | Includes file in common |
| include / types.h | include / tamtypes.h |
| include / sys / types.h | include / tamtypes.h |

---

## PS2SDK: iop/kernel/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000538_000000.html>

###### include → common Relation
| File in iop/kernel/include | Includes file in common |
| types.h | include / tamtypes.h |
| sys / types.h | include / tamtypes.h |

---

## PS2SDK: iop/kernel/include/sys -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000539_000000.html>

###### sys → common Relation
| File in iop/kernel/include/sys | Includes file in common |
| types.h | include / tamtypes.h |

---

## PS2SDK: tools/ps2-irxgen -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000540_000006.html>

###### ps2-irxgen → iop Relation
| File in tools/ps2-irxgen | Includes file in iop |
| src / ps2-irxgen.c | system / stdio / include / stdio.h |
| src / ps2-irxgen.c | tcpip / tcpip-base / include / stdlib.h |
| src / ps2-irxgen.c | system / sysclib / include / ctype.h |

---

## PS2SDK: tools/ps2-irxgen/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000541_000006.html>

###### src → iop Relation
| File in tools/ps2-irxgen/src | Includes file in iop |
| ps2-irxgen.c | system / sysclib / include / ctype.h |
| ps2-irxgen.c | system / stdio / include / stdio.h |
| ps2-irxgen.c | tcpip / tcpip-base / include / stdlib.h |

---

## PS2SDK: iop/memorycard/mcman/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000542_000000.html>

###### include → common Relation
| File in iop/memorycard/mcman/include | Includes file in common |
| mcman.h | include / libmc-common.h |

---

## PS2SDK: iop/memorycard/mcman/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000542_000537.html>

###### include → kernel Relation
| File in iop/memorycard/mcman/include | Includes file in iop/kernel |
| mcman.h | include / irx.h |

---

## PS2SDK: iop/network/netman/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000544_000000.html>

###### include → common Relation
| File in iop/network/netman/include | Includes file in common |
| netdev.h | include / tamtypes.h |

---

## PS2SDK: iop/network/smap/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000545_000000.html>

###### include → common Relation
| File in iop/network/smap/include | Includes file in common |
| smap_modular.h | include / tamtypes.h |

---

## PS2SDK: iop/network/spduart/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000546_000537.html>

###### include → kernel Relation
| File in iop/network/spduart/include | Includes file in iop/kernel |
| modem.h | include / irx.h |

---

## PS2SDK: iop/security/secrman/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000547_000000.html>

###### include → common Relation
| File in iop/security/secrman/include | Includes file in common |
| secrman.h | include / libsecr-common.h |

---

## PS2SDK: iop/security/secrman/include -&gt; sio Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000547_000197.html>

###### include → sio Relation
| File in iop/security/secrman/include | Includes file in iop/sio |
| secrman.h | sio2man / include / sio2man.h |

---

## PS2SDK: iop/security/secrman/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000547_000537.html>

###### include → kernel Relation
| File in iop/security/secrman/include | Includes file in iop/kernel |
| secrman.h | include / irx.h |

---

## PS2SDK: iop/sio/mtapman/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000548_000537.html>

###### include → kernel Relation
| File in iop/sio/mtapman/include | Includes file in iop/kernel |
| xmtapman.h | include / irx.h |

---

## PS2SDK: iop/sio/sio2man/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000549_000537.html>

###### include → kernel Relation
| File in iop/sio/sio2man/include | Includes file in iop/kernel |
| sio2man.h | include / irx.h |

---

## PS2SDK: iop/sound/libsnd2 -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000553_000000.html>

###### libsnd2 → common Relation
| File in iop/sound/libsnd2 | Includes file in common |
| src / include / libsnd2_internal.h | include / tamtypes.h |

---

## PS2SDK: iop/sound/libsnd2 -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000553_000223.html>

###### libsnd2 → system Relation
| File in iop/sound/libsnd2 | Includes file in iop/system |
| src / include / libsnd2_internal.h | intrman / include / intrman.h |
| src / include / libsnd2_internal.h | stdio / include / stdio.h |
| src / include / libsnd2_internal.h | sysclib / include / sysclib.h |
| src / include / libsnd2_internal.h | threadman / include / thbase.h |
| src / include / libsnd2_internal.h | timrman / include / timrman.h |
| src / include / libsnd2_internal.h | vblank / include / vblank.h |

---

## PS2SDK: iop/sound/libsnd2/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000555_000000.html>

###### src → common Relation
| File in iop/sound/libsnd2/src | Includes file in common |
| include / libsnd2_internal.h | include / tamtypes.h |

---

## PS2SDK: iop/sound/libsnd2/src -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000555_000223.html>

###### src → system Relation
| File in iop/sound/libsnd2/src | Includes file in iop/system |
| include / libsnd2_internal.h | intrman / include / intrman.h |
| include / libsnd2_internal.h | stdio / include / stdio.h |
| include / libsnd2_internal.h | sysclib / include / sysclib.h |
| include / libsnd2_internal.h | threadman / include / thbase.h |
| include / libsnd2_internal.h | timrman / include / timrman.h |
| include / libsnd2_internal.h | vblank / include / vblank.h |

---

## PS2SDK: iop/sound/libsnd2/src/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000556_000000.html>

###### include → common Relation
| File in iop/sound/libsnd2/src/include | Includes file in common |
| libsnd2_internal.h | include / tamtypes.h |

---

## PS2SDK: iop/sound/libsnd2/src/include -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000556_000223.html>

###### include → system Relation
| File in iop/sound/libsnd2/src/include | Includes file in iop/system |
| libsnd2_internal.h | intrman / include / intrman.h |
| libsnd2_internal.h | stdio / include / stdio.h |
| libsnd2_internal.h | sysclib / include / sysclib.h |
| libsnd2_internal.h | threadman / include / thbase.h |
| libsnd2_internal.h | timrman / include / timrman.h |
| libsnd2_internal.h | vblank / include / vblank.h |

---

## PS2SDK: iop/sound/libspu2 -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000558_000000.html>

###### libspu2 → common Relation
| File in iop/sound/libspu2 | Includes file in common |
| include / libspu2_internal.h | include / tamtypes.h |

---

## PS2SDK: iop/sound/libspu2 -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000558_000223.html>

###### libspu2 → system Relation
| File in iop/sound/libspu2 | Includes file in iop/system |
| include / libspu2_internal.h | intrman / include / intrman.h |
| include / libspu2_internal.h | loadcore / include / loadcore.h |
| include / libspu2_internal.h | stdio / include / stdio.h |

---

## PS2SDK: iop/sound/libspu2/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000559_000000.html>

###### include → common Relation
| File in iop/sound/libspu2/include | Includes file in common |
| libspu2_internal.h | include / tamtypes.h |

---

## PS2SDK: iop/sound/libspu2/include -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000559_000223.html>

###### include → system Relation
| File in iop/sound/libspu2/include | Includes file in iop/system |
| libspu2_internal.h | intrman / include / intrman.h |
| libspu2_internal.h | loadcore / include / loadcore.h |
| libspu2_internal.h | stdio / include / stdio.h |

---

## PS2SDK: iop/sound/rspu2drv/src/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000561_000000.html>

###### include → common Relation
| File in iop/sound/rspu2drv/src/include | Includes file in common |
| rs_i.h | include / tamtypes.h |

---

## PS2SDK: iop/sound/rspu2drv/src/include -&gt; system Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000561_000223.html>

###### include → system Relation
| File in iop/sound/rspu2drv/src/include | Includes file in iop/system |
| rs_i.h | intrman / include / intrman.h |
| rs_i.h | loadcore / include / loadcore.h |
| rs_i.h | sifman / include / sifman.h |
| rs_i.h | threadman / include / thbase.h |

---

## PS2SDK: iop/sound/sdrdrv/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000563_000000.html>

###### include → common Relation
| File in iop/sound/sdrdrv/include | Includes file in common |
| sdrdrv.h | include / libsdr-common.h |

---

## PS2SDK: iop/system/alloc/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000565_000537.html>

###### include → kernel Relation
| File in iop/system/alloc/include | Includes file in iop/kernel |
| alloc.h | include / irx.h |

---

## PS2SDK: iop/system/dmacman/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000566_000537.html>

###### include → kernel Relation
| File in iop/system/dmacman/include | Includes file in iop/kernel |
| dmacman.h | include / irx.h |

---

## PS2SDK: iop/system/dummymod -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000567_000248.html>

###### dummymod → loadcore Relation
| File in iop/system/dummymod | Includes file in iop/system/loadcore |
| src / dummymod.c | include / loadcore.h |

---

## PS2SDK: iop/system/dummymod/src -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000568_000248.html>

###### src → loadcore Relation
| File in iop/system/dummymod/src | Includes file in iop/system/loadcore |
| dummymod.c | include / loadcore.h |

---

## PS2SDK: iop/system/excepman/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000569_000537.html>

###### include → kernel Relation
| File in iop/system/excepman/include | Includes file in iop/kernel |
| excepman.h | include / irx.h |

---

## PS2SDK: iop/system/heaplib/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000570_000537.html>

###### include → kernel Relation
| File in iop/system/heaplib/include | Includes file in iop/kernel |
| heaplib.h | include / irx.h |

---

## PS2SDK: iop/system/intrman/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000571_000537.html>

###### include → kernel Relation
| File in iop/system/intrman/include | Includes file in iop/kernel |
| intrman.h | include / irx.h |

---

## PS2SDK: iop/system/ioman/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000572_000000.html>

###### include → common Relation
| File in iop/system/ioman/include | Includes file in common |
| ioman.h | include / io_common.h |
| ioman_mod.h | include / io_common.h |
| ioman_mod.h | include / iox_stat.h |

---

## PS2SDK: iop/system/ioman/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000572_000537.html>

###### include → kernel Relation
| File in iop/system/ioman/include | Includes file in iop/kernel |
| ioman.h | include / irx.h |
| ioman_mod.h | include / irx.h |

---

## PS2SDK: iop/system/iomanx/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000573_000000.html>

###### include → common Relation
| File in iop/system/iomanx/include | Includes file in common |
| iomanX.h | include / io_common.h |
| iomanX.h | include / iox_stat.h |

---

## PS2SDK: iop/system/iopmgr/include -&gt; ioman Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000574_000242.html>

###### include → ioman Relation
| File in iop/system/iopmgr/include | Includes file in iop/system/ioman |
| iopmgr.h | include / ioman.h |

---

## PS2SDK: iop/system/iopmgr/include -&gt; loadcore Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000574_000248.html>

###### include → loadcore Relation
| File in iop/system/iopmgr/include | Includes file in iop/system/loadcore |
| iopmgr.h | include / loadcore.h |

---

## PS2SDK: iop/system/iopmgr/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000574_000537.html>

###### include → kernel Relation
| File in iop/system/iopmgr/include | Includes file in iop/kernel |
| iopmgr.h | include / irx.h |

---

## PS2SDK: iop/system/loadcore/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000575_000537.html>

###### include → kernel Relation
| File in iop/system/loadcore/include | Includes file in iop/kernel |
| loadcore.h | include / irx.h |

---

## PS2SDK: iop/system/modload/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000576_000537.html>

###### include → kernel Relation
| File in iop/system/modload/include | Includes file in iop/kernel |
| modload.h | include / irx.h |

---

## PS2SDK: iop/system/sbusintr/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000578_000537.html>

###### include → kernel Relation
| File in iop/system/sbusintr/include | Includes file in iop/kernel |
| sbusintr.h | include / irx.h |

---

## PS2SDK: iop/system/sifman/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000579_000537.html>

###### include → kernel Relation
| File in iop/system/sifman/include | Includes file in iop/kernel |
| sifman.h | include / irx.h |

---

## PS2SDK: iop/system/siftoo/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000580_000537.html>

###### include → kernel Relation
| File in iop/system/siftoo/include | Includes file in iop/kernel |
| siftoo.h | include / irx.h |

---

## PS2SDK: iop/system/ssbusc/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000581_000537.html>

###### include → kernel Relation
| File in iop/system/ssbusc/include | Includes file in iop/kernel |
| ssbusc.h | include / irx.h |

---

## PS2SDK: iop/system/stdio/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000582_000537.html>

###### include → kernel Relation
| File in iop/system/stdio/include | Includes file in iop/kernel |
| stdio.h | include / irx.h |

---

## PS2SDK: iop/system/sysclib/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000583_000000.html>

###### include → common Relation
| File in iop/system/sysclib/include | Includes file in common |
| setjmp.h | include / tamtypes.h |

---

## PS2SDK: iop/system/sysclib/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000583_000537.html>

###### include → kernel Relation
| File in iop/system/sysclib/include | Includes file in iop/kernel |
| sysclib.h | include / irx.h |

---

## PS2SDK: iop/system/sysclib/src/embeddedartistry_libc -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000584_000583.html>

###### embeddedartistry_libc → include Relation
| File in iop/system/sysclib/src/embeddedartistry_libc | Includes file in iop/system/sysclib/include |
| stdlib / strtol.c | ctype.h |
| stdlib / strtol.c | sysclib.h |
| stdlib / strtoul.c | ctype.h |
| stdlib / strtoul.c | sysclib.h |

---

## PS2SDK: iop/system/sysclib/src/embeddedartistry_libc/stdlib -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000585_000583.html>

###### stdlib → include Relation
| File in iop/system/sysclib/src/embeddedartistry_libc/stdlib | Includes file in iop/system/sysclib/include |
| strtol.c | ctype.h |
| strtol.c | sysclib.h |
| strtoul.c | ctype.h |
| strtoul.c | sysclib.h |

---

## PS2SDK: iop/system/sysclib/src/size_optimized -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000586_000583.html>

###### size_optimized → include Relation
| File in iop/system/sysclib/src/size_optimized | Includes file in iop/system/sysclib/include |
| memchr.c | sysclib.h |
| memcpy.c | sysclib.h |
| memmove.c | sysclib.h |
| memset.c | sysclib.h |
| rindex.c | sysclib.h |
| strchr.c | sysclib.h |
| strcmp.c | sysclib.h |
| strrchr.c | sysclib.h |
| strspn.c | sysclib.h |
| strstr.c | sysclib.h |
| strtok.c | sysclib.h |
| strtok_r.c | sysclib.h |
| strtol.c | sysclib.h |
| strtoul.c | sysclib.h |
| sysclib_determine_base.c | sysclib.h |

---

## PS2SDK: iop/system/sysclib/src/eyalroz_printf -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000587_000583.html>

###### eyalroz_printf → include Relation
| File in iop/system/sysclib/src/eyalroz_printf | Includes file in iop/system/sysclib/include |
| printf.c | sysclib.h |

---

## PS2SDK: iop/system/sysclib/src/musl -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000588_000583.html>

###### musl → include Relation
| File in iop/system/sysclib/src/musl | Includes file in iop/system/sysclib/include |
| ctype / tolower.c | sysclib.h |
| ctype / toupper.c | sysclib.h |
| string / bcmp.c | sysclib.h |
| string / bcopy.c | sysclib.h |
| string / bzero.c | sysclib.h |
| string / index.c | sysclib.h |
| string / memchr.c | sysclib.h |
| string / memcmp.c | sysclib.h |
| string / memcpy.c | sysclib.h |
| string / memmove.c | sysclib.h |
| string / memrchr.c | sysclib.h |
| string / memset.c | sysclib.h |
| string / rindex.c | sysclib.h |
| string / stpcpy.c | sysclib.h |
| string / stpncpy.c | sysclib.h |
| string / strcat.c | sysclib.h |
| string / strchr.c | sysclib.h |
| string / strchrnul.c | sysclib.h |
| string / strcmp.c | sysclib.h |
| string / strcpy.c | sysclib.h |
| string / strcspn.c | sysclib.h |
| string / strlen.c | sysclib.h |
| string / strncat.c | sysclib.h |
| string / strncmp.c | sysclib.h |
| string / strncpy.c | sysclib.h |
| string / strpbrk.c | sysclib.h |
| string / strrchr.c | sysclib.h |
| string / strspn.c | sysclib.h |
| string / strstr.c | sysclib.h |
| string / strtok.c | sysclib.h |

---

## PS2SDK: iop/system/sysclib/src/musl/ctype -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000589_000583.html>

###### ctype → include Relation
| File in iop/system/sysclib/src/musl/ctype | Includes file in iop/system/sysclib/include |
| tolower.c | sysclib.h |
| toupper.c | sysclib.h |

---

## PS2SDK: iop/system/sysclib/src/musl/string -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000590_000583.html>

###### string → include Relation
| File in iop/system/sysclib/src/musl/string | Includes file in iop/system/sysclib/include |
| bcmp.c | sysclib.h |
| bcopy.c | sysclib.h |
| bzero.c | sysclib.h |
| index.c | sysclib.h |
| memchr.c | sysclib.h |
| memcmp.c | sysclib.h |
| memcpy.c | sysclib.h |
| memmove.c | sysclib.h |
| memrchr.c | sysclib.h |
| memset.c | sysclib.h |
| rindex.c | sysclib.h |
| stpcpy.c | sysclib.h |
| stpncpy.c | sysclib.h |
| strcat.c | sysclib.h |
| strchr.c | sysclib.h |
| strchrnul.c | sysclib.h |
| strcmp.c | sysclib.h |
| strcpy.c | sysclib.h |
| strcspn.c | sysclib.h |
| strlen.c | sysclib.h |
| strncat.c | sysclib.h |
| strncmp.c | sysclib.h |
| strncpy.c | sysclib.h |
| strpbrk.c | sysclib.h |
| strrchr.c | sysclib.h |
| strspn.c | sysclib.h |
| strstr.c | sysclib.h |
| strtok.c | sysclib.h |

---

## PS2SDK: iop/system/sysclib/src/newlib -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000591_000000.html>

###### newlib → common Relation
| File in iop/system/sysclib/src/newlib | Includes file in common |
| libc / machine / mips / machine / fenv-softfloat.h | include / errno.h |

---

## PS2SDK: iop/system/sysclib/src/newlib -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000591_000583.html>

###### newlib → include Relation
| File in iop/system/sysclib/src/newlib | Includes file in iop/system/sysclib/include |
| libc / machine / mips / strncpy.c | sysclib.h |

---

## PS2SDK: iop/system/sysclib/src/newlib/libc -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000592_000000.html>

###### libc → common Relation
| File in iop/system/sysclib/src/newlib/libc | Includes file in common |
| machine / mips / machine / fenv-softfloat.h | include / errno.h |

---

## PS2SDK: iop/system/sysclib/src/newlib/libc -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000592_000583.html>

###### libc → include Relation
| File in iop/system/sysclib/src/newlib/libc | Includes file in iop/system/sysclib/include |
| machine / mips / strncpy.c | sysclib.h |

---

## PS2SDK: iop/system/sysclib/src/newlib/libc/machine -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000593_000000.html>

###### machine → common Relation
| File in iop/system/sysclib/src/newlib/libc/machine | Includes file in common |
| mips / machine / fenv-softfloat.h | include / errno.h |

---

## PS2SDK: iop/system/sysclib/src/newlib/libc/machine -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000593_000583.html>

###### machine → include Relation
| File in iop/system/sysclib/src/newlib/libc/machine | Includes file in iop/system/sysclib/include |
| mips / strncpy.c | sysclib.h |

---

## PS2SDK: iop/system/sysclib/src/newlib/libc/machine/mips -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000594_000000.html>

###### mips → common Relation
| File in iop/system/sysclib/src/newlib/libc/machine/mips | Includes file in common |
| machine / fenv-softfloat.h | include / errno.h |

---

## PS2SDK: iop/system/sysclib/src/newlib/libc/machine/mips -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000594_000583.html>

###### mips → include Relation
| File in iop/system/sysclib/src/newlib/libc/machine/mips | Includes file in iop/system/sysclib/include |
| strncpy.c | sysclib.h |

---

## PS2SDK: iop/system/sysclib/src/newlib/libc/machine/mips/machine -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000595_000000.html>

###### machine → common Relation
| File in iop/system/sysclib/src/newlib/libc/machine/mips/machine | Includes file in common |
| fenv-softfloat.h | include / errno.h |

---

## PS2SDK: iop/system/sysclib/src/nonstd -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000596_000583.html>

###### nonstd → include Relation
| File in iop/system/sysclib/src/nonstd | Includes file in iop/system/sysclib/include |
| _wmemcopy.c | sysclib.h |
| _wmemset.c | sysclib.h |
| atob.c | sysclib.h |
| ctype.c | sysclib.h |

---

## PS2SDK: iop/system/sysmem/src -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000597_000524.html>

###### src → include Relation
| File in iop/system/sysmem/src | Includes file in iop/system/sysmem/include |
| sysmem.c | xsysmem.h |

---

## PS2SDK: iop/system/threadman/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000598_000537.html>

###### include → kernel Relation
| File in iop/system/threadman/include | Includes file in iop/kernel |
| thbase.h | include / irx.h |
| thevent.h | include / irx.h |
| thfpool.h | include / irx.h |
| thmsgbx.h | include / irx.h |
| thsemap.h | include / irx.h |
| thvpool.h | include / irx.h |

---

## PS2SDK: iop/system/threadman/src/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000599_000000.html>

###### include → common Relation
| File in iop/system/threadman/src/include | Includes file in common |
| thcommon.h | include / tamtypes.h |

---

## PS2SDK: iop/system/threadman/src/include -&gt; include Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000599_000598.html>

###### include → include Relation
| File in iop/system/threadman/src/include | Includes file in iop/system/threadman/include |
| thcommon.h | thbase.h |
| thcommon.h | thmsgbx.h |

---

## PS2SDK: iop/system/timrman/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000600_000537.html>

###### include → kernel Relation
| File in iop/system/timrman/include | Includes file in iop/kernel |
| timrman.h | include / irx.h |

---

## PS2SDK: iop/system/vblank/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000601_000537.html>

###### include → kernel Relation
| File in iop/system/vblank/include | Includes file in iop/kernel |
| vblank.h | include / irx.h |

---

## PS2SDK: iop/usb/usbd/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000603_000537.html>

###### include → kernel Relation
| File in iop/usb/usbd/include | Includes file in iop/kernel |
| usbd.h | include / irx.h |

---

## PS2SDK: iop/usb/usbhdfsd/include -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000604_000000.html>

###### include → common Relation
| File in iop/usb/usbhdfsd/include | Includes file in common |
| usbhdfsd.h | include / usbhdfsd-common.h |

---

## PS2SDK: iop/usb/usbhdfsd/include -&gt; kernel Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000604_000537.html>

###### include → kernel Relation
| File in iop/usb/usbhdfsd/include | Includes file in iop/kernel |
| usbhdfsd.h | include / irx.h |

---

## PS2SDK: tools/srxfixup -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000607_000000.html>

###### srxfixup → common Relation
| File in tools/srxfixup | Includes file in common |
| src / elflib.c | include / errno.h |
| src / readconf.c | include / errno.h |

---

## PS2SDK: tools/srxfixup -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000607_000006.html>

###### srxfixup → iop Relation
| File in tools/srxfixup | Includes file in iop |
| src / anaarg.c | system / stdio / include / stdio.h |
| src / anaarg.c | tcpip / tcpip-base / include / stdlib.h |
| src / elfdump.c | system / stdio / include / stdio.h |
| src / elfdump.c | tcpip / tcpip-base / include / stdlib.h |
| src / elflib.c | system / stdio / include / stdio.h |
| src / elflib.c | tcpip / tcpip-base / include / stdlib.h |
| src / mipsdis.c | system / stdio / include / stdio.h |
| src / mipsdis.c | tcpip / tcpip-base / include / stdlib.h |
| src / readconf.c | system / sysclib / include / ctype.h |
| src / readconf.c | system / stdio / include / stdio.h |
| src / readconf.c | tcpip / tcpip-base / include / stdlib.h |
| src / srxfixup.c | system / stdio / include / stdio.h |
| src / srxfixup.c | tcpip / tcpip-base / include / stdlib.h |
| src / srxgen.c | system / stdio / include / stdio.h |
| src / srxgen.c | tcpip / tcpip-base / include / stdlib.h |

---

## PS2SDK: tools/bin2c -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000608_000006.html>

###### bin2c → iop Relation
| File in tools/bin2c | Includes file in iop |
| src / bin2c.c | tcpip / tcpip-base / include / stdlib.h |
| src / bin2c.c | system / stdio / include / stdio.h |

---

## PS2SDK: tools/bin2c/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000609_000006.html>

###### src → iop Relation
| File in tools/bin2c/src | Includes file in iop |
| bin2c.c | system / stdio / include / stdio.h |
| bin2c.c | tcpip / tcpip-base / include / stdlib.h |

---

## PS2SDK: tools/srxfixup/src -&gt; common Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000610_000000.html>

###### src → common Relation
| File in tools/srxfixup/src | Includes file in common |
| elflib.c | include / errno.h |
| readconf.c | include / errno.h |

---

## PS2SDK: tools/srxfixup/src -&gt; iop Relation

Page: <https://ps2dev.github.io/ps2sdk/dir_000610_000006.html>

###### src → iop Relation
| File in tools/srxfixup/src | Includes file in iop |
| anaarg.c | system / stdio / include / stdio.h |
| anaarg.c | tcpip / tcpip-base / include / stdlib.h |
| elfdump.c | system / stdio / include / stdio.h |
| elfdump.c | tcpip / tcpip-base / include / stdlib.h |
| elflib.c | system / stdio / include / stdio.h |
| elflib.c | tcpip / tcpip-base / include / stdlib.h |
| mipsdis.c | system / stdio / include / stdio.h |
| mipsdis.c | tcpip / tcpip-base / include / stdlib.h |
| readconf.c | system / sysclib / include / ctype.h |
| readconf.c | system / stdio / include / stdio.h |
| readconf.c | tcpip / tcpip-base / include / stdlib.h |
| srxfixup.c | system / stdio / include / stdio.h |
| srxfixup.c | tcpip / tcpip-base / include / stdlib.h |
| srxgen.c | system / stdio / include / stdio.h |
| srxgen.c | tcpip / tcpip-base / include / stdlib.h |

---

## hdsk Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_00d6fa0d09c5792a738445385c091044.html>

Directory dependency graph for hdsk:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_00e8a216ae9cff254bd9d39011256e74.html>

Directory dependency graph for src:
##### Files
| file | erl.c [code] |

---

## bdm Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_0134b0376fbe77322088b496fb368f9b.html>

Directory dependency graph for bdm:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_01501b883201dcb99681b284dc447cd3.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_01cf0d0d14f0be3d7fbcbe1a8f31822d.html>

Directory dependency graph for src:

---

## igreeting Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_01d758e74f9dc999d6afb4cc0aea262a.html>

Directory dependency graph for igreeting:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_01e562a7eba275d197a1ab0d788a2427.html>

*(no textual content on this page)*

---

## mouse Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_023d61e4a9775347d84fc5d33820923f.html>

Directory dependency graph for mouse:
##### Directories

---

## iopmgr Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_024ed9b5cab300e9b0cec9fa63c26df3.html>

Directory dependency graph for iopmgr:
##### Directories

---

## romdrv Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_026e95636ee7a5fe61bdfe401a766815.html>

Directory dependency graph for romdrv:
##### Directories

---

## timrman Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_031757951e60c16ad930ba76071ecfef.html>

Directory dependency graph for timrman:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_045af3c93ddda0c519219edb2a8fe08a.html>

Directory dependency graph for include:
##### Files
| file | packet.h [code] |

---

## ee Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_049738f1909e8dc3e45fe1f6b3faa109.html>

Directory dependency graph for ee:
##### Directories
| directory | debug |
| directory | dma |
| directory | draw |
| directory | eedebug |
| directory | elf-loader |
| directory | elf-loader2 |
| directory | erl |
| directory | erl-loader |
| directory | font |
| directory | graph |
| directory | input |
| directory | iopreboot |
| directory | ioprpgen |
| directory | libcglue |
| directory | libgs |
| directory | libprofglue |
| directory | libpthreadglue |
| directory | libvux |
| directory | math3d |
| directory | mpeg |
| directory | network |
| directory | packet |
| directory | packet2 |
| directory | rpc |
| directory | sbv |
| directory | startup |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_04b7edd16940ea0b39ef53819f3e66c2.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_05548f5c43376a182e98a31d23da3cca.html>

Directory dependency graph for include:
##### Files
| file | libsdr.h [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_06508ded56efeb0264642d328f7c09ba.html>

Directory dependency graph for src:
##### Files
| file | ps2ipc.c [code] |

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_072d739ab4e5df2618470b14012a0f75.html>

##### Files
| file | startup.h [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_078466d19e2c07d35cefa1d92cc85a8d.html>

Directory dependency graph for src:

---

## excepman Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_07d95afa3a823c57813d0b20ca3e9410.html>

Directory dependency graph for excepman:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_084c3ccb3eeb869f6b2ed92eea27983e.html>

Directory dependency graph for include:
##### Files
| file | stdio.h [code] |

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_087ec6d829fa5149c3c411dbd4f26dd8.html>

Directory dependency graph for include:
##### Files
| file | cdvdman.h [code] |

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_08d70405097c99e30db4dc706e919eb5.html>

*(no textual content on this page)*

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_091fb412ea895ba245469a0ae307f42f.html>

Directory dependency graph for include:

---

## iop Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_0981ace215aa2029f526b70c145b9fbe.html>

Directory dependency graph for iop:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_0a4671ad047c01d5afa56274ab81ddbc.html>

Directory dependency graph for src:

---

## dummymod Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_0a9d37126d3b936a2cd77bfafbdc06cf.html>

Directory dependency graph for dummymod:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_0aa9326f8220a9dcd66988ff919badd9.html>

Directory dependency graph for src:

---

## libsnd2 Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_0b9117660766c284fe50bbf9fd6992c7.html>

Directory dependency graph for libsnd2:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_0bd4cecc065cbd19f484fdaa8dc65a58.html>

Directory dependency graph for include:

---

## size_optimized Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_0beacc05ac1d7f4fed3f447a40616c4b.html>

Directory dependency graph for size_optimized:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_0bef156b26d0b9d7633e44398b178fff.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_0c8008b518a3418ede49e87f54eaf07c.html>

Directory dependency graph for include:
##### Files
| file | ioptrap.h [code] |

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_0cd450caaa4db46b47a6dfe36d291a89.html>

*(no textual content on this page)*

---

## rmman Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_0d4a06d2fb3b112f7b62a2f21991c61d.html>

Directory dependency graph for rmman:
##### Directories

---

## arch Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_0d9680ecd09e14b3d7838227a56c72b1.html>

Directory dependency graph for arch:

---

## usbmload Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_0e44eec822d0f16d7c5797b7b3482243.html>

Directory dependency graph for usbmload:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_0ebede9b392157881872441ee7719c59.html>

##### Files
| file | libpad.h [code] |

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_0f813698607c3b694207b515d15a76ee.html>

Directory dependency graph for include:
##### Files
| file | modem.h [code] |

---

## ps2snd Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_0fa59b7b5c95696e5fa18237205389fe.html>

Directory dependency graph for ps2snd:
##### Directories

---

## sior Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_1019ee746f7ebb462d4ffdfca40dcd8c.html>

Directory dependency graph for sior:
##### Directories

---

## libbdm Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_10cce8191a2d4629e92aaca1231c0797.html>

Directory dependency graph for libbdm:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_110e40b434acbed75cb95dacd80213fb.html>

Directory dependency graph for src:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_116803b6ae9ead050112c82eaa6ccbbe.html>

Directory dependency graph for src:
##### Files
| file | ioptrap.c [code] |

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_11c221392ef51a238b9c195e459ef5de.html>

Directory dependency graph for include:
##### Files
| file | iopdebug.h [code] |

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_11e1917e435ac241c6d03c8c7e43533b.html>

Directory dependency graph for include:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_11fbc4217d50ab21044e5ad6614aede5.html>

Directory dependency graph for include:
##### Directories
##### Files
| file | aifregs.h [code] |
| file | as_reg_compat.h [code] |
| file | atahw.h [code] |
| file | blkio-ioctl.h [code] |
| file | cdvd-ioctl.h [code] |
| file | dev5_mmio_hwport.h [code] |
| file | dev9regs.h [code] |
| file | ee_cop0_defs.h [code] |
| file | ee_regs.h [code] |
| file | errno.h [code] |
| file | fileio-common.h [code] |
| file | fileXio.h [code] |
| file | gif_registers.h [code] |
| file | gif_tags.h [code] |
| file | gs_gp.h [code] |
| file | gs_privileged.h [code] |
| file | gs_psm.h [code] |
| file | hdd-ioctl.h [code] |
| file | io_common.h [code] |
| file | iop_cop0_defs.h [code] |
| file | iop_low_memory_globals.h [code] |
| file | iop_mmio_hwport.h [code] |
| file | iop_regs.h [code] |
| file | iopheap-common.h [code] |
| file | iox_stat.h [code] |
| file | libcdvd-common.h [code] |
| file | libcdvd-rpc.h [code] |
| file | libmc-common.h [code] |
| file | librm-common.h [code] |
| file | libsd-common.h [code] |
| file | libsdr-common.h [code] |
| file | libsecr-common.h [code] |
| file | loadfile-common.h [code] |
| file | mipscopaccess.h [code] |
| file | netman.h [code] |
| file | netman_rpc.h [code] |
| file | ps2_debug.h [code] |
| file | ps2_reg_defs.h [code] |
| file | ps2ip_rpc.h [code] |
| file | ps2lib_err.h [code] |
| file | ps2smb.h [code] |
| file | ps2snd.h [code] |
| file | pwroff_rpc.h [code] |
| file | s147_mmio_hwport.h [code] |
| file | sif_mmio_hwport.h [code] |
| file | sifcmd-common.h [code] |
| file | sifrpc-common.h [code] |
| file | sior-common.h [code] |
| file | smapregs.h [code] |
| file | speedregs.h [code] |
| file | spu2_mmio_hwport.h [code] |
| file | tamtypes.h [code] |
| file | tcpip.h [code] |
| file | usbhdfsd-common.h [code] |
| file | vif_codes.h [code] |
| file | vif_registers.h [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_1330cdeae45deffc488198fbac42e9b7.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_139d70fd891b64edfcd5f802a3d19228.html>

Directory dependency graph for include:
##### Directories
##### Files
| file | sjis.h [code] |

---

## eromdrv Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_142b7481c6c3c098cbb52321b961d34b.html>

Directory dependency graph for eromdrv:
##### Directories

---

## acram Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_1431105f3fb19cd016c4be314bacdc47.html>

Directory dependency graph for acram:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_149368a66351dc297906871c4b85f61b.html>

Directory dependency graph for include:
##### Files
| file | ssbusc.h [code] |

---

## dvrmisc Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_14f5f0f9fe610eb1d19d953c1b59d5ca.html>

Directory dependency graph for dvrmisc:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_180e179e842835315c1a0a2fde604530.html>

Directory dependency graph for src:
##### Directories

---

## dev9 Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_18566863331aaba44604539ca78be099.html>

Directory dependency graph for dev9:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_192cb8dc90ce20c6feb1ebf06f9e0f32.html>

*(no textual content on this page)*

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_1a0c1cc6a62ce99b34521e1896eac836.html>

Directory dependency graph for include:
##### Files
| file | siftoo.h [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_1a15d16f9d67565cc9b389bcd85d26fc.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_1a6a5c5b3f159e21af436fb86af6ff87.html>

Directory dependency graph for src:
##### Files
| file | libkbd.c [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_1a7f0e9c955f51a704f1181957f21135.html>

Directory dependency graph for src:
##### Files
| file | commandline.c [code] |
| file | devices.c [code] |
| file | main.c [code] |
| file | slib.c [code] |
| file | smod.c [code] |

---

## fileio Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_1af2fbc890c779e5008e3d270a0ec9ec.html>

Directory dependency graph for fileio:
##### Directories

---

## packet2 Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_1af66471b4b3ad2da2cd94ca709331b2.html>

Directory dependency graph for packet2:
##### Directories

---

## mx4sio_bd Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_1b4c53ad4cba67b900d09766188e54d5.html>

Directory dependency graph for mx4sio_bd:
##### Directories

---

## sysclib Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_1bd32d4ef826aeeda00870843eb45c97.html>

Directory dependency graph for sysclib:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_1be4f468fd3869a0e0c79ea67b3fec9d.html>

Directory dependency graph for include:
##### Files
| file | heaplib.h [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_1bf9d7f8fdc080f66e5f30cbc433a0d9.html>

Directory dependency graph for src:
##### Directories
| directory | ldrsrc |

---

## acrtc Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_1ce65a17f8f99ac874f77278c69e114f.html>

Directory dependency graph for acrtc:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_1cf1dd8a7bd9698d15d4cde14597cf7a.html>

Directory dependency graph for src:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_1cf9825758cfa96e5407c225ac2b98d0.html>

Directory dependency graph for src:

---

## tcpips Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_1cfecee880be5098a90e1a8a26e46a3f.html>

Directory dependency graph for tcpips:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_1d2d052e00250e536a87902d7d819545.html>

Directory dependency graph for src:

---

## input Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_1d5b5972f55298e8143c1e3e800fccfd.html>

Directory dependency graph for input:

---

## loadcore Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_1d64e5e9f20206636d72b5bbe3d2b274.html>

Directory dependency graph for loadcore:
##### Directories

---

## tcpip Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_1e6823be46b3bf5bb635c8394bb31ba4.html>

Directory dependency graph for tcpip:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_1f40ef72980d3b99e22f53eb9e1ca715.html>

Directory dependency graph for src:

---

## cdvdfsv Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_1f6440c08895654e298b91d0ddcbd2c2.html>

Directory dependency graph for cdvdfsv:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_1f79197ed0f2fe87066ca3a0bf95d7af.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_1f9c0e40349f60b0e30c14f93ed10e1a.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_20e91a8bae2e1f802bcb7f8435cbf723.html>

Directory dependency graph for include:

---

## netman Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_2103a4ed81746d00ca3b9488f9daf9c4.html>

Directory dependency graph for netman:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_21af483e535eeeda1b3e0ebbd7a8a7a3.html>

Directory dependency graph for include:
##### Files
| file | fileXio_rpc.h [code] |

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_21c98801a0c0c7d17001a0beb0986fce.html>

Directory dependency graph for include:
##### Files
| file | draw.h [code] |
| file | draw2d.h [code] |
| file | draw3d.h [code] |
| file | draw_blending.h [code] |
| file | draw_buffers.h [code] |
| file | draw_dithering.h [code] |
| file | draw_fog.h [code] |
| file | draw_masking.h [code] |
| file | draw_primitives.h [code] |
| file | draw_sampling.h [code] |
| file | draw_tests.h [code] |
| file | draw_types.h [code] |

---

## hdd Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_221acb9d8828939c8c28e19ee4eb114c.html>

Directory dependency graph for hdd:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_2348634bf16b768e7dee2a8a765970c1.html>

Directory dependency graph for src:
##### Files
| file | font.c [code] |
| file | scr_printf.c [code] |
| file | screenshot.c [code] |

---

## alloc Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_249e27ed47f6a2eab7da7b1ddc4f92fd.html>

Directory dependency graph for alloc:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_24c1c949c858c36913d6ba307943c059.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_25533febd014b1d004e3f813822814e7.html>

##### Files
| file | ps2mouse.h [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_2571ebee515db4e1813cfe114253807e.html>

Directory dependency graph for src:

---

## draw Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_2649a81c7f56a709216892bc1285ef27.html>

Directory dependency graph for draw:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_273f27a832f2f748f995b7326cfb9278.html>

Directory dependency graph for src:
##### Files
| file | log.c [code] |
| file | sio2man.c [code] |

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_277463bc5d441fdf9e34fcca67a1451e.html>

*(no textual content on this page)*

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_2806c30bcfe757664fc71812642581f7.html>

##### Files
| file | elf-loader.h [code] |

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_28a909d5f29a09cdabda212007cd73f7.html>

Directory dependency graph for include:
##### Directories
##### Files
| file | defs.h [code] |
| file | irx.h [code] |
| file | kerr.h [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_299fc344f3d84fb60b0cbe5f3754b3f9.html>

Directory dependency graph for src:
##### Directories

---

## string Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_2ab3a38ab7e9b371bdca8a66b280cfb7.html>

Directory dependency graph for string:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_2b17b0c67077abc3c0780a2585a106f6.html>

Directory dependency graph for src:

---

## sio2man Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_2b715144a97ae64ccc5e8147b0a5bdab.html>

Directory dependency graph for sio2man:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_2bbe6eb3d46e6950ab20e680e13bb9a2.html>

Directory dependency graph for src:
##### Files
| file | ioman_sbv.c [code] |
| file | iomanX.c [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_2cf43a9cac33627348f8ccf1a22f3e96.html>

Directory dependency graph for src:

---

## fssk Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_2df0faac20d9a51e003e7c685c1cc5dd.html>

Directory dependency graph for fssk:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_2e51deef12334dd084da5d9140b29b47.html>

Directory dependency graph for src:
##### Files
| file | fileXio_ps2sdk.c [code] |
| file | fileXio_rpc.c [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_2eb3529d6b06fd839688ef6eec3e5e84.html>

Directory dependency graph for src:

---

## sys Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_2eb8b288ff4914514e106c5451e7ae02.html>

Directory dependency graph for sys:
##### Files
| file | termios.h [code] |

---

## iop_sbusdbg Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_2f080771f6205bbf07c3b5e6545bd3fa.html>

Directory dependency graph for iop_sbusdbg:
##### Directories

---

## audsrv Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_2f702b7d905adcbb9469a6404dbe84ec.html>

Directory dependency graph for audsrv:
##### Directories

---

## gensymtab Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_2feef82756d5481f2e3fcf626f1975a7.html>

Directory dependency graph for gensymtab:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_3033a7a443f64c6f3e07e254502c7c60.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_30406d93c31043602a8c1a1e1e4c9b2e.html>

Directory dependency graph for src:
##### Files
| file | usbdpriv.h [code] |

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_30a389187753df23749947c0b14cee5f.html>

##### Files
| file | libvux.h [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_318f623de840e331e96f424145758455.html>

Directory dependency graph for src:

---

## iLinkman Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_3217d47ebe458155e7239d0a228ab153.html>

Directory dependency graph for iLinkman:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_33790995acc46d7cb7f4437dbae6c0f4.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_33ea23cd07a093e1cffe92a7ce6effba.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_3428d8daebcd806ef824f3d00ac89ba3.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_345d8429d3cb3ccd32f3e92029247ace.html>

Directory dependency graph for include:
##### Files
| file | usbd.h [code] |
| file | usbd_macro.h [code] |

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_34c191326057ba1e8020bff9b5c0b8a0.html>

*(no textual content on this page)*

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_35447b3e6ceb192e07f9d91db1c83712.html>

Directory dependency graph for src:
##### Files
| file | librm.c [code] |

---

## camera Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_354d0fe30f8451f44d30d5ee272e7643.html>

Directory dependency graph for camera:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_35627888e3e0e91a0397ea271ffc9b90.html>

Directory dependency graph for src:
##### Files
| file | ahx_rpc.c [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_35e4cd4c6b68d708ba33184e89b685ac.html>

Directory dependency graph for src:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_365d48d01aaf7da764409f739ddc76ab.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_36b98ff8a35b2ed655cbfa91e3ae73e8.html>

Directory dependency graph for include:
##### Files
| file | iop_sbusdbg.h [code] |

---

## erl-loader Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_37fa55bbac087392668600612418aa68.html>

Directory dependency graph for erl-loader:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_37ff4da14fd6396548e6fcaf9ebcf2f6.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_391aa322b736be17fe3bb7d416d9cac3.html>

Directory dependency graph for src:

---

## input Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_39941762bcf6eb45f8acbe5afd6e1dcf.html>

Directory dependency graph for input:
##### Directories

---

## smbman Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_39d17f469530f79363f6574f3e93b68d.html>

Directory dependency graph for smbman:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_3a7a010c28010a16f6513751c6839763.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_3a8354039741e2cc6ac7389e05536610.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_3a96145256e208ba8e54b2dc9687859a.html>

Directory dependency graph for include:
##### Files
| file | font.h [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_3a9c6fe855c5d1af04ce6ee63ecedf2c.html>

Directory dependency graph for src:

---

## sdrdrv Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_3aa0035d36047302fc2eb81337a6a532.html>

Directory dependency graph for sdrdrv:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_3b98ff2c691c6f2c545fcc182457325d.html>

##### Files
| file | libpwroff.h [code] |
|  | Power-off library. |

---

## IEEE1394_bd Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_3bc9c0aee413f19edf678d71a08ea153.html>

Directory dependency graph for IEEE1394_bd:
##### Directories

---

## libspu2 Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_3bdb928cbd5acb3c07c5155022fcf7d7.html>

Directory dependency graph for libspu2:
##### Directories

---

## sbv Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_3c99d3595cafa99f0e2683197c97edf9.html>

Directory dependency graph for sbv:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_3cc6d9732948698af21c8f45bed58010.html>

Directory dependency graph for src:
##### Directories

---

## apa Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_3cf15560dfc813cf049b4197fff2fad4.html>

Directory dependency graph for apa:
##### Directories

---

## filexio Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_3d3c25f590b74dfbd50a8b02c417c665.html>

Directory dependency graph for filexio:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_3d497bebe21502a336cf5c633aa734d5.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_3df15571f2d889d39f44f0244a444c2b.html>

Directory dependency graph for src:
##### Files
| file | ps2cam.c [code] |

---

## acatad Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_3e33cc838f00d2e02fc45a4479cb1f60.html>

Directory dependency graph for acatad:
##### Directories

---

## acmeme Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_3e86b8adf38d0f4d7eedc40eae73f90a.html>

Directory dependency graph for acmeme:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_3ecaac98bf4a7074230173a0d41eeb7f.html>

##### Files
| file | romdrv.h [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_3edd3adbbfdd3f9c0a2ba29f35e4fb40.html>

Directory dependency graph for src:

---

## acfpgald Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_3f94e3a7ba0cb8dddc276738ef412c16.html>

Directory dependency graph for acfpgald:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_3f98625ebb06f42a01468b7a037d1337.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_3ff72236a21ffe4b52e3a463ca2d6474.html>

Directory dependency graph for src:

---

## subfile Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_404b9ec8288863f6b21c74e0ce16c047.html>

Directory dependency graph for subfile:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_40981f36b04c31e4ddb6678e354ab389.html>

Directory dependency graph for src:

---

## system Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_40ac35421bc63b72c26b6c69b1517fd6.html>

Directory dependency graph for system:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_40c561062edbd99ebfb63c3ad64cebed.html>

*(no textual content on this page)*

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_410b7125f3dcf88f57abb0970a4bbcbf.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_413ea6b66ae557d0d7cb038b88135642.html>

Directory dependency graph for include:
##### Files
| file | libmpeg.h [code] |

---

## srxfixup Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_4219d2c0f6303884499173a28a74746a.html>

Directory dependency graph for srxfixup:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_4235aca40d92d2d6923267ff8588d97a.html>

Directory dependency graph for include:
##### Files
| file | sbv_patches.h [code] |
| file | slib.h [code] |
| file | smem.h [code] |
| file | smod.h [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_424b5f4939962cf017e03cf59eafb723.html>

Directory dependency graph for src:
##### Files
| file | ioman.c [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_4304e6a09d2ca52231132d217435644b.html>

Directory dependency graph for src:
##### Files
| file | adpcm.c [code] |
| file | audsrv.c [code] |
| file | audsrv_internal.h [code] |
| file | cdrom.c [code] |
| file | cdrom.h [code] |
| file | common.c [code] |
| file | common.h [code] |
| file | hw.h [code] |
| file | rpc_client.h [code] |
| file | rpc_server.c [code] |
| file | rpc_server.h [code] |
| file | spu.h [code] |
| file | upsamplers.c [code] |
| file | upsamplers.h [code] |

---

## ioptrap Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_43255a50c3a5642889795edf08bb8408.html>

Directory dependency graph for ioptrap:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_4348197a43cefe9746e12a9e8b89bb8b.html>

*(no textual content on this page)*

---

## sysmem Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_44719da65bb992f08c8ee8632a1136c7.html>

Directory dependency graph for sysmem:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_44a3b09642b338b60501cc0d22aa7c4d.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_457a51f410f9bf085893b4d5cb4aa8ef.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_465291803e00dfefa1e1a83db7deacb1.html>

##### Files
| file | fls.h [code] |

---

## rspu2drv Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_46f718c737dc136fbfd1d21209bd1e7f.html>

Directory dependency graph for rspu2drv:
##### Directories

---

## ps2adpcm Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_47818b46b1cf08114dcb647bd070ea80.html>

Directory dependency graph for ps2adpcm:
##### Directories

---

## accdvde Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_4802f7d95fb602d0291cc88043ed0216.html>

Directory dependency graph for accdvde:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_48185d4162af4b76c95e522da1e1d975.html>

Directory dependency graph for src:
##### Files
| file | internal.h [code] |
| file | libcdvd.c [code] |
| file | ncmd.c [code] |
| file | scmd.c [code] |

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_48c6b85e120a8bbf6e2a405ed1701c1a.html>

Directory dependency graph for include:
##### Files
| file | poweroff.h [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_48cc7f642712205fa02db4fa927ae7fc.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_49651291c8708643fe3704a6e4ba269d.html>

Directory dependency graph for src:
##### Files
| file | freepad.c [code] |
| file | freepad.h [code] |
| file | padCmds.c [code] |
| file | padCmds.h [code] |
| file | padData.c [code] |
| file | padData.h [code] |
| file | padInit.c [code] |
| file | padMiscFuncs.c [code] |
| file | padPortOpen.c [code] |
| file | rpcserver.c [code] |
| file | rpcserver.h [code] |
| file | sio2Cmds.c [code] |
| file | sio2Cmds.h [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_49702882664caafb69d7373eb6fcc470.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_4974e182f13b0e90631ab347bf0c5323.html>

*(no textual content on this page)*

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_49800e59bafb3f4d3e12b3e0b3d6dc48.html>

Directory dependency graph for include:
##### Files
| file | sbusintr.h [code] |

---

## ahx Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_4aa16fa050235bfcc2447f6060318e0e.html>

Directory dependency graph for ahx:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_4aa3f641574c4329e5ed721597730e1e.html>

Directory dependency graph for include:
##### Files
| file | bdm.h [code] |

---

## bin2c Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_4aa7630bf94b1e948c1a72cd18b9557b.html>

Directory dependency graph for bin2c:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_4ac27e15e8009e434c98c966b6c4f83e.html>

*(no textual content on this page)*

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_4b07fc6c87685f1b9fec8d385a07b704.html>

Directory dependency graph for src:
##### Files
| file | fdman.c [code] |
| file | init.c [code] |
| file | lock.c [code] |
| file | ps2sdkapi.c [code] |
| file | rtc.c [code] |
| file | sjis.c [code] |
| file | sleep.c [code] |
| file | timezone.c [code] |

---

## sbusintr Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_4bae4802256ab45fc18d13b3c6375605.html>

Directory dependency graph for sbusintr:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_4bcab64f02c9afa07f251ccf509f359c.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_4bea4738b41f5b6c7a7d9f127adc10f0.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_4e78fb665b6edbed0f7a13a393f2c1a3.html>

Directory dependency graph for include:
##### Files
| file | dma.h [code] |
| file | dma_registers.h [code] |
| file | dma_tags.h [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_4ecf5ddff8bf76922e66af8136c8ed02.html>

Directory dependency graph for src:
##### Files
| file | fileXio_iop.c [code] |

---

## tools Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_4eeb864c4eec08c7d6b9d3b0352cfdde.html>

Directory dependency graph for tools:

---

## multitap Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_4fe02c3598ec986dac9823d5144e53a1.html>

Directory dependency graph for multitap:
##### Directories

---

## acjv Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_50d3aa1cb52f1ed06631164a65eecb46.html>

Directory dependency graph for acjv:
##### Directories

---

## adddrv Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_511aea66b1e7cdedbb181e4504632afe.html>

Directory dependency graph for adddrv:
##### Directories

---

## libprofglue Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_511ffd3230153c1a97c9d908d233380d.html>

Directory dependency graph for libprofglue:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_514e17767bb30ba07d1dfde9b71de206.html>

Directory dependency graph for src:

---

## osdsrc Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_51b4fd419f5cef2df1fa20f57f0c92da.html>

Directory dependency graph for osdsrc:
##### Directories

---

## sys Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_51f393a161ada3120603c40b1f44207f.html>

Directory dependency graph for sys:
##### Files
| file | ioctl.h [code] |

---

## netcnfif Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_5221eff48c49182d9326bbebad1b24c6.html>

Directory dependency graph for netcnfif:
##### Directories

---

## memorycard Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_52af18bf396be92337d4eeddb9a1740b.html>

Directory dependency graph for memorycard:
##### Directories

---

## machine Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_52b517ede27dad439198e3fb326d5f5e.html>

Directory dependency graph for machine:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_535a26643990b2aae7c4085335cb5fe3.html>

Directory dependency graph for include:
##### Files
| file | usbhdfsd.h [code] |

---

## acsram Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_537c1a5f31ee55d93fbd41130c9584dc.html>

Directory dependency graph for acsram:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_53ad030f333c935e5c167b0ea2eb5f9b.html>

Directory dependency graph for src:

---

## libvux Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_53afae995724263ef157d83ff8fe3fe4.html>

Directory dependency graph for libvux:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_54d42e7ac0c8c9b0bd3fe2b073c61af7.html>

Directory dependency graph for include:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_558a024a0ed10ce4a9f4d947b2e1a991.html>

Directory dependency graph for src:

---

## dvripl Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_55b81c7b0811889843fb7d99073d4918.html>

Directory dependency graph for dvripl:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_55de3dde79234ee6800af66dd2b2efb1.html>

Directory dependency graph for include:
##### Files
| file | mcman.h [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_5679162401fbcaa032643186726d7931.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_56c96d436b95cd5650376ca3df086363.html>

Directory dependency graph for src:
##### Files
| file | pipe.c [code] |

---

## pad Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_5799e6857a1212b105de941c1bfdc588.html>

Directory dependency graph for pad:
##### Directories

---

## memorycard Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_5805bfcfbe100e4767f47461b3e6402b.html>

Directory dependency graph for memorycard:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_58692563475c8582953c11bc1da04f9e.html>

Directory dependency graph for include:
##### Files
| file | dev9.h [code] |

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_587f58ae6bff4b1360d4911800bd5f72.html>

##### Files
| file | graph.h [code] |
| file | graph_config.h [code] |
| file | graph_vram.h [code] |

---

## sbus Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_58a8fc8f1a03774579661b06bb97dd1a.html>

Directory dependency graph for sbus:
##### Directories

---

## s147mdev Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_58e31a5d2ae5137ed065a2438731004f.html>

Directory dependency graph for s147mdev:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_59876a643fc90dc01f8619910869c249.html>

Directory dependency graph for include:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_59a6ec5db7b7dbaae5b63f59483095d4.html>

*(no textual content on this page)*

---

## mpeg Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_5a30d30e86afe8e71e8256ba8d77d003.html>

Directory dependency graph for mpeg:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_5adc6e0e6d24a5d34469112c0267949c.html>

Directory dependency graph for src:

---

## rpc Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_5b119dc963fa9b25ef41951231899460.html>

Directory dependency graph for rpc:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_5b54603b8242cba98124b6b7116aed85.html>

Directory dependency graph for src:

---

## libpfs Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_5b638697113ca3fae3dbb2942f3ebff2.html>

Directory dependency graph for libpfs:
##### Directories

---

## heaplib Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_5b8198e02a40a72d2abec04f62d1fd43.html>

Directory dependency graph for heaplib:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_5c70caa0b94395675119bf3ed52b9ab8.html>

Directory dependency graph for include:
##### Files
| file | libkbd.h [code] |
| file | ps2kbd.h [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_5d316d15cd77caf7e3d96de601896449.html>

Directory dependency graph for src:
##### Files
| file | ps2mouse.c [code] |

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_5dc1218e3fbe6447e9a0ef568f079980.html>

##### Files
| file | iopcontrol_special.h [code] |

---

## newlib Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_5e6d19e02aff7b7ecdcee2b32d4e4d69.html>

Directory dependency graph for newlib:

---

## boardinf Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_5ec8cbed913f77dce8be99aba816b4e2.html>

Directory dependency graph for boardinf:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_5fac0142058176777a206f411a269586.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_60b37a5e5d239c959d748ecb9bc4d345.html>

Directory dependency graph for include:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_60b92096f37991a4061e29e96b6ea950.html>

Directory dependency graph for include:
##### Files
| file | ee_debug.h [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_60c0b0581c07fba9514a94139971315c.html>

Directory dependency graph for src:
##### Files
| file | eedebug_defs.h [code] |

---

## vblank Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_60f7c75aab99249ed9879339d7562ada.html>

Directory dependency graph for vblank:
##### Directories

---

## sio Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_6133ef156cce03413acfdeebec722ba1.html>

Directory dependency graph for sio:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_6198a94c6409eda66b1bd48a967d0514.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_62fec4584208731863c4d71a1afb4f5e.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_63f4f3a4e1ed51b283da57602199373c.html>

Directory dependency graph for include:
##### Files
| file | ps2ip.h [code] |

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_641b55ca6dd3a94a9d2f54c39a5f1aa3.html>

Directory dependency graph for include:
##### Files
| file | atad.h [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_649ece9c59c1ccd3cc9fc0658b53f87d.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_649efdce889a9164ac5e894f2ff13a76.html>

Directory dependency graph for src:
##### Files
| file | ps2kbd.c [code] |
| file | us_keymap.h [code] |

---

## tests Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_64d4a519d213c2c63a5ddfe35029a653.html>

Directory dependency graph for tests:
##### Directories

---

## eedebug Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_650207f478e190855aca53e9453b1a94.html>

Directory dependency graph for eedebug:
##### Directories

---

## security Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_65b0066184b118a668041f55a1e77c0f.html>

Directory dependency graph for security:
##### Directories
| directory | secrman |
| directory | secrsif |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_65e2eb5cf23fa8836ba56dbe0c705175.html>

Directory dependency graph for src:
##### Files
| file | fakehost.c [code] |
| file | nprintf.c [code] |

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_660bfe733945cea18d05bf7eea32d232.html>

##### Files
| file | audsrv.h [code] |

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_6626ad1ade24955741d807414843f429.html>

*(no textual content on this page)*

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_6688fa9908affc4d334571bbc03eaee9.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_674d4bf0891c267e7e23627b72783290.html>

Directory dependency graph for src:
##### Files
| file | libmtap.c [code] |

---

## machine Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_67b2c9c050fe7ff1951c6b85ae729a71.html>

Directory dependency graph for machine:
##### Directories

---

## kernel Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_694ec83a64f58cbdefbefce65cd1011c.html>

Directory dependency graph for kernel:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_697e079727c0d4c73a79472c13971083.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_698b81740f3d5006362b5cbe81359408.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_69cf9eba4292ca384eb404f09e7842a3.html>

Directory dependency graph for include:
##### Files
| file | iomanX.h [code] |

---

## font Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_6a18a5fb12cb9e6be5f051ff6b53d12a.html>

Directory dependency graph for font:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_6a3670c15e32956093e6f2ed3680cbc0.html>

Directory dependency graph for include:
##### Files
| file | alloc.h [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_6ad7f2ab8ef00bea214c65f3ba81f481.html>

Directory dependency graph for src:
##### Files
| file | ps2dev9.c [code] |

---

## filexio Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_6b1fe306776c19ae02b5b1275d4c63ec.html>

Directory dependency graph for filexio:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_6b3a3a5d267f0fea31b7a7f9b7d2beaf.html>

Directory dependency graph for src:
##### Directories
| directory | embeddedartistry_libc |
| directory | musl |
| directory | newlib |

---

## spduart Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_6bcb0fd5e733f1a80749b2e929f95b9a.html>

Directory dependency graph for spduart:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_6bfe454f00a9ae0a35a711fd5ea16f8c.html>

Directory dependency graph for src:
##### Files
| file | alloc.c [code] |

---

## mouse Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_6c36fa94566b53a53d1b33c49cbff7fb.html>

Directory dependency graph for mouse:
##### Directories

---

## poweroff Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_6c63d3a31e7cac2d832eb76295920122.html>

Directory dependency graph for poweroff:
##### Directories

---

## IEEE1394_disk Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_6ca9d86174d61418b8e0fc2b61cd84c1.html>

Directory dependency graph for IEEE1394_disk:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_6cc1d0983affcb72bbae6e53cb3c97f1.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_6dae2d9a37ea67072c02f1156a06c4ec.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_6dfc7f2de77774155f50e8637d69a505.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_6dfd448eafa07cba6cecfd41ce373157.html>

Directory dependency graph for include:
##### Files
| file | ioman.h [code] |
| file | ioman_mod.h [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_6ea41b5b43554e915c7a075face66b06.html>

Directory dependency graph for src:
##### Files
| file | devfs.c [code] |

---

## fakehost Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_6ec8af8771869123149626592b760e4b.html>

Directory dependency graph for fakehost:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_6eea34e18c64762ff7f8ff55dfecf941.html>

*(no textual content on this page)*

---

## dev9 Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_6f16cad81de2453a6f48c5e272ba4a18.html>

Directory dependency graph for dev9:

---

## reboot Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_6f170e5d4e2c7a590428c890b6770715.html>

Directory dependency graph for reboot:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_6f34e666724a9a843f952a9b1fa7880b.html>

Directory dependency graph for src:
##### Files
| file | audsrv_rpc.c [code] |
| file | audsrv_rpc.h [code] |

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_6fd08c545c881b4d2b356c02a10aa6b3.html>

*(no textual content on this page)*

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_6ff4c5f15c2219ca21327ddbc0ba9850.html>

*(no textual content on this page)*

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_702336a0435434f6b8cf6e517dc2db4d.html>

Directory dependency graph for src:
##### Directories

---

## deckard Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_7183b37c369e4a38814ada922784ddfa.html>

Directory dependency graph for deckard:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_71bd830da3b128f94f4da5847e7d6fcb.html>

Directory dependency graph for src:
##### Files
| file | byteorder.h [code] |
| file | devscan.c [code] |
| file | devscan.h [code] |
| file | ps2_fio.c [code] |
| file | ps2_fio.h [code] |
| file | ps2fs.h [code] |
| file | ps2netfs.c [code] |

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_71fde4f0207fc0e816aa54ff3c3cace1.html>

Directory dependency graph for include:
##### Files
| file | ps2_sbus.h [code] |

---

## s147nand Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_725c2a76e1b3597c05dc69f4285c4eb8.html>

Directory dependency graph for s147nand:
##### Directories

---

## acuart Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_7268553a12e6a8f82f5fa90127c455c6.html>

Directory dependency graph for acuart:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_72fd2ca65a98aa6f116e0a45d1317c83.html>

Directory dependency graph for src:
##### Directories
##### Files
| file | ps2ip.c [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_738e6c3ecf4bac81e89a6d577702e070.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_73dce0403f7a76ba0287e52bc234423f.html>

Directory dependency graph for include:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_73fb5736705d41bde0e686b372d7e351.html>

Directory dependency graph for src:

---

## intrman Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_7422a0894415a12ccd1d562a8ad09f2d.html>

Directory dependency graph for intrman:
##### Directories

---

## libapa Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_74c6a9c949eb32128aa5a6adc613f35b.html>

Directory dependency graph for libapa:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_752d63180ca3e6100001131e79733bcb.html>

Directory dependency graph for include:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_754b202cb4f9b24a6deb35fb6a704912.html>

*(no textual content on this page)*

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_76a31671fd11daaeda5d19d9c5f3313b.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_76c0ea988611758bf556e82d119dc5f5.html>

Directory dependency graph for include:
##### Files
| file | libmc.h [code] |

---

## embeddedartistry_libc Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_76f6712385aad5f71054d252dc76d79e.html>

Directory dependency graph for embeddedartistry_libc:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_77f726fe8e3a252d97c01a812608e9e2.html>

Directory dependency graph for include:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_78d8e4304e0da60e345c03079cd31955.html>

Directory dependency graph for include:

---

## rmreset Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_797db46b62803b3c61428b9ee622e041.html>

Directory dependency graph for rmreset:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_79cc41b78d650d94271256f66f3b3a8f.html>

Directory dependency graph for include:
##### Files
| file | bd_cache.h [code] |
| file | bd_defrag.h [code] |

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_7a30004114210d8a58166e09a9078b00.html>

##### Files
| file | sior_rpc.h [code] |

---

## romimg Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_7a9487a4ac2fac09687c40a3e41e5ece.html>

Directory dependency graph for romimg:
##### Directories

---

## adpenc Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_7ae3e066c48cbf1e456bf7b5af53fbfa.html>

Directory dependency graph for adpenc:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_7b24259007ae4a691b1d64f87af8425d.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_7ba9d505bd1ee82cf81eef47633068e9.html>

Directory dependency graph for src:

---

## libc Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_7ce330b52aeb23b4ce737d3f4b393244.html>

Directory dependency graph for libc:

---

## xparam Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_7cf5eb5a2c48355b2440a9966a07daac.html>

Directory dependency graph for xparam:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_7d0a621685e4738f4449cb73774f552c.html>

Directory dependency graph for src:
##### Files
| file | ps2ip.c [code] |

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_7d211158700cf4b9e7ab76ef88fd6011.html>

Directory dependency graph for include:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_7deb1e7c7f2a31ef848b115fdbd89def.html>

Directory dependency graph for src:

---

## hdpro_atad Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_7e10c943c08a69732df0d9710348ffa0.html>

Directory dependency graph for hdpro_atad:
##### Directories

---

## smap Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_7e8098252786d103c47acfa14c0859f4.html>

Directory dependency graph for smap:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_7ea4ab416d8e3e8b817386f3fccc52c9.html>

Directory dependency graph for src:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_7f629dfb5bddaac9a0e91bf56b6d3731.html>

Directory dependency graph for include:
##### Files
| file | libsd.h [code] |
| file | spu2regs.h [code] |

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_7fe979218212ccd9b615f44ceca681f9.html>

Directory dependency graph for include:
##### Directories
##### Files
| file | stdlib.h [code] |

---

## ioprpgen Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_7ffa00d7677efd57051c764ddd3b028e.html>

Directory dependency graph for ioprpgen:
##### Directories

---

## acflash Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_80f6da64465a1795342f9b5f13be8909.html>

Directory dependency graph for acflash:
##### Directories

---

## netcnf Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_833c310e0e857a1c07a064dc981f4d4d.html>

Directory dependency graph for netcnf:
##### Directories

---

## arcade Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_83706370b12deb47497ed91304cced4b.html>

Directory dependency graph for arcade:

---

## sound Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_838e88315325ec0d843359dcae22d639.html>

Directory dependency graph for sound:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_840d45e55d4a7bd01c453be7ad942e0e.html>

Directory dependency graph for include:

---

## mcserv Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_841d05e6e469c6e67dc741c932691089.html>

Directory dependency graph for mcserv:
##### Directories

---

## debug Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_8494d76ae2586079db82d45fe3dd6aec.html>

Directory dependency graph for debug:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_8537469ca2583b39b1def51c0becc649.html>

*(no textual content on this page)*

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_8599489b2aeb3113307eaa3156921889.html>

Directory dependency graph for src:
##### Files
| file | freemtap.c [code] |
| file | freemtap.h [code] |
| file | rpcservers.c [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_85ced1b8f6efd1ca0ed52ab82124f15c.html>

Directory dependency graph for src:
##### Files
| file | libpad.c [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_8633b8e760ba4c3acaa1842d703e990f.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_867cf3572160928cd3d771e065cbcda5.html>

Directory dependency graph for include:
##### Files
| file | intrman.h [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_877a24e332e8fb1301c97400aa573f28.html>

Directory dependency graph for src:

---

## modload Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_87c98c5970299b04095b64caaae46c44.html>

Directory dependency graph for modload:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_8806379264ffea16411011c87cd5d5d1.html>

##### Files
| file | ahx.h [code] |

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_881b1332c24d49df8de53b62db8f32cd.html>

Directory dependency graph for include:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_889111e6013952a2fadab5588c28433a.html>

Directory dependency graph for include:
##### Files
| file | libhdd.h [code] |

---

## sdhd Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_88aaed4afc7023eb90012be638e1ff48.html>

Directory dependency graph for sdhd:
##### Directories

---

## s147netb Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_895fc664e901f3249c2045cb4206a7bf.html>

Directory dependency graph for s147netb:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_899cd3c0131c820f355da9f217e83d0e.html>

Directory dependency graph for include:
##### Files
| file | sifman.h [code] |

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_8a6a67431f985d69787ebf051412922f.html>

Directory dependency graph for include:
##### Files
| file | deci2.h [code] |
| file | fileio.h [code] |
| file | iopcontrol.h [code] |
| file | iopheap.h [code] |
| file | kernel.h [code] |
| file | kernel_util.h [code] |
| file | loadfile.h [code] |
| file | osd_config.h [code] |
| file | rom0_info.h [code] |
| file | sifcmd.h [code] |
| file | sifdma.h [code] |
| file | sifrpc.h [code] |
| file | sio.h [code] |
| file | syscallnr.h [code] |
| file | timer.h [code] |
| file | tty.h [code] |

---

## accore Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_8c41b7aa740fda79cdc4490331cf7b7d.html>

Directory dependency graph for accore:
##### Directories

---

## dir.c

Page: <https://ps2dev.github.io/ps2sdk/dir_8c_source.html>

```
/*
# _____     ___ ____     ___ ____
#  ____|   |    ____|   |        | |____|
# |     ___|   |____ ___|    ____| |    \    PS2DEV Open Source Project.
#-----------------------------------------------------------------------
# Copyright 2001-2004, ps2dev - http://www.ps2dev.org
# Licenced under Academic Free License version 2.0
# Review ps2sdk README & LICENSE files for further details.
#
# PFS directory parsing routines
*/

#include <errno.h>
#include <stdio.h>
#ifdef _IOP
#include <sysclib.h>
#else
#include <string.h>
#endif
#include <iomanX.h>

#include "libpfs.h"

extern u32 pfsMetaSize;

// Gets a dir entry from the inode specified by clink
pfs_cache_t *pfsGetDentry(pfs_cache_t *clink, char *path, pfs_dentry_t **dentry, u32 *size, int option)
{
    pfs_blockpos_t block_pos;
    pfs_dentry_t *d;
    u16 aLen;
    pfs_dentry_t *d2;
    pfs_cache_t *dentCache;
    u32 new_dentryLen=0,dentryLen;
    int len=0, result;

    if (path)
    {
        len = strlen(path);
        new_dentryLen = (len+8+3) &~3;
    }
    *size = 0;

    block_pos.inode = pfsCacheUsedAdd(clink);
    block_pos.block_segment = 1;
    block_pos.block_offset = 0;
    block_pos.byte_offset = 0;
    dentCache = pfsGetDentriesChunk(&block_pos, &result);

    if (dentCache != NULL)
    {
        d2=d=dentCache->u.dentry;
        while(*size < clink->u.inode->size)
        {
            // Read another dentry chunk if we need to
            if (d2 >= (pfs_dentry_t*)((u8*)dentCache->u.inode + pfsMetaSize))
            {
                if (pfsInodeSync(&block_pos, pfsMetaSize, clink->u.inode->number_data))
                    break;
                pfsCacheFree(dentCache);

                if ((dentCache=pfsGetDentriesChunk(&block_pos, &result)) == NULL)
                    break;
                d=dentCache->u.dentry;
            }

            // Scan through the sector.
            for (d2=(pfs_dentry_t*)((u8*)d+512); d < d2; d=(pfs_dentry_t *)((u8*)d + aLen))
            {
                aLen=(d->aLen & 0xFFF);

                if (aLen & 3){
                    PFS_PRINTF(PFS_DRV_NAME": Error: dentry allocated length/4 != 0\n");
                    goto _exit;
                }
                dentryLen = (d->pLen + 8 + 3) & 0x1FC;
                if (aLen < dentryLen){
                    PFS_PRINTF(PFS_DRV_NAME": Error: dentry is too small\n");
                    goto _exit;
                }
                if (d2 < (pfs_dentry_t*)((u8*)d + aLen)){
                    PFS_PRINTF(PFS_DRV_NAME": Error: dentry across sectors\n");
                    goto _exit;
                }

                // decide if the current dentry meets the required criteria, based on 'option'
                switch(option)
                {
                    case 0: // result = 1 when paths are equal
                        result = (len==d->pLen) && (memcmp(path, d->path, d->pLen)==0);
                        break;
                    case 1: // result = 1 when either there is no inode or if there is enough space remaining in the inode.
                        result = ((d->inode) || (aLen < new_dentryLen)) ? (aLen - dentryLen
                                >= new_dentryLen) : 1;
                        break;
                    case 2: // result = 1 when dir path is not empty, "." or ".."
                        result = d->pLen && strcmp(d->path, ".") && strcmp(d->path, "..");
                        break;
                    default:
                        goto _exit;
                }

                if (result)
                {
                    *dentry=d;
                    pfsCacheFree(block_pos.inode);
                    return dentCache;
                }
                *size+=aLen;
            }
        }
_exit:      pfsCacheFree(dentCache);
    }
    pfsCacheFree(block_pos.inode);
    return NULL;
}

int pfsGetNextDentry(pfs_cache_t *clink, pfs_blockpos_t *blockpos, u32 *position, char *name, pfs_blockinfo_t *bi)
{
    int result;
    pfs_dentry_t *dentry;
    u32 len=0;

    // loop until a non-empty entry is found or until the end of the dentry chunk is reached
    while((len == 0) && (*position < clink->u.inode->size))
    {
        pfs_cache_t *dcache;

        if (!(dcache=pfsGetDentriesChunk(blockpos, &result)))
        {
            PFS_PRINTF(PFS_DRV_NAME": couldnt get dentries chunk for dread!\n");
            break;
        }

        dentry = (pfs_dentry_t*)((u8*)dcache->u.data + (blockpos->byte_offset % pfsMetaSize));

        len = dentry->pLen;
        memcpy(name, dentry->path, len);
        name[len] = '\0';

        bi->subpart = dentry->sub;
        bi->number = dentry->inode;
        pfsCacheFree(dcache);

        *position += dentry->aLen & 0xFFF;

        // update blockpos
        if (pfsInodeSync(blockpos, dentry->aLen & 0xFFF, clink->u.inode->number_data))
            break;
    }

    return len;
}

pfs_cache_t *pfsFillDentry(pfs_cache_t *clink, pfs_dentry_t *dentry, char *path1, pfs_blockinfo_t *bi, u32 len, u16 mode)
{
    dentry->inode=bi->number;
    dentry->sub=(u8)bi->subpart;
    dentry->pLen=strlen(path1);
    dentry->aLen=len | (mode & FIO_S_IFMT);
    memcpy(dentry->path, path1, dentry->pLen & 0xFF);

    return clink;
}

pfs_cache_t *pfsDirAddEntry(pfs_cache_t *dir, char *filename, pfs_blockinfo_t *bi, u16 mode, int *result)
{
    pfs_dentry_t *dentry;
    u32 size;
    u32 len;
    pfs_cache_t *dcache;

    dcache=pfsGetDentry(dir, filename, &dentry, &size, 1);
    if (dcache != NULL){
        len=dentry->aLen & 0xFFF;
        if (dentry->pLen)
            len-=(dentry->pLen + 11) & 0x1FC;
        dentry->aLen=(dentry->aLen & FIO_S_IFMT) | ((dentry->aLen & 0xFFF) - len);
        dentry=(pfs_dentry_t *)((u8*)dentry + (dentry->aLen & 0xFFF));
    }else{
        int offset;

        if ((*result=pfsAllocZones(dir, sizeof(pfs_dentry_t), 0))<0)
            return NULL;
        dcache=pfsGetDentriesAtPos(dir, dir->u.inode->size, &offset, result);
        if (dcache==NULL)
            return NULL;

        dir->u.inode->size += sizeof(pfs_dentry_t);

        dentry=(pfs_dentry_t*)((u8*)dcache->u.dentry+offset);
        len=sizeof(pfs_dentry_t);
    }
    return pfsFillDentry(dcache, dentry, filename, bi, len, mode);
}

pfs_cache_t *pfsDirRemoveEntry(pfs_cache_t *clink, char *path)
{
    pfs_dentry_t *dentry;
    u32 size;
    u16 aLen;
    pfs_dentry_t *dlast=NULL, *dnext;
    pfs_cache_t *c;

    if ((c=pfsGetDentry(clink, path, &dentry, &size, 0)) != NULL){
        int i=0, val;

        val=(u8*)dentry-(u8*)c->u.dentry;
        if (val<0)  val +=511;
        val /=512;
        val *=512;

        dnext=(pfs_dentry_t*)((u8*)c->u.dentry+val);
        do{
            aLen = dnext->aLen & 0xFFF;

            if (dnext==dentry){
                if (dlast)
                    dlast->aLen=(dlast->aLen & FIO_S_IFMT) | ((dlast->aLen & 0xFFF) + aLen);
                else{
                    dnext->inode=0;
                    dnext->pLen=0;

                    if (size+aLen >= clink->u.inode->size)
                            clink->u.inode->size -= aLen;
                }
                return c;
            }
            i+=aLen;
            dlast=dnext;
            dnext=(pfs_dentry_t *)((u8*)dnext + aLen);
        }while (i<512);
    }
    return NULL;
}

int pfsCheckDirForFiles(pfs_cache_t *clink)
{
    pfs_dentry_t *dentry;
    pfs_cache_t *dcache;
    u32 size;

    if((dcache=pfsGetDentry(clink, NULL, &dentry, &size, 2))){
        pfsCacheFree(dcache);
        return 0;
    }
    return 1;
}

void pfsFillSelfAndParentDentries(pfs_cache_t *clink, pfs_blockinfo_t *self, pfs_blockinfo_t *parent)
{
    pfs_dentry_t *dentry=clink->u.dentry;

    memset(dentry, 0, pfsMetaSize);
    dentry->inode=self->number;
    dentry->path[0]='.';
    dentry->path[1]='\0';
    dentry->sub=(u8)self->subpart;
    dentry->pLen=1;
    dentry->aLen=12 | FIO_S_IFDIR;

    dentry=(pfs_dentry_t *)((u8*)dentry + 12);

    dentry->inode=parent->number;
    dentry->path[0]='.';
    dentry->path[1]='.';
    dentry->path[2]='\0';
    dentry->sub=(u8)parent->subpart;
    dentry->pLen=2;
    dentry->aLen=500 | FIO_S_IFDIR;
}

pfs_cache_t* pfsSetDentryParent(pfs_cache_t *clink, pfs_blockinfo_t *bi, int *result)
{
    int offset;
    pfs_cache_t *dcache;

    dcache=pfsGetDentriesAtPos(clink, 0, &offset, result);
    if (dcache){
        pfs_dentry_t *d=(pfs_dentry_t*)(12+(u8*)dcache->u.data);
        d->inode=bi->number;
        d->sub  =(u8)bi->subpart;
    }
    return dcache;
}

// Returns the cached inode for the file (dir) in the directory pointed
// to by the dir inode.
pfs_cache_t *pfsInodeGetFileInDir(pfs_cache_t *dirInode, char *path, int *result)
{
    pfs_dentry_t *dentry;
    u32 size;
    pfs_cache_t *clink;

    if (path[0]==0)
        return pfsCacheUsedAdd(dirInode);

    // If we're in the root dir, don't do anything for ".."
    if ((dirInode->block ==
         dirInode->pfsMount->root_dir.number << dirInode->pfsMount->inode_scale) &&
        (dirInode->sub    == dirInode->pfsMount->root_dir.subpart) &&
        (strcmp(path, "..") == 0))
        return pfsCacheUsedAdd(dirInode);

    if ((*result=pfsCheckAccess(dirInode, 1)) < 0)
        return NULL;

    // Get dentry of file/dir specified by path from the dir pointed to
    // by the inode (dirInode). Then return the cached inode for that dentry.
    if ((clink=pfsGetDentry(dirInode, path, &dentry, &size, 0))){
        pfsCacheFree(clink);
        return pfsInodeGetData(dirInode->pfsMount,
            dentry->sub, dentry->inode, result);
    }

    *result=-ENOENT;
    return NULL;
}

pfs_cache_t *pfsInodeGetFile(pfs_mount_t *pfsMount, pfs_cache_t *clink,
            const char *name, int *result) {
    char path[256];
    pfs_cache_t *c;

    c=pfsInodeGetParent(pfsMount, clink, name, path, result);
    if (c){
        pfs_cache_t *fileInode;

        fileInode=pfsInodeGetFileInDir(c, path, result);
        pfsCacheFree(c);
        return fileInode;
    }
    return NULL;
}

void pfsInodeFill(pfs_cache_t *ci, pfs_blockinfo_t *bi, u16 mode, u16 uid, u16 gid)
{
    u32 val;

    memset(ci->u.inode, 0, pfsMetaSize);

    ci->u.inode->magic=PFS_SEGD_MAGIC;

    ci->u.inode->inode_block.number=bi->number;
    ci->u.inode->inode_block.subpart=bi->subpart;
    ci->u.inode->inode_block.count=bi->count;

    ci->u.inode->last_segment.number=bi->number;
    ci->u.inode->last_segment.subpart=bi->subpart;
    ci->u.inode->last_segment.count=bi->count;

    ci->u.inode->mode=mode;
    ci->u.inode->uid=uid;
    ci->u.inode->gid=gid;

    if ((mode & FIO_S_IFMT) == FIO_S_IFDIR){
        ci->u.inode->attr=0xA0;
        ci->u.inode->size=sizeof(pfs_dentry_t);
        val=2;
    }else{
        ci->u.inode->size=0;
        val=1;
    }
    ci->u.inode->number_data=val;
    ci->u.inode->number_blocks=val;

    pfsGetTime(&ci->u.inode->ctime);
    memcpy(&ci->u.inode->atime, &ci->u.inode->ctime, sizeof(pfs_datetime_t));
    memcpy(&ci->u.inode->mtime, &ci->u.inode->ctime, sizeof(pfs_datetime_t));

    ci->u.inode->number_segdesg=1;
    ci->u.inode->data[0].number =bi->number;
    ci->u.inode->data[0].subpart=bi->subpart;
    ci->u.inode->data[0].count  =bi->count;

    ci->u.inode->subpart=bi->subpart;

    ci->flags |= PFS_CACHE_FLAG_DIRTY;
}

// Given a path, this function will return the inode for the directory which holds
// the file (dir) specified by the filename.
//
// ie: if filename = /usr/local/ps2/games then it will return the inode for /usr/local/ps2
pfs_cache_t* pfsInodeGetParent(pfs_mount_t *pfsMount, pfs_cache_t *clink, const char *filename,
                                char *path, int *result)
{
    static int pfsSymbolicLinks = 0;
    pfs_cache_t *link, *inode;
    char *filename2=(char*)filename;

    if (filename2[0]==0)
    {
        *result=-ENOENT;
        if (clink)  pfsCacheFree(clink);
        return NULL;
    }

    if (filename2[0] == '/')
    {

        // Get inode for root dir

        if (clink)  pfsCacheFree(clink);
        if ((clink=pfsInodeGetData(pfsMount, pfsMount->root_dir.subpart,
                      pfsMount->root_dir.number, result))==0)
            return NULL;
    }
    else if (clink==NULL)
    {

        // Otherwise if relative path, get inode for current dir

        if ((clink=pfsInodeGetData(pfsMount, pfsMount->current_dir.subpart,
                      pfsMount->current_dir.number, result))==0)
            return NULL;
    }

    do
    {
        filename2=pfsSplitPath(filename2, path, result);
        if (filename2==NULL)    return NULL;

        // If we've reached the end of the path, then we want to return
        // the cached inode for the directory which holds the file/dir in path
        if (filename2[0]==0)
        {
            if ((clink->u.inode->mode & FIO_S_IFMT) == FIO_S_IFDIR)
                return clink;

            pfsCacheFree(clink);
            *result=-ENOTDIR;   // not a directory
            return NULL;
        }

        inode=pfsInodeGetFileInDir(clink, path, result);

        if (inode && ((inode->u.inode->mode & FIO_S_IFMT) == FIO_S_IFLNK))
        {
            if (pfsSymbolicLinks >= 4)
            {
                *result=-ELOOP; // too many symbolic links
                pfsCacheFree(clink);
                pfsCacheFree(inode);
                return NULL;
            }

            pfsSymbolicLinks++;
            link=pfsInodeGetFile(pfsMount, clink, (char*)&inode->u.inode->data[1], result);
            pfsSymbolicLinks--;

            clink=inode;
            if (link==0)
            {
                pfsCacheFree(inode);
                return NULL;
            }
            inode=link;
        }
        pfsCacheFree(clink);
        clink=inode;

    } while (inode);

    return NULL;
}

int pfsInodeRemove(pfs_cache_t *parent, pfs_cache_t *inode, char *path)
{
    pfs_cache_t *entry;
    int rv=0;

    if((entry=pfsDirRemoveEntry(parent, path))!=NULL)
    {
        pfsInodeSetTimeParent(parent, entry);
        pfsCacheFree(entry);
    }
    else
        rv=-ENOENT;

    pfsCacheFree(parent);
    if(rv==0)
    {
        inode->flags&=~PFS_CACHE_FLAG_DIRTY;
        pfsBitmapFreeInodeBlocks(inode);
        //if(parent->pfsMount->flags & PFS_FIO_ATTR_WRITEABLE)  //Not checked for in late versions of PFS.
        pfsCacheFlushAllDirty(parent->pfsMount);
    }

    pfsCacheFree(inode);
    return rv;
}

pfs_cache_t *pfsInodeCreate(pfs_cache_t *clink, u16 mode, u16 uid, u16 gid, int *result)
{
    pfs_blockinfo_t a, b;

    pfs_mount_t *pfsMount=clink->pfsMount;
    u32 j;
    u32 i;
    pfs_cache_t *inode;

    if ((mode & FIO_S_IFMT) == FIO_S_IFDIR)
    {
        if (pfsMount->num_subs > clink->u.inode->subpart)
            clink->u.inode->subpart++;
        else
            clink->u.inode->subpart=0;
        a.number =0;
        a.subpart=clink->u.inode->subpart;
        j= (pfsMount->zfree * (u64)100) / pfsMount->total_zones;
        i= (pfsMount->free_zone[a.subpart] * (u64)100) /
            (pfsMount->blockDev->getSize(pfsMount->fd, a.subpart) >> pfsMount->sector_scale);
        if ((i < j) && ((j-i) >= 11))
            a.subpart=pfsGetMaxIndex(pfsMount);
    }else{
        a.number=clink->u.inode->inode_block.number;
        a.subpart=clink->u.inode->inode_block.subpart;
    }
    a.count=1;

    // Search for a free zone, starting from parent dir inode block
    *result=pfsBitmapSearchFreeZone(pfsMount, &a, 2);
    if (*result<0)  return 0;
    inode=pfsCacheGetData(pfsMount, a.subpart, a.number << pfsMount->inode_scale,
            PFS_CACHE_FLAG_SEGD | PFS_CACHE_FLAG_NOLOAD, result);
    if (inode == NULL)
        return NULL;

    // Initialise the inode (which has been allocate blocks specified by a)
    pfsInodeFill(inode, (pfs_blockinfo_t*)&a, mode, uid, gid);
    if ((mode & FIO_S_IFMT) != FIO_S_IFDIR)
        return inode;

    b.number=a.number;
    b.subpart=a.subpart;
    b.count=a.count;

    *result=pfsBitmapSearchFreeZone(pfsMount, (pfs_blockinfo_t*)&a, 0);
    if (*result<0){
        pfsCacheFree(inode);
        pfsBitmapFreeBlockSegment(pfsMount, (pfs_blockinfo_t*)&b);
        return NULL;
    }

    inode->u.inode->data[1].number=a.number;
    inode->u.inode->data[1].subpart=a.subpart;
    inode->u.inode->data[1].count =a.count;

    return inode;
}

int pfsCheckAccess(pfs_cache_t *clink, int flags)
{
    int mode;

    // Bail if trying to write to read-only mount
    if ((clink->pfsMount->flags & FIO_MT_RDONLY) && (flags & FIO_O_WRONLY))
        return -EROFS;

    if (((clink->u.inode->mode & FIO_S_IFMT) != FIO_S_IFDIR) &&
        ((clink->u.inode->mode & 0111) == 0))
        mode=6;
    else
        mode=7;
    return ((mode & flags) & 7) == flags ? 0 : -EACCES;
}

char* pfsSplitPath(char *filename, char *path, int *result)
{
    int i=0;
    int j=0;

    for (i=0; filename[i] == '/'; i++)
        ;

    for (; i<1024 && filename[i] != '/'; i++){
        if (filename[i] == 0)   break;
        if (j < 255)
            path[j++] = filename[i];
    }

    if (j<256)
        path[j]=0;

    while (filename[i] == '/')
        if (i<1024)
            i++;
        else
            break;
    if (i<1024)
        return &filename[i];

    *result=-ENAMETOOLONG;
    return 0;
}

u16 pfsGetMaxIndex(pfs_mount_t *pfsMount)
{
    u32 max=0, maxI=0, i, v;

    for (i=0; i < pfsMount->num_subs + 1; i++)  //enumerate all subs
    {
        v = (pfsMount->free_zone[i] * (u64)100) /
            (pfsMount->blockDev->getSize(pfsMount->fd, i) >> pfsMount->sector_scale);
        if (max < v)
        {
            max=v;
            maxI=i;
        }
    }
    return maxI;
}

int pfsAllocZones(pfs_cache_t *clink, int msize, int mode)
{
    pfs_blockpos_t blockpos;
    int result=0;
    u32 val;
    int zsize;

    zsize=clink->pfsMount->zsize;
    val=((msize-1 + zsize) & (-zsize)) / zsize;

    if(mode==0)
        if (((clink->u.inode->number_blocks-clink->u.inode->number_segdesg) *(u64)zsize)
            >= (clink->u.inode->size + msize))
            return 0;

    if((blockpos.inode = pfsBlockGetLastSegmentDescriptorInode(clink, &result)))
    {
        blockpos.block_offset=blockpos.byte_offset=0;
        blockpos.block_segment=clink->u.inode->number_data-1;
        val-=pfsBlockExpandSegment(clink, &blockpos, val);
        while (val && ((result=pfsBlockAllocNewSegment(clink, &blockpos, val))>=0)){
            val-=result;
            result=0;
        }
        pfsCacheFree(blockpos.inode);
    }
    return result;
}

void pfsFreeZones(pfs_cache_t *pfree)
{
    pfs_blockinfo_t b;
    int result;
    pfs_mount_t *pfsMount = pfree->pfsMount;
    pfs_inode_t *inode = pfree->u.inode;
    u32 nextsegdesc = 1, limit = inode->number_data, i, j = 0, zones;
    pfs_blockinfo_t *bi;
    pfs_cache_t *clink;

    zones = (u32)(inode->size / pfsMount->zsize);
    if(inode->size % pfsMount->zsize)
        zones++;
    if(inode->number_segdesg + zones == inode->number_blocks)
        return;

    j = zones;
    b.number = 0;
    clink = pfsCacheUsedAdd(pfree);

    // iterate through each of the block segments used by the inode
    for (i = 1; i < limit && j; i++)
    {
        if(pfsFixIndex(i) == 0)
        {
            if ((clink = pfsBlockGetNextSegment(clink, &result)) == 0)
                return;

            nextsegdesc++;
        }
        else
        {
            bi = &clink->u.inode->data[pfsFixIndex(i)];

            if(j < bi->count)
            {
                bi->count -= j;
                b.subpart = bi->subpart;
                b.count = j;
                b.number = bi->number +
                    bi->count;
                j = 0;
                clink->flags |= PFS_CACHE_FLAG_DIRTY;
            }
            else
                j -= bi->count;
        }
    }

    pfree->u.inode->number_data = i;
    pfree->u.inode->number_blocks = zones + nextsegdesc;
    pfree->u.inode->number_segdesg = nextsegdesc;
    pfree->u.inode->last_segment.number = clink->u.inode->data[0].number;
    pfree->u.inode->last_segment.subpart= clink->u.inode->data[0].subpart;
    pfree->u.inode->last_segment.count  = clink->u.inode->data[0].count;
    pfree->flags |= PFS_CACHE_FLAG_DIRTY;

    if (b.number)
        pfsBitmapFreeBlockSegment(pfsMount, &b);

    for( ; i < limit; i++)
    {
        if (pfsFixIndex(i) == 0)
        {
            if((clink = pfsBlockGetNextSegment(clink, &result)) == 0)
                return;
        }
        bi = &clink->u.inode->data[pfsFixIndex(i)];
        pfsBitmapFreeBlockSegment(pfsMount, bi);
        pfsCacheMarkClean(pfsMount, bi->subpart, bi->number<<pfsMount->inode_scale,
            (bi->number+bi->count)<<pfsMount->inode_scale);
    }

    pfsCacheFree(clink);
}
```

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_8d23988136bc744fa84648d381d7c6e1.html>

##### Files
| file | elf-loader.h [code] |

---

## dvr Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_8d816be76444126f1148a76612486d4b.html>

Directory dependency graph for dvr:
##### Directories

---

## netinet Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_8dadea75015a41719a66be55b9c6dcab.html>

Directory dependency graph for netinet:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_8f4cc36d3d091528309542afe6a411b5.html>

Directory dependency graph for src:

---

## usbd Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_8f550b51c304fe10978bfd792866fae2.html>

Directory dependency graph for usbd:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_8ff1c094aecb3826deec8c22f732d049.html>

Directory dependency graph for src:

---

## dvrfile Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_90fe12cfe0c184e93ce162881a1343e2.html>

Directory dependency graph for dvrfile:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_9160062ad929ec06a5fd151d66e7b140.html>

Directory dependency graph for include:
##### Files
| file | sior.h [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_91e901f4669815123068a4acba61e31d.html>

Directory dependency graph for src:
##### Directories
##### Files
| file | batch.c [code] |
| file | block.c [code] |
| file | effect.c [code] |
| file | freesd.c [code] |
| file | voice.c [code] |

---

## stdlib Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_91f668bae3b63b2f0c696a752c6e3e8b.html>

Directory dependency graph for stdlib:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_92097a15f19d7acf3fc8dc8fc00a22b0.html>

Directory dependency graph for src:

---

## ps2snd Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_9257be179ffb1bae505ffa73096b7986.html>

Directory dependency graph for ps2snd:
##### Directories

---

## ps2-irxgen Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_92da0d7cbf784bf8c518f9b82538e0f7.html>

Directory dependency graph for ps2-irxgen:
##### Directories

---

## graph Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_933591e1cd95ed33f946db8a4302cbd1.html>

Directory dependency graph for graph:
##### Directories

---

## ahx Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_9337eeae2b875a84dbe6e00bf944922d.html>

Directory dependency graph for ahx:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_93782aa3b15333f5f3e250c044e02306.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_93e72ac5e0899245066e72da711db400.html>

Directory dependency graph for include:
##### Files
| file | excepman.h [code] |

---

## acjvld Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_940f37c3979c10ff959587dc675877f7.html>

Directory dependency graph for acjvld:
##### Directories

---

## musl Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_950112c2cce41ca0fe6d06ee08cf690a.html>

Directory dependency graph for musl:
##### Directories

---

## stdio Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_952a988346c879bc3b2834e2377036db.html>

Directory dependency graph for stdio:
##### Directories

---

## fsck Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_9541e23af0221debb6bd9c707cda09ba.html>

Directory dependency graph for fsck:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_955b1a9953d8165e5418b61b127de031.html>

Directory dependency graph for include:
##### Files
| file | modload.h [code] |
| file | xmodload.h [code] |

---

## srcfile Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_956615eb5c1ba3c328b30cb4364be616.html>

Directory dependency graph for srcfile:
##### Directories

---

## pvrdrv Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_965b04ab41d8424e7ba3e3f78bb2fea4.html>

Directory dependency graph for pvrdrv:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_965b2c0ff1542ea613c0ef9ad84df925.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_97266484b38e875e0a4d570fbe2370ab.html>

Directory dependency graph for include:
##### Files
| file | sifcmd.h [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_972b40c78cb4e5b6d65cc6bc53c22b1f.html>

Directory dependency graph for src:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_974d5174780fe889dca37a7e0a150649.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_976cac3a009daf9653fca3e5520d5af8.html>

Directory dependency graph for include:
##### Files
| file | audsrv.h [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_978a4b8b56b6fb3e26b15a692e8f0cfd.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_97f09241239d7d5372d6f9efe5fe96c8.html>

Directory dependency graph for include:
##### Files
| file | erl.h [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_9805d618bf049a122c516d9b6b072b3f.html>

Directory dependency graph for src:

---

## startup Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_980fbc83f434ee581df0dda8a6c16376.html>

Directory dependency graph for startup:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_9919254319ca33220f387ac6faa6f022.html>

*(no textual content on this page)*

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_99cace3514b50ba2406a70ad1e94d391.html>

Directory dependency graph for include:
##### Files
| file | vblank.h [code] |

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_9a2ed50503c4a05c33e063cab27eda7b.html>

Directory dependency graph for include:
##### Files
| file | debug.h [code] |
| file | hwbp.h [code] |
| file | screenshot.h [code] |

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_9a86dbb94afa354b42c3b83282a0ba50.html>

##### Files
| file | ps2cam.h [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_9a86ed6e8896e7e0c8bbb87e67885b72.html>

Directory dependency graph for src:

---

## tlbsrc Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_9a87498b9a1b570e9d1e3baca4c4d515.html>

Directory dependency graph for tlbsrc:
##### Directories

---

## camera Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_9a8d1e453fec95aa02b6b391ce710514.html>

Directory dependency graph for camera:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_9adfede304c1081b01015a76d5669ba3.html>

*(no textual content on this page)*

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_9b52241a62bfbf5408dbbd7f06bda581.html>

Directory dependency graph for include:
##### Files
| file | dmacman.h [code] |

---

## sifcmd Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_9b72dc07a1836a88bbfd185895c8f3de.html>

Directory dependency graph for sifcmd:
##### Directories

---

## eeconf Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_9b8b5a8f700c1b50e04941c843dd61d9.html>

Directory dependency graph for eeconf:
##### Directories

---

## kernel Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_9be0baa3d4a3e9f480a9ee70594037fa.html>

Directory dependency graph for kernel:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_9ca527b14f2d2169259cc21ce8c4f089.html>

##### Files
| file | ps2cam_rpc.h [code] |

---

## poffsim Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_9cb22f3580e9b820d735857d49891159.html>

Directory dependency graph for poffsim:
##### Directories

---

## secr Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_9cb70fa9cd0fdb24be23bccc65a6123b.html>

Directory dependency graph for secr:
##### Directories

---

## tcpip-netman Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_9df346544416700849519ab7a98decca.html>

Directory dependency graph for tcpip-netman:
##### Directories

---

## sdr Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_9e0428e83ee0eb714ec5acc0a72cfb15.html>

Directory dependency graph for sdr:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_9e3c5d5093573b24d7eea99b486ff3d8.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_9ee7a87fd78246ba2006e1826d3b598d.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_9f22b650fed5b856a4b827fc85eed6fb.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_9f3151072a2cf3387609e11808f78fdc.html>

Directory dependency graph for include:
##### Files
| file | s147nand.h [code] |

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_9f3c625f7970e44b9f3af46a3aea5793.html>

Directory dependency graph for include:
##### Files
| file | rmman.h [code] |

---

## devfs Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_a0342a6ef9487eda55789d2e07a75ee7.html>

Directory dependency graph for devfs:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_a05adc316625002d920f1719f73759f9.html>

Directory dependency graph for src:

---

## erl Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_a0a8ac7efb6662b749c1285408048e6d.html>

Directory dependency graph for erl:
##### Directories

---

## sifman Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_a0d37aaf829787e8da99f7ff6597b371.html>

Directory dependency graph for sifman:
##### Directories

---

## cdvd Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_a12d8da7b0731a57c6a388326ad5e612.html>

Directory dependency graph for cdvd:

---

## dvrp Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_a16ad4cba4b1f15056f2b7b0b5931815.html>

Directory dependency graph for dvrp:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_a16c9e0a8cdb78654a589031bd60794d.html>

Directory dependency graph for src:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_a17103320e7b55573b6692b5b08c9050.html>

Directory dependency graph for src:

---

## ldrsrc Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_a27eec25d83e12bfa1e0525665b46f53.html>

Directory dependency graph for ldrsrc:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_a2c795235980acedb0cb99ba6b45f6fe.html>

Directory dependency graph for include:
##### Files
| file | pvrdrv.h [code] |

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_a334b0fa66072ae2ecbe29a491f27ebb.html>

Directory dependency graph for include:

---

## ssbusc Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_a41af06f3bbae69c1382d5deb2bdd8e8.html>

Directory dependency graph for ssbusc:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_a493926c6e9678712bca5b1e822bb94f.html>

Directory dependency graph for src:
##### Files
| file | alarm.c [code] |
| file | deci2.c [code] |
| file | delaythread.c [code] |
| file | exit.c [code] |
| file | fileio.c [code] |
| file | getkernel.c [code] |
| file | glue.c [code] |
| file | initsys.c [code] |
| file | iopcontrol.c [code] |
| file | libosd.c [code] |
| file | libosd_common.c [code] |
| file | libosd_full.c [code] |
| file | loadfile.c [code] |
| file | osd_config.c [code] |
| file | rom0_info.c [code] |
| file | setup.c [code] |
| file | sifcmd.c [code] |
| file | sifrpc.c [code] |
| file | sio.c [code] |
| file | thread.c [code] |
| file | timer.c [code] |
| file | timer_alarm.c [code] |
| file | tty.c [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_a498588c2d5275b63f4912378b4fcc14.html>

Directory dependency graph for src:
##### Files
| file | SifIopRebootBuffer.c [code] |

---

## mtapman Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_a4e67f1f26c786efcb65152c9bde5a70.html>

Directory dependency graph for mtapman:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_a5154322bc74c9fccf7755c77a53b216.html>

Directory dependency graph for include:
##### Files
| file | xatapi.h [code] |

---

## padman Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_a557906189af728f4106d0a041fcd170.html>

Directory dependency graph for padman:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_a6461ff8fdd7d046f5f8a1e32f705515.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_a689f65c7ec1db2bd6e0c28a593c3abb.html>

Directory dependency graph for include:
##### Files
| file | log.h [code] |
| file | rsio2man.h [code] |
| file | sio2man.h [code] |
| file | xsio2man.h [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_a6aef61d3911eff8577226fa39299eeb.html>

Directory dependency graph for src:

---

## acmem Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_a75e69d790b6d0b75ca4561c0370959b.html>

Directory dependency graph for acmem:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_a7a4ee9224592e8b230e4c752a3af655.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_a7b91cccb02c4e3ff005f6cfec8ac8b2.html>

Directory dependency graph for src:

---

## loader Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_a823facde94c6bc1001721fbc16ab82f.html>

Directory dependency graph for loader:
##### Directories

---

## secrsif Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_a962c81a387027290051f8c67837a8ed.html>

Directory dependency graph for secrsif:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_aa0d5e3d566b838d5df154bca66431e9.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_aac407a7a5679478d0631d0d52d3c8a2.html>

Directory dependency graph for include:
##### Files
| file | libcdvd.h [code] |

---

## tcpip-base Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_ab0c940ac9afa06c331831ae52f4280f.html>

Directory dependency graph for tcpip-base:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_ab19dda6107f84e683ccc0253199f4b6.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_ac1b9311aa44ad4cf108d5fb93dfb606.html>

Directory dependency graph for src:
##### Directories

---

## arpa Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_ac9abccd0926f2a07cee52807b3f1055.html>

Directory dependency graph for arpa:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_acebec3dd40a86cc7d5227abe81a2a6c.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_ae0c0d12ba79935994e6f04422f81491.html>

Directory dependency graph for include:
##### Files
| file | ctype.h [code] |
| file | setjmp.h [code] |
| file | sysclib.h [code] |

---

## cdfs Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_ae2e5b2d61c32fda6e87ab98b4cec460.html>

Directory dependency graph for cdfs:
##### Directories

---

## mcman Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_ae48e1b29bfa2db4ecbd893188b24955.html>

Directory dependency graph for mcman:
##### Directories

---

## keyboard Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_ae67f713f6bc0e42016b6962e584ff13.html>

Directory dependency graph for keyboard:
##### Directories

---

## dvrdv Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_afbf9061e6cd2939a0cc5b3ca7d5328d.html>

Directory dependency graph for dvrdv:
##### Directories

---

## sys Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_afd48996a710abaf5168dda39bb9c23c.html>

Directory dependency graph for sys:
##### Files
| file | time.h [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_afe8e9069a558f7a54a2a2685d2ad2e6.html>

Directory dependency graph for src:
##### Files
| file | ps2atad.c [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_affa5bc1c2f19f5b87b45a614768f7a2.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_b0134b01f921c95b97e052ed9574a667.html>

*(no textual content on this page)*

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_b069942e15a16e77815020525fc2d119.html>

Directory dependency graph for src:
##### Files
| file | ps2ips.c [code] |

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_b084f479ea9ac78d26fb42c3739613d7.html>

Directory dependency graph for include:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_b0f0258a6750b76dde6d0e448c99d653.html>

Directory dependency graph for include:
##### Files
| file | xmtapman.h [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_b11c102c899063f3c26f9e1eac520e38.html>

Directory dependency graph for src:

---

## iopdebug Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_b128a11f24e38182ade4e9889f6c5833.html>

Directory dependency graph for iopdebug:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_b13870b8cbb1ed54253f2a75128daced.html>

Directory dependency graph for src:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_b143042d7a68010e5823de2e404a2924.html>

Directory dependency graph for include:
##### Files
| file | libmouse.h [code] |
| file | ps2mouse.h [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_b1d79714e4f399f37a02c510a4ba57cf.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_b1eb8c8c36c60dd16b95b1412f1809ce.html>

Directory dependency graph for include:
##### Files
| file | secrman.h [code] |

---

## usbmass_bd Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_b21605a940872bbf5de5d8b063daf48d.html>

Directory dependency graph for usbmass_bd:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_b2ec982152147e07bc20d03fb22ae98b.html>

Directory dependency graph for include:
##### Files
| file | math3d.h [code] |

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_b30018f570f668a0b06e9dfb03f925ee.html>

Directory dependency graph for include:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_b31a284edc9ae7f7d75e3646a67d7aaf.html>

Directory dependency graph for src:

---

## startup Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_b3ada97b29f34abd88a10915e46a265a.html>

Directory dependency graph for startup:
##### Directories

---

## libsd Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_b3b65c61938638f28675fc77a7fe35e3.html>

Directory dependency graph for libsd:
##### Directories

---

## poweroff Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_b4755258f2e93c4a8a26138734da4ea3.html>

Directory dependency graph for poweroff:
##### Directories

---

## network Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_b47d22a23da27aa98d6e01bcdbde3243.html>

Directory dependency graph for network:

---

## actimer Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_b480fdbd9089eb9ef496e03587bad219.html>

Directory dependency graph for actimer:
##### Directories

---

## romwrite Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_b63e325ae40e3f3156afef11425dfcf2.html>

Directory dependency graph for romwrite:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_b66894283d75c30189b4c869a6ae3cf5.html>

Directory dependency graph for src:
##### Files
| file | ps2cam_rpc.c [code] |

---

## hdd Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_b6763ea08a8f9364194ebe3565e6b1f0.html>

Directory dependency graph for hdd:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_b6b38ef3e90c88055356c83dd9b95535.html>

Directory dependency graph for src:

---

## libgs Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_b6bcbdb02df18226d1f2b0d9af42cc14.html>

Directory dependency graph for libgs:
##### Directories

---

## usb Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_b6c875632944d243a548db157cd77ec2.html>

Directory dependency graph for usb:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_b86d8e8cc4ff73a3835f86acf7570149.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_b885b894e4096334a2f073c9bc278b43.html>

Directory dependency graph for src:

---

## usbhdfsd Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_b8874c233d466218401f983297aca89b.html>

Directory dependency graph for usbhdfsd:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_b984735f55d4ac900581a956eea77940.html>

*(no textual content on this page)*

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_ba20cf19084f343ca09b1f733fd5cb70.html>

Directory dependency graph for include:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_ba28af0095b87002b3d23c93d4ce8d9d.html>

Directory dependency graph for src:

---

## remote Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_ba37a805e2af6959a7cee62b248f44cb.html>

Directory dependency graph for remote:
##### Directories

---

## cdvd Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_ba4b21ee1217591b79746c791fe162fc.html>

Directory dependency graph for cdvd:
##### Directories

---

## udnl Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_ba5b6e33a21a738024e426bc2a53820a.html>

Directory dependency graph for udnl:
##### Directories

---

## http Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_bb1a65baea34b53b4bbf06e6d3ddfe57.html>

Directory dependency graph for http:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_bb6a3a7d8adb654c719be286ee32591c.html>

Directory dependency graph for src:

---

## an986 Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_bc1b9c69a4b8a1b909185ad20026d0b9.html>

Directory dependency graph for an986:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_bcd2c58d4ad7915f6bedffda715c21a5.html>

Directory dependency graph for include:
##### Files
| file | libgs.h [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_bce8d32bac1ae42108a1f1e0bd747840.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_bd0b2718f6cbaa7d5f7a645cbab55d03.html>

*(no textual content on this page)*

---

## eyalroz_printf Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_bd62be9475ca4f332fbf19becd78d95e.html>

Directory dependency graph for eyalroz_printf:

---

## s147ctrl Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_bdc7f5ab64e11bfb8293504cf1d9163b.html>

Directory dependency graph for s147ctrl:
##### Directories

---

## common Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_bdd9a5d540de89e9fe90efdfc6973a4f.html>

Directory dependency graph for common:
##### Directories
| directory | sbus |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_be36dfe0fa2692ece4088139be3fa1db.html>

*(no textual content on this page)*

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_be4e3f326d0b1f8e64f890721d59e043.html>

*(no textual content on this page)*

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_be6a4eb92b3e198248caebd4132877bb.html>

##### Files
| file | ps2ips.h [code] |

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_bfe1897d6ab97ad9855e87f2c456ed84.html>

Directory dependency graph for include:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_bfec2874d182eb71a9023b046bce5656.html>

Directory dependency graph for src:
##### Files
| file | libmouse.c [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_bfefd3566efd1047bfb5ae95f609b467.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_c15c3f3fb57f56539c5f292b37505da8.html>

Directory dependency graph for src:
##### Files
| file | libmpeg_internal.h [code] |

---

## acata Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_c2249c15dcb99f353cb0bb3a93761cbc.html>

Directory dependency graph for acata:
##### Directories

---

## audsrv Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_c224f8f6f41c46dc69cc573710289bc0.html>

Directory dependency graph for audsrv:
##### Directories

---

## vm Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_c247aa5216deb56a59c507e95c948f5f.html>

*(no textual content on this page)*

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_c2745311b335edcded8abb10f5a23735.html>

Directory dependency graph for src:

---

## udptty Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_c29ab4c22b7bc0d7876a510e876257b9.html>

Directory dependency graph for udptty:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_c2b748831c3fae7af36726db19c0943f.html>

*(no textual content on this page)*

---

## cdvdstm Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_c39f392af7f13c65e7a482de8f63f0c9.html>

Directory dependency graph for cdvdstm:
##### Directories

---

## siftoo Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_c3fae06f71c3e401160299d109ef6df7.html>

Directory dependency graph for siftoo:
##### Directories

---

## netfs Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_c49d6f7b24cb4247c18d467361672153.html>

Directory dependency graph for netfs:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_c5a272b641a8aa1be005aad5e45cddba.html>

Directory dependency graph for include:
##### Files
| file | loadcore.h [code] |
| file | xloadcore.h [code] |

---

## msifrpc Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_c6b5e9471ae732442a9e11cae3c074af.html>

Directory dependency graph for msifrpc:
##### Directories

---

## loadfile Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_c70e074c247f0fc7ba2b5b627ea24568.html>

Directory dependency graph for loadfile:
##### Directories

---

## debug Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_c7a9def6f98954b831c78937abc1a97c.html>

Directory dependency graph for debug:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_c8b38286a00d2d4baa2f0cee94e4927f.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_c99e289baa83bc65c8ca004663027398.html>

Directory dependency graph for include:
##### Files
| file | ioprpgen.h [code] |

---

## atad Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_c9fad5ea75093c7356ef5f2b903232b1.html>

Directory dependency graph for atad:
##### Directories

---

## tcpip Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_ca24a423c1b235320d00c488564f2476.html>

Directory dependency graph for tcpip:
##### Directories

---

## bdmfs_fatfs Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_ca4e6ad4571d2d160c85f86efebac72d.html>

Directory dependency graph for bdmfs_fatfs:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_ca6cfcffd6c37235e476126984936748.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_caf0af085a7c65a631c06dc345ebd7aa.html>

Directory dependency graph for src:
##### Files
| file | libmc.c [code] |

---

## tcpip Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_cb38d55d28446d14702541320714f23c.html>

Directory dependency graph for tcpip:
##### Directories
| directory | tcpip |
| directory | tcpip-netman |
| directory | tcpips |

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_cb50f4a8529b26463793155357bbfc11.html>

Directory dependency graph for include:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_cb942abaf7cd6bcef012f84a33678468.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_cba1770cfc6ae13e02c5af9607396ed3.html>

*(no textual content on this page)*

---

## pfs Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_cece7c3de560cfc4de14abf3198b3696.html>

Directory dependency graph for pfs:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_cf43a48f832f5c6078b2594de76b351f.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_cf9909246eeaec7dd789467615c7574c.html>

Directory dependency graph for src:

---

## elf-loader2 Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_d07386db992f9b8f3252747c64912580.html>

Directory dependency graph for elf-loader2:
##### Directories

---

## ioman Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_d204d0cf134f4cdf6ccf23f48ed9ae60.html>

Directory dependency graph for ioman:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_d23044be0d8ef2a9b3860a856376b9fb.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_d236ca42f0241c3c711c47cabfd53918.html>

Directory dependency graph for src:

---

## eesync Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_d26cb44661e10025c70afdeb6a3fa91f.html>

Directory dependency graph for eesync:
##### Directories

---

## netman Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_d3008f816dc1c94b20a03a6df12b797a.html>

Directory dependency graph for netman:
##### Directories

---

## tcpips Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_d367c99d526987235c59a734292a94e2.html>

Directory dependency graph for tcpips:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_d3a9eea9e5254f05d390a494baa7dd0f.html>

Directory dependency graph for src:
##### Directories

---

## threadman Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_d3b40e87d731c1e886b7a70e6daaf700.html>

Directory dependency graph for threadman:
##### Directories

---

## ppctty Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_d3ded9369ca517f344f23b4db50242ea.html>

Directory dependency graph for ppctty:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_d3e4ec746f8f014b16cee2f1cbb9eaa2.html>

Directory dependency graph for include:
##### Files
| file | thbase.h [code] |
| file | thevent.h [code] |
| file | thfpool.h [code] |
| file | thmsgbx.h [code] |
| file | thsemap.h [code] |
| file | thvpool.h [code] |
| file | xthbase.h [code] |

---

## sior Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_d4a6eac35d72455d405007552e574e19.html>

Directory dependency graph for sior:
##### Directories

---

## libpthreadglue Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_d4c047276d2aa3c6952cb907fbc768a4.html>

Directory dependency graph for libpthreadglue:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_d4d8b80efad9686e8abc6af08c017e38.html>

Directory dependency graph for src:

---

## accdvd Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_d5480c28c70feff4085e53014a5bb4c3.html>

Directory dependency graph for accdvd:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_d55b4e69e33af9fb5c08903da6cf2ea7.html>

*(no textual content on this page)*

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_d55f23d8ba757b23ee1ce2ded4afdb2b.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_d56d07feea212d2cdb5d2d86474d890a.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_d59d238c90b001f6a8c82332ee6c0164.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_d61dc2cc7a3fea5cf83a4c127f7dea92.html>

Directory dependency graph for include:

---

## sifinit Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_d660f1d0a410b188ebc642aba8c19599.html>

Directory dependency graph for sifinit:
##### Directories

---

## dma Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_d6c8ea3c46b2d4fe2308a65fe0836890.html>

Directory dependency graph for dma:
##### Directories

---

## dmacman Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_d7026c86e7f8fc62fc6c0ebacfebf381.html>

Directory dependency graph for dmacman:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_d743091465ee8a68e4febb0fca48bea4.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_d809a6a3c5621df28b9f2ead765ca843.html>

Directory dependency graph for include:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_d85fc139258090bae3d41b643db2b8d6.html>

Directory dependency graph for include:
##### Files
| file | devfs.h [code] |

---

## addrom2 Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_d88f8949096e46f9e554069e44cde349.html>

Directory dependency graph for addrom2:
##### Directories

---

## xatapi Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_d892e9234db8c7dfaa79ee0fe28ecb70.html>

Directory dependency graph for xatapi:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_d8a2072387ffd8123a4de1c649214686.html>

Directory dependency graph for include:
##### Files
| file | s147mdev.h [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_d8e9f3932b80db8eabaaa05262791dac.html>

Directory dependency graph for src:
##### Files
| file | ps2ip.c [code] |

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_d96040052f185a41787759ef73c94cbc.html>

Directory dependency graph for include:
##### Files
| file | gpt_types.h [code] |
| file | mbr_types.h [code] |
| file | part_driver.h [code] |

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_da90a009e03e832953b0458a16d394a7.html>

Directory dependency graph for include:
##### Files
| file | cdvdfsv.h [code] |

---

## acdev9 Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_db911554707e5978c632e5ebc00a1f14.html>

Directory dependency graph for acdev9:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_dc278788ab44aeea11d12433df75e4c2.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_dc5895c301db7fa25093677632930453.html>

Directory dependency graph for src:

---

## arch Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_dc679784e9af5b83c39640f602330bdc.html>

Directory dependency graph for arch:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_dce4a208cb4992793dc296e9f1f99230.html>

Directory dependency graph for include:
##### Files
| file | timrman.h [code] |
| file | xtimrman.h [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_dd15e966dfe8a4239d7e9367008bc621.html>

Directory dependency graph for src:
##### Files
| file | iop_debug.c [code] |
| file | iopdebug_defs.h [code] |
| file | iopdebug_priv.h [code] |
| file | main.c [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_de280b54cbc4af6d061f4292a6699227.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_dfd0648f7ccdaeb6e4c87cb596a9ba55.html>

Directory dependency graph for src:

---

## keyboard Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_dfd34f7999bdb28cb70101636e016b16.html>

Directory dependency graph for keyboard:
##### Directories

---

## thmon Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_dff89ea4f3392a2e49b7401cf3785b58.html>

Directory dependency graph for thmon:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_e148382086b2a2856fe56816471b7674.html>

Directory dependency graph for src:

---

## vfat Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_e169fc947b78f95c57d275a8c94aa84e.html>

Directory dependency graph for vfat:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_e18cef6d754604f83c1d4afc72605bc2.html>

Directory dependency graph for src:

---

## acdev Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_e1d9c48c0fe693840f397bd0f86d700a.html>

Directory dependency graph for acdev:
##### Directories

---

## nonstd Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_e27c3ee1507bfb964a7b3cbac14762a5.html>

Directory dependency graph for nonstd:

---

## elf-loader Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_e299e00cada893e7503c7ad35bb90f27.html>

Directory dependency graph for elf-loader:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_e4166c97f91ebf3383055a8d189b65ea.html>

Directory dependency graph for include:
##### Files
| file | xpadman.h [code] |

---

## libcglue Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_e42c7571aba127d36ebf1b64b3eb3ddc.html>

Directory dependency graph for libcglue:
##### Directories

---

## s147link Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_e456da8ab8120481e822513fb37bb7b1.html>

Directory dependency graph for s147link:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_e45d88c07cbfec1ea295334984feb137.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_e4694b96285dd2df921b57b1206c9a6b.html>

Directory dependency graph for include:
##### Files
| file | sysmem.h [code] |
| file | xsysmem.h [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_e59fb6a30210cb18518aef290b62855b.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_e6a8a4ea8085298a3170c9700467a79c.html>

##### Files
| file | libmtap.h [code] |

---

## secrman Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_e87a748976a4b7d8bcde9ae973d63de3.html>

Directory dependency graph for secrman:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_e958439eae9e499529b4758660d27573.html>

##### Files
| file | ps2kbd.h [code] |

---

## xesdrv Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_e9f6397765e90b9450cf2a2f2169ae17.html>

Directory dependency graph for xesdrv:
##### Directories

---

## bdmfs_vfat Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_eabe988c95970cb88382a9440b1d86c2.html>

Directory dependency graph for bdmfs_vfat:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_eaf097373852e67154ee977045ee89d0.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_ebe7e6174b0ffb5fb3dae074343f32a7.html>

Directory dependency graph for src:

---

## clearspu Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_ec70ebae439c2e5e4973a97a9e3f90a5.html>

Directory dependency graph for clearspu:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_ed221be002b748c2b427296b2fccd1b2.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_ed3452e94ee5fc37855e7a7af1df18cc.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_eead4ded970bb501941913089bc8e720.html>

Directory dependency graph for include:

---

## daemon Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_ef36e8adbc4006275a4a85debe48eb61.html>

Directory dependency graph for daemon:
##### Directories

---

## math3d Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_ef61ae23abebf035898b2c6525d9b365.html>

Directory dependency graph for math3d:
##### Directories

---

## mips Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_ef7bf7eca87c8b3cdcf1dd371e9b3d72.html>

Directory dependency graph for mips:
##### Directories

---

## packet Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_ef7db18cfb93c4891bb35babb04f0d85.html>

Directory dependency graph for packet:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_efd911068bd98c5b8ecc421070f7e163.html>

Directory dependency graph for src:
##### Files
| file | common.c [code] |
| file | patch_disable_prefix_check.c [code] |
| file | patch_enable_lmb.c [code] |
| file | patch_romdrv_set_rom1_info.c [code] |
| file | patch_user_mem_clear.c [code] |
| file | slib.c [code] |
| file | smem.c [code] |
| file | smod.c [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_f0daa06f548bbd51a8a549805553b036.html>

Directory dependency graph for src:
##### Files
| file | sbusintr.c [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_f22cef6dc5ce81fd774cb16dad291073.html>

Directory dependency graph for src:

---

## hdck Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_f24565d8e5c1fee073eb5b759b3d7497.html>

Directory dependency graph for hdck:
##### Directories

---

## fs Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_f24daea2522ffa8b6dc5fa9cdf5b8f5c.html>

Directory dependency graph for fs:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_f30e57f6b5b76337d5c3983a1dbc8886.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_f335ad7fdd71679ab019891088db11a0.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_f38af649c18175eef64498f7ded53ff0.html>

Directory dependency graph for src:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_f3cefdad461251ef1ac341e57fd948be.html>

Directory dependency graph for src:

---

## ctype Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_f3f1c70370cc6f5ecdb4c01348601eab.html>

Directory dependency graph for ctype:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_f43a10262b73c6e7d8c393ecfde6f1ae.html>

Directory dependency graph for include:
##### Files
| file | iopmgr.h [code] |

---

## cdvdman Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_f449e64e40a305c379232bc791e77932.html>

Directory dependency graph for cdvdman:
##### Directories

---

## extflash Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_f44f46f2cd21d59a913dd7de442a4869.html>

Directory dependency graph for extflash:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_f44fbee28c87ccaf0699713fb55dc4d0.html>

*(no textual content on this page)*

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_f569607cb6afe3f1a6eca55bcfb9e9e7.html>

Directory dependency graph for src:
##### Files
| file | sior_rpc.c [code] |

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_f5863da36fbb72d29e9b1dbcb4acc18d.html>

Directory dependency graph for include:
##### Files
| file | ps2ip.h [code] |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_f5a864409d3e095bcda6e0b97e9111ab.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_f6b3ac9ef47c20d6a81140c1329c3c32.html>

Directory dependency graph for src:

---

## sdsq Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_f6cc0a29c52682018d7d3e4d1b8065b8.html>

Directory dependency graph for sdsq:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_f6d409efb8c225447b4f5511042ceaec.html>

Directory dependency graph for src:
##### Directories

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_f6f36f3eb6875262b2c2259532f4a7d0.html>

Directory dependency graph for include:
##### Files
| file | input.h [code] |

---

## dvrav Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_f7741f78ef7687a58b2e9b3b36050a7e.html>

Directory dependency graph for dvrav:
##### Directories

---

## iomanx Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_f82a163f83eb0dcdf294ef3743365a67.html>

Directory dependency graph for iomanx:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_f877eea6f4a67835df99bf91eacfa5d8.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_f880cd0723e9ab7c57124c2f1349ba73.html>

##### Files
| file | ahx_rpc.h [code] |

---

## network Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_f89050b4b7ba0179c2c7efd2300413d9.html>

Directory dependency graph for network:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_f8c803150f5a80db82e6e0d083e86f49.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_f8f00ca48f0867f976c806c2aee604a7.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_f9025b2b9c2ed835e66cd5059fb3ed0a.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_f9184cf480022417928648bd2c15dc59.html>

Directory dependency graph for src:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_fa42cafb55f2a381bf7d4b59cfe4d4ef.html>

Directory dependency graph for include:

---

## include Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_fa645703e9d75d6dc5aaf566568fec79.html>

Directory dependency graph for include:
##### Files
| file | librm.h [code] |
|  | RPC Interface for PS2 Remote Control Driver (RMMAN) |

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_fc6ed93249c3e8a38fecd27b20067b99.html>

Directory dependency graph for src:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_fc80c3c91208c3ad5a3a0585da287820.html>

Directory dependency graph for src:
##### Directories

---

## iLink Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_fc941b9cdd19bfc53379effb1dbc42b0.html>

Directory dependency graph for iLink:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_fce568178081d3712212941b5708ede5.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_fdef1eebfae5774bf0c87050bc04492e.html>

Directory dependency graph for src:

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_fe4d942b553a0f3632b13732d211a99b.html>

Directory dependency graph for src:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_febd96eaa193534db0a21df01d562a0f.html>

Directory dependency graph for src:

---

## iopreboot Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_ff70674bc173ff6e32f1bc3a678b82a6.html>

Directory dependency graph for iopreboot:
##### Directories

---

## src Directory Reference

Page: <https://ps2dev.github.io/ps2sdk/dir_ffd7594d846340e67d78bcacff900475.html>

Directory dependency graph for src:

---
