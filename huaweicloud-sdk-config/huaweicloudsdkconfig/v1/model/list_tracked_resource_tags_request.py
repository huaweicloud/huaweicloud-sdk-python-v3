# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTrackedResourceTagsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'marker': 'str',
        'limit': 'int',
        'resource_deleted': 'bool'
    }

    attribute_map = {
        'key': 'key',
        'marker': 'marker',
        'limit': 'limit',
        'resource_deleted': 'resource_deleted'
    }

    def __init__(self, key=None, marker=None, limit=None, resource_deleted=None):
        r"""ListTrackedResourceTagsRequest

        The model defined in huaweicloud sdk

        :param key: 标签键名
        :type key: str
        :param marker: 分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页
        :type marker: str
        :param limit: 最大的返回数量。
        :type limit: int
        :param resource_deleted: 是否查询已删除的资源。默认为false，不查询已删除的资源
        :type resource_deleted: bool
        """
        
        

        self._key = None
        self._marker = None
        self._limit = None
        self._resource_deleted = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if resource_deleted is not None:
            self.resource_deleted = resource_deleted

    @property
    def key(self):
        r"""Gets the key of this ListTrackedResourceTagsRequest.

        标签键名

        :return: The key of this ListTrackedResourceTagsRequest.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this ListTrackedResourceTagsRequest.

        标签键名

        :param key: The key of this ListTrackedResourceTagsRequest.
        :type key: str
        """
        self._key = key

    @property
    def marker(self):
        r"""Gets the marker of this ListTrackedResourceTagsRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :return: The marker of this ListTrackedResourceTagsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListTrackedResourceTagsRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :param marker: The marker of this ListTrackedResourceTagsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListTrackedResourceTagsRequest.

        最大的返回数量。

        :return: The limit of this ListTrackedResourceTagsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTrackedResourceTagsRequest.

        最大的返回数量。

        :param limit: The limit of this ListTrackedResourceTagsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def resource_deleted(self):
        r"""Gets the resource_deleted of this ListTrackedResourceTagsRequest.

        是否查询已删除的资源。默认为false，不查询已删除的资源

        :return: The resource_deleted of this ListTrackedResourceTagsRequest.
        :rtype: bool
        """
        return self._resource_deleted

    @resource_deleted.setter
    def resource_deleted(self, resource_deleted):
        r"""Sets the resource_deleted of this ListTrackedResourceTagsRequest.

        是否查询已删除的资源。默认为false，不查询已删除的资源

        :param resource_deleted: The resource_deleted of this ListTrackedResourceTagsRequest.
        :type resource_deleted: bool
        """
        self._resource_deleted = resource_deleted

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
        if not isinstance(other, ListTrackedResourceTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
