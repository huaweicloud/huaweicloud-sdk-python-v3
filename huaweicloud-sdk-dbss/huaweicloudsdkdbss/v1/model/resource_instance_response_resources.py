# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceInstanceResponseResources:

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
        'resource_name': 'str',
        'resource_detail': 'object',
        'tags': 'list[ResourceInstanceResponseTags]',
        'sys_tags': 'list[ResourceInstanceResponseSysTags]'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'resource_detail': 'resource_detail',
        'tags': 'tags',
        'sys_tags': 'sys_tags'
    }

    def __init__(self, resource_id=None, resource_name=None, resource_detail=None, tags=None, sys_tags=None):
        r"""ResourceInstanceResponseResources

        The model defined in huaweicloud sdk

        :param resource_id: 资源ID
        :type resource_id: str
        :param resource_name: 资源名称，资源没有名称时默认为空字符串，eip返回ip地址。
        :type resource_name: str
        :param resource_detail: 资源详情。 资源对象，用于扩展，默认为空。
        :type resource_detail: object
        :param tags: 标签列表，没有标签默认为空数组
        :type tags: list[:class:`huaweicloudsdkdbss.v1.ResourceInstanceResponseTags`]
        :param sys_tags: 仅op_service权限才可以可以获取此字段： 目前只包含一个resource_tag 结构体 key：_sys_enterprise_project_id value：企业项目id，0表示默认企业项目 非op_service场景不能返回此字段
        :type sys_tags: list[:class:`huaweicloudsdkdbss.v1.ResourceInstanceResponseSysTags`]
        """
        
        

        self._resource_id = None
        self._resource_name = None
        self._resource_detail = None
        self._tags = None
        self._sys_tags = None
        self.discriminator = None

        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_detail = resource_detail
        self.tags = tags
        if sys_tags is not None:
            self.sys_tags = sys_tags

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ResourceInstanceResponseResources.

        资源ID

        :return: The resource_id of this ResourceInstanceResponseResources.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ResourceInstanceResponseResources.

        资源ID

        :param resource_id: The resource_id of this ResourceInstanceResponseResources.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        r"""Gets the resource_name of this ResourceInstanceResponseResources.

        资源名称，资源没有名称时默认为空字符串，eip返回ip地址。

        :return: The resource_name of this ResourceInstanceResponseResources.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this ResourceInstanceResponseResources.

        资源名称，资源没有名称时默认为空字符串，eip返回ip地址。

        :param resource_name: The resource_name of this ResourceInstanceResponseResources.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_detail(self):
        r"""Gets the resource_detail of this ResourceInstanceResponseResources.

        资源详情。 资源对象，用于扩展，默认为空。

        :return: The resource_detail of this ResourceInstanceResponseResources.
        :rtype: object
        """
        return self._resource_detail

    @resource_detail.setter
    def resource_detail(self, resource_detail):
        r"""Sets the resource_detail of this ResourceInstanceResponseResources.

        资源详情。 资源对象，用于扩展，默认为空。

        :param resource_detail: The resource_detail of this ResourceInstanceResponseResources.
        :type resource_detail: object
        """
        self._resource_detail = resource_detail

    @property
    def tags(self):
        r"""Gets the tags of this ResourceInstanceResponseResources.

        标签列表，没有标签默认为空数组

        :return: The tags of this ResourceInstanceResponseResources.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.ResourceInstanceResponseTags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ResourceInstanceResponseResources.

        标签列表，没有标签默认为空数组

        :param tags: The tags of this ResourceInstanceResponseResources.
        :type tags: list[:class:`huaweicloudsdkdbss.v1.ResourceInstanceResponseTags`]
        """
        self._tags = tags

    @property
    def sys_tags(self):
        r"""Gets the sys_tags of this ResourceInstanceResponseResources.

        仅op_service权限才可以可以获取此字段： 目前只包含一个resource_tag 结构体 key：_sys_enterprise_project_id value：企业项目id，0表示默认企业项目 非op_service场景不能返回此字段

        :return: The sys_tags of this ResourceInstanceResponseResources.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.ResourceInstanceResponseSysTags`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        r"""Sets the sys_tags of this ResourceInstanceResponseResources.

        仅op_service权限才可以可以获取此字段： 目前只包含一个resource_tag 结构体 key：_sys_enterprise_project_id value：企业项目id，0表示默认企业项目 非op_service场景不能返回此字段

        :param sys_tags: The sys_tags of this ResourceInstanceResponseResources.
        :type sys_tags: list[:class:`huaweicloudsdkdbss.v1.ResourceInstanceResponseSysTags`]
        """
        self._sys_tags = sys_tags

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
        if not isinstance(other, ResourceInstanceResponseResources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
