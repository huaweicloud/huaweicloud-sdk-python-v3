# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplyHistoryInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'instance_name': 'str',
        'apply_result': 'str',
        'apply_time': 'str',
        'error_code': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'apply_result': 'apply_result',
        'apply_time': 'apply_time',
        'error_code': 'error_code'
    }

    def __init__(self, instance_id=None, instance_name=None, apply_result=None, apply_time=None, error_code=None):
        r"""ApplyHistoryInfo

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**：  参数组应用目标实例ID,，此参数是实例的唯一标识。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，长度为36个字符。  **默认取值**：  不涉及。
        :type instance_id: str
        :param instance_name: **参数解释**：  参数组应用目标实例名称  **约束限制**：  不涉及。  **取值范围**：  不涉及  **默认取值**：  不涉及。
        :type instance_name: str
        :param apply_result: **参数解释**：  参数组应用结果。  **约束限制**：  不涉及。  **取值范围**：  不涉及  **默认取值**：  不涉及。
        :type apply_result: str
        :param apply_time: **参数解释**：  参数组应用时间。  **约束限制**：  不涉及。  **取值范围**：  不涉及  **默认取值**：  不涉及。
        :type apply_time: str
        :param error_code: **参数解释**：  参数组应用错误码  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type error_code: str
        """
        
        

        self._instance_id = None
        self._instance_name = None
        self._apply_result = None
        self._apply_time = None
        self._error_code = None
        self.discriminator = None

        self.instance_id = instance_id
        self.instance_name = instance_name
        self.apply_result = apply_result
        self.apply_time = apply_time
        self.error_code = error_code

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ApplyHistoryInfo.

        **参数解释**：  参数组应用目标实例ID,，此参数是实例的唯一标识。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，长度为36个字符。  **默认取值**：  不涉及。

        :return: The instance_id of this ApplyHistoryInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ApplyHistoryInfo.

        **参数解释**：  参数组应用目标实例ID,，此参数是实例的唯一标识。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，长度为36个字符。  **默认取值**：  不涉及。

        :param instance_id: The instance_id of this ApplyHistoryInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this ApplyHistoryInfo.

        **参数解释**：  参数组应用目标实例名称  **约束限制**：  不涉及。  **取值范围**：  不涉及  **默认取值**：  不涉及。

        :return: The instance_name of this ApplyHistoryInfo.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this ApplyHistoryInfo.

        **参数解释**：  参数组应用目标实例名称  **约束限制**：  不涉及。  **取值范围**：  不涉及  **默认取值**：  不涉及。

        :param instance_name: The instance_name of this ApplyHistoryInfo.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def apply_result(self):
        r"""Gets the apply_result of this ApplyHistoryInfo.

        **参数解释**：  参数组应用结果。  **约束限制**：  不涉及。  **取值范围**：  不涉及  **默认取值**：  不涉及。

        :return: The apply_result of this ApplyHistoryInfo.
        :rtype: str
        """
        return self._apply_result

    @apply_result.setter
    def apply_result(self, apply_result):
        r"""Sets the apply_result of this ApplyHistoryInfo.

        **参数解释**：  参数组应用结果。  **约束限制**：  不涉及。  **取值范围**：  不涉及  **默认取值**：  不涉及。

        :param apply_result: The apply_result of this ApplyHistoryInfo.
        :type apply_result: str
        """
        self._apply_result = apply_result

    @property
    def apply_time(self):
        r"""Gets the apply_time of this ApplyHistoryInfo.

        **参数解释**：  参数组应用时间。  **约束限制**：  不涉及。  **取值范围**：  不涉及  **默认取值**：  不涉及。

        :return: The apply_time of this ApplyHistoryInfo.
        :rtype: str
        """
        return self._apply_time

    @apply_time.setter
    def apply_time(self, apply_time):
        r"""Sets the apply_time of this ApplyHistoryInfo.

        **参数解释**：  参数组应用时间。  **约束限制**：  不涉及。  **取值范围**：  不涉及  **默认取值**：  不涉及。

        :param apply_time: The apply_time of this ApplyHistoryInfo.
        :type apply_time: str
        """
        self._apply_time = apply_time

    @property
    def error_code(self):
        r"""Gets the error_code of this ApplyHistoryInfo.

        **参数解释**：  参数组应用错误码  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The error_code of this ApplyHistoryInfo.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ApplyHistoryInfo.

        **参数解释**：  参数组应用错误码  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param error_code: The error_code of this ApplyHistoryInfo.
        :type error_code: str
        """
        self._error_code = error_code

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
        if not isinstance(other, ApplyHistoryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
