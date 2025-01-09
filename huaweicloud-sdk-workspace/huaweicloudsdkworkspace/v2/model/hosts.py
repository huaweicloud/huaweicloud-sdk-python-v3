# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Hosts:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'availability_zone': 'str',
        'name': 'str',
        'auto_placement': 'str',
        'host_type': 'str',
        'quantity': 'int',
        'product_id': 'str'
    }

    attribute_map = {
        'availability_zone': 'availability_zone',
        'name': 'name',
        'auto_placement': 'auto_placement',
        'host_type': 'host_type',
        'quantity': 'quantity',
        'product_id': 'product_id'
    }

    def __init__(self, availability_zone=None, name=None, auto_placement=None, host_type=None, quantity=None, product_id=None):
        """Hosts

        The model defined in huaweicloud sdk

        :param availability_zone: 主机所属AZ。
        :type availability_zone: str
        :param name: 主机名称。
        :type name: str
        :param auto_placement: 在创建云服务器时（未指定主机ID），是否允许云服务器自动分配在一台可用的主机上。取值范围：“on”或“off”默认为 “on”。
        :type auto_placement: str
        :param host_type: 主机类型。
        :type host_type: str
        :param quantity: 待分配的主机数量
        :type quantity: int
        :param product_id: 主机产品Id
        :type product_id: str
        """
        
        

        self._availability_zone = None
        self._name = None
        self._auto_placement = None
        self._host_type = None
        self._quantity = None
        self._product_id = None
        self.discriminator = None

        self.availability_zone = availability_zone
        self.name = name
        if auto_placement is not None:
            self.auto_placement = auto_placement
        self.host_type = host_type
        self.quantity = quantity
        self.product_id = product_id

    @property
    def availability_zone(self):
        """Gets the availability_zone of this Hosts.

        主机所属AZ。

        :return: The availability_zone of this Hosts.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this Hosts.

        主机所属AZ。

        :param availability_zone: The availability_zone of this Hosts.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def name(self):
        """Gets the name of this Hosts.

        主机名称。

        :return: The name of this Hosts.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Hosts.

        主机名称。

        :param name: The name of this Hosts.
        :type name: str
        """
        self._name = name

    @property
    def auto_placement(self):
        """Gets the auto_placement of this Hosts.

        在创建云服务器时（未指定主机ID），是否允许云服务器自动分配在一台可用的主机上。取值范围：“on”或“off”默认为 “on”。

        :return: The auto_placement of this Hosts.
        :rtype: str
        """
        return self._auto_placement

    @auto_placement.setter
    def auto_placement(self, auto_placement):
        """Sets the auto_placement of this Hosts.

        在创建云服务器时（未指定主机ID），是否允许云服务器自动分配在一台可用的主机上。取值范围：“on”或“off”默认为 “on”。

        :param auto_placement: The auto_placement of this Hosts.
        :type auto_placement: str
        """
        self._auto_placement = auto_placement

    @property
    def host_type(self):
        """Gets the host_type of this Hosts.

        主机类型。

        :return: The host_type of this Hosts.
        :rtype: str
        """
        return self._host_type

    @host_type.setter
    def host_type(self, host_type):
        """Sets the host_type of this Hosts.

        主机类型。

        :param host_type: The host_type of this Hosts.
        :type host_type: str
        """
        self._host_type = host_type

    @property
    def quantity(self):
        """Gets the quantity of this Hosts.

        待分配的主机数量

        :return: The quantity of this Hosts.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this Hosts.

        待分配的主机数量

        :param quantity: The quantity of this Hosts.
        :type quantity: int
        """
        self._quantity = quantity

    @property
    def product_id(self):
        """Gets the product_id of this Hosts.

        主机产品Id

        :return: The product_id of this Hosts.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this Hosts.

        主机产品Id

        :param product_id: The product_id of this Hosts.
        :type product_id: str
        """
        self._product_id = product_id

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
        if not isinstance(other, Hosts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
