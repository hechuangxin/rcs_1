# _*_ coding : UTF-8 _*_
# 开发团队 : 火星团队
# 开发人员 : hcx
# 开发时间 : 2020/10/10 15:12
# 文件名称 : 
# 开发工具 : PyCharm
#盘点单
import xmltodict
import json
list2 = []
for i in range(1,3):
    id = str(i) + "${uuid}"
    skuCode = "${sku_code1_" + str(i) + "}"
    packCode = "${sku_code1_" + str(i) + "}-${sku_code1_" + str(i) + "}"
    json1 = {
				"ownerCode": "${ownerCode}",
				"skuCode": "{}".format(skuCode),
				"lotAtt01": "1",
				"lotAtt02": "",
				"lotAtt03": "",
				"lotAtt04": "",
				"lotAtt05": "",
				"lotAtt06": "",
				"lotAtt07": "",
				"lotAtt08": "",
				"lotAtt09": "",
				"lotAtt10": "",
				"lotAtt11": "",
				"lotAtt12": ""
			}

    list2.append(json1)
print(json1)
print(list2)
a={
 "root": {
  "header": {
   "appid": "FH001",
   "appkey": "vip@FH001",
   "request_id": "5a9281c9-0773-4cbf-a777-c4bff0b2e02d",
   "warehouse": "VIP_NH",
   "version": "1.0"
  },
  "body": {
   "item": [
    {
     "id": "{}1",
     "warehouse_code": "VIP_NH",
     "source_code": "VIPS",
     "destination_code": "FH",
     "action_type": "NEW",
     "work_no": "test{}-1",
     "work_type": "FLOWPICK_MS",
     "action_time": "{}",
     "remark": "1211",
     "line_count": "1",
     "container_count": "0",
     "inf_function": "1",
     "priority": "0",
     "details": {
      "item": {
       "id": "1{}",
       "container_code": "null",
       "item_code": "{}",
       "item_desc": "{}",
       "brand_name": "brand001{}",
       "item_cat1_code": "cat1code01{}",
       "item_cat1_name": "cat101{}",
       "item_cat2_code": "cat2code01{}",
       "item_cat2_name": "cat201{}",
       "item_cat3_code": "cat3code01{}",
       "item_cat3_name": "cat301{}",
       "unit_item": "EACH",
       "item_size": "A",
       "item_color": "\u7ea2\u8272",
       "item_spec_class": "VAL,FRG",
       "gross_weight": "5.000",
       "net_weight": "5.000",
       "weight_um": "g",
       "volume": "6000.000",
       "volume_um": "cm3",
       "img": "123",
       "qty": "1",
       "warehouse_code": "VIP_NH",
       "company_code": "VIPS",
       "quality": "{}",
       "mfg_date": "{}",
       "exp_date": "{}",
       "inv_type": "{}",
       "vendor_code": "{}",
       "po_no": "{}"
      }
     }
    },
    {
     "id": "{}2",
     "warehouse_code": "VIP_NH",
     "source_code": "VIPS",
     "destination_code": "FH",
     "action_type": "NEW",
     "work_no": "test{}-2",
     "work_type": "FLOWPICK_MS",
     "action_time": "{}",
     "remark": "1211",
     "line_count": "1",
     "container_count": "0",
     "inf_function": "1",
     "priority": "0",
     "details": {
      "item": {
       "id": "2{}",
       "container_code": "null",
       "item_code": "{}",
       "item_desc": "{}",
       "brand_name": "brand{}",
       "item_cat1_code": "cat1code02{}",
       "item_cat1_name": "cat102{}",
       "item_cat2_code": "cat2code02{}",
       "item_cat2_name": "cat202{}",
       "item_cat3_code": "cat3code02{}",
       "item_cat3_name": "cat302{}",
       "unit_item": "EACH",
       "item_size": "A",
       "item_color": "\u7ea2\u8272",
       "item_spec_class": "VAL,FRG",
       "gross_weight": "5.000",
       "net_weight": "5.000",
       "weight_um": "g",
       "volume": "6000.000",
       "volume_um": "cm3",
       "img": "123",
       "qty": "1",
       "warehouse_code": "VIP_NH",
       "company_code": "VIPS",
       "quality": "{}",
       "mfg_date": "{}",
       "exp_date": "{}",
       "inv_type": "{}",
       "vendor_code": "{}",
       "po_no": "{}"
      }
     }
    },
    {
     "id": "{}3",
     "warehouse_code": "VIP_NH",
     "source_code": "VIPS",
     "destination_code": "FH",
     "action_type": "NEW",
     "work_no": "test{}-3",
     "work_type": "FLOWPICK_MS",
     "action_time": "{}",
     "remark": "1211",
     "line_count": "1",
     "container_count": "0",
     "inf_function": "1",
     "priority": "0",
     "details": {
      "item": {
       "id": "33{}",
       "container_code": "null",
       "item_code": "{}",
       "item_desc": "{}",
       "brand_name": "brand03{}",
       "item_cat1_code": "cat1code03{}",
       "item_cat1_name": "cat103{}",
       "item_cat2_code": "cat2code03{}",
       "item_cat2_name": "cat203{}",
       "item_cat3_code": "cat3code03{}",
       "item_cat3_name": "cat303{}",
       "unit_item": "EACH",
       "item_size": "A",
       "item_color": "\u7ea2\u8272",
       "item_spec_class": "VAL,FRG",
       "gross_weight": "5.000",
       "net_weight": "5.000",
       "weight_um": "g",
       "volume": "6000.000",
       "volume_um": "cm3",
       "img": "123",
       "qty": "1",
       "warehouse_code": "VIP_NH",
       "company_code": "VIPS",
       "quality": "{}",
       "mfg_date": "{}",
       "exp_date": "{}",
       "inv_type": "{}",
       "vendor_code": "{}",
       "po_no": "{}"
      }
     }
    },
    {
     "id": "{}4",
     "warehouse_code": "VIP_NH",
     "source_code": "VIPS",
     "destination_code": "FH",
     "action_type": "NEW",
     "work_no": "test{}-4",
     "work_type": "FLOWPICK_MS",
     "action_time": "{}",
     "remark": "1211",
     "line_count": "1",
     "container_count": "0",
     "inf_function": "1",
     "priority": "0",
     "details": {
      "item": {
       "id": "4{}",
       "container_code": "null",
       "item_code": "{}",
       "item_desc": "{}",
       "brand_name": "brand04{}",
       "item_cat1_code": "cat1code04{}",
       "item_cat1_name": "cat104{}",
       "item_cat2_code": "cat2code04{}",
       "item_cat2_name": "cat204{}",
       "item_cat3_code": "cat3code04{}",
       "item_cat3_name": "cat304{}",
       "unit_item": "EACH",
       "item_size": "A",
       "item_color": "\u7ea2\u8272",
       "item_spec_class": "VAL,FRG",
       "gross_weight": "5.000",
       "net_weight": "5.000",
       "weight_um": "g",
       "volume": "6000.000",
       "volume_um": "cm3",
       "img": "123",
       "qty": "1",
       "warehouse_code": "VIP_NH",
       "company_code": "VIPS",
       "quality": "{}",
       "mfg_date": "{}",
       "exp_date": "{}",
       "inv_type": "{}",
       "vendor_code": "{}",
       "po_no": "{}"
      }
     }
    },
    {
     "id": "{}5",
     "warehouse_code": "VIP_NH",
     "source_code": "VIPS",
     "destination_code": "FH",
     "action_type": "NEW",
     "work_no": "test{}-5",
     "work_type": "FLOWPICK_MS",
     "action_time": "{}",
     "remark": "1211",
     "line_count": "1",
     "container_count": "0",
     "inf_function": "1",
     "priority": "0",
     "details": {
      "item": {
       "id": "5{}",
       "container_code": "null",
       "item_code": "{}",
       "item_desc": "{}",
       "brand_name": "brand05{}",
       "item_cat1_code": "cat1code05{}",
       "item_cat1_name": "cat105{}",
       "item_cat2_code": "cat2code05{}",
       "item_cat2_name": "cat205{}",
       "item_cat3_code": "cat3code05{}",
       "item_cat3_name": "cat305{}",
       "unit_item": "EACH",
       "item_size": "A",
       "item_color": "\u7ea2\u8272",
       "item_spec_class": "VAL,FRG",
       "gross_weight": "5.000",
       "net_weight": "5.000",
       "weight_um": "g",
       "volume": "6000.000",
       "volume_um": "cm3",
       "img": "123",
       "qty": "1",
       "warehouse_code": "VIP_NH",
       "company_code": "VIPS",
       "quality": "{}",
       "mfg_date": "{}",
       "exp_date": "{}",
       "inv_type": "{}",
       "vendor_code": "{}",
       "po_no": "{}"
      }
     }
    },
    {
     "id": "{}6",
     "warehouse_code": "VIP_NH",
     "source_code": "VIPS",
     "destination_code": "FH",
     "action_type": "NEW",
     "work_no": "test{}-6",
     "work_type": "FLOWPICK_MS",
     "action_time": "{}",
     "remark": "1211",
     "line_count": "1",
     "container_count": "0",
     "inf_function": "1",
     "priority": "0",
     "details": {
      "item": {
       "id": "6{}",
       "container_code": "null",
       "item_code": "{}",
       "item_desc": "{}",
       "brand_name": "brand06{}",
       "item_cat1_code": "cat1code06{}",
       "item_cat1_name": "cat106{}",
       "item_cat2_code": "cat2code06{}",
       "item_cat2_name": "cat206{}",
       "item_cat3_code": "cat3code06{}",
       "item_cat3_name": "cat306{}",
       "unit_item": "EACH",
       "item_size": "A",
       "item_color": "\u7ea2\u8272",
       "item_spec_class": "VAL,FRG",
       "gross_weight": "5.000",
       "net_weight": "5.000",
       "weight_um": "g",
       "volume": "6000.000",
       "volume_um": "cm3",
       "img": "123",
       "qty": "1",
       "warehouse_code": "VIP_NH",
       "company_code": "VIPS",
       "quality": "{}",
       "mfg_date": "{}",
       "exp_date": "{}",
       "inv_type": "{}",
       "vendor_code": "{}",
       "po_no": "{}"
      }
     }
    },
    {
     "id": "{}7",
     "warehouse_code": "VIP_NH",
     "source_code": "VIPS",
     "destination_code": "FH",
     "action_type": "NEW",
     "work_no": "test{}-7",
     "work_type": "FLOWPICK_MS",
     "action_time": "{}",
     "remark": "1211",
     "line_count": "1",
     "container_count": "0",
     "inf_function": "1",
     "priority": "0",
     "details": {
      "item": {
       "id": "7{}",
       "container_code": "null",
       "item_code": "{}",
       "item_desc": "{}",
       "brand_name": "brand07{}",
       "item_cat1_code": "cat1code07{}",
       "item_cat1_name": "cat107{}",
       "item_cat2_code": "cat2code07{}",
       "item_cat2_name": "cat207{}",
       "item_cat3_code": "cat3code07{}",
       "item_cat3_name": "cat307{}",
       "unit_item": "EACH",
       "item_size": "A",
       "item_color": "\u7ea2\u8272",
       "item_spec_class": "VAL,FRG",
       "gross_weight": "5.000",
       "net_weight": "5.000",
       "weight_um": "g",
       "volume": "6000.000",
       "volume_um": "cm3",
       "img": "123",
       "qty": "1",
       "warehouse_code": "VIP_NH",
       "company_code": "VIPS",
       "quality": "{}",
       "mfg_date": "{}",
       "exp_date": "{}",
       "inv_type": "{}",
       "vendor_code": "{}",
       "po_no": "{}"
      }
     }
    },
    {
     "id": "{}8",
     "warehouse_code": "VIP_NH",
     "source_code": "VIPS",
     "destination_code": "FH",
     "action_type": "NEW",
     "work_no": "test{}-8",
     "work_type": "FLOWPICK_MS",
     "action_time": "{}",
     "remark": "1211",
     "line_count": "1",
     "container_count": "0",
     "inf_function": "1",
     "priority": "0",
     "details": {
      "item": {
       "id": "8{}",
       "container_code": "null",
       "item_code": "{}",
       "item_desc": "{}",
       "brand_name": "brand08{}",
       "item_cat1_code": "cat1code08{}",
       "item_cat1_name": "cat108{}",
       "item_cat2_code": "cat2code08{}",
       "item_cat2_name": "cat208{}",
       "item_cat3_code": "cat3code08{}",
       "item_cat3_name": "cat308{}",
       "unit_item": "EACH",
       "item_size": "A",
       "item_color": "\u7ea2\u8272",
       "item_spec_class": "VAL,FRG",
       "gross_weight": "5.000",
       "net_weight": "5.000",
       "weight_um": "g",
       "volume": "6000.000",
       "volume_um": "cm3",
       "img": "123",
       "qty": "1",
       "warehouse_code": "VIP_NH",
       "company_code": "VIPS",
       "quality": "{}",
       "mfg_date": "{}",
       "exp_date": "{}",
       "inv_type": "{}",
       "vendor_code": "{}",
       "po_no": "{}"
      }
     }
    },
    {
     "id": "{}9",
     "warehouse_code": "VIP_NH",
     "source_code": "VIPS",
     "destination_code": "FH",
     "action_type": "NEW",
     "work_no": "test{}-9",
     "work_type": "FLOWPICK_MS",
     "action_time": "{}",
     "remark": "1211",
     "line_count": "1",
     "container_count": "0",
     "inf_function": "1",
     "priority": "0",
     "details": {
      "item": {
       "id": "9{}",
       "container_code": "null",
       "item_code": "{}",
       "item_desc": "{}",
       "brand_name": "brand09{}",
       "item_cat1_code": "cat1code09{}",
       "item_cat1_name": "cat109{}",
       "item_cat2_code": "cat2code09{}",
       "item_cat2_name": "cat209{}",
       "item_cat3_code": "cat3code09{}",
       "item_cat3_name": "cat309{}",
       "unit_item": "EACH",
       "item_size": "A",
       "item_color": "\u7ea2\u8272",
       "item_spec_class": "VAL,FRG",
       "gross_weight": "5.000",
       "net_weight": "5.000",
       "weight_um": "g",
       "volume": "6000.000",
       "volume_um": "cm3",
       "img": "123",
       "qty": "1",
       "warehouse_code": "VIP_NH",
       "company_code": "VIPS",
       "quality": "{}",
       "mfg_date": "{}",
       "exp_date": "{}",
       "inv_type": "{}",
       "vendor_code": "{}",
       "po_no": "{}"
      }
     }
    },
    {
     "id": "{}10",
     "warehouse_code": "VIP_NH",
     "source_code": "VIPS",
     "destination_code": "FH",
     "action_type": "NEW",
     "work_no": "test{}-10",
     "work_type": "FLOWPICK_MS",
     "action_time": "{}",
     "remark": "1211",
     "line_count": "1",
     "container_count": "0",
     "inf_function": "1",
     "priority": "0",
     "details": {
      "item": {
       "id": "100{}",
       "container_code": "null",
       "item_code": "{}",
       "item_desc": "{}",
       "brand_name": "brand10{}",
       "item_cat1_code": "cat1code10{}",
       "item_cat1_name": "cat110{}",
       "item_cat2_code": "cat2code10{}",
       "item_cat2_name": "cat210{}",
       "item_cat3_code": "cat3code10{}",
       "item_cat3_name": "cat310{}",
       "unit_item": "EACH",
       "item_size": "A",
       "item_color": "\u7ea2\u8272",
       "item_spec_class": "VAL,FRG",
       "gross_weight": "5.000",
       "net_weight": "5.000",
       "weight_um": "g",
       "volume": "6000.000",
       "volume_um": "cm3",
       "img": "123",
       "qty": "1",
       "warehouse_code": "VIP_NH",
       "company_code": "VIPS",
       "quality": "{}",
       "mfg_date": "{}",
       "exp_date": "{}",
       "inv_type": "{}",
       "vendor_code": "{}",
       "po_no": "{}"
      }
     }
    }
   ]
  }
 }
}

