# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HapComponentItem:

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
        'visible': 'bool',
        'actions_with_entities': 'list[ActionWithEntities]'
    }

    attribute_map = {
        'name': 'name',
        'visible': 'visible',
        'actions_with_entities': 'actions_with_entities'
    }

    def __init__(self, name=None, visible=None, actions_with_entities=None):
        r"""HapComponentItem

        The model defined in huaweicloud sdk

        :param name: 组件名称
        :type name: str
        :param visible: 元能力可见
        :type visible: bool
        :param actions_with_entities: 动作和实体列表
        :type actions_with_entities: list[:class:`huaweicloudsdkcodeartsgovernance.v1.ActionWithEntities`]
        """
        
        

        self._name = None
        self._visible = None
        self._actions_with_entities = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if visible is not None:
            self.visible = visible
        if actions_with_entities is not None:
            self.actions_with_entities = actions_with_entities

    @property
    def name(self):
        r"""Gets the name of this HapComponentItem.

        组件名称

        :return: The name of this HapComponentItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this HapComponentItem.

        组件名称

        :param name: The name of this HapComponentItem.
        :type name: str
        """
        self._name = name

    @property
    def visible(self):
        r"""Gets the visible of this HapComponentItem.

        元能力可见

        :return: The visible of this HapComponentItem.
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        r"""Sets the visible of this HapComponentItem.

        元能力可见

        :param visible: The visible of this HapComponentItem.
        :type visible: bool
        """
        self._visible = visible

    @property
    def actions_with_entities(self):
        r"""Gets the actions_with_entities of this HapComponentItem.

        动作和实体列表

        :return: The actions_with_entities of this HapComponentItem.
        :rtype: list[:class:`huaweicloudsdkcodeartsgovernance.v1.ActionWithEntities`]
        """
        return self._actions_with_entities

    @actions_with_entities.setter
    def actions_with_entities(self, actions_with_entities):
        r"""Sets the actions_with_entities of this HapComponentItem.

        动作和实体列表

        :param actions_with_entities: The actions_with_entities of this HapComponentItem.
        :type actions_with_entities: list[:class:`huaweicloudsdkcodeartsgovernance.v1.ActionWithEntities`]
        """
        self._actions_with_entities = actions_with_entities

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
        if not isinstance(other, HapComponentItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
