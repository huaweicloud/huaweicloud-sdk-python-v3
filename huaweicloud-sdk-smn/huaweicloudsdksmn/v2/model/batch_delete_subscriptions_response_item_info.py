# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteSubscriptionsResponseItemInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'http_code': 'int',
        'code': 'str',
        'message': 'str'
    }

    attribute_map = {
        'request_id': 'request_id',
        'http_code': 'http_code',
        'code': 'code',
        'message': 'message'
    }

    def __init__(self, request_id=None, http_code=None, code=None, message=None):
        r"""BatchDeleteSubscriptionsResponseItemInfo

        The model defined in huaweicloud sdk

        :param request_id: 请求的唯一标识ID。
        :type request_id: str
        :param http_code: 返回码。
        :type http_code: int
        :param code: 服务异常错误信息编码。
        :type code: str
        :param message: 服务异常错误信息描述。
        :type message: str
        """
        
        

        self._request_id = None
        self._http_code = None
        self._code = None
        self._message = None
        self.discriminator = None

        self.request_id = request_id
        self.http_code = http_code
        if code is not None:
            self.code = code
        if message is not None:
            self.message = message

    @property
    def request_id(self):
        r"""Gets the request_id of this BatchDeleteSubscriptionsResponseItemInfo.

        请求的唯一标识ID。

        :return: The request_id of this BatchDeleteSubscriptionsResponseItemInfo.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this BatchDeleteSubscriptionsResponseItemInfo.

        请求的唯一标识ID。

        :param request_id: The request_id of this BatchDeleteSubscriptionsResponseItemInfo.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def http_code(self):
        r"""Gets the http_code of this BatchDeleteSubscriptionsResponseItemInfo.

        返回码。

        :return: The http_code of this BatchDeleteSubscriptionsResponseItemInfo.
        :rtype: int
        """
        return self._http_code

    @http_code.setter
    def http_code(self, http_code):
        r"""Sets the http_code of this BatchDeleteSubscriptionsResponseItemInfo.

        返回码。

        :param http_code: The http_code of this BatchDeleteSubscriptionsResponseItemInfo.
        :type http_code: int
        """
        self._http_code = http_code

    @property
    def code(self):
        r"""Gets the code of this BatchDeleteSubscriptionsResponseItemInfo.

        服务异常错误信息编码。

        :return: The code of this BatchDeleteSubscriptionsResponseItemInfo.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this BatchDeleteSubscriptionsResponseItemInfo.

        服务异常错误信息编码。

        :param code: The code of this BatchDeleteSubscriptionsResponseItemInfo.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        r"""Gets the message of this BatchDeleteSubscriptionsResponseItemInfo.

        服务异常错误信息描述。

        :return: The message of this BatchDeleteSubscriptionsResponseItemInfo.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this BatchDeleteSubscriptionsResponseItemInfo.

        服务异常错误信息描述。

        :param message: The message of this BatchDeleteSubscriptionsResponseItemInfo.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, BatchDeleteSubscriptionsResponseItemInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
