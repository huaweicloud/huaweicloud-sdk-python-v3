# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListObsBucketsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'buckets': 'list[ObsBucket]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'count': 'count',
        'buckets': 'buckets',
        'x_request_id': 'X-request-Id'
    }

    def __init__(self, count=None, buckets=None, x_request_id=None):
        r"""ListObsBucketsResponse

        The model defined in huaweicloud sdk

        :param count: 桶的总数
        :type count: int
        :param buckets: 桶信息
        :type buckets: list[:class:`huaweicloudsdkcloudrtc.v2.ObsBucket`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListObsBucketsResponse, self).__init__()

        self._count = None
        self._buckets = None
        self._x_request_id = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if buckets is not None:
            self.buckets = buckets
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def count(self):
        r"""Gets the count of this ListObsBucketsResponse.

        桶的总数

        :return: The count of this ListObsBucketsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListObsBucketsResponse.

        桶的总数

        :param count: The count of this ListObsBucketsResponse.
        :type count: int
        """
        self._count = count

    @property
    def buckets(self):
        r"""Gets the buckets of this ListObsBucketsResponse.

        桶信息

        :return: The buckets of this ListObsBucketsResponse.
        :rtype: list[:class:`huaweicloudsdkcloudrtc.v2.ObsBucket`]
        """
        return self._buckets

    @buckets.setter
    def buckets(self, buckets):
        r"""Sets the buckets of this ListObsBucketsResponse.

        桶信息

        :param buckets: The buckets of this ListObsBucketsResponse.
        :type buckets: list[:class:`huaweicloudsdkcloudrtc.v2.ObsBucket`]
        """
        self._buckets = buckets

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListObsBucketsResponse.

        :return: The x_request_id of this ListObsBucketsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListObsBucketsResponse.

        :param x_request_id: The x_request_id of this ListObsBucketsResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListObsBucketsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
