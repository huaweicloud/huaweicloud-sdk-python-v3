# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourcesLevelResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_level_list': 'list[ResourceLevelItem]',
        'count': 'int'
    }

    attribute_map = {
        'resource_level_list': 'resource_level_list',
        'count': 'count'
    }

    def __init__(self, resource_level_list=None, count=None):
        r"""ListResourcesLevelResponse

        The model defined in huaweicloud sdk

        :param resource_level_list: 资源分级列表数据
        :type resource_level_list: list[:class:`huaweicloudsdkbcc.v1.ResourceLevelItem`]
        :param count: 资源等级总数
        :type count: int
        """
        
        super(ListResourcesLevelResponse, self).__init__()

        self._resource_level_list = None
        self._count = None
        self.discriminator = None

        if resource_level_list is not None:
            self.resource_level_list = resource_level_list
        if count is not None:
            self.count = count

    @property
    def resource_level_list(self):
        r"""Gets the resource_level_list of this ListResourcesLevelResponse.

        资源分级列表数据

        :return: The resource_level_list of this ListResourcesLevelResponse.
        :rtype: list[:class:`huaweicloudsdkbcc.v1.ResourceLevelItem`]
        """
        return self._resource_level_list

    @resource_level_list.setter
    def resource_level_list(self, resource_level_list):
        r"""Sets the resource_level_list of this ListResourcesLevelResponse.

        资源分级列表数据

        :param resource_level_list: The resource_level_list of this ListResourcesLevelResponse.
        :type resource_level_list: list[:class:`huaweicloudsdkbcc.v1.ResourceLevelItem`]
        """
        self._resource_level_list = resource_level_list

    @property
    def count(self):
        r"""Gets the count of this ListResourcesLevelResponse.

        资源等级总数

        :return: The count of this ListResourcesLevelResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListResourcesLevelResponse.

        资源等级总数

        :param count: The count of this ListResourcesLevelResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListResourcesLevelResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
