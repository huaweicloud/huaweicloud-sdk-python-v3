# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAndAuthorizeBucketResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bucket_name': 'str'
    }

    attribute_map = {
        'bucket_name': 'bucket_name'
    }

    def __init__(self, bucket_name=None):
        r"""CreateAndAuthorizeBucketResponse

        The model defined in huaweicloud sdk

        :param bucket_name: 桶名称。
        :type bucket_name: str
        """
        
        super(CreateAndAuthorizeBucketResponse, self).__init__()

        self._bucket_name = None
        self.discriminator = None

        if bucket_name is not None:
            self.bucket_name = bucket_name

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this CreateAndAuthorizeBucketResponse.

        桶名称。

        :return: The bucket_name of this CreateAndAuthorizeBucketResponse.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this CreateAndAuthorizeBucketResponse.

        桶名称。

        :param bucket_name: The bucket_name of this CreateAndAuthorizeBucketResponse.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

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
        if not isinstance(other, CreateAndAuthorizeBucketResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