# json转xml函数
def json_to_xml(json_str):
    # xmltodict库的unparse()json转xml
    # 参数pretty 是格式化xml
    xml_str = xmltodict.unparse(json_str, pretty=1)
    return xml_str
print(json_to_xml(a))


b='<?xml version="1.0" encoding="UTF-8"?>\
<root>\
    <header>\
        <appid>FH001</appid>\
        <appkey>vip@FH001</appkey>\
        <request_id>5a9281c9-0773-4cbf-a777-c4bff0b2e02d</request_id>\
        <warehouse>VIP_NH</warehouse>\
        <version>1.0</version>\
    </header>\
    <body>\
        <item>\
            <id>{}1</id>\
            <warehouse_code>VIP_NH</warehouse_code>\
            <source_code>VIPS</source_code>\
            <destination_code>FH</destination_code>\
            <action_type>NEW</action_type>\
            <work_no>test{}-1</work_no>\
            <work_type>FLOWPICK_MS</work_type>\
            <action_time>{}</action_time>\
            <remark>1211</remark>\
            <line_count>1</line_count>\
            <container_count>0</container_count>\
            <inf_function>1</inf_function>\
            <priority>0</priority>\
            <details>\
                <item>\
                    <id>1{}</id>\
                    <container_code/>\
                    <item_code>{}</item_code>\
                    <item_desc>{}</item_desc>\
                    <brand_name>brand001{}</brand_name>\
                    <item_cat1_code>cat1code01{}</item_cat1_code>\
                    <item_cat1_name>cat101{}</item_cat1_name>\
                    <item_cat2_code>cat2code01{}</item_cat2_code>\
                    <item_cat2_name>cat201{}</item_cat2_name>\
                    <item_cat3_code>cat3code01{}</item_cat3_code>\
                    <item_cat3_name>cat301{}</item_cat3_name>\
                    <unit_item>EACH</unit_item>\
                    <item_size><![CDATA[A]]></item_size>\
                    <item_color><![CDATA[红色]]></item_color>\
                    <item_spec_class>VAL,FRG</item_spec_class>\
                    <gross_weight>5.000</gross_weight>\
                    <net_weight>5.000</net_weight>\
                    <weight_um>g</weight_um>\
                    <volume>6000.000</volume>\
                    <volume_um>cm3</volume_um>\
                    <img>123</img>\
                    <qty>1</qty>\
                    <warehouse_code>VIP_NH</warehouse_code>\
                    <company_code>VIPS</company_code>\
                    <quality>{}</quality>\
                    <mfg_date>{}</mfg_date>\
                    <exp_date>{}</exp_date>\
                    <inv_type>{}</inv_type>\
                    <vendor_code>{}</vendor_code>\
                    <po_no>{}</po_no>\
                </item>\
    </details>\
    </item>\
    <item>\
        <id>{}2</id>\
        <warehouse_code>VIP_NH</warehouse_code>\
        <source_code>VIPS</source_code>\
        <destination_code>FH</destination_code>\
        <action_type>NEW</action_type>\
        <work_no>test{}-2</work_no>\
        <work_type>FLOWPICK_MS</work_type>\
        <action_time>{}</action_time>\
        <remark>1211</remark>\
        <line_count>1</line_count>\
        <container_count>0</container_count>\
        <inf_function>1</inf_function>\
        <priority>0</priority>\
        <details>\
                <item>\
                            <id>2{}</id>\
                            <container_code/>\
                            <item_code>{}</item_code>\
                            <item_desc>{}</item_desc>\
                            <brand_name>brand{}</brand_name>\
                            <item_cat1_code>cat1code02{}</item_cat1_code>\
                            <item_cat1_name>cat102{}</item_cat1_name>\
                            <item_cat2_code>cat2code02{}</item_cat2_code>\
                            <item_cat2_name>cat202{}</item_cat2_name>\
                            <item_cat3_code>cat3code02{}</item_cat3_code>\
                            <item_cat3_name>cat302{}</item_cat3_name>\
                            <unit_item>EACH</unit_item>\
                            <item_size><![CDATA[A]]></item_size>\
                            <item_color><![CDATA[红色]]></item_color>\
                            <item_spec_class>VAL,FRG</item_spec_class>\
                            <gross_weight>5.000</gross_weight>\
                            <net_weight>5.000</net_weight>\
                            <weight_um>g</weight_um>\
                            <volume>6000.000</volume>\
                            <volume_um>cm3</volume_um>\
                            <img>123</img>\
                            <qty>1</qty>\
                            <warehouse_code>VIP_NH</warehouse_code>\
                            <company_code>VIPS</company_code>\
                            <quality>{}</quality>\
                            <mfg_date>{}</mfg_date>\
                            <exp_date>{}</exp_date>\
                            <inv_type>{}</inv_type>\
                            <vendor_code>{}</vendor_code>\
                            <po_no>{}</po_no>\
            </item>\
    </details>\
    </item>\
    <item>\
        <id>{}3</id>\
        <warehouse_code>VIP_NH</warehouse_code>\
        <source_code>VIPS</source_code>\
        <destination_code>FH</destination_code>\
        <action_type>NEW</action_type>\
        <work_no>test{}-3</work_no>\
        <work_type>FLOWPICK_MS</work_type>\
        <action_time>{}</action_time>\
        <remark>1211</remark>\
        <line_count>1</line_count>\
        <container_count>0</container_count>\
        <inf_function>1</inf_function>\
        <priority>0</priority>\
        <details>\
            <item>\
                    <id>33{}</id>\
                    <container_code/>\
                    <item_code>{}</item_code>\
                    <item_desc>{}</item_desc>\
                    <brand_name>brand03{}</brand_name>\
                    <item_cat1_code>cat1code03{}</item_cat1_code>\
                    <item_cat1_name>cat103{}</item_cat1_name>\
                    <item_cat2_code>cat2code03{}</item_cat2_code>\
                    <item_cat2_name>cat203{}</item_cat2_name>\
                    <item_cat3_code>cat3code03{}</item_cat3_code>\
                    <item_cat3_name>cat303{}</item_cat3_name>\
                    <unit_item>EACH</unit_item>\
                    <item_size><![CDATA[A]]></item_size>\
                    <item_color><![CDATA[红色]]></item_color>\
                    <item_spec_class>VAL,FRG</item_spec_class>\
                    <gross_weight>5.000</gross_weight>\
                    <net_weight>5.000</net_weight>\
                    <weight_um>g</weight_um>\
                    <volume>6000.000</volume>\
                    <volume_um>cm3</volume_um>\
                    <img>123</img>\
                    <qty>1</qty>\
                    <warehouse_code>VIP_NH</warehouse_code>\
                    <company_code>VIPS</company_code>\
                    <quality>{}</quality>\
                    <mfg_date>{}</mfg_date>\
                    <exp_date>{}</exp_date>\
                    <inv_type>{}</inv_type>\
                    <vendor_code>{}</vendor_code>\
                    <po_no>{}</po_no>\
            </item>\
    </details>\
    </item>\
    <item>\
        <id>{}4</id>\
        <warehouse_code>VIP_NH</warehouse_code>\
        <source_code>VIPS</source_code>\
        <destination_code>FH</destination_code>\
        <action_type>NEW</action_type>\
        <work_no>test{}-4</work_no>\
        <work_type>FLOWPICK_MS</work_type>\
        <action_time>{}</action_time>\
        <remark>1211</remark>\
        <line_count>1</line_count>\
        <container_count>0</container_count>\
        <inf_function>1</inf_function>\
        <priority>0</priority>\
        <details>\
            <item>\
                        <id>4{}</id>\
                        <container_code/>\
                        <item_code>{}</item_code>\
                        <item_desc>{}</item_desc>\
                        <brand_name>brand04{}</brand_name>\
                        <item_cat1_code>cat1code04{}</item_cat1_code>\
                        <item_cat1_name>cat104{}</item_cat1_name>\
                        <item_cat2_code>cat2code04{}</item_cat2_code>\
                        <item_cat2_name>cat204{}</item_cat2_name>\
                        <item_cat3_code>cat3code04{}</item_cat3_code>\
                        <item_cat3_name>cat304{}</item_cat3_name>\
                        <unit_item>EACH</unit_item>\
                        <item_size><![CDATA[A]]></item_size>\
                        <item_color><![CDATA[红色]]></item_color>\
                        <item_spec_class>VAL,FRG</item_spec_class>\
                        <gross_weight>5.000</gross_weight>\
                        <net_weight>5.000</net_weight>\
                        <weight_um>g</weight_um>\
                        <volume>6000.000</volume>\
                        <volume_um>cm3</volume_um>\
                        <img>123</img>\
                        <qty>1</qty>\
                        <warehouse_code>VIP_NH</warehouse_code>\
                        <company_code>VIPS</company_code>\
                        <quality>{}</quality>\
                        <mfg_date>{}</mfg_date>\
                        <exp_date>{}</exp_date>\
                        <inv_type>{}</inv_type>\
                        <vendor_code>{}</vendor_code>\
                        <po_no>{}</po_no>\
                </item>\
    </details>\
    </item>\
    <item>\
        <id>{}5</id>\
        <warehouse_code>VIP_NH</warehouse_code>\
        <source_code>VIPS</source_code>\
        <destination_code>FH</destination_code>\
        <action_type>NEW</action_type>\
        <work_no>test{}-5</work_no>\
        <work_type>FLOWPICK_MS</work_type>\
        <action_time>{}</action_time>\
        <remark>1211</remark>\
        <line_count>1</line_count>\
        <container_count>0</container_count>\
        <inf_function>1</inf_function>\
        <priority>0</priority>\
        <details>\
                <item>\
                        <id>5{}</id>\
                        <container_code/>\
                        <item_code>{}</item_code>\
                        <item_desc>{}</item_desc>\
                        <brand_name>brand05{}</brand_name>\
                        <item_cat1_code>cat1code05{}</item_cat1_code>\
                        <item_cat1_name>cat105{}</item_cat1_name>\
                        <item_cat2_code>cat2code05{}</item_cat2_code>\
                        <item_cat2_name>cat205{}</item_cat2_name>\
                        <item_cat3_code>cat3code05{}</item_cat3_code>\
                        <item_cat3_name>cat305{}</item_cat3_name>\
                        <unit_item>EACH</unit_item>\
                        <item_size><![CDATA[A]]></item_size>\
                        <item_color><![CDATA[红色]]></item_color>\
                        <item_spec_class>VAL,FRG</item_spec_class>\
                        <gross_weight>5.000</gross_weight>\
                        <net_weight>5.000</net_weight>\
                        <weight_um>g</weight_um>\
                        <volume>6000.000</volume>\
                        <volume_um>cm3</volume_um>\
                        <img>123</img>\
                        <qty>1</qty>\
                        <warehouse_code>VIP_NH</warehouse_code>\
                        <company_code>VIPS</company_code>\
                        <quality>{}</quality>\
                        <mfg_date>{}</mfg_date>\
                        <exp_date>{}</exp_date>\
                        <inv_type>{}</inv_type>\
                        <vendor_code>{}</vendor_code>\
                        <po_no>{}</po_no>\
                </item>\
    </details>\
    </item>\
    <item>\
        <id>{}6</id>\
        <warehouse_code>VIP_NH</warehouse_code>\
        <source_code>VIPS</source_code>\
        <destination_code>FH</destination_code>\
        <action_type>NEW</action_type>\
        <work_no>test{}-6</work_no>\
        <work_type>FLOWPICK_MS</work_type>\
        <action_time>{}</action_time>\
        <remark>1211</remark>\
        <line_count>1</line_count>\
        <container_count>0</container_count>\
        <inf_function>1</inf_function>\
        <priority>0</priority>\
        <details>\
                <item>\
                        <id>6{}</id>\
                        <container_code/>\
                        <item_code>{}</item_code>\
                        <item_desc>{}</item_desc>\
                        <brand_name>brand06{}</brand_name>\
                        <item_cat1_code>cat1code06{}</item_cat1_code>\
                        <item_cat1_name>cat106{}</item_cat1_name>\
                        <item_cat2_code>cat2code06{}</item_cat2_code>\
                        <item_cat2_name>cat206{}</item_cat2_name>\
                        <item_cat3_code>cat3code06{}</item_cat3_code>\
                        <item_cat3_name>cat306{}</item_cat3_name>\
                        <unit_item>EACH</unit_item>\
                        <item_size><![CDATA[A]]></item_size>\
                        <item_color><![CDATA[红色]]></item_color>\
                        <item_spec_class>VAL,FRG</item_spec_class>\
                        <gross_weight>5.000</gross_weight>\
                        <net_weight>5.000</net_weight>\
                        <weight_um>g</weight_um>\
                        <volume>6000.000</volume>\
                        <volume_um>cm3</volume_um>\
                        <img>123</img>\
                        <qty>1</qty>\
                        <warehouse_code>VIP_NH</warehouse_code>\
                        <company_code>VIPS</company_code>\
                        <quality>{}</quality>\
                        <mfg_date>{}</mfg_date>\
                        <exp_date>{}</exp_date>\
                        <inv_type>{}</inv_type>\
                        <vendor_code>{}</vendor_code>\
                        <po_no>{}</po_no>\
                </item>\
    </details>\
    </item>\
    <item>\
        <id>{}7</id>\
        <warehouse_code>VIP_NH</warehouse_code>\
        <source_code>VIPS</source_code>\
        <destination_code>FH</destination_code>\
        <action_type>NEW</action_type>\
        <work_no>test{}-7</work_no>\
        <work_type>FLOWPICK_MS</work_type>\
        <action_time>{}</action_time>\
        <remark>1211</remark>\
        <line_count>1</line_count>\
        <container_count>0</container_count>\
        <inf_function>1</inf_function>\
        <priority>0</priority>\
        <details>\
                <item>\
                        <id>7{}</id>\
                        <container_code/>\
                        <item_code>{}</item_code>\
                        <item_desc>{}</item_desc>\
                        <brand_name>brand07{}</brand_name>\
                        <item_cat1_code>cat1code07{}</item_cat1_code>\
                        <item_cat1_name>cat107{}</item_cat1_name>\
                        <item_cat2_code>cat2code07{}</item_cat2_code>\
                        <item_cat2_name>cat207{}</item_cat2_name>\
                        <item_cat3_code>cat3code07{}</item_cat3_code>\
                        <item_cat3_name>cat307{}</item_cat3_name>\
                        <unit_item>EACH</unit_item>\
                        <item_size><![CDATA[A]]></item_size>\
                        <item_color><![CDATA[红色]]></item_color>\
                        <item_spec_class>VAL,FRG</item_spec_class>\
                        <gross_weight>5.000</gross_weight>\
                        <net_weight>5.000</net_weight>\
                        <weight_um>g</weight_um>\
                        <volume>6000.000</volume>\
                        <volume_um>cm3</volume_um>\
                        <img>123</img>\
                        <qty>1</qty>\
                        <warehouse_code>VIP_NH</warehouse_code>\
                        <company_code>VIPS</company_code>\
                        <quality>{}</quality>\
                        <mfg_date>{}</mfg_date>\
                        <exp_date>{}</exp_date>\
                        <inv_type>{}</inv_type>\
                        <vendor_code>{}</vendor_code>\
                        <po_no>{}</po_no>\
                </item>\
    </details>\
    </item>\
    <item>\
        <id>{}8</id>\
        <warehouse_code>VIP_NH</warehouse_code>\
        <source_code>VIPS</source_code>\
        <destination_code>FH</destination_code>\
        <action_type>NEW</action_type>\
        <work_no>test{}-8</work_no>\
        <work_type>FLOWPICK_MS</work_type>\
        <action_time>{}</action_time>\
        <remark>1211</remark>\
        <line_count>1</line_count>\
        <container_count>0</container_count>\
        <inf_function>1</inf_function>\
        <priority>0</priority>\
        <details>\
                <item>\
                        <id>8{}</id>\
                        <container_code/>\
                        <item_code>{}</item_code>\
                        <item_desc>{}</item_desc>\
                        <brand_name>brand08{}</brand_name>\
                        <item_cat1_code>cat1code08{}</item_cat1_code>\
                        <item_cat1_name>cat108{}</item_cat1_name>\
                        <item_cat2_code>cat2code08{}</item_cat2_code>\
                        <item_cat2_name>cat208{}</item_cat2_name>\
                        <item_cat3_code>cat3code08{}</item_cat3_code>\
                        <item_cat3_name>cat308{}</item_cat3_name>\
                        <unit_item>EACH</unit_item>\
                        <item_size><![CDATA[A]]></item_size>\
                        <item_color><![CDATA[红色]]></item_color>\
                        <item_spec_class>VAL,FRG</item_spec_class>\
                        <gross_weight>5.000</gross_weight>\
                        <net_weight>5.000</net_weight>\
                        <weight_um>g</weight_um>\
                        <volume>6000.000</volume>\
                        <volume_um>cm3</volume_um>\
                        <img>123</img>\
                        <qty>1</qty>\
                        <warehouse_code>VIP_NH</warehouse_code>\
                        <company_code>VIPS</company_code>\
                        <quality>{}</quality>\
                        <mfg_date>{}</mfg_date>\
                        <exp_date>{}</exp_date>\
                        <inv_type>{}</inv_type>\
                        <vendor_code>{}</vendor_code>\
                        <po_no>{}</po_no>\
                </item>\
    </details>\
    </item>\
    <item>\
        <id>{}9</id>\
        <warehouse_code>VIP_NH</warehouse_code>\
        <source_code>VIPS</source_code>\
        <destination_code>FH</destination_code>\
        <action_type>NEW</action_type>\
        <work_no>test{}-9</work_no>\
        <work_type>FLOWPICK_MS</work_type>\
        <action_time>{}</action_time>\
        <remark>1211</remark>\
        <line_count>1</line_count>\
        <container_count>0</container_count>\
        <inf_function>1</inf_function>\
        <priority>0</priority>\
        <details>\
                <item>\
                        <id>9{}</id>\
                        <container_code/>\
                        <item_code>{}</item_code>\
                        <item_desc>{}</item_desc>\
                        <brand_name>brand09{}</brand_name>\
                        <item_cat1_code>cat1code09{}</item_cat1_code>\
                        <item_cat1_name>cat109{}</item_cat1_name>\
                        <item_cat2_code>cat2code09{}</item_cat2_code>\
                        <item_cat2_name>cat209{}</item_cat2_name>\
                        <item_cat3_code>cat3code09{}</item_cat3_code>\
                        <item_cat3_name>cat309{}</item_cat3_name>\
                        <unit_item>EACH</unit_item>\
                        <item_size><![CDATA[A]]></item_size>\
                        <item_color><![CDATA[红色]]></item_color>\
                        <item_spec_class>VAL,FRG</item_spec_class>\
                        <gross_weight>5.000</gross_weight>\
                        <net_weight>5.000</net_weight>\
                        <weight_um>g</weight_um>\
                        <volume>6000.000</volume>\
                        <volume_um>cm3</volume_um>\
                        <img>123</img>\
                        <qty>1</qty>\
                        <warehouse_code>VIP_NH</warehouse_code>\
                        <company_code>VIPS</company_code>\
                        <quality>{}</quality>\
                        <mfg_date>{}</mfg_date>\
                        <exp_date>{}</exp_date>\
                        <inv_type>{}</inv_type>\
                        <vendor_code>{}</vendor_code>\
                        <po_no>{}</po_no>\
                </item>\
    </details>\
    </item>\
    <item>\
        <id>{}10</id>\
        <warehouse_code>VIP_NH</warehouse_code>\
        <source_code>VIPS</source_code>\
        <destination_code>FH</destination_code>\
        <action_type>NEW</action_type>\
        <work_no>test{}-10</work_no>\
        <work_type>FLOWPICK_MS</work_type>\
        <action_time>{}</action_time>\
        <remark>1211</remark>\
        <line_count>1</line_count>\
        <container_count>0</container_count>\
        <inf_function>1</inf_function>\
        <priority>0</priority>\
        <details>\
                <item>\
                        <id>100{}</id>\
                        <container_code/>\
                        <item_code>{}</item_code>\
                        <item_desc>{}</item_desc>\
                        <brand_name>brand10{}</brand_name>\
                        <item_cat1_code>cat1code10{}</item_cat1_code>\
                        <item_cat1_name>cat110{}</item_cat1_name>\
                        <item_cat2_code>cat2code10{}</item_cat2_code>\
                        <item_cat2_name>cat210{}</item_cat2_name>\
                        <item_cat3_code>cat3code10{}</item_cat3_code>\
                        <item_cat3_name>cat310{}</item_cat3_name>\
                        <unit_item>EACH</unit_item>\
                        <item_size><![CDATA[A]]></item_size>\
                        <item_color><![CDATA[红色]]></item_color>\
                        <item_spec_class>VAL,FRG</item_spec_class>\
                        <gross_weight>5.000</gross_weight>\
                        <net_weight>5.000</net_weight>\
                        <weight_um>g</weight_um>\
                        <volume>6000.000</volume>\
                        <volume_um>cm3</volume_um>\
                        <img>123</img>\
                        <qty>1</qty>\
                        <warehouse_code>VIP_NH</warehouse_code>\
                        <company_code>VIPS</company_code>\
                        <quality>{}</quality>\
                        <mfg_date>{}</mfg_date>\
                        <exp_date>{}</exp_date>\
                        <inv_type>{}</inv_type>\
                        <vendor_code>{}</vendor_code>\
                        <po_no>{}</po_no>\
                </item>\
            </details>\
        </item>\
    </body>\
</root>'
# 定义xml转json的函数
def xml_to_json(xml_str):
    # parse是的xml解析器
    xml_parse = xmltodict.parse(xml_str)
    # json库dumps()是将dict转化成json格式,loads()是将json转化成dict格式。
    # dumps()方法的ident=1,格式化json
    json_str = json.dumps(xml_parse, indent=1)
    return json_str
print(xml_to_json(b))













