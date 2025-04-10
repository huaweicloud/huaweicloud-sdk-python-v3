# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'message': 'str',
        'subscription_urn': 'str'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'subscription_urn': 'subscription_urn'
    }

    def __init__(self, code=None, message=None, subscription_urn=None):
        r"""BatchResult

        The model defined in huaweicloud sdk

        :param code: 执行结果code
        :type code: str
        :param message: 执行结果message
        :type message: str
        :param subscription_urn: 订阅者urn
        :type subscription_urn: str
        """
        
        

        self._code = None
        self._message = None
        self._subscription_urn = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if subscription_urn is not None:
            self.subscription_urn = subscription_urn

    @property
    def code(self):
        r"""Gets the code of this BatchResult.

        执行结果code

        :return: The code of this BatchResult.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this BatchResult.

        执行结果code

        :param code: The code of this BatchResult.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        r"""Gets the message of this BatchResult.

        执行结果message

        :return: The message of this BatchResult.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this BatchResult.

        执行结果message

        :param message: The message of this BatchResult.
        :type message: str
        """
        self._message = message

    @property
    def subscription_urn(self):
        r"""Gets the subscription_urn of this BatchResult.

        订阅者urn

        :return: The subscription_urn of this BatchResult.
        :rtype: str
        """
        return self._subscription_urn

    @subscription_urn.setter
    def subscription_urn(self, subscription_urn):
        r"""Sets the subscription_urn of this BatchResult.

        订阅者urn

        :param subscription_urn: The subscription_urn of this BatchResult.
        :type subscription_urn: str
        """
        self._subscription_urn = subscription_urn

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
        if not isinstance(other, BatchResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
