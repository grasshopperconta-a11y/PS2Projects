# Part 5 — Globals

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals.html>

Here is a list of all documented functions, variables, defines, enums, and typedefs with links to the documentation:
###### - _ -
- __attribute__ : libgs.h , libpad.c , cdrom.c , rpc_server.c , ps2_fio.c , batch.c , effect.c , audsrv_rpc.c , adpcm.c , ps2mouse.c , audsrv.c
- __fioMkdirHelper() : ps2sdkapi.c
- _ata_identify_offsets : atahw.h
- _B : ctype.h
- _C : ctype.h
- _EX_DBG_STACK_SIZE : iopdebug_defs.h
- _EX_DEF_STACK_SIZE : iopdebug_defs.h
- _exp_audsrv : audsrv.c
- _gp : libcdvd.c
- _heap_mem_fit() : alloc.c
- _L : ctype.h
- _N : ctype.h
- _P : ctype.h
- _ps2lib_errors : ps2lib_err.h
- _S : ctype.h
- _sif_regs : sifman.h , sifdma.h
- _SifLoadModule() : loadfile.h
- _start() : devfs.c , ps2netfs.c , audsrv.c , main.c , fakehost.c
- _U : ctype.h
- _X : ctype.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_a.html>

Here is a list of all documented functions, variables, defines, enums, and typedefs with links to the documentation:
###### - a -
- A_PS1_1F801018 : iop_regs.h
- A_PS1_1F801020 : iop_regs.h
- adpcm_loaded() : adpcm.c
- AHX_Init() : ahx_rpc.h , ahx_rpc.c
- AHX_LoadSong() : ahx_rpc.h , ahx_rpc.c
- AHX_LoadSongBuffer() : ahx_rpc.h , ahx_rpc.c
- AHX_Pause() : ahx_rpc.h , ahx_rpc.c
- AHX_Play() : ahx_rpc.h , ahx_rpc.c
- AHX_Quit() : ahx_rpc.h , ahx_rpc.c
- AHX_SetBoost() : ahx_rpc.h , ahx_rpc.c
- AHX_SetVolume() : ahx_rpc.h , ahx_rpc.c
- AHX_SubSong() : ahx_rpc.h , ahx_rpc.c
- AHX_ToggleOversampling() : ahx_rpc.h , ahx_rpc.c
- alloc_new_sample() : adpcm.c
- ALPHA_CORRECT_RGBA32 : draw_blending.h
- ALPHA_EXPAND_NORMAL : draw_sampling.h
- APA_FLAG_SUB : hdd-ioctl.h
- APA_MAXSUB : hdd-ioctl.h
- APA_TYPE_MBR : hdd-ioctl.h
- ATA_AIF_HDD_BASE : atahw.h
- ATA_C_CODES : atahw.h
- ata_hwport_t : atahw.h
- audsrv_adpcm_init() : audsrv.h , audsrv_rpc.c , audsrv.h , adpcm.c
- audsrv_adpcm_set_volume() : audsrv.h , adpcm.c
- audsrv_adpcm_set_volume_and_pan() : audsrv.h , audsrv_rpc.c
- audsrv_adpcm_t : audsrv.h
- audsrv_available() : audsrv.h , audsrv_rpc.c , audsrv.h , audsrv.c
- audsrv_cd_pause() : audsrv.h , cdrom.c
- audsrv_cd_play_sectors() : audsrv.h , cdrom.c
- audsrv_cd_resume() : audsrv.h , cdrom.c
- audsrv_ch_play_adpcm() : audsrv.h , audsrv_rpc.c , audsrv.h , adpcm.c
- AUDSRV_ERR_NOERROR : audsrv.h
- audsrv_fmt_t : audsrv.h
- AUDSRV_FORMAT_OK : audsrv_rpc.h , audsrv.h
- audsrv_format_ok() : audsrv.h , audsrv.c
- audsrv_free_adpcm() : audsrv.h , audsrv_rpc.c
- audsrv_get_cd_status() : audsrv.h , audsrv_rpc.c , audsrv.h , cdrom.c
- audsrv_get_cd_type() : audsrv.h , audsrv_rpc.c , audsrv.h , cdrom.c
- audsrv_get_cdpos() : audsrv.h , audsrv_rpc.c , audsrv.h , cdrom.c
- audsrv_get_error() : audsrv.h , audsrv_rpc.c
- audsrv_get_error_string() : audsrv.h , audsrv_rpc.c
- audsrv_get_numtracks() : audsrv.h , audsrv_rpc.c , audsrv.h , cdrom.c
- audsrv_get_track_offset() : cdrom.c , audsrv.h , audsrv_rpc.c , audsrv.h
- audsrv_get_trackpos() : cdrom.c , audsrv.h , audsrv_rpc.c , audsrv.h
- AUDSRV_INIT : audsrv_rpc.h , audsrv.h
- audsrv_init() : audsrv_rpc.c , audsrv.h , audsrv.c , audsrv.h
- AUDSRV_INIT_ADPCM : audsrv_rpc.h
- audsrv_is_adpcm_playing() : audsrv.h , audsrv_rpc.c
- audsrv_load_adpcm() : audsrv.h , adpcm.c , audsrv_rpc.c
- audsrv_on_cdda_stop() : audsrv.h , audsrv_rpc.c
- audsrv_on_fillbuf() : audsrv.h , audsrv_rpc.c
- audsrv_pause_cd() : audsrv.h , audsrv_rpc.c
- audsrv_play_audio() : audsrv.c , audsrv.h , audsrv_rpc.c , audsrv.h
- audsrv_play_cd() : audsrv_rpc.c
- AUDSRV_PLAY_CD : audsrv.h
- audsrv_play_cd() : audsrv.h , cdrom.c
- AUDSRV_PLAY_CD : audsrv_rpc.h
- audsrv_play_cd() : audsrv.h
- audsrv_play_sectors() : audsrv_rpc.c , audsrv.h
- audsrv_queued() : audsrv.c , audsrv_rpc.c , audsrv.h
- audsrv_quit() : audsrv_rpc.c , audsrv.h , audsrv.c
- audsrv_read_adpcm_header() : adpcm.c
- audsrv_resume_cd() : audsrv_rpc.c , audsrv.h
- audsrv_set_format() : audsrv.c , audsrv.h , audsrv_rpc.c
- audsrv_set_volume() : audsrv.c , audsrv.h , audsrv_rpc.c , audsrv.h
- audsrv_stop_audio() : audsrv.h , audsrv_rpc.c , audsrv.h , audsrv.c
- audsrv_stop_cd() : audsrv.h , cdrom.c , audsrv_rpc.c , audsrv.h
- audsrv_stop_cd_stream() : cdrom.c
- audsrv_wait_audio() : audsrv.h , audsrv.c , audsrv.h , audsrv_rpc.c

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_b.html>

Here is a list of all documented functions, variables, defines, enums, and typedefs with links to the documentation:
###### - b -
- BLEND_COLOR_SOURCE : draw_blending.h
- BPC_BED : hwbp.h
- BPC_DKE : hwbp.h
- BPC_DRB : hwbp.h
- BPC_DRE : hwbp.h
- BPC_DSE : hwbp.h
- BPC_DTE : hwbp.h
- BPC_DUE : hwbp.h
- BPC_DVE : hwbp.h
- BPC_DWB : hwbp.h
- BPC_DWE : hwbp.h
- BPC_DXE : hwbp.h
- BPC_IAB : hwbp.h
- BPC_IAE : hwbp.h
- BPC_IKE : hwbp.h
- BPC_ISE : hwbp.h
- BPC_ITE : hwbp.h
- BPC_IUE : hwbp.h
- BPC_IXE : hwbp.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_c.html>

Here is a list of all documented functions, variables, defines, enums, and typedefs with links to the documentation:
###### - c -
- calculate_colours() : math3d.h
- calculate_lights() : math3d.h
- calculate_normals() : math3d.h
- calculate_vertices() : math3d.h
- call_rpc_1() : audsrv_rpc.c
- call_rpc_2() : audsrv_rpc.c
- call_rpc_3() : audsrv_rpc.c
- CAM_ERROR_BADHANDLE : ps2cam_rpc.h , ps2cam.h
- CAM_ERROR_BADRANGE : ps2cam_rpc.h , ps2cam.h
- CAM_ERROR_COMMUNKNOWN : ps2cam_rpc.h , ps2cam.h
- CAM_ERROR_DEVNOTREADY : ps2cam_rpc.h , ps2cam.h
- CAM_ERROR_DISCONNECTED : ps2cam_rpc.h , ps2cam.h
- CAM_ERROR_MAXHANDLE : ps2cam_rpc.h , ps2cam.h
- CAM_ERROR_NODEVICE : ps2cam_rpc.h , ps2cam.h
- CAM_ERROR_NONE : ps2cam_rpc.h , ps2cam.h
- CAM_ERROR_UNKNOWN : ps2cam_rpc.h , ps2cam.h
- CAM_STATUS_CONNECTED : ps2cam_rpc.h , ps2cam.h
- CAM_STATUS_CONNECTEDREADY : ps2cam_rpc.h , ps2cam.h
- CAM_STATUS_NOTCONNECTED : ps2cam_rpc.h , ps2cam.h
- camDisableSystem() : ps2cam.h , ps2cam.c
- camEnableSystem() : ps2cam.h , ps2cam.c
- camResetDevice() : ps2cam.h , ps2cam.c
- camResetUsb() : ps2cam.h , ps2cam.c
- camSetUsbInit() : ps2cam.h , ps2cam.c
- camSetUsbWork() : ps2cam.h , ps2cam.c
- camStartStream() : ps2cam.h , ps2cam.c
- camTurnOffRedLed() : ps2cam.h , ps2cam.c
- camTurnOnRedLed() : ps2cam.h , ps2cam.c
- CD_NCMD_CMDS : ncmd.c
- CD_NCMD_READCHAIN : ncmd.c
- cd_paused : cdrom.c
- cd_playing : cdrom.c
- CD_SERVER_NCMD : ncmd.c
- CD_SERVER_POFF : libcdvd.c
- CD_SERVER_SCMD : scmd.c
- cd_transfer_complete() : cdrom.c
- cd_transfer_sema : cdrom.c
- cdda_initialized : cdrom.c
- cdda_play_end : cdrom.c
- cdda_play_start : cdrom.c
- cdda_play_tid : cdrom.c
- cdda_pos : cdrom.c
- cdda_procedure() : cdrom.c
- CdlAcknowledge : libcdvd-common.h
- CdlDataEnd : libcdvd-common.h
- CdlDataReady : libcdvd-common.h
- CdlDiskError : libcdvd-common.h
- CdlLEDEjectBlue : libcdvd-common.h
- CdlLEDPowerGreen : libcdvd-common.h
- CdlLEDPowerRed : libcdvd-common.h
- CdlLEDPowerYellow : libcdvd-common.h
- CdlMAXDIR : libcdvd-common.h
- CdlMAXFILE : libcdvd-common.h
- CdlMAXLEVEL : libcdvd-common.h
- CdlMAXTOC : libcdvd-common.h
- CdlNoIntr : libcdvd-common.h
- CdlRCDisableEject : libcdvd-common.h
- CdlRCDisablePowerOff : libcdvd-common.h
- CdlRCDisablePowerOn : libcdvd-common.h
- CdlRCDisablePowerReset : libcdvd-common.h
- CdlRCDisableReset : libcdvd-common.h
- CdlRTCStatClockBatteryMonitoringVoltageProblem : libcdvd-common.h
- CdlRTCStatClockStopDetected : libcdvd-common.h
- CdlRTCStatCommandError : libcdvd-common.h
- CdlRTCStatCTLRegProblem : libcdvd-common.h
- CdlWakeUpReasonExtraGameReset : libcdvd-common.h
- CdlWakeUpReasonExtraPowerOn : libcdvd-common.h
- CdlWakeUpReasonExtraReset : libcdvd-common.h
- CdlWakeUpReasonExtraSlotIn : libcdvd-common.h
- CdlWakeUpReasonExtraTimer : libcdvd-common.h
- CdlWakeUpReasonMainDevice : libcdvd-common.h
- CdlWakeUpReasonMainPowerOn : libcdvd-common.h
- CdlWakeUpReasonMainReset : libcdvd-common.h
- CdlWakeUpReasonMainTimer : libcdvd-common.h
- CDVD_TRAY_STAT_OPEN : iop_regs.h
- cdvdman_152_get_temperature() : libcdvd-common.h
- cdvdman_167_atapi2dragon() : libcdvd-common.h
- cdvdman_169_dragon2atapi() : libcdvd-common.h
- CdvdStCmd_t : ncmd.c
- CLUT_NO_LOAD : draw_buffers.h
- CLUT_STORAGE_MODE1 : draw_buffers.h
- cmdline_handle() : commandline.c , main.c
- COLOR_CLAMP_MASK : draw_masking.h
- configConvertToGmtTime() : osd_config.h
- configConvertToLocalTime() : osd_config.h
- configGetDateFormat() : osd_config.h
- configGetLanguage() : osd_config.h
- configGetTimeFormat() : osd_config.h
- configGetTimezone() : osd_config.h
- configGetTvScreenType() : osd_config.h
- configIsDaylightSavingEnabled() : osd_config.h
- configIsSpdifEnabled() : osd_config.h
- configSetDateFormat() : osd_config.h
- configSetDaylightSavingEnabled() : osd_config.h
- configSetLanguage() : osd_config.h
- configSetSpdifEnabled() : osd_config.h
- configSetTimeFormat() : osd_config.h
- configSetTimezone() : osd_config.h
- configSetTvScreenType() : osd_config.h
- convmode_from_iomanx() : ps2_fio.c
- convmode_to_iomanx() : ps2_fio.c
- COP0_REG_BadPAddr : mipscopaccess.h
- COP0_REG_BadVAddr : mipscopaccess.h
- COP0_REG_Cause : mipscopaccess.h
- COP0_REG_Compare : mipscopaccess.h
- COP0_REG_Config : mipscopaccess.h
- COP0_REG_Context : mipscopaccess.h
- COP0_REG_Count : mipscopaccess.h
- COP0_REG_Debug : mipscopaccess.h
- COP0_REG_EntryHi : mipscopaccess.h
- COP0_REG_EntryLo0 : mipscopaccess.h
- COP0_REG_EntryLo1 : mipscopaccess.h
- COP0_REG_EPC : mipscopaccess.h
- COP0_REG_ErrorPC : mipscopaccess.h
- COP0_REG_Index : mipscopaccess.h
- COP0_REG_PageMask : mipscopaccess.h
- COP0_REG_Perf : mipscopaccess.h
- COP0_REG_PRId : mipscopaccess.h
- COP0_REG_Random : mipscopaccess.h
- COP0_REG_Status : mipscopaccess.h
- COP0_REG_TagHi : mipscopaccess.h
- COP0_REG_TagLo : mipscopaccess.h
- COP0_REG_Wired : mipscopaccess.h
- core1_bits : audsrv.c
- core1_channels : audsrv.c
- core1_freq : audsrv.c
- core1_sample_shift : audsrv.c
- core1_volume : audsrv.c
- count : usbhdfsd-common.h
- CPU_CONFIG : kernel.h
- CPU_DATA_CACHE : kernel.h
- CPUCLK : sio.c
- CpuDisableIntr() : intrman.h
- CpuEnableIntr() : intrman.h
- CpuInvokeInKmode() : intrman.h
- CpuResumeIntr() : intrman.h
- CpuSuspendIntr() : intrman.h
- create_local_light() : math3d.h
- create_local_screen() : math3d.h
- create_local_world() : math3d.h
- create_thread() : common.c , common.h
- create_view_screen() : math3d.h
- create_world_view() : math3d.h
- CRTC_SETTINGS_BLENDRC1 : libgs.h
- CRTC_SETTINGS_BLENDVAL : libgs.h
- CRTC_SETTINGS_EN1 : libgs.h
- CRTC_SETTINGS_EN2 : libgs.h
- CRTC_SETTINGS_ENBOTH : libgs.h
- CRTC_SETTINGS_OUTRC1 : libgs.h
- CRTC_SETTINGS_OUTRC2 : libgs.h
- CRTC_SETTINGS_STYLEBG : libgs.h
- CRTC_SETTINGS_STYLERC1 : libgs.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_d.html>

Here is a list of all documented functions, variables, defines, enums, and typedefs with links to the documentation:
###### - d -
- DATE_FORMAT_TYPES : osd_config.h
- DEFAULT_ALIGNMENT : alloc.c
- demux() : upsamplers.c
- dev_info_list : devscan.c
- devfs_check_devname() : devfs.c
- devfs_close() : devfs.c
- devfs_create_device() : devfs.c
- devfs_dclose() : devfs.c
- devfs_delete_device() : devfs.c
- DEVFS_DEVTYPE_BLOCK : devfs.h
- DEVFS_DEVTYPE_CHAR : devfs.h
- DEVFS_DEVTYPE_STREAM : devfs.h
- devfs_devtypes : devfs.h
- devfs_dopen() : devfs.c
- devfs_fill_dirent() : devfs.c
- devfs_find_deviceid() : devfs.c
- devfs_find_devicename() : devfs.c
- devfs_getstat() : devfs.c
- devfs_ioctl() : devfs.c
- devfs_ioctl2() : devfs.c
- DEVFS_IOCTL_GETDESC : devfs.h
- DEVFS_IOCTL_TYPE_1 : devfs.h
- DEVFS_IOCTL_TYPE_2 : devfs.h
- devfs_lseek() : devfs.c
- devfs_lseek64() : devfs.c
- DEVFS_MAX_DESC_LENGTH : devfs.h
- DEVFS_MAX_DEVNAME_LENGTH : devfs.h
- DEVFS_MAX_SUBDEVS : devfs.h
- DEVFS_MODE_EX : devfs.h
- DEVFS_MODE_R : devfs.h
- DEVFS_MODE_RW : devfs.h
- DEVFS_MODE_W : devfs.h
- devfs_open() : devfs.c
- devfs_read() : devfs.c
- devfs_subdev_modes : devfs.h
- devfs_subdev_to_str() : devfs.c
- devfs_write() : devfs.c
- DevFSAddDevice() : devfs.h , devfs.c
- DevFSAddSubDevice() : devfs.h , devfs.c
- DevFSDelDevice() : devfs.h , devfs.c
- DevFSDelSubDevice() : devfs.h , devfs.c
- devices : ps2kbd.c , ps2mouse.c
- devscan_getdevlist() : devscan.c , devscan.h
- devscan_getmodule() : devscan.c , devscan.h
- devscan_gettype() : devscan.c , devscan.h
- DEVSCAN_MASK : devscan.h
- DEVSCAN_MAX : devscan.h
- devscan_setup() : devscan.c , devscan.h
- DisableDispatchIntr() : intrman.h
- DisableIntr() : intrman.h
- dma_channel_fast_waits() : dma.h
- dma_channel_initialize() : dma.h
- dma_channel_receive_chain() : dma.h
- dma_channel_receive_normal() : dma.h
- dma_channel_send_chain() : dma.h
- dma_channel_send_chain_ucab() : dma.h
- dma_channel_send_normal() : dma.h
- dma_channel_send_normal_ucab() : dma.h
- dma_channel_send_packet2() : dma.h
- dma_channel_shutdown() : dma.h
- dma_channel_wait() : dma.h
- DMA_REG_CTRL : dma_registers.h
- DMA_REG_ENABLER : dma_registers.h
- DMA_REG_ENABLEW : dma_registers.h
- DMA_REG_PCR : dma_registers.h
- DMA_REG_RBOR : dma_registers.h
- DMA_REG_RBSR : dma_registers.h
- DMA_REG_SQWC : dma_registers.h
- DMA_REG_STADR : dma_registers.h
- DMA_REG_STAT : dma_registers.h
- DMA_SET_CHCR : dma_registers.h
- DMA_TAG_CALL : dma_tags.h
- DMA_TAG_CNT : dma_tags.h
- DMA_TAG_CNTS : dma_tags.h
- DMA_TAG_END : dma_tags.h
- DMA_TAG_NEXT : dma_tags.h
- DMA_TAG_REF : dma_tags.h
- DMA_TAG_REFE : dma_tags.h
- DMA_TAG_REFS : dma_tags.h
- DMA_TAG_RET : dma_tags.h
- dma_wait_fast() : dma.h
- DMAC_CHCR_CO : dmacman.h
- DMAC_CHCR_DR : dmacman.h
- DMAC_CHCR_LI : dmacman.h
- DMAC_CHCR_TR : dmacman.h
- DMAE_DISABLE : dma_registers.h
- DMATAG_CALL : dma_tags.h
- DMATAG_CNT : dma_tags.h
- DMATAG_CNTS : dma_tags.h
- DMATAG_END : dma_tags.h
- DMATAG_NEXT : dma_tags.h
- DMATAG_REF : dma_tags.h
- DMATAG_REFE : dma_tags.h
- DMATAG_REFS : dma_tags.h
- DMATAG_RET : dma_tags.h
- dns_found_callback : tcpip.h
- DNS_TMR_INTERVAL : tcpip.h
- draw_alpha_blending() : draw_blending.h
- draw_alpha_correction() : draw_blending.h
- draw_arc_filled() : draw2d.h
- draw_arc_outline() : draw2d.h
- draw_clear() : draw.h
- draw_clut_offset() : draw_buffers.h
- draw_clutbuffer() : draw_buffers.h
- draw_color_clamping() : draw_masking.h
- draw_convert_rgbaq() : draw3d.h
- draw_convert_rgbq() : draw3d.h
- draw_convert_st() : draw3d.h
- draw_convert_xyz() : draw3d.h
- draw_disable_blending() : draw2d.h
- draw_disable_tests() : draw_tests.h
- draw_dither_matrix() : draw_dithering.h
- draw_dithering() : draw_dithering.h
- draw_enable_blending() : draw2d.h
- draw_enable_tests() : draw_tests.h
- draw_finish() : draw.h
- draw_fog_color() : draw_fog.h
- draw_framebuffer() : draw_buffers.h
- draw_line() : draw2d.h
- draw_log2() : draw_buffers.h
- draw_mipmap1() : draw_sampling.h
- draw_mipmap2() : draw_sampling.h
- draw_pixel_alpha_control() : draw_blending.h
- draw_pixel_test() : draw_tests.h
- draw_point() : draw2d.h
- draw_prim_end() : draw3d.h
- draw_prim_start() : draw3d.h
- draw_primitive_override() : draw_primitives.h
- draw_primitive_override_setting() : draw_primitives.h
- draw_primitive_xyoffset() : draw_primitives.h
- draw_rect_filled() : draw2d.h
- draw_rect_filled_strips() : draw2d.h
- draw_rect_outline() : draw2d.h
- draw_rect_textured() : draw2d.h
- draw_rect_textured_strips() : draw2d.h
- draw_round_rect_filled() : draw2d.h
- draw_round_rect_outline() : draw2d.h
- draw_scan_masking() : draw_masking.h
- draw_scissor_area() : draw_tests.h
- draw_setup_environment() : draw.h
- DRAW_STQ2_REGLIST : draw3d.h
- draw_texture_expand_alpha() : draw_sampling.h
- draw_texture_flush() : draw.h
- draw_texture_sampling() : draw_sampling.h
- draw_texture_transfer() : draw.h
- draw_texture_wrapping() : draw_sampling.h
- draw_texturebuffer() : draw_buffers.h
- draw_triangle_filled() : draw2d.h
- draw_triangle_outline() : draw2d.h
- draw_wait_finish() : draw.h
- DRAW_XYZ_REGLIST : draw3d.h
- draw_zbuffer() : draw_buffers.h
- DTEST_METHOD_PASS_ZERO : draw_tests.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_defs.html>

###### - _ -
- _B : ctype.h
- _C : ctype.h
- _EX_DBG_STACK_SIZE : iopdebug_defs.h
- _EX_DEF_STACK_SIZE : iopdebug_defs.h
- _L : ctype.h
- _N : ctype.h
- _P : ctype.h
- _S : ctype.h
- _U : ctype.h
- _X : ctype.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_defs_a.html>

###### - a -
- A_PS1_1F801018 : iop_regs.h
- A_PS1_1F801020 : iop_regs.h
- ALPHA_CORRECT_RGBA32 : draw_blending.h
- ALPHA_EXPAND_NORMAL : draw_sampling.h
- APA_FLAG_SUB : hdd-ioctl.h
- APA_MAXSUB : hdd-ioctl.h
- APA_TYPE_MBR : hdd-ioctl.h
- ATA_AIF_HDD_BASE : atahw.h
- AUDSRV_ERR_NOERROR : audsrv.h
- AUDSRV_FORMAT_OK : audsrv.h , audsrv_rpc.h
- AUDSRV_INIT : audsrv_rpc.h , audsrv.h , audsrv_rpc.h
- AUDSRV_INIT_ADPCM : audsrv_rpc.h
- AUDSRV_PLAY_CD : audsrv_rpc.h , audsrv.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_defs_b.html>

###### - b -
- BLEND_COLOR_SOURCE : draw_blending.h
- BPC_BED : hwbp.h
- BPC_DKE : hwbp.h
- BPC_DRB : hwbp.h
- BPC_DRE : hwbp.h
- BPC_DSE : hwbp.h
- BPC_DTE : hwbp.h
- BPC_DUE : hwbp.h
- BPC_DVE : hwbp.h
- BPC_DWB : hwbp.h
- BPC_DWE : hwbp.h
- BPC_DXE : hwbp.h
- BPC_IAB : hwbp.h
- BPC_IAE : hwbp.h
- BPC_IKE : hwbp.h
- BPC_ISE : hwbp.h
- BPC_ITE : hwbp.h
- BPC_IUE : hwbp.h
- BPC_IXE : hwbp.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_defs_c.html>

###### - c -
- CAM_ERROR_BADHANDLE : ps2cam_rpc.h , ps2cam.h
- CAM_ERROR_BADRANGE : ps2cam.h , ps2cam_rpc.h
- CAM_ERROR_COMMUNKNOWN : ps2cam_rpc.h , ps2cam.h
- CAM_ERROR_DEVNOTREADY : ps2cam.h , ps2cam_rpc.h
- CAM_ERROR_DISCONNECTED : ps2cam_rpc.h , ps2cam.h
- CAM_ERROR_MAXHANDLE : ps2cam_rpc.h , ps2cam.h
- CAM_ERROR_NODEVICE : ps2cam_rpc.h , ps2cam.h
- CAM_ERROR_NONE : ps2cam.h , ps2cam_rpc.h
- CAM_ERROR_UNKNOWN : ps2cam_rpc.h , ps2cam.h
- CAM_STATUS_CONNECTED : ps2cam_rpc.h , ps2cam.h
- CAM_STATUS_CONNECTEDREADY : ps2cam_rpc.h , ps2cam.h
- CAM_STATUS_NOTCONNECTED : ps2cam_rpc.h , ps2cam.h
- CD_SERVER_NCMD : ncmd.c
- CD_SERVER_POFF : libcdvd.c
- CD_SERVER_SCMD : scmd.c
- CdlLEDEjectBlue : libcdvd-common.h
- CdlLEDPowerGreen : libcdvd-common.h
- CdlLEDPowerRed : libcdvd-common.h
- CdlLEDPowerYellow : libcdvd-common.h
- CdlMAXDIR : libcdvd-common.h
- CdlMAXFILE : libcdvd-common.h
- CdlMAXLEVEL : libcdvd-common.h
- CdlMAXTOC : libcdvd-common.h
- CdlRCDisableEject : libcdvd-common.h
- CdlRCDisablePowerOff : libcdvd-common.h
- CdlRCDisablePowerOn : libcdvd-common.h
- CdlRCDisablePowerReset : libcdvd-common.h
- CdlRCDisableReset : libcdvd-common.h
- CdlRTCStatClockBatteryMonitoringVoltageProblem : libcdvd-common.h
- CdlRTCStatClockStopDetected : libcdvd-common.h
- CdlRTCStatCommandError : libcdvd-common.h
- CdlRTCStatCTLRegProblem : libcdvd-common.h
- CdlWakeUpReasonExtraGameReset : libcdvd-common.h
- CdlWakeUpReasonExtraPowerOn : libcdvd-common.h
- CdlWakeUpReasonExtraReset : libcdvd-common.h
- CdlWakeUpReasonExtraSlotIn : libcdvd-common.h
- CdlWakeUpReasonExtraTimer : libcdvd-common.h
- CdlWakeUpReasonMainDevice : libcdvd-common.h
- CdlWakeUpReasonMainPowerOn : libcdvd-common.h
- CdlWakeUpReasonMainReset : libcdvd-common.h
- CdlWakeUpReasonMainTimer : libcdvd-common.h
- CDVD_TRAY_STAT_OPEN : iop_regs.h
- CLUT_NO_LOAD : draw_buffers.h
- CLUT_STORAGE_MODE1 : draw_buffers.h
- COLOR_CLAMP_MASK : draw_masking.h
- CPU_DATA_CACHE : kernel.h
- CPUCLK : sio.c
- CRTC_SETTINGS_BLENDRC1 : libgs.h
- CRTC_SETTINGS_BLENDVAL : libgs.h
- CRTC_SETTINGS_EN1 : libgs.h
- CRTC_SETTINGS_EN2 : libgs.h
- CRTC_SETTINGS_ENBOTH : libgs.h
- CRTC_SETTINGS_OUTRC1 : libgs.h
- CRTC_SETTINGS_OUTRC2 : libgs.h
- CRTC_SETTINGS_STYLEBG : libgs.h
- CRTC_SETTINGS_STYLERC1 : libgs.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_defs_d.html>

