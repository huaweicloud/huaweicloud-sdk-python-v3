# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAllBucketsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'buckets': 'list[ObsBucket]'
    }

    attribute_map = {
        'buckets': 'buckets'
    }

    def __init__(self, buckets=None):
        """ListAllBucketsResponse

        The model defined in huaweicloud sdk

        :param buckets: 桶列表
        :type buckets: list[:class:`huaweicloudsdkmpc.v1.ObsBucket`]
        """
        
        super(ListAllBucketsResponse, self).__init__()

        self._buckets = None
        self.discriminator = None

        if buckets is not None:
            self.buckets = buckets

    @property
    def buckets(self):
        """Gets the buckets of this ListAllBucketsResponse.

        桶列表

        :return: The buckets of this ListAllBucketsResponse.
        :rtype: list[:class:`huaweicloudsdkmpc.v1.ObsBucket`]
        """
        return self._buckets

    @buckets.setter
    def buckets(self, buckets):
        """Sets the buckets of this ListAllBucketsResponse.

        桶列表

        :param buckets: The buckets of this ListAllBucketsResponse.
        :type buckets: list[:class:`huaweicloudsdkmpc.v1.ObsBucket`]
        """
        self._buckets = buckets

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
        if not isinstance(other, ListAllBucketsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
