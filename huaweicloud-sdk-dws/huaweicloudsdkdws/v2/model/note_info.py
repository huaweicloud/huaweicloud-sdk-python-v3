# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NoteInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bucket_split_info': 'BucketSplitInfo'
    }

    attribute_map = {
        'bucket_split_info': 'bucket_split_info'
    }

    def __init__(self, bucket_split_info=None):
        r"""NoteInfo

        The model defined in huaweicloud sdk

        :param bucket_split_info: 
        :type bucket_split_info: :class:`huaweicloudsdkdws.v2.BucketSplitInfo`
        """
        
        

        self._bucket_split_info = None
        self.discriminator = None

        if bucket_split_info is not None:
            self.bucket_split_info = bucket_split_info

    @property
    def bucket_split_info(self):
        r"""Gets the bucket_split_info of this NoteInfo.

        :return: The bucket_split_info of this NoteInfo.
        :rtype: :class:`huaweicloudsdkdws.v2.BucketSplitInfo`
        """
        return self._bucket_split_info

    @bucket_split_info.setter
    def bucket_split_info(self, bucket_split_info):
        r"""Sets the bucket_split_info of this NoteInfo.

        :param bucket_split_info: The bucket_split_info of this NoteInfo.
        :type bucket_split_info: :class:`huaweicloudsdkdws.v2.BucketSplitInfo`
        """
        self._bucket_split_info = bucket_split_info

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
        if not isinstance(other, NoteInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
