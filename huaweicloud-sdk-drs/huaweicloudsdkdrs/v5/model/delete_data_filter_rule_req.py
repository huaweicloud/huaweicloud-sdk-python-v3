# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteDataFilterRuleReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_ids': 'list[int]',
        'type': 'str'
    }

    attribute_map = {
        'rule_ids': 'rule_ids',
        'type': 'type'
    }

    def __init__(self, rule_ids=None, type=None):
        r"""DeleteDataFilterRuleReq

        The model defined in huaweicloud sdk

        :param rule_ids: 待删除的数据过滤规则ID列表，支持批量删除多个规则。对应查询接口响应中的&#x60;batch_id&#x60;字段。
        :type rule_ids: list[int]
        :param type: 数据过滤条件类型，指定要删除的过滤规则所属的配置层级，取值common表示一般过滤条件，config表示高级配置过滤条件
        :type type: str
        """
        
        

        self._rule_ids = None
        self._type = None
        self.discriminator = None

        self.rule_ids = rule_ids
        self.type = type

    @property
    def rule_ids(self):
        r"""Gets the rule_ids of this DeleteDataFilterRuleReq.

        待删除的数据过滤规则ID列表，支持批量删除多个规则。对应查询接口响应中的`batch_id`字段。

        :return: The rule_ids of this DeleteDataFilterRuleReq.
        :rtype: list[int]
        """
        return self._rule_ids

    @rule_ids.setter
    def rule_ids(self, rule_ids):
        r"""Sets the rule_ids of this DeleteDataFilterRuleReq.

        待删除的数据过滤规则ID列表，支持批量删除多个规则。对应查询接口响应中的`batch_id`字段。

        :param rule_ids: The rule_ids of this DeleteDataFilterRuleReq.
        :type rule_ids: list[int]
        """
        self._rule_ids = rule_ids

    @property
    def type(self):
        r"""Gets the type of this DeleteDataFilterRuleReq.

        数据过滤条件类型，指定要删除的过滤规则所属的配置层级，取值common表示一般过滤条件，config表示高级配置过滤条件

        :return: The type of this DeleteDataFilterRuleReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DeleteDataFilterRuleReq.

        数据过滤条件类型，指定要删除的过滤规则所属的配置层级，取值common表示一般过滤条件，config表示高级配置过滤条件

        :param type: The type of this DeleteDataFilterRuleReq.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, DeleteDataFilterRuleReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
