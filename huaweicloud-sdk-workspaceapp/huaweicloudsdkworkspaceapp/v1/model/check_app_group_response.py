# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckAppGroupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'bool',
        'validate_rule': 'str'
    }

    attribute_map = {
        'result': 'result',
        'validate_rule': 'validate_rule'
    }

    def __init__(self, result=None, validate_rule=None):
        r"""CheckAppGroupResponse

        The model defined in huaweicloud sdk

        :param result: 校验结果。
        :type result: bool
        :param validate_rule: 校验类型： * &#x60;naming&#x60; - 命名规范 * &#x60;duplicate&#x60; - 重复
        :type validate_rule: str
        """
        
        super().__init__()

        self._result = None
        self._validate_rule = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if validate_rule is not None:
            self.validate_rule = validate_rule

    @property
    def result(self):
        r"""Gets the result of this CheckAppGroupResponse.

        校验结果。

        :return: The result of this CheckAppGroupResponse.
        :rtype: bool
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this CheckAppGroupResponse.

        校验结果。

        :param result: The result of this CheckAppGroupResponse.
        :type result: bool
        """
        self._result = result

    @property
    def validate_rule(self):
        r"""Gets the validate_rule of this CheckAppGroupResponse.

        校验类型： * `naming` - 命名规范 * `duplicate` - 重复

        :return: The validate_rule of this CheckAppGroupResponse.
        :rtype: str
        """
        return self._validate_rule

    @validate_rule.setter
    def validate_rule(self, validate_rule):
        r"""Sets the validate_rule of this CheckAppGroupResponse.

        校验类型： * `naming` - 命名规范 * `duplicate` - 重复

        :param validate_rule: The validate_rule of this CheckAppGroupResponse.
        :type validate_rule: str
        """
        self._validate_rule = validate_rule

    def to_dict(self):
        import warnings
        warnings.warn("CheckAppGroupResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, CheckAppGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
