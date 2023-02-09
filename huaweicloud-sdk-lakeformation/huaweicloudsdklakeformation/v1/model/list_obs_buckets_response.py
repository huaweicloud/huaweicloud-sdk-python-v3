# coding: utf-8

import re
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
        'buckets': 'list[BucketDetail]',
        'total': 'int',
        'x_request_id': 'str'
    }

    attribute_map = {
        'buckets': 'buckets',
        'total': 'total',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, buckets=None, total=None, x_request_id=None):
        """ListObsBucketsResponse

        The model defined in huaweicloud sdk

        :param buckets: obs桶列表
        :type buckets: list[:class:`huaweicloudsdklakeformation.v1.BucketDetail`]
        :param total: obs桶总数
        :type total: int
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListObsBucketsResponse, self).__init__()

        self._buckets = None
        self._total = None
        self._x_request_id = None
        self.discriminator = None

        if buckets is not None:
            self.buckets = buckets
        if total is not None:
            self.total = total
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def buckets(self):
        """Gets the buckets of this ListObsBucketsResponse.

        obs桶列表

        :return: The buckets of this ListObsBucketsResponse.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.BucketDetail`]
        """
        return self._buckets

    @buckets.setter
    def buckets(self, buckets):
        """Sets the buckets of this ListObsBucketsResponse.

        obs桶列表

        :param buckets: The buckets of this ListObsBucketsResponse.
        :type buckets: list[:class:`huaweicloudsdklakeformation.v1.BucketDetail`]
        """
        self._buckets = buckets

    @property
    def total(self):
        """Gets the total of this ListObsBucketsResponse.

        obs桶总数

        :return: The total of this ListObsBucketsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListObsBucketsResponse.

        obs桶总数

        :param total: The total of this ListObsBucketsResponse.
        :type total: int
        """
        self._total = total

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ListObsBucketsResponse.

        :return: The x_request_id of this ListObsBucketsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ListObsBucketsResponse.

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
