# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceTagRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'list[KeyValueBean]',
        'sys_tags': 'list[KeyValueBean]'
    }

    attribute_map = {
        'tags': 'tags',
        'sys_tags': 'sys_tags'
    }

    def __init__(self, tags=None, sys_tags=None):
        """ResourceTagRequest

        The model defined in huaweicloud sdk

        :param tags: 标签列表 租户权限时该字段必选，op_service权限时和sys_tags二选一
        :type tags: list[:class:`huaweicloudsdkdbss.v1.KeyValueBean`]
        :param sys_tags: 系统标签列表 op_service权限可以访问，和tags二选一。 目前TMS调用时只包含一个resource_tag结构体 ，key固定为：_sys_enterprise_project_id value是UUID或0,value为0表示默认企业项目
        :type sys_tags: list[:class:`huaweicloudsdkdbss.v1.KeyValueBean`]
        """
        
        

        self._tags = None
        self._sys_tags = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags
        if sys_tags is not None:
            self.sys_tags = sys_tags

    @property
    def tags(self):
        """Gets the tags of this ResourceTagRequest.

        标签列表 租户权限时该字段必选，op_service权限时和sys_tags二选一

        :return: The tags of this ResourceTagRequest.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.KeyValueBean`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ResourceTagRequest.

        标签列表 租户权限时该字段必选，op_service权限时和sys_tags二选一

        :param tags: The tags of this ResourceTagRequest.
        :type tags: list[:class:`huaweicloudsdkdbss.v1.KeyValueBean`]
        """
        self._tags = tags

    @property
    def sys_tags(self):
        """Gets the sys_tags of this ResourceTagRequest.

        系统标签列表 op_service权限可以访问，和tags二选一。 目前TMS调用时只包含一个resource_tag结构体 ，key固定为：_sys_enterprise_project_id value是UUID或0,value为0表示默认企业项目

        :return: The sys_tags of this ResourceTagRequest.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.KeyValueBean`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        """Sets the sys_tags of this ResourceTagRequest.

        系统标签列表 op_service权限可以访问，和tags二选一。 目前TMS调用时只包含一个resource_tag结构体 ，key固定为：_sys_enterprise_project_id value是UUID或0,value为0表示默认企业项目

        :param sys_tags: The sys_tags of this ResourceTagRequest.
        :type sys_tags: list[:class:`huaweicloudsdkdbss.v1.KeyValueBean`]
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
        if not isinstance(other, ResourceTagRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