###### - d -
- DEFAULT_ALIGNMENT : alloc.c
- DEVFS_IOCTL_GETDESC : devfs.h
- DEVFS_IOCTL_TYPE_1 : devfs.h
- DEVFS_IOCTL_TYPE_2 : devfs.h
- DEVFS_MAX_DESC_LENGTH : devfs.h
- DEVFS_MAX_DEVNAME_LENGTH : devfs.h
- DEVFS_MAX_SUBDEVS : devfs.h
- DEVSCAN_MASK : devscan.h
- DEVSCAN_MAX : devscan.h
- DMA_REG_CTRL : dma_registers.h
- DMA_REG_ENABLER : dma_registers.h
- DMA_REG_ENABLEW : dma_registers.h
- DMA_REG_PCR : dma_registers.h
- DMA_REG_RBOR : dma_registers.h
- DMA_REG_RBSR : dma_registers.h
- DMA_REG_SQWC : dma_registers.h
- DMA_REG_STADR : dma_registers.h
- DMA_REG_STAT : dma_registers.h
- DMA_SET_CHCR : dma_registers.h
- DMA_TAG_CALL : dma_tags.h
- DMA_TAG_CNT : dma_tags.h
- DMA_TAG_CNTS : dma_tags.h
- DMA_TAG_END : dma_tags.h
- DMA_TAG_NEXT : dma_tags.h
- DMA_TAG_REF : dma_tags.h
- DMA_TAG_REFE : dma_tags.h
- DMA_TAG_REFS : dma_tags.h
- DMA_TAG_RET : dma_tags.h
- DMAC_CHCR_CO : dmacman.h
- DMAC_CHCR_DR : dmacman.h
- DMAC_CHCR_LI : dmacman.h
- DMAC_CHCR_TR : dmacman.h
- DMAE_DISABLE : dma_registers.h
- DMATAG_CALL : dma_tags.h
- DMATAG_CNT : dma_tags.h
- DMATAG_CNTS : dma_tags.h
- DMATAG_END : dma_tags.h
- DMATAG_NEXT : dma_tags.h
- DMATAG_REF : dma_tags.h
- DMATAG_REFE : dma_tags.h
- DMATAG_REFS : dma_tags.h
- DMATAG_RET : dma_tags.h
- DNS_TMR_INTERVAL : tcpip.h
- DRAW_STQ2_REGLIST : draw3d.h
- DRAW_XYZ_REGLIST : draw3d.h
- DTEST_METHOD_PASS_ZERO : draw_tests.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_defs_e.html>

###### - e -
- E2BIG : errno.h
- EA_MULTI : thevent.h
- EA_SINGLE : thevent.h
- EACCES : errno.h
- EADDRINUSE : errno.h
- EADDRNOTAVAIL : errno.h
- EADV : errno.h
- EAFNOSUPPORT : errno.h
- EAGAIN : errno.h
- EAI_NONAME : tcpip.h
- EALREADY : errno.h
- EBADE : errno.h
- EBADF : errno.h
- EBADFD : errno.h
- EBADMSG : errno.h
- EBADR : errno.h
- EBADRQC : errno.h
- EBADSLT : errno.h
- EBFONT : errno.h
- EBUSY : errno.h
- ECANCELED : errno.h
- ECASECLASH : errno.h
- ECHILD : errno.h
- ECHRNG : errno.h
- ECOMM : errno.h
- ECONNABORTED : errno.h
- ECONNREFUSED : errno.h
- ECONNRESET : errno.h
- EDEADLK : errno.h
- EDEADLOCK : errno.h
- EDESTADDRREQ : errno.h
- EDOM : errno.h
- EDOTDOT : errno.h
- EDQUOT : errno.h
- EE_CAUSE_SIO : ee_cop0_defs.h
- EEXIST : errno.h
- EFAULT : errno.h
- EFBIG : errno.h
- EFORMAT : errno.h
- EFTYPE : errno.h
- EHOSTDOWN : errno.h
- EHOSTUNREACH : errno.h
- EIDRM : errno.h
- EILSEQ : errno.h
- EINPROGRESS : errno.h
- EINTR : errno.h
- EINVAL : errno.h
- EIO : errno.h
- EISCONN : errno.h
- EISDIR : errno.h
- EL2HLT : errno.h
- EL2NSYNC : errno.h
- EL3HLT : errno.h
- EL3RST : errno.h
- ELBIN : errno.h
- ELIBACC : errno.h
- ELIBBAD : errno.h
- ELIBEXEC : errno.h
- ELIBMAX : errno.h
- ELIBSCN : errno.h
- ELNRNG : errno.h
- ELOOP : errno.h
- EMFILE : errno.h
- EMLINK : errno.h
- EMSGSIZE : errno.h
- EMULTIHOP : errno.h
- ENAMETOOLONG : errno.h
- ENETDOWN : errno.h
- ENETRESET : errno.h
- ENETUNREACH : errno.h
- ENFILE : errno.h
- ENMFILE : errno.h
- ENOANO : errno.h
- ENOBUFS : errno.h
- ENOCSI : errno.h
- ENODATA : errno.h
- ENODEV : errno.h
- ENOENT : errno.h
- ENOEXEC : errno.h
- ENOLCK : errno.h
- ENOLINK : errno.h
- ENOMEDIUM : errno.h
- ENOMEM : errno.h
- ENOMSG : errno.h
- ENONET : errno.h
- ENOPKG : errno.h
- ENOPROTOOPT : errno.h
- ENOSHARE : errno.h
- ENOSPC : errno.h
- ENOSR : errno.h
- ENOSTR : errno.h
- ENOSYS : errno.h
- ENOTBLK : errno.h
- ENOTCONN : errno.h
- ENOTDIR : errno.h
- ENOTEMPTY : errno.h
- ENOTRECOVERABLE : errno.h
- ENOTSOCK : errno.h
- ENOTSUP : errno.h
- ENOTTY : errno.h
- ENOTUNIQ : errno.h
- ENXIO : errno.h
- EOPNOTSUPP : errno.h
- EOVERFLOW : errno.h
- EOWNERDEAD : errno.h
- EPERM : errno.h
- EPFNOSUPPORT : errno.h
- EPIPE : errno.h
- EPROCLIM : errno.h
- EPROTO : errno.h
- EPROTONOSUPPORT : errno.h
- EPROTOTYPE : errno.h
- ERANGE : errno.h
- EREMCHG : errno.h
- EREMOTE : errno.h
- ERL_FLAG_CLEAR : erl.h
- ERL_FLAG_STATIC : erl.h
- ERL_FLAG_STICKY : erl.h
- EROFS : errno.h
- ESHUTDOWN : errno.h
- ESOCKTNOSUPPORT : errno.h
- ESPIPE : errno.h
- ESRCH : errno.h
- ESRMNT : errno.h
- ESTALE : errno.h
- ESTRPIPE : errno.h
- ETIME : errno.h
- ETIMEDOUT : errno.h
- ETOOMANYREFS : errno.h
- ETXTBSY : errno.h
- EUNATCH : errno.h
- EUNSUP : errno.h
- EUSERS : errno.h
- EWOULDBLOCK : errno.h
- EXDEV : errno.h
- EXFULL : errno.h
- EYETOY_ALTERNATE_SIZE_0 : ps2cam.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_defs_f.html>

###### - f -
- fdh_get : ps2_fio.c
- fdh_getfdtype : ps2_fio.c
- fdh_getrealfd : ps2_fio.c
- fdh_getused : ps2_fio.c
- FILEXIO_DEFAULT_RW_BUFFER_SIZE : fileXio.h
- FILEXIO_DT_FSEXT : fileXio.h
- FIO_DEFAULT_XFER_SIZE : fileio-common.h
- FIO_S_IFDIR : iox_stat.h
- FIO_S_IFLNK : iox_stat.h
- FIO_S_IFMT : iox_stat.h
- FIO_S_IFREG : iox_stat.h
- FIO_S_IRGRP : iox_stat.h
- FIO_S_IROTH : iox_stat.h
- FIO_S_IRUSR : iox_stat.h
- FIO_S_IRWXG : iox_stat.h
- FIO_S_IRWXO : iox_stat.h
- FIO_S_IRWXU : iox_stat.h
- FIO_S_ISGID : iox_stat.h
- FIO_S_ISUID : iox_stat.h
- FIO_S_ISVTX : iox_stat.h
- FIO_S_IWGRP : iox_stat.h
- FIO_S_IWOTH : iox_stat.h
- FIO_S_IWUSR : iox_stat.h
- FIO_S_IXGRP : iox_stat.h
- FIO_S_IXOTH : iox_stat.h
- FIO_S_IXUSR : iox_stat.h
- FIO_SO_IFDIR : iox_stat.h
- FIO_SO_IFLNK : iox_stat.h
- FIO_SO_IFMT : iox_stat.h
- FIO_SO_IFREG : iox_stat.h
- FIO_SO_IROTH : iox_stat.h
- FIO_SO_IWOTH : iox_stat.h
- FIO_SO_IXOTH : iox_stat.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_defs_g.html>

###### - g -
- GIF_BLOCK_SIZE : gif_tags.h
- GIF_FLG_IMAGE : gif_tags.h
- GIF_FLG_PACKED : gif_tags.h
- GIF_FLG_REGLIST : gif_tags.h
- GIF_PRE_DISABLE : gif_tags.h
- GIF_PRE_ENABLE : gif_tags.h
- GIF_PRIM_LINE : gif_tags.h
- GIF_PRIM_LINE_STRIP : gif_tags.h
- GIF_PRIM_POINT : gif_tags.h
- GIF_PRIM_SPRITE : gif_tags.h
- GIF_PRIM_TRIANGLE : gif_tags.h
- GIF_PRIM_TRIANGLE_FAN : gif_tags.h
- GIF_PRIM_TRIANGLE_STRIP : gif_tags.h
- gif_rd_ad : libgs.h
- gif_rd_nop : libgs.h
- GIF_REG_AD : gif_tags.h
- GIF_REG_CLAMP : gif_tags.h
- GIF_REG_CLAMP_1 : gif_tags.h
- GIF_REG_CLAMP_2 : gif_tags.h
- GIF_REG_CNT : gif_registers.h
- GIF_REG_CTRL : gif_registers.h
- GIF_REG_FOG : gif_tags.h
- GIF_REG_MODE : gif_registers.h
- GIF_REG_NOP : gif_tags.h
- GIF_REG_P3CNT : gif_registers.h
- GIF_REG_P3TAG : gif_registers.h
- GIF_REG_PRIM : gif_tags.h
- GIF_REG_RGBAQ : gif_tags.h
- GIF_REG_ST : gif_tags.h
- GIF_REG_STAT : gif_registers.h
- GIF_REG_TAG0 : gif_registers.h
- GIF_REG_TAG1 : gif_registers.h
- GIF_REG_TAG2 : gif_registers.h
- GIF_REG_TAG3 : gif_registers.h
- GIF_REG_TEX0 : gif_tags.h
- GIF_REG_TEX0_1 : gif_tags.h
- GIF_REG_TEX0_2 : gif_tags.h
- GIF_REG_UV : gif_tags.h
- GIF_REG_XYZ2 : gif_tags.h
- GIF_REG_XYZ3 : gif_tags.h
- GIF_REG_XYZF2 : gif_tags.h
- GIF_REG_XYZF3 : gif_tags.h
- GRAPH_ALIGN_BLOCK : graph_vram.h
- GRAPH_ALIGN_PAGE : graph_vram.h
- GRAPH_BLEND_RC2 : graph.h
- GRAPH_DISABLE : graph.h
- GRAPH_GCONT_RGB : graph.h
- GRAPH_MODE_AUTO : graph.h
- GRAPH_MODE_HDTV_1080I : graph.h
- GRAPH_MODE_HDTV_480P : graph.h
- GRAPH_MODE_HDTV_576P : graph.h
- GRAPH_MODE_HDTV_720P : graph.h
- GRAPH_MODE_NTSC : graph.h
- GRAPH_MODE_PAL : graph.h
- GRAPH_MODE_VGA_1024_60 : graph.h
- GRAPH_MODE_VGA_1024_70 : graph.h
- GRAPH_MODE_VGA_1024_75 : graph.h
- GRAPH_MODE_VGA_1024_85 : graph.h
- GRAPH_MODE_VGA_1280_60 : graph.h
- GRAPH_MODE_VGA_1280_75 : graph.h
- GRAPH_MODE_VGA_640_60 : graph.h
- GRAPH_MODE_VGA_640_72 : graph.h
- GRAPH_MODE_VGA_640_75 : graph.h
- GRAPH_MODE_VGA_640_85 : graph.h
- GRAPH_MODE_VGA_800_56 : graph.h
- GRAPH_MODE_VGA_800_60 : graph.h
- GRAPH_MODE_VGA_800_72 : graph.h
- GRAPH_MODE_VGA_800_75 : graph.h
- GRAPH_MODE_VGA_800_85 : graph.h
- GRAPH_RC1_ALPHA : graph.h
- GRAPH_VALUE_RC1 : graph.h
- GRAPH_VRAM_MAX_WORDS : graph_vram.h
- GS_CLUT_32 : libgs.h
- GS_FFMD_FIELD : libgs.h
- GS_FFMD_FRAME : libgs.h
- gs_g_alpha_1 : libgs.h
- gs_g_alpha_2 : libgs.h
- gs_g_bitbltbuf : libgs.h
- gs_g_clamp_1 : libgs.h
- gs_g_clamp_2 : libgs.h
- gs_g_colclamp : libgs.h
- gs_g_dimx : libgs.h
- gs_g_dthe : libgs.h
- gs_g_fba_1 : libgs.h
- gs_g_fba_2 : libgs.h
- gs_g_fog : libgs.h
- gs_g_fogcol : libgs.h
- gs_g_frame_1 : libgs.h
- gs_g_frame_2 : libgs.h
- gs_g_miptbp1_1 : libgs.h
- gs_g_miptbp1_2 : libgs.h
- gs_g_miptbp2_1 : libgs.h
- gs_g_miptbp2_2 : libgs.h
- gs_g_nop : libgs.h
- gs_g_pabe : libgs.h
- gs_g_prim : libgs.h
- gs_g_prmode : libgs.h
- gs_g_prmodecont : libgs.h
- gs_g_rgbaq : libgs.h
- gs_g_scanmsk : libgs.h
- gs_g_scissor_1 : libgs.h
- gs_g_scissor_2 : libgs.h
- gs_g_st : libgs.h
- gs_g_test_1 : libgs.h
- gs_g_test_2 : libgs.h
- gs_g_tex0_1 : libgs.h
- gs_g_tex0_2 : libgs.h
- gs_g_tex2_1 : libgs.h
- gs_g_tex2_2 : libgs.h
- gs_g_texa : libgs.h
- gs_g_texflush : libgs.h
- gs_g_trxdir : libgs.h
- gs_g_trxpos : libgs.h
- gs_g_trxreg : libgs.h
- gs_g_uv : libgs.h
- gs_g_xyoffset_1 : libgs.h
- gs_g_xyoffset_2 : libgs.h
- gs_g_xyz2 : libgs.h
- gs_g_xyz3 : libgs.h
- gs_g_xyzf2 : libgs.h
- gs_g_xyzf3 : libgs.h
- gs_g_zbuf_1 : libgs.h
- gs_g_zbuf_2 : libgs.h
- GS_INIT_DRAW_RESET : libgs.h
- GS_INIT_RESET : libgs.h
- gs_p_bgcolor : libgs.h
- gs_p_busdir : libgs.h
- gs_p_csr : libgs.h
- gs_p_dispfb1 : libgs.h
- gs_p_dispfb2 : libgs.h
- gs_p_display1 : libgs.h
- gs_p_display2 : libgs.h
- gs_p_imr : libgs.h
- gs_p_pmode : libgs.h
- gs_p_siglblid : libgs.h
- gs_p_smode1 : libgs.h
- gs_p_smode2 : libgs.h
- GS_PIXMODE_32 : libgs.h
- GS_PRIM_LINE : gs_gp.h
- GS_PRIM_LINE_STRIP : gs_gp.h
- GS_PRIM_POINT : gs_gp.h
- GS_PRIM_SPRITE : gs_gp.h
- GS_PRIM_TRIANGLE : gs_gp.h
- GS_PRIM_TRIANGLE_FAN : gs_gp.h
- GS_PRIM_TRIANGLE_STRIP : gs_gp.h
- GS_PSM_16 : gs_psm.h
- GS_PSM_16S : gs_psm.h
- GS_PSM_24 : gs_psm.h
- GS_PSM_32 : gs_psm.h
- GS_PSM_4 : gs_psm.h
- GS_PSM_4HH : gs_psm.h
- GS_PSM_4HL : gs_psm.h
- GS_PSM_8 : gs_psm.h
- GS_PSM_8H : gs_psm.h
- GS_PSM_PS24 : gs_psm.h
- GS_PSMZ_16 : gs_psm.h
- GS_PSMZ_16S : gs_psm.h
- GS_PSMZ_24 : gs_psm.h
- GS_PSMZ_32 : gs_psm.h
- GS_REG_ALPHA : gs_gp.h
- GS_REG_ALPHA_1 : gs_gp.h
- GS_REG_ALPHA_2 : gs_gp.h
- GS_REG_BGCOLOR : gs_privileged.h
- GS_REG_BITBLTBUF : gs_gp.h
- GS_REG_BUSDIR : gs_privileged.h
- GS_REG_CLAMP : gs_gp.h
- GS_REG_CLAMP_1 : gs_gp.h
- GS_REG_CLAMP_2 : gs_gp.h
- GS_REG_COLCLAMP : gs_gp.h
- GS_REG_CSR : gs_privileged.h
- GS_REG_DIMX : gs_gp.h
- GS_REG_DISPFB1 : gs_privileged.h
- GS_REG_DISPFB2 : gs_privileged.h
- GS_REG_DISPLAY1 : gs_privileged.h
- GS_REG_DISPLAY2 : gs_privileged.h
- GS_REG_DTHE : gs_gp.h
- GS_REG_EXTBUF : gs_privileged.h
- GS_REG_EXTDATA : gs_privileged.h
- GS_REG_EXTWRITE : gs_privileged.h
- GS_REG_FBA : gs_gp.h
- GS_REG_FBA_1 : gs_gp.h
- GS_REG_FBA_2 : gs_gp.h
- GS_REG_FINISH : gs_gp.h
- GS_REG_FOG : gs_gp.h
- GS_REG_FOGCOL : gs_gp.h
- GS_REG_FRAME : gs_gp.h
- GS_REG_FRAME_1 : gs_gp.h
- GS_REG_FRAME_2 : gs_gp.h
- GS_REG_HWREG : gs_gp.h
- GS_REG_IMR : gs_privileged.h
- GS_REG_LABEL : gs_gp.h
- GS_REG_MIPTBP1 : gs_gp.h
- GS_REG_MIPTBP1_1 : gs_gp.h
- GS_REG_MIPTBP1_2 : gs_gp.h
- GS_REG_MIPTBP2 : gs_gp.h
- GS_REG_MIPTBP2_1 : gs_gp.h
- GS_REG_MIPTBP2_2 : gs_gp.h
- GS_REG_NOP : gs_gp.h
- GS_REG_PABE : gs_gp.h
- GS_REG_PMODE : gs_privileged.h
- GS_REG_PRIM : gs_gp.h
- GS_REG_PRMODE : gs_gp.h
- GS_REG_PRMODECONT : gs_gp.h
- GS_REG_RGBAQ : gs_gp.h
- GS_REG_SCANMSK : gs_gp.h
- GS_REG_SCISSOR : gs_gp.h
- GS_REG_SCISSOR_1 : gs_gp.h
- GS_REG_SCISSOR_2 : gs_gp.h
- GS_REG_SIGLBLID : gs_privileged.h
- GS_REG_SIGNAL : gs_gp.h
- GS_REG_SMODE1 : gs_privileged.h
- GS_REG_SMODE2 : gs_privileged.h
- GS_REG_SRFSH : gs_privileged.h
- GS_REG_ST : gs_gp.h
- GS_REG_SYNCH1 : gs_privileged.h
- GS_REG_SYNCH2 : gs_privileged.h
- GS_REG_SYNCHV : gs_privileged.h
- GS_REG_TEST : gs_gp.h
- GS_REG_TEST_1 : gs_gp.h
- GS_REG_TEST_2 : gs_gp.h
- GS_REG_TEX0 : gs_gp.h
- GS_REG_TEX0_1 : gs_gp.h
- GS_REG_TEX0_2 : gs_gp.h
- GS_REG_TEX1 : gs_gp.h
- GS_REG_TEX1_1 : gs_gp.h
- GS_REG_TEX1_2 : gs_gp.h
- GS_REG_TEX2 : gs_gp.h
- GS_REG_TEX2_1 : gs_gp.h
- GS_REG_TEX2_2 : gs_gp.h
- GS_REG_TEXA : gs_gp.h
- GS_REG_TEXCLUT : gs_gp.h
- GS_REG_TEXFLUSH : gs_gp.h
- GS_REG_TRXDIR : gs_gp.h
- GS_REG_TRXPOS : gs_gp.h
- GS_REG_TRXREG : gs_gp.h
- GS_REG_UV : gs_gp.h
- GS_REG_XYOFFSET : gs_gp.h
- GS_REG_XYOFFSET_1 : gs_gp.h
- GS_REG_XYOFFSET_2 : gs_gp.h
- GS_REG_XYZ2 : gs_gp.h
- GS_REG_XYZ3 : gs_gp.h
- GS_REG_XYZF2 : gs_gp.h
- GS_REG_XYZF3 : gs_gp.h
- GS_REG_ZBUF : gs_gp.h
- GS_REG_ZBUF_1 : gs_gp.h
- GS_REG_ZBUF_2 : gs_gp.h
- GS_SET_SMODE1 : libgs.h
- GS_TEX_32 : libgs.h
- GS_TEX_CALC : libgs.h
- GS_TEX_FIXED : libgs.h
- GS_TEX_MIPMAP_AUTO : libgs.h
- GS_TEX_MIPMAP_DEFINE : libgs.h
- GS_ZBUF_16 : gs_psm.h
- GS_ZBUF_16S : gs_psm.h
- GS_ZBUF_24 : gs_psm.h
- GS_ZBUF_32 : gs_psm.h
- GS_ZBUFF_32 : libgs.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_defs_h.html>

###### - h -
- HDDCTLDRIVEREAD : ioctl.h
- HDDCTLDRIVEWRITE : ioctl.h
- HDDCTLFLUSH : ioctl.h
- HDDCTLGETDATE : ioctl.h
- HDDCTLGETERROR : ioctl.h
- HDDCTLGETERRORID : ioctl.h
- HDDCTLGETFMTVER : ioctl.h
- HDDCTLGETMAXSECT : ioctl.h
- HDDCTLGETSMARTSTAT : ioctl.h
- HDDCTLGETSTATUS : ioctl.h
- HDDCTLGETTOTALSECT : ioctl.h
- HDDCTLINSTALLOSD : ioctl.h
- HDDCTLSCEIDENTIFY : ioctl.h
- HDDCTLSETIDLE : ioctl.h
- HDDCTLSHUTDOWN : ioctl.h
- HDDCTLSWAPTMP : ioctl.h
- HDDIOCADDSUB : ioctl.h
- HDDIOCDELSUB : ioctl.h
- HDDIOCDEVIO : ioctl.h
- HDDIOCFLUSH : ioctl.h
- HDDIOCGETERROR : ioctl.h
- HDDIOCGETSIZE : ioctl.h
- HDDIOCGETSUBS : ioctl.h
- HDDIOCSETERROR : ioctl.h
- HDIOC_FREESECTOR : hdd-ioctl.h
- HDIOC_GETERRORPARTNAME : hdd-ioctl.h
- HDIOC_MAXSECTOR : hdd-ioctl.h
- HDIOC_READSECTOR : hdd-ioctl.h
- HDIOC_SCEIDENTIFY : hdd-ioctl.h
- HDIOC_SETMAXLBA28 : hdd-ioctl.h
- HDIOC_SETOSDMBR : hdd-ioctl.h
- HDIOC_TOTALSECTOR : hdd-ioctl.h
- HDIOC_WRITESECTOR : hdd-ioctl.h
- HIOCGETPARTERROR : hdd-ioctl.h
- HIOCGETSIZE : hdd-ioctl.h
- HIOCSETPARTERROR : hdd-ioctl.h
- HIOCTRANSFER : hdd-ioctl.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_defs_i.html>

###### - i -
- INADDR_ANY : tcpip.h
- INADDR_BROADCAST : tcpip.h
- INADDR_LOOPBACK : tcpip.h
- INADDR_NONE : tcpip.h
- INIT_DMAC : kernel.h
- INVALID_HDEV : devfs.h
- IOP_CHCR_30 : iop_regs.h
- IOP_CHCR_CO : iop_regs.h
- IOP_CHCR_DR : iop_regs.h
- IOP_CHCR_LI : iop_regs.h
- IOP_CHCR_TR : iop_regs.h
- IOP_DCIC_D : iop_cop0_defs.h
- IOP_DCIC_DA : iop_cop0_defs.h
- IOP_DCIC_DAE : iop_cop0_defs.h
- IOP_DCIC_DB : iop_cop0_defs.h
- IOP_DCIC_DE : iop_cop0_defs.h
- IOP_DCIC_DL : iop_cop0_defs.h
- IOP_DCIC_DR : iop_cop0_defs.h
- IOP_DCIC_DW : iop_cop0_defs.h
- IOP_DCIC_I : iop_cop0_defs.h
- IOP_DCIC_IL : iop_cop0_defs.h
- IOP_DCIC_KD : iop_cop0_defs.h
- IOP_DCIC_PC : iop_cop0_defs.h
- IOP_DCIC_PCE : iop_cop0_defs.h
- IOP_DCIC_R : iop_cop0_defs.h
- IOP_DCIC_T : iop_cop0_defs.h
- IOP_DCIC_TE : iop_cop0_defs.h
- IOP_DCIC_TR : iop_cop0_defs.h
- IOP_DCIC_UD : iop_cop0_defs.h
- IOP_DCIC_W : iop_cop0_defs.h
- IOP_DT_FSEXT : iomanX.h
- IOP_EXCEPTION_ADEL : excepman.h
- IOP_EXCEPTION_ADES : excepman.h
- IOP_EXCEPTION_BP : excepman.h
- IOP_EXCEPTION_CPU : excepman.h
- IOP_EXCEPTION_DBE : excepman.h
- IOP_EXCEPTION_HDB : excepman.h
- IOP_EXCEPTION_IBE : excepman.h
- IOP_EXCEPTION_INT : excepman.h
- IOP_EXCEPTION_MOD : excepman.h
- IOP_EXCEPTION_OVF : excepman.h
- IOP_EXCEPTION_R13 : excepman.h
- IOP_EXCEPTION_R14 : excepman.h
- IOP_EXCEPTION_RI : excepman.h
- IOP_EXCEPTION_SYS : excepman.h
- IOP_EXCEPTION_TLBL : excepman.h
- IOP_EXCEPTION_TLBS : excepman.h
- IOP_MEM : ahx_rpc.c , sior_rpc.c
- IP4_ADDR : tcpip.h
- IP4_ADDR_ANY : tcpip.h
- IP4_ADDR_ANY4 : tcpip.h
- ip4_addr_copy : tcpip.h
- ip4_addr_get_network : tcpip.h
- ip4_addr_get_u32 : tcpip.h
- ip4_addr_isloopback : tcpip.h
- ip4_addr_netcmp : tcpip.h
- ip4_addr_set : tcpip.h
- ip4_addr_set_any : tcpip.h
- ip4_addr_set_hton : tcpip.h
- ip4_addr_set_loopback : tcpip.h
- ip4_addr_set_u32 : tcpip.h
- ip4_addr_set_zero : tcpip.h
- IP6_ADDR : tcpip.h
- IP6_ADDR_BLOCK1 : tcpip.h
- IP6_ADDR_BLOCK2 : tcpip.h
- IP6_ADDR_BLOCK3 : tcpip.h
- IP6_ADDR_BLOCK4 : tcpip.h
- IP6_ADDR_BLOCK5 : tcpip.h
- IP6_ADDR_BLOCK6 : tcpip.h
- IP6_ADDR_BLOCK7 : tcpip.h
- IP6_ADDR_BLOCK8 : tcpip.h
- ip6_addr_copy : tcpip.h
- ip6_addr_netcmp : tcpip.h
- IP6_ADDR_PART : tcpip.h
- ip6_addr_set : tcpip.h
- ip6_addr_set_any : tcpip.h
- ip6_addr_set_hton : tcpip.h
- ip6_addr_set_loopback : tcpip.h
- ip6_addr_set_zero : tcpip.h
- IP_ADDR_ANY : tcpip.h
- IPADDR2_COPY : tcpip.h
- IPADDR_ANY : tcpip.h
- IPADDR_BROADCAST : tcpip.h
- IPADDR_LOOPBACK : tcpip.h
- IPADDR_NONE : tcpip.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_defs_l.html>

