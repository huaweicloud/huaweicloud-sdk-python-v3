# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActionWithEntities:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'actions': 'list[str]',
        'entities': 'list[str]'
    }

    attribute_map = {
        'actions': 'actions',
        'entities': 'entities'
    }

    def __init__(self, actions=None, entities=None):
        r"""ActionWithEntities

        The model defined in huaweicloud sdk

        :param actions: 动作列表
        :type actions: list[str]
        :param entities: 实体列表
        :type entities: list[str]
        """
        
        

        self._actions = None
        self._entities = None
        self.discriminator = None

        if actions is not None:
            self.actions = actions
        if entities is not None:
            self.entities = entities

    @property
    def actions(self):
        r"""Gets the actions of this ActionWithEntities.

        动作列表

        :return: The actions of this ActionWithEntities.
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this ActionWithEntities.

        动作列表

        :param actions: The actions of this ActionWithEntities.
        :type actions: list[str]
        """
        self._actions = actions

    @property
    def entities(self):
        r"""Gets the entities of this ActionWithEntities.

        实体列表

        :return: The entities of this ActionWithEntities.
        :rtype: list[str]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        r"""Sets the entities of this ActionWithEntities.

        实体列表

        :param entities: The entities of this ActionWithEntities.
        :type entities: list[str]
        """
        self._entities = entities

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
        if not isinstance(other, ActionWithEntities):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
