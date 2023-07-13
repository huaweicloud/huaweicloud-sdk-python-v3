# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateL7RuleRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'l7policy_id': 'str',
        'l7rule_id': 'str',
        'body': 'UpdateL7RuleRequestBody'
    }

    attribute_map = {
        'l7policy_id': 'l7policy_id',
        'l7rule_id': 'l7rule_id',
        'body': 'body'
    }

    def __init__(self, l7policy_id=None, l7rule_id=None, body=None):
        """UpdateL7RuleRequest

        The model defined in huaweicloud sdk

        :param l7policy_id: 策略ID。
        :type l7policy_id: str
        :param l7rule_id: 规则ID。
        :type l7rule_id: str
        :param body: Body of the UpdateL7RuleRequest
        :type body: :class:`huaweicloudsdkelb.v3.UpdateL7RuleRequestBody`
        """
        
        

        self._l7policy_id = None
        self._l7rule_id = None
        self._body = None
        self.discriminator = None

        self.l7policy_id = l7policy_id
        self.l7rule_id = l7rule_id
        if body is not None:
            self.body = body

    @property
    def l7policy_id(self):
        """Gets the l7policy_id of this UpdateL7RuleRequest.

        策略ID。

        :return: The l7policy_id of this UpdateL7RuleRequest.
        :rtype: str
        """
        return self._l7policy_id

    @l7policy_id.setter
    def l7policy_id(self, l7policy_id):
        """Sets the l7policy_id of this UpdateL7RuleRequest.

        策略ID。

        :param l7policy_id: The l7policy_id of this UpdateL7RuleRequest.
        :type l7policy_id: str
        """
        self._l7policy_id = l7policy_id

    @property
    def l7rule_id(self):
        """Gets the l7rule_id of this UpdateL7RuleRequest.

        规则ID。

        :return: The l7rule_id of this UpdateL7RuleRequest.
        :rtype: str
        """
        return self._l7rule_id

    @l7rule_id.setter
    def l7rule_id(self, l7rule_id):
        """Sets the l7rule_id of this UpdateL7RuleRequest.

        规则ID。

        :param l7rule_id: The l7rule_id of this UpdateL7RuleRequest.
        :type l7rule_id: str
        """
        self._l7rule_id = l7rule_id

    @property
    def body(self):
        """Gets the body of this UpdateL7RuleRequest.

        :return: The body of this UpdateL7RuleRequest.
        :rtype: :class:`huaweicloudsdkelb.v3.UpdateL7RuleRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateL7RuleRequest.

        :param body: The body of this UpdateL7RuleRequest.
        :type body: :class:`huaweicloudsdkelb.v3.UpdateL7RuleRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateL7RuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
