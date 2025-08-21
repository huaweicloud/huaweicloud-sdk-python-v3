# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGroupsInheritRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'int',
        'setting_type': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'setting_type': 'setting_type'
    }

    def __init__(self, group_id=None, setting_type=None):
        r"""ShowGroupsInheritRequest

        The model defined in huaweicloud sdk

        :param group_id: **参数解释：** 代码组id，代码组首页，Group ID后的数字Id
        :type group_id: int
        :param setting_type: **参数解释：** 设置类型protected_branches保护分支 protected_tags保护tag push_rules推送规则 merge_requests合并请求 mr_branch_policies合并分支 reviews检视意见 e2e_settings e2e设置 webhook_settings hook设置 deploy_keys 部署key watermark水印 repository_settings仓库设置。
        :type setting_type: str
        """
        
        

        self._group_id = None
        self._setting_type = None
        self.discriminator = None

        self.group_id = group_id
        if setting_type is not None:
            self.setting_type = setting_type

    @property
    def group_id(self):
        r"""Gets the group_id of this ShowGroupsInheritRequest.

        **参数解释：** 代码组id，代码组首页，Group ID后的数字Id

        :return: The group_id of this ShowGroupsInheritRequest.
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ShowGroupsInheritRequest.

        **参数解释：** 代码组id，代码组首页，Group ID后的数字Id

        :param group_id: The group_id of this ShowGroupsInheritRequest.
        :type group_id: int
        """
        self._group_id = group_id

    @property
    def setting_type(self):
        r"""Gets the setting_type of this ShowGroupsInheritRequest.

        **参数解释：** 设置类型protected_branches保护分支 protected_tags保护tag push_rules推送规则 merge_requests合并请求 mr_branch_policies合并分支 reviews检视意见 e2e_settings e2e设置 webhook_settings hook设置 deploy_keys 部署key watermark水印 repository_settings仓库设置。

        :return: The setting_type of this ShowGroupsInheritRequest.
        :rtype: str
        """
        return self._setting_type

    @setting_type.setter
    def setting_type(self, setting_type):
        r"""Sets the setting_type of this ShowGroupsInheritRequest.

        **参数解释：** 设置类型protected_branches保护分支 protected_tags保护tag push_rules推送规则 merge_requests合并请求 mr_branch_policies合并分支 reviews检视意见 e2e_settings e2e设置 webhook_settings hook设置 deploy_keys 部署key watermark水印 repository_settings仓库设置。

        :param setting_type: The setting_type of this ShowGroupsInheritRequest.
        :type setting_type: str
        """
        self._setting_type = setting_type

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
        if not isinstance(other, ShowGroupsInheritRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
