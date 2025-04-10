# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OnError:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error': 'str',
        'transition': 'str',
        'retry_ref': 'str'
    }

    attribute_map = {
        'error': 'error',
        'transition': 'transition',
        'retry_ref': 'retry_ref'
    }

    def __init__(self, error=None, transition=None, retry_ref=None):
        r"""OnError

        The model defined in huaweicloud sdk

        :param error: 错误匹配表达式，用来过滤需要处理的异常
        :type error: str
        :param transition: 下一步骤节点ID
        :type transition: str
        :param retry_ref: 重试策略名称
        :type retry_ref: str
        """
        
        

        self._error = None
        self._transition = None
        self._retry_ref = None
        self.discriminator = None

        if error is not None:
            self.error = error
        if transition is not None:
            self.transition = transition
        if retry_ref is not None:
            self.retry_ref = retry_ref

    @property
    def error(self):
        r"""Gets the error of this OnError.

        错误匹配表达式，用来过滤需要处理的异常

        :return: The error of this OnError.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        r"""Sets the error of this OnError.

        错误匹配表达式，用来过滤需要处理的异常

        :param error: The error of this OnError.
        :type error: str
        """
        self._error = error

    @property
    def transition(self):
        r"""Gets the transition of this OnError.

        下一步骤节点ID

        :return: The transition of this OnError.
        :rtype: str
        """
        return self._transition

    @transition.setter
    def transition(self, transition):
        r"""Sets the transition of this OnError.

        下一步骤节点ID

        :param transition: The transition of this OnError.
        :type transition: str
        """
        self._transition = transition

    @property
    def retry_ref(self):
        r"""Gets the retry_ref of this OnError.

        重试策略名称

        :return: The retry_ref of this OnError.
        :rtype: str
        """
        return self._retry_ref

    @retry_ref.setter
    def retry_ref(self, retry_ref):
        r"""Sets the retry_ref of this OnError.

        重试策略名称

        :param retry_ref: The retry_ref of this OnError.
        :type retry_ref: str
        """
        self._retry_ref = retry_ref

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
        if not isinstance(other, OnError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
