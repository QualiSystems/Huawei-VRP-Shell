#!/usr/bin/python
# -*- coding: utf-8 -*-
from cloudshell.shell.core.context import ResourceCommandContext, ResourceContextDetails, ReservationContextDetails
from cloudshell.networking.Huawei.vrp.huawei_vrp_resource_driver import HuaweiVRPResourceDriver
import re


def create_context():
    context = ResourceCommandContext()
    context.resource = ResourceContextDetails()
    context.resource.name = 'Huawei37'
    context.reservation = ReservationContextDetails()
    context.reservation.reservation_id = 'test_id'
    context.resource.attributes = {}
    context.resource.attributes['User'] = 'telnet'
    context.resource.attributes['Password'] = 'Huawei@123'
    context.resource.attributes['Enable Password'] = 'Huawei@123'
    context.resource.address = '172.19.0.37'
    context.resource.attributes['SNMP Version'] = '2'
    context.resource.attributes['SNMP Read Community'] = 'esdkr0key'
    return context

if __name__ == '__main__':
    context = create_context()
    driver = HuaweiVRPResourceDriver()
    #response = driver.get_inventory(context)
    res = driver.save(context, 'tftp://82.80.35.226/test', 'startup')
    #print driver.send_custom_command(context, "display version")
    # print response