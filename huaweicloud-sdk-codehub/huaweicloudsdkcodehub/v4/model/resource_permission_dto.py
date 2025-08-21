# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourcePermissionDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'permission_id': 'int',
        'action': 'str',
        'display_name': 'str',
        'display_name_cn': 'str',
        'enabled': 'bool',
        'editable': 'bool'
    }

    attribute_map = {
        'permission_id': 'permission_id',
        'action': 'action',
        'display_name': 'display_name',
        'display_name_cn': 'display_name_cn',
        'enabled': 'enabled',
        'editable': 'editable'
    }

    def __init__(self, permission_id=None, action=None, display_name=None, display_name_cn=None, enabled=None, editable=None):
        r"""ResourcePermissionDto

        The model defined in huaweicloud sdk

        :param permission_id: **参数解释：** 记录id。
        :type permission_id: int
        :param action: **参数解释：** 操作。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type action: str
        :param display_name: **参数解释：** 操作名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type display_name: str
        :param display_name_cn: **参数解释：** 操作中文名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type display_name_cn: str
        :param enabled: **参数解释：** 是否开启。
        :type enabled: bool
        :param editable: **参数解释：** 是否编辑。
        :type editable: bool
        """
        
        

        self._permission_id = None
        self._action = None
        self._display_name = None
        self._display_name_cn = None
        self._enabled = None
        self._editable = None
        self.discriminator = None

        if permission_id is not None:
            self.permission_id = permission_id
        if action is not None:
            self.action = action
        if display_name is not None:
            self.display_name = display_name
        if display_name_cn is not None:
            self.display_name_cn = display_name_cn
        if enabled is not None:
            self.enabled = enabled
        if editable is not None:
            self.editable = editable

    @property
    def permission_id(self):
        r"""Gets the permission_id of this ResourcePermissionDto.

        **参数解释：** 记录id。

        :return: The permission_id of this ResourcePermissionDto.
        :rtype: int
        """
        return self._permission_id

    @permission_id.setter
    def permission_id(self, permission_id):
        r"""Sets the permission_id of this ResourcePermissionDto.

        **参数解释：** 记录id。

        :param permission_id: The permission_id of this ResourcePermissionDto.
        :type permission_id: int
        """
        self._permission_id = permission_id

    @property
    def action(self):
        r"""Gets the action of this ResourcePermissionDto.

        **参数解释：** 操作。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The action of this ResourcePermissionDto.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ResourcePermissionDto.

        **参数解释：** 操作。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param action: The action of this ResourcePermissionDto.
        :type action: str
        """
        self._action = action

    @property
    def display_name(self):
        r"""Gets the display_name of this ResourcePermissionDto.

        **参数解释：** 操作名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The display_name of this ResourcePermissionDto.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this ResourcePermissionDto.

        **参数解释：** 操作名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param display_name: The display_name of this ResourcePermissionDto.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def display_name_cn(self):
        r"""Gets the display_name_cn of this ResourcePermissionDto.

        **参数解释：** 操作中文名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The display_name_cn of this ResourcePermissionDto.
        :rtype: str
        """
        return self._display_name_cn

    @display_name_cn.setter
    def display_name_cn(self, display_name_cn):
        r"""Sets the display_name_cn of this ResourcePermissionDto.

        **参数解释：** 操作中文名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param display_name_cn: The display_name_cn of this ResourcePermissionDto.
        :type display_name_cn: str
        """
        self._display_name_cn = display_name_cn

    @property
    def enabled(self):
        r"""Gets the enabled of this ResourcePermissionDto.

        **参数解释：** 是否开启。

        :return: The enabled of this ResourcePermissionDto.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this ResourcePermissionDto.

        **参数解释：** 是否开启。

        :param enabled: The enabled of this ResourcePermissionDto.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def editable(self):
        r"""Gets the editable of this ResourcePermissionDto.

        **参数解释：** 是否编辑。

        :return: The editable of this ResourcePermissionDto.
        :rtype: bool
        """
        return self._editable

    @editable.setter
    def editable(self, editable):
        r"""Sets the editable of this ResourcePermissionDto.

        **参数解释：** 是否编辑。

        :param editable: The editable of this ResourcePermissionDto.
        :type editable: bool
        """
        self._editable = editable

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
        if not isinstance(other, ResourcePermissionDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
