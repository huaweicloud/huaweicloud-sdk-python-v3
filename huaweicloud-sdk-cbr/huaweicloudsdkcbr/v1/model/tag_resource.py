# coding: utf-8

import pprint
import re

import six





class TagResource:


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
        'resource_detail': 'list[Vault]',
        'tags': 'list[Tag]',
        'resource_name': 'str',
        'sys_tags': 'list[SysTag]'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'resource_detail': 'resource_detail',
        'tags': 'tags',
        'resource_name': 'resource_name',
        'sys_tags': 'sys_tags'
    }

    def __init__(self, resource_id=None, resource_detail=None, tags=None, resource_name=None, sys_tags=None):
        """TagResource - a model defined in huaweicloud sdk"""
        
        

        self._resource_id = None
        self._resource_detail = None
        self._tags = None
        self._resource_name = None
        self._sys_tags = None
        self.discriminator = None

        self.resource_id = resource_id
        self.resource_detail = resource_detail
        self.tags = tags
        self.resource_name = resource_name
        self.sys_tags = sys_tags

    @property
    def resource_id(self):
        """Gets the resource_id of this TagResource.

        资源ID

        :return: The resource_id of this TagResource.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this TagResource.

        资源ID

        :param resource_id: The resource_id of this TagResource.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def resource_detail(self):
        """Gets the resource_detail of this TagResource.

        资源详情

        :return: The resource_detail of this TagResource.
        :rtype: list[Vault]
        """
        return self._resource_detail

    @resource_detail.setter
    def resource_detail(self, resource_detail):
        """Sets the resource_detail of this TagResource.

        资源详情

        :param resource_detail: The resource_detail of this TagResource.
        :type: list[Vault]
        """
        self._resource_detail = resource_detail

    @property
    def tags(self):
        """Gets the tags of this TagResource.

        标签列表 没有标签默认为空数字。

        :return: The tags of this TagResource.
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TagResource.

        标签列表 没有标签默认为空数字。

        :param tags: The tags of this TagResource.
        :type: list[Tag]
        """
        self._tags = tags

    @property
    def resource_name(self):
        """Gets the resource_name of this TagResource.

        资源名称

        :return: The resource_name of this TagResource.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this TagResource.

        资源名称

        :param resource_name: The resource_name of this TagResource.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def sys_tags(self):
        """Gets the sys_tags of this TagResource.

        仅op_service权限才可以可以获取此字段：  目前只包含一个resource_tag 结构体。  key：_sys_enterprise_project_id  value：企业项目id，0表示默认企业项目  非op_service场景不能返回此字段。

        :return: The sys_tags of this TagResource.
        :rtype: list[SysTag]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        """Sets the sys_tags of this TagResource.

        仅op_service权限才可以可以获取此字段：  目前只包含一个resource_tag 结构体。  key：_sys_enterprise_project_id  value：企业项目id，0表示默认企业项目  非op_service场景不能返回此字段。

        :param sys_tags: The sys_tags of this TagResource.
        :type: list[SysTag]
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TagResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