###### - l -
- LCR_SCS_VAL : sio.c
- LEFT_ALIGN : font.h
- LIGHT_AMBIENT : math3d.h
- LIGHT_DIRECTIONAL : math3d.h
- LOD_FORMULAIC : draw_sampling.h
- LOD_MAG_NEAREST : draw_sampling.h
- LOD_MIPMAP_REGISTER : draw_sampling.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_defs_m.html>

###### - m -
- MAX_THREADS : kernel.h
- MAX_VOLUME : audsrv.h
- MC_ATTR_HIDDEN : libmc.h
- MC_ATTR_OBJECT : libmc.h
- MFD_OFF : dma_registers.h
- MIN : audsrv_internal.h
- MIN_VOLUME : audsrv.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_defs_n.html>

###### - n -
- NETIF_FLAG_BROADCAST : tcpip.h
- NETIF_FLAG_ETHARP : tcpip.h
- NETIF_FLAG_ETHERNET : tcpip.h
- NETIF_FLAG_IGMP : tcpip.h
- NETIF_FLAG_LINK_UP : tcpip.h
- NETIF_FLAG_MLD6 : tcpip.h
- NETIF_FLAG_UP : tcpip.h
- netif_get_client_data : tcpip.h
- netif_is_link_up : tcpip.h
- netif_is_up : tcpip.h
- NETIF_MAX_HWADDR_LEN : tcpip.h
- netif_set_client_data : tcpip.h
- NETMAN_NETIF_DIALUP : netman.h
- NETMAN_NETIF_ETH_LINK_DISABLE_PAUSE : netman.h
- NETMAN_NETIF_ETHERNET : netman.h
- NETMAN_NETIF_IN_USE : netman.h
- NETMAN_NETIF_LINK_UP : netman.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_defs_p.html>

###### - p -
- PACKET_F_ALLOC : sifrpc.c
- PFS_ZONE_SIZE : ps2_fio.c
- PRIM_MAP_ST : draw_primitives.h
- PRIM_OVERRIDE_ENABLE : draw_primitives.h
- PRIM_POINT : draw_primitives.h
- PRIM_SHADE_FLAT : draw_primitives.h
- PRIM_UNFIXED : draw_primitives.h
- PS2CAM_PROD_EYETOY : ps2cam.h
- PS2CAM_PROD_EYETOY2 : ps2cam.h
- PS2CAM_PROD_EYETOY3 : ps2cam.h
- PS2CAM_PROD_EYETOY4 : ps2cam.h
- PS2CAM_PROD_VISUALSTREAM : ps2cam.h
- PS2CAM_RPC_GETDEVCOUNT : ps2cam_rpc.h , ps2cam.h
- PS2CAM_RPC_GETDEVINFO : ps2cam.h , ps2cam_rpc.h
- PS2CAM_RPC_GETDEVSTATUS : ps2cam_rpc.h , ps2cam.h
- PS2CAM_RPC_GETIRXVERSION : ps2cam_rpc.h , ps2cam.h
- PS2CAM_RPC_INITIALIZE : ps2cam_rpc.h , ps2cam.h
- PS2CAM_RPC_READPACKET : ps2cam_rpc.h , ps2cam.h
- PS2CAM_RPC_SETDEVBANDWIDTH : ps2cam_rpc.h , ps2cam.h
- PS2CAM_RPC_SETLEDMODE : ps2cam_rpc.h , ps2cam.h
- PS2CAM_VEND_DLINK : ps2cam.h
- PS2CAM_VEND_LOGITECH : ps2cam.h
- PS2CAM_VEND_SONY : ps2cam.h
- PS2KBD_IOCTL_FLUSHBUFFER : ps2kbd.h
- PS2KBD_IOCTL_RESETKEYMAP : ps2kbd.h
- PS2KBD_IOCTL_SETALTMAP : ps2kbd.h
- PS2KBD_IOCTL_SETBLOCKMODE : ps2kbd.h
- PS2KBD_IOCTL_SETCTRLMAP : ps2kbd.h
- PS2KBD_IOCTL_SETKEYMAP : ps2kbd.h
- PS2KBD_IOCTL_SETLEDS : ps2kbd.h
- PS2KBD_IOCTL_SETREADMODE : ps2kbd.h
- PS2KBD_IOCTL_SETREPEATRATE : ps2kbd.h
- PS2KBD_IOCTL_SETSPECIALMAP : ps2kbd.h
- PS2KBD_REPEATWAIT : ps2kbd.c

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_defs_q.html>

###### - q -
- QWC_MAX : packet.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_defs_r.html>

###### - r -
- R_CDVD_DEC_CTRL : iop_regs.h
- R_CDVD_KEY_FLAGS : iop_regs.h
- R_CDVD_KEY_XOR : iop_regs.h
- R_CDVD_N_CMD : iop_regs.h
- R_CDVD_N_CMD_STATUS : iop_regs.h
- R_CDVD_S_CMD : iop_regs.h
- R_CDVD_S_RES_FIFO : iop_regs.h
- R_EE_D0_ASR0 : ee_regs.h
- R_EE_D0_ASR1 : ee_regs.h
- R_EE_D0_CHCR : ee_regs.h
- R_EE_D0_MADR : ee_regs.h
- R_EE_D0_QWC : ee_regs.h
- R_EE_D0_TADR : ee_regs.h
- R_EE_D1_ASR0 : ee_regs.h
- R_EE_D1_ASR1 : ee_regs.h
- R_EE_D1_CHCR : ee_regs.h
- R_EE_D1_MADR : ee_regs.h
- R_EE_D1_QWC : ee_regs.h
- R_EE_D1_TADR : ee_regs.h
- R_EE_D2_ASR0 : ee_regs.h
- R_EE_D2_ASR1 : ee_regs.h
- R_EE_D2_CHCR : ee_regs.h
- R_EE_D2_MADR : ee_regs.h
- R_EE_D2_QWC : ee_regs.h
- R_EE_D2_TADR : ee_regs.h
- R_EE_D3_CHCR : ee_regs.h
- R_EE_D3_MADR : ee_regs.h
- R_EE_D3_QWC : ee_regs.h
- R_EE_D4_CHCR : ee_regs.h
- R_EE_D4_MADR : ee_regs.h
- R_EE_D4_QWC : ee_regs.h
- R_EE_D4_TADR : ee_regs.h
- R_EE_D5_CHCR : ee_regs.h
- R_EE_D5_MADR : ee_regs.h
- R_EE_D5_QWC : ee_regs.h
- R_EE_D6_CHCR : ee_regs.h
- R_EE_D6_MADR : ee_regs.h
- R_EE_D6_QWC : ee_regs.h
- R_EE_D6_TADR : ee_regs.h
- R_EE_D7_CHCR : ee_regs.h
- R_EE_D7_MADR : ee_regs.h
- R_EE_D7_QWC : ee_regs.h
- R_EE_D8_CHCR : ee_regs.h
- R_EE_D8_MADR : ee_regs.h
- R_EE_D8_QWC : ee_regs.h
- R_EE_D8_SADR : ee_regs.h
- R_EE_D9_CHCR : ee_regs.h
- R_EE_D9_MADR : ee_regs.h
- R_EE_D9_QWC : ee_regs.h
- R_EE_D9_SADR : ee_regs.h
- R_EE_D9_TADR : ee_regs.h
- R_EE_D_CTRL : ee_regs.h
- R_EE_D_ENABLER : ee_regs.h
- R_EE_D_ENABLEW : ee_regs.h
- R_EE_D_PCR : ee_regs.h
- R_EE_D_RBOR : ee_regs.h
- R_EE_D_RBSR : ee_regs.h
- R_EE_D_SQWC : ee_regs.h
- R_EE_D_STADR : ee_regs.h
- R_EE_D_STAT : ee_regs.h
- R_EE_GIF_CNT : ee_regs.h
- R_EE_GIF_CTRL : ee_regs.h
- R_EE_GIF_FIFO : ee_regs.h
- R_EE_GIF_MODE : ee_regs.h
- R_EE_GIF_P3CNT : ee_regs.h
- R_EE_GIF_P3TAG : ee_regs.h
- R_EE_GIF_STAT : ee_regs.h
- R_EE_GIF_TAG0 : ee_regs.h
- R_EE_GIF_TAG1 : ee_regs.h
- R_EE_GIF_TAG2 : ee_regs.h
- R_EE_GIF_TAG3 : ee_regs.h
- R_EE_GS_BGCOLOR : ee_regs.h
- R_EE_GS_BUSDIR : ee_regs.h
- R_EE_GS_CSR : ee_regs.h
- R_EE_GS_DISPFB1 : ee_regs.h
- R_EE_GS_DISPFB2 : ee_regs.h
- R_EE_GS_DISPLAY1 : ee_regs.h
- R_EE_GS_DISPLAY2 : ee_regs.h
- R_EE_GS_EXTBUF : ee_regs.h
- R_EE_GS_EXTDATA : ee_regs.h
- R_EE_GS_EXTWRITE : ee_regs.h
- R_EE_GS_IMR : ee_regs.h
- R_EE_GS_PMODE : ee_regs.h
- R_EE_GS_SIGLBLID : ee_regs.h
- R_EE_GS_SMODE1 : ee_regs.h
- R_EE_GS_SMODE2 : ee_regs.h
- R_EE_GS_SRFSH : ee_regs.h
- R_EE_GS_SYNCH1 : ee_regs.h
- R_EE_GS_SYNCH2 : ee_regs.h
- R_EE_GS_SYNCV : ee_regs.h
- R_EE_I_MASK : ee_regs.h
- R_EE_I_STAT : ee_regs.h
- R_EE_IPU_BP : ee_regs.h
- R_EE_IPU_CMD : ee_regs.h
- R_EE_IPU_CTRL : ee_regs.h
- R_EE_IPU_in_FIFO : ee_regs.h
- R_EE_IPU_out_FIFO : ee_regs.h
- R_EE_IPU_TOP : ee_regs.h
- R_EE_PGIF_CFIFO_DATA : ee_regs.h
- R_EE_PGIF_CFIFO_STAT : ee_regs.h
- R_EE_PGIF_GPU_STAT : ee_regs.h
- R_EE_PGIF_REG10 : ee_regs.h
- R_EE_PGIF_REG20 : ee_regs.h
- R_EE_PGIF_REG30 : ee_regs.h
- R_EE_PGIF_REG40 : ee_regs.h
- R_EE_PGIF_REG50 : ee_regs.h
- R_EE_PGIF_REG60 : ee_regs.h
- R_EE_PGIF_REG70 : ee_regs.h
- R_EE_PGIF_REG90 : ee_regs.h
- R_EE_PGIF_REGA0 : ee_regs.h
- R_EE_PGIF_REGB0 : ee_regs.h
- R_EE_PGIF_REGD0 : ee_regs.h
- R_EE_PGIF_REGE0 : ee_regs.h
- R_EE_PGIF_REGF0 : ee_regs.h
- R_EE_SBUS_MADDR : ee_regs.h
- R_EE_SBUS_MSFLAG : ee_regs.h
- R_EE_SBUS_REG40 : ee_regs.h
- R_EE_SBUS_REG50 : ee_regs.h
- R_EE_SBUS_REG60 : ee_regs.h
- R_EE_SBUS_REG70 : ee_regs.h
- R_EE_SBUS_REG80 : ee_regs.h
- R_EE_SBUS_REG90 : ee_regs.h
- R_EE_SBUS_REGA0 : ee_regs.h
- R_EE_SBUS_REGB0 : ee_regs.h
- R_EE_SBUS_REGC0 : ee_regs.h
- R_EE_SBUS_REGD0 : ee_regs.h
- R_EE_SBUS_REGE0 : ee_regs.h
- R_EE_SBUS_REGF0 : ee_regs.h
- R_EE_SBUS_SADDR : ee_regs.h
- R_EE_SBUS_SMFLAG : ee_regs.h
- R_EE_SIO_BRC : ee_regs.h
- R_EE_SIO_FCR : ee_regs.h
- R_EE_SIO_IER : ee_regs.h
- R_EE_SIO_ISR : ee_regs.h
- R_EE_SIO_LCR : ee_regs.h
- R_EE_SIO_LSR : ee_regs.h
- R_EE_SIO_REG60 : ee_regs.h
- R_EE_SIO_REG70 : ee_regs.h
- R_EE_SIO_REG90 : ee_regs.h
- R_EE_SIO_REGA0 : ee_regs.h
- R_EE_SIO_REGB0 : ee_regs.h
- R_EE_SIO_RXFIFO : ee_regs.h
- R_EE_SIO_TXFIFO : ee_regs.h
- R_EE_T0_COMP : ee_regs.h
- R_EE_T0_COUNT : ee_regs.h
- R_EE_T0_HOLD : ee_regs.h
- R_EE_T0_MODE : ee_regs.h
- R_EE_T1_COMP : ee_regs.h
- R_EE_T1_COUNT : ee_regs.h
- R_EE_T1_HOLD : ee_regs.h
- R_EE_T1_MODE : ee_regs.h
- R_EE_T2_COMP : ee_regs.h
- R_EE_T2_COUNT : ee_regs.h
- R_EE_T2_MODE : ee_regs.h
- R_EE_T3_COMP : ee_regs.h
- R_EE_T3_COUNT : ee_regs.h
- R_EE_T3_MODE : ee_regs.h
- R_EE_VIF0_C0 : ee_regs.h
- R_EE_VIF0_C1 : ee_regs.h
- R_EE_VIF0_C2 : ee_regs.h
- R_EE_VIF0_C3 : ee_regs.h
- R_EE_VIF0_CODE : ee_regs.h
- R_EE_VIF0_CYCLE : ee_regs.h
- R_EE_VIF0_ERR : ee_regs.h
- R_EE_VIF0_FBRST : ee_regs.h
- R_EE_VIF0_FIFO : ee_regs.h
- R_EE_VIF0_ITOP : ee_regs.h
- R_EE_VIF0_ITOPS : ee_regs.h
- R_EE_VIF0_MARK : ee_regs.h
- R_EE_VIF0_MASK : ee_regs.h
- R_EE_VIF0_MODE : ee_regs.h
- R_EE_VIF0_NUM : ee_regs.h
- R_EE_VIF0_R0 : ee_regs.h
- R_EE_VIF0_R1 : ee_regs.h
- R_EE_VIF0_R2 : ee_regs.h
- R_EE_VIF0_R3 : ee_regs.h
- R_EE_VIF0_STAT : ee_regs.h
- R_EE_VIF1_BASE : ee_regs.h
- R_EE_VIF1_C0 : ee_regs.h
- R_EE_VIF1_C1 : ee_regs.h
- R_EE_VIF1_C2 : ee_regs.h
- R_EE_VIF1_C3 : ee_regs.h
- R_EE_VIF1_CODE : ee_regs.h
- R_EE_VIF1_CYCLE : ee_regs.h
- R_EE_VIF1_ERR : ee_regs.h
- R_EE_VIF1_FBRST : ee_regs.h
- R_EE_VIF1_FIFO : ee_regs.h
- R_EE_VIF1_ITOP : ee_regs.h
- R_EE_VIF1_ITOPS : ee_regs.h
- R_EE_VIF1_MARK : ee_regs.h
- R_EE_VIF1_MASK : ee_regs.h
- R_EE_VIF1_MODE : ee_regs.h
- R_EE_VIF1_NUM : ee_regs.h
- R_EE_VIF1_OFST : ee_regs.h
- R_EE_VIF1_R0 : ee_regs.h
- R_EE_VIF1_R1 : ee_regs.h
- R_EE_VIF1_R2 : ee_regs.h
- R_EE_VIF1_R3 : ee_regs.h
- R_EE_VIF1_STAT : ee_regs.h
- R_EE_VIF1_TOP : ee_regs.h
- R_EE_VIF1_TOPS : ee_regs.h
- R_IOP_DMAC_1578 : iop_regs.h
- R_IOP_SBUS_REG_BASE : iop_regs.h
- RCYC_8 : dma_registers.h
- RELE_OFF : dma_registers.h
- RESET_ARG_MAX : sifcmd-common.h
- RTC_24H : aifregs.h
- RTC_AIE : aifregs.h
- RTC_DIV_RESET1 : aifregs.h
- RTC_DM_BINARY : aifregs.h
- RTC_DST_EN : aifregs.h
- RTC_IRQF : aifregs.h
- RTC_PIE : aifregs.h
- RTC_RATE_SELECT : aifregs.h
- RTC_REF_CLCK_4MHZ : aifregs.h
- RTC_SET : aifregs.h
- RTC_SQWE : aifregs.h
- RTC_UIE : aifregs.h
- RTC_UIP : aifregs.h
- RTC_VRT : aifregs.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_defs_s.html>

###### - s -
- SBUS_CTRL_MSCLK : ps2_reg_defs.h
- SBUS_CTRL_MSINT : ps2_reg_defs.h
- SBUS_CTRL_PGPU_INT : ps2_reg_defs.h
- SBUS_CTRL_PS1_RESET : ps2_reg_defs.h
- SCAN_MASK_NORMAL : draw_masking.h
- SCE_CdSTREAM : libcdvd-common.h
- SCE_EBINDMISS : loadfile.h
- SCE_ECALLMISS : loadfile.h
- SCE_ELOADMISS : loadfile.h
- SIF_CMD_ID_SYSTEM : sifcmd-common.h
- SIF_CMD_M_INTR : sifcmd-common.h
- SIF_CMD_M_WBDC : sifcmd-common.h
- SIF_RPC_M_NOWAIT : sifrpc-common.h
- SIF_RPC_M_NOWBDC : sifrpc-common.h
- SIF_SREG_RPCINIT : sifcmd-common.h
- SIF_STAT_BOOTEND : sifdma.h , sifman.h
- SIF_STAT_CMDINIT : sifdma.h , sifman.h
- SIF_STAT_SIFINIT : sifdma.h , sifman.h
- SINGLE_BYTE : font.h
- SIO_BGR : sio.h
- SIO_CAUSE_BIT : sio.h
- SIO_FCR : sio.h
- SIO_FCR_FRSTE : sio.h
- SIO_FCR_RFRST : sio.h
- SIO_FCR_TFRST : sio.h
- SIO_IER : sio.h
- SIO_IER_ELSI : sio.h
- SIO_IER_ERDAI : sio.h
- SIO_ISR : sio.h
- SIO_LCR : sio.h
- SIO_LCR_UEPS_ODD : sio.h
- SIO_LCR_UMODE_8BIT : sio.h
- SIO_LCR_UPEN_OFF : sio.h
- SIO_LCR_USBL_1BIT : sio.h
- SIO_LSR : sio.h
- SIO_LSR_DR : sio.h
- SIO_LSR_FE : sio.h
- SIO_LSR_OE : sio.h
- SIO_LSR_PE : sio.h
- SIO_RXFIFO : sio.h
- SIO_TXFIFO : sio.h
- SMAP_BD_RX_ALIGNERR : smapregs.h
- SMAP_BD_RX_BADFCS : smapregs.h
- SMAP_BD_RX_BADFRM : smapregs.h
- SMAP_BD_RX_EMPTY : smapregs.h
- SMAP_BD_RX_FRMTOOLONG : smapregs.h
- SMAP_BD_RX_INRANGE : smapregs.h
- SMAP_BD_RX_OUTRANGE : smapregs.h
- SMAP_BD_RX_OVERRUN : smapregs.h
- SMAP_BD_RX_PFRM : smapregs.h
- SMAP_BD_RX_RUNTFRM : smapregs.h
- SMAP_BD_RX_SHORTEVNT : smapregs.h
- SMAP_BD_TX_BADFCS : smapregs.h
- SMAP_BD_TX_BADPKT : smapregs.h
- SMAP_BD_TX_ECOLL : smapregs.h
- SMAP_BD_TX_EDEFER : smapregs.h
- SMAP_BD_TX_GENFCS : smapregs.h
- SMAP_BD_TX_GENPAD : smapregs.h
- SMAP_BD_TX_INSSA : smapregs.h
- SMAP_BD_TX_INSVLAN : smapregs.h
- SMAP_BD_TX_LCOLL : smapregs.h
- SMAP_BD_TX_LOSSCR : smapregs.h
- SMAP_BD_TX_MCOLL : smapregs.h
- SMAP_BD_TX_READY : smapregs.h
- SMAP_BD_TX_RPLSA : smapregs.h
- SMAP_BD_TX_RPLVLAN : smapregs.h
- SMAP_BD_TX_SCOLL : smapregs.h
- SMAP_BD_TX_SQE : smapregs.h
- SMAP_BD_TX_UNDERRUN : smapregs.h
- SMAP_E3_ALLOW_EXTMNGIF : smapregs.h
- SMAP_E3_ALLOW_PF : smapregs.h
- SMAP_E3_FLOWCTRL_ENABLE : smapregs.h
- SMAP_E3_INLPBK_ENABLE : smapregs.h
- SMAP_E3_INTR_OVERRUN : smapregs.h
- SMAP_E3_PHY_OP_COMP : smapregs.h
- SMAP_E3_RX_PROP_PF : smapregs.h
- SMAP_E3_TX_GNP_0 : smapregs.h
- SMAP_E3_TX_GNP_1 : smapregs.h
- SMAP_E3_TX_GNP_DEPEND : smapregs.h
- SMAP_E3_TX_LOW_REQ_BITSFT : smapregs.h
- SMAP_E3_TX_LOW_REQ_MSK : smapregs.h
- SMAP_E3_TX_URG_REQ_BITSFT : smapregs.h
- SMAP_E3_TX_URG_REQ_MSK : smapregs.h
- SMAP_PHY_10BTSCR_2 : smapregs.h
- SMAP_PHY_10BTSCR_AUTOPOL_DIS : smapregs.h
- SMAP_PHY_10BTSCR_FORCE_10_LINK : smapregs.h
- SMAP_PHY_10BTSCR_FORCE_POL_COR : smapregs.h
- SMAP_PHY_10BTSCR_HEARTBEAT_DIS : smapregs.h
- SMAP_PHY_10BTSCR_JABBER_DIS : smapregs.h
- SMAP_PHY_10BTSCR_LOOPBACK_10_DIS : smapregs.h
- SMAP_PHY_10BTSCR_LP_DIS : smapregs.h
- SMAP_PHY_10BTSCR_POLARITY : smapregs.h
- SMAP_PHY_ANAR_10 : smapregs.h
- SMAP_PHY_ANAR_10_FD : smapregs.h
- SMAP_PHY_ANAR_PAUSE : smapregs.h
- SMAP_PHY_ANAR_RFLT : smapregs.h
- SMAP_PHY_ANAR_T4 : smapregs.h
- SMAP_PHY_ANAR_TX : smapregs.h
- SMAP_PHY_ANAR_TX_FD : smapregs.h
- SMAP_PHY_BMSR_ANCP : smapregs.h
- SMAP_PHY_BMSR_LINK : smapregs.h
- SMAP_PHY_STS_100M : smapregs.h
- SMAP_PHY_STS_10M : smapregs.h
- SMAP_PHY_STS_ANCP : smapregs.h
- SMAP_PHY_STS_DSL : smapregs.h
- SMAP_PHY_STS_DUPS : smapregs.h
- SMAP_PHY_STS_FCSL : smapregs.h
- SMAP_PHY_STS_FDX : smapregs.h
- SMAP_PHY_STS_HDX : smapregs.h
- SMAP_PHY_STS_JBDT : smapregs.h
- SMAP_PHY_STS_LINK : smapregs.h
- SMAP_PHY_STS_LPBK : smapregs.h
- SMAP_PHY_STS_POST : smapregs.h
- SMAP_PHY_STS_PRCV : smapregs.h
- SMAP_PHY_STS_REL : smapregs.h
- SMAP_PHY_STS_RFLT : smapregs.h
- SMAP_PHY_STS_SD : smapregs.h
- SMAP_PHY_STS_SPDS : smapregs.h
- SPD_PP_CSEL : speedregs.h
- SPD_PP_DIN : speedregs.h
- SPD_PP_DOUT : speedregs.h
- SPD_PP_SCLK : speedregs.h
- STD_OFF : dma_registers.h
- STS_UNSPEC : dma_registers.h
- SUB_VIRT_MEM : smem.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_defs_t.html>

###### - t -
- TEXTURE_COMPONENTS_RGB : draw_buffers.h
- TEXTURE_FUNCTION_MODULATE : draw_buffers.h
- TH_SELF : thbase.h , kernel.h
- THS_RUN : kernel.h
- TSW_NONE : kernel.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_defs_u.html>

###### - u -
- USB_KEYB_NUMLOCK : ps2kbd.c
- USB_RC_ABORTED : usbd.h
- USB_RC_BADCONTEXT : usbd.h
- USB_RC_BADDEV : usbd.h
- USB_RC_BADDRIVER : usbd.h
- USB_RC_BADLENGTH : usbd.h
- USB_RC_BADOPTION : usbd.h
- USB_RC_BADPID : usbd.h
- USB_RC_BADPIPE : usbd.h
- USB_RC_BITSTUFF : usbd.h
- USB_RC_BUFFOVER : usbd.h
- USB_RC_BUFFUNDER : usbd.h
- USB_RC_BUSY : usbd.h
- USB_RC_CRC : usbd.h
- USB_RC_DATAOVER : usbd.h
- USB_RC_DATAUNDER : usbd.h
- USB_RC_ED : usbd.h
- USB_RC_IOREQ : usbd.h
- USB_RC_NORESPONSE : usbd.h
- USB_RC_NOSUPPORT : usbd.h
- USB_RC_NOTACCESSED : usbd.h
- USB_RC_NOTACCESSED2 : usbd.h
- USB_RC_OK : usbd.h
- USB_RC_STALL : usbd.h
- USB_RC_TOGGLE : usbd.h
- USB_RC_UNKNOWN : usbd.h
- USB_RC_WRONGPID : usbd.h
- USBMASS_DEV_STAT_CONF : usbhdfsd-common.h
- USBMASS_DEV_STAT_CONN : usbhdfsd-common.h
- USBMASS_DEV_STAT_ERR : usbhdfsd-common.h
- USBMASS_DEVCTL_STOP_ALL : usbhdfsd-common.h
- USBMASS_DEVCTL_STOP_UNIT : usbhdfsd-common.h
- USBMASS_IOCTL_CHECK_CHAIN : usbhdfsd-common.h
- USBMASS_IOCTL_GET_CLUSTER : usbhdfsd-common.h
- USBMASS_IOCTL_GET_DEVICE_NUMBER : usbhdfsd-common.h
- USBMASS_IOCTL_GET_DRIVERNAME : usbhdfsd-common.h
- USBMASS_IOCTL_GET_FRAGLIST : usbhdfsd-common.h
- USBMASS_IOCTL_GET_LBA : usbhdfsd-common.h
- USBMASS_IOCTL_RENAME : usbhdfsd-common.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_defs_v.html>

###### - v -
- VIF_CMD_BASE : vif_codes.h
- VIF_CMD_DIRECT : vif_codes.h
- VIF_CMD_DIRECTHL : vif_codes.h
- VIF_CMD_FLUSH : vif_codes.h
- VIF_CMD_FLUSHA : vif_codes.h
- VIF_CMD_FLUSHE : vif_codes.h
- VIF_CMD_ITOP : vif_codes.h
- VIF_CMD_MARK : vif_codes.h
- VIF_CMD_MPG : vif_codes.h
- VIF_CMD_MSCAL : vif_codes.h
- VIF_CMD_MSCALF : vif_codes.h
- VIF_CMD_MSCNT : vif_codes.h
- VIF_CMD_MSKPATH3 : vif_codes.h
- VIF_CMD_NOP : vif_codes.h
- VIF_CMD_OFFSET : vif_codes.h
- VIF_CMD_STCOL : vif_codes.h
- VIF_CMD_STCYCL : vif_codes.h
- VIF_CMD_STMASK : vif_codes.h
- VIF_CMD_STMOD : vif_codes.h
- VIF_CMD_STROW : vif_codes.h
- VIF_CMD_UNPACK : vif_codes.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_defs_w.html>

###### - w -
- WRAP_REPEAT : draw_sampling.h
- WRITEBACK_DCACHE : kernel.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_defs_z.html>

###### - z -
- ZTEST_METHOD_ALLFAIL : draw_tests.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_e.html>

