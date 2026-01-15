# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSubscriptionListsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'limit': 'int',
        'offset': 'int',
        'body': 'QuerySubscriptionsReq'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'limit': 'limit',
        'offset': 'offset',
        'body': 'body'
    }

    def __init__(self, x_language=None, limit=None, offset=None, body=None):
        r"""ShowSubscriptionListsRequest

        The model defined in huaweicloud sdk

        :param x_language: 请求语言类型。
        :type x_language: str
        :param limit: 查询返回记录的数量限制，默认为10。
        :type limit: int
        :param offset: 偏移量，表示查询该偏移量后面的记录，默认为0。
        :type offset: int
        :param body: Body of the ShowSubscriptionListsRequest
        :type body: :class:`huaweicloudsdkdrs.v5.QuerySubscriptionsReq`
        """
        
        

        self._x_language = None
        self._limit = None
        self._offset = None
        self._body = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if body is not None:
            self.body = body

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowSubscriptionListsRequest.

        请求语言类型。

        :return: The x_language of this ShowSubscriptionListsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowSubscriptionListsRequest.

        请求语言类型。

        :param x_language: The x_language of this ShowSubscriptionListsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def limit(self):
        r"""Gets the limit of this ShowSubscriptionListsRequest.

        查询返回记录的数量限制，默认为10。

        :return: The limit of this ShowSubscriptionListsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowSubscriptionListsRequest.

        查询返回记录的数量限制，默认为10。

        :param limit: The limit of this ShowSubscriptionListsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowSubscriptionListsRequest.

        偏移量，表示查询该偏移量后面的记录，默认为0。

        :return: The offset of this ShowSubscriptionListsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowSubscriptionListsRequest.

        偏移量，表示查询该偏移量后面的记录，默认为0。

        :param offset: The offset of this ShowSubscriptionListsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def body(self):
        r"""Gets the body of this ShowSubscriptionListsRequest.

        :return: The body of this ShowSubscriptionListsRequest.
        :rtype: :class:`huaweicloudsdkdrs.v5.QuerySubscriptionsReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ShowSubscriptionListsRequest.

        :param body: The body of this ShowSubscriptionListsRequest.
        :type body: :class:`huaweicloudsdkdrs.v5.QuerySubscriptionsReq`
        """
        self._body = body

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowSubscriptionListsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
