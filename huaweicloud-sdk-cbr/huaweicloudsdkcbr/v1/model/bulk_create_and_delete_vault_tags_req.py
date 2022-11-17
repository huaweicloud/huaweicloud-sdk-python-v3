# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BulkCreateAndDeleteVaultTagsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'list[Tag]',
        'sys_tags': 'list[SysTag]',
        'action': 'str'
    }

    attribute_map = {
        'tags': 'tags',
        'sys_tags': 'sys_tags',
        'action': 'action'
    }

    def __init__(self, tags=None, sys_tags=None, action=None):
        """BulkCreateAndDeleteVaultTagsReq

        The model defined in huaweicloud sdk

        :param tags: 标签列表。  tags不允许为空列表。  tags中最多包含10个key。  tags中key不允许重复。
        :type tags: list[:class:`huaweicloudsdkcbr.v1.Tag`]
        :param sys_tags: 系统标签列表。  op_service权限可以访问，和tags二选一。  目前TMS调用时只包含一个resource_tag结构体 ，key固定为：_sys_enterprise_project_id。  value是UUID或0,value为0表示默认企业项目。  现在仅支持create操作。
        :type sys_tags: list[:class:`huaweicloudsdkcbr.v1.SysTag`]
        :param action: 操作标识：仅限于create（创建）、delete（删除）
        :type action: str
        """
        
        

        self._tags = None
        self._sys_tags = None
        self._action = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags
        if sys_tags is not None:
            self.sys_tags = sys_tags
        self.action = action

    @property
    def tags(self):
        """Gets the tags of this BulkCreateAndDeleteVaultTagsReq.

        标签列表。  tags不允许为空列表。  tags中最多包含10个key。  tags中key不允许重复。

        :return: The tags of this BulkCreateAndDeleteVaultTagsReq.
        :rtype: list[:class:`huaweicloudsdkcbr.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this BulkCreateAndDeleteVaultTagsReq.

        标签列表。  tags不允许为空列表。  tags中最多包含10个key。  tags中key不允许重复。

        :param tags: The tags of this BulkCreateAndDeleteVaultTagsReq.
        :type tags: list[:class:`huaweicloudsdkcbr.v1.Tag`]
        """
        self._tags = tags

    @property
    def sys_tags(self):
        """Gets the sys_tags of this BulkCreateAndDeleteVaultTagsReq.

        系统标签列表。  op_service权限可以访问，和tags二选一。  目前TMS调用时只包含一个resource_tag结构体 ，key固定为：_sys_enterprise_project_id。  value是UUID或0,value为0表示默认企业项目。  现在仅支持create操作。

        :return: The sys_tags of this BulkCreateAndDeleteVaultTagsReq.
        :rtype: list[:class:`huaweicloudsdkcbr.v1.SysTag`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        """Sets the sys_tags of this BulkCreateAndDeleteVaultTagsReq.

        系统标签列表。  op_service权限可以访问，和tags二选一。  目前TMS调用时只包含一个resource_tag结构体 ，key固定为：_sys_enterprise_project_id。  value是UUID或0,value为0表示默认企业项目。  现在仅支持create操作。

        :param sys_tags: The sys_tags of this BulkCreateAndDeleteVaultTagsReq.
        :type sys_tags: list[:class:`huaweicloudsdkcbr.v1.SysTag`]
        """
        self._sys_tags = sys_tags

    @property
    def action(self):
        """Gets the action of this BulkCreateAndDeleteVaultTagsReq.

        操作标识：仅限于create（创建）、delete（删除）

        :return: The action of this BulkCreateAndDeleteVaultTagsReq.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this BulkCreateAndDeleteVaultTagsReq.

        操作标识：仅限于create（创建）、delete（删除）

        :param action: The action of this BulkCreateAndDeleteVaultTagsReq.
        :type action: str
        """
        self._action = action

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
        if not isinstance(other, BulkCreateAndDeleteVaultTagsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
