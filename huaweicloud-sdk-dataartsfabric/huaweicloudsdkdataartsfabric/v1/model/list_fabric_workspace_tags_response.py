# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFabricWorkspaceTagsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'list[ResourceTag]',
        'sys_tags': 'list[SystemTag]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'tags': 'tags',
        'sys_tags': 'sys_tags',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, tags=None, sys_tags=None, x_request_id=None):
        r"""ListFabricWorkspaceTagsResponse

        The model defined in huaweicloud sdk

        :param tags: 资源标签列表
        :type tags: list[:class:`huaweicloudsdkdataartsfabric.v1.ResourceTag`]
        :param sys_tags: 系统标签列表。
        :type sys_tags: list[:class:`huaweicloudsdkdataartsfabric.v1.SystemTag`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListFabricWorkspaceTagsResponse, self).__init__()

        self._tags = None
        self._sys_tags = None
        self._x_request_id = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags
        if sys_tags is not None:
            self.sys_tags = sys_tags
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def tags(self):
        r"""Gets the tags of this ListFabricWorkspaceTagsResponse.

        资源标签列表

        :return: The tags of this ListFabricWorkspaceTagsResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsfabric.v1.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListFabricWorkspaceTagsResponse.

        资源标签列表

        :param tags: The tags of this ListFabricWorkspaceTagsResponse.
        :type tags: list[:class:`huaweicloudsdkdataartsfabric.v1.ResourceTag`]
        """
        self._tags = tags

    @property
    def sys_tags(self):
        r"""Gets the sys_tags of this ListFabricWorkspaceTagsResponse.

        系统标签列表。

        :return: The sys_tags of this ListFabricWorkspaceTagsResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsfabric.v1.SystemTag`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        r"""Sets the sys_tags of this ListFabricWorkspaceTagsResponse.

        系统标签列表。

        :param sys_tags: The sys_tags of this ListFabricWorkspaceTagsResponse.
        :type sys_tags: list[:class:`huaweicloudsdkdataartsfabric.v1.SystemTag`]
        """
        self._sys_tags = sys_tags

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListFabricWorkspaceTagsResponse.

        :return: The x_request_id of this ListFabricWorkspaceTagsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListFabricWorkspaceTagsResponse.

        :param x_request_id: The x_request_id of this ListFabricWorkspaceTagsResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListFabricWorkspaceTagsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
