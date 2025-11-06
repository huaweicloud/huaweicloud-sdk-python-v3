# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradeDatabaseVersionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'upgrade_mode': 'str',
        'is_delayed': 'bool'
    }

    attribute_map = {
        'upgrade_mode': 'upgrade_mode',
        'is_delayed': 'is_delayed'
    }

    def __init__(self, upgrade_mode=None, is_delayed=None):
        r"""UpgradeDatabaseVersionRequestBody

        The model defined in huaweicloud sdk

        :param upgrade_mode: **参数解释：** 升级模式。 **约束限制：** 不涉及。 **取值范围：** minimized_interrupt_time：表示中断时间最短优先模式：升级过程对业务影响相对较小的升级方式。 minimized_upgrade_time：表示升级时长最短优先模式：升级过程时长相对较快的升级方式。 **默认取值：** minimized_interrupt_time。
        :type upgrade_mode: str
        :param is_delayed: **参数解释：** 实例是否在可维护时间窗内自动升级。 **约束限制：** 不涉及。 **取值范围：** true：表示延迟升级，实例将在可维护时间窗内自动升级。 false：表示立即升级。 **默认取值：** false。
        :type is_delayed: bool
        """
        
        

        self._upgrade_mode = None
        self._is_delayed = None
        self.discriminator = None

        if upgrade_mode is not None:
            self.upgrade_mode = upgrade_mode
        if is_delayed is not None:
            self.is_delayed = is_delayed

    @property
    def upgrade_mode(self):
        r"""Gets the upgrade_mode of this UpgradeDatabaseVersionRequestBody.

        **参数解释：** 升级模式。 **约束限制：** 不涉及。 **取值范围：** minimized_interrupt_time：表示中断时间最短优先模式：升级过程对业务影响相对较小的升级方式。 minimized_upgrade_time：表示升级时长最短优先模式：升级过程时长相对较快的升级方式。 **默认取值：** minimized_interrupt_time。

        :return: The upgrade_mode of this UpgradeDatabaseVersionRequestBody.
        :rtype: str
        """
        return self._upgrade_mode

    @upgrade_mode.setter
    def upgrade_mode(self, upgrade_mode):
        r"""Sets the upgrade_mode of this UpgradeDatabaseVersionRequestBody.

        **参数解释：** 升级模式。 **约束限制：** 不涉及。 **取值范围：** minimized_interrupt_time：表示中断时间最短优先模式：升级过程对业务影响相对较小的升级方式。 minimized_upgrade_time：表示升级时长最短优先模式：升级过程时长相对较快的升级方式。 **默认取值：** minimized_interrupt_time。

        :param upgrade_mode: The upgrade_mode of this UpgradeDatabaseVersionRequestBody.
        :type upgrade_mode: str
        """
        self._upgrade_mode = upgrade_mode

    @property
    def is_delayed(self):
        r"""Gets the is_delayed of this UpgradeDatabaseVersionRequestBody.

        **参数解释：** 实例是否在可维护时间窗内自动升级。 **约束限制：** 不涉及。 **取值范围：** true：表示延迟升级，实例将在可维护时间窗内自动升级。 false：表示立即升级。 **默认取值：** false。

        :return: The is_delayed of this UpgradeDatabaseVersionRequestBody.
        :rtype: bool
        """
        return self._is_delayed

    @is_delayed.setter
    def is_delayed(self, is_delayed):
        r"""Sets the is_delayed of this UpgradeDatabaseVersionRequestBody.

        **参数解释：** 实例是否在可维护时间窗内自动升级。 **约束限制：** 不涉及。 **取值范围：** true：表示延迟升级，实例将在可维护时间窗内自动升级。 false：表示立即升级。 **默认取值：** false。

        :param is_delayed: The is_delayed of this UpgradeDatabaseVersionRequestBody.
        :type is_delayed: bool
        """
        self._is_delayed = is_delayed

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
        if not isinstance(other, UpgradeDatabaseVersionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
