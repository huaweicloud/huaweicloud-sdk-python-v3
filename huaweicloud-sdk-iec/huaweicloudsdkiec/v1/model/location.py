# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Location:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'site_id': 'str',
        'area': 'str',
        'province': 'str',
        'city': 'str',
        'operator': 'str',
        'pool_id': 'str',
        'stack_count': 'int',
        'city_short_name': 'str'
    }

    attribute_map = {
        'site_id': 'site_id',
        'area': 'area',
        'province': 'province',
        'city': 'city',
        'operator': 'operator',
        'pool_id': 'pool_id',
        'stack_count': 'stack_count',
        'city_short_name': 'city_short_name'
    }

    def __init__(self, site_id=None, area=None, province=None, city=None, operator=None, pool_id=None, stack_count=None, city_short_name=None):
        """Location

        The model defined in huaweicloud sdk

        :param site_id: 站点ID。
        :type site_id: str
        :param area: 所在大区。
        :type area: str
        :param province: 所属省份英文名称。 大小写通用，皆支持
        :type province: str
        :param city: 所在城市英文名称。
        :type city: str
        :param operator: 所属运营商。
        :type operator: str
        :param pool_id: 线路ID。多线路场景下，创建的弹性公网IP在该线路下。
        :type pool_id: str
        :param stack_count: 站点需要发放的资源(组)总数。
        :type stack_count: int
        :param city_short_name: 城市简称。
        :type city_short_name: str
        """
        
        

        self._site_id = None
        self._area = None
        self._province = None
        self._city = None
        self._operator = None
        self._pool_id = None
        self._stack_count = None
        self._city_short_name = None
        self.discriminator = None

        if site_id is not None:
            self.site_id = site_id
        if area is not None:
            self.area = area
        if province is not None:
            self.province = province
        if city is not None:
            self.city = city
        if operator is not None:
            self.operator = operator
        if pool_id is not None:
            self.pool_id = pool_id
        if stack_count is not None:
            self.stack_count = stack_count
        if city_short_name is not None:
            self.city_short_name = city_short_name

    @property
    def site_id(self):
        """Gets the site_id of this Location.

        站点ID。

        :return: The site_id of this Location.
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this Location.

        站点ID。

        :param site_id: The site_id of this Location.
        :type site_id: str
        """
        self._site_id = site_id

    @property
    def area(self):
        """Gets the area of this Location.

        所在大区。

        :return: The area of this Location.
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this Location.

        所在大区。

        :param area: The area of this Location.
        :type area: str
        """
        self._area = area

    @property
    def province(self):
        """Gets the province of this Location.

        所属省份英文名称。 大小写通用，皆支持

        :return: The province of this Location.
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        """Sets the province of this Location.

        所属省份英文名称。 大小写通用，皆支持

        :param province: The province of this Location.
        :type province: str
        """
        self._province = province

    @property
    def city(self):
        """Gets the city of this Location.

        所在城市英文名称。

        :return: The city of this Location.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Location.

        所在城市英文名称。

        :param city: The city of this Location.
        :type city: str
        """
        self._city = city

    @property
    def operator(self):
        """Gets the operator of this Location.

        所属运营商。

        :return: The operator of this Location.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this Location.

        所属运营商。

        :param operator: The operator of this Location.
        :type operator: str
        """
        self._operator = operator

    @property
    def pool_id(self):
        """Gets the pool_id of this Location.

        线路ID。多线路场景下，创建的弹性公网IP在该线路下。

        :return: The pool_id of this Location.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """Sets the pool_id of this Location.

        线路ID。多线路场景下，创建的弹性公网IP在该线路下。

        :param pool_id: The pool_id of this Location.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def stack_count(self):
        """Gets the stack_count of this Location.

        站点需要发放的资源(组)总数。

        :return: The stack_count of this Location.
        :rtype: int
        """
        return self._stack_count

    @stack_count.setter
    def stack_count(self, stack_count):
        """Sets the stack_count of this Location.

        站点需要发放的资源(组)总数。

        :param stack_count: The stack_count of this Location.
        :type stack_count: int
        """
        self._stack_count = stack_count

    @property
    def city_short_name(self):
        """Gets the city_short_name of this Location.

        城市简称。

        :return: The city_short_name of this Location.
        :rtype: str
        """
        return self._city_short_name

    @city_short_name.setter
    def city_short_name(self, city_short_name):
        """Sets the city_short_name of this Location.

        城市简称。

        :param city_short_name: The city_short_name of this Location.
        :type city_short_name: str
        """
        self._city_short_name = city_short_name

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
        if not isinstance(other, Location):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
