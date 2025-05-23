# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConnectErrorInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'phone_id': 'str',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'phone_id': 'phone_id',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, phone_id=None, error_code=None, error_msg=None):
        r"""ConnectErrorInfo

        The model defined in huaweicloud sdk

        :param phone_id: 云手机的唯一标识ID。
        :type phone_id: str
        :param error_code: 错误码。
        :type error_code: str
        :param error_msg: 错误说明。
        :type error_msg: str
        """
        
        

        self._phone_id = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if phone_id is not None:
            self.phone_id = phone_id
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def phone_id(self):
        r"""Gets the phone_id of this ConnectErrorInfo.

        云手机的唯一标识ID。

        :return: The phone_id of this ConnectErrorInfo.
        :rtype: str
        """
        return self._phone_id

    @phone_id.setter
    def phone_id(self, phone_id):
        r"""Sets the phone_id of this ConnectErrorInfo.

        云手机的唯一标识ID。

        :param phone_id: The phone_id of this ConnectErrorInfo.
        :type phone_id: str
        """
        self._phone_id = phone_id

    @property
    def error_code(self):
        r"""Gets the error_code of this ConnectErrorInfo.

        错误码。

        :return: The error_code of this ConnectErrorInfo.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ConnectErrorInfo.

        错误码。

        :param error_code: The error_code of this ConnectErrorInfo.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this ConnectErrorInfo.

        错误说明。

        :return: The error_msg of this ConnectErrorInfo.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this ConnectErrorInfo.

        错误说明。

        :param error_msg: The error_msg of this ConnectErrorInfo.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, ConnectErrorInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
