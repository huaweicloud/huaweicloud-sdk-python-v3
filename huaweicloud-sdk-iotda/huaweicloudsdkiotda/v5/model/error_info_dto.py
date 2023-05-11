# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ErrorInfoDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, error_code=None, error_msg=None):
        """ErrorInfoDTO

        The model defined in huaweicloud sdk

        :param error_code: **参数说明**：异常信息错误码，包含IOTDA.014016和IOTDA.014112。IOTDA.014016表示设备不在线；IOTDA.014112表示设备没有订阅topic。
        :type error_code: str
        :param error_msg: **参数说明**：异常信息说明，包含设备不在线和设备没有订阅topic说明。
        :type error_msg: str
        """
        
        

        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def error_code(self):
        """Gets the error_code of this ErrorInfoDTO.

        **参数说明**：异常信息错误码，包含IOTDA.014016和IOTDA.014112。IOTDA.014016表示设备不在线；IOTDA.014112表示设备没有订阅topic。

        :return: The error_code of this ErrorInfoDTO.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ErrorInfoDTO.

        **参数说明**：异常信息错误码，包含IOTDA.014016和IOTDA.014112。IOTDA.014016表示设备不在线；IOTDA.014112表示设备没有订阅topic。

        :param error_code: The error_code of this ErrorInfoDTO.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this ErrorInfoDTO.

        **参数说明**：异常信息说明，包含设备不在线和设备没有订阅topic说明。

        :return: The error_msg of this ErrorInfoDTO.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this ErrorInfoDTO.

        **参数说明**：异常信息说明，包含设备不在线和设备没有订阅topic说明。

        :param error_msg: The error_msg of this ErrorInfoDTO.
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
        if not isinstance(other, ErrorInfoDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
