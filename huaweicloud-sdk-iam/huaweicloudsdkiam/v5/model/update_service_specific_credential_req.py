# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateServiceSpecificCredentialReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'description': 'str'
    }

    attribute_map = {
        'status': 'status',
        'description': 'description'
    }

    def __init__(self, status=None, description=None):
        r"""UpdateServiceSpecificCredentialReq

        The model defined in huaweicloud sdk

        :param status: 凭证状态。不支持用户主动设置为 Expired（Expired 仅由系统在凭证过期时自动设置）。status和description至少指定一个。
        :type status: str
        :param description: 要设置的凭证描述。status和description至少指定一个，长度0-255，正则限制为^[^@#%&amp;&lt;&gt;\\\\\\$\\^\\*]*$
        :type description: str
        """
        
        

        self._status = None
        self._description = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if description is not None:
            self.description = description

    @property
    def status(self):
        r"""Gets the status of this UpdateServiceSpecificCredentialReq.

        凭证状态。不支持用户主动设置为 Expired（Expired 仅由系统在凭证过期时自动设置）。status和description至少指定一个。

        :return: The status of this UpdateServiceSpecificCredentialReq.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateServiceSpecificCredentialReq.

        凭证状态。不支持用户主动设置为 Expired（Expired 仅由系统在凭证过期时自动设置）。status和description至少指定一个。

        :param status: The status of this UpdateServiceSpecificCredentialReq.
        :type status: str
        """
        self._status = status

    @property
    def description(self):
        r"""Gets the description of this UpdateServiceSpecificCredentialReq.

        要设置的凭证描述。status和description至少指定一个，长度0-255，正则限制为^[^@#%&<>\\\\\\$\\^\\*]*$

        :return: The description of this UpdateServiceSpecificCredentialReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateServiceSpecificCredentialReq.

        要设置的凭证描述。status和description至少指定一个，长度0-255，正则限制为^[^@#%&<>\\\\\\$\\^\\*]*$

        :param description: The description of this UpdateServiceSpecificCredentialReq.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, UpdateServiceSpecificCredentialReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
