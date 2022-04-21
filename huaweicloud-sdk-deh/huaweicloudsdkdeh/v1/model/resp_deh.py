# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RespDeh:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'resouce_detail': 'str',
        'tags': 'list[ResourceTag]',
        'resource_name': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'resouce_detail': 'resouce_detail',
        'tags': 'tags',
        'resource_name': 'resource_name'
    }

    def __init__(self, resource_id=None, resouce_detail=None, tags=None, resource_name=None):
        """RespDeh

        The model defined in huaweicloud sdk

        :param resource_id: 专属主机ID。
        :type resource_id: str
        :param resouce_detail: 专属主机详情。  该字段用于后续扩展，默认为空。
        :type resouce_detail: str
        :param tags: 标签列表。
        :type tags: list[:class:`huaweicloudsdkdeh.v1.ResourceTag`]
        :param resource_name: 资源名称。
        :type resource_name: str
        """
        
        

        self._resource_id = None
        self._resouce_detail = None
        self._tags = None
        self._resource_name = None
        self.discriminator = None

        self.resource_id = resource_id
        self.resouce_detail = resouce_detail
        self.tags = tags
        self.resource_name = resource_name

    @property
    def resource_id(self):
        """Gets the resource_id of this RespDeh.

        专属主机ID。

        :return: The resource_id of this RespDeh.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this RespDeh.

        专属主机ID。

        :param resource_id: The resource_id of this RespDeh.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resouce_detail(self):
        """Gets the resouce_detail of this RespDeh.

        专属主机详情。  该字段用于后续扩展，默认为空。

        :return: The resouce_detail of this RespDeh.
        :rtype: str
        """
        return self._resouce_detail

    @resouce_detail.setter
    def resouce_detail(self, resouce_detail):
        """Sets the resouce_detail of this RespDeh.

        专属主机详情。  该字段用于后续扩展，默认为空。

        :param resouce_detail: The resouce_detail of this RespDeh.
        :type resouce_detail: str
        """
        self._resouce_detail = resouce_detail

    @property
    def tags(self):
        """Gets the tags of this RespDeh.

        标签列表。

        :return: The tags of this RespDeh.
        :rtype: list[:class:`huaweicloudsdkdeh.v1.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this RespDeh.

        标签列表。

        :param tags: The tags of this RespDeh.
        :type tags: list[:class:`huaweicloudsdkdeh.v1.ResourceTag`]
        """
        self._tags = tags

    @property
    def resource_name(self):
        """Gets the resource_name of this RespDeh.

        资源名称。

        :return: The resource_name of this RespDeh.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this RespDeh.

        资源名称。

        :param resource_name: The resource_name of this RespDeh.
        :type resource_name: str
        """
        self._resource_name = resource_name

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
        if not isinstance(other, RespDeh):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
