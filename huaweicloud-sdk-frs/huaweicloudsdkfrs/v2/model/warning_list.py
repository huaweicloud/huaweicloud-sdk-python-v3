# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WarningList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'warning_code': 'int',
        'warning_msg': 'str'
    }

    attribute_map = {
        'warning_code': 'warningCode',
        'warning_msg': 'warningMsg'
    }

    def __init__(self, warning_code=None, warning_msg=None):
        r"""WarningList

        The model defined in huaweicloud sdk

        :param warning_code: 警告ID。
        :type warning_code: int
        :param warning_msg: 告警消息。
        :type warning_msg: str
        """
        
        

        self._warning_code = None
        self._warning_msg = None
        self.discriminator = None

        if warning_code is not None:
            self.warning_code = warning_code
        if warning_msg is not None:
            self.warning_msg = warning_msg

    @property
    def warning_code(self):
        r"""Gets the warning_code of this WarningList.

        警告ID。

        :return: The warning_code of this WarningList.
        :rtype: int
        """
        return self._warning_code

    @warning_code.setter
    def warning_code(self, warning_code):
        r"""Sets the warning_code of this WarningList.

        警告ID。

        :param warning_code: The warning_code of this WarningList.
        :type warning_code: int
        """
        self._warning_code = warning_code

    @property
    def warning_msg(self):
        r"""Gets the warning_msg of this WarningList.

        告警消息。

        :return: The warning_msg of this WarningList.
        :rtype: str
        """
        return self._warning_msg

    @warning_msg.setter
    def warning_msg(self, warning_msg):
        r"""Sets the warning_msg of this WarningList.

        告警消息。

        :param warning_msg: The warning_msg of this WarningList.
        :type warning_msg: str
        """
        self._warning_msg = warning_msg

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
        if not isinstance(other, WarningList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
