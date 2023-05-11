# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResouceInfo:

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
        'description': 'str',
        'home_link': 'str',
        'subscribe_link': 'str',
        'subscribe_guide': 'str',
        'type': 'str',
        'reference_price': 'str',
        'price_details_link': 'str',
        'specifications': 'object'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'home_link': 'home_link',
        'subscribe_link': 'subscribe_link',
        'subscribe_guide': 'subscribe_guide',
        'type': 'type',
        'reference_price': 'reference_price',
        'price_details_link': 'price_details_link',
        'specifications': 'specifications'
    }

    def __init__(self, name=None, description=None, home_link=None, subscribe_link=None, subscribe_guide=None, type=None, reference_price=None, price_details_link=None, specifications=None):
        """ResouceInfo

        The model defined in huaweicloud sdk

        :param name: 云服务名称。
        :type name: str
        :param description: 描述。
        :type description: str
        :param home_link: 首页链接。
        :type home_link: str
        :param subscribe_link: 开通链接。
        :type subscribe_link: str
        :param subscribe_guide: 开通指导。
        :type subscribe_guide: str
        :param type: 服务类型。
        :type type: str
        :param reference_price: 参考价格。
        :type reference_price: str
        :param price_details_link: 价格详情链接。
        :type price_details_link: str
        :param specifications: 规格,例如: {\&quot;cpu\&quot; : \&quot;0.5\&quot;,\&quot;ram\&quot; : 1GB}。
        :type specifications: object
        """
        
        

        self._name = None
        self._description = None
        self._home_link = None
        self._subscribe_link = None
        self._subscribe_guide = None
        self._type = None
        self._reference_price = None
        self._price_details_link = None
        self._specifications = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if home_link is not None:
            self.home_link = home_link
        if subscribe_link is not None:
            self.subscribe_link = subscribe_link
        if subscribe_guide is not None:
            self.subscribe_guide = subscribe_guide
        if type is not None:
            self.type = type
        if reference_price is not None:
            self.reference_price = reference_price
        if price_details_link is not None:
            self.price_details_link = price_details_link
        if specifications is not None:
            self.specifications = specifications

    @property
    def name(self):
        """Gets the name of this ResouceInfo.

        云服务名称。

        :return: The name of this ResouceInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResouceInfo.

        云服务名称。

        :param name: The name of this ResouceInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ResouceInfo.

        描述。

        :return: The description of this ResouceInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ResouceInfo.

        描述。

        :param description: The description of this ResouceInfo.
        :type description: str
        """
        self._description = description

    @property
    def home_link(self):
        """Gets the home_link of this ResouceInfo.

        首页链接。

        :return: The home_link of this ResouceInfo.
        :rtype: str
        """
        return self._home_link

    @home_link.setter
    def home_link(self, home_link):
        """Sets the home_link of this ResouceInfo.

        首页链接。

        :param home_link: The home_link of this ResouceInfo.
        :type home_link: str
        """
        self._home_link = home_link

    @property
    def subscribe_link(self):
        """Gets the subscribe_link of this ResouceInfo.

        开通链接。

        :return: The subscribe_link of this ResouceInfo.
        :rtype: str
        """
        return self._subscribe_link

    @subscribe_link.setter
    def subscribe_link(self, subscribe_link):
        """Sets the subscribe_link of this ResouceInfo.

        开通链接。

        :param subscribe_link: The subscribe_link of this ResouceInfo.
        :type subscribe_link: str
        """
        self._subscribe_link = subscribe_link

    @property
    def subscribe_guide(self):
        """Gets the subscribe_guide of this ResouceInfo.

        开通指导。

        :return: The subscribe_guide of this ResouceInfo.
        :rtype: str
        """
        return self._subscribe_guide

    @subscribe_guide.setter
    def subscribe_guide(self, subscribe_guide):
        """Sets the subscribe_guide of this ResouceInfo.

        开通指导。

        :param subscribe_guide: The subscribe_guide of this ResouceInfo.
        :type subscribe_guide: str
        """
        self._subscribe_guide = subscribe_guide

    @property
    def type(self):
        """Gets the type of this ResouceInfo.

        服务类型。

        :return: The type of this ResouceInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ResouceInfo.

        服务类型。

        :param type: The type of this ResouceInfo.
        :type type: str
        """
        self._type = type

    @property
    def reference_price(self):
        """Gets the reference_price of this ResouceInfo.

        参考价格。

        :return: The reference_price of this ResouceInfo.
        :rtype: str
        """
        return self._reference_price

    @reference_price.setter
    def reference_price(self, reference_price):
        """Sets the reference_price of this ResouceInfo.

        参考价格。

        :param reference_price: The reference_price of this ResouceInfo.
        :type reference_price: str
        """
        self._reference_price = reference_price

    @property
    def price_details_link(self):
        """Gets the price_details_link of this ResouceInfo.

        价格详情链接。

        :return: The price_details_link of this ResouceInfo.
        :rtype: str
        """
        return self._price_details_link

    @price_details_link.setter
    def price_details_link(self, price_details_link):
        """Sets the price_details_link of this ResouceInfo.

        价格详情链接。

        :param price_details_link: The price_details_link of this ResouceInfo.
        :type price_details_link: str
        """
        self._price_details_link = price_details_link

    @property
    def specifications(self):
        """Gets the specifications of this ResouceInfo.

        规格,例如: {\"cpu\" : \"0.5\",\"ram\" : 1GB}。

        :return: The specifications of this ResouceInfo.
        :rtype: object
        """
        return self._specifications

    @specifications.setter
    def specifications(self, specifications):
        """Sets the specifications of this ResouceInfo.

        规格,例如: {\"cpu\" : \"0.5\",\"ram\" : 1GB}。

        :param specifications: The specifications of this ResouceInfo.
        :type specifications: object
        """
        self._specifications = specifications

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
        if not isinstance(other, ResouceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