Here is a list of all documented functions, variables, defines, enums, and typedefs with links to the documentation:
###### - e -
- E2BIG : errno.h
- E_IOP_DEPENDANCY : ps2lib_err.h
- E_IOP_INTR_CONTEXT : ps2lib_err.h
- E_IOP_NO_MEMORY : ps2lib_err.h
- E_LF_FILE_IO_ERROR : ps2lib_err.h
- E_LF_FILE_NOT_FOUND : ps2lib_err.h
- E_LF_NOT_IRX : ps2lib_err.h
- E_LIB_API_INIT : ps2lib_err.h
- E_LIB_ERROR : ps2lib_err.h
- E_LIB_FILE_NOT_FOUND : ps2lib_err.h
- E_LIB_INVALID_ARG : ps2lib_err.h
- E_LIB_IO_ERROR : ps2lib_err.h
- E_LIB_MATH_DOMAIN : ps2lib_err.h
- E_LIB_MATH_RANGE : ps2lib_err.h
- E_LIB_OUT_OF_MEMORY : ps2lib_err.h
- E_LIB_SEMA_CREATE : ps2lib_err.h
- E_LIB_THREAD_CREATE : ps2lib_err.h
- E_LIB_THREAD_START : ps2lib_err.h
- E_LIB_UNSUPPORTED : ps2lib_err.h
- E_SIF_PKT_ALLOC : ps2lib_err.h
- E_SIF_PKT_SEND : ps2lib_err.h
- E_SIF_RPC_BIND : ps2lib_err.h
- E_SIF_RPC_CALL : ps2lib_err.h
- EA_MULTI : thevent.h
- EA_SINGLE : thevent.h
- EACCES : errno.h
- EADDRINUSE : errno.h
- EADDRNOTAVAIL : errno.h
- EADV : errno.h
- EAFNOSUPPORT : errno.h
- EAGAIN : errno.h
- EAI_NONAME : tcpip.h
- EALREADY : errno.h
- EBADE : errno.h
- EBADF : errno.h
- EBADFD : errno.h
- EBADMSG : errno.h
- EBADR : errno.h
- EBADRQC : errno.h
- EBADSLT : errno.h
- EBFONT : errno.h
- EBUSY : errno.h
- ECANCELED : errno.h
- ECASECLASH : errno.h
- ECHILD : errno.h
- ECHRNG : errno.h
- ECOMM : errno.h
- ECONNABORTED : errno.h
- ECONNREFUSED : errno.h
- ECONNRESET : errno.h
- EDEADLK : errno.h
- EDEADLOCK : errno.h
- EDESTADDRREQ : errno.h
- EDOM : errno.h
- EDOTDOT : errno.h
- EDQUOT : errno.h
- EE_CAUSE_SIO : ee_cop0_defs.h
- EEXIST : errno.h
- EFAULT : errno.h
- EFBIG : errno.h
- EFORMAT : errno.h
- EFTYPE : errno.h
- EHOSTDOWN : errno.h
- EHOSTUNREACH : errno.h
- EIDRM : errno.h
- EILSEQ : errno.h
- EINPROGRESS : errno.h
- EINTR : errno.h
- EINVAL : errno.h
- EIO : errno.h
- EISCONN : errno.h
- EISDIR : errno.h
- EL2HLT : errno.h
- EL2NSYNC : errno.h
- EL3HLT : errno.h
- EL3RST : errno.h
- ELBIN : errno.h
- ELIBACC : errno.h
- ELIBBAD : errno.h
- ELIBEXEC : errno.h
- ELIBMAX : errno.h
- ELIBSCN : errno.h
- ELNRNG : errno.h
- ELOOP : errno.h
- EMFILE : errno.h
- EMLINK : errno.h
- EMSGSIZE : errno.h
- EMULTIHOP : errno.h
- EnableDispatchIntr() : intrman.h
- EnableIntr() : intrman.h
- ENAMETOOLONG : errno.h
- ENETDOWN : errno.h
- ENETRESET : errno.h
- ENETUNREACH : errno.h
- ENFILE : errno.h
- ENMFILE : errno.h
- ENOANO : errno.h
- ENOBUFS : errno.h
- ENOCSI : errno.h
- ENODATA : errno.h
- ENODEV : errno.h
- ENOENT : errno.h
- ENOEXEC : errno.h
- ENOLCK : errno.h
- ENOLINK : errno.h
- ENOMEDIUM : errno.h
- ENOMEM : errno.h
- ENOMSG : errno.h
- ENONET : errno.h
- ENOPKG : errno.h
- ENOPROTOOPT : errno.h
- ENOSHARE : errno.h
- ENOSPC : errno.h
- ENOSR : errno.h
- ENOSTR : errno.h
- ENOSYS : errno.h
- ENOTBLK : errno.h
- ENOTCONN : errno.h
- ENOTDIR : errno.h
- ENOTEMPTY : errno.h
- ENOTRECOVERABLE : errno.h
- ENOTSOCK : errno.h
- ENOTSUP : errno.h
- ENOTTY : errno.h
- ENOTUNIQ : errno.h
- EnterCritical() : iopdebug_priv.h
- ENXIO : errno.h
- EOPNOTSUPP : errno.h
- EOVERFLOW : errno.h
- EOWNERDEAD : errno.h
- EPERM : errno.h
- EPFNOSUPPORT : errno.h
- EPIPE : errno.h
- EPROCLIM : errno.h
- EPROTO : errno.h
- EPROTONOSUPPORT : errno.h
- EPROTOTYPE : errno.h
- ERANGE : errno.h
- EREMCHG : errno.h
- EREMOTE : errno.h
- ERL_FLAG_CLEAR : erl.h
- ERL_FLAG_STATIC : erl.h
- ERL_FLAG_STICKY : erl.h
- EROFS : errno.h
- ESHUTDOWN : errno.h
- ESOCKTNOSUPPORT : errno.h
- ESPIPE : errno.h
- ESRCH : errno.h
- ESRMNT : errno.h
- ESTALE : errno.h
- ESTRPIPE : errno.h
- ETIME : errno.h
- ETIMEDOUT : errno.h
- ETOOMANYREFS : errno.h
- ETXTBSY : errno.h
- EUNATCH : errno.h
- EUNSUP : errno.h
- EUSERS : errno.h
- EWOULDBLOCK : errno.h
- EXDEV : errno.h
- EXFULL : errno.h
- ExitCritical() : iopdebug_priv.h
- EYETOY_ALTERNATE_SIZE_0 : ps2cam.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_enum.html>

###### - _ -
- _ata_identify_offsets : atahw.h
- _ps2lib_errors : ps2lib_err.h
- _sif_regs : sifdma.h , sifman.h
###### - a -
- ATA_C_CODES : atahw.h
###### - c -
- CD_NCMD_CMDS : ncmd.c
- CdvdStCmd_t : ncmd.c
- CPU_CONFIG : kernel.h
###### - d -
- DATE_FORMAT_TYPES : osd_config.h
- devfs_devtypes : devfs.h
- devfs_subdev_modes : devfs.h
###### - g -
- GsATestFailedUpdateMethods : libgs.h
- GsATestMethods : libgs.h
- GsGifDataFormat : libgs.h
- GsPrimitiveTypes : libgs.h
- GsTexFilterMethods : libgs.h
- GsTexFunctions : libgs.h
- GsTexMipmaps : libgs.h
- GsZTestMethodTypes : libgs.h
###### - i -
- iop_irq_list : intrman.h
###### - l -
- lwip_ip_addr_type : tcpip.h
###### - m -
- MC_FUNC_NUMBERS : libmc.h
- MCICON_TYPES : libmc.h
- mips_cop0_reg : mipscopaccess.h
###### - n -
- netif_mac_filter_action : tcpip.h
- NETMAN_NETIF_ETH_LINK_MODE : netman.h
- NETMAN_NETIF_IOCTL_CODES : netman.h
###### - o -
- OSD_LANGUAGES : osd_config.h
###### - p -
- pbuf_layer : tcpip.h
- pbuf_type : tcpip.h
###### - s -
- sbus_errors : sbusintr.h
- SCECdvdDriveState : libcdvd-common.h
- SCECdvdErrorCode : libcdvd-common.h
- SCECdvdFanSpeed : libcdvd-common.h
- SCECdvdInitMode : libcdvd-common.h
- SCECdvdInterruptCode : libcdvd-common.h
- SCECdvdMediaType : libcdvd-common.h
- SCECdvdSpinValue : libcdvd-common.h
- SCECdvdStreamMode : libcdvd-common.h
- SCECdvdTrayReqMode : libcdvd-common.h
- sif2_errors : siftoo.h
- SSBUSC_DEV : ssbusc.h
###### - t -
- TIME_FORMAT_TYPES : osd_config.h
- TV_SCREEN_TYPES : osd_config.h
###### - v -
- VIDEO_OUTPUT_TYPES : osd_config.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_eval.html>

###### - c -
- CD_NCMD_READCHAIN : ncmd.c
- CdlAcknowledge : libcdvd-common.h
- CdlDataEnd : libcdvd-common.h
- CdlDataReady : libcdvd-common.h
- CdlDiskError : libcdvd-common.h
- CdlNoIntr : libcdvd-common.h
- COP0_REG_BadPAddr : mipscopaccess.h
- COP0_REG_BadVAddr : mipscopaccess.h
- COP0_REG_Cause : mipscopaccess.h
- COP0_REG_Compare : mipscopaccess.h
- COP0_REG_Config : mipscopaccess.h
- COP0_REG_Context : mipscopaccess.h
- COP0_REG_Count : mipscopaccess.h
- COP0_REG_Debug : mipscopaccess.h
- COP0_REG_EntryHi : mipscopaccess.h
- COP0_REG_EntryLo0 : mipscopaccess.h
- COP0_REG_EntryLo1 : mipscopaccess.h
- COP0_REG_EPC : mipscopaccess.h
- COP0_REG_ErrorPC : mipscopaccess.h
- COP0_REG_Index : mipscopaccess.h
- COP0_REG_PageMask : mipscopaccess.h
- COP0_REG_Perf : mipscopaccess.h
- COP0_REG_PRId : mipscopaccess.h
- COP0_REG_Random : mipscopaccess.h
- COP0_REG_Status : mipscopaccess.h
- COP0_REG_TagHi : mipscopaccess.h
- COP0_REG_TagLo : mipscopaccess.h
- COP0_REG_Wired : mipscopaccess.h
###### - d -
- DEVFS_DEVTYPE_BLOCK : devfs.h
- DEVFS_DEVTYPE_CHAR : devfs.h
- DEVFS_DEVTYPE_STREAM : devfs.h
- DEVFS_MODE_EX : devfs.h
- DEVFS_MODE_R : devfs.h
- DEVFS_MODE_RW : devfs.h
- DEVFS_MODE_W : devfs.h
###### - e -
- E_IOP_DEPENDANCY : ps2lib_err.h
- E_IOP_INTR_CONTEXT : ps2lib_err.h
- E_IOP_NO_MEMORY : ps2lib_err.h
- E_LF_FILE_IO_ERROR : ps2lib_err.h
- E_LF_FILE_NOT_FOUND : ps2lib_err.h
- E_LF_NOT_IRX : ps2lib_err.h
- E_LIB_API_INIT : ps2lib_err.h
- E_LIB_ERROR : ps2lib_err.h
- E_LIB_FILE_NOT_FOUND : ps2lib_err.h
- E_LIB_INVALID_ARG : ps2lib_err.h
- E_LIB_IO_ERROR : ps2lib_err.h
- E_LIB_MATH_DOMAIN : ps2lib_err.h
- E_LIB_MATH_RANGE : ps2lib_err.h
- E_LIB_OUT_OF_MEMORY : ps2lib_err.h
- E_LIB_SEMA_CREATE : ps2lib_err.h
- E_LIB_THREAD_CREATE : ps2lib_err.h
- E_LIB_THREAD_START : ps2lib_err.h
- E_LIB_UNSUPPORTED : ps2lib_err.h
- E_SIF_PKT_ALLOC : ps2lib_err.h
- E_SIF_PKT_SEND : ps2lib_err.h
- E_SIF_RPC_BIND : ps2lib_err.h
- E_SIF_RPC_CALL : ps2lib_err.h
###### - g -
- GS_ALPHA_NO_UPDATE : libgs.h
- GS_GIF_DISABLE : libgs.h
- GS_TEX_DECAL : libgs.h
- GS_TEX_HIGHLIHGT1 : libgs.h
- GS_TEX_HIGHLIHGT2 : libgs.h
- GS_TEX_LINEAR : libgs.h
- GS_TEX_MIPMAP0 : libgs.h
- GS_TEX_MIPMAP1 : libgs.h
- GS_TEX_MIPMAP2 : libgs.h
- GS_TEX_MIPMAP3 : libgs.h
- GS_TEX_MIPMAP4 : libgs.h
- GS_TEX_MIPMAP5 : libgs.h
- GS_TEX_MIPMAP6 : libgs.h
- GS_TEX_NEAREST : libgs.h
###### - i -
- IOP_IRQ_DMA : intrman.h
- IOP_IRQ_DMA_BERR : intrman.h
- IOP_IRQ_DVD : intrman.h
- IOP_IRQ_EXTR : intrman.h
- IOP_IRQ_FDMA : intrman.h
- IOP_IRQ_SW1 : intrman.h
- IOP_IRQ_SW2 : intrman.h
- IPADDR_TYPE_ANY : tcpip.h
- IPADDR_TYPE_V4 : tcpip.h
- IPADDR_TYPE_V6 : tcpip.h
###### - n -
- NETIF_ADD_MAC_FILTER : tcpip.h
- NETIF_DEL_MAC_FILTER : tcpip.h
- NETMAN_NETIF_ETH_LINK_MODE_100M_FDX : netman.h
- NETMAN_NETIF_ETH_LINK_MODE_100M_HDX : netman.h
- NETMAN_NETIF_ETH_LINK_MODE_10M_FDX : netman.h
- NETMAN_NETIF_ETH_LINK_MODE_10M_HDX : netman.h
- NETMAN_NETIF_ETH_LINK_MODE_AUTO : netman.h
- NETMAN_NETIF_IOCTL_ETH_GET_MAC : netman.h
- NETMAN_NETIF_IOCTL_ETH_SET_LINK_MODE : netman.h
###### - p -
- PBUF_IP : tcpip.h
- PBUF_LINK : tcpip.h
- PBUF_POOL : tcpip.h
- PBUF_RAM : tcpip.h
- PBUF_RAW : tcpip.h
- PBUF_RAW_TX : tcpip.h
- PBUF_REF : tcpip.h
- PBUF_ROM : tcpip.h
- PBUF_TRANSPORT : tcpip.h
###### - s -
- SBUS_E_ARG : sbusintr.h
- SBUS_E_INIT : sbusintr.h
- SBUS_E_IRQ : sbusintr.h
- SCECdCDDA : libcdvd-common.h
- SCECdComplete : libcdvd-common.h
- SCECdDETCT : libcdvd-common.h
- SCECdDVDV : libcdvd-common.h
- SCECdDVDVR : libcdvd-common.h
- SCECdErABRT : libcdvd-common.h
- SCECdErCMD : libcdvd-common.h
- SCECdErCUD : libcdvd-common.h
- SCECdErEOM : libcdvd-common.h
- SCECdErFAIL : libcdvd-common.h
- SCECdErILI : libcdvd-common.h
- SCECdErIPI : libcdvd-common.h
- SCECdErNO : libcdvd-common.h
- SCECdErNODISC : libcdvd-common.h
- SCECdErNORDY : libcdvd-common.h
- SCECdErOPENS : libcdvd-common.h
- SCECdErPRM : libcdvd-common.h
- SCECdErREAD : libcdvd-common.h
- SCECdErREADCF : libcdvd-common.h
- SCECdErREADCFR : libcdvd-common.h
- SCECdErTRMOPN : libcdvd-common.h
- SCECdEXIT : libcdvd-common.h
- SCECdIllegalMedia : libcdvd-common.h
- SCECdINIT : libcdvd-common.h
- SCECdINoD : libcdvd-common.h
- SCECdNODISC : libcdvd-common.h
- SCECdNotReady : libcdvd-common.h
- SCECdPS2CD : libcdvd-common.h
- SCECdPS2CDDA : libcdvd-common.h
- SCECdPS2DVD : libcdvd-common.h
- SCECdPSCD : libcdvd-common.h
- SCECdPSCDDA : libcdvd-common.h
- SCECdSpin1p6 : libcdvd-common.h
- SCECdSpinDvdDL0 : libcdvd-common.h
- SCECdSpinMax : libcdvd-common.h
- SCECdSpinMx : libcdvd-common.h
- SCECdSpinNm2 : libcdvd-common.h
- SCECdSpinNom : libcdvd-common.h
- SCECdSpinStm : libcdvd-common.h
- SCECdSpinX1 : libcdvd-common.h
- SCECdSpinX12 : libcdvd-common.h
- SCECdSpinX2 : libcdvd-common.h
- SCECdSpinX4 : libcdvd-common.h
- SCECdStatEmg : libcdvd-common.h
- SCECdStatPause : libcdvd-common.h
- SCECdStatRead : libcdvd-common.h
- SCECdStatSeek : libcdvd-common.h
- SCECdStatShellOpen : libcdvd-common.h
- SCECdStatSpin : libcdvd-common.h
- SCECdStatStop : libcdvd-common.h
- SCECdTrayCheck : libcdvd-common.h
- SCECdTrayClose : libcdvd-common.h
- SCECdTrayOpen : libcdvd-common.h
- SCECdUNKNOWN : libcdvd-common.h
- SCECdvdFanSpeedMaximum : libcdvd-common.h
- SCECdvdFanSpeedMedium : libcdvd-common.h
- SCECdvdFanSpeedMinimum : libcdvd-common.h
- SIF2_E_INIT : siftoo.h
- SIF2_E_OK : siftoo.h
- SIF_REG_MAINADDR : sifdma.h , sifman.h
- SIF_REG_MSFLAG : sifdma.h , sifman.h
- SIF_REG_SMFLAG : sifdma.h , sifman.h
- SIF_REG_SUBADDR : sifdma.h , sifman.h
- SSBUSC_DEV0 : ssbusc.h
- SSBUSC_DEV_BOOTROM : ssbusc.h
- SSBUSC_DEV_CDVD : ssbusc.h
- SSBUSC_DEV_DVDROM : ssbusc.h
- SSBUSC_DEV_SPU : ssbusc.h
- SSBUSC_DEV_SPU2 : ssbusc.h
- STMBLK : libcdvd-common.h
- STMNBLK : libcdvd-common.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_f.html>

Here is a list of all documented functions, variables, defines, enums, and typedefs with links to the documentation:
###### - f -
- fd_close() : fakehost.c
- fd_lseek() : fakehost.c
- fd_name() : fakehost.c
- fd_open() : fakehost.c
- fd_read() : fakehost.c
- fd_save() : fakehost.c
- fd_write() : fakehost.c
- fdh_freefd() : ps2_fio.c
- fdh_get : ps2_fio.c
- fdh_getfd() : ps2_fio.c
- fdh_getfdtype : ps2_fio.c
- fdh_getrealfd : ps2_fio.c
- fdh_getused : ps2_fio.c
- fdh_setup() : ps2_fio.c
- FILEXIO_DEFAULT_RW_BUFFER_SIZE : fileXio.h
- FILEXIO_DT_FSEXT : fileXio.h
- fillbuf_threshold : audsrv.c
- find_upsampler() : upsamplers.c , upsamplers.h
- FIO_DEFAULT_XFER_SIZE : fileio-common.h
- FIO_S_IFDIR : iox_stat.h
- FIO_S_IFLNK : iox_stat.h
- FIO_S_IFMT : iox_stat.h
- FIO_S_IFREG : iox_stat.h
- FIO_S_IRGRP : iox_stat.h
- FIO_S_IROTH : iox_stat.h
- FIO_S_IRUSR : iox_stat.h
- FIO_S_IRWXG : iox_stat.h
- FIO_S_IRWXO : iox_stat.h
- FIO_S_IRWXU : iox_stat.h
- FIO_S_ISGID : iox_stat.h
- FIO_S_ISUID : iox_stat.h
- FIO_S_ISVTX : iox_stat.h
- FIO_S_IWGRP : iox_stat.h
- FIO_S_IWOTH : iox_stat.h
- FIO_S_IWUSR : iox_stat.h
- FIO_S_IXGRP : iox_stat.h
- FIO_S_IXOTH : iox_stat.h
- FIO_S_IXUSR : iox_stat.h
- FIO_SO_IFDIR : iox_stat.h
- FIO_SO_IFLNK : iox_stat.h
- FIO_SO_IFMT : iox_stat.h
- FIO_SO_IFREG : iox_stat.h
- FIO_SO_IROTH : iox_stat.h
- FIO_SO_IWOTH : iox_stat.h
- FIO_SO_IXOTH : iox_stat.h
- fontstudio_init() : font.h
- fontstudio_load_ini() : font.h
- fontstudio_parse_ini() : font.h
- fontstudio_print_string() : font.h
- fontstudio_unload_ini() : font.h
- fontx_load() : font.h
- fontx_print_ascii() : font.h
- fontx_print_sjis() : font.h
- fontx_unload() : font.h
- format_changed : audsrv.c
- free_all_samples() : adpcm.c
- free_sample() : adpcm.c , audsrv.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_func.html>

###### - _ -
- __attribute__() : libgs.h , audsrv_rpc.c , ps2_fio.c , rpc_server.c , batch.c , adpcm.c , effect.c , ps2mouse.c , libpad.c , audsrv.c , cdrom.c
- __fioMkdirHelper() : ps2sdkapi.c
- _heap_mem_fit() : alloc.c
- _SifLoadModule() : loadfile.h
- _start() : fakehost.c , main.c , ps2netfs.c , audsrv.c , devfs.c

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_func_a.html>

###### - a -
- adpcm_loaded() : adpcm.c
- AHX_Init() : ahx_rpc.h , ahx_rpc.c
- AHX_LoadSong() : ahx_rpc.h , ahx_rpc.c
- AHX_LoadSongBuffer() : ahx_rpc.h , ahx_rpc.c
- AHX_Pause() : ahx_rpc.h , ahx_rpc.c
- AHX_Play() : ahx_rpc.h , ahx_rpc.c
- AHX_Quit() : ahx_rpc.h , ahx_rpc.c
- AHX_SetBoost() : ahx_rpc.h , ahx_rpc.c
- AHX_SetVolume() : ahx_rpc.h , ahx_rpc.c
- AHX_SubSong() : ahx_rpc.h , ahx_rpc.c
- AHX_ToggleOversampling() : ahx_rpc.h , ahx_rpc.c
- alloc_new_sample() : adpcm.c
- audsrv_adpcm_init() : audsrv.h , audsrv_rpc.c , audsrv.h , adpcm.c
- audsrv_adpcm_set_volume() : audsrv.h , adpcm.c
- audsrv_adpcm_set_volume_and_pan() : audsrv.h , audsrv_rpc.c
- audsrv_available() : audsrv_rpc.c , audsrv.h , audsrv.c , audsrv.h
- audsrv_cd_pause() : audsrv.h , cdrom.c
- audsrv_cd_play_sectors() : audsrv.h , cdrom.c
- audsrv_cd_resume() : audsrv.h , cdrom.c
- audsrv_ch_play_adpcm() : audsrv.h , audsrv_rpc.c , audsrv.h , adpcm.c
- audsrv_format_ok() : audsrv.h , audsrv.c
- audsrv_free_adpcm() : audsrv.h , audsrv_rpc.c
- audsrv_get_cd_status() : audsrv.h , audsrv_rpc.c , audsrv.h , cdrom.c
- audsrv_get_cd_type() : audsrv.h , audsrv_rpc.c , audsrv.h , cdrom.c
- audsrv_get_cdpos() : audsrv.h , audsrv_rpc.c , audsrv.h , cdrom.c
- audsrv_get_error() : audsrv.h , audsrv_rpc.c
- audsrv_get_error_string() : audsrv_rpc.c , audsrv.h
- audsrv_get_numtracks() : audsrv.h , audsrv_rpc.c , audsrv.h , cdrom.c
- audsrv_get_track_offset() : audsrv.h , audsrv_rpc.c , cdrom.c
- audsrv_get_trackpos() : audsrv.h , audsrv_rpc.c , cdrom.c , audsrv.h
- audsrv_init() : audsrv.h , audsrv_rpc.c , audsrv.c , audsrv.h
- audsrv_is_adpcm_playing() : audsrv.h , audsrv_rpc.c
- audsrv_load_adpcm() : audsrv.h , audsrv_rpc.c , audsrv.h , adpcm.c
- audsrv_on_cdda_stop() : audsrv_rpc.c , audsrv.h
- audsrv_on_fillbuf() : audsrv.h , audsrv_rpc.c
- audsrv_pause_cd() : audsrv.h , audsrv_rpc.c
- audsrv_play_audio() : audsrv_rpc.c , audsrv.h , audsrv.c
- audsrv_play_cd() : audsrv.h , audsrv_rpc.c , cdrom.c
- audsrv_play_sectors() : audsrv_rpc.c , audsrv.h
- audsrv_queued() : audsrv.h , audsrv_rpc.c , audsrv.c
- audsrv_quit() : audsrv.c , audsrv_rpc.c , audsrv.h
- audsrv_read_adpcm_header() : adpcm.c
- audsrv_resume_cd() : audsrv_rpc.c , audsrv.h
- audsrv_set_format() : audsrv.h , audsrv_rpc.c , audsrv.c
- audsrv_set_volume() : audsrv.c , audsrv_rpc.c , audsrv.h
- audsrv_stop_audio() : audsrv.c , audsrv.h , audsrv_rpc.c
- audsrv_stop_cd() : cdrom.c , audsrv.h , audsrv_rpc.c
- audsrv_stop_cd_stream() : cdrom.c
- audsrv_wait_audio() : audsrv.h , audsrv.c , audsrv.h , audsrv_rpc.c

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_func_c.html>

###### - c -
- calculate_colours() : math3d.h
- calculate_lights() : math3d.h
- calculate_normals() : math3d.h
- calculate_vertices() : math3d.h
- call_rpc_1() : audsrv_rpc.c
- call_rpc_2() : audsrv_rpc.c
- call_rpc_3() : audsrv_rpc.c
- camDisableSystem() : ps2cam.h , ps2cam.c
- camEnableSystem() : ps2cam.h , ps2cam.c
- camResetDevice() : ps2cam.h , ps2cam.c
- camResetUsb() : ps2cam.h , ps2cam.c
- camSetUsbInit() : ps2cam.h , ps2cam.c
- camSetUsbWork() : ps2cam.h , ps2cam.c
- camStartStream() : ps2cam.h , ps2cam.c
- camTurnOffRedLed() : ps2cam.h , ps2cam.c
- camTurnOnRedLed() : ps2cam.h , ps2cam.c
- cd_transfer_complete() : cdrom.c
- cdda_procedure() : cdrom.c
- cdvdman_152_get_temperature() : libcdvd-common.h
- cdvdman_167_atapi2dragon() : libcdvd-common.h
- cdvdman_169_dragon2atapi() : libcdvd-common.h
- cmdline_handle() : main.c , commandline.c
- configConvertToGmtTime() : osd_config.h
- configConvertToLocalTime() : osd_config.h
- configGetDateFormat() : osd_config.h
- configGetLanguage() : osd_config.h
- configGetTimeFormat() : osd_config.h
- configGetTimezone() : osd_config.h
- configGetTvScreenType() : osd_config.h
- configIsDaylightSavingEnabled() : osd_config.h
- configIsSpdifEnabled() : osd_config.h
- configSetDateFormat() : osd_config.h
- configSetDaylightSavingEnabled() : osd_config.h
- configSetLanguage() : osd_config.h
- configSetSpdifEnabled() : osd_config.h
- configSetTimeFormat() : osd_config.h
- configSetTimezone() : osd_config.h
- configSetTvScreenType() : osd_config.h
- convmode_from_iomanx() : ps2_fio.c
- convmode_to_iomanx() : ps2_fio.c
- CpuDisableIntr() : intrman.h
- CpuEnableIntr() : intrman.h
- CpuInvokeInKmode() : intrman.h
- CpuResumeIntr() : intrman.h
- CpuSuspendIntr() : intrman.h
- create_local_light() : math3d.h
- create_local_screen() : math3d.h
- create_local_world() : math3d.h
- create_thread() : common.h , common.c
- create_view_screen() : math3d.h
- create_world_view() : math3d.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_func_d.html>

