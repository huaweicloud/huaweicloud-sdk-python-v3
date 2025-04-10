# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CaptureRuleAddressDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'address': 'str',
        'address_type': 'int',
        'type': 'int'
    }

    attribute_map = {
        'address': 'address',
        'address_type': 'address_type',
        'type': 'type'
    }

    def __init__(self, address=None, address_type=None, type=None):
        r"""CaptureRuleAddressDto

        The model defined in huaweicloud sdk

        :param address: 地址
        :type address: str
        :param address_type: 目的地址类型0 ipv4，1 ipv6
        :type address_type: int
        :param type: 输入地址类型，目前只支持0，手工输入类型
        :type type: int
        """
        
        

        self._address = None
        self._address_type = None
        self._type = None
        self.discriminator = None

        self.address = address
        self.address_type = address_type
        self.type = type

    @property
    def address(self):
        r"""Gets the address of this CaptureRuleAddressDto.

        地址

        :return: The address of this CaptureRuleAddressDto.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this CaptureRuleAddressDto.

        地址

        :param address: The address of this CaptureRuleAddressDto.
        :type address: str
        """
        self._address = address

    @property
    def address_type(self):
        r"""Gets the address_type of this CaptureRuleAddressDto.

        目的地址类型0 ipv4，1 ipv6

        :return: The address_type of this CaptureRuleAddressDto.
        :rtype: int
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        r"""Sets the address_type of this CaptureRuleAddressDto.

        目的地址类型0 ipv4，1 ipv6

        :param address_type: The address_type of this CaptureRuleAddressDto.
        :type address_type: int
        """
        self._address_type = address_type

    @property
    def type(self):
        r"""Gets the type of this CaptureRuleAddressDto.

        输入地址类型，目前只支持0，手工输入类型

        :return: The type of this CaptureRuleAddressDto.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CaptureRuleAddressDto.

        输入地址类型，目前只支持0，手工输入类型

        :param type: The type of this CaptureRuleAddressDto.
        :type type: int
        """
        self._type = type

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
        if not isinstance(other, CaptureRuleAddressDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
