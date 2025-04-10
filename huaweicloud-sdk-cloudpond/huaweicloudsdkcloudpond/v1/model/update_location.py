# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateLocation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'country': 'str',
        'province': 'str',
        'city': 'str',
        'district': 'str',
        'condition': 'UpdateCondition',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'country': 'country',
        'province': 'province',
        'city': 'city',
        'district': 'district',
        'condition': 'condition',
        'description': 'description'
    }

    def __init__(self, name=None, country=None, province=None, city=None, district=None, condition=None, description=None):
        r"""UpdateLocation

        The model defined in huaweicloud sdk

        :param name: 场地名称（已废弃），传入该参数不会再生效，新建站点也不会再返回该字段
        :type name: str
        :param country: 场地所在国家
        :type country: str
        :param province: 场地所在省/自治区/直辖市
        :type province: str
        :param city: 场地所在市/区
        :type city: str
        :param district: 场地所在区/县
        :type district: str
        :param condition: 
        :type condition: :class:`huaweicloudsdkcloudpond.v1.UpdateCondition`
        :param description: 场地描述，最大支持长度为255个字节，不允许包含&lt;&gt;
        :type description: str
        """
        
        

        self._name = None
        self._country = None
        self._province = None
        self._city = None
        self._district = None
        self._condition = None
        self._description = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if country is not None:
            self.country = country
        if province is not None:
            self.province = province
        if city is not None:
            self.city = city
        if district is not None:
            self.district = district
        if condition is not None:
            self.condition = condition
        if description is not None:
            self.description = description

    @property
    def name(self):
        r"""Gets the name of this UpdateLocation.

        场地名称（已废弃），传入该参数不会再生效，新建站点也不会再返回该字段

        :return: The name of this UpdateLocation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateLocation.

        场地名称（已废弃），传入该参数不会再生效，新建站点也不会再返回该字段

        :param name: The name of this UpdateLocation.
        :type name: str
        """
        self._name = name

    @property
    def country(self):
        r"""Gets the country of this UpdateLocation.

        场地所在国家

        :return: The country of this UpdateLocation.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        r"""Sets the country of this UpdateLocation.

        场地所在国家

        :param country: The country of this UpdateLocation.
        :type country: str
        """
        self._country = country

    @property
    def province(self):
        r"""Gets the province of this UpdateLocation.

        场地所在省/自治区/直辖市

        :return: The province of this UpdateLocation.
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        r"""Sets the province of this UpdateLocation.

        场地所在省/自治区/直辖市

        :param province: The province of this UpdateLocation.
        :type province: str
        """
        self._province = province

    @property
    def city(self):
        r"""Gets the city of this UpdateLocation.

        场地所在市/区

        :return: The city of this UpdateLocation.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        r"""Sets the city of this UpdateLocation.

        场地所在市/区

        :param city: The city of this UpdateLocation.
        :type city: str
        """
        self._city = city

    @property
    def district(self):
        r"""Gets the district of this UpdateLocation.

        场地所在区/县

        :return: The district of this UpdateLocation.
        :rtype: str
        """
        return self._district

    @district.setter
    def district(self, district):
        r"""Sets the district of this UpdateLocation.

        场地所在区/县

        :param district: The district of this UpdateLocation.
        :type district: str
        """
        self._district = district

    @property
    def condition(self):
        r"""Gets the condition of this UpdateLocation.

        :return: The condition of this UpdateLocation.
        :rtype: :class:`huaweicloudsdkcloudpond.v1.UpdateCondition`
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        r"""Sets the condition of this UpdateLocation.

        :param condition: The condition of this UpdateLocation.
        :type condition: :class:`huaweicloudsdkcloudpond.v1.UpdateCondition`
        """
        self._condition = condition

    @property
    def description(self):
        r"""Gets the description of this UpdateLocation.

        场地描述，最大支持长度为255个字节，不允许包含<>

        :return: The description of this UpdateLocation.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateLocation.

        场地描述，最大支持长度为255个字节，不允许包含<>

        :param description: The description of this UpdateLocation.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, UpdateLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
