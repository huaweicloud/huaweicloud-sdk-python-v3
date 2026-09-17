# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchSqlLimitingRuleNewRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine_type': 'str',
        'item_ids': 'str',
        'action': 'str'
    }

    attribute_map = {
        'engine_type': 'engine_type',
        'item_ids': 'item_ids',
        'action': 'action'
    }

    def __init__(self, engine_type=None, item_ids=None, action=None):
        r"""SwitchSqlLimitingRuleNewRequestBody

        The model defined in huaweicloud sdk

        :param engine_type: 数据库引擎类型
        :type engine_type: str
        :param item_ids: SQL限流规则ID，可组合，用逗号分隔
        :type item_ids: str
        :param action: SQL限流动作标志
        :type action: str
        """
        
        

        self._engine_type = None
        self._item_ids = None
        self._action = None
        self.discriminator = None

        self.engine_type = engine_type
        self.item_ids = item_ids
        self.action = action

    @property
    def engine_type(self):
        r"""Gets the engine_type of this SwitchSqlLimitingRuleNewRequestBody.

        数据库引擎类型

        :return: The engine_type of this SwitchSqlLimitingRuleNewRequestBody.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this SwitchSqlLimitingRuleNewRequestBody.

        数据库引擎类型

        :param engine_type: The engine_type of this SwitchSqlLimitingRuleNewRequestBody.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def item_ids(self):
        r"""Gets the item_ids of this SwitchSqlLimitingRuleNewRequestBody.

        SQL限流规则ID，可组合，用逗号分隔

        :return: The item_ids of this SwitchSqlLimitingRuleNewRequestBody.
        :rtype: str
        """
        return self._item_ids

    @item_ids.setter
    def item_ids(self, item_ids):
        r"""Sets the item_ids of this SwitchSqlLimitingRuleNewRequestBody.

        SQL限流规则ID，可组合，用逗号分隔

        :param item_ids: The item_ids of this SwitchSqlLimitingRuleNewRequestBody.
        :type item_ids: str
        """
        self._item_ids = item_ids

    @property
    def action(self):
        r"""Gets the action of this SwitchSqlLimitingRuleNewRequestBody.

        SQL限流动作标志

        :return: The action of this SwitchSqlLimitingRuleNewRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this SwitchSqlLimitingRuleNewRequestBody.

        SQL限流动作标志

        :param action: The action of this SwitchSqlLimitingRuleNewRequestBody.
        :type action: str
        """
        self._action = action

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SwitchSqlLimitingRuleNewRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
