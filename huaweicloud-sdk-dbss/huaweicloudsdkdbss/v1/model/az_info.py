# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AzInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'zone_name': 'str',
        'zone_number': 'int',
        'az_type': 'str',
        'alias': 'str',
        'alias_us': 'str'
    }

    attribute_map = {
        'zone_name': 'zone_name',
        'zone_number': 'zone_number',
        'az_type': 'az_type',
        'alias': 'alias',
        'alias_us': 'alias_us'
    }

    def __init__(self, zone_name=None, zone_number=None, az_type=None, alias=None, alias_us=None):
        """AzInfo

        The model defined in huaweicloud sdk

        :param zone_name: 可用区名称
        :type zone_name: str
        :param zone_number: 可用区编号
        :type zone_number: int
        :param az_type: 可用区类型
        :type az_type: str
        :param alias: 可用区别名
        :type alias: str
        :param alias_us: 可用区别名英文
        :type alias_us: str
        """
        
        

        self._zone_name = None
        self._zone_number = None
        self._az_type = None
        self._alias = None
        self._alias_us = None
        self.discriminator = None

        self.zone_name = zone_name
        self.zone_number = zone_number
        self.az_type = az_type
        self.alias = alias
        self.alias_us = alias_us

    @property
    def zone_name(self):
        """Gets the zone_name of this AzInfo.

        可用区名称

        :return: The zone_name of this AzInfo.
        :rtype: str
        """
        return self._zone_name

    @zone_name.setter
    def zone_name(self, zone_name):
        """Sets the zone_name of this AzInfo.

        可用区名称

        :param zone_name: The zone_name of this AzInfo.
        :type zone_name: str
        """
        self._zone_name = zone_name

    @property
    def zone_number(self):
        """Gets the zone_number of this AzInfo.

        可用区编号

        :return: The zone_number of this AzInfo.
        :rtype: int
        """
        return self._zone_number

    @zone_number.setter
    def zone_number(self, zone_number):
        """Sets the zone_number of this AzInfo.

        可用区编号

        :param zone_number: The zone_number of this AzInfo.
        :type zone_number: int
        """
        self._zone_number = zone_number

    @property
    def az_type(self):
        """Gets the az_type of this AzInfo.

        可用区类型

        :return: The az_type of this AzInfo.
        :rtype: str
        """
        return self._az_type

    @az_type.setter
    def az_type(self, az_type):
        """Sets the az_type of this AzInfo.

        可用区类型

        :param az_type: The az_type of this AzInfo.
        :type az_type: str
        """
        self._az_type = az_type

    @property
    def alias(self):
        """Gets the alias of this AzInfo.

        可用区别名

        :return: The alias of this AzInfo.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this AzInfo.

        可用区别名

        :param alias: The alias of this AzInfo.
        :type alias: str
        """
        self._alias = alias

    @property
    def alias_us(self):
        """Gets the alias_us of this AzInfo.

        可用区别名英文

        :return: The alias_us of this AzInfo.
        :rtype: str
        """
        return self._alias_us

    @alias_us.setter
    def alias_us(self, alias_us):
        """Sets the alias_us of this AzInfo.

        可用区别名英文

        :param alias_us: The alias_us of this AzInfo.
        :type alias_us: str
        """
        self._alias_us = alias_us

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
        if not isinstance(other, AzInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
