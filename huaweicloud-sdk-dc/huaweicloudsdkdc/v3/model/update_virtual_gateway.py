# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateVirtualGateway:

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
        'local_ep_group': 'list[str]',
        'local_ep_group_ipv6': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'local_ep_group': 'local_ep_group',
        'local_ep_group_ipv6': 'local_ep_group_ipv6'
    }

    def __init__(self, name=None, description=None, local_ep_group=None, local_ep_group_ipv6=None):
        """UpdateVirtualGateway

        The model defined in huaweicloud sdk

        :param name: 更新虚拟网关的名字
        :type name: str
        :param description: 虚拟网关的描述信息
        :type description: str
        :param local_ep_group: 虚拟网关到访问云上服务IPv4子网列表，通常是vpc的cidrs
        :type local_ep_group: list[str]
        :param local_ep_group_ipv6: 虚拟网关到访问云上服务IPv6子网列表，通常是vpc的cidrs
        :type local_ep_group_ipv6: list[str]
        """
        
        

        self._name = None
        self._description = None
        self._local_ep_group = None
        self._local_ep_group_ipv6 = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if local_ep_group is not None:
            self.local_ep_group = local_ep_group
        if local_ep_group_ipv6 is not None:
            self.local_ep_group_ipv6 = local_ep_group_ipv6

    @property
    def name(self):
        """Gets the name of this UpdateVirtualGateway.

        更新虚拟网关的名字

        :return: The name of this UpdateVirtualGateway.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateVirtualGateway.

        更新虚拟网关的名字

        :param name: The name of this UpdateVirtualGateway.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateVirtualGateway.

        虚拟网关的描述信息

        :return: The description of this UpdateVirtualGateway.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateVirtualGateway.

        虚拟网关的描述信息

        :param description: The description of this UpdateVirtualGateway.
        :type description: str
        """
        self._description = description

    @property
    def local_ep_group(self):
        """Gets the local_ep_group of this UpdateVirtualGateway.

        虚拟网关到访问云上服务IPv4子网列表，通常是vpc的cidrs

        :return: The local_ep_group of this UpdateVirtualGateway.
        :rtype: list[str]
        """
        return self._local_ep_group

    @local_ep_group.setter
    def local_ep_group(self, local_ep_group):
        """Sets the local_ep_group of this UpdateVirtualGateway.

        虚拟网关到访问云上服务IPv4子网列表，通常是vpc的cidrs

        :param local_ep_group: The local_ep_group of this UpdateVirtualGateway.
        :type local_ep_group: list[str]
        """
        self._local_ep_group = local_ep_group

    @property
    def local_ep_group_ipv6(self):
        """Gets the local_ep_group_ipv6 of this UpdateVirtualGateway.

        虚拟网关到访问云上服务IPv6子网列表，通常是vpc的cidrs

        :return: The local_ep_group_ipv6 of this UpdateVirtualGateway.
        :rtype: list[str]
        """
        return self._local_ep_group_ipv6

    @local_ep_group_ipv6.setter
    def local_ep_group_ipv6(self, local_ep_group_ipv6):
        """Sets the local_ep_group_ipv6 of this UpdateVirtualGateway.

        虚拟网关到访问云上服务IPv6子网列表，通常是vpc的cidrs

        :param local_ep_group_ipv6: The local_ep_group_ipv6 of this UpdateVirtualGateway.
        :type local_ep_group_ipv6: list[str]
        """
        self._local_ep_group_ipv6 = local_ep_group_ipv6

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
        if not isinstance(other, UpdateVirtualGateway):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
