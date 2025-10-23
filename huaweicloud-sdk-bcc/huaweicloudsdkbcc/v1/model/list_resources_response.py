# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourcesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resources': 'list[ResourceItem]',
        'count': 'int',
        'next_marker': 'str'
    }

    attribute_map = {
        'resources': 'resources',
        'count': 'count',
        'next_marker': 'next_marker'
    }

    def __init__(self, resources=None, count=None, next_marker=None):
        r"""ListResourcesResponse

        The model defined in huaweicloud sdk

        :param resources: 资源列表
        :type resources: list[:class:`huaweicloudsdkbcc.v1.ResourceItem`]
        :param count: 资源总数
        :type count: int
        :param next_marker: 下一页的marker
        :type next_marker: str
        """
        
        super(ListResourcesResponse, self).__init__()

        self._resources = None
        self._count = None
        self._next_marker = None
        self.discriminator = None

        if resources is not None:
            self.resources = resources
        if count is not None:
            self.count = count
        if next_marker is not None:
            self.next_marker = next_marker

    @property
    def resources(self):
        r"""Gets the resources of this ListResourcesResponse.

        资源列表

        :return: The resources of this ListResourcesResponse.
        :rtype: list[:class:`huaweicloudsdkbcc.v1.ResourceItem`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this ListResourcesResponse.

        资源列表

        :param resources: The resources of this ListResourcesResponse.
        :type resources: list[:class:`huaweicloudsdkbcc.v1.ResourceItem`]
        """
        self._resources = resources

    @property
    def count(self):
        r"""Gets the count of this ListResourcesResponse.

        资源总数

        :return: The count of this ListResourcesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListResourcesResponse.

        资源总数

        :param count: The count of this ListResourcesResponse.
        :type count: int
        """
        self._count = count

    @property
    def next_marker(self):
        r"""Gets the next_marker of this ListResourcesResponse.

        下一页的marker

        :return: The next_marker of this ListResourcesResponse.
        :rtype: str
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        r"""Sets the next_marker of this ListResourcesResponse.

        下一页的marker

        :param next_marker: The next_marker of this ListResourcesResponse.
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
        if not isinstance(other, ListResourcesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
