# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EmailStatusInfo:

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
        'confirm_status': 'str'
    }

    attribute_map = {
        'address': 'address',
        'confirm_status': 'confirm_status'
    }

    def __init__(self, address=None, confirm_status=None):
        r"""EmailStatusInfo

        The model defined in huaweicloud sdk

        :param address: 邮箱地址
        :type address: str
        :param confirm_status: 邮箱状态，FINISH表示已通过校验；其他状态需要校验
        :type confirm_status: str
        """
        
        

        self._address = None
        self._confirm_status = None
        self.discriminator = None

        self.address = address
        self.confirm_status = confirm_status

    @property
    def address(self):
        r"""Gets the address of this EmailStatusInfo.

        邮箱地址

        :return: The address of this EmailStatusInfo.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this EmailStatusInfo.

        邮箱地址

        :param address: The address of this EmailStatusInfo.
        :type address: str
        """
        self._address = address

    @property
    def confirm_status(self):
        r"""Gets the confirm_status of this EmailStatusInfo.

        邮箱状态，FINISH表示已通过校验；其他状态需要校验

        :return: The confirm_status of this EmailStatusInfo.
        :rtype: str
        """
        return self._confirm_status

    @confirm_status.setter
    def confirm_status(self, confirm_status):
        r"""Sets the confirm_status of this EmailStatusInfo.

        邮箱状态，FINISH表示已通过校验；其他状态需要校验

        :param confirm_status: The confirm_status of this EmailStatusInfo.
        :type confirm_status: str
        """
        self._confirm_status = confirm_status

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
        if not isinstance(other, EmailStatusInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