###### - d -
- demux() : upsamplers.c
- devfs_check_devname() : devfs.c
- devfs_close() : devfs.c
- devfs_create_device() : devfs.c
- devfs_dclose() : devfs.c
- devfs_delete_device() : devfs.c
- devfs_dopen() : devfs.c
- devfs_fill_dirent() : devfs.c
- devfs_find_deviceid() : devfs.c
- devfs_find_devicename() : devfs.c
- devfs_getstat() : devfs.c
- devfs_ioctl() : devfs.c
- devfs_ioctl2() : devfs.c
- devfs_lseek() : devfs.c
- devfs_lseek64() : devfs.c
- devfs_open() : devfs.c
- devfs_read() : devfs.c
- devfs_subdev_to_str() : devfs.c
- devfs_write() : devfs.c
- DevFSAddDevice() : devfs.h , devfs.c
- DevFSAddSubDevice() : devfs.h , devfs.c
- DevFSDelDevice() : devfs.h , devfs.c
- DevFSDelSubDevice() : devfs.h , devfs.c
- devscan_getdevlist() : devscan.c , devscan.h
- devscan_getmodule() : devscan.c , devscan.h
- devscan_gettype() : devscan.c , devscan.h
- devscan_setup() : devscan.c , devscan.h
- DisableDispatchIntr() : intrman.h
- DisableIntr() : intrman.h
- dma_channel_fast_waits() : dma.h
- dma_channel_initialize() : dma.h
- dma_channel_receive_chain() : dma.h
- dma_channel_receive_normal() : dma.h
- dma_channel_send_chain() : dma.h
- dma_channel_send_chain_ucab() : dma.h
- dma_channel_send_normal() : dma.h
- dma_channel_send_normal_ucab() : dma.h
- dma_channel_send_packet2() : dma.h
- dma_channel_shutdown() : dma.h
- dma_channel_wait() : dma.h
- dma_wait_fast() : dma.h
- draw_alpha_blending() : draw_blending.h
- draw_alpha_correction() : draw_blending.h
- draw_arc_filled() : draw2d.h
- draw_arc_outline() : draw2d.h
- draw_clear() : draw.h
- draw_clut_offset() : draw_buffers.h
- draw_clutbuffer() : draw_buffers.h
- draw_color_clamping() : draw_masking.h
- draw_convert_rgbaq() : draw3d.h
- draw_convert_rgbq() : draw3d.h
- draw_convert_st() : draw3d.h
- draw_convert_xyz() : draw3d.h
- draw_disable_blending() : draw2d.h
- draw_disable_tests() : draw_tests.h
- draw_dither_matrix() : draw_dithering.h
- draw_dithering() : draw_dithering.h
- draw_enable_blending() : draw2d.h
- draw_enable_tests() : draw_tests.h
- draw_finish() : draw.h
- draw_fog_color() : draw_fog.h
- draw_framebuffer() : draw_buffers.h
- draw_line() : draw2d.h
- draw_log2() : draw_buffers.h
- draw_mipmap1() : draw_sampling.h
- draw_mipmap2() : draw_sampling.h
- draw_pixel_alpha_control() : draw_blending.h
- draw_pixel_test() : draw_tests.h
- draw_point() : draw2d.h
- draw_prim_end() : draw3d.h
- draw_prim_start() : draw3d.h
- draw_primitive_override() : draw_primitives.h
- draw_primitive_override_setting() : draw_primitives.h
- draw_primitive_xyoffset() : draw_primitives.h
- draw_rect_filled() : draw2d.h
- draw_rect_filled_strips() : draw2d.h
- draw_rect_outline() : draw2d.h
- draw_rect_textured() : draw2d.h
- draw_rect_textured_strips() : draw2d.h
- draw_round_rect_filled() : draw2d.h
- draw_round_rect_outline() : draw2d.h
- draw_scan_masking() : draw_masking.h
- draw_scissor_area() : draw_tests.h
- draw_setup_environment() : draw.h
- draw_texture_expand_alpha() : draw_sampling.h
- draw_texture_flush() : draw.h
- draw_texture_sampling() : draw_sampling.h
- draw_texture_transfer() : draw.h
- draw_texture_wrapping() : draw_sampling.h
- draw_texturebuffer() : draw_buffers.h
- draw_triangle_filled() : draw2d.h
- draw_triangle_outline() : draw2d.h
- draw_wait_finish() : draw.h
- draw_zbuffer() : draw_buffers.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_func_e.html>

###### - e -
- EnableDispatchIntr() : intrman.h
- EnableIntr() : intrman.h
- EnterCritical() : iopdebug_priv.h
- ExitCritical() : iopdebug_priv.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_func_f.html>

###### - f -
- fd_close() : fakehost.c
- fd_lseek() : fakehost.c
- fd_name() : fakehost.c
- fd_open() : fakehost.c
- fd_read() : fakehost.c
- fd_save() : fakehost.c
- fd_write() : fakehost.c
- fdh_freefd() : ps2_fio.c
- fdh_getfd() : ps2_fio.c
- fdh_setup() : ps2_fio.c
- find_upsampler() : upsamplers.c , upsamplers.h
- fontstudio_init() : font.h
- fontstudio_load_ini() : font.h
- fontstudio_parse_ini() : font.h
- fontstudio_print_string() : font.h
- fontstudio_unload_ini() : font.h
- fontx_load() : font.h
- fontx_print_ascii() : font.h
- fontx_print_sjis() : font.h
- fontx_unload() : font.h
- free_all_samples() : adpcm.c
- free_sample() : audsrv.h , adpcm.c

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_func_g.html>

###### - g -
- GetBPC() : hwbp.h
- GetDAB() : hwbp.h
- GetDABM() : hwbp.h
- GetDVB() : hwbp.h
- GetDVBM() : hwbp.h
- GetIAB() : hwbp.h
- GetIABM() : hwbp.h
- GetLibraryEntryTable() : loadcore.h
- getReg8() : ps2cam.h , ps2cam.c
- GetRomName() : rom0_info.h
- graph_add_vsync_handler() : graph.h
- graph_aspect_ratio() : graph.h
- graph_check_vsync() : graph.h
- graph_disable_output() : graph.h
- graph_enable_output() : graph.h
- graph_get_config() : graph_config.h
- graph_get_region() : graph.h
- graph_initialize() : graph.h
- graph_load_config() : graph_config.h
- graph_make_config() : graph_config.h
- graph_remove_vsync_handler() : graph.h
- graph_save_config() : graph_config.h
- graph_set_bgcolor() : graph.h
- graph_set_config() : graph_config.h
- graph_set_framebuffer() : graph.h
- graph_set_framebuffer_filtered() : graph.h
- graph_set_mode() : graph.h
- graph_set_output() : graph.h
- graph_set_screen() : graph.h
- graph_shutdown() : graph.h
- graph_start_vsync() : graph.h
- graph_vram_allocate() : graph_vram.h
- graph_vram_clear() : graph_vram.h
- graph_vram_free() : graph_vram.h
- graph_vram_size() : graph_vram.h
- graph_wait_hsync() : graph.h
- graph_wait_vsync() : graph.h
- GsClearDrawEnv1() : libgs.h
- GsClearDrawEnv2() : libgs.h
- GsVramFreeAllTextureBuffer() : libgs.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_func_h.html>

###### - h -
- HasIopRebootedSinceLastCall() : iopcontrol.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_func_i.html>

###### - i -
- init_devfs() : devfs.c
- InitBPC() : hwbp.h
- iomanX_format() : iomanX.c , iomanX.h
- iop_readwrite() : ahx_rpc.c
- iopmgr_get_device() : iopmgr.h , devices.c
- iopmgr_get_devicelist() : iopmgr.h , devices.c
- iopmgr_get_devicetype() : iopmgr.h , devices.c
- iopmgr_get_iomandev() : iopmgr.h , devices.c
- iopmgr_get_iomanxdev() : devices.c , iopmgr.h
- ioprpgen_setup_membuf() : ioprpgen.h
- ioprpgen_write_ioprp() : ioprpgen.h
- ip4addr_ntoa() : ps2ip.h
- IsDESRMachine() : rom0_info.h
- IsEarlyJap() : osd_config.h
- IsT10K() : rom0_info.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_func_l.html>

###### - l -
- list_all_libraries() : commandline.c
- list_all_modules() : commandline.c
- list_devices_ioman() : commandline.c
- list_devices_iomanx() : commandline.c
- list_fs_devices() : commandline.c
- LoadELFFromFileWithPartition() : elf-loader.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_func_m.html>

###### - m -
- matrix_copy() : math3d.h
- matrix_inverse() : math3d.h
- matrix_multiply() : math3d.h
- matrix_rotate() : math3d.h
- matrix_scale() : math3d.h
- matrix_translate() : math3d.h
- matrix_transpose() : math3d.h
- matrix_unit() : math3d.h
- mcChangeThreadPriority() : libmc.h , libmc.c
- mcChdir() : libmc.h , libmc.c
- mcClose() : libmc.h , libmc.c
- mcDelete() : libmc.c , libmc.h
- mcEraseBlock() : libmc.h , libmc.c
- mcFlush() : libmc.h , libmc.c
- mcFormat() : libmc.h , libmc.c
- mcGetDir() : libmc.h , libmc.c
- mcGetEntSpace() : libmc.h , libmc.c
- mcGetInfo() : libmc.h , libmc.c
- mcGetInfoApdxNew() : libmc.c
- mcGetInfoApdxOld() : libmc.c
- mcInit() : libmc.c , libmc.h
- mcMkDir() : libmc.h , libmc.c
- mcOpen() : libmc.h , libmc.c
- mcRead() : libmc.h , libmc.c
- mcReadFixAlignNew() : libmc.c
- mcReadFixAlignOld() : libmc.c
- mcReadPage() : libmc.h , libmc.c
- mcRename() : libmc.c , libmc.h
- mcReset() : libmc.h , libmc.c
- mcSeek() : libmc.h , libmc.c
- mcSetFileInfo() : libmc.c , libmc.h
- mcStoreDir() : libmc.c
- mcSync() : libmc.c , libmc.h
- mcUnformat() : libmc.h , libmc.c
- mcWrite() : libmc.c , libmc.h
- mcWritePage() : libmc.h , libmc.c
- mtapGetConnection() : libmtap.h , libmtap.c
- mtapInit() : libmtap.h , libmtap.c
- mtapPortClose() : libmtap.h , libmtap.c
- mtapPortOpen() : libmtap.c , libmtap.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_func_n.html>

###### - n -
- naplinkRpcHandler() : nprintf.c
- naplinkRpcInit() : fakehost.c , nprintf.c
- napThread() : nprintf.c
- netif_find() : ps2ip.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_func_p.html>

###### - p -
- packet_free() : packet.h
- packet_get_qword() : packet.h
- packet_increment_qwc() : packet.h
- packet_init() : packet.h
- packet_reset() : packet.h
- pad_close() : input.h
- pad_get_buttons() : input.h
- pad_get_mode() : input.h
- pad_get_num_modes() : input.h
- pad_get_state() : input.h
- pad_get_type() : input.h
- pad_has_type() : input.h
- pad_init_actuators() : input.h
- pad_open() : input.h
- pad_set_actuators() : input.h
- pad_set_mode() : input.h
- pad_set_sensitivity() : input.h
- pad_wait() : input.h
- padEnd() : libpad.h , libpad.c , xpadman.h , freepad.h , padMiscFuncs.c
- padEnterPressMode() : libpad.h , libpad.c
- padExitPressMode() : libpad.h , libpad.c
- padGetConnDmaStr() : libpad.c
- padGetConnection() : libpad.h , libpad.c
- padGetDmaStrNew() : libpad.c
- padGetModVersion() : libpad.h , libpad.c , freepad.h , padMiscFuncs.c
- padGetPortMax() : libpad.h , libpad.c , freepad.h , padMiscFuncs.c
- padGetReqState() : libpad.h , libpad.c
- padGetSlotMax() : libpad.h , libpad.c
- padGetState() : libpad.h , libpad.c
- padInfoAct() : libpad.h , libpad.c
- padInfoMode() : libpad.h , libpad.c
- padInfoPressMode() : libpad.h , libpad.c
- padInit() : libpad.h , libpad.c
- padPortClose() : libpad.h , libpad.c
- padPortInit() : libpad.h , libpad.c
- padPortOpen() : libpad.h , libpad.c
- padRead() : libpad.h , libpad.c
- padSetActAlign() : libpad.h , libpad.c
- padSetActDirect() : libpad.h , libpad.c
- padSetMainMode() : libpad.h , libpad.c
- padSetReqState() : libpad.h , libpad.c
- play_thread() : audsrv.c
- poweroffChangeThreadPriority() : libpwroff.h
- poweroffInit() : libpwroff.h
- poweroffSetCallback() : libpwroff.h
- poweroffShutdown() : libpwroff.h
- print_hex_buffer() : common.c , common.h
- process_toc() : cdrom.c
- progdma() : scr_printf.c
- ps2_screenshot() : screenshot.h , screenshot.c
- ps2_screenshot_16to32_buffer() : screenshot.c
- ps2_screenshot_16to32_line() : screenshot.c
- PS2CamCallback() : ps2cam.h , ps2cam.c
- PS2CamCloseDevice() : ps2cam_rpc.h , ps2cam.h , ps2cam.c
- PS2CamConnect() : ps2cam.h , ps2cam.c
- PS2CamDisconnect() : ps2cam.h , ps2cam.c
- PS2CamGetDeviceCount() : ps2cam_rpc.h , ps2cam.h , ps2cam.c
- PS2CamGetDeviceInfo() : ps2cam.h , ps2cam.c
- PS2CamGetDeviceSring() : ps2cam.h , ps2cam.c
- PS2CamGetDeviceStatus() : ps2cam_rpc.h , ps2cam.h , ps2cam.c
- PS2CamGetIRXVersion() : ps2cam_rpc.h , ps2cam.h , ps2cam.c
- PS2CamInit() : ps2cam_rpc.h , ps2cam.h , ps2cam.c
- PS2CamInitDriver() : ps2cam.h , ps2cam.c
- PS2CamInitializeNewDevice() : ps2cam.c , ps2cam.h
- PS2CamOpenDevice() : ps2cam_rpc.h , ps2cam.h , ps2cam.c
- PS2CamProbe() : ps2cam.h , ps2cam.c
- PS2CamReadPacket() : ps2cam.c , ps2cam_rpc.h , ps2cam.h
- PS2CamSelectInterface() : ps2cam.h , ps2cam.c
- PS2CamSetDeviceBandwidth() : ps2cam.h , ps2cam_rpc.h , ps2cam.c
- PS2CamSetDeviceConfig() : ps2cam.h , ps2cam.c
- PS2CamSetDeviceConfiguration() : ps2cam.c , ps2cam.h
- PS2CamSetDeviceDefaults() : ps2cam.h , ps2cam.c
- PS2CamSetLEDMode() : ps2cam_rpc.h , ps2cam.h , ps2cam.c
- ps2fs_Destroy() : ps2_fio.c
- ps2ipInit() : ps2ip.c , ps2ip.h
- ps2ipSetHsyncTicksPerMSec() : ps2ip.h , ps2ip.c
- PS2KbdClose() : libkbd.c , libkbd.h
- PS2KbdFlushBuffer() : libkbd.h , libkbd.c
- PS2KbdInit() : libkbd.h , libkbd.c
- PS2KbdRead() : libkbd.c , libkbd.h
- PS2KbdReadRaw() : libkbd.h , libkbd.c
- PS2KbdResetKeymap() : libkbd.h , libkbd.c
- PS2KbdSetAltmap() : libkbd.c , libkbd.h
- PS2KbdSetBlockingMode() : libkbd.c , libkbd.h
- PS2KbdSetCtrlmap() : libkbd.c , libkbd.h
- PS2KbdSetKeymap() : libkbd.h , libkbd.c
- PS2KbdSetLeds() : libkbd.c , libkbd.h
- PS2KbdSetReadmode() : libkbd.h , libkbd.c
- PS2KbdSetRepeatRate() : libkbd.c , libkbd.h
- PS2KbdSetSpecialmap() : libkbd.h , libkbd.c
- PS2MouseGetReadMode() : libmouse.c , libmouse.h
- PS2MouseInit() : libmouse.h , libmouse.c
- PS2MouseRead() : libmouse.c , libmouse.h
- PS2MouseSetReadMode() : libmouse.c , libmouse.h
- ps2netfs_accept_pktunknown() : ps2_fio.c
- ps2netfs_close_fsys() : ps2_fio.c
- ps2netfs_close_socket() : ps2_fio.c
- ps2netfs_Init() : ps2_fio.h , ps2_fio.c
- ps2netfs_Listener() : ps2_fio.c
- ps2netfs_op_chdir() : ps2_fio.c
- ps2netfs_op_chstat() : ps2_fio.c
- ps2netfs_op_close() : ps2_fio.c
- ps2netfs_op_dclose() : ps2_fio.c
- ps2netfs_op_devctl() : ps2_fio.c
- ps2netfs_op_devlist() : ps2_fio.c
- ps2netfs_op_dopen() : ps2_fio.c
- ps2netfs_op_dread() : ps2_fio.c
- ps2netfs_op_fstype() : ps2_fio.c
- ps2netfs_op_getstat() : ps2_fio.c
- ps2netfs_op_info() : ps2_fio.c
- ps2netfs_op_ioctl() : ps2_fio.c
- ps2netfs_op_ioctl2() : ps2_fio.c
- ps2netfs_op_lseek() : ps2_fio.c
- ps2netfs_op_lseek64() : ps2_fio.c
- ps2netfs_op_mkdir() : ps2_fio.c
- ps2netfs_op_mount() : ps2_fio.c
- ps2netfs_op_open() : ps2_fio.c
- ps2netfs_op_read() : ps2_fio.c
- ps2netfs_op_readlink() : ps2_fio.c
- ps2netfs_op_remove() : ps2_fio.c
- ps2netfs_op_rename() : ps2_fio.c
- ps2netfs_op_rmdir() : ps2_fio.c
- ps2netfs_op_symlink() : ps2_fio.c
- ps2netfs_op_sync() : ps2_fio.c
- ps2netfs_op_umount() : ps2_fio.c
- ps2netfs_op_write() : ps2_fio.c
- ps2netfs_recv_bytes() : ps2_fio.c
- ps2netfs_serv() : ps2_fio.c

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_func_q.html>

###### - q -
- QueryIntrContext() : intrman.h
- QueryIntrStack() : intrman.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_func_r.html>

###### - r -
- read_sectors() : cdrom.c
- realfd() : fakehost.c
- RegisterExceptionHandler() : excepman.h
- RegisterIntrHandler() : intrman.h
- ReleaseIntrHandler() : intrman.h
- RMMan_Close() : librm.h , librm.c
- RMMan_End() : librm.h , librm.c
- RMMan_GetModuleVersion() : librm.h , librm.c
- RMMan_Init() : librm.h , librm.c
- RMMan_Open() : librm.h , librm.c
- RMMan_Read() : librm.c , librm.h
- rpc_command() : rpc_server.c
- rpc_server_thread() : rpc_server.c

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_func_s.html>

###### - s -
- sbv_patch_disable_prefix_check() : sbv_patches.h , patch_disable_prefix_check.c
- sbv_patch_enable_lmb() : patch_enable_lmb.c , sbv_patches.h
- sbv_patch_fileio() : sbv_patches.h
- sbv_patch_romdrv_set_rom1_info() : sbv_patches.h , patch_romdrv_set_rom1_info.c
- sbv_patch_user_mem_clear() : sbv_patches.h , patch_user_mem_clear.c
- sceCdApplyNCmd() : libcdvd-common.h
- sceCdApplySCmd() : libcdvd-common.h
- sceCdApplySCmd2() : cdvdman.h
- sceCdApplySCmd3() : cdvdman.h
- sceCdAutoAdjustCtrl() : libcdvd-common.h
- sceCdBlueLEDCtl() : libcdvd-common.h
- sceCdBootCertify() : libcdvd-common.h
- sceCdBreak() : libcdvd-common.h
- sceCdBuzzerCtl() : libcdvd-common.h
- sceCdCallback() : libcdvd-common.h
- sceCdCancelPOffRdy() : libcdvd-common.h
- sceCdChangeThreadPriority() : libcdvd-common.h , cdvdfsv.h
- sceCdChgSys() : libcdvd-common.h
- sceCdCloseConfig() : libcdvd-common.h
- sceCdCtrlADout() : libcdvd-common.h
- sceCdDecSet() : libcdvd-common.h
- sceCdDeobfuscateUsingUniqueKey() : cdvdman.h
- sceCdDiskReady() : libcdvd-common.h
- sceCdDoesUniqueKeyExist() : libcdvd-common.h
- sceCdForbidDVDP() : libcdvd-common.h
- sceCdForbidRead() : libcdvd-common.h
- sceCdGetDiskType() : libcdvd-common.h
- sceCdGetError() : libcdvd-common.h
- sceCdGetMediumRemoval() : libcdvd-common.h
- sceCdGetReadPos() : libcdvd-common.h
- sceCdGetToc() : libcdvd-common.h
- sceCdGetToc2() : libcdvd-common.h
- sceCdGetWakeUpReason() : libcdvd-common.h
- sceCdInit() : libcdvd-common.h
- sceCdInitEeCB() : libcdvd-common.h
- sceCdIntToPos() : libcdvd-common.h
- sceCdLayerSearchFile() : libcdvd-common.h
- sceCdMmode() : libcdvd-common.h
- sceCdMV() : libcdvd-common.h
- sceCdNCmdDiskReady() : libcdvd.h
- sceCdNoticeGameStart() : libcdvd-common.h
- sceCdOpenConfig() : libcdvd-common.h
- sceCdPause() : libcdvd-common.h
- sceCdPOffCallback() : libcdvd-common.h
- sceCdPosToInt() : libcdvd-common.h
- sceCdPowerOff() : libcdvd-common.h
- sceCdRcBypassCtl() : libcdvd-common.h
- sceCdRE() : libcdvd-common.h
- sceCdRead() : libcdvd-common.h
- sceCdReadChain() : libcdvd-common.h
- sceCdReadClock() : libcdvd-common.h
- sceCdReadConfig() : libcdvd-common.h
- sceCdReadConsoleID() : libcdvd-common.h
- sceCdReadDiskID() : cdvdman.h
- sceCdReadDvdDualInfo() : libcdvd-common.h
- sceCdReadFull() : libcdvd-common.h
- sceCdReadGUID() : libcdvd-common.h
- sceCdReadIOPMem() : libcdvd.h
- sceCdReadKey() : libcdvd-common.h
- sceCdReadModelID() : libcdvd-common.h
- sceCdReadNVM() : libcdvd-common.h
- sceCdReadPS1BootParam() : libcdvd-common.h
- sceCdReadRegionParams() : libcdvd-common.h
- sceCdReadSUBQ() : libcdvd-common.h
- sceCdReadWakeUpTime() : libcdvd-common.h
- sceCdRI() : libcdvd-common.h
- sceCdRM() : libcdvd-common.h
- sceCdRV() : cdvdman.h
- sceCdSearchFile() : libcdvd-common.h
- sceCdSeek() : libcdvd-common.h
- sceCdSendSCmd1D() : libcdvd-common.h
- sceCdSetAtapiEjectCallback() : cdvdman.h
- sceCdSetFanProfile() : libcdvd-common.h
- sceCdSetHDMode() : libcdvd-common.h
- sceCdSetLEDsMode() : libcdvd-common.h
- sceCdSetMediumRemoval() : libcdvd-common.h
- sceCdSetTimeout() : libcdvd-common.h
- sceCdSpinCtrlEE() : libcdvd.h
- sceCdSpinCtrlIOP() : cdvdman.h
- sceCdStandby() : libcdvd-common.h
- sceCdStatus() : libcdvd-common.h
- sceCdStatus2() : libcdvd-common.h
- sceCdStInit() : libcdvd-common.h
- sceCdStop() : libcdvd-common.h
- sceCdStPause() : libcdvd-common.h
- sceCdStRead() : libcdvd-common.h
- sceCdStResume() : libcdvd-common.h
- sceCdStSeek() : libcdvd-common.h
- sceCdStSeekF() : libcdvd-common.h
- sceCdStStart() : libcdvd-common.h
- sceCdStStat() : libcdvd-common.h
- sceCdStStop() : libcdvd-common.h
- sceCdSync() : libcdvd-common.h
- sceCdTrayReq() : libcdvd-common.h
- sceCdWI() : libcdvd-common.h
- sceCdWM() : libcdvd-common.h
- sceCdWriteClock() : libcdvd-common.h
- sceCdWriteConfig() : libcdvd-common.h
- sceCdWriteConsoleID() : libcdvd-common.h
- sceCdWriteNVM() : libcdvd-common.h
- sceCdWriteRegionParams() : libcdvd-common.h
- sceCdWriteWakeUpTime() : libcdvd-common.h
- sceCdXBSPowerCtl() : libcdvd-common.h
- sceCdXDVRPReset() : libcdvd-common.h
- sceCdXLEDCtl() : libcdvd-common.h
- sceRemote2_7() : libcdvd-common.h
- sceRemote2_7Get() : libcdvd-common.h
- set_error() : audsrv_rpc.c
- SetBPC() : hwbp.h
- SetDAB() : hwbp.h
- SetDABM() : hwbp.h
- SetDataAddrBP() : hwbp.h
- SetDataValueBP() : hwbp.h
- SetDVB() : hwbp.h
- SetDVBM() : hwbp.h
- SetIAB() : hwbp.h
- SetIABM() : hwbp.h
- SetInstructionBP() : hwbp.h
- SetNewCtxCb() : intrman.h
- setReg8() : ps2cam.h , ps2cam.c
- setReg8Mask() : ps2cam.c , ps2cam.h
- shutdown() : commandline.c , main.c
- SifExecModuleBuffer() : loadfile.h
- SifExecModuleFile() : loadfile.h
- SifIopGetVal() : loadfile.h
- SifIopIsAlive() : iopcontrol.h
- SifIopReboot() : iopcontrol.h
- SifIopRebootBuffer() : iopcontrol_special.h
- SifIopRebootBufferEncrypted() : iopcontrol_special.h
- SifIopReset() : iopcontrol.h
- SifIopSetVal() : loadfile.h
- SifIopSync() : iopcontrol.h
- SifLoadElf() : loadfile.h
- SifLoadElfEncrypted() : loadfile.h
- SifLoadElfPart() : loadfile.h
- SifLoadFileExit() : loadfile.h
- SifLoadFileInit() : loadfile.h
- SifLoadModule() : loadfile.h
- SifLoadModuleBuffer() : loadfile.h
- SifLoadModuleEncrypted() : loadfile.h
- SifLoadStartModule() : loadfile.h
- SifLoadStartModuleBuffer() : loadfile.h
- sio_flush() : sior.h , sio.h
- sio_getc_block() : sio.h , sior.h
- sio_gets() : sior.h , sio.h
- sio_read() : sio.h
- sio_write() : sio.h
- slib_exp_lib_list() : slib.c , slib.h
- slib_get_exp_lib() : slib.c , slib.h
- slib_get_exportlist_by_name() : slib.c , iopmgr.h
- slib_get_lib_by_name() : iopmgr.h , slib.c
- slib_get_version_by_name() : iopmgr.h , slib.c
- slib_release_library() : iopmgr.h , slib.c
- SMapIFInit() : ps2ip.c
- smod_get_mod_by_name() : iopmgr.h , smod.h , smod.c
- smod_get_modcount_by_name() : iopmgr.h , smod.c
- smod_get_modversion_by_name() : smod.c , iopmgr.h
- smod_get_next_mod() : smod.c , smod.h , iopmgr.h
- smod_unload_module() : iopmgr.h , smod.c
- strcpy_ascii() : sjis.h
- strcpy_sjis() : sjis.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_func_t.html>

###### - t -
- transfer_complete() : audsrv.c

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_func_u.html>

###### - u -
- update_volume() : audsrv.c

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_func_v.html>

###### - v -
- vector_add() : math3d.h
- vector_apply() : math3d.h
- vector_clamp() : math3d.h
- vector_copy() : math3d.h
- vector_cross_product() : math3d.h
- vector_innerproduct() : math3d.h
- vector_multiply() : math3d.h
- vector_normalize() : math3d.h
- vector_outerproduct() : math3d.h
- vector_triangle_normal() : math3d.h
- VuxUpdateLocalScreenMatrix() : libvux.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_func_x.html>

###### - x -
- xfromChangeThreadPriority() : libmc.h , libmc.c
- xfromChdir() : libmc.c , libmc.h
- xfromClose() : libmc.h , libmc.c
- xfromDelete() : libmc.c , libmc.h
- xfromEraseBlock() : libmc.h , libmc.c
- xfromFlush() : libmc.h , libmc.c
- xfromFormat() : libmc.h , libmc.c
- xfromGetDir() : libmc.c , libmc.h
- xfromGetEntSpace() : libmc.h , libmc.c
- xfromGetInfo() : libmc.h , libmc.c
- xfromInit() : libmc.h , libmc.c
- xfromMkDir() : libmc.h , libmc.c
- xfromOpen() : libmc.h , libmc.c
- xfromRead() : libmc.h , libmc.c
- xfromReadPage() : libmc.h , libmc.c
- xfromRename() : libmc.c , libmc.h
- xfromReset() : libmc.c , libmc.h
- xfromSeek() : libmc.h , libmc.c
- xfromSetFileInfo() : libmc.c , libmc.h
- xfromSync() : libmc.h , libmc.c
- xfromUnformat() : libmc.h , libmc.c
- xfromWrite() : libmc.h , libmc.c
- xfromWritePage() : libmc.c , libmc.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_g.html>

