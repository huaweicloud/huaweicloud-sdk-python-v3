# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateConnectGateway:

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
        'address_family': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'address_family': 'address_family'
    }

    def __init__(self, name=None, description=None, address_family=None):
        r"""UpdateConnectGateway

        The model defined in huaweicloud sdk

        :param name: 网关名字
        :type name: str
        :param description: 描述信息
        :type description: str
        :param address_family: 地址族信息
        :type address_family: str
        """
        
        

        self._name = None
        self._description = None
        self._address_family = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if address_family is not None:
            self.address_family = address_family

    @property
    def name(self):
        r"""Gets the name of this UpdateConnectGateway.

        网关名字

        :return: The name of this UpdateConnectGateway.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateConnectGateway.

        网关名字

        :param name: The name of this UpdateConnectGateway.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateConnectGateway.

        描述信息

        :return: The description of this UpdateConnectGateway.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateConnectGateway.

        描述信息

        :param description: The description of this UpdateConnectGateway.
        :type description: str
        """
        self._description = description

    @property
    def address_family(self):
        r"""Gets the address_family of this UpdateConnectGateway.

        地址族信息

        :return: The address_family of this UpdateConnectGateway.
        :rtype: str
        """
        return self._address_family

    @address_family.setter
    def address_family(self, address_family):
        r"""Sets the address_family of this UpdateConnectGateway.

        地址族信息

        :param address_family: The address_family of this UpdateConnectGateway.
        :type address_family: str
        """
        self._address_family = address_family

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
        if not isinstance(other, UpdateConnectGateway):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
