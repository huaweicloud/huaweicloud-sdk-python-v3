# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExceptionResponseSum:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'failed_assert': 'int',
        'failed_others': 'int',
        'failed_parsed': 'int',
        'failed_refused': 'int',
        'failed_timeout': 'int'
    }

    attribute_map = {
        'failed_assert': 'failed_assert',
        'failed_others': 'failed_others',
        'failed_parsed': 'failed_parsed',
        'failed_refused': 'failed_refused',
        'failed_timeout': 'failed_timeout'
    }

    def __init__(self, failed_assert=None, failed_others=None, failed_parsed=None, failed_refused=None, failed_timeout=None):
        r"""ExceptionResponseSum

        The model defined in huaweicloud sdk

        :param failed_assert: 断言失败数
        :type failed_assert: int
        :param failed_others: 其他错误失败数
        :type failed_others: int
        :param failed_parsed: 解析失败数
        :type failed_parsed: int
        :param failed_refused: 连接被拒绝失败数
        :type failed_refused: int
        :param failed_timeout: 响应超时失败数
        :type failed_timeout: int
        """
        
        

        self._failed_assert = None
        self._failed_others = None
        self._failed_parsed = None
        self._failed_refused = None
        self._failed_timeout = None
        self.discriminator = None

        if failed_assert is not None:
            self.failed_assert = failed_assert
        if failed_others is not None:
            self.failed_others = failed_others
        if failed_parsed is not None:
            self.failed_parsed = failed_parsed
        if failed_refused is not None:
            self.failed_refused = failed_refused
        if failed_timeout is not None:
            self.failed_timeout = failed_timeout

    @property
    def failed_assert(self):
        r"""Gets the failed_assert of this ExceptionResponseSum.

        断言失败数

        :return: The failed_assert of this ExceptionResponseSum.
        :rtype: int
        """
        return self._failed_assert

    @failed_assert.setter
    def failed_assert(self, failed_assert):
        r"""Sets the failed_assert of this ExceptionResponseSum.

        断言失败数

        :param failed_assert: The failed_assert of this ExceptionResponseSum.
        :type failed_assert: int
        """
        self._failed_assert = failed_assert

    @property
    def failed_others(self):
        r"""Gets the failed_others of this ExceptionResponseSum.

        其他错误失败数

        :return: The failed_others of this ExceptionResponseSum.
        :rtype: int
        """
        return self._failed_others

    @failed_others.setter
    def failed_others(self, failed_others):
        r"""Sets the failed_others of this ExceptionResponseSum.

        其他错误失败数

        :param failed_others: The failed_others of this ExceptionResponseSum.
        :type failed_others: int
        """
        self._failed_others = failed_others

    @property
    def failed_parsed(self):
        r"""Gets the failed_parsed of this ExceptionResponseSum.

        解析失败数

        :return: The failed_parsed of this ExceptionResponseSum.
        :rtype: int
        """
        return self._failed_parsed

    @failed_parsed.setter
    def failed_parsed(self, failed_parsed):
        r"""Sets the failed_parsed of this ExceptionResponseSum.

        解析失败数

        :param failed_parsed: The failed_parsed of this ExceptionResponseSum.
        :type failed_parsed: int
        """
        self._failed_parsed = failed_parsed

    @property
    def failed_refused(self):
        r"""Gets the failed_refused of this ExceptionResponseSum.

        连接被拒绝失败数

        :return: The failed_refused of this ExceptionResponseSum.
        :rtype: int
        """
        return self._failed_refused

    @failed_refused.setter
    def failed_refused(self, failed_refused):
        r"""Sets the failed_refused of this ExceptionResponseSum.

        连接被拒绝失败数

        :param failed_refused: The failed_refused of this ExceptionResponseSum.
        :type failed_refused: int
        """
        self._failed_refused = failed_refused

    @property
    def failed_timeout(self):
        r"""Gets the failed_timeout of this ExceptionResponseSum.

        响应超时失败数

        :return: The failed_timeout of this ExceptionResponseSum.
        :rtype: int
        """
        return self._failed_timeout

    @failed_timeout.setter
    def failed_timeout(self, failed_timeout):
        r"""Sets the failed_timeout of this ExceptionResponseSum.

        响应超时失败数

        :param failed_timeout: The failed_timeout of this ExceptionResponseSum.
        :type failed_timeout: int
        """
        self._failed_timeout = failed_timeout

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
        if not isinstance(other, ExceptionResponseSum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
