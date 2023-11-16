# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'bool',
        'rule_id': 'str'
    }

    attribute_map = {
        'status': 'status',
        'rule_id': 'rule_id'
    }

    def __init__(self, status=None, rule_id=None):
        """UpdateRuleResponse

        The model defined in huaweicloud sdk

        :param status: 创建状态
        :type status: bool
        :param rule_id: 规则ID
        :type rule_id: str
        """
        
        super(UpdateRuleResponse, self).__init__()

        self._status = None
        self._rule_id = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if rule_id is not None:
            self.rule_id = rule_id

    @property
    def status(self):
        """Gets the status of this UpdateRuleResponse.

        创建状态

        :return: The status of this UpdateRuleResponse.
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateRuleResponse.

        创建状态

        :param status: The status of this UpdateRuleResponse.
        :type status: bool
        """
        self._status = status

    @property
    def rule_id(self):
        """Gets the rule_id of this UpdateRuleResponse.

        规则ID

        :return: The rule_id of this UpdateRuleResponse.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this UpdateRuleResponse.

        规则ID

        :param rule_id: The rule_id of this UpdateRuleResponse.
        :type rule_id: str
        """
        self._rule_id = rule_id

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
        if not isinstance(other, UpdateRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
