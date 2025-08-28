# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVirtualMfaDeviceReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'virtual_mfa_device_name': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'virtual_mfa_device_name': 'virtual_mfa_device_name',
        'user_id': 'user_id'
    }

    def __init__(self, virtual_mfa_device_name=None, user_id=None):
        r"""CreateVirtualMfaDeviceReqBody

        The model defined in huaweicloud sdk

        :param virtual_mfa_device_name: MFA设备名称，长度为1到64个字符，只包含字母、数字、\&quot;_\&quot;和\&quot;-\&quot;的字符串。
        :type virtual_mfa_device_name: str
        :param user_id: IAM用户ID。
        :type user_id: str
        """
        
        

        self._virtual_mfa_device_name = None
        self._user_id = None
        self.discriminator = None

        self.virtual_mfa_device_name = virtual_mfa_device_name
        self.user_id = user_id

    @property
    def virtual_mfa_device_name(self):
        r"""Gets the virtual_mfa_device_name of this CreateVirtualMfaDeviceReqBody.

        MFA设备名称，长度为1到64个字符，只包含字母、数字、\"_\"和\"-\"的字符串。

        :return: The virtual_mfa_device_name of this CreateVirtualMfaDeviceReqBody.
        :rtype: str
        """
        return self._virtual_mfa_device_name

    @virtual_mfa_device_name.setter
    def virtual_mfa_device_name(self, virtual_mfa_device_name):
        r"""Sets the virtual_mfa_device_name of this CreateVirtualMfaDeviceReqBody.

        MFA设备名称，长度为1到64个字符，只包含字母、数字、\"_\"和\"-\"的字符串。

        :param virtual_mfa_device_name: The virtual_mfa_device_name of this CreateVirtualMfaDeviceReqBody.
        :type virtual_mfa_device_name: str
        """
        self._virtual_mfa_device_name = virtual_mfa_device_name

    @property
    def user_id(self):
        r"""Gets the user_id of this CreateVirtualMfaDeviceReqBody.

        IAM用户ID。

        :return: The user_id of this CreateVirtualMfaDeviceReqBody.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this CreateVirtualMfaDeviceReqBody.

        IAM用户ID。

        :param user_id: The user_id of this CreateVirtualMfaDeviceReqBody.
        :type user_id: str
        """
        self._user_id = user_id

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
        if not isinstance(other, CreateVirtualMfaDeviceReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