Here is a list of all documented functions, variables, defines, enums, and typedefs with links to the documentation:
###### - g -
- GetBPC() : hwbp.h
- GetDAB() : hwbp.h
- GetDABM() : hwbp.h
- GetDVB() : hwbp.h
- GetDVBM() : hwbp.h
- GetIAB() : hwbp.h
- GetIABM() : hwbp.h
- GetLibraryEntryTable() : loadcore.h
- getReg8() : ps2cam.h , ps2cam.c
- GetRomName() : rom0_info.h
- GIF_BLOCK_SIZE : gif_tags.h
- GIF_FLG_IMAGE : gif_tags.h
- GIF_FLG_PACKED : gif_tags.h
- GIF_FLG_REGLIST : gif_tags.h
- GIF_PRE_DISABLE : gif_tags.h
- GIF_PRE_ENABLE : gif_tags.h
- GIF_PRIM_LINE : gif_tags.h
- GIF_PRIM_LINE_STRIP : gif_tags.h
- GIF_PRIM_POINT : gif_tags.h
- GIF_PRIM_SPRITE : gif_tags.h
- GIF_PRIM_TRIANGLE : gif_tags.h
- GIF_PRIM_TRIANGLE_FAN : gif_tags.h
- GIF_PRIM_TRIANGLE_STRIP : gif_tags.h
- gif_rd_ad : libgs.h
- gif_rd_nop : libgs.h
- GIF_REG_AD : gif_tags.h
- GIF_REG_CLAMP : gif_tags.h
- GIF_REG_CLAMP_1 : gif_tags.h
- GIF_REG_CLAMP_2 : gif_tags.h
- GIF_REG_CNT : gif_registers.h
- GIF_REG_CTRL : gif_registers.h
- GIF_REG_FOG : gif_tags.h
- GIF_REG_MODE : gif_registers.h
- GIF_REG_NOP : gif_tags.h
- GIF_REG_P3CNT : gif_registers.h
- GIF_REG_P3TAG : gif_registers.h
- GIF_REG_PRIM : gif_tags.h
- GIF_REG_RGBAQ : gif_tags.h
- GIF_REG_ST : gif_tags.h
- GIF_REG_STAT : gif_registers.h
- GIF_REG_TAG0 : gif_registers.h
- GIF_REG_TAG1 : gif_registers.h
- GIF_REG_TAG2 : gif_registers.h
- GIF_REG_TAG3 : gif_registers.h
- GIF_REG_TEX0 : gif_tags.h
- GIF_REG_TEX0_1 : gif_tags.h
- GIF_REG_TEX0_2 : gif_tags.h
- GIF_REG_UV : gif_tags.h
- GIF_REG_XYZ2 : gif_tags.h
- GIF_REG_XYZ3 : gif_tags.h
- GIF_REG_XYZF2 : gif_tags.h
- GIF_REG_XYZF3 : gif_tags.h
- graph_add_vsync_handler() : graph.h
- GRAPH_ALIGN_BLOCK : graph_vram.h
- GRAPH_ALIGN_PAGE : graph_vram.h
- graph_aspect_ratio() : graph.h
- GRAPH_BLEND_RC2 : graph.h
- graph_check_vsync() : graph.h
- GRAPH_DISABLE : graph.h
- graph_disable_output() : graph.h
- graph_enable_output() : graph.h
- GRAPH_GCONT_RGB : graph.h
- graph_get_config() : graph_config.h
- graph_get_region() : graph.h
- graph_initialize() : graph.h
- graph_load_config() : graph_config.h
- graph_make_config() : graph_config.h
- GRAPH_MODE_AUTO : graph.h
- GRAPH_MODE_HDTV_1080I : graph.h
- GRAPH_MODE_HDTV_480P : graph.h
- GRAPH_MODE_HDTV_576P : graph.h
- GRAPH_MODE_HDTV_720P : graph.h
- GRAPH_MODE_NTSC : graph.h
- GRAPH_MODE_PAL : graph.h
- GRAPH_MODE_VGA_1024_60 : graph.h
- GRAPH_MODE_VGA_1024_70 : graph.h
- GRAPH_MODE_VGA_1024_75 : graph.h
- GRAPH_MODE_VGA_1024_85 : graph.h
- GRAPH_MODE_VGA_1280_60 : graph.h
- GRAPH_MODE_VGA_1280_75 : graph.h
- GRAPH_MODE_VGA_640_60 : graph.h
- GRAPH_MODE_VGA_640_72 : graph.h
- GRAPH_MODE_VGA_640_75 : graph.h
- GRAPH_MODE_VGA_640_85 : graph.h
- GRAPH_MODE_VGA_800_56 : graph.h
- GRAPH_MODE_VGA_800_60 : graph.h
- GRAPH_MODE_VGA_800_72 : graph.h
- GRAPH_MODE_VGA_800_75 : graph.h
- GRAPH_MODE_VGA_800_85 : graph.h
- GRAPH_RC1_ALPHA : graph.h
- graph_remove_vsync_handler() : graph.h
- graph_save_config() : graph_config.h
- graph_set_bgcolor() : graph.h
- graph_set_config() : graph_config.h
- graph_set_framebuffer() : graph.h
- graph_set_framebuffer_filtered() : graph.h
- graph_set_mode() : graph.h
- graph_set_output() : graph.h
- graph_set_screen() : graph.h
- graph_shutdown() : graph.h
- graph_start_vsync() : graph.h
- GRAPH_VALUE_RC1 : graph.h
- graph_vram_allocate() : graph_vram.h
- graph_vram_clear() : graph_vram.h
- graph_vram_free() : graph_vram.h
- GRAPH_VRAM_MAX_WORDS : graph_vram.h
- graph_vram_size() : graph_vram.h
- graph_wait_hsync() : graph.h
- graph_wait_vsync() : graph.h
- GS_ALPHA_NO_UPDATE : libgs.h
- GS_CLUT_32 : libgs.h
- GS_FFMD_FIELD : libgs.h
- GS_FFMD_FRAME : libgs.h
- gs_g_alpha_1 : libgs.h
- gs_g_alpha_2 : libgs.h
- gs_g_bitbltbuf : libgs.h
- gs_g_clamp_1 : libgs.h
- gs_g_clamp_2 : libgs.h
- gs_g_colclamp : libgs.h
- gs_g_dimx : libgs.h
- gs_g_dthe : libgs.h
- gs_g_fba_1 : libgs.h
- gs_g_fba_2 : libgs.h
- gs_g_fog : libgs.h
- gs_g_fogcol : libgs.h
- gs_g_frame_1 : libgs.h
- gs_g_frame_2 : libgs.h
- gs_g_miptbp1_1 : libgs.h
- gs_g_miptbp1_2 : libgs.h
- gs_g_miptbp2_1 : libgs.h
- gs_g_miptbp2_2 : libgs.h
- gs_g_nop : libgs.h
- gs_g_pabe : libgs.h
- gs_g_prim : libgs.h
- gs_g_prmode : libgs.h
- gs_g_prmodecont : libgs.h
- gs_g_rgbaq : libgs.h
- gs_g_scanmsk : libgs.h
- gs_g_scissor_1 : libgs.h
- gs_g_scissor_2 : libgs.h
- gs_g_st : libgs.h
- gs_g_test_1 : libgs.h
- gs_g_test_2 : libgs.h
- gs_g_tex0_1 : libgs.h
- gs_g_tex0_2 : libgs.h
- gs_g_tex2_1 : libgs.h
- gs_g_tex2_2 : libgs.h
- gs_g_texa : libgs.h
- gs_g_texflush : libgs.h
- gs_g_trxdir : libgs.h
- gs_g_trxpos : libgs.h
- gs_g_trxreg : libgs.h
- gs_g_uv : libgs.h
- gs_g_xyoffset_1 : libgs.h
- gs_g_xyoffset_2 : libgs.h
- gs_g_xyz2 : libgs.h
- gs_g_xyz3 : libgs.h
- gs_g_xyzf2 : libgs.h
- gs_g_xyzf3 : libgs.h
- gs_g_zbuf_1 : libgs.h
- gs_g_zbuf_2 : libgs.h
- GS_GIF_DISABLE : libgs.h
- GS_INIT_DRAW_RESET : libgs.h
- GS_INIT_RESET : libgs.h
- gs_p_bgcolor : libgs.h
- gs_p_busdir : libgs.h
- gs_p_csr : libgs.h
- gs_p_dispfb1 : libgs.h
- gs_p_dispfb2 : libgs.h
- gs_p_display1 : libgs.h
- gs_p_display2 : libgs.h
- gs_p_imr : libgs.h
- gs_p_pmode : libgs.h
- gs_p_siglblid : libgs.h
- gs_p_smode1 : libgs.h
- gs_p_smode2 : libgs.h
- GS_PIXMODE_32 : libgs.h
- GS_PRIM_LINE : gs_gp.h
- GS_PRIM_LINE_STRIP : gs_gp.h
- GS_PRIM_POINT : gs_gp.h
- GS_PRIM_SPRITE : gs_gp.h
- GS_PRIM_TRIANGLE : gs_gp.h
- GS_PRIM_TRIANGLE_FAN : gs_gp.h
- GS_PRIM_TRIANGLE_STRIP : gs_gp.h
- GS_PSM_16 : gs_psm.h
- GS_PSM_16S : gs_psm.h
- GS_PSM_24 : gs_psm.h
- GS_PSM_32 : gs_psm.h
- GS_PSM_4 : gs_psm.h
- GS_PSM_4HH : gs_psm.h
- GS_PSM_4HL : gs_psm.h
- GS_PSM_8 : gs_psm.h
- GS_PSM_8H : gs_psm.h
- GS_PSM_PS24 : gs_psm.h
- GS_PSMZ_16 : gs_psm.h
- GS_PSMZ_16S : gs_psm.h
- GS_PSMZ_24 : gs_psm.h
- GS_PSMZ_32 : gs_psm.h
- GS_REG_ALPHA : gs_gp.h
- GS_REG_ALPHA_1 : gs_gp.h
- GS_REG_ALPHA_2 : gs_gp.h
- GS_REG_BGCOLOR : gs_privileged.h
- GS_REG_BITBLTBUF : gs_gp.h
- GS_REG_BUSDIR : gs_privileged.h
- GS_REG_CLAMP : gs_gp.h
- GS_REG_CLAMP_1 : gs_gp.h
- GS_REG_CLAMP_2 : gs_gp.h
- GS_REG_COLCLAMP : gs_gp.h
- GS_REG_CSR : gs_privileged.h
- GS_REG_DIMX : gs_gp.h
- GS_REG_DISPFB1 : gs_privileged.h
- GS_REG_DISPFB2 : gs_privileged.h
- GS_REG_DISPLAY1 : gs_privileged.h
- GS_REG_DISPLAY2 : gs_privileged.h
- GS_REG_DTHE : gs_gp.h
- GS_REG_EXTBUF : gs_privileged.h
- GS_REG_EXTDATA : gs_privileged.h
- GS_REG_EXTWRITE : gs_privileged.h
- GS_REG_FBA : gs_gp.h
- GS_REG_FBA_1 : gs_gp.h
- GS_REG_FBA_2 : gs_gp.h
- GS_REG_FINISH : gs_gp.h
- GS_REG_FOG : gs_gp.h
- GS_REG_FOGCOL : gs_gp.h
- GS_REG_FRAME : gs_gp.h
- GS_REG_FRAME_1 : gs_gp.h
- GS_REG_FRAME_2 : gs_gp.h
- GS_REG_HWREG : gs_gp.h
- GS_REG_IMR : gs_privileged.h
- GS_REG_LABEL : gs_gp.h
- GS_REG_MIPTBP1 : gs_gp.h
- GS_REG_MIPTBP1_1 : gs_gp.h
- GS_REG_MIPTBP1_2 : gs_gp.h
- GS_REG_MIPTBP2 : gs_gp.h
- GS_REG_MIPTBP2_1 : gs_gp.h
- GS_REG_MIPTBP2_2 : gs_gp.h
- GS_REG_NOP : gs_gp.h
- GS_REG_PABE : gs_gp.h
- GS_REG_PMODE : gs_privileged.h
- GS_REG_PRIM : gs_gp.h
- GS_REG_PRMODE : gs_gp.h
- GS_REG_PRMODECONT : gs_gp.h
- GS_REG_RGBAQ : gs_gp.h
- GS_REG_SCANMSK : gs_gp.h
- GS_REG_SCISSOR : gs_gp.h
- GS_REG_SCISSOR_1 : gs_gp.h
- GS_REG_SCISSOR_2 : gs_gp.h
- GS_REG_SIGLBLID : gs_privileged.h
- GS_REG_SIGNAL : gs_gp.h
- GS_REG_SMODE1 : gs_privileged.h
- GS_REG_SMODE2 : gs_privileged.h
- GS_REG_SRFSH : gs_privileged.h
- GS_REG_ST : gs_gp.h
- GS_REG_SYNCH1 : gs_privileged.h
- GS_REG_SYNCH2 : gs_privileged.h
- GS_REG_SYNCHV : gs_privileged.h
- GS_REG_TEST : gs_gp.h
- GS_REG_TEST_1 : gs_gp.h
- GS_REG_TEST_2 : gs_gp.h
- GS_REG_TEX0 : gs_gp.h
- GS_REG_TEX0_1 : gs_gp.h
- GS_REG_TEX0_2 : gs_gp.h
- GS_REG_TEX1 : gs_gp.h
- GS_REG_TEX1_1 : gs_gp.h
- GS_REG_TEX1_2 : gs_gp.h
- GS_REG_TEX2 : gs_gp.h
- GS_REG_TEX2_1 : gs_gp.h
- GS_REG_TEX2_2 : gs_gp.h
- GS_REG_TEXA : gs_gp.h
- GS_REG_TEXCLUT : gs_gp.h
- GS_REG_TEXFLUSH : gs_gp.h
- GS_REG_TRXDIR : gs_gp.h
- GS_REG_TRXPOS : gs_gp.h
- GS_REG_TRXREG : gs_gp.h
- GS_REG_UV : gs_gp.h
- GS_REG_XYOFFSET : gs_gp.h
- GS_REG_XYOFFSET_1 : gs_gp.h
- GS_REG_XYOFFSET_2 : gs_gp.h
- GS_REG_XYZ2 : gs_gp.h
- GS_REG_XYZ3 : gs_gp.h
- GS_REG_XYZF2 : gs_gp.h
- GS_REG_XYZF3 : gs_gp.h
- GS_REG_ZBUF : gs_gp.h
- GS_REG_ZBUF_1 : gs_gp.h
- GS_REG_ZBUF_2 : gs_gp.h
- GS_SET_SMODE1 : libgs.h
- GS_TEX_32 : libgs.h
- GS_TEX_CALC : libgs.h
- GS_TEX_DECAL : libgs.h
- GS_TEX_FIXED : libgs.h
- GS_TEX_HIGHLIHGT1 : libgs.h
- GS_TEX_HIGHLIHGT2 : libgs.h
- GS_TEX_LINEAR : libgs.h
- GS_TEX_MIPMAP0 : libgs.h
- GS_TEX_MIPMAP1 : libgs.h
- GS_TEX_MIPMAP2 : libgs.h
- GS_TEX_MIPMAP3 : libgs.h
- GS_TEX_MIPMAP4 : libgs.h
- GS_TEX_MIPMAP5 : libgs.h
- GS_TEX_MIPMAP6 : libgs.h
- GS_TEX_MIPMAP_AUTO : libgs.h
- GS_TEX_MIPMAP_DEFINE : libgs.h
- GS_TEX_NEAREST : libgs.h
- GS_ZBUF_16 : gs_psm.h
- GS_ZBUF_16S : gs_psm.h
- GS_ZBUF_24 : gs_psm.h
- GS_ZBUF_32 : gs_psm.h
- GS_ZBUFF_32 : libgs.h
- GsATestFailedUpdateMethods : libgs.h
- GsATestMethods : libgs.h
- GsClearDrawEnv1() : libgs.h
- GsClearDrawEnv2() : libgs.h
- GsGifDataFormat : libgs.h
- GsPrimitiveTypes : libgs.h
- GsTexFilterMethods : libgs.h
- GsTexFunctions : libgs.h
- GsTexMipmaps : libgs.h
- GsVramFreeAllTextureBuffer() : libgs.h
- GsZTestMethodTypes : libgs.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_h.html>

Here is a list of all documented functions, variables, defines, enums, and typedefs with links to the documentation:
###### - h -
- HasIopRebootedSinceLastCall() : iopcontrol.h
- HDDCTLDRIVEREAD : ioctl.h
- HDDCTLDRIVEWRITE : ioctl.h
- HDDCTLFLUSH : ioctl.h
- HDDCTLGETDATE : ioctl.h
- HDDCTLGETERROR : ioctl.h
- HDDCTLGETERRORID : ioctl.h
- HDDCTLGETFMTVER : ioctl.h
- HDDCTLGETMAXSECT : ioctl.h
- HDDCTLGETSMARTSTAT : ioctl.h
- HDDCTLGETSTATUS : ioctl.h
- HDDCTLGETTOTALSECT : ioctl.h
- HDDCTLINSTALLOSD : ioctl.h
- HDDCTLSCEIDENTIFY : ioctl.h
- HDDCTLSETIDLE : ioctl.h
- HDDCTLSHUTDOWN : ioctl.h
- HDDCTLSWAPTMP : ioctl.h
- HDDIOCADDSUB : ioctl.h
- HDDIOCDELSUB : ioctl.h
- HDDIOCDEVIO : ioctl.h
- HDDIOCFLUSH : ioctl.h
- HDDIOCGETERROR : ioctl.h
- HDDIOCGETSIZE : ioctl.h
- HDDIOCGETSUBS : ioctl.h
- HDDIOCSETERROR : ioctl.h
- HDEV : devfs.h
- HDIOC_FREESECTOR : hdd-ioctl.h
- HDIOC_GETERRORPARTNAME : hdd-ioctl.h
- HDIOC_MAXSECTOR : hdd-ioctl.h
- HDIOC_READSECTOR : hdd-ioctl.h
- HDIOC_SCEIDENTIFY : hdd-ioctl.h
- HDIOC_SETMAXLBA28 : hdd-ioctl.h
- HDIOC_SETOSDMBR : hdd-ioctl.h
- HDIOC_TOTALSECTOR : hdd-ioctl.h
- HDIOC_WRITESECTOR : hdd-ioctl.h
- HIOCGETPARTERROR : hdd-ioctl.h
- HIOCGETSIZE : hdd-ioctl.h
- HIOCSETPARTERROR : hdd-ioctl.h
- HIOCTRANSFER : hdd-ioctl.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_i.html>

Here is a list of all documented functions, variables, defines, enums, and typedefs with links to the documentation:
###### - i -
- INADDR_ANY : tcpip.h
- INADDR_BROADCAST : tcpip.h
- INADDR_LOOPBACK : tcpip.h
- INADDR_NONE : tcpip.h
- init_devfs() : devfs.c
- INIT_DMAC : kernel.h
- InitBPC() : hwbp.h
- initialized : audsrv.c
- INVALID_HDEV : devfs.h
- ioctl_handler : devfs.h
- iomanX_format() : iomanX.h , iomanX.c
- iomanX_iop_file_t : iomanX.h
- IOP_CHCR_30 : iop_regs.h
- IOP_CHCR_CO : iop_regs.h
- IOP_CHCR_DR : iop_regs.h
- IOP_CHCR_LI : iop_regs.h
- IOP_CHCR_TR : iop_regs.h
- IOP_DCIC_D : iop_cop0_defs.h
- IOP_DCIC_DA : iop_cop0_defs.h
- IOP_DCIC_DAE : iop_cop0_defs.h
- IOP_DCIC_DB : iop_cop0_defs.h
- IOP_DCIC_DE : iop_cop0_defs.h
- IOP_DCIC_DL : iop_cop0_defs.h
- IOP_DCIC_DR : iop_cop0_defs.h
- IOP_DCIC_DW : iop_cop0_defs.h
- IOP_DCIC_I : iop_cop0_defs.h
- IOP_DCIC_IL : iop_cop0_defs.h
- IOP_DCIC_KD : iop_cop0_defs.h
- IOP_DCIC_PC : iop_cop0_defs.h
- IOP_DCIC_PCE : iop_cop0_defs.h
- IOP_DCIC_R : iop_cop0_defs.h
- IOP_DCIC_T : iop_cop0_defs.h
- IOP_DCIC_TE : iop_cop0_defs.h
- IOP_DCIC_TR : iop_cop0_defs.h
- IOP_DCIC_UD : iop_cop0_defs.h
- IOP_DCIC_W : iop_cop0_defs.h
- IOP_DT_FSEXT : iomanX.h
- IOP_EXCEPTION_ADEL : excepman.h
- IOP_EXCEPTION_ADES : excepman.h
- IOP_EXCEPTION_BP : excepman.h
- IOP_EXCEPTION_CPU : excepman.h
- IOP_EXCEPTION_DBE : excepman.h
- IOP_EXCEPTION_HDB : excepman.h
- IOP_EXCEPTION_IBE : excepman.h
- IOP_EXCEPTION_INT : excepman.h
- IOP_EXCEPTION_MOD : excepman.h
- IOP_EXCEPTION_OVF : excepman.h
- IOP_EXCEPTION_R13 : excepman.h
- IOP_EXCEPTION_R14 : excepman.h
- IOP_EXCEPTION_RI : excepman.h
- IOP_EXCEPTION_SYS : excepman.h
- IOP_EXCEPTION_TLBL : excepman.h
- IOP_EXCEPTION_TLBS : excepman.h
- iop_file_t : ioman.h
- iop_io_file_t : ioman_mod.h
- IOP_IRQ_DMA : intrman.h
- IOP_IRQ_DMA_BERR : intrman.h
- IOP_IRQ_DVD : intrman.h
- IOP_IRQ_EXTR : intrman.h
- IOP_IRQ_FDMA : intrman.h
- iop_irq_list : intrman.h
- IOP_IRQ_SW1 : intrman.h
- IOP_IRQ_SW2 : intrman.h
- IOP_MEM : ahx_rpc.c , sior_rpc.c
- iop_readwrite() : ahx_rpc.c
- iopbuf : sifcmd.c
- iopmgr_get_device() : iopmgr.h , devices.c
- iopmgr_get_devicelist() : devices.c , iopmgr.h
- iopmgr_get_devicetype() : iopmgr.h , devices.c
- iopmgr_get_iomandev() : devices.c , iopmgr.h
- iopmgr_get_iomanxdev() : iopmgr.h , devices.c
- ioprpgen_setup_membuf() : ioprpgen.h
- ioprpgen_write_ioprp() : ioprpgen.h
- IP4_ADDR : tcpip.h
- IP4_ADDR_ANY : tcpip.h
- IP4_ADDR_ANY4 : tcpip.h
- ip4_addr_copy : tcpip.h
- ip4_addr_get_network : tcpip.h
- ip4_addr_get_u32 : tcpip.h
- ip4_addr_isloopback : tcpip.h
- ip4_addr_netcmp : tcpip.h
- ip4_addr_set : tcpip.h
- ip4_addr_set_any : tcpip.h
- ip4_addr_set_hton : tcpip.h
- ip4_addr_set_loopback : tcpip.h
- ip4_addr_set_u32 : tcpip.h
- ip4_addr_set_zero : tcpip.h
- ip4_addr_t : tcpip.h
- ip4addr_ntoa() : ps2ip.h
- IP6_ADDR : tcpip.h
- IP6_ADDR_BLOCK1 : tcpip.h
- IP6_ADDR_BLOCK2 : tcpip.h
- IP6_ADDR_BLOCK3 : tcpip.h
- IP6_ADDR_BLOCK4 : tcpip.h
- IP6_ADDR_BLOCK5 : tcpip.h
- IP6_ADDR_BLOCK6 : tcpip.h
- IP6_ADDR_BLOCK7 : tcpip.h
- IP6_ADDR_BLOCK8 : tcpip.h
- ip6_addr_copy : tcpip.h
- ip6_addr_netcmp : tcpip.h
- IP6_ADDR_PART : tcpip.h
- ip6_addr_set : tcpip.h
- ip6_addr_set_any : tcpip.h
- ip6_addr_set_hton : tcpip.h
- ip6_addr_set_loopback : tcpip.h
- ip6_addr_set_zero : tcpip.h
- ip6_addr_t : tcpip.h
- IP_ADDR_ANY : tcpip.h
- IPADDR2_COPY : tcpip.h
- IPADDR_ANY : tcpip.h
- IPADDR_BROADCAST : tcpip.h
- IPADDR_LOOPBACK : tcpip.h
- IPADDR_NONE : tcpip.h
- IPADDR_TYPE_ANY : tcpip.h
- IPADDR_TYPE_V4 : tcpip.h
- IPADDR_TYPE_V6 : tcpip.h
- IsDESRMachine() : rom0_info.h
- IsEarlyJap() : osd_config.h
- IsT10K() : rom0_info.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_k.html>

Here is a list of all documented functions, variables, defines, enums, and typedefs with links to the documentation:
###### - k -
- keycap : ps2kbd.c
- keymap : ps2kbd.c

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_l.html>

Here is a list of all documented functions, variables, defines, enums, and typedefs with links to the documentation:
###### - l -
- lc_internals_t : loadcore.h
- LCR_SCS_VAL : sio.c
- LEFT_ALIGN : font.h
- LIGHT_AMBIENT : math3d.h
- LIGHT_DIRECTIONAL : math3d.h
- list_all_libraries() : commandline.c
- list_all_modules() : commandline.c
- list_devices_ioman() : commandline.c
- list_devices_iomanx() : commandline.c
- list_fs_devices() : commandline.c
- LoadELFFromFileWithPartition() : elf-loader.h
- LOD_FORMULAIC : draw_sampling.h
- LOD_MAG_NEAREST : draw_sampling.h
- LOD_MIPMAP_REGISTER : draw_sampling.h
- lwip_ip_addr_type : tcpip.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_m.html>

Here is a list of all documented functions, variables, defines, enums, and typedefs with links to the documentation:
###### - m -
- matrix_copy() : math3d.h
- matrix_inverse() : math3d.h
- matrix_multiply() : math3d.h
- matrix_rotate() : math3d.h
- matrix_scale() : math3d.h
- matrix_translate() : math3d.h
- matrix_transpose() : math3d.h
- matrix_unit() : math3d.h
- MAX_THREADS : kernel.h
- MAX_VOLUME : audsrv.h
- MC_ATTR_HIDDEN : libmc.h
- MC_ATTR_OBJECT : libmc.h
- MC_FUNC_NUMBERS : libmc.h
- mcChangeThreadPriority() : libmc.h , libmc.c
- mcChdir() : libmc.h , libmc.c
- mcClose() : libmc.h , libmc.c
- mcDelete() : libmc.h , libmc.c
- mcEraseBlock() : libmc.h , libmc.c
- mcFlush() : libmc.h , libmc.c
- mcFormat() : libmc.h , libmc.c
- mcGetDir() : libmc.h , libmc.c
- mcGetEntSpace() : libmc.h , libmc.c
- mcGetInfo() : libmc.h , libmc.c
- mcGetInfoApdxNew() : libmc.c
- mcGetInfoApdxOld() : libmc.c
- MCICON_TYPES : libmc.h
- mcInit() : libmc.h , libmc.c
- mcMkDir() : libmc.h , libmc.c
- mcOpen() : libmc.h , libmc.c
- mcRead() : libmc.h , libmc.c
- mcReadFixAlignNew() : libmc.c
- mcReadFixAlignOld() : libmc.c
- mcReadPage() : libmc.h , libmc.c
- mcRename() : libmc.h , libmc.c
- mcReset() : libmc.c , libmc.h
- mcSeek() : libmc.h , libmc.c
- mcSetFileInfo() : libmc.h , libmc.c
- mcStoreDir() : libmc.c
- mcSync() : libmc.c , libmc.h
- mcUnformat() : libmc.c , libmc.h
- mcWrite() : libmc.c , libmc.h
- mcWritePage() : libmc.h , libmc.c
- MFD_OFF : dma_registers.h
- MIN : audsrv_internal.h
- MIN_VOLUME : audsrv.h
- mips_cop0_reg : mipscopaccess.h
- ModuleInfo_t : loadcore.h
- mouse : ps2mouse.c
- mtapGetConnection() : libmtap.h , libmtap.c
- mtapInit() : libmtap.c , libmtap.h
- mtapPortClose() : libmtap.c , libmtap.h
- mtapPortOpen() : libmtap.c , libmtap.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_n.html>

