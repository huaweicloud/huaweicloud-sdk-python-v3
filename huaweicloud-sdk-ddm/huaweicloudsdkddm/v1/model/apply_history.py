# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplyHistory:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_id': 'str',
        'target_name': 'str',
        'apply_result': 'str',
        'applied_at': 'datetime',
        'error_code': 'str'
    }

    attribute_map = {
        'target_id': 'target_id',
        'target_name': 'target_name',
        'apply_result': 'apply_result',
        'applied_at': 'applied_at',
        'error_code': 'error_code'
    }

    def __init__(self, target_id=None, target_name=None, apply_result=None, applied_at=None, error_code=None):
        r"""ApplyHistory

        The model defined in huaweicloud sdk

        :param target_id: **参数解释**：  参数组ID。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，长度为36个字符。  **默认取值**：  不涉及。
        :type target_id: str
        :param target_name: **参数解释**：  参数组的名称。  **参数范围**：  不涉及。
        :type target_name: str
        :param apply_result: **参数解释**：  应用结果。  **参数范围**：  不涉及。
        :type apply_result: str
        :param applied_at: **参数解释**：  应用日期。  格式为yyyy-mm-dd Thh:mm:ssZ。  其中，T指定某个时间的开始；Z指示 UTC 时间。  **参数范围**：  不涉及。
        :type applied_at: datetime
        :param error_code: **参数解释**：  错误码。  **参数范围**：  不涉及。
        :type error_code: str
        """
        
        

        self._target_id = None
        self._target_name = None
        self._apply_result = None
        self._applied_at = None
        self._error_code = None
        self.discriminator = None

        if target_id is not None:
            self.target_id = target_id
        if target_name is not None:
            self.target_name = target_name
        if apply_result is not None:
            self.apply_result = apply_result
        if applied_at is not None:
            self.applied_at = applied_at
        if error_code is not None:
            self.error_code = error_code

    @property
    def target_id(self):
        r"""Gets the target_id of this ApplyHistory.

        **参数解释**：  参数组ID。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，长度为36个字符。  **默认取值**：  不涉及。

        :return: The target_id of this ApplyHistory.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        r"""Sets the target_id of this ApplyHistory.

        **参数解释**：  参数组ID。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，长度为36个字符。  **默认取值**：  不涉及。

        :param target_id: The target_id of this ApplyHistory.
        :type target_id: str
        """
        self._target_id = target_id

    @property
    def target_name(self):
        r"""Gets the target_name of this ApplyHistory.

        **参数解释**：  参数组的名称。  **参数范围**：  不涉及。

        :return: The target_name of this ApplyHistory.
        :rtype: str
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        r"""Sets the target_name of this ApplyHistory.

        **参数解释**：  参数组的名称。  **参数范围**：  不涉及。

        :param target_name: The target_name of this ApplyHistory.
        :type target_name: str
        """
        self._target_name = target_name

    @property
    def apply_result(self):
        r"""Gets the apply_result of this ApplyHistory.

        **参数解释**：  应用结果。  **参数范围**：  不涉及。

        :return: The apply_result of this ApplyHistory.
        :rtype: str
        """
        return self._apply_result

    @apply_result.setter
    def apply_result(self, apply_result):
        r"""Sets the apply_result of this ApplyHistory.

        **参数解释**：  应用结果。  **参数范围**：  不涉及。

        :param apply_result: The apply_result of this ApplyHistory.
        :type apply_result: str
        """
        self._apply_result = apply_result

    @property
    def applied_at(self):
        r"""Gets the applied_at of this ApplyHistory.

        **参数解释**：  应用日期。  格式为yyyy-mm-dd Thh:mm:ssZ。  其中，T指定某个时间的开始；Z指示 UTC 时间。  **参数范围**：  不涉及。

        :return: The applied_at of this ApplyHistory.
        :rtype: datetime
        """
        return self._applied_at

    @applied_at.setter
    def applied_at(self, applied_at):
        r"""Sets the applied_at of this ApplyHistory.

        **参数解释**：  应用日期。  格式为yyyy-mm-dd Thh:mm:ssZ。  其中，T指定某个时间的开始；Z指示 UTC 时间。  **参数范围**：  不涉及。

        :param applied_at: The applied_at of this ApplyHistory.
        :type applied_at: datetime
        """
        self._applied_at = applied_at

    @property
    def error_code(self):
        r"""Gets the error_code of this ApplyHistory.

        **参数解释**：  错误码。  **参数范围**：  不涉及。

        :return: The error_code of this ApplyHistory.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ApplyHistory.

        **参数解释**：  错误码。  **参数范围**：  不涉及。

        :param error_code: The error_code of this ApplyHistory.
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
        if not isinstance(other, ApplyHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
