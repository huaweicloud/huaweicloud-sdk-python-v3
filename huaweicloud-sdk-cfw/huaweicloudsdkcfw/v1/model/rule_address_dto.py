# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleAddressDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'int',
        'address_type': 'int',
        'address': 'str',
        'address_set_id': 'str',
        'address_set_name': 'str',
        'domain_address_name': 'str'
    }

    attribute_map = {
        'type': 'type',
        'address_type': 'address_type',
        'address': 'address',
        'address_set_id': 'address_set_id',
        'address_set_name': 'address_set_name',
        'domain_address_name': 'domain_address_name'
    }

    def __init__(self, type=None, address_type=None, address=None, address_set_id=None, address_set_name=None, domain_address_name=None):
        """RuleAddressDto

        The model defined in huaweicloud sdk

        :param type: 源类型0手工输入,1关联IP地址组,2域名
        :type type: int
        :param address_type: 源类型0 ipv4,1 ipv6
        :type address_type: int
        :param address: 源IP，手动类型不能为空，自动及domain类型为空
        :type address: str
        :param address_set_id: 关联IP地址组ID，自动类型不能为空，手动类型合domain类型为空
        :type address_set_id: str
        :param address_set_name: 地址组名称
        :type address_set_name: str
        :param domain_address_name: 域名地址名称，域名类型时不能为空，手动类型及自动类型时为空
        :type domain_address_name: str
        """
        
        

        self._type = None
        self._address_type = None
        self._address = None
        self._address_set_id = None
        self._address_set_name = None
        self._domain_address_name = None
        self.discriminator = None

        self.type = type
        if address_type is not None:
            self.address_type = address_type
        if address is not None:
            self.address = address
        if address_set_id is not None:
            self.address_set_id = address_set_id
        if address_set_name is not None:
            self.address_set_name = address_set_name
        if domain_address_name is not None:
            self.domain_address_name = domain_address_name

    @property
    def type(self):
        """Gets the type of this RuleAddressDto.

        源类型0手工输入,1关联IP地址组,2域名

        :return: The type of this RuleAddressDto.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RuleAddressDto.

        源类型0手工输入,1关联IP地址组,2域名

        :param type: The type of this RuleAddressDto.
        :type type: int
        """
        self._type = type

    @property
    def address_type(self):
        """Gets the address_type of this RuleAddressDto.

        源类型0 ipv4,1 ipv6

        :return: The address_type of this RuleAddressDto.
        :rtype: int
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        """Sets the address_type of this RuleAddressDto.

        源类型0 ipv4,1 ipv6

        :param address_type: The address_type of this RuleAddressDto.
        :type address_type: int
        """
        self._address_type = address_type

    @property
    def address(self):
        """Gets the address of this RuleAddressDto.

        源IP，手动类型不能为空，自动及domain类型为空

        :return: The address of this RuleAddressDto.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this RuleAddressDto.

        源IP，手动类型不能为空，自动及domain类型为空

        :param address: The address of this RuleAddressDto.
        :type address: str
        """
        self._address = address

    @property
    def address_set_id(self):
        """Gets the address_set_id of this RuleAddressDto.

        关联IP地址组ID，自动类型不能为空，手动类型合domain类型为空

        :return: The address_set_id of this RuleAddressDto.
        :rtype: str
        """
        return self._address_set_id

    @address_set_id.setter
    def address_set_id(self, address_set_id):
        """Sets the address_set_id of this RuleAddressDto.

        关联IP地址组ID，自动类型不能为空，手动类型合domain类型为空

        :param address_set_id: The address_set_id of this RuleAddressDto.
        :type address_set_id: str
        """
        self._address_set_id = address_set_id

    @property
    def address_set_name(self):
        """Gets the address_set_name of this RuleAddressDto.

        地址组名称

        :return: The address_set_name of this RuleAddressDto.
        :rtype: str
        """
        return self._address_set_name

    @address_set_name.setter
    def address_set_name(self, address_set_name):
        """Sets the address_set_name of this RuleAddressDto.

        地址组名称

        :param address_set_name: The address_set_name of this RuleAddressDto.
        :type address_set_name: str
        """
        self._address_set_name = address_set_name

    @property
    def domain_address_name(self):
        """Gets the domain_address_name of this RuleAddressDto.

        域名地址名称，域名类型时不能为空，手动类型及自动类型时为空

        :return: The domain_address_name of this RuleAddressDto.
        :rtype: str
        """
        return self._domain_address_name

    @domain_address_name.setter
    def domain_address_name(self, domain_address_name):
        """Sets the domain_address_name of this RuleAddressDto.

        域名地址名称，域名类型时不能为空，手动类型及自动类型时为空

        :param domain_address_name: The domain_address_name of this RuleAddressDto.
        :type domain_address_name: str
        """
        self._domain_address_name = domain_address_name

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
        if not isinstance(other, RuleAddressDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
