# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateStrategyResponse(SdkResponse):

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
        'rule_set_id': 'str'
    }

    attribute_map = {
        'status': 'status',
        'rule_set_id': 'rule_set_id'
    }

    def __init__(self, status=None, rule_set_id=None):
        """UpdateStrategyResponse

        The model defined in huaweicloud sdk

        :param status: 状态
        :type status: bool
        :param rule_set_id: 策略ID
        :type rule_set_id: str
        """
        
        super(UpdateStrategyResponse, self).__init__()

        self._status = None
        self._rule_set_id = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if rule_set_id is not None:
            self.rule_set_id = rule_set_id

    @property
    def status(self):
        """Gets the status of this UpdateStrategyResponse.

        状态

        :return: The status of this UpdateStrategyResponse.
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateStrategyResponse.

        状态

        :param status: The status of this UpdateStrategyResponse.
        :type status: bool
        """
        self._status = status

    @property
    def rule_set_id(self):
        """Gets the rule_set_id of this UpdateStrategyResponse.

        策略ID

        :return: The rule_set_id of this UpdateStrategyResponse.
        :rtype: str
        """
        return self._rule_set_id

    @rule_set_id.setter
    def rule_set_id(self, rule_set_id):
        """Sets the rule_set_id of this UpdateStrategyResponse.

        策略ID

        :param rule_set_id: The rule_set_id of this UpdateStrategyResponse.
        :type rule_set_id: str
        """
        self._rule_set_id = rule_set_id

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
        if not isinstance(other, UpdateStrategyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