Here is a list of all documented functions, variables, defines, enums, and typedefs with links to the documentation:
###### - n -
- naplinkRpcHandler() : nprintf.c
- naplinkRpcInit() : fakehost.c , nprintf.c
- napThread() : nprintf.c
- NETIF_ADD_MAC_FILTER : tcpip.h
- netif_default : tcpip.h
- NETIF_DEL_MAC_FILTER : tcpip.h
- netif_find() : ps2ip.h
- NETIF_FLAG_BROADCAST : tcpip.h
- NETIF_FLAG_ETHARP : tcpip.h
- NETIF_FLAG_ETHERNET : tcpip.h
- NETIF_FLAG_IGMP : tcpip.h
- NETIF_FLAG_LINK_UP : tcpip.h
- NETIF_FLAG_MLD6 : tcpip.h
- NETIF_FLAG_UP : tcpip.h
- netif_get_client_data : tcpip.h
- netif_init_fn : tcpip.h
- netif_input_fn : tcpip.h
- netif_is_link_up : tcpip.h
- netif_is_up : tcpip.h
- netif_linkoutput_fn : tcpip.h
- netif_list : tcpip.h
- netif_mac_filter_action : tcpip.h
- NETIF_MAX_HWADDR_LEN : tcpip.h
- netif_output_fn : tcpip.h
- netif_set_client_data : tcpip.h
- netif_status_callback_fn : tcpip.h
- NETMAN_NETIF_DIALUP : netman.h
- NETMAN_NETIF_ETH_LINK_DISABLE_PAUSE : netman.h
- NETMAN_NETIF_ETH_LINK_MODE : netman.h
- NETMAN_NETIF_ETH_LINK_MODE_100M_FDX : netman.h
- NETMAN_NETIF_ETH_LINK_MODE_100M_HDX : netman.h
- NETMAN_NETIF_ETH_LINK_MODE_10M_FDX : netman.h
- NETMAN_NETIF_ETH_LINK_MODE_10M_HDX : netman.h
- NETMAN_NETIF_ETH_LINK_MODE_AUTO : netman.h
- NETMAN_NETIF_ETHERNET : netman.h
- NETMAN_NETIF_IN_USE : netman.h
- NETMAN_NETIF_IOCTL_CODES : netman.h
- NETMAN_NETIF_IOCTL_ETH_GET_MAC : netman.h
- NETMAN_NETIF_IOCTL_ETH_SET_LINK_MODE : netman.h
- NETMAN_NETIF_LINK_UP : netman.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_o.html>

Here is a list of all documented functions, variables, defines, enums, and typedefs with links to the documentation:
###### - o -
- OSD_LANGUAGES : osd_config.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_p.html>

Here is a list of all documented functions, variables, defines, enums, and typedefs with links to the documentation:
###### - p -
- PACKET_F_ALLOC : sifrpc.c
- packet_free() : packet.h
- packet_get_qword() : packet.h
- packet_increment_qwc() : packet.h
- packet_init() : packet.h
- packet_reset() : packet.h
- pad_close() : input.h
- pad_get_buttons() : input.h
- pad_get_mode() : input.h
- pad_get_num_modes() : input.h
- pad_get_state() : input.h
- pad_get_type() : input.h
- pad_has_type() : input.h
- pad_init_actuators() : input.h
- pad_open() : input.h
- pad_set_actuators() : input.h
- pad_set_mode() : input.h
- pad_set_sensitivity() : input.h
- pad_wait() : input.h
- padEnd() : libpad.h , libpad.c , xpadman.h , freepad.h , padMiscFuncs.c
- padEnterPressMode() : libpad.h , libpad.c
- padExitPressMode() : libpad.h , libpad.c
- padGetConnDmaStr() : libpad.c
- padGetConnection() : libpad.h , libpad.c
- padGetDmaStrNew() : libpad.c
- padGetModVersion() : libpad.h , libpad.c , freepad.h , padMiscFuncs.c
- padGetPortMax() : libpad.h , libpad.c , freepad.h , padMiscFuncs.c
- padGetReqState() : libpad.h , libpad.c
- padGetSlotMax() : libpad.h , libpad.c
- padGetState() : libpad.h , libpad.c
- padInfoAct() : libpad.h , libpad.c
- padInfoMode() : libpad.h , libpad.c
- padInfoPressMode() : libpad.h , libpad.c
- padInit() : libpad.h , libpad.c
- padPortClose() : libpad.h , libpad.c
- padPortInit() : libpad.h , libpad.c
- padPortOpen() : libpad.h , libpad.c
- padRead() : libpad.h , libpad.c
- padSetActAlign() : libpad.c , libpad.h
- padSetActDirect() : libpad.h , libpad.c
- padSetMainMode() : libpad.h , libpad.c
- padSetReqState() : libpad.h , libpad.c
- PBUF_IP : tcpip.h
- pbuf_layer : tcpip.h
- PBUF_LINK : tcpip.h
- PBUF_POOL : tcpip.h
- PBUF_RAM : tcpip.h
- PBUF_RAW : tcpip.h
- PBUF_RAW_TX : tcpip.h
- PBUF_REF : tcpip.h
- PBUF_ROM : tcpip.h
- PBUF_TRANSPORT : tcpip.h
- pbuf_type : tcpip.h
- PFS_ZONE_SIZE : ps2_fio.c
- pktbuf : sifcmd.c
- play_thread() : audsrv.c
- play_tid : audsrv.c
- playing : audsrv.c
- poweroff_callback : libpwroff.h
- poweroffChangeThreadPriority() : libpwroff.h
- poweroffInit() : libpwroff.h
- poweroffSetCallback() : libpwroff.h
- poweroffShutdown() : libpwroff.h
- PRIM_MAP_ST : draw_primitives.h
- PRIM_OVERRIDE_ENABLE : draw_primitives.h
- PRIM_POINT : draw_primitives.h
- PRIM_SHADE_FLAT : draw_primitives.h
- PRIM_UNFIXED : draw_primitives.h
- print_hex_buffer() : common.c , common.h
- process_toc() : cdrom.c
- progdma() : scr_printf.c
- ps2_screenshot() : screenshot.h , screenshot.c
- ps2_screenshot_16to32_buffer() : screenshot.c
- ps2_screenshot_16to32_line() : screenshot.c
- PS2CAM_PROD_EYETOY : ps2cam.h
- PS2CAM_PROD_EYETOY2 : ps2cam.h
- PS2CAM_PROD_EYETOY3 : ps2cam.h
- PS2CAM_PROD_EYETOY4 : ps2cam.h
- PS2CAM_PROD_VISUALSTREAM : ps2cam.h
- PS2CAM_RPC_GETDEVCOUNT : ps2cam_rpc.h , ps2cam.h
- PS2CAM_RPC_GETDEVINFO : ps2cam_rpc.h , ps2cam.h
- PS2CAM_RPC_GETDEVSTATUS : ps2cam_rpc.h , ps2cam.h
- PS2CAM_RPC_GETIRXVERSION : ps2cam_rpc.h , ps2cam.h
- PS2CAM_RPC_INITIALIZE : ps2cam_rpc.h , ps2cam.h
- PS2CAM_RPC_READPACKET : ps2cam_rpc.h , ps2cam.h
- PS2CAM_RPC_SETDEVBANDWIDTH : ps2cam_rpc.h , ps2cam.h
- PS2CAM_RPC_SETLEDMODE : ps2cam_rpc.h , ps2cam.h
- PS2CAM_VEND_DLINK : ps2cam.h
- PS2CAM_VEND_LOGITECH : ps2cam.h
- PS2CAM_VEND_SONY : ps2cam.h
- PS2CamCallback() : ps2cam.h , ps2cam.c
- PS2CamCloseDevice() : ps2cam_rpc.h , ps2cam.h , ps2cam.c
- PS2CamConnect() : ps2cam.h , ps2cam.c
- PS2CamDisconnect() : ps2cam.h , ps2cam.c
- PS2CamGetDeviceCount() : ps2cam_rpc.h , ps2cam.h , ps2cam.c
- PS2CamGetDeviceInfo() : ps2cam.h , ps2cam.c
- PS2CamGetDeviceSring() : ps2cam.h , ps2cam.c
- PS2CamGetDeviceStatus() : ps2cam_rpc.h , ps2cam.h , ps2cam.c
- PS2CamGetIRXVersion() : ps2cam_rpc.h , ps2cam.h , ps2cam.c
- PS2CamInit() : ps2cam.h , ps2cam.c , ps2cam_rpc.h
- PS2CamInitDriver() : ps2cam.h , ps2cam.c
- PS2CamInitializeNewDevice() : ps2cam.h , ps2cam.c
- PS2CamOpenDevice() : ps2cam_rpc.h , ps2cam.c , ps2cam.h
- PS2CamProbe() : ps2cam.h , ps2cam.c
- PS2CamReadPacket() : ps2cam_rpc.h , ps2cam.h , ps2cam.c
- PS2CamSelectInterface() : ps2cam.h , ps2cam.c
- PS2CamSetDeviceBandwidth() : ps2cam_rpc.h , ps2cam.h , ps2cam.c
- PS2CamSetDeviceConfig() : ps2cam.c , ps2cam.h
- PS2CamSetDeviceConfiguration() : ps2cam.h , ps2cam.c
- PS2CamSetDeviceDefaults() : ps2cam.c , ps2cam.h
- PS2CamSetLEDMode() : ps2cam_rpc.h , ps2cam.h , ps2cam.c
- ps2fs_Destroy() : ps2_fio.c
- ps2ipInit() : ps2ip.h , ps2ip.c
- ps2ipSetHsyncTicksPerMSec() : ps2ip.h , ps2ip.c
- PS2KBD_IOCTL_FLUSHBUFFER : ps2kbd.h
- PS2KBD_IOCTL_RESETKEYMAP : ps2kbd.h
- PS2KBD_IOCTL_SETALTMAP : ps2kbd.h
- PS2KBD_IOCTL_SETBLOCKMODE : ps2kbd.h
- PS2KBD_IOCTL_SETCTRLMAP : ps2kbd.h
- PS2KBD_IOCTL_SETKEYMAP : ps2kbd.h
- PS2KBD_IOCTL_SETLEDS : ps2kbd.h
- PS2KBD_IOCTL_SETREADMODE : ps2kbd.h
- PS2KBD_IOCTL_SETREPEATRATE : ps2kbd.h
- PS2KBD_IOCTL_SETSPECIALMAP : ps2kbd.h
- PS2KBD_REPEATWAIT : ps2kbd.c
- PS2KbdClose() : libkbd.c , libkbd.h
- PS2KbdFlushBuffer() : libkbd.h , libkbd.c
- PS2KbdInit() : libkbd.c , libkbd.h
- PS2KbdRead() : libkbd.c , libkbd.h
- PS2KbdReadRaw() : libkbd.c , libkbd.h
- PS2KbdResetKeymap() : libkbd.h , libkbd.c
- PS2KbdSetAltmap() : libkbd.h , libkbd.c
- PS2KbdSetBlockingMode() : libkbd.h , libkbd.c
- PS2KbdSetCtrlmap() : libkbd.h , libkbd.c
- PS2KbdSetKeymap() : libkbd.c , libkbd.h
- PS2KbdSetLeds() : libkbd.h , libkbd.c
- PS2KbdSetReadmode() : libkbd.c , libkbd.h
- PS2KbdSetRepeatRate() : libkbd.c , libkbd.h
- PS2KbdSetSpecialmap() : libkbd.c , libkbd.h
- PS2MouseGetReadMode() : libmouse.h , libmouse.c
- PS2MouseInit() : libmouse.c , libmouse.h
- PS2MouseRead() : libmouse.c , libmouse.h
- PS2MouseSetReadMode() : libmouse.c , libmouse.h
- ps2netfs_accept_pktunknown() : ps2_fio.c
- ps2netfs_close_fsys() : ps2_fio.c
- ps2netfs_close_socket() : ps2_fio.c
- ps2netfs_Init() : ps2_fio.c , ps2_fio.h
- ps2netfs_Listener() : ps2_fio.c
- ps2netfs_op_chdir() : ps2_fio.c
- ps2netfs_op_chstat() : ps2_fio.c
- ps2netfs_op_close() : ps2_fio.c
- ps2netfs_op_dclose() : ps2_fio.c
- ps2netfs_op_devctl() : ps2_fio.c
- ps2netfs_op_devlist() : ps2_fio.c
- ps2netfs_op_dopen() : ps2_fio.c
- ps2netfs_op_dread() : ps2_fio.c
- ps2netfs_op_fstype() : ps2_fio.c
- ps2netfs_op_getstat() : ps2_fio.c
- ps2netfs_op_info() : ps2_fio.c
- ps2netfs_op_ioctl() : ps2_fio.c
- ps2netfs_op_ioctl2() : ps2_fio.c
- ps2netfs_op_lseek() : ps2_fio.c
- ps2netfs_op_lseek64() : ps2_fio.c
- ps2netfs_op_mkdir() : ps2_fio.c
- ps2netfs_op_mount() : ps2_fio.c
- ps2netfs_op_open() : ps2_fio.c
- ps2netfs_op_read() : ps2_fio.c
- ps2netfs_op_readlink() : ps2_fio.c
- ps2netfs_op_remove() : ps2_fio.c
- ps2netfs_op_rename() : ps2_fio.c
- ps2netfs_op_rmdir() : ps2_fio.c
- ps2netfs_op_symlink() : ps2_fio.c
- ps2netfs_op_sync() : ps2_fio.c
- ps2netfs_op_umount() : ps2_fio.c
- ps2netfs_op_write() : ps2_fio.c
- ps2netfs_recv_bytes() : ps2_fio.c
- ps2netfs_serv() : ps2_fio.c

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_q.html>

Here is a list of all documented functions, variables, defines, enums, and typedefs with links to the documentation:
###### - q -
- qd : rpc_server.c
- QueryIntrContext() : intrman.h
- QueryIntrStack() : intrman.h
- queue_sema : audsrv.c
- QWC_MAX : packet.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_r.html>

Here is a list of all documented functions, variables, defines, enums, and typedefs with links to the documentation:
###### - r -
- R_CDVD_DEC_CTRL : iop_regs.h
- R_CDVD_KEY_FLAGS : iop_regs.h
- R_CDVD_KEY_XOR : iop_regs.h
- R_CDVD_N_CMD : iop_regs.h
- R_CDVD_N_CMD_STATUS : iop_regs.h
- R_CDVD_S_CMD : iop_regs.h
- R_CDVD_S_RES_FIFO : iop_regs.h
- R_EE_D0_ASR0 : ee_regs.h
- R_EE_D0_ASR1 : ee_regs.h
- R_EE_D0_CHCR : ee_regs.h
- R_EE_D0_MADR : ee_regs.h
- R_EE_D0_QWC : ee_regs.h
- R_EE_D0_TADR : ee_regs.h
- R_EE_D1_ASR0 : ee_regs.h
- R_EE_D1_ASR1 : ee_regs.h
- R_EE_D1_CHCR : ee_regs.h
- R_EE_D1_MADR : ee_regs.h
- R_EE_D1_QWC : ee_regs.h
- R_EE_D1_TADR : ee_regs.h
- R_EE_D2_ASR0 : ee_regs.h
- R_EE_D2_ASR1 : ee_regs.h
- R_EE_D2_CHCR : ee_regs.h
- R_EE_D2_MADR : ee_regs.h
- R_EE_D2_QWC : ee_regs.h
- R_EE_D2_TADR : ee_regs.h
- R_EE_D3_CHCR : ee_regs.h
- R_EE_D3_MADR : ee_regs.h
- R_EE_D3_QWC : ee_regs.h
- R_EE_D4_CHCR : ee_regs.h
- R_EE_D4_MADR : ee_regs.h
- R_EE_D4_QWC : ee_regs.h
- R_EE_D4_TADR : ee_regs.h
- R_EE_D5_CHCR : ee_regs.h
- R_EE_D5_MADR : ee_regs.h
- R_EE_D5_QWC : ee_regs.h
- R_EE_D6_CHCR : ee_regs.h
- R_EE_D6_MADR : ee_regs.h
- R_EE_D6_QWC : ee_regs.h
- R_EE_D6_TADR : ee_regs.h
- R_EE_D7_CHCR : ee_regs.h
- R_EE_D7_MADR : ee_regs.h
- R_EE_D7_QWC : ee_regs.h
- R_EE_D8_CHCR : ee_regs.h
- R_EE_D8_MADR : ee_regs.h
- R_EE_D8_QWC : ee_regs.h
- R_EE_D8_SADR : ee_regs.h
- R_EE_D9_CHCR : ee_regs.h
- R_EE_D9_MADR : ee_regs.h
- R_EE_D9_QWC : ee_regs.h
- R_EE_D9_SADR : ee_regs.h
- R_EE_D9_TADR : ee_regs.h
- R_EE_D_CTRL : ee_regs.h
- R_EE_D_ENABLER : ee_regs.h
- R_EE_D_ENABLEW : ee_regs.h
- R_EE_D_PCR : ee_regs.h
- R_EE_D_RBOR : ee_regs.h
- R_EE_D_RBSR : ee_regs.h
- R_EE_D_SQWC : ee_regs.h
- R_EE_D_STADR : ee_regs.h
- R_EE_D_STAT : ee_regs.h
- R_EE_GIF_CNT : ee_regs.h
- R_EE_GIF_CTRL : ee_regs.h
- R_EE_GIF_FIFO : ee_regs.h
- R_EE_GIF_MODE : ee_regs.h
- R_EE_GIF_P3CNT : ee_regs.h
- R_EE_GIF_P3TAG : ee_regs.h
- R_EE_GIF_STAT : ee_regs.h
- R_EE_GIF_TAG0 : ee_regs.h
- R_EE_GIF_TAG1 : ee_regs.h
- R_EE_GIF_TAG2 : ee_regs.h
- R_EE_GIF_TAG3 : ee_regs.h
- R_EE_GS_BGCOLOR : ee_regs.h
- R_EE_GS_BUSDIR : ee_regs.h
- R_EE_GS_CSR : ee_regs.h
- R_EE_GS_DISPFB1 : ee_regs.h
- R_EE_GS_DISPFB2 : ee_regs.h
- R_EE_GS_DISPLAY1 : ee_regs.h
- R_EE_GS_DISPLAY2 : ee_regs.h
- R_EE_GS_EXTBUF : ee_regs.h
- R_EE_GS_EXTDATA : ee_regs.h
- R_EE_GS_EXTWRITE : ee_regs.h
- R_EE_GS_IMR : ee_regs.h
- R_EE_GS_PMODE : ee_regs.h
- R_EE_GS_SIGLBLID : ee_regs.h
- R_EE_GS_SMODE1 : ee_regs.h
- R_EE_GS_SMODE2 : ee_regs.h
- R_EE_GS_SRFSH : ee_regs.h
- R_EE_GS_SYNCH1 : ee_regs.h
- R_EE_GS_SYNCH2 : ee_regs.h
- R_EE_GS_SYNCV : ee_regs.h
- R_EE_I_MASK : ee_regs.h
- R_EE_I_STAT : ee_regs.h
- R_EE_IPU_BP : ee_regs.h
- R_EE_IPU_CMD : ee_regs.h
- R_EE_IPU_CTRL : ee_regs.h
- R_EE_IPU_in_FIFO : ee_regs.h
- R_EE_IPU_out_FIFO : ee_regs.h
- R_EE_IPU_TOP : ee_regs.h
- R_EE_PGIF_CFIFO_DATA : ee_regs.h
- R_EE_PGIF_CFIFO_STAT : ee_regs.h
- R_EE_PGIF_GPU_STAT : ee_regs.h
- R_EE_PGIF_REG10 : ee_regs.h
- R_EE_PGIF_REG20 : ee_regs.h
- R_EE_PGIF_REG30 : ee_regs.h
- R_EE_PGIF_REG40 : ee_regs.h
- R_EE_PGIF_REG50 : ee_regs.h
- R_EE_PGIF_REG60 : ee_regs.h
- R_EE_PGIF_REG70 : ee_regs.h
- R_EE_PGIF_REG90 : ee_regs.h
- R_EE_PGIF_REGA0 : ee_regs.h
- R_EE_PGIF_REGB0 : ee_regs.h
- R_EE_PGIF_REGD0 : ee_regs.h
- R_EE_PGIF_REGE0 : ee_regs.h
- R_EE_PGIF_REGF0 : ee_regs.h
- R_EE_SBUS_MADDR : ee_regs.h
- R_EE_SBUS_MSFLAG : ee_regs.h
- R_EE_SBUS_REG40 : ee_regs.h
- R_EE_SBUS_REG50 : ee_regs.h
- R_EE_SBUS_REG60 : ee_regs.h
- R_EE_SBUS_REG70 : ee_regs.h
- R_EE_SBUS_REG80 : ee_regs.h
- R_EE_SBUS_REG90 : ee_regs.h
- R_EE_SBUS_REGA0 : ee_regs.h
- R_EE_SBUS_REGB0 : ee_regs.h
- R_EE_SBUS_REGC0 : ee_regs.h
- R_EE_SBUS_REGD0 : ee_regs.h
- R_EE_SBUS_REGE0 : ee_regs.h
- R_EE_SBUS_REGF0 : ee_regs.h
- R_EE_SBUS_SADDR : ee_regs.h
- R_EE_SBUS_SMFLAG : ee_regs.h
- R_EE_SIO_BRC : ee_regs.h
- R_EE_SIO_FCR : ee_regs.h
- R_EE_SIO_IER : ee_regs.h
- R_EE_SIO_ISR : ee_regs.h
- R_EE_SIO_LCR : ee_regs.h
- R_EE_SIO_LSR : ee_regs.h
- R_EE_SIO_REG60 : ee_regs.h
- R_EE_SIO_REG70 : ee_regs.h
- R_EE_SIO_REG90 : ee_regs.h
- R_EE_SIO_REGA0 : ee_regs.h
- R_EE_SIO_REGB0 : ee_regs.h
- R_EE_SIO_RXFIFO : ee_regs.h
- R_EE_SIO_TXFIFO : ee_regs.h
- R_EE_T0_COMP : ee_regs.h
- R_EE_T0_COUNT : ee_regs.h
- R_EE_T0_HOLD : ee_regs.h
- R_EE_T0_MODE : ee_regs.h
- R_EE_T1_COMP : ee_regs.h
- R_EE_T1_COUNT : ee_regs.h
- R_EE_T1_HOLD : ee_regs.h
- R_EE_T1_MODE : ee_regs.h
- R_EE_T2_COMP : ee_regs.h
- R_EE_T2_COUNT : ee_regs.h
- R_EE_T2_MODE : ee_regs.h
- R_EE_T3_COMP : ee_regs.h
- R_EE_T3_COUNT : ee_regs.h
- R_EE_T3_MODE : ee_regs.h
- R_EE_VIF0_C0 : ee_regs.h
- R_EE_VIF0_C1 : ee_regs.h
- R_EE_VIF0_C2 : ee_regs.h
- R_EE_VIF0_C3 : ee_regs.h
- R_EE_VIF0_CODE : ee_regs.h
- R_EE_VIF0_CYCLE : ee_regs.h
- R_EE_VIF0_ERR : ee_regs.h
- R_EE_VIF0_FBRST : ee_regs.h
- R_EE_VIF0_FIFO : ee_regs.h
- R_EE_VIF0_ITOP : ee_regs.h
- R_EE_VIF0_ITOPS : ee_regs.h
- R_EE_VIF0_MARK : ee_regs.h
- R_EE_VIF0_MASK : ee_regs.h
- R_EE_VIF0_MODE : ee_regs.h
- R_EE_VIF0_NUM : ee_regs.h
- R_EE_VIF0_R0 : ee_regs.h
- R_EE_VIF0_R1 : ee_regs.h
- R_EE_VIF0_R2 : ee_regs.h
- R_EE_VIF0_R3 : ee_regs.h
- R_EE_VIF0_STAT : ee_regs.h
- R_EE_VIF1_BASE : ee_regs.h
- R_EE_VIF1_C0 : ee_regs.h
- R_EE_VIF1_C1 : ee_regs.h
- R_EE_VIF1_C2 : ee_regs.h
- R_EE_VIF1_C3 : ee_regs.h
- R_EE_VIF1_CODE : ee_regs.h
- R_EE_VIF1_CYCLE : ee_regs.h
- R_EE_VIF1_ERR : ee_regs.h
- R_EE_VIF1_FBRST : ee_regs.h
- R_EE_VIF1_FIFO : ee_regs.h
- R_EE_VIF1_ITOP : ee_regs.h
- R_EE_VIF1_ITOPS : ee_regs.h
- R_EE_VIF1_MARK : ee_regs.h
- R_EE_VIF1_MASK : ee_regs.h
- R_EE_VIF1_MODE : ee_regs.h
- R_EE_VIF1_NUM : ee_regs.h
- R_EE_VIF1_OFST : ee_regs.h
- R_EE_VIF1_R0 : ee_regs.h
- R_EE_VIF1_R1 : ee_regs.h
- R_EE_VIF1_R2 : ee_regs.h
- R_EE_VIF1_R3 : ee_regs.h
- R_EE_VIF1_STAT : ee_regs.h
- R_EE_VIF1_TOP : ee_regs.h
- R_EE_VIF1_TOPS : ee_regs.h
- R_IOP_DMAC_1578 : iop_regs.h
- R_IOP_SBUS_REG_BASE : iop_regs.h
- raw_toc : cdrom.c
- RCYC_8 : dma_registers.h
- read_handler : devfs.h
- read_sectors() : cdrom.c
- readpos : audsrv.c
- realfd() : fakehost.c
- RegisterExceptionHandler() : excepman.h
- RegisterIntrHandler() : intrman.h
- RELE_OFF : dma_registers.h
- ReleaseIntrHandler() : intrman.h
- RESET_ARG_MAX : sifcmd-common.h
- ringbuf : audsrv.c
- ringbuf_size : audsrv.c
- RMMan_Close() : librm.h , librm.c
- RMMan_End() : librm.h , librm.c
- RMMan_GetModuleVersion() : librm.h , librm.c
- RMMan_Init() : librm.h , librm.c
- RMMan_Open() : librm.c , librm.h
- RMMan_Read() : librm.c , librm.h
- root_device : devfs.c
- rpc_command() : rpc_server.c
- rpc_server_thread() : rpc_server.c
- RTC_24H : aifregs.h
- RTC_AIE : aifregs.h
- RTC_DIV_RESET1 : aifregs.h
- RTC_DM_BINARY : aifregs.h
- RTC_DST_EN : aifregs.h
- RTC_IRQF : aifregs.h
- RTC_PIE : aifregs.h
- RTC_RATE_SELECT : aifregs.h
- RTC_REF_CLCK_4MHZ : aifregs.h
- RTC_SET : aifregs.h
- RTC_SQWE : aifregs.h
- RTC_UIE : aifregs.h
- RTC_UIP : aifregs.h
- RTC_VRT : aifregs.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_s.html>

