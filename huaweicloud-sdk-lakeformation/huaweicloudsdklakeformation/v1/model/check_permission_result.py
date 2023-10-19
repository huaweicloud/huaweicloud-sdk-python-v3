# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckPermissionResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'check_result': 'bool',
        'error_message': 'str'
    }

    attribute_map = {
        'check_result': 'check_result',
        'error_message': 'error_message'
    }

    def __init__(self, check_result=None, error_message=None):
        """CheckPermissionResult

        The model defined in huaweicloud sdk

        :param check_result: 对应输入策略的检查结果
        :type check_result: bool
        :param error_message: 错误信息
        :type error_message: str
        """
        
        

        self._check_result = None
        self._error_message = None
        self.discriminator = None

        self.check_result = check_result
        if error_message is not None:
            self.error_message = error_message

    @property
    def check_result(self):
        """Gets the check_result of this CheckPermissionResult.

        对应输入策略的检查结果

        :return: The check_result of this CheckPermissionResult.
        :rtype: bool
        """
        return self._check_result

    @check_result.setter
    def check_result(self, check_result):
        """Sets the check_result of this CheckPermissionResult.

        对应输入策略的检查结果

        :param check_result: The check_result of this CheckPermissionResult.
        :type check_result: bool
        """
        self._check_result = check_result

    @property
    def error_message(self):
        """Gets the error_message of this CheckPermissionResult.

        错误信息

        :return: The error_message of this CheckPermissionResult.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this CheckPermissionResult.

        错误信息

        :param error_message: The error_message of this CheckPermissionResult.
        :type error_message: str
        """
        self._error_message = error_message

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
        if not isinstance(other, CheckPermissionResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
