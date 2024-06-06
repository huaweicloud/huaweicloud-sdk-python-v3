# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OBSBucket:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bucket_acl': 'str',
        'bucket_policy': 'str'
    }

    attribute_map = {
        'bucket_acl': 'bucket_acl',
        'bucket_policy': 'bucket_policy'
    }

    def __init__(self, bucket_acl=None, bucket_policy=None):
        """OBSBucket

        The model defined in huaweicloud sdk

        :param bucket_acl: 桶ACL xml文件的string格式。
        :type bucket_acl: str
        :param bucket_policy: 该策略JSON格式策略文档。
        :type bucket_policy: str
        """
        
        

        self._bucket_acl = None
        self._bucket_policy = None
        self.discriminator = None

        if bucket_acl is not None:
            self.bucket_acl = bucket_acl
        if bucket_policy is not None:
            self.bucket_policy = bucket_policy

    @property
    def bucket_acl(self):
        """Gets the bucket_acl of this OBSBucket.

        桶ACL xml文件的string格式。

        :return: The bucket_acl of this OBSBucket.
        :rtype: str
        """
        return self._bucket_acl

    @bucket_acl.setter
    def bucket_acl(self, bucket_acl):
        """Sets the bucket_acl of this OBSBucket.

        桶ACL xml文件的string格式。

        :param bucket_acl: The bucket_acl of this OBSBucket.
        :type bucket_acl: str
        """
        self._bucket_acl = bucket_acl

    @property
    def bucket_policy(self):
        """Gets the bucket_policy of this OBSBucket.

        该策略JSON格式策略文档。

        :return: The bucket_policy of this OBSBucket.
        :rtype: str
        """
        return self._bucket_policy

    @bucket_policy.setter
    def bucket_policy(self, bucket_policy):
        """Sets the bucket_policy of this OBSBucket.

        该策略JSON格式策略文档。

        :param bucket_policy: The bucket_policy of this OBSBucket.
        :type bucket_policy: str
        """
        self._bucket_policy = bucket_policy

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
        if not isinstance(other, OBSBucket):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