Here is a list of all documented functions, variables, defines, enums, and typedefs with links to the documentation:
###### - s -
- SBUS_CTRL_MSCLK : ps2_reg_defs.h
- SBUS_CTRL_MSINT : ps2_reg_defs.h
- SBUS_CTRL_PGPU_INT : ps2_reg_defs.h
- SBUS_CTRL_PS1_RESET : ps2_reg_defs.h
- SBUS_E_ARG : sbusintr.h
- SBUS_E_INIT : sbusintr.h
- SBUS_E_IRQ : sbusintr.h
- sbus_errors : sbusintr.h
- sbv_patch_disable_prefix_check() : sbv_patches.h , patch_disable_prefix_check.c
- sbv_patch_enable_lmb() : sbv_patches.h , patch_enable_lmb.c
- sbv_patch_fileio() : sbv_patches.h
- sbv_patch_romdrv_set_rom1_info() : sbv_patches.h , patch_romdrv_set_rom1_info.c
- sbv_patch_user_mem_clear() : sbv_patches.h , patch_user_mem_clear.c
- SCAN_MASK_NORMAL : draw_masking.h
- SCE_CdSTREAM : libcdvd-common.h
- SCE_EBINDMISS : loadfile.h
- SCE_ECALLMISS : loadfile.h
- SCE_ELOADMISS : loadfile.h
- sceCdApplyNCmd() : libcdvd-common.h
- sceCdApplySCmd() : libcdvd-common.h
- sceCdApplySCmd2() : cdvdman.h
- sceCdApplySCmd3() : cdvdman.h
- sceCdAutoAdjustCtrl() : libcdvd-common.h
- sceCdBlueLEDCtl() : libcdvd-common.h
- sceCdBootCertify() : libcdvd-common.h
- sceCdBreak() : libcdvd-common.h
- sceCdBuzzerCtl() : libcdvd-common.h
- sceCdCallback() : libcdvd-common.h
- sceCdCancelPOffRdy() : libcdvd-common.h
- sceCdCBFunc : libcdvd-common.h
- SCECdCDDA : libcdvd-common.h
- sceCdChangeThreadPriority() : libcdvd-common.h , cdvdfsv.h
- sceCdChgSys() : libcdvd-common.h
- sceCdCloseConfig() : libcdvd-common.h
- SCECdComplete : libcdvd-common.h
- sceCdCtrlADout() : libcdvd-common.h
- sceCdDecSet() : libcdvd-common.h
- sceCdDeobfuscateUsingUniqueKey() : cdvdman.h
- SCECdDETCT : libcdvd-common.h
- sceCdDiskReady() : libcdvd-common.h
- sceCdDoesUniqueKeyExist() : libcdvd-common.h
- SCECdDVDV : libcdvd-common.h
- SCECdDVDVR : libcdvd-common.h
- SCECdErABRT : libcdvd-common.h
- SCECdErCMD : libcdvd-common.h
- SCECdErCUD : libcdvd-common.h
- SCECdErEOM : libcdvd-common.h
- SCECdErFAIL : libcdvd-common.h
- SCECdErILI : libcdvd-common.h
- SCECdErIPI : libcdvd-common.h
- SCECdErNO : libcdvd-common.h
- SCECdErNODISC : libcdvd-common.h
- SCECdErNORDY : libcdvd-common.h
- SCECdErOPENS : libcdvd-common.h
- SCECdErPRM : libcdvd-common.h
- SCECdErREAD : libcdvd-common.h
- SCECdErREADCF : libcdvd-common.h
- SCECdErREADCFR : libcdvd-common.h
- SCECdErTRMOPN : libcdvd-common.h
- SCECdEXIT : libcdvd-common.h
- sceCdForbidDVDP() : libcdvd-common.h
- sceCdForbidRead() : libcdvd-common.h
- sceCdGetDiskType() : libcdvd-common.h
- sceCdGetError() : libcdvd-common.h
- sceCdGetMediumRemoval() : libcdvd-common.h
- sceCdGetReadPos() : libcdvd-common.h
- sceCdGetToc() : libcdvd-common.h
- sceCdGetToc2() : libcdvd-common.h
- sceCdGetWakeUpReason() : libcdvd-common.h
- SCECdIllegalMedia : libcdvd-common.h
- SCECdINIT : libcdvd-common.h
- sceCdInit() : libcdvd-common.h
- sceCdInitEeCB() : libcdvd-common.h
- SCECdINoD : libcdvd-common.h
- sceCdIntToPos() : libcdvd-common.h
- sceCdLayerSearchFile() : libcdvd-common.h
- sceCdMmode() : libcdvd-common.h
- sceCdMV() : libcdvd-common.h
- sceCdNCmdDiskReady() : libcdvd.h
- SCECdNODISC : libcdvd-common.h
- sceCdNoticeGameStart() : libcdvd-common.h
- SCECdNotReady : libcdvd-common.h
- sceCdOpenConfig() : libcdvd-common.h
- sceCdPause() : libcdvd-common.h
- sceCdPOffCallback() : libcdvd-common.h
- sceCdPosToInt() : libcdvd-common.h
- sceCdPowerOff() : libcdvd-common.h
- SCECdPS2CD : libcdvd-common.h
- SCECdPS2CDDA : libcdvd-common.h
- SCECdPS2DVD : libcdvd-common.h
- SCECdPSCD : libcdvd-common.h
- SCECdPSCDDA : libcdvd-common.h
- sceCdRcBypassCtl() : libcdvd-common.h
- sceCdRE() : libcdvd-common.h
- sceCdRead() : libcdvd-common.h
- sceCdReadChain() : libcdvd-common.h
- sceCdReadClock() : libcdvd-common.h
- sceCdReadConfig() : libcdvd-common.h
- sceCdReadConsoleID() : libcdvd-common.h
- sceCdReadDiskID() : cdvdman.h
- sceCdReadDvdDualInfo() : libcdvd-common.h
- sceCdReadFull() : libcdvd-common.h
- sceCdReadGUID() : libcdvd-common.h
- sceCdReadIOPMem() : libcdvd.h
- sceCdReadKey() : libcdvd-common.h
- sceCdReadModelID() : libcdvd-common.h
- sceCdReadNVM() : libcdvd-common.h
- sceCdReadPS1BootParam() : libcdvd-common.h
- sceCdReadRegionParams() : libcdvd-common.h
- sceCdReadSUBQ() : libcdvd-common.h
- sceCdReadWakeUpTime() : libcdvd-common.h
- sceCdRI() : libcdvd-common.h
- sceCdRM() : libcdvd-common.h
- sceCdRV() : cdvdman.h
- sceCdSearchFile() : libcdvd-common.h
- sceCdSeek() : libcdvd-common.h
- sceCdSendSCmd1D() : libcdvd-common.h
- sceCdSetAtapiEjectCallback() : cdvdman.h
- sceCdSetFanProfile() : libcdvd-common.h
- sceCdSetHDMode() : libcdvd-common.h
- sceCdSetLEDsMode() : libcdvd-common.h
- sceCdSetMediumRemoval() : libcdvd-common.h
- sceCdSetTimeout() : libcdvd-common.h
- SCECdSpin1p6 : libcdvd-common.h
- sceCdSpinCtrlEE() : libcdvd.h
- sceCdSpinCtrlIOP() : cdvdman.h
- SCECdSpinDvdDL0 : libcdvd-common.h
- SCECdSpinMax : libcdvd-common.h
- SCECdSpinMx : libcdvd-common.h
- SCECdSpinNm2 : libcdvd-common.h
- SCECdSpinNom : libcdvd-common.h
- SCECdSpinStm : libcdvd-common.h
- SCECdSpinX1 : libcdvd-common.h
- SCECdSpinX12 : libcdvd-common.h
- SCECdSpinX2 : libcdvd-common.h
- SCECdSpinX4 : libcdvd-common.h
- sceCdStandby() : libcdvd-common.h
- SCECdStatEmg : libcdvd-common.h
- SCECdStatPause : libcdvd-common.h
- SCECdStatRead : libcdvd-common.h
- SCECdStatSeek : libcdvd-common.h
- SCECdStatShellOpen : libcdvd-common.h
- SCECdStatSpin : libcdvd-common.h
- SCECdStatStop : libcdvd-common.h
- sceCdStatus() : libcdvd-common.h
- sceCdStatus2() : libcdvd-common.h
- sceCdStInit() : libcdvd-common.h
- sceCdStop() : libcdvd-common.h
- sceCdStPause() : libcdvd-common.h
- sceCdStRead() : libcdvd-common.h
- sceCdStResume() : libcdvd-common.h
- sceCdStSeek() : libcdvd-common.h
- sceCdStSeekF() : libcdvd-common.h
- sceCdStStart() : libcdvd-common.h
- sceCdStStat() : libcdvd-common.h
- sceCdStStop() : libcdvd-common.h
- sceCdSync() : libcdvd-common.h
- SCECdTrayCheck : libcdvd-common.h
- SCECdTrayClose : libcdvd-common.h
- SCECdTrayOpen : libcdvd-common.h
- sceCdTrayReq() : libcdvd-common.h
- SCECdUNKNOWN : libcdvd-common.h
- SCECdvdDriveState : libcdvd-common.h
- SCECdvdErrorCode : libcdvd-common.h
- SCECdvdFanSpeed : libcdvd-common.h
- SCECdvdFanSpeedMaximum : libcdvd-common.h
- SCECdvdFanSpeedMedium : libcdvd-common.h
- SCECdvdFanSpeedMinimum : libcdvd-common.h
- SCECdvdInitMode : libcdvd-common.h
- SCECdvdInterruptCode : libcdvd-common.h
- SCECdvdMediaType : libcdvd-common.h
- SCECdvdSpinValue : libcdvd-common.h
- SCECdvdStreamMode : libcdvd-common.h
- SCECdvdTrayReqMode : libcdvd-common.h
- sceCdWI() : libcdvd-common.h
- sceCdWM() : libcdvd-common.h
- sceCdWriteClock() : libcdvd-common.h
- sceCdWriteConfig() : libcdvd-common.h
- sceCdWriteConsoleID() : libcdvd-common.h
- sceCdWriteNVM() : libcdvd-common.h
- sceCdWriteRegionParams() : libcdvd-common.h
- sceCdWriteWakeUpTime() : libcdvd-common.h
- sceCdXBSPowerCtl() : libcdvd-common.h
- sceCdXDVRPReset() : libcdvd-common.h
- sceCdXLEDCtl() : libcdvd-common.h
- sceRemote2_7() : libcdvd-common.h
- sceRemote2_7Get() : libcdvd-common.h
- sceUsbdLddOps : usbd.h
- sd0 : rpc_server.c
- SecrBitBlockData_t : libsecr-common.h
- SecrBitTable_t : libsecr-common.h
- SecrKELFHeader_t : libsecr-common.h
- set_error() : audsrv_rpc.c
- SetBPC() : hwbp.h
- SetDAB() : hwbp.h
- SetDABM() : hwbp.h
- SetDataAddrBP() : hwbp.h
- SetDataValueBP() : hwbp.h
- SetDVB() : hwbp.h
- SetDVBM() : hwbp.h
- SetIAB() : hwbp.h
- SetIABM() : hwbp.h
- SetInstructionBP() : hwbp.h
- SetNewCtxCb() : intrman.h
- setReg8() : ps2cam.h , ps2cam.c
- setReg8Mask() : ps2cam.h , ps2cam.c
- shiftkeymap : ps2kbd.c
- shutdown() : commandline.c , main.c
- SIF2_E_INIT : siftoo.h
- SIF2_E_OK : siftoo.h
- sif2_errors : siftoo.h
- SIF_CMD_ID_SYSTEM : sifcmd-common.h
- SIF_CMD_M_INTR : sifcmd-common.h
- SIF_CMD_M_WBDC : sifcmd-common.h
- SIF_REG_MAINADDR : sifdma.h , sifman.h
- SIF_REG_MSFLAG : sifdma.h , sifman.h
- SIF_REG_SMFLAG : sifdma.h , sifman.h
- SIF_REG_SUBADDR : sifdma.h , sifman.h
- SIF_RPC_M_NOWAIT : sifrpc-common.h
- SIF_RPC_M_NOWBDC : sifrpc-common.h
- SIF_SREG_RPCINIT : sifcmd-common.h
- SIF_STAT_BOOTEND : sifman.h , sifdma.h
- SIF_STAT_CMDINIT : sifdma.h , sifman.h
- SIF_STAT_SIFINIT : sifman.h , sifdma.h
- SifCmdHeader_t : sifcmd-common.h
- SifCmdSRegData_t : sifcmd-common.h
- SifExecModuleBuffer() : loadfile.h
- SifExecModuleFile() : loadfile.h
- SifIopGetVal() : loadfile.h
- SifIopIsAlive() : iopcontrol.h
- SifIopReboot() : iopcontrol.h
- SifIopRebootBuffer() : iopcontrol_special.h
- SifIopRebootBufferEncrypted() : iopcontrol_special.h
- SifIopReset() : iopcontrol.h
- SifIopSetVal() : loadfile.h
- SifIopSync() : iopcontrol.h
- SifLoadElf() : loadfile.h
- SifLoadElfEncrypted() : loadfile.h
- SifLoadElfPart() : loadfile.h
- SifLoadFileExit() : loadfile.h
- SifLoadFileInit() : loadfile.h
- SifLoadModule() : loadfile.h
- SifLoadModuleBuffer() : loadfile.h
- SifLoadModuleEncrypted() : loadfile.h
- SifLoadStartModule() : loadfile.h
- SifLoadStartModuleBuffer() : loadfile.h
- SINGLE_BYTE : font.h
- SIO_BGR : sio.h
- SIO_CAUSE_BIT : sio.h
- SIO_FCR : sio.h
- SIO_FCR_FRSTE : sio.h
- SIO_FCR_RFRST : sio.h
- SIO_FCR_TFRST : sio.h
- sio_flush() : sio.h , sior.h
- sio_getc_block() : sior.h , sio.h
- sio_gets() : sio.h , sior.h
- SIO_IER : sio.h
- SIO_IER_ELSI : sio.h
- SIO_IER_ERDAI : sio.h
- SIO_ISR : sio.h
- SIO_LCR : sio.h
- SIO_LCR_UEPS_ODD : sio.h
- SIO_LCR_UMODE_8BIT : sio.h
- SIO_LCR_UPEN_OFF : sio.h
- SIO_LCR_USBL_1BIT : sio.h
- SIO_LSR : sio.h
- SIO_LSR_DR : sio.h
- SIO_LSR_FE : sio.h
- SIO_LSR_OE : sio.h
- SIO_LSR_PE : sio.h
- sio_read() : sio.h
- SIO_RXFIFO : sio.h
- SIO_TXFIFO : sio.h
- sio_write() : sio.h
- slib_exp_lib_list() : slib.h , slib.c
- slib_exp_lib_list_t : slib.h
- slib_exp_lib_t : slib.h
- slib_get_exp_lib() : slib.c , slib.h
- slib_get_exportlist_by_name() : slib.c , iopmgr.h
- slib_get_lib_by_name() : iopmgr.h , slib.c
- slib_get_version_by_name() : slib.c , iopmgr.h
- slib_imp_list_t : slib.h
- slib_release_library() : iopmgr.h , slib.c
- SMAP_BD_RX_ALIGNERR : smapregs.h
- SMAP_BD_RX_BADFCS : smapregs.h
- SMAP_BD_RX_BADFRM : smapregs.h
- SMAP_BD_RX_EMPTY : smapregs.h
- SMAP_BD_RX_FRMTOOLONG : smapregs.h
- SMAP_BD_RX_INRANGE : smapregs.h
- SMAP_BD_RX_OUTRANGE : smapregs.h
- SMAP_BD_RX_OVERRUN : smapregs.h
- SMAP_BD_RX_PFRM : smapregs.h
- SMAP_BD_RX_RUNTFRM : smapregs.h
- SMAP_BD_RX_SHORTEVNT : smapregs.h
- smap_bd_t : smapregs.h
- SMAP_BD_TX_BADFCS : smapregs.h
- SMAP_BD_TX_BADPKT : smapregs.h
- SMAP_BD_TX_ECOLL : smapregs.h
- SMAP_BD_TX_EDEFER : smapregs.h
- SMAP_BD_TX_GENFCS : smapregs.h
- SMAP_BD_TX_GENPAD : smapregs.h
- SMAP_BD_TX_INSSA : smapregs.h
- SMAP_BD_TX_INSVLAN : smapregs.h
- SMAP_BD_TX_LCOLL : smapregs.h
- SMAP_BD_TX_LOSSCR : smapregs.h
- SMAP_BD_TX_MCOLL : smapregs.h
- SMAP_BD_TX_READY : smapregs.h
- SMAP_BD_TX_RPLSA : smapregs.h
- SMAP_BD_TX_RPLVLAN : smapregs.h
- SMAP_BD_TX_SCOLL : smapregs.h
- SMAP_BD_TX_SQE : smapregs.h
- SMAP_BD_TX_UNDERRUN : smapregs.h
- SMAP_E3_ALLOW_EXTMNGIF : smapregs.h
- SMAP_E3_ALLOW_PF : smapregs.h
- SMAP_E3_FLOWCTRL_ENABLE : smapregs.h
- SMAP_E3_INLPBK_ENABLE : smapregs.h
- SMAP_E3_INTR_OVERRUN : smapregs.h
- SMAP_E3_PHY_OP_COMP : smapregs.h
- SMAP_E3_RX_PROP_PF : smapregs.h
- SMAP_E3_TX_GNP_0 : smapregs.h
- SMAP_E3_TX_GNP_1 : smapregs.h
- SMAP_E3_TX_GNP_DEPEND : smapregs.h
- SMAP_E3_TX_LOW_REQ_BITSFT : smapregs.h
- SMAP_E3_TX_LOW_REQ_MSK : smapregs.h
- SMAP_E3_TX_URG_REQ_BITSFT : smapregs.h
- SMAP_E3_TX_URG_REQ_MSK : smapregs.h
- SMAP_PHY_10BTSCR_2 : smapregs.h
- SMAP_PHY_10BTSCR_AUTOPOL_DIS : smapregs.h
- SMAP_PHY_10BTSCR_FORCE_10_LINK : smapregs.h
- SMAP_PHY_10BTSCR_FORCE_POL_COR : smapregs.h
- SMAP_PHY_10BTSCR_HEARTBEAT_DIS : smapregs.h
- SMAP_PHY_10BTSCR_JABBER_DIS : smapregs.h
- SMAP_PHY_10BTSCR_LOOPBACK_10_DIS : smapregs.h
- SMAP_PHY_10BTSCR_LP_DIS : smapregs.h
- SMAP_PHY_10BTSCR_POLARITY : smapregs.h
- SMAP_PHY_ANAR_10 : smapregs.h
- SMAP_PHY_ANAR_10_FD : smapregs.h
- SMAP_PHY_ANAR_PAUSE : smapregs.h
- SMAP_PHY_ANAR_RFLT : smapregs.h
- SMAP_PHY_ANAR_T4 : smapregs.h
- SMAP_PHY_ANAR_TX : smapregs.h
- SMAP_PHY_ANAR_TX_FD : smapregs.h
- SMAP_PHY_BMSR_ANCP : smapregs.h
- SMAP_PHY_BMSR_LINK : smapregs.h
- SMAP_PHY_STS_100M : smapregs.h
- SMAP_PHY_STS_10M : smapregs.h
- SMAP_PHY_STS_ANCP : smapregs.h
- SMAP_PHY_STS_DSL : smapregs.h
- SMAP_PHY_STS_DUPS : smapregs.h
- SMAP_PHY_STS_FCSL : smapregs.h
- SMAP_PHY_STS_FDX : smapregs.h
- SMAP_PHY_STS_HDX : smapregs.h
- SMAP_PHY_STS_JBDT : smapregs.h
- SMAP_PHY_STS_LINK : smapregs.h
- SMAP_PHY_STS_LPBK : smapregs.h
- SMAP_PHY_STS_POST : smapregs.h
- SMAP_PHY_STS_PRCV : smapregs.h
- SMAP_PHY_STS_REL : smapregs.h
- SMAP_PHY_STS_RFLT : smapregs.h
- SMAP_PHY_STS_SD : smapregs.h
- SMAP_PHY_STS_SPDS : smapregs.h
- SMapIFInit() : ps2ip.c
- smod_get_mod_by_name() : smod.c , iopmgr.h , smod.h , smod.c
- smod_get_modcount_by_name() : iopmgr.h , smod.c
- smod_get_modversion_by_name() : smod.c , iopmgr.h
- smod_get_next_mod() : smod.c , iopmgr.h , smod.h
- smod_mod_info_t : smod.h
- smod_unload_module() : smod.c , iopmgr.h
- SPD_PP_CSEL : speedregs.h
- SPD_PP_DIN : speedregs.h
- SPD_PP_DOUT : speedregs.h
- SPD_PP_SCLK : speedregs.h
- SSBUSC_DEV : ssbusc.h
- SSBUSC_DEV0 : ssbusc.h
- SSBUSC_DEV_BOOTROM : ssbusc.h
- SSBUSC_DEV_CDVD : ssbusc.h
- SSBUSC_DEV_DVDROM : ssbusc.h
- SSBUSC_DEV_SPU : ssbusc.h
- SSBUSC_DEV_SPU2 : ssbusc.h
- STD_OFF : dma_registers.h
- STMBLK : libcdvd-common.h
- STMNBLK : libcdvd-common.h
- strcpy_ascii() : sjis.h
- strcpy_sjis() : sjis.h
- STS_UNSPEC : dma_registers.h
- SUB_VIRT_MEM : smem.h
- sysmem_internals_t : sysmem.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_t.html>

Here is a list of all documented functions, variables, defines, enums, and typedefs with links to the documentation:
###### - t -
- tcpip_callback_fn : ps2ip.h
- TEXTURE_COMPONENTS_RGB : draw_buffers.h
- TEXTURE_FUNCTION_MODULATE : draw_buffers.h
- TH_SELF : kernel.h , thbase.h
- THS_RUN : kernel.h
- TIME_FORMAT_TYPES : osd_config.h
- toc : cdrom.c
- transfer_complete() : audsrv.c
- transfer_sema : audsrv.c
- TSW_NONE : kernel.h
- TV_SCREEN_TYPES : osd_config.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_type.html>

###### - a -
- ata_hwport_t : atahw.h
- audsrv_adpcm_t : audsrv.h
- audsrv_fmt_t : audsrv.h
###### - d -
- dns_found_callback : tcpip.h
###### - h -
- HDEV : devfs.h
###### - i -
- ioctl_handler : devfs.h
- iomanX_iop_file_t : iomanX.h
- iop_file_t : ioman.h
- iop_io_file_t : ioman_mod.h
- ip4_addr_t : tcpip.h
- ip6_addr_t : tcpip.h
###### - l -
- lc_internals_t : loadcore.h
###### - m -
- ModuleInfo_t : loadcore.h
###### - n -
- netif_init_fn : tcpip.h
- netif_input_fn : tcpip.h
- netif_linkoutput_fn : tcpip.h
- netif_output_fn : tcpip.h
- netif_status_callback_fn : tcpip.h
###### - p -
- poweroff_callback : libpwroff.h
###### - r -
- read_handler : devfs.h
###### - s -
- sceCdCBFunc : libcdvd-common.h
- sceUsbdLddOps : usbd.h
- SecrBitBlockData_t : libsecr-common.h
- SecrBitTable_t : libsecr-common.h
- SecrKELFHeader_t : libsecr-common.h
- SifCmdHeader_t : sifcmd-common.h
- SifCmdSRegData_t : sifcmd-common.h
- slib_exp_lib_list_t : slib.h
- slib_exp_lib_t : slib.h
- slib_imp_list_t : slib.h
- smap_bd_t : smapregs.h
- smod_mod_info_t : smod.h
- sysmem_internals_t : sysmem.h
###### - t -
- tcpip_callback_fn : ps2ip.h
###### - w -
- write_handler : devfs.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_u.html>

Here is a list of all documented functions, variables, defines, enums, and typedefs with links to the documentation:
###### - u -
- up_11025_lut : upsamplers.c
- up_22050_lut : upsamplers.c
- up_32000_lut : upsamplers.c
- up_44100_lut : upsamplers.c
- update_volume() : audsrv.c
- upsamplers : upsamplers.c
- USB_KEYB_NUMLOCK : ps2kbd.c
- USB_RC_ABORTED : usbd.h
- USB_RC_BADCONTEXT : usbd.h
- USB_RC_BADDEV : usbd.h
- USB_RC_BADDRIVER : usbd.h
- USB_RC_BADLENGTH : usbd.h
- USB_RC_BADOPTION : usbd.h
- USB_RC_BADPID : usbd.h
- USB_RC_BADPIPE : usbd.h
- USB_RC_BITSTUFF : usbd.h
- USB_RC_BUFFOVER : usbd.h
- USB_RC_BUFFUNDER : usbd.h
- USB_RC_BUSY : usbd.h
- USB_RC_CRC : usbd.h
- USB_RC_DATAOVER : usbd.h
- USB_RC_DATAUNDER : usbd.h
- USB_RC_ED : usbd.h
- USB_RC_IOREQ : usbd.h
- USB_RC_NORESPONSE : usbd.h
- USB_RC_NOSUPPORT : usbd.h
- USB_RC_NOTACCESSED : usbd.h
- USB_RC_NOTACCESSED2 : usbd.h
- USB_RC_OK : usbd.h
- USB_RC_STALL : usbd.h
- USB_RC_TOGGLE : usbd.h
- USB_RC_UNKNOWN : usbd.h
- USB_RC_WRONGPID : usbd.h
- USBMASS_DEV_STAT_CONF : usbhdfsd-common.h
- USBMASS_DEV_STAT_CONN : usbhdfsd-common.h
- USBMASS_DEV_STAT_ERR : usbhdfsd-common.h
- USBMASS_DEVCTL_STOP_ALL : usbhdfsd-common.h
- USBMASS_DEVCTL_STOP_UNIT : usbhdfsd-common.h
- USBMASS_IOCTL_CHECK_CHAIN : usbhdfsd-common.h
- USBMASS_IOCTL_GET_CLUSTER : usbhdfsd-common.h
- USBMASS_IOCTL_GET_DEVICE_NUMBER : usbhdfsd-common.h
- USBMASS_IOCTL_GET_DRIVERNAME : usbhdfsd-common.h
- USBMASS_IOCTL_GET_FRAGLIST : usbhdfsd-common.h
- USBMASS_IOCTL_GET_LBA : usbhdfsd-common.h
- USBMASS_IOCTL_RENAME : usbhdfsd-common.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_v.html>

Here is a list of all documented functions, variables, defines, enums, and typedefs with links to the documentation:
###### - v -
- vector_add() : math3d.h
- vector_apply() : math3d.h
- vector_clamp() : math3d.h
- vector_copy() : math3d.h
- vector_cross_product() : math3d.h
- vector_innerproduct() : math3d.h
- vector_multiply() : math3d.h
- vector_normalize() : math3d.h
- vector_outerproduct() : math3d.h
- vector_triangle_normal() : math3d.h
- version : fileXio.h
- VIDEO_OUTPUT_TYPES : osd_config.h
- VIF_CMD_BASE : vif_codes.h
- VIF_CMD_DIRECT : vif_codes.h
- VIF_CMD_DIRECTHL : vif_codes.h
- VIF_CMD_FLUSH : vif_codes.h
- VIF_CMD_FLUSHA : vif_codes.h
- VIF_CMD_FLUSHE : vif_codes.h
- VIF_CMD_ITOP : vif_codes.h
- VIF_CMD_MARK : vif_codes.h
- VIF_CMD_MPG : vif_codes.h
- VIF_CMD_MSCAL : vif_codes.h
- VIF_CMD_MSCALF : vif_codes.h
- VIF_CMD_MSCNT : vif_codes.h
- VIF_CMD_MSKPATH3 : vif_codes.h
- VIF_CMD_NOP : vif_codes.h
- VIF_CMD_OFFSET : vif_codes.h
- VIF_CMD_STCOL : vif_codes.h
- VIF_CMD_STCYCL : vif_codes.h
- VIF_CMD_STMASK : vif_codes.h
- VIF_CMD_STMOD : vif_codes.h
- VIF_CMD_STROW : vif_codes.h
- VIF_CMD_UNPACK : vif_codes.h
- VuxUpdateLocalScreenMatrix() : libvux.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_vars.html>

###### - _ -
- __attribute__ : libgs.h
- _exp_audsrv : audsrv.c
- _gp : libcdvd.c
###### - c -
- cd_paused : cdrom.c
- cd_playing : cdrom.c
- cd_transfer_sema : cdrom.c
- cdda_initialized : cdrom.c
- cdda_play_end : cdrom.c
- cdda_play_start : cdrom.c
- cdda_play_tid : cdrom.c
- cdda_pos : cdrom.c
- core1_bits : audsrv.c
- core1_channels : audsrv.c
- core1_freq : audsrv.c
- core1_sample_shift : audsrv.c
- core1_volume : audsrv.c
- count : usbhdfsd-common.h
###### - d -
- dev_info_list : devscan.c
- devices : ps2kbd.c , ps2mouse.c
###### - f -
- fillbuf_threshold : audsrv.c
- format_changed : audsrv.c
###### - i -
- initialized : audsrv.c
- iopbuf : sifcmd.c
###### - k -
- keycap : ps2kbd.c
- keymap : ps2kbd.c
###### - m -
- mouse : ps2mouse.c
###### - n -
- netif_default : tcpip.h
- netif_list : tcpip.h
###### - p -
- pktbuf : sifcmd.c
- play_tid : audsrv.c
- playing : audsrv.c
###### - q -
- qd : rpc_server.c
- queue_sema : audsrv.c
###### - r -
- raw_toc : cdrom.c
- readpos : audsrv.c
- ringbuf : audsrv.c
- ringbuf_size : audsrv.c
- root_device : devfs.c
###### - s -
- sd0 : rpc_server.c
- shiftkeymap : ps2kbd.c
###### - t -
- toc : cdrom.c
- transfer_sema : audsrv.c
###### - u -
- up_11025_lut : upsamplers.c
- up_22050_lut : upsamplers.c
- up_32000_lut : upsamplers.c
- up_44100_lut : upsamplers.c
- upsamplers : upsamplers.c
###### - v -
- version : fileXio.h
###### - w -
- writepos : audsrv.c

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_w.html>

Here is a list of all documented functions, variables, defines, enums, and typedefs with links to the documentation:
###### - w -
- WRAP_REPEAT : draw_sampling.h
- write_handler : devfs.h
- WRITEBACK_DCACHE : kernel.h
- writepos : audsrv.c

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_x.html>

Here is a list of all documented functions, variables, defines, enums, and typedefs with links to the documentation:
###### - x -
- xfromChangeThreadPriority() : libmc.h , libmc.c
- xfromChdir() : libmc.c , libmc.h
- xfromClose() : libmc.h , libmc.c
- xfromDelete() : libmc.c , libmc.h
- xfromEraseBlock() : libmc.h , libmc.c
- xfromFlush() : libmc.h , libmc.c
- xfromFormat() : libmc.h , libmc.c
- xfromGetDir() : libmc.c , libmc.h
- xfromGetEntSpace() : libmc.h , libmc.c
- xfromGetInfo() : libmc.h , libmc.c
- xfromInit() : libmc.h , libmc.c
- xfromMkDir() : libmc.h , libmc.c
- xfromOpen() : libmc.h , libmc.c
- xfromRead() : libmc.h , libmc.c
- xfromReadPage() : libmc.h , libmc.c
- xfromRename() : libmc.c , libmc.h
- xfromReset() : libmc.c , libmc.h
- xfromSeek() : libmc.h , libmc.c
- xfromSetFileInfo() : libmc.c , libmc.h
- xfromSync() : libmc.h , libmc.c
- xfromUnformat() : libmc.h , libmc.c
- xfromWrite() : libmc.h , libmc.c
- xfromWritePage() : libmc.c , libmc.h

---

## PS2SDK: Globals

Page: <https://ps2dev.github.io/ps2sdk/globals_z.html>

Here is a list of all documented functions, variables, defines, enums, and typedefs with links to the documentation:
###### - z -
- ZTEST_METHOD_ALLFAIL : draw_tests.h

---
