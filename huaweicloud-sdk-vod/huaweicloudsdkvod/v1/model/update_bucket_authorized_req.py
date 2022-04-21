# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateBucketAuthorizedReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bucket': 'str',
        'operation': 'str'
    }

    attribute_map = {
        'bucket': 'bucket',
        'operation': 'operation'
    }

    def __init__(self, bucket=None, operation=None):
        """UpdateBucketAuthorizedReq

        The model defined in huaweicloud sdk

        :param bucket: OBS桶名称。
        :type bucket: str
        :param operation: 是否进行桶授权。  取值如下： - 0：取消授权。 - 1：授权。
        :type operation: str
        """
        
        

        self._bucket = None
        self._operation = None
        self.discriminator = None

        self.bucket = bucket
        self.operation = operation

    @property
    def bucket(self):
        """Gets the bucket of this UpdateBucketAuthorizedReq.

        OBS桶名称。

        :return: The bucket of this UpdateBucketAuthorizedReq.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this UpdateBucketAuthorizedReq.

        OBS桶名称。

        :param bucket: The bucket of this UpdateBucketAuthorizedReq.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def operation(self):
        """Gets the operation of this UpdateBucketAuthorizedReq.

        是否进行桶授权。  取值如下： - 0：取消授权。 - 1：授权。

        :return: The operation of this UpdateBucketAuthorizedReq.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this UpdateBucketAuthorizedReq.

        是否进行桶授权。  取值如下： - 0：取消授权。 - 1：授权。

        :param operation: The operation of this UpdateBucketAuthorizedReq.
        :type operation: str
        """
        self._operation = operation

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
        if not isinstance(other, UpdateBucketAuthorizedReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
