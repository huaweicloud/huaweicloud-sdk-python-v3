# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePolicyRequestBody:

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
        'log_action_replaced': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'log_action_replaced': 'log_action_replaced'
    }

    def __init__(self, name=None, log_action_replaced=None):
        """CreatePolicyRequestBody

        The model defined in huaweicloud sdk

        :param name: 策略名称（策略名称只能由数字、字母和下划线组成，长度不能超过64为字符）
        :type name: str
        :param log_action_replaced: cc规则和精准防护规则“防护动作”选择“仅记录”时，Web基础防护是否命中策略规则并阻断，默认为true
        :type log_action_replaced: bool
        """
        
        

        self._name = None
        self._log_action_replaced = None
        self.discriminator = None

        self.name = name
        if log_action_replaced is not None:
            self.log_action_replaced = log_action_replaced

    @property
    def name(self):
        """Gets the name of this CreatePolicyRequestBody.

        策略名称（策略名称只能由数字、字母和下划线组成，长度不能超过64为字符）

        :return: The name of this CreatePolicyRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreatePolicyRequestBody.

        策略名称（策略名称只能由数字、字母和下划线组成，长度不能超过64为字符）

        :param name: The name of this CreatePolicyRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def log_action_replaced(self):
        """Gets the log_action_replaced of this CreatePolicyRequestBody.

        cc规则和精准防护规则“防护动作”选择“仅记录”时，Web基础防护是否命中策略规则并阻断，默认为true

        :return: The log_action_replaced of this CreatePolicyRequestBody.
        :rtype: bool
        """
        return self._log_action_replaced

    @log_action_replaced.setter
    def log_action_replaced(self, log_action_replaced):
        """Sets the log_action_replaced of this CreatePolicyRequestBody.

        cc规则和精准防护规则“防护动作”选择“仅记录”时，Web基础防护是否命中策略规则并阻断，默认为true

        :param log_action_replaced: The log_action_replaced of this CreatePolicyRequestBody.
        :type log_action_replaced: bool
        """
        self._log_action_replaced = log_action_replaced

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
        if not isinstance(other, CreatePolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
