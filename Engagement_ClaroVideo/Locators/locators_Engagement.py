class Locators_Engagement:

    def transform_Keys(keys):
        new_keys = ",\n".join(keys) # Solo se agrega el Salto de Línea ENTRE los Elementos.
        return new_keys

    URL = "https://engagement-east.clarovideo.net/v1/queue/paneles/mail-test?authpn=M41L3R&authpt=L03LL7"

    email = "pruebasl735@gmail.com"

    region = "PY"

    keys_ClaroVideo = ['cv-welcome', 'cv-passwordreminder', 'cv-change-password-success', 'cv-activatecontrolpin', 'cv-remembercontrolpin', 'cv-newlogin-notification']
    #keys_ClaroVideo = ['email_cancel_universal_plus_paraguay_amcogate','email_cancel_universal_plus_paraguay_hubfacturafijagate','email_cancel_universal_plus_paraguay_hubgate']
    keys_ClaroVideo = transform_Keys(keys_ClaroVideo)

    keys_ClaroMusic = ["cm-welcome-jwt"]
    keys_ClaroMusic = transform_Keys(keys_ClaroMusic)

    Keys_ClaroDrive = ["cb_welcome", "cd-recovery-password"]
    Keys_ClaroDrive = transform_Keys(Keys_ClaroDrive)

    keys_ClaroConnect = ["cc-emails-remember", "cc-emails-invite", "cc-emails-forgotpw", "cc-emails-cancel"]
    keys_ClaroConnect = transform_Keys(keys_ClaroConnect)

    variables = {"NAME":"Prueba",
                "PRECIO":"440",
                "DATE":"13/12/2024",
                "PROMO_DESC":"Suscripción Universal Plus"
                }