# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProPricePlansRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'main_search_key': 'str',
        'flow_total': 'int',
        'network_type': 'int',
        'location_type': 'int',
        'carrier_type': 'int',
        'country_type': 'int',
        'sim_card_id': 'int',
        'partner': 'int',
        'package_type': 'int',
        'sim_type': 'int'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'main_search_key': 'main_search_key',
        'flow_total': 'flow_total',
        'network_type': 'network_type',
        'location_type': 'location_type',
        'carrier_type': 'carrier_type',
        'country_type': 'country_type',
        'sim_card_id': 'sim_card_id',
        'partner': 'partner',
        'package_type': 'package_type',
        'sim_type': 'sim_type'
    }

    def __init__(self, limit=None, offset=None, main_search_key=None, flow_total=None, network_type=None, location_type=None, carrier_type=None, country_type=None, sim_card_id=None, partner=None, package_type=None, sim_type=None):
        """ListProPricePlansRequest - a model defined in huaweicloud sdk"""
        
        

        self._limit = None
        self._offset = None
        self._main_search_key = None
        self._flow_total = None
        self._network_type = None
        self._location_type = None
        self._carrier_type = None
        self._country_type = None
        self._sim_card_id = None
        self._partner = None
        self._package_type = None
        self._sim_type = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if main_search_key is not None:
            self.main_search_key = main_search_key
        if flow_total is not None:
            self.flow_total = flow_total
        if network_type is not None:
            self.network_type = network_type
        if location_type is not None:
            self.location_type = location_type
        if carrier_type is not None:
            self.carrier_type = carrier_type
        if country_type is not None:
            self.country_type = country_type
        if sim_card_id is not None:
            self.sim_card_id = sim_card_id
        if partner is not None:
            self.partner = partner
        if package_type is not None:
            self.package_type = package_type
        if sim_type is not None:
            self.sim_type = sim_type

    @property
    def limit(self):
        """Gets the limit of this ListProPricePlansRequest.

        分页查询时每页显示的记录数，默认值为10，取值范围为10-500的整数

        :return: The limit of this ListProPricePlansRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListProPricePlansRequest.

        分页查询时每页显示的记录数，默认值为10，取值范围为10-500的整数

        :param limit: The limit of this ListProPricePlansRequest.
        :type: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListProPricePlansRequest.

        分页查询时的页码数，默认值为1，取值范围为1-1000000的整数

        :return: The offset of this ListProPricePlansRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListProPricePlansRequest.

        分页查询时的页码数，默认值为1，取值范围为1-1000000的整数

        :param offset: The offset of this ListProPricePlansRequest.
        :type: int
        """
        self._offset = offset

    @property
    def main_search_key(self):
        """Gets the main_search_key of this ListProPricePlansRequest.

        查询关键标识类型：套餐名称 例如中国香港每月10M联接服务

        :return: The main_search_key of this ListProPricePlansRequest.
        :rtype: str
        """
        return self._main_search_key

    @main_search_key.setter
    def main_search_key(self, main_search_key):
        """Sets the main_search_key of this ListProPricePlansRequest.

        查询关键标识类型：套餐名称 例如中国香港每月10M联接服务

        :param main_search_key: The main_search_key of this ListProPricePlansRequest.
        :type: str
        """
        self._main_search_key = main_search_key

    @property
    def flow_total(self):
        """Gets the flow_total of this ListProPricePlansRequest.

        流量总量(MB)

        :return: The flow_total of this ListProPricePlansRequest.
        :rtype: int
        """
        return self._flow_total

    @flow_total.setter
    def flow_total(self, flow_total):
        """Sets the flow_total of this ListProPricePlansRequest.

        流量总量(MB)

        :param flow_total: The flow_total of this ListProPricePlansRequest.
        :type: int
        """
        self._flow_total = flow_total

    @property
    def network_type(self):
        """Gets the network_type of this ListProPricePlansRequest.

        网络制式

        :return: The network_type of this ListProPricePlansRequest.
        :rtype: int
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        """Sets the network_type of this ListProPricePlansRequest.

        网络制式

        :param network_type: The network_type of this ListProPricePlansRequest.
        :type: int
        """
        self._network_type = network_type

    @property
    def location_type(self):
        """Gets the location_type of this ListProPricePlansRequest.

        覆盖区域:1.  中国 2.  欧洲 3.  大洋洲 4.  非洲 5.  亚太

        :return: The location_type of this ListProPricePlansRequest.
        :rtype: int
        """
        return self._location_type

    @location_type.setter
    def location_type(self, location_type):
        """Sets the location_type of this ListProPricePlansRequest.

        覆盖区域:1.  中国 2.  欧洲 3.  大洋洲 4.  非洲 5.  亚太

        :param location_type: The location_type of this ListProPricePlansRequest.
        :type: int
        """
        self._location_type = location_type

    @property
    def carrier_type(self):
        """Gets the carrier_type of this ListProPricePlansRequest.

        运营商 101/1 中国移动/中国移动（实体卡） 102/2中国电信/中国电信（实体卡） 3中国联通（实体卡） 201.欧洲 501.中国香港 502.中国澳门 503.泰国 504.日本 505.柬埔寨 506.印度尼西亚 507.马来西亚 508.新加坡 509.斯里兰卡 510.中国台湾 511.孟加拉 

        :return: The carrier_type of this ListProPricePlansRequest.
        :rtype: int
        """
        return self._carrier_type

    @carrier_type.setter
    def carrier_type(self, carrier_type):
        """Sets the carrier_type of this ListProPricePlansRequest.

        运营商 101/1 中国移动/中国移动（实体卡） 102/2中国电信/中国电信（实体卡） 3中国联通（实体卡） 201.欧洲 501.中国香港 502.中国澳门 503.泰国 504.日本 505.柬埔寨 506.印度尼西亚 507.马来西亚 508.新加坡 509.斯里兰卡 510.中国台湾 511.孟加拉 

        :param carrier_type: The carrier_type of this ListProPricePlansRequest.
        :type: int
        """
        self._carrier_type = carrier_type

    @property
    def country_type(self):
        """Gets the country_type of this ListProPricePlansRequest.

        国家/地区 1中国香港，2中国澳门，3泰国，4日本，5，柬埔寨，6印尼，7马来西亚，8新加坡，9斯里兰卡，10中国台湾，11孟加拉

        :return: The country_type of this ListProPricePlansRequest.
        :rtype: int
        """
        return self._country_type

    @country_type.setter
    def country_type(self, country_type):
        """Sets the country_type of this ListProPricePlansRequest.

        国家/地区 1中国香港，2中国澳门，3泰国，4日本，5，柬埔寨，6印尼，7马来西亚，8新加坡，9斯里兰卡，10中国台湾，11孟加拉

        :param country_type: The country_type of this ListProPricePlansRequest.
        :type: int
        """
        self._country_type = country_type

    @property
    def sim_card_id(self):
        """Gets the sim_card_id of this ListProPricePlansRequest.

        sim card id sim卡标识

        :return: The sim_card_id of this ListProPricePlansRequest.
        :rtype: int
        """
        return self._sim_card_id

    @sim_card_id.setter
    def sim_card_id(self, sim_card_id):
        """Sets the sim_card_id of this ListProPricePlansRequest.

        sim card id sim卡标识

        :param sim_card_id: The sim_card_id of this ListProPricePlansRequest.
        :type: int
        """
        self._sim_card_id = sim_card_id

    @property
    def partner(self):
        """Gets the partner of this ListProPricePlansRequest.

        伙伴

        :return: The partner of this ListProPricePlansRequest.
        :rtype: int
        """
        return self._partner

    @partner.setter
    def partner(self, partner):
        """Sets the partner of this ListProPricePlansRequest.

        伙伴

        :param partner: The partner of this ListProPricePlansRequest.
        :type: int
        """
        self._partner = partner

    @property
    def package_type(self):
        """Gets the package_type of this ListProPricePlansRequest.

        套餐类型

        :return: The package_type of this ListProPricePlansRequest.
        :rtype: int
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        """Sets the package_type of this ListProPricePlansRequest.

        套餐类型

        :param package_type: The package_type of this ListProPricePlansRequest.
        :type: int
        """
        self._package_type = package_type

    @property
    def sim_type(self):
        """Gets the sim_type of this ListProPricePlansRequest.

        适用SIM卡类型

        :return: The sim_type of this ListProPricePlansRequest.
        :rtype: int
        """
        return self._sim_type

    @sim_type.setter
    def sim_type(self, sim_type):
        """Sets the sim_type of this ListProPricePlansRequest.

        适用SIM卡类型

        :param sim_type: The sim_type of this ListProPricePlansRequest.
        :type: int
        """
        self._sim_type = sim_type

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
        if not isinstance(other, ListProPricePlansRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
