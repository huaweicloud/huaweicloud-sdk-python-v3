# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInteractionRuleRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_app_user_id': 'str',
        'group_id': 'str',
        'rule_id': 'str',
        'body': 'CreateInteractionRuleReq'
    }

    attribute_map = {
        'x_app_user_id': 'X-App-UserId',
        'group_id': 'group_id',
        'rule_id': 'rule_id',
        'body': 'body'
    }

    def __init__(self, x_app_user_id=None, group_id=None, rule_id=None, body=None):
        r"""UpdateInteractionRuleRequest

        The model defined in huaweicloud sdk

        :param x_app_user_id: 第三方用户ID。不允许输入中文。
        :type x_app_user_id: str
        :param group_id: 互动规则库ID。
        :type group_id: str
        :param rule_id: 互动规则ID。
        :type rule_id: str
        :param body: Body of the UpdateInteractionRuleRequest
        :type body: :class:`huaweicloudsdkmetastudio.v1.CreateInteractionRuleReq`
        """
        
        

        self._x_app_user_id = None
        self._group_id = None
        self._rule_id = None
        self._body = None
        self.discriminator = None

        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        self.group_id = group_id
        self.rule_id = rule_id
        if body is not None:
            self.body = body

    @property
    def x_app_user_id(self):
        r"""Gets the x_app_user_id of this UpdateInteractionRuleRequest.

        第三方用户ID。不允许输入中文。

        :return: The x_app_user_id of this UpdateInteractionRuleRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        r"""Sets the x_app_user_id of this UpdateInteractionRuleRequest.

        第三方用户ID。不允许输入中文。

        :param x_app_user_id: The x_app_user_id of this UpdateInteractionRuleRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def group_id(self):
        r"""Gets the group_id of this UpdateInteractionRuleRequest.

        互动规则库ID。

        :return: The group_id of this UpdateInteractionRuleRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this UpdateInteractionRuleRequest.

        互动规则库ID。

        :param group_id: The group_id of this UpdateInteractionRuleRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def rule_id(self):
        r"""Gets the rule_id of this UpdateInteractionRuleRequest.

        互动规则ID。

        :return: The rule_id of this UpdateInteractionRuleRequest.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this UpdateInteractionRuleRequest.

        互动规则ID。

        :param rule_id: The rule_id of this UpdateInteractionRuleRequest.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def body(self):
        r"""Gets the body of this UpdateInteractionRuleRequest.

        :return: The body of this UpdateInteractionRuleRequest.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateInteractionRuleReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateInteractionRuleRequest.

        :param body: The body of this UpdateInteractionRuleRequest.
        :type body: :class:`huaweicloudsdkmetastudio.v1.CreateInteractionRuleReq`
        """
        self._body = body

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
        if not isinstance(other, UpdateInteractionRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
