# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTagsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_type': 'ResourceType',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, resource_type=None, limit=None, offset=None):
        r"""ListTagsRequest

        The model defined in huaweicloud sdk

        :param resource_type: 资源类型。
        :type resource_type: :class:`huaweicloudsdkga.v1.ResourceType`
        :param limit: 每页返回的个数。
        :type limit: int
        :param offset: 偏移量。
        :type offset: int
        """
        
        

        self._resource_type = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.resource_type = resource_type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ListTagsRequest.

        资源类型。

        :return: The resource_type of this ListTagsRequest.
        :rtype: :class:`huaweicloudsdkga.v1.ResourceType`
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ListTagsRequest.

        资源类型。

        :param resource_type: The resource_type of this ListTagsRequest.
        :type resource_type: :class:`huaweicloudsdkga.v1.ResourceType`
        """
        self._resource_type = resource_type

    @property
    def limit(self):
        r"""Gets the limit of this ListTagsRequest.

        每页返回的个数。

        :return: The limit of this ListTagsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTagsRequest.

        每页返回的个数。

        :param limit: The limit of this ListTagsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListTagsRequest.

        偏移量。

        :return: The offset of this ListTagsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListTagsRequest.

        偏移量。

        :param offset: The offset of this ListTagsRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
