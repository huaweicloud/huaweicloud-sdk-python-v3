# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteAlertRuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_id': 'str',
        'delete_time': 'int',
        'x_request_id': 'str'
    }

    attribute_map = {
        'rule_id': 'rule_id',
        'delete_time': 'delete_time',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, rule_id=None, delete_time=None, x_request_id=None):
        """DeleteAlertRuleResponse

        The model defined in huaweicloud sdk

        :param rule_id: 告警规则 ID。Alert rule ID.
        :type rule_id: str
        :param delete_time: 删除时间。Delete time.
        :type delete_time: int
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(DeleteAlertRuleResponse, self).__init__()

        self._rule_id = None
        self._delete_time = None
        self._x_request_id = None
        self.discriminator = None

        if rule_id is not None:
            self.rule_id = rule_id
        if delete_time is not None:
            self.delete_time = delete_time
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def rule_id(self):
        """Gets the rule_id of this DeleteAlertRuleResponse.

        告警规则 ID。Alert rule ID.

        :return: The rule_id of this DeleteAlertRuleResponse.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this DeleteAlertRuleResponse.

        告警规则 ID。Alert rule ID.

        :param rule_id: The rule_id of this DeleteAlertRuleResponse.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def delete_time(self):
        """Gets the delete_time of this DeleteAlertRuleResponse.

        删除时间。Delete time.

        :return: The delete_time of this DeleteAlertRuleResponse.
        :rtype: int
        """
        return self._delete_time

    @delete_time.setter
    def delete_time(self, delete_time):
        """Sets the delete_time of this DeleteAlertRuleResponse.

        删除时间。Delete time.

        :param delete_time: The delete_time of this DeleteAlertRuleResponse.
        :type delete_time: int
        """
        self._delete_time = delete_time

    @property
    def x_request_id(self):
        """Gets the x_request_id of this DeleteAlertRuleResponse.

        :return: The x_request_id of this DeleteAlertRuleResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this DeleteAlertRuleResponse.

        :param x_request_id: The x_request_id of this DeleteAlertRuleResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, DeleteAlertRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
