# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportIpInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'number': 'str',
        'ip_address': 'str',
        'subnet_mask': 'str',
        'error_code': 'str'
    }

    attribute_map = {
        'number': 'number',
        'ip_address': 'ip_address',
        'subnet_mask': 'subnet_mask',
        'error_code': 'error_code'
    }

    def __init__(self, number=None, ip_address=None, subnet_mask=None, error_code=None):
        r"""ImportIpInfo

        The model defined in huaweicloud sdk

        :param number: 编号。
        :type number: str
        :param ip_address: ip地址。
        :type ip_address: str
        :param subnet_mask: 子网掩码。
        :type subnet_mask: str
        :param error_code: 错误码。
        :type error_code: str
        """
        
        

        self._number = None
        self._ip_address = None
        self._subnet_mask = None
        self._error_code = None
        self.discriminator = None

        if number is not None:
            self.number = number
        if ip_address is not None:
            self.ip_address = ip_address
        if subnet_mask is not None:
            self.subnet_mask = subnet_mask
        if error_code is not None:
            self.error_code = error_code

    @property
    def number(self):
        r"""Gets the number of this ImportIpInfo.

        编号。

        :return: The number of this ImportIpInfo.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this ImportIpInfo.

        编号。

        :param number: The number of this ImportIpInfo.
        :type number: str
        """
        self._number = number

    @property
    def ip_address(self):
        r"""Gets the ip_address of this ImportIpInfo.

        ip地址。

        :return: The ip_address of this ImportIpInfo.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        r"""Sets the ip_address of this ImportIpInfo.

        ip地址。

        :param ip_address: The ip_address of this ImportIpInfo.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def subnet_mask(self):
        r"""Gets the subnet_mask of this ImportIpInfo.

        子网掩码。

        :return: The subnet_mask of this ImportIpInfo.
        :rtype: str
        """
        return self._subnet_mask

    @subnet_mask.setter
    def subnet_mask(self, subnet_mask):
        r"""Sets the subnet_mask of this ImportIpInfo.

        子网掩码。

        :param subnet_mask: The subnet_mask of this ImportIpInfo.
        :type subnet_mask: str
        """
        self._subnet_mask = subnet_mask

    @property
    def error_code(self):
        r"""Gets the error_code of this ImportIpInfo.

        错误码。

        :return: The error_code of this ImportIpInfo.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ImportIpInfo.

        错误码。

        :param error_code: The error_code of this ImportIpInfo.
        :type error_code: str
        """
        self._error_code = error_code

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ImportIpInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
