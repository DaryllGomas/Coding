def get_wifi_interface():
    wifi = PyWiFi()
    if len(wifi.interfaces()) <= 0:
        print u'Wireless Card Interface Not Found !'
        exit()
        if len(wifi.interfaces()) == 1:
            print u'Wireless car interface: %s'%(wifi.interfaces()[0].name.())
            return wifi.interfaces()[0]
        else:
            print