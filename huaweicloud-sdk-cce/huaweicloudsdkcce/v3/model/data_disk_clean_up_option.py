# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataDiskCleanUpOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool',
        'on_failure': 'str'
    }

    attribute_map = {
        'enable': 'enable',
        'on_failure': 'onFailure'
    }

    def __init__(self, enable=None, on_failure=None):
        r"""DataDiskCleanUpOption

        The model defined in huaweicloud sdk

        :param enable: **参数解释：** 该参数用于控制腾挪节点时，是否擦除节点的除系统盘外的数据盘。 **约束限制：** 不涉及 **取值范围：** - false：腾挪节点时，不擦除节点的除系统盘外的数据盘。           - true：腾挪节点时，擦除节点的除系统盘外的数据盘。  **默认取值：** false
        :type enable: bool
        :param on_failure: **参数解释：** 该参数用于控制腾挪节点时，擦除节点的数据盘失败时的处理策略。 **约束限制：** 不涉及 **取值范围：** - ignore：表示清理数据盘失败时忽略错误，继续执行。 - abort：表示清理数据盘失败时立即停止，并向上报错。  **默认取值：** ignore
        :type on_failure: str
        """
        
        

        self._enable = None
        self._on_failure = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        if on_failure is not None:
            self.on_failure = on_failure

    @property
    def enable(self):
        r"""Gets the enable of this DataDiskCleanUpOption.

        **参数解释：** 该参数用于控制腾挪节点时，是否擦除节点的除系统盘外的数据盘。 **约束限制：** 不涉及 **取值范围：** - false：腾挪节点时，不擦除节点的除系统盘外的数据盘。           - true：腾挪节点时，擦除节点的除系统盘外的数据盘。  **默认取值：** false

        :return: The enable of this DataDiskCleanUpOption.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this DataDiskCleanUpOption.

        **参数解释：** 该参数用于控制腾挪节点时，是否擦除节点的除系统盘外的数据盘。 **约束限制：** 不涉及 **取值范围：** - false：腾挪节点时，不擦除节点的除系统盘外的数据盘。           - true：腾挪节点时，擦除节点的除系统盘外的数据盘。  **默认取值：** false

        :param enable: The enable of this DataDiskCleanUpOption.
        :type enable: bool
        """
        self._enable = enable

    @property
    def on_failure(self):
        r"""Gets the on_failure of this DataDiskCleanUpOption.

        **参数解释：** 该参数用于控制腾挪节点时，擦除节点的数据盘失败时的处理策略。 **约束限制：** 不涉及 **取值范围：** - ignore：表示清理数据盘失败时忽略错误，继续执行。 - abort：表示清理数据盘失败时立即停止，并向上报错。  **默认取值：** ignore

        :return: The on_failure of this DataDiskCleanUpOption.
        :rtype: str
        """
        return self._on_failure

    @on_failure.setter
    def on_failure(self, on_failure):
        r"""Sets the on_failure of this DataDiskCleanUpOption.

        **参数解释：** 该参数用于控制腾挪节点时，擦除节点的数据盘失败时的处理策略。 **约束限制：** 不涉及 **取值范围：** - ignore：表示清理数据盘失败时忽略错误，继续执行。 - abort：表示清理数据盘失败时立即停止，并向上报错。  **默认取值：** ignore

        :param on_failure: The on_failure of this DataDiskCleanUpOption.
        :type on_failure: str
        """
        self._on_failure = on_failure

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
        if not isinstance(other, DataDiskCleanUpOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
