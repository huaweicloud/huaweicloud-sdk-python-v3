# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FuseConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_rate_fuse_enable': 'bool',
        'error_rate_threshold': 'float'
    }

    attribute_map = {
        'error_rate_fuse_enable': 'error_rate_fuse_enable',
        'error_rate_threshold': 'error_rate_threshold'
    }

    def __init__(self, error_rate_fuse_enable=None, error_rate_threshold=None):
        r"""FuseConfig

        The model defined in huaweicloud sdk

        :param error_rate_fuse_enable: **参数解释：** 错误率熔断开关。 **约束限制：** 不涉及。 **取值范围：** * true：开启错误率熔断。 * false：不打开错误率熔断。 **默认取值：** false：不打开错误率熔断。
        :type error_rate_fuse_enable: bool
        :param error_rate_threshold: **参数解释：** 错误率熔断阈值。 **约束限制：** 不涉及。 **取值范围：** (0, 1]（最多支持2位小数，小数点后第3位做四舍五入处理）。 **默认取值：** 不涉及。
        :type error_rate_threshold: float
        """
        
        

        self._error_rate_fuse_enable = None
        self._error_rate_threshold = None
        self.discriminator = None

        if error_rate_fuse_enable is not None:
            self.error_rate_fuse_enable = error_rate_fuse_enable
        if error_rate_threshold is not None:
            self.error_rate_threshold = error_rate_threshold

    @property
    def error_rate_fuse_enable(self):
        r"""Gets the error_rate_fuse_enable of this FuseConfig.

        **参数解释：** 错误率熔断开关。 **约束限制：** 不涉及。 **取值范围：** * true：开启错误率熔断。 * false：不打开错误率熔断。 **默认取值：** false：不打开错误率熔断。

        :return: The error_rate_fuse_enable of this FuseConfig.
        :rtype: bool
        """
        return self._error_rate_fuse_enable

    @error_rate_fuse_enable.setter
    def error_rate_fuse_enable(self, error_rate_fuse_enable):
        r"""Sets the error_rate_fuse_enable of this FuseConfig.

        **参数解释：** 错误率熔断开关。 **约束限制：** 不涉及。 **取值范围：** * true：开启错误率熔断。 * false：不打开错误率熔断。 **默认取值：** false：不打开错误率熔断。

        :param error_rate_fuse_enable: The error_rate_fuse_enable of this FuseConfig.
        :type error_rate_fuse_enable: bool
        """
        self._error_rate_fuse_enable = error_rate_fuse_enable

    @property
    def error_rate_threshold(self):
        r"""Gets the error_rate_threshold of this FuseConfig.

        **参数解释：** 错误率熔断阈值。 **约束限制：** 不涉及。 **取值范围：** (0, 1]（最多支持2位小数，小数点后第3位做四舍五入处理）。 **默认取值：** 不涉及。

        :return: The error_rate_threshold of this FuseConfig.
        :rtype: float
        """
        return self._error_rate_threshold

    @error_rate_threshold.setter
    def error_rate_threshold(self, error_rate_threshold):
        r"""Sets the error_rate_threshold of this FuseConfig.

        **参数解释：** 错误率熔断阈值。 **约束限制：** 不涉及。 **取值范围：** (0, 1]（最多支持2位小数，小数点后第3位做四舍五入处理）。 **默认取值：** 不涉及。

        :param error_rate_threshold: The error_rate_threshold of this FuseConfig.
        :type error_rate_threshold: float
        """
        self._error_rate_threshold = error_rate_threshold

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
        if not isinstance(other, FuseConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
