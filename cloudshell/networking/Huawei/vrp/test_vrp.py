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
    context.resource.attributes['Password'] = 'XXXXXXX'
    context.resource.attributes['Enable Password'] = 'XXXXXXXX'
    context.resource.address = '172.19.0.37'
    context.resource.attributes['SNMP Version'] = '2'
    context.resource.attributes['SNMP Read Community'] = 'XXXXXXX'
    return context
#Access
request = """{
	"driverRequest" : {
		"actions" : [{
				"connectionId" : "457238ad-4023-49cf-8943-219cb038c0dc",
				"connectionParams" : {
					"vlanId" : "46",
					"mode" : "Trunk",
					"vlanServiceAttributes" : [{
							"attributeName" : "QnQ",
							"attributeValue" : "False",
							"type" : "vlanServiceAttribute"
						}, {
							"attributeName" : "CTag",
							"attributeValue" : "",
							"type" : "vlanServiceAttribute"
						}, {
							"attributeName" : "Isolation Level",
							"attributeValue" : "Shared",
							"type" : "vlanServiceAttribute"
						}, {
							"attributeName" : "Access Mode",
							"attributeValue" : "Access",
							"type" : "vlanServiceAttribute"
						}, {
							"attributeName" : "VLAN ID",
							"attributeValue" : "46",
							"type" : "vlanServiceAttribute"
						}, {
							"attributeName" : "Virtual Network",
							"attributeValue" : "45",
							"type" : "vlanServiceAttribute"
						}, {
							"attributeName" : "Pool Name",
							"attributeValue" : "",
							"type" : "vlanServiceAttribute"
						}
					],
					"type" : "setVlanParameter"
				},
				"connectorAttributes" : [],
				"actionId" : "457238ad-4023-49cf-8943-219cb038c0dc_4244579e-bf6f-4d14-84f9-32d9cacaf9d9",
				"actionTarget" : {
					"fullName" : "Huawei37/Chassis 1/GigabitEthernet0-0-10",
					"fullAddress" : "172.19.0.37/1/0/10",
					"type" : "actionTarget"
				},
				"customActionAttributes" : [],
				"type" : "setVlan"
			}
		]
	}
}"""


if __name__ == '__main__':
    context = create_context()
    driver = HuaweiVRPResourceDriver()

    #response = driver.get_inventory(context)
    #res = driver.save(context, 'tftp://82.80.35.226/test', 'startup')
    #
    #res = driver.save(context, 'flash:/config_backup/','startup')
    #C:/Users/Administrator/Desktop/test
    #tftp://12.30.245.98/test/test.txt
    #res = driver.restore(context,'flash:/config_backup/vrpcfg.zip', 'startup', 'override')

    #response = driver.get_inventory(context)
    #res = driver.save(context, 'tftp://82.80.35.226/test', 'startup')
    res = driver.ApplyConnectivityChanges(context, request)
    #print driver.send_custom_command(context, "display version")
    # print response