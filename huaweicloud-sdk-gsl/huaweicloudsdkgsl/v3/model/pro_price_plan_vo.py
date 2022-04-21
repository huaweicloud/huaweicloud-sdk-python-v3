# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProPricePlanVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'price_plan_id': 'str',
        'price_plan_name': 'str',
        'description': 'str',
        'flow_total': 'int',
        'package_type': 'int',
        'period': 'int',
        'period_type': 'int',
        'effect_type': 'int',
        'silent_period_day': 'int',
        'silent_period_unit': 'int',
        'auto_renew': 'bool',
        'location_desc': 'str',
        'location_type': 'int',
        'sim_type': 'int',
        'carrier_type': 'int',
        'price': 'int'
    }

    attribute_map = {
        'price_plan_id': 'price_plan_id',
        'price_plan_name': 'price_plan_name',
        'description': 'description',
        'flow_total': 'flow_total',
        'package_type': 'package_type',
        'period': 'period',
        'period_type': 'period_type',
        'effect_type': 'effect_type',
        'silent_period_day': 'silent_period_day',
        'silent_period_unit': 'silent_period_unit',
        'auto_renew': 'auto_renew',
        'location_desc': 'location_desc',
        'location_type': 'location_type',
        'sim_type': 'sim_type',
        'carrier_type': 'carrier_type',
        'price': 'price'
    }

    def __init__(self, price_plan_id=None, price_plan_name=None, description=None, flow_total=None, package_type=None, period=None, period_type=None, effect_type=None, silent_period_day=None, silent_period_unit=None, auto_renew=None, location_desc=None, location_type=None, sim_type=None, carrier_type=None, price=None):
        """ProPricePlanVo

        The model defined in huaweicloud sdk

        :param price_plan_id: 套餐ID
        :type price_plan_id: str
        :param price_plan_name: 套餐名称
        :type price_plan_name: str
        :param description: 描述
        :type description: str
        :param flow_total: 流量总量(MB)
        :type flow_total: int
        :param package_type: 套餐类型 1基础套餐;2叠加包套餐;如果是国际漫游不区分基础套餐包和叠加包
        :type package_type: int
        :param period: 套餐周期
        :type period: int
        :param period_type: 套餐周期类型 10:日;20:月;30:季;40:半年;50:年
        :type period_type: int
        :param effect_type: 套餐生效类型 1.订购后激活使用时生效 2.订购即时生效 3.订购下个月开始生效
        :type effect_type: int
        :param silent_period_day: 沉默期
        :type silent_period_day: int
        :param silent_period_unit: 沉默期单位 1.年 2.月 3.日
        :type silent_period_unit: int
        :param auto_renew: 是否自动续订
        :type auto_renew: bool
        :param location_desc: 套餐适用区域
        :type location_desc: str
        :param location_type: 区域 1.中国 2.欧洲 3.大洋洲 4.非洲 5.亚太
        :type location_type: int
        :param sim_type: SIM卡类型 1.vSIM 2.eSIM 3.实体卡
        :type sim_type: int
        :param carrier_type: 运营商 101/1 中国移动/中国移动（实体卡） 102/2中国电信/中国电信（实体卡） 3中国联通（实体卡） 201.欧洲 501.中国香港 502.中国澳门 503.泰国 504.日本 505.柬埔寨 506.印度尼西亚 507.马来西亚 508.新加坡 509.斯里兰卡 510.中国台湾 511.孟加拉 
        :type carrier_type: int
        :param price: 价格(分)
        :type price: int
        """
        
        

        self._price_plan_id = None
        self._price_plan_name = None
        self._description = None
        self._flow_total = None
        self._package_type = None
        self._period = None
        self._period_type = None
        self._effect_type = None
        self._silent_period_day = None
        self._silent_period_unit = None
        self._auto_renew = None
        self._location_desc = None
        self._location_type = None
        self._sim_type = None
        self._carrier_type = None
        self._price = None
        self.discriminator = None

        if price_plan_id is not None:
            self.price_plan_id = price_plan_id
        if price_plan_name is not None:
            self.price_plan_name = price_plan_name
        if description is not None:
            self.description = description
        if flow_total is not None:
            self.flow_total = flow_total
        if package_type is not None:
            self.package_type = package_type
        if period is not None:
            self.period = period
        if period_type is not None:
            self.period_type = period_type
        if effect_type is not None:
            self.effect_type = effect_type
        if silent_period_day is not None:
            self.silent_period_day = silent_period_day
        if silent_period_unit is not None:
            self.silent_period_unit = silent_period_unit
        if auto_renew is not None:
            self.auto_renew = auto_renew
        if location_desc is not None:
            self.location_desc = location_desc
        if location_type is not None:
            self.location_type = location_type
        if sim_type is not None:
            self.sim_type = sim_type
        if carrier_type is not None:
            self.carrier_type = carrier_type
        if price is not None:
            self.price = price

    @property
    def price_plan_id(self):
        """Gets the price_plan_id of this ProPricePlanVo.

        套餐ID

        :return: The price_plan_id of this ProPricePlanVo.
        :rtype: str
        """
        return self._price_plan_id

    @price_plan_id.setter
    def price_plan_id(self, price_plan_id):
        """Sets the price_plan_id of this ProPricePlanVo.

        套餐ID

        :param price_plan_id: The price_plan_id of this ProPricePlanVo.
        :type price_plan_id: str
        """
        self._price_plan_id = price_plan_id

    @property
    def price_plan_name(self):
        """Gets the price_plan_name of this ProPricePlanVo.

        套餐名称

        :return: The price_plan_name of this ProPricePlanVo.
        :rtype: str
        """
        return self._price_plan_name

    @price_plan_name.setter
    def price_plan_name(self, price_plan_name):
        """Sets the price_plan_name of this ProPricePlanVo.

        套餐名称

        :param price_plan_name: The price_plan_name of this ProPricePlanVo.
        :type price_plan_name: str
        """
        self._price_plan_name = price_plan_name

    @property
    def description(self):
        """Gets the description of this ProPricePlanVo.

        描述

        :return: The description of this ProPricePlanVo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProPricePlanVo.

        描述

        :param description: The description of this ProPricePlanVo.
        :type description: str
        """
        self._description = description

    @property
    def flow_total(self):
        """Gets the flow_total of this ProPricePlanVo.

        流量总量(MB)

        :return: The flow_total of this ProPricePlanVo.
        :rtype: int
        """
        return self._flow_total

    @flow_total.setter
    def flow_total(self, flow_total):
        """Sets the flow_total of this ProPricePlanVo.

        流量总量(MB)

        :param flow_total: The flow_total of this ProPricePlanVo.
        :type flow_total: int
        """
        self._flow_total = flow_total

    @property
    def package_type(self):
        """Gets the package_type of this ProPricePlanVo.

        套餐类型 1基础套餐;2叠加包套餐;如果是国际漫游不区分基础套餐包和叠加包

        :return: The package_type of this ProPricePlanVo.
        :rtype: int
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        """Sets the package_type of this ProPricePlanVo.

        套餐类型 1基础套餐;2叠加包套餐;如果是国际漫游不区分基础套餐包和叠加包

        :param package_type: The package_type of this ProPricePlanVo.
        :type package_type: int
        """
        self._package_type = package_type

    @property
    def period(self):
        """Gets the period of this ProPricePlanVo.

        套餐周期

        :return: The period of this ProPricePlanVo.
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this ProPricePlanVo.

        套餐周期

        :param period: The period of this ProPricePlanVo.
        :type period: int
        """
        self._period = period

    @property
    def period_type(self):
        """Gets the period_type of this ProPricePlanVo.

        套餐周期类型 10:日;20:月;30:季;40:半年;50:年

        :return: The period_type of this ProPricePlanVo.
        :rtype: int
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this ProPricePlanVo.

        套餐周期类型 10:日;20:月;30:季;40:半年;50:年

        :param period_type: The period_type of this ProPricePlanVo.
        :type period_type: int
        """
        self._period_type = period_type

    @property
    def effect_type(self):
        """Gets the effect_type of this ProPricePlanVo.

        套餐生效类型 1.订购后激活使用时生效 2.订购即时生效 3.订购下个月开始生效

        :return: The effect_type of this ProPricePlanVo.
        :rtype: int
        """
        return self._effect_type

    @effect_type.setter
    def effect_type(self, effect_type):
        """Sets the effect_type of this ProPricePlanVo.

        套餐生效类型 1.订购后激活使用时生效 2.订购即时生效 3.订购下个月开始生效

        :param effect_type: The effect_type of this ProPricePlanVo.
        :type effect_type: int
        """
        self._effect_type = effect_type

    @property
    def silent_period_day(self):
        """Gets the silent_period_day of this ProPricePlanVo.

        沉默期

        :return: The silent_period_day of this ProPricePlanVo.
        :rtype: int
        """
        return self._silent_period_day

    @silent_period_day.setter
    def silent_period_day(self, silent_period_day):
        """Sets the silent_period_day of this ProPricePlanVo.

        沉默期

        :param silent_period_day: The silent_period_day of this ProPricePlanVo.
        :type silent_period_day: int
        """
        self._silent_period_day = silent_period_day

    @property
    def silent_period_unit(self):
        """Gets the silent_period_unit of this ProPricePlanVo.

        沉默期单位 1.年 2.月 3.日

        :return: The silent_period_unit of this ProPricePlanVo.
        :rtype: int
        """
        return self._silent_period_unit

    @silent_period_unit.setter
    def silent_period_unit(self, silent_period_unit):
        """Sets the silent_period_unit of this ProPricePlanVo.

        沉默期单位 1.年 2.月 3.日

        :param silent_period_unit: The silent_period_unit of this ProPricePlanVo.
        :type silent_period_unit: int
        """
        self._silent_period_unit = silent_period_unit

    @property
    def auto_renew(self):
        """Gets the auto_renew of this ProPricePlanVo.

        是否自动续订

        :return: The auto_renew of this ProPricePlanVo.
        :rtype: bool
        """
        return self._auto_renew

    @auto_renew.setter
    def auto_renew(self, auto_renew):
        """Sets the auto_renew of this ProPricePlanVo.

        是否自动续订

        :param auto_renew: The auto_renew of this ProPricePlanVo.
        :type auto_renew: bool
        """
        self._auto_renew = auto_renew

    @property
    def location_desc(self):
        """Gets the location_desc of this ProPricePlanVo.

        套餐适用区域

        :return: The location_desc of this ProPricePlanVo.
        :rtype: str
        """
        return self._location_desc

    @location_desc.setter
    def location_desc(self, location_desc):
        """Sets the location_desc of this ProPricePlanVo.

        套餐适用区域

        :param location_desc: The location_desc of this ProPricePlanVo.
        :type location_desc: str
        """
        self._location_desc = location_desc

    @property
    def location_type(self):
        """Gets the location_type of this ProPricePlanVo.

        区域 1.中国 2.欧洲 3.大洋洲 4.非洲 5.亚太

        :return: The location_type of this ProPricePlanVo.
        :rtype: int
        """
        return self._location_type

    @location_type.setter
    def location_type(self, location_type):
        """Sets the location_type of this ProPricePlanVo.

        区域 1.中国 2.欧洲 3.大洋洲 4.非洲 5.亚太

        :param location_type: The location_type of this ProPricePlanVo.
        :type location_type: int
        """
        self._location_type = location_type

    @property
    def sim_type(self):
        """Gets the sim_type of this ProPricePlanVo.

        SIM卡类型 1.vSIM 2.eSIM 3.实体卡

        :return: The sim_type of this ProPricePlanVo.
        :rtype: int
        """
        return self._sim_type

    @sim_type.setter
    def sim_type(self, sim_type):
        """Sets the sim_type of this ProPricePlanVo.

        SIM卡类型 1.vSIM 2.eSIM 3.实体卡

        :param sim_type: The sim_type of this ProPricePlanVo.
        :type sim_type: int
        """
        self._sim_type = sim_type

    @property
    def carrier_type(self):
        """Gets the carrier_type of this ProPricePlanVo.

        运营商 101/1 中国移动/中国移动（实体卡） 102/2中国电信/中国电信（实体卡） 3中国联通（实体卡） 201.欧洲 501.中国香港 502.中国澳门 503.泰国 504.日本 505.柬埔寨 506.印度尼西亚 507.马来西亚 508.新加坡 509.斯里兰卡 510.中国台湾 511.孟加拉 

        :return: The carrier_type of this ProPricePlanVo.
        :rtype: int
        """
        return self._carrier_type

    @carrier_type.setter
    def carrier_type(self, carrier_type):
        """Sets the carrier_type of this ProPricePlanVo.

        运营商 101/1 中国移动/中国移动（实体卡） 102/2中国电信/中国电信（实体卡） 3中国联通（实体卡） 201.欧洲 501.中国香港 502.中国澳门 503.泰国 504.日本 505.柬埔寨 506.印度尼西亚 507.马来西亚 508.新加坡 509.斯里兰卡 510.中国台湾 511.孟加拉 

        :param carrier_type: The carrier_type of this ProPricePlanVo.
        :type carrier_type: int
        """
        self._carrier_type = carrier_type

    @property
    def price(self):
        """Gets the price of this ProPricePlanVo.

        价格(分)

        :return: The price of this ProPricePlanVo.
        :rtype: int
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this ProPricePlanVo.

        价格(分)

        :param price: The price of this ProPricePlanVo.
        :type price: int
        """
        self._price = price

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProPricePlanVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
