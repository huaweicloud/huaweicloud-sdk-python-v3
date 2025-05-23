# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProtectionServerInfoBackupError:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_code': 'int',
        'error_description': 'str'
    }

    attribute_map = {
        'error_code': 'error_code',
        'error_description': 'error_description'
    }

    def __init__(self, error_code=None, error_description=None):
        r"""ProtectionServerInfoBackupError

        The model defined in huaweicloud sdk

        :param error_code: 错误编码，包含如下2种。   - 0 ：无错误信息。   - 1 ：已綁定至其它存储库，无法开启备份。   - 2 ：备份库已超过最大限额。   - 3 ：CBR接口调用异常。
        :type error_code: int
        :param error_description: 错误描述
        :type error_description: str
        """
        
        

        self._error_code = None
        self._error_description = None
        self.discriminator = None

        if error_code is not None:
            self.error_code = error_code
        if error_description is not None:
            self.error_description = error_description

    @property
    def error_code(self):
        r"""Gets the error_code of this ProtectionServerInfoBackupError.

        错误编码，包含如下2种。   - 0 ：无错误信息。   - 1 ：已綁定至其它存储库，无法开启备份。   - 2 ：备份库已超过最大限额。   - 3 ：CBR接口调用异常。

        :return: The error_code of this ProtectionServerInfoBackupError.
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ProtectionServerInfoBackupError.

        错误编码，包含如下2种。   - 0 ：无错误信息。   - 1 ：已綁定至其它存储库，无法开启备份。   - 2 ：备份库已超过最大限额。   - 3 ：CBR接口调用异常。

        :param error_code: The error_code of this ProtectionServerInfoBackupError.
        :type error_code: int
        """
        self._error_code = error_code

    @property
    def error_description(self):
        r"""Gets the error_description of this ProtectionServerInfoBackupError.

        错误描述

        :return: The error_description of this ProtectionServerInfoBackupError.
        :rtype: str
        """
        return self._error_description

    @error_description.setter
    def error_description(self, error_description):
        r"""Sets the error_description of this ProtectionServerInfoBackupError.

        错误描述

        :param error_description: The error_description of this ProtectionServerInfoBackupError.
        :type error_description: str
        """
        self._error_description = error_description

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
        if not isinstance(other, ProtectionServerInfoBackupError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
