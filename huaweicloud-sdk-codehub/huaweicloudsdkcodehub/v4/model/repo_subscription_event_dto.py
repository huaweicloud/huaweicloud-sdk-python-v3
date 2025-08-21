# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepoSubscriptionEventDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_type': 'str',
        'action': 'str',
        'enabled': 'bool',
        'role_ids': 'list[str]',
        'role_names': 'list[str]'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'action': 'action',
        'enabled': 'enabled',
        'role_ids': 'role_ids',
        'role_names': 'role_names'
    }

    def __init__(self, resource_type=None, action=None, enabled=None, role_ids=None, role_names=None):
        r"""RepoSubscriptionEventDto

        The model defined in huaweicloud sdk

        :param resource_type: **参数解释：** 资源类型。 - repo，仓库。 - mr，合并请求。  - member，成员。 - note，检视意见。
        :type resource_type: str
        :param action: **参数解释：** 事件名。 - create，创建。 - open，开启。 - update，更新。  - delete，删除。 - merge，合并。 - review，检视。  - approve，审核。 - create_note，新建评审意见。 - resolve_note，解决评审意见。 - mention，被提及。
        :type action: str
        :param enabled: **参数解释：** 启用事件通知
        :type enabled: bool
        :param role_ids: **参数解释：** 通知的角色ID列表
        :type role_ids: list[str]
        :param role_names: **参数解释：** 通知的角色名称列表。 - creator，创建者。 - assignee，合并人。 - reviewer，评审人。 - scorer，审核人。 - approver，检视人。
        :type role_names: list[str]
        """
        
        

        self._resource_type = None
        self._action = None
        self._enabled = None
        self._role_ids = None
        self._role_names = None
        self.discriminator = None

        if resource_type is not None:
            self.resource_type = resource_type
        if action is not None:
            self.action = action
        if enabled is not None:
            self.enabled = enabled
        if role_ids is not None:
            self.role_ids = role_ids
        if role_names is not None:
            self.role_names = role_names

    @property
    def resource_type(self):
        r"""Gets the resource_type of this RepoSubscriptionEventDto.

        **参数解释：** 资源类型。 - repo，仓库。 - mr，合并请求。  - member，成员。 - note，检视意见。

        :return: The resource_type of this RepoSubscriptionEventDto.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this RepoSubscriptionEventDto.

        **参数解释：** 资源类型。 - repo，仓库。 - mr，合并请求。  - member，成员。 - note，检视意见。

        :param resource_type: The resource_type of this RepoSubscriptionEventDto.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def action(self):
        r"""Gets the action of this RepoSubscriptionEventDto.

        **参数解释：** 事件名。 - create，创建。 - open，开启。 - update，更新。  - delete，删除。 - merge，合并。 - review，检视。  - approve，审核。 - create_note，新建评审意见。 - resolve_note，解决评审意见。 - mention，被提及。

        :return: The action of this RepoSubscriptionEventDto.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this RepoSubscriptionEventDto.

        **参数解释：** 事件名。 - create，创建。 - open，开启。 - update，更新。  - delete，删除。 - merge，合并。 - review，检视。  - approve，审核。 - create_note，新建评审意见。 - resolve_note，解决评审意见。 - mention，被提及。

        :param action: The action of this RepoSubscriptionEventDto.
        :type action: str
        """
        self._action = action

    @property
    def enabled(self):
        r"""Gets the enabled of this RepoSubscriptionEventDto.

        **参数解释：** 启用事件通知

        :return: The enabled of this RepoSubscriptionEventDto.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this RepoSubscriptionEventDto.

        **参数解释：** 启用事件通知

        :param enabled: The enabled of this RepoSubscriptionEventDto.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def role_ids(self):
        r"""Gets the role_ids of this RepoSubscriptionEventDto.

        **参数解释：** 通知的角色ID列表

        :return: The role_ids of this RepoSubscriptionEventDto.
        :rtype: list[str]
        """
        return self._role_ids

    @role_ids.setter
    def role_ids(self, role_ids):
        r"""Sets the role_ids of this RepoSubscriptionEventDto.

        **参数解释：** 通知的角色ID列表

        :param role_ids: The role_ids of this RepoSubscriptionEventDto.
        :type role_ids: list[str]
        """
        self._role_ids = role_ids

    @property
    def role_names(self):
        r"""Gets the role_names of this RepoSubscriptionEventDto.

        **参数解释：** 通知的角色名称列表。 - creator，创建者。 - assignee，合并人。 - reviewer，评审人。 - scorer，审核人。 - approver，检视人。

        :return: The role_names of this RepoSubscriptionEventDto.
        :rtype: list[str]
        """
        return self._role_names

    @role_names.setter
    def role_names(self, role_names):
        r"""Sets the role_names of this RepoSubscriptionEventDto.

        **参数解释：** 通知的角色名称列表。 - creator，创建者。 - assignee，合并人。 - reviewer，评审人。 - scorer，审核人。 - approver，检视人。

        :param role_names: The role_names of this RepoSubscriptionEventDto.
        :type role_names: list[str]
        """
        self._role_names = role_names

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
        if not isinstance(other, RepoSubscriptionEventDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
