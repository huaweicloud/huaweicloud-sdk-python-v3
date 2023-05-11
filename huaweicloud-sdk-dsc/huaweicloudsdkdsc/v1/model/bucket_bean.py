# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BucketBean:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_name': 'str',
        'location': 'str',
        'bucket_name': 'str',
        'bucket_policy': 'str'
    }

    attribute_map = {
        'asset_name': 'asset_name',
        'location': 'location',
        'bucket_name': 'bucket_name',
        'bucket_policy': 'bucket_policy'
    }

    def __init__(self, asset_name=None, location=None, bucket_name=None, bucket_policy=None):
        """BucketBean

        The model defined in huaweicloud sdk

        :param asset_name: 资产名称
        :type asset_name: str
        :param location: 桶位置
        :type location: str
        :param bucket_name: 桶名称
        :type bucket_name: str
        :param bucket_policy: 桶策略
        :type bucket_policy: str
        """
        
        

        self._asset_name = None
        self._location = None
        self._bucket_name = None
        self._bucket_policy = None
        self.discriminator = None

        if asset_name is not None:
            self.asset_name = asset_name
        if location is not None:
            self.location = location
        if bucket_name is not None:
            self.bucket_name = bucket_name
        if bucket_policy is not None:
            self.bucket_policy = bucket_policy

    @property
    def asset_name(self):
        """Gets the asset_name of this BucketBean.

        资产名称

        :return: The asset_name of this BucketBean.
        :rtype: str
        """
        return self._asset_name

    @asset_name.setter
    def asset_name(self, asset_name):
        """Sets the asset_name of this BucketBean.

        资产名称

        :param asset_name: The asset_name of this BucketBean.
        :type asset_name: str
        """
        self._asset_name = asset_name

    @property
    def location(self):
        """Gets the location of this BucketBean.

        桶位置

        :return: The location of this BucketBean.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this BucketBean.

        桶位置

        :param location: The location of this BucketBean.
        :type location: str
        """
        self._location = location

    @property
    def bucket_name(self):
        """Gets the bucket_name of this BucketBean.

        桶名称

        :return: The bucket_name of this BucketBean.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this BucketBean.

        桶名称

        :param bucket_name: The bucket_name of this BucketBean.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def bucket_policy(self):
        """Gets the bucket_policy of this BucketBean.

        桶策略

        :return: The bucket_policy of this BucketBean.
        :rtype: str
        """
        return self._bucket_policy

    @bucket_policy.setter
    def bucket_policy(self, bucket_policy):
        """Sets the bucket_policy of this BucketBean.

        桶策略

        :param bucket_policy: The bucket_policy of this BucketBean.
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
        if not isinstance(other, BucketBean):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
