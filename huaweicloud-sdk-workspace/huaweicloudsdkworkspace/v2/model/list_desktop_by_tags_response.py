# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDesktopByTagsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'resources': 'list[TagResource]',
        'total_count': 'int'
    }

    attribute_map = {
        'offset': 'offset',
        'resources': 'resources',
        'total_count': 'total_count'
    }

    def __init__(self, offset=None, resources=None, total_count=None):
        """ListDesktopByTagsResponse

        The model defined in huaweicloud sdk

        :param offset: 指定查询信息列表的偏移量，默认为0
        :type offset: int
        :param resources: 资源对象
        :type resources: list[:class:`huaweicloudsdkworkspace.v2.TagResource`]
        :param total_count: 数量
        :type total_count: int
        """
        
        super(ListDesktopByTagsResponse, self).__init__()

        self._offset = None
        self._resources = None
        self._total_count = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if resources is not None:
            self.resources = resources
        if total_count is not None:
            self.total_count = total_count

    @property
    def offset(self):
        """Gets the offset of this ListDesktopByTagsResponse.

        指定查询信息列表的偏移量，默认为0

        :return: The offset of this ListDesktopByTagsResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDesktopByTagsResponse.

        指定查询信息列表的偏移量，默认为0

        :param offset: The offset of this ListDesktopByTagsResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def resources(self):
        """Gets the resources of this ListDesktopByTagsResponse.

        资源对象

        :return: The resources of this ListDesktopByTagsResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.TagResource`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this ListDesktopByTagsResponse.

        资源对象

        :param resources: The resources of this ListDesktopByTagsResponse.
        :type resources: list[:class:`huaweicloudsdkworkspace.v2.TagResource`]
        """
        self._resources = resources

    @property
    def total_count(self):
        """Gets the total_count of this ListDesktopByTagsResponse.

        数量

        :return: The total_count of this ListDesktopByTagsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListDesktopByTagsResponse.

        数量

        :param total_count: The total_count of this ListDesktopByTagsResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListDesktopByTagsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
