# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteBucketRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bucket_id': 'str'
    }

    attribute_map = {
        'bucket_id': 'bucket_id'
    }

    def __init__(self, bucket_id=None):
        r"""DeleteBucketRequest

        The model defined in huaweicloud sdk

        :param bucket_id: 桶ID
        :type bucket_id: str
        """
        
        

        self._bucket_id = None
        self.discriminator = None

        self.bucket_id = bucket_id

    @property
    def bucket_id(self):
        r"""Gets the bucket_id of this DeleteBucketRequest.

        桶ID

        :return: The bucket_id of this DeleteBucketRequest.
        :rtype: str
        """
        return self._bucket_id

    @bucket_id.setter
    def bucket_id(self, bucket_id):
        r"""Sets the bucket_id of this DeleteBucketRequest.

        桶ID

        :param bucket_id: The bucket_id of this DeleteBucketRequest.
        :type bucket_id: str
        """
        self._bucket_id = bucket_id

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
        if not isinstance(other, DeleteBucketRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
