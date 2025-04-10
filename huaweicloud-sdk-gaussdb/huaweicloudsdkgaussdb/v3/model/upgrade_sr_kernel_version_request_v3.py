# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradeSrKernelVersionRequestV3:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'delay': 'str',
        'is_skip_validate': 'str'
    }

    attribute_map = {
        'delay': 'delay',
        'is_skip_validate': 'is_skip_validate'
    }

    def __init__(self, delay=None, is_skip_validate=None):
        r"""UpgradeSrKernelVersionRequestV3

        The model defined in huaweicloud sdk

        :param delay: **参数解释**： 是否延时升级。  **约束限制**： 不涉及  **取值范围**： - true - false  **默认取值**： false。
        :type delay: str
        :param is_skip_validate: **参数解释**： 是否跳过升级校验。  **约束限制**： 不涉及  **取值范围**： - true - false  **默认取值**： false。
        :type is_skip_validate: str
        """
        
        

        self._delay = None
        self._is_skip_validate = None
        self.discriminator = None

        if delay is not None:
            self.delay = delay
        if is_skip_validate is not None:
            self.is_skip_validate = is_skip_validate

    @property
    def delay(self):
        r"""Gets the delay of this UpgradeSrKernelVersionRequestV3.

        **参数解释**： 是否延时升级。  **约束限制**： 不涉及  **取值范围**： - true - false  **默认取值**： false。

        :return: The delay of this UpgradeSrKernelVersionRequestV3.
        :rtype: str
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        r"""Sets the delay of this UpgradeSrKernelVersionRequestV3.

        **参数解释**： 是否延时升级。  **约束限制**： 不涉及  **取值范围**： - true - false  **默认取值**： false。

        :param delay: The delay of this UpgradeSrKernelVersionRequestV3.
        :type delay: str
        """
        self._delay = delay

    @property
    def is_skip_validate(self):
        r"""Gets the is_skip_validate of this UpgradeSrKernelVersionRequestV3.

        **参数解释**： 是否跳过升级校验。  **约束限制**： 不涉及  **取值范围**： - true - false  **默认取值**： false。

        :return: The is_skip_validate of this UpgradeSrKernelVersionRequestV3.
        :rtype: str
        """
        return self._is_skip_validate

    @is_skip_validate.setter
    def is_skip_validate(self, is_skip_validate):
        r"""Sets the is_skip_validate of this UpgradeSrKernelVersionRequestV3.

        **参数解释**： 是否跳过升级校验。  **约束限制**： 不涉及  **取值范围**： - true - false  **默认取值**： false。

        :param is_skip_validate: The is_skip_validate of this UpgradeSrKernelVersionRequestV3.
        :type is_skip_validate: str
        """
        self._is_skip_validate = is_skip_validate

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
        if not isinstance(other, UpgradeSrKernelVersionRequestV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
