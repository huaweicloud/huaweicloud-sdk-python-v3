# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteMfaDeviceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_id': 'str',
        'serial_number': 'str'
    }

    attribute_map = {
        'user_id': 'user_id',
        'serial_number': 'serial_number'
    }

    def __init__(self, user_id=None, serial_number=None):
        r"""DeleteMfaDeviceRequest

        The model defined in huaweicloud sdk

        :param user_id: 绑定MFA设备的IAM 用户ID。
        :type user_id: str
        :param serial_number: MFA设备序列号。
        :type serial_number: str
        """
        
        

        self._user_id = None
        self._serial_number = None
        self.discriminator = None

        self.user_id = user_id
        self.serial_number = serial_number

    @property
    def user_id(self):
        r"""Gets the user_id of this DeleteMfaDeviceRequest.

        绑定MFA设备的IAM 用户ID。

        :return: The user_id of this DeleteMfaDeviceRequest.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this DeleteMfaDeviceRequest.

        绑定MFA设备的IAM 用户ID。

        :param user_id: The user_id of this DeleteMfaDeviceRequest.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def serial_number(self):
        r"""Gets the serial_number of this DeleteMfaDeviceRequest.

        MFA设备序列号。

        :return: The serial_number of this DeleteMfaDeviceRequest.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        r"""Sets the serial_number of this DeleteMfaDeviceRequest.

        MFA设备序列号。

        :param serial_number: The serial_number of this DeleteMfaDeviceRequest.
        :type serial_number: str
        """
        self._serial_number = serial_number

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
        if not isinstance(other, DeleteMfaDeviceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
