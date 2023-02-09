# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListObsObjectResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_names': 'list[str]',
        'location': 'str',
        'prefix': 'str',
        'bucket_name': 'str',
        'next_marker': 'str'
    }

    attribute_map = {
        'object_names': 'object_names',
        'location': 'location',
        'prefix': 'prefix',
        'bucket_name': 'bucket_name',
        'next_marker': 'next_marker'
    }

    def __init__(self, object_names=None, location=None, prefix=None, bucket_name=None, next_marker=None):
        """ListObsObjectResponse

        The model defined in huaweicloud sdk

        :param object_names: object名称列表
        :type object_names: list[str]
        :param location: region编码
        :type location: str
        :param prefix: 搜索前缀
        :type prefix: str
        :param bucket_name: obs桶名
        :type bucket_name: str
        :param next_marker: 下一个object起始位置
        :type next_marker: str
        """
        
        super(ListObsObjectResponse, self).__init__()

        self._object_names = None
        self._location = None
        self._prefix = None
        self._bucket_name = None
        self._next_marker = None
        self.discriminator = None

        if object_names is not None:
            self.object_names = object_names
        if location is not None:
            self.location = location
        if prefix is not None:
            self.prefix = prefix
        if bucket_name is not None:
            self.bucket_name = bucket_name
        if next_marker is not None:
            self.next_marker = next_marker

    @property
    def object_names(self):
        """Gets the object_names of this ListObsObjectResponse.

        object名称列表

        :return: The object_names of this ListObsObjectResponse.
        :rtype: list[str]
        """
        return self._object_names

    @object_names.setter
    def object_names(self, object_names):
        """Sets the object_names of this ListObsObjectResponse.

        object名称列表

        :param object_names: The object_names of this ListObsObjectResponse.
        :type object_names: list[str]
        """
        self._object_names = object_names

    @property
    def location(self):
        """Gets the location of this ListObsObjectResponse.

        region编码

        :return: The location of this ListObsObjectResponse.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this ListObsObjectResponse.

        region编码

        :param location: The location of this ListObsObjectResponse.
        :type location: str
        """
        self._location = location

    @property
    def prefix(self):
        """Gets the prefix of this ListObsObjectResponse.

        搜索前缀

        :return: The prefix of this ListObsObjectResponse.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this ListObsObjectResponse.

        搜索前缀

        :param prefix: The prefix of this ListObsObjectResponse.
        :type prefix: str
        """
        self._prefix = prefix

    @property
    def bucket_name(self):
        """Gets the bucket_name of this ListObsObjectResponse.

        obs桶名

        :return: The bucket_name of this ListObsObjectResponse.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this ListObsObjectResponse.

        obs桶名

        :param bucket_name: The bucket_name of this ListObsObjectResponse.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def next_marker(self):
        """Gets the next_marker of this ListObsObjectResponse.

        下一个object起始位置

        :return: The next_marker of this ListObsObjectResponse.
        :rtype: str
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        """Sets the next_marker of this ListObsObjectResponse.

        下一个object起始位置

        :param next_marker: The next_marker of this ListObsObjectResponse.
        :type next_marker: str
        """
        self._next_marker = next_marker

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
        if not isinstance(other, ListObsObjectResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
