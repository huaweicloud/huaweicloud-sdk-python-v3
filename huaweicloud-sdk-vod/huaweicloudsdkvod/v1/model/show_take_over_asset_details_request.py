# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTakeOverAssetDetailsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_bucket': 'str',
        'source_object': 'str'
    }

    attribute_map = {
        'source_bucket': 'source_bucket',
        'source_object': 'source_object'
    }

    def __init__(self, source_bucket=None, source_object=None):
        """ShowTakeOverAssetDetailsRequest

        The model defined in huaweicloud sdk

        :param source_bucket: 媒资原始输入存放的桶。
        :type source_bucket: str
        :param source_object: 媒资原始输入的objectKey。
        :type source_object: str
        """
        
        

        self._source_bucket = None
        self._source_object = None
        self.discriminator = None

        self.source_bucket = source_bucket
        self.source_object = source_object

    @property
    def source_bucket(self):
        """Gets the source_bucket of this ShowTakeOverAssetDetailsRequest.

        媒资原始输入存放的桶。

        :return: The source_bucket of this ShowTakeOverAssetDetailsRequest.
        :rtype: str
        """
        return self._source_bucket

    @source_bucket.setter
    def source_bucket(self, source_bucket):
        """Sets the source_bucket of this ShowTakeOverAssetDetailsRequest.

        媒资原始输入存放的桶。

        :param source_bucket: The source_bucket of this ShowTakeOverAssetDetailsRequest.
        :type source_bucket: str
        """
        self._source_bucket = source_bucket

    @property
    def source_object(self):
        """Gets the source_object of this ShowTakeOverAssetDetailsRequest.

        媒资原始输入的objectKey。

        :return: The source_object of this ShowTakeOverAssetDetailsRequest.
        :rtype: str
        """
        return self._source_object

    @source_object.setter
    def source_object(self, source_object):
        """Sets the source_object of this ShowTakeOverAssetDetailsRequest.

        媒资原始输入的objectKey。

        :param source_object: The source_object of this ShowTakeOverAssetDetailsRequest.
        :type source_object: str
        """
        self._source_object = source_object

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
        if not isinstance(other, ShowTakeOverAssetDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
