# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UnreasonablePermission:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'str',
        'count': 'int'
    }

    attribute_map = {
        'result': 'result',
        'count': 'count'
    }

    def __init__(self, result=None, count=None):
        r"""UnreasonablePermission

        The model defined in huaweicloud sdk

        :param result: 检测结果 * NO_RISK 无风险 * MEDIUM_RISK 中风险 * HIGH_RISK 高风险 * NOT_SCANNED 未扫描
        :type result: str
        :param count: 存在风险的权限控制数量。
        :type count: int
        """
        
        

        self._result = None
        self._count = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if count is not None:
            self.count = count

    @property
    def result(self):
        r"""Gets the result of this UnreasonablePermission.

        检测结果 * NO_RISK 无风险 * MEDIUM_RISK 中风险 * HIGH_RISK 高风险 * NOT_SCANNED 未扫描

        :return: The result of this UnreasonablePermission.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this UnreasonablePermission.

        检测结果 * NO_RISK 无风险 * MEDIUM_RISK 中风险 * HIGH_RISK 高风险 * NOT_SCANNED 未扫描

        :param result: The result of this UnreasonablePermission.
        :type result: str
        """
        self._result = result

    @property
    def count(self):
        r"""Gets the count of this UnreasonablePermission.

        存在风险的权限控制数量。

        :return: The count of this UnreasonablePermission.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this UnreasonablePermission.

        存在风险的权限控制数量。

        :param count: The count of this UnreasonablePermission.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, UnreasonablePermission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
