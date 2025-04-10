# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddSubscriptionFromSubscriptionUserResponseItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'http_code': 'int',
        'request_id': 'str',
        'subscription_urn': 'str',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'http_code': 'http_code',
        'request_id': 'request_id',
        'subscription_urn': 'subscription_urn',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, http_code=None, request_id=None, subscription_urn=None, error_code=None, error_msg=None):
        r"""AddSubscriptionFromSubscriptionUserResponseItem

        The model defined in huaweicloud sdk

        :param http_code: 返回码。
        :type http_code: int
        :param request_id: 请求的唯一标识ID。
        :type request_id: str
        :param subscription_urn: 订阅者的唯一资源标识。
        :type subscription_urn: str
        :param error_code: 返回信息对应的代码。
        :type error_code: str
        :param error_msg: 服务异常错误信息描述。
        :type error_msg: str
        """
        
        

        self._http_code = None
        self._request_id = None
        self._subscription_urn = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        self.http_code = http_code
        self.request_id = request_id
        if subscription_urn is not None:
            self.subscription_urn = subscription_urn
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def http_code(self):
        r"""Gets the http_code of this AddSubscriptionFromSubscriptionUserResponseItem.

        返回码。

        :return: The http_code of this AddSubscriptionFromSubscriptionUserResponseItem.
        :rtype: int
        """
        return self._http_code

    @http_code.setter
    def http_code(self, http_code):
        r"""Sets the http_code of this AddSubscriptionFromSubscriptionUserResponseItem.

        返回码。

        :param http_code: The http_code of this AddSubscriptionFromSubscriptionUserResponseItem.
        :type http_code: int
        """
        self._http_code = http_code

    @property
    def request_id(self):
        r"""Gets the request_id of this AddSubscriptionFromSubscriptionUserResponseItem.

        请求的唯一标识ID。

        :return: The request_id of this AddSubscriptionFromSubscriptionUserResponseItem.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this AddSubscriptionFromSubscriptionUserResponseItem.

        请求的唯一标识ID。

        :param request_id: The request_id of this AddSubscriptionFromSubscriptionUserResponseItem.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def subscription_urn(self):
        r"""Gets the subscription_urn of this AddSubscriptionFromSubscriptionUserResponseItem.

        订阅者的唯一资源标识。

        :return: The subscription_urn of this AddSubscriptionFromSubscriptionUserResponseItem.
        :rtype: str
        """
        return self._subscription_urn

    @subscription_urn.setter
    def subscription_urn(self, subscription_urn):
        r"""Sets the subscription_urn of this AddSubscriptionFromSubscriptionUserResponseItem.

        订阅者的唯一资源标识。

        :param subscription_urn: The subscription_urn of this AddSubscriptionFromSubscriptionUserResponseItem.
        :type subscription_urn: str
        """
        self._subscription_urn = subscription_urn

    @property
    def error_code(self):
        r"""Gets the error_code of this AddSubscriptionFromSubscriptionUserResponseItem.

        返回信息对应的代码。

        :return: The error_code of this AddSubscriptionFromSubscriptionUserResponseItem.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this AddSubscriptionFromSubscriptionUserResponseItem.

        返回信息对应的代码。

        :param error_code: The error_code of this AddSubscriptionFromSubscriptionUserResponseItem.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this AddSubscriptionFromSubscriptionUserResponseItem.

        服务异常错误信息描述。

        :return: The error_msg of this AddSubscriptionFromSubscriptionUserResponseItem.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this AddSubscriptionFromSubscriptionUserResponseItem.

        服务异常错误信息描述。

        :param error_msg: The error_msg of this AddSubscriptionFromSubscriptionUserResponseItem.
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
        if not isinstance(other, AddSubscriptionFromSubscriptionUserResponseItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
