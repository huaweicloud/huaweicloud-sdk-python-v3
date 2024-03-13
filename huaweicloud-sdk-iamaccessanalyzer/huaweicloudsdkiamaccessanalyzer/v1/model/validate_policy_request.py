# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValidatePolicyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'x_language': 'str',
        'body': 'ValidatePolicyReqBody'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'x_language': 'X-Language',
        'body': 'body'
    }

    def __init__(self, limit=None, marker=None, x_language=None, body=None):
        """ValidatePolicyRequest

        The model defined in huaweicloud sdk

        :param limit: 单页最大结果数。
        :type limit: int
        :param marker: 页面标记。
        :type marker: str
        :param x_language: 返回消息的语言，默认值为&#39;zh-cn&#39;，表示中文。
        :type x_language: str
        :param body: Body of the ValidatePolicyRequest
        :type body: :class:`huaweicloudsdkiamaccessanalyzer.v1.ValidatePolicyReqBody`
        """
        
        

        self._limit = None
        self._marker = None
        self._x_language = None
        self._body = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if x_language is not None:
            self.x_language = x_language
        if body is not None:
            self.body = body

    @property
    def limit(self):
        """Gets the limit of this ValidatePolicyRequest.

        单页最大结果数。

        :return: The limit of this ValidatePolicyRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ValidatePolicyRequest.

        单页最大结果数。

        :param limit: The limit of this ValidatePolicyRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ValidatePolicyRequest.

        页面标记。

        :return: The marker of this ValidatePolicyRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ValidatePolicyRequest.

        页面标记。

        :param marker: The marker of this ValidatePolicyRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def x_language(self):
        """Gets the x_language of this ValidatePolicyRequest.

        返回消息的语言，默认值为'zh-cn'，表示中文。

        :return: The x_language of this ValidatePolicyRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ValidatePolicyRequest.

        返回消息的语言，默认值为'zh-cn'，表示中文。

        :param x_language: The x_language of this ValidatePolicyRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def body(self):
        """Gets the body of this ValidatePolicyRequest.

        :return: The body of this ValidatePolicyRequest.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.ValidatePolicyReqBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ValidatePolicyRequest.

        :param body: The body of this ValidatePolicyRequest.
        :type body: :class:`huaweicloudsdkiamaccessanalyzer.v1.ValidatePolicyReqBody`
        """
        self._body = body

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
        if not isinstance(other, ValidatePolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
