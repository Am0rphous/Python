from netaddr import IPNetwork, IPAddress
#https://codefather.tech/blog/validate-ip-address-python/

#pip install netaddr
#pip install --upgrade netaddr

if IPAddress("10.0.2.24") in IPNetwork("10.0.2/23"):
    print("IP er i subnet!")
else:
    print("IP er IKKE i subnet..")