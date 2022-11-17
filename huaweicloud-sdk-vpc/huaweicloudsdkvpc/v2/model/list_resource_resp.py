# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourceResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resouce_detail': 'object',
        'resource_id': 'str',
        'resource_name': 'str',
        'tags': 'list[ResourceTag]'
    }

    attribute_map = {
        'resouce_detail': 'resouce_detail',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'tags': 'tags'
    }

    def __init__(self, resouce_detail=None, resource_id=None, resource_name=None, tags=None):
        """ListResourceResp

        The model defined in huaweicloud sdk

        :param resouce_detail: 资源详情。 资源对象，用于扩展。默认为空
        :type resouce_detail: object
        :param resource_id: 资源ID
        :type resource_id: str
        :param resource_name: 资源名称，没有默认为空字符串
        :type resource_name: str
        :param tags: 标签列表，没有标签默认为空数组
        :type tags: list[:class:`huaweicloudsdkvpc.v2.ResourceTag`]
        """
        
        

        self._resouce_detail = None
        self._resource_id = None
        self._resource_name = None
        self._tags = None
        self.discriminator = None

        self.resouce_detail = resouce_detail
        self.resource_id = resource_id
        self.resource_name = resource_name
        if tags is not None:
            self.tags = tags

    @property
    def resouce_detail(self):
        """Gets the resouce_detail of this ListResourceResp.

        资源详情。 资源对象，用于扩展。默认为空

        :return: The resouce_detail of this ListResourceResp.
        :rtype: object
        """
        return self._resouce_detail

    @resouce_detail.setter
    def resouce_detail(self, resouce_detail):
        """Sets the resouce_detail of this ListResourceResp.

        资源详情。 资源对象，用于扩展。默认为空

        :param resouce_detail: The resouce_detail of this ListResourceResp.
        :type resouce_detail: object
        """
        self._resouce_detail = resouce_detail

    @property
    def resource_id(self):
        """Gets the resource_id of this ListResourceResp.

        资源ID

        :return: The resource_id of this ListResourceResp.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ListResourceResp.

        资源ID

        :param resource_id: The resource_id of this ListResourceResp.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """Gets the resource_name of this ListResourceResp.

        资源名称，没有默认为空字符串

        :return: The resource_name of this ListResourceResp.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this ListResourceResp.

        资源名称，没有默认为空字符串

        :param resource_name: The resource_name of this ListResourceResp.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def tags(self):
        """Gets the tags of this ListResourceResp.

        标签列表，没有标签默认为空数组

        :return: The tags of this ListResourceResp.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListResourceResp.

        标签列表，没有标签默认为空数组

        :param tags: The tags of this ListResourceResp.
        :type tags: list[:class:`huaweicloudsdkvpc.v2.ResourceTag`]
        """
        self._tags = tags

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
        if not isinstance(other, ListResourceResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
