# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'resource_detail': 'InstancesResourceDetail',
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
        r"""TagResource

        The model defined in huaweicloud sdk

        :param resource_id: 资源ID
        :type resource_id: str
        :param resource_detail: 
        :type resource_detail: :class:`huaweicloudsdkcbr.v1.InstancesResourceDetail`
        :param tags: 标签列表 没有标签默认为空数字。
        :type tags: list[:class:`huaweicloudsdkcbr.v1.Tag`]
        :param resource_name: 资源名称
        :type resource_name: str
        :param sys_tags: 仅op_service权限才可以获取此字段：  目前只包含一个resource_tag 结构体。  key：_sys_enterprise_project_id  value：企业项目id，0表示默认企业项目  非op_service场景不能返回此字段。
        :type sys_tags: list[:class:`huaweicloudsdkcbr.v1.SysTag`]
        """
        
        

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
        r"""Gets the resource_id of this TagResource.

        资源ID

        :return: The resource_id of this TagResource.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this TagResource.

        资源ID

        :param resource_id: The resource_id of this TagResource.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_detail(self):
        r"""Gets the resource_detail of this TagResource.

        :return: The resource_detail of this TagResource.
        :rtype: :class:`huaweicloudsdkcbr.v1.InstancesResourceDetail`
        """
        return self._resource_detail

    @resource_detail.setter
    def resource_detail(self, resource_detail):
        r"""Sets the resource_detail of this TagResource.

        :param resource_detail: The resource_detail of this TagResource.
        :type resource_detail: :class:`huaweicloudsdkcbr.v1.InstancesResourceDetail`
        """
        self._resource_detail = resource_detail

    @property
    def tags(self):
        r"""Gets the tags of this TagResource.

        标签列表 没有标签默认为空数字。

        :return: The tags of this TagResource.
        :rtype: list[:class:`huaweicloudsdkcbr.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this TagResource.

        标签列表 没有标签默认为空数字。

        :param tags: The tags of this TagResource.
        :type tags: list[:class:`huaweicloudsdkcbr.v1.Tag`]
        """
        self._tags = tags

    @property
    def resource_name(self):
        r"""Gets the resource_name of this TagResource.

        资源名称

        :return: The resource_name of this TagResource.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this TagResource.

        资源名称

        :param resource_name: The resource_name of this TagResource.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def sys_tags(self):
        r"""Gets the sys_tags of this TagResource.

        仅op_service权限才可以获取此字段：  目前只包含一个resource_tag 结构体。  key：_sys_enterprise_project_id  value：企业项目id，0表示默认企业项目  非op_service场景不能返回此字段。

        :return: The sys_tags of this TagResource.
        :rtype: list[:class:`huaweicloudsdkcbr.v1.SysTag`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        r"""Sets the sys_tags of this TagResource.

        仅op_service权限才可以获取此字段：  目前只包含一个resource_tag 结构体。  key：_sys_enterprise_project_id  value：企业项目id，0表示默认企业项目  非op_service场景不能返回此字段。

        :param sys_tags: The sys_tags of this TagResource.
        :type sys_tags: list[:class:`huaweicloudsdkcbr.v1.SysTag`]
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
        if not isinstance(other, TagResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
