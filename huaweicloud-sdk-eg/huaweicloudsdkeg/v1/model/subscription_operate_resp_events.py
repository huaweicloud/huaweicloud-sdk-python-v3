# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubscriptionOperateRespEvents:

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
        'error_msg': 'str',
        'subscription_id': 'str'
    }

    attribute_map = {
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'subscription_id': 'subscription_id'
    }

    def __init__(self, error_code=None, error_msg=None, subscription_id=None):
        r"""SubscriptionOperateRespEvents

        The model defined in huaweicloud sdk

        :param error_code: 失败的错误码
        :type error_code: str
        :param error_msg: 失败的原因
        :type error_msg: str
        :param subscription_id: 订阅ID
        :type subscription_id: str
        """
        
        

        self._error_code = None
        self._error_msg = None
        self._subscription_id = None
        self.discriminator = None

        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if subscription_id is not None:
            self.subscription_id = subscription_id

    @property
    def error_code(self):
        r"""Gets the error_code of this SubscriptionOperateRespEvents.

        失败的错误码

        :return: The error_code of this SubscriptionOperateRespEvents.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this SubscriptionOperateRespEvents.

        失败的错误码

        :param error_code: The error_code of this SubscriptionOperateRespEvents.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this SubscriptionOperateRespEvents.

        失败的原因

        :return: The error_msg of this SubscriptionOperateRespEvents.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this SubscriptionOperateRespEvents.

        失败的原因

        :param error_msg: The error_msg of this SubscriptionOperateRespEvents.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def subscription_id(self):
        r"""Gets the subscription_id of this SubscriptionOperateRespEvents.

        订阅ID

        :return: The subscription_id of this SubscriptionOperateRespEvents.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        r"""Sets the subscription_id of this SubscriptionOperateRespEvents.

        订阅ID

        :param subscription_id: The subscription_id of this SubscriptionOperateRespEvents.
        :type subscription_id: str
        """
        self._subscription_id = subscription_id

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
        if not isinstance(other, SubscriptionOperateRespEvents):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
