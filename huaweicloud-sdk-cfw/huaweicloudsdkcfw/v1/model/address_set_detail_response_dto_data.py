# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddressSetDetailResponseDTOData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'address_set_type': 'int',
        'address_type': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'address_set_type': 'address_set_type',
        'address_type': 'address_type'
    }

    def __init__(self, id=None, name=None, description=None, address_set_type=None, address_type=None):
        r"""AddressSetDetailResponseDTOData

        The model defined in huaweicloud sdk

        :param id: 地址组id
        :type id: str
        :param name: 地址组名称
        :type name: str
        :param description: 地址组描述
        :type description: str
        :param address_set_type: 地址组类型，0表示自定义地址组，1表示WAF回源IP地址组，2表示DDoS回源IP地址组，3表示NAT64转换地址组
        :type address_set_type: int
        :param address_type: 地址类型0 ipv4，1 ipv6
        :type address_type: int
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._address_set_type = None
        self._address_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if address_set_type is not None:
            self.address_set_type = address_set_type
        if address_type is not None:
            self.address_type = address_type

    @property
    def id(self):
        r"""Gets the id of this AddressSetDetailResponseDTOData.

        地址组id

        :return: The id of this AddressSetDetailResponseDTOData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AddressSetDetailResponseDTOData.

        地址组id

        :param id: The id of this AddressSetDetailResponseDTOData.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this AddressSetDetailResponseDTOData.

        地址组名称

        :return: The name of this AddressSetDetailResponseDTOData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AddressSetDetailResponseDTOData.

        地址组名称

        :param name: The name of this AddressSetDetailResponseDTOData.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this AddressSetDetailResponseDTOData.

        地址组描述

        :return: The description of this AddressSetDetailResponseDTOData.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AddressSetDetailResponseDTOData.

        地址组描述

        :param description: The description of this AddressSetDetailResponseDTOData.
        :type description: str
        """
        self._description = description

    @property
    def address_set_type(self):
        r"""Gets the address_set_type of this AddressSetDetailResponseDTOData.

        地址组类型，0表示自定义地址组，1表示WAF回源IP地址组，2表示DDoS回源IP地址组，3表示NAT64转换地址组

        :return: The address_set_type of this AddressSetDetailResponseDTOData.
        :rtype: int
        """
        return self._address_set_type

    @address_set_type.setter
    def address_set_type(self, address_set_type):
        r"""Sets the address_set_type of this AddressSetDetailResponseDTOData.

        地址组类型，0表示自定义地址组，1表示WAF回源IP地址组，2表示DDoS回源IP地址组，3表示NAT64转换地址组

        :param address_set_type: The address_set_type of this AddressSetDetailResponseDTOData.
        :type address_set_type: int
        """
        self._address_set_type = address_set_type

    @property
    def address_type(self):
        r"""Gets the address_type of this AddressSetDetailResponseDTOData.

        地址类型0 ipv4，1 ipv6

        :return: The address_type of this AddressSetDetailResponseDTOData.
        :rtype: int
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        r"""Sets the address_type of this AddressSetDetailResponseDTOData.

        地址类型0 ipv4，1 ipv6

        :param address_type: The address_type of this AddressSetDetailResponseDTOData.
        :type address_type: int
        """
        self._address_type = address_type

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
        if not isinstance(other, AddressSetDetailResponseDTOData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
