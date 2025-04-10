# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourceSharesByTagsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('x_security_token')

    openapi_types = {
        'limit': 'int',
        'offset': 'str',
        'x_security_token': 'str',
        'body': 'ResourceSharesByTagsReqBody'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'x_security_token': 'X-Security-Token',
        'body': 'body'
    }

    def __init__(self, limit=None, offset=None, x_security_token=None, body=None):
        r"""ListResourceSharesByTagsRequest

        The model defined in huaweicloud sdk

        :param limit: 分页页面的最大值。
        :type limit: int
        :param offset: 分页标记。
        :type offset: str
        :param x_security_token: 如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。
        :type x_security_token: str
        :param body: Body of the ListResourceSharesByTagsRequest
        :type body: :class:`huaweicloudsdkram.v1.ResourceSharesByTagsReqBody`
        """
        
        

        self._limit = None
        self._offset = None
        self._x_security_token = None
        self._body = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if x_security_token is not None:
            self.x_security_token = x_security_token
        if body is not None:
            self.body = body

    @property
    def limit(self):
        r"""Gets the limit of this ListResourceSharesByTagsRequest.

        分页页面的最大值。

        :return: The limit of this ListResourceSharesByTagsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListResourceSharesByTagsRequest.

        分页页面的最大值。

        :param limit: The limit of this ListResourceSharesByTagsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListResourceSharesByTagsRequest.

        分页标记。

        :return: The offset of this ListResourceSharesByTagsRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListResourceSharesByTagsRequest.

        分页标记。

        :param offset: The offset of this ListResourceSharesByTagsRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def x_security_token(self):
        r"""Gets the x_security_token of this ListResourceSharesByTagsRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :return: The x_security_token of this ListResourceSharesByTagsRequest.
        :rtype: str
        """
        return self._x_security_token

    @x_security_token.setter
    def x_security_token(self, x_security_token):
        r"""Sets the x_security_token of this ListResourceSharesByTagsRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :param x_security_token: The x_security_token of this ListResourceSharesByTagsRequest.
        :type x_security_token: str
        """
        self._x_security_token = x_security_token

    @property
    def body(self):
        r"""Gets the body of this ListResourceSharesByTagsRequest.

        :return: The body of this ListResourceSharesByTagsRequest.
        :rtype: :class:`huaweicloudsdkram.v1.ResourceSharesByTagsReqBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ListResourceSharesByTagsRequest.

        :param body: The body of this ListResourceSharesByTagsRequest.
        :type body: :class:`huaweicloudsdkram.v1.ResourceSharesByTagsReqBody`
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
        if not isinstance(other, ListResourceSharesByTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
