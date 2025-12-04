# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowKafkaScalePreCheckInfoResponseBody:

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
        'success': 'bool',
        'reason': 'str',
        'risk': 'str'
    }

    attribute_map = {
        'name': 'name',
        'success': 'success',
        'reason': 'reason',
        'risk': 'risk'
    }

    def __init__(self, name=None, success=None, reason=None, risk=None):
        r"""ShowKafkaScalePreCheckInfoResponseBody

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 检查项名称。  **取值范围**： 不涉及。
        :type name: str
        :param success: **参数解释**： 检查项状态。 **取值范围**： - true：正常。 - false：异常。
        :type success: bool
        :param reason: **参数解释**： 失败原因。    **取值范围**： 不涉及。
        :type reason: str
        :param risk: **参数解释**： 风险等级。   **取值范围**： - low：低风险。 - medium：中风险。 - high：高风险。
        :type risk: str
        """
        
        

        self._name = None
        self._success = None
        self._reason = None
        self._risk = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if success is not None:
            self.success = success
        if reason is not None:
            self.reason = reason
        if risk is not None:
            self.risk = risk

    @property
    def name(self):
        r"""Gets the name of this ShowKafkaScalePreCheckInfoResponseBody.

        **参数解释**： 检查项名称。  **取值范围**： 不涉及。

        :return: The name of this ShowKafkaScalePreCheckInfoResponseBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowKafkaScalePreCheckInfoResponseBody.

        **参数解释**： 检查项名称。  **取值范围**： 不涉及。

        :param name: The name of this ShowKafkaScalePreCheckInfoResponseBody.
        :type name: str
        """
        self._name = name

    @property
    def success(self):
        r"""Gets the success of this ShowKafkaScalePreCheckInfoResponseBody.

        **参数解释**： 检查项状态。 **取值范围**： - true：正常。 - false：异常。

        :return: The success of this ShowKafkaScalePreCheckInfoResponseBody.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this ShowKafkaScalePreCheckInfoResponseBody.

        **参数解释**： 检查项状态。 **取值范围**： - true：正常。 - false：异常。

        :param success: The success of this ShowKafkaScalePreCheckInfoResponseBody.
        :type success: bool
        """
        self._success = success

    @property
    def reason(self):
        r"""Gets the reason of this ShowKafkaScalePreCheckInfoResponseBody.

        **参数解释**： 失败原因。    **取值范围**： 不涉及。

        :return: The reason of this ShowKafkaScalePreCheckInfoResponseBody.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this ShowKafkaScalePreCheckInfoResponseBody.

        **参数解释**： 失败原因。    **取值范围**： 不涉及。

        :param reason: The reason of this ShowKafkaScalePreCheckInfoResponseBody.
        :type reason: str
        """
        self._reason = reason

    @property
    def risk(self):
        r"""Gets the risk of this ShowKafkaScalePreCheckInfoResponseBody.

        **参数解释**： 风险等级。   **取值范围**： - low：低风险。 - medium：中风险。 - high：高风险。

        :return: The risk of this ShowKafkaScalePreCheckInfoResponseBody.
        :rtype: str
        """
        return self._risk

    @risk.setter
    def risk(self, risk):
        r"""Sets the risk of this ShowKafkaScalePreCheckInfoResponseBody.

        **参数解释**： 风险等级。   **取值范围**： - low：低风险。 - medium：中风险。 - high：高风险。

        :param risk: The risk of this ShowKafkaScalePreCheckInfoResponseBody.
        :type risk: str
        """
        self._risk = risk

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
        if not isinstance(other, ShowKafkaScalePreCheckInfoResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
