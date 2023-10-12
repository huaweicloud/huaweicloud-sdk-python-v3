# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckObsBucketsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'buckets': 'list[Bucket]'
    }

    attribute_map = {
        'buckets': 'buckets'
    }

    def __init__(self, buckets=None):
        """CheckObsBucketsResponse

        The model defined in huaweicloud sdk

        :param buckets: 检查OBS桶状态响应体。
        :type buckets: list[:class:`huaweicloudsdkcts.v3.Bucket`]
        """
        
        super(CheckObsBucketsResponse, self).__init__()

        self._buckets = None
        self.discriminator = None

        if buckets is not None:
            self.buckets = buckets

    @property
    def buckets(self):
        """Gets the buckets of this CheckObsBucketsResponse.

        检查OBS桶状态响应体。

        :return: The buckets of this CheckObsBucketsResponse.
        :rtype: list[:class:`huaweicloudsdkcts.v3.Bucket`]
        """
        return self._buckets

    @buckets.setter
    def buckets(self, buckets):
        """Sets the buckets of this CheckObsBucketsResponse.

        检查OBS桶状态响应体。

        :param buckets: The buckets of this CheckObsBucketsResponse.
        :type buckets: list[:class:`huaweicloudsdkcts.v3.Bucket`]
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
        if not isinstance(other, CheckObsBucketsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
