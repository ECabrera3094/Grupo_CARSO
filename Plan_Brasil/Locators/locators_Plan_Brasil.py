class Locators_Plan_Brasil:

    str_Country = 'BRASIL'

    str_Acronym_Country = 'BR'

    int_Code_Country = 742

    int_Code_Sub_Country = 3

    str_Date = '2024-12-01'

    int_Date = 20241204

    dict_Tables = {
        'amco-cv-qa.VIS.ACTIVOS30_CENAMPA' : ['PAIS', str_Country, 'ID_FECHA', str_Date],
        'amco-cv-qa.VIS.ACTIVOS30_KPIS' : ['PAIS', str_Country, 'ID_FECHA', str_Date],
        'amco-cv-qa.VIS.ACTIVOS30_USR_ADMIN' : ['PAIS', str_Country, 'ID_FECHA', str_Date],
        'amco-cv-qa.VIS.AGR_FAC_VIS_MES' : ['PAIS', str_Country, 'MES_VIS_PAIS', str_Date],
        'amco-cv-qa.PAG.AGR_REGALIAS_DISP_DEBUTANTES' : ['ID_PAIS_SUB', int_Code_Sub_Country, 'FECHA_VIS_PAIS', str_Date],
        'amco-cv-des.BI.BI_AGR_VIS_ACT_30_MP' : ['PAIS', str_Country, 'FECHA_CIERRE', str_Date],
        'amco-cv-des.BI.BI_AGR_VIS_OVH_MP' : ['PAIS', str_Country, 'FECHA_CIERRE', str_Date],
        'amco-cv-des.BI.BI_AGR_VIS_TRANSACCIONES_MP' : ['PAIS', str_Country, 'FECHA_CIERRE', str_Date],
        'amco-cv-des.BI.BI_CA_DW_CLIENTE' : ['PAIS', str_Country, 'COD_FECHA', str_Date],
        'amco-cv-des.BI.BI_CA_FAC_AG_KPIS_CLARO_VIDEO_MP' : ['PAIS', str_Country, 'FECHA_INSERT', str_Date],
        'amco-cv-des.BI.BI_CA_FAC_CLIENTE_COMPRA_RENTA' : ['PAIS', str_Country, 'FECHA_PAIS', str_Date],
        'amco-cv-des.BI.BI_TA_DW_SUSC_ACTIVAS' : ['PAIS', str_Country, 'ID_FECHA', str_Date],
        'amco-cv-qa.PAG.BQ_REGALIAS' : ['PAIS', str_Country, 'FECHA_VIS_PAIS', int_Date],
        'amco-cv-qa.VIS.CONSUMO_CONTENIDO' : ['ID_PAIS', int_Code_Country, 'FECHA', str_Date],
        'amco-cv-qa.VIS.FAC_CANAL_ALTAS_BAJAS' : ['COD_PAIS', int_Code_Country, 'ID_FECHA', str_Date],
        'amco-cv-qa.TXT.TXT_TRANSACCIONES' : ['PAIS', str_Country, 'FECHA_CORTE', str_Date],
        'amco-cv-qa.LOGIN_REGISTRO.FAC_PRIMER_LOGIN' : ['PAIS', str_Country, 'MES_EVENTO_PAIS', str_Date],
        'amco-cv-qa.VIS.AGR_VIS_R1_DISP_NORMALIZADO' : ['id_pais_sub', int_Code_Country, 'fecha_vis_pais', str_Date],
        'amco-cv-qa.PAG.BQ_REGALIAS' : ['PAIS', str_Country, 'FECHA_VIS_PAIS', int_Date],
        'amco-cv-qa.VIS.TXT_VIS_NORM_JUMP' : ['ds_pais', str_Country, 'fecha_vis_pais', str_Date],
        'amco-cv-con.JUMP.TXT_CATALOGO_CV' : ['PAIS', str_Country, 'FECHA_CORTE', str_Date],
        'amco-cv-qa.TXT.TXT_SUSCRIPCIONES' : ['PAIS', str_Country, 'FECHA_CORTE', str_Date],
        'amco-cv-des.BI.BI_AGR_VIS_PRODUCTO_DISP_NORM_HIST' : ['ID_PAIS_NAT', int_Code_Country, 'ID_FECHA', str_Date],
        'amco-cv-qa.VIS.DIM_GRUPO_EVENTOS_ESPECIALES' : ['ID_PAIS', int_Code_Country, 'FECHA_DESDE', str_Date],
        'amco-cv-qa.VIS.ACTIVOS30_LATAM' : ['COD_PAIS', int_Code_Country, 'FECHA_CORTE', str_Date],
        'amco-cv-qa.VIS.CONSUMO_CONTENIDO' : ['ID_PAIS', int_Code_Country, 'FECHA', str_Date],
        'amco-cv-qa.VIS.TV_EVERYWHERE' : ['PAIS', str_Country,'FECHA_EVENTO', str_Date], 
        'amco-cv-qa.GRAL.GRAL_CA_OPERACIONES_LOGIN_TXT' : ['PAIS', str_Country, 'VENCIMIENTO', str_Date],
        'amco-cv-qa.GRAL.OPERACIONES_BUCKET_ARCHIVOS' : ['PAIS', str_Country, 'VENCIMIENTO', str_Date],
        'amco-cv-des.BI.BI_CA_FAC_LOGIN_REGISTRO_DET_LOOKER' : ['PAIS', str_Country, 'FECHA_EVENTO', str_Date],
        'amco-cv-des.BI.BI_CA_FAC_LOGIN_REGISTRO_LOOKER' : ['PAIS', str_Country, 'ID_FECHA', str_Date],
        'amco-cv-qa.PAG.FAC_SUSCRITOS_ESPECIALES' : ['PAIS', str_Country, 'FECHA', str_Date],
        'amco-cv-qa.PAG.BD_COMPLETA_HUB' : ['PAIS', str_Country, 'FECHA_CREACION', str_Date],
        'amco-cv-qa.PAG.DW_SUSC_ACTIVAS_DIARIAS_DETALLE' : ['PAIS', str_Country, 'ID_FECHA', str_Date],
        'amco-cv-qa.TXT.TXT_CLIENTES' : ['PAIS', str_Country, 'COD_FECHA_BAJA', str_Date],
        'amco-cv-qa.GRAL.DIM_PAIS' : ['DS_PAIS', str_Country, 'FECHA_CARGA', str_Date],
        'amco-cv-des.ENG.ENG_AG_FAC_EMAIL_METRICAS_DIA_KEY' : ['PAIS', str_Country, 'event_time', str_Date],
        'amco-cv-qa.VIS.DIM_PROD_TEC_PAIS' : ['PAIS', str_Country, 'FECHA_ACTUALIZACION', str_Date],
        'amco-cv-qa.CONTROL.FAC_KPIS_MONITOR' : ['PAIS', str_Country, 'FECHA', str_Date],
        'amco-cv-qa.CTE.DW_CLIENTE_FNAL' : ['COD_PAIS', int_Code_Country,'COD_FECHA', str_Date],
        'amco-cv-qa.GRAL.DIM_PAIS_ORACLE' : ['PAIS', str_Country, 'FECHA_ALTA', str_Date],
        'amco-cv-qa.PAG.PINCODES_DETALLE' : ['COUNTRY', str_Country, 'FECHA_INICIO', str_Date],
        'amco-cv-qa.GRAL.GRAL_CA_OPERACIONES_TXT' : ['PAIS', str_Country, 'VENCIMIENTO', str_Date],
        'amco-cv-des.ENG.TA_ENVIOS_ENG' : ['PAIS', str_Acronym_Country, 'fecha_envio', str_Date],
        'amco-cv-des.ENG.ENG_AG_FAC_EMAIL_METRICAS_DIA' : ['PAIS', str_Country, 'event_time', str_Date],
        'amco-cv-qa.VIS.REG_PRIMER_VIS_EVENTOS_ESP' : ['ID_PAIS_SUB', int_Code_Sub_Country, 'ULTIMA_VIS', str_Date],
        'amco-cv-qa.CONTROL.DW_EVENTOS_CV' : ['PAIS', str_Country, 'FECHA_ALTA', str_Date], 
        'amco-cv-qa.VIS.VIS_EVENTOS_ESPECIALES' : ['ID_PAIS_NAT', int_Code_Country, 'ID_FECHA', str_Date],
        'amco-cv-qa.VIS.FAC_CANAL_ALTAS_BAJAS' : ['COD_PAIS', int_Code_Country, 'ID_FECHA', str_Date],
        'amco-cv-qa.CONTROL.ABONOS_PRODUCTID' : ['PAIS', str_Country, 'FECHA_CORTE', str_Date],
        'amco-cv-qa.CONTROL.DW_CAMBIO_TARIFA' : ['TX_PAIS', str_Country, 'COD_FECHA', str_Date],
        'amco-cv-qa.PAG.PINCODES_TOTALES_MV' : ['COUNTRY', str_Country, 'FECHA_INICIO', str_Date],
        'amco-cv-qa.PAG.DW_SUSC_ACTIVAS_DIARIAS' : ['PAIS', str_Country, 'ID_FECHA', str_Date],
        'amco-cv-des.BI.BI_TA_DW_SUSC_ACTIVAS' : ['PAIS', str_Country, 'ID_FECHA', str_Date],
        'amco-cv-des.BI.BI_CA_FAC_ALTAS_BAJAS_SUSC' : ['PAIS', str_Country, 'ID_FECHA', str_Date],
        'amco-cv-des.BI.BI_CA_DIM_PAIS' : ['PAIS', str_Country, 'FECHA_ALTA', str_Date],
        'amco-cv-qa.VIS.EVENTOS_ESPECIALES_AGR' : ['DS_PAIS', str_Country, 'FECHA_CORTE', str_Date],
        'amco-cv-qa.CTE.DW_CLIENTE_RESUMEN' : ['COD_PAIS', int_Code_Country, 'COD_FECHA_DIARIO', str_Date], 
        'amco-cv-qa.TXT.TXT_CATALOGO_CV' : ['PAIS', str_Country, 'FECHA_CORTE', str_Date],
        'amco-cv-con.JUMP.TXT_CATALOGO_CV' : ['PAIS', str_Country, 'FECHA_CORTE', str_Date],
        'amco-cv-des.BI.BI_AGR_VIS_TRANSACCIONES_MP' : ['PAIS', str_Country, 'FECHA_CIERRE', str_Date],
        'amco-cv-qa.PAG.DW_SUSC_ACTIVAS_DIARIAS_DET' : ['PAIS', str_Country, 'ID_FECHA', str_Date]
    }