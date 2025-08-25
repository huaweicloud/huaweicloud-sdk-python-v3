# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProtectedBranchBodyApiDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'actions': 'list[ProtectedActionBasicApiDto]'
    }

    attribute_map = {
        'name': 'name',
        'actions': 'actions'
    }

    def __init__(self, name=None, actions=None):
        r"""ProtectedBranchBodyApiDto

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 保护分支名称。 **取值范围** 字符串长度不少于1，不超过1000。
        :type name: str
        :param actions: **参数解释：** 事件列表。
        :type actions: list[:class:`huaweicloudsdkcodehub.v4.ProtectedActionBasicApiDto`]
        """
        
        

        self._name = None
        self._actions = None
        self.discriminator = None

        self.name = name
        if actions is not None:
            self.actions = actions

    @property
    def name(self):
        r"""Gets the name of this ProtectedBranchBodyApiDto.

        **参数解释：** 保护分支名称。 **取值范围** 字符串长度不少于1，不超过1000。

        :return: The name of this ProtectedBranchBodyApiDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ProtectedBranchBodyApiDto.

        **参数解释：** 保护分支名称。 **取值范围** 字符串长度不少于1，不超过1000。

        :param name: The name of this ProtectedBranchBodyApiDto.
        :type name: str
        """
        self._name = name

    @property
    def actions(self):
        r"""Gets the actions of this ProtectedBranchBodyApiDto.

        **参数解释：** 事件列表。

        :return: The actions of this ProtectedBranchBodyApiDto.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.ProtectedActionBasicApiDto`]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this ProtectedBranchBodyApiDto.

        **参数解释：** 事件列表。

        :param actions: The actions of this ProtectedBranchBodyApiDto.
        :type actions: list[:class:`huaweicloudsdkcodehub.v4.ProtectedActionBasicApiDto`]
        """
        self._actions = actions

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
        if not isinstance(other, ProtectedBranchBodyApiDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
