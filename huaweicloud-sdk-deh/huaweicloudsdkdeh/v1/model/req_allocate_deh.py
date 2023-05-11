# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReqAllocateDeh:

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
        'auto_placement': 'str',
        'availability_zone': 'str',
        'host_type': 'str',
        'quantity': 'int',
        'tags': 'list[ResourceTag]'
    }

    attribute_map = {
        'name': 'name',
        'auto_placement': 'auto_placement',
        'availability_zone': 'availability_zone',
        'host_type': 'host_type',
        'quantity': 'quantity',
        'tags': 'tags'
    }

    def __init__(self, name=None, auto_placement=None, availability_zone=None, host_type=None, quantity=None, tags=None):
        """ReqAllocateDeh

        The model defined in huaweicloud sdk

        :param name: 专属主机名称。
        :type name: str
        :param auto_placement: 在创建云服务器时（未指定专属主机ID），是否允许云服务器自动分配在一台可用的专属主机上。 取值范围：“on”或“off”。 默认值：“on”。
        :type auto_placement: str
        :param availability_zone: 专属主机所属AZ。
        :type availability_zone: str
        :param host_type: 专属主机类型。
        :type host_type: str
        :param quantity: 待分配的专属主机数量。
        :type quantity: int
        :param tags: 专属主机标签列表。
        :type tags: list[:class:`huaweicloudsdkdeh.v1.ResourceTag`]
        """
        
        

        self._name = None
        self._auto_placement = None
        self._availability_zone = None
        self._host_type = None
        self._quantity = None
        self._tags = None
        self.discriminator = None

        self.name = name
        if auto_placement is not None:
            self.auto_placement = auto_placement
        self.availability_zone = availability_zone
        self.host_type = host_type
        self.quantity = quantity
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        """Gets the name of this ReqAllocateDeh.

        专属主机名称。

        :return: The name of this ReqAllocateDeh.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReqAllocateDeh.

        专属主机名称。

        :param name: The name of this ReqAllocateDeh.
        :type name: str
        """
        self._name = name

    @property
    def auto_placement(self):
        """Gets the auto_placement of this ReqAllocateDeh.

        在创建云服务器时（未指定专属主机ID），是否允许云服务器自动分配在一台可用的专属主机上。 取值范围：“on”或“off”。 默认值：“on”。

        :return: The auto_placement of this ReqAllocateDeh.
        :rtype: str
        """
        return self._auto_placement

    @auto_placement.setter
    def auto_placement(self, auto_placement):
        """Sets the auto_placement of this ReqAllocateDeh.

        在创建云服务器时（未指定专属主机ID），是否允许云服务器自动分配在一台可用的专属主机上。 取值范围：“on”或“off”。 默认值：“on”。

        :param auto_placement: The auto_placement of this ReqAllocateDeh.
        :type auto_placement: str
        """
        self._auto_placement = auto_placement

    @property
    def availability_zone(self):
        """Gets the availability_zone of this ReqAllocateDeh.

        专属主机所属AZ。

        :return: The availability_zone of this ReqAllocateDeh.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this ReqAllocateDeh.

        专属主机所属AZ。

        :param availability_zone: The availability_zone of this ReqAllocateDeh.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def host_type(self):
        """Gets the host_type of this ReqAllocateDeh.

        专属主机类型。

        :return: The host_type of this ReqAllocateDeh.
        :rtype: str
        """
        return self._host_type

    @host_type.setter
    def host_type(self, host_type):
        """Sets the host_type of this ReqAllocateDeh.

        专属主机类型。

        :param host_type: The host_type of this ReqAllocateDeh.
        :type host_type: str
        """
        self._host_type = host_type

    @property
    def quantity(self):
        """Gets the quantity of this ReqAllocateDeh.

        待分配的专属主机数量。

        :return: The quantity of this ReqAllocateDeh.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this ReqAllocateDeh.

        待分配的专属主机数量。

        :param quantity: The quantity of this ReqAllocateDeh.
        :type quantity: int
        """
        self._quantity = quantity

    @property
    def tags(self):
        """Gets the tags of this ReqAllocateDeh.

        专属主机标签列表。

        :return: The tags of this ReqAllocateDeh.
        :rtype: list[:class:`huaweicloudsdkdeh.v1.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ReqAllocateDeh.

        专属主机标签列表。

        :param tags: The tags of this ReqAllocateDeh.
        :type tags: list[:class:`huaweicloudsdkdeh.v1.ResourceTag`]
        """
        self._tags = tags

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
        if not isinstance(other, ReqAllocateDeh):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
