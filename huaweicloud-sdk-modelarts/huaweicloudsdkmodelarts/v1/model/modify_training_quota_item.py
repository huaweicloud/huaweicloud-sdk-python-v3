# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyTrainingQuotaItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource': 'str',
        'quota': 'int',
        'used': 'int',
        'extra_info': 'str'
    }

    attribute_map = {
        'resource': 'resource',
        'quota': 'quota',
        'used': 'used',
        'extra_info': 'extra_info'
    }

    def __init__(self, resource=None, quota=None, used=None, extra_info=None):
        r"""ModifyTrainingQuotaItem

        The model defined in huaweicloud sdk

        :param resource: **参数解释**：配额的资源类型。 **约束限制**：不涉及。 **取值范围**：枚举值如下： - job-num: 作业个数配额 - visual-job-num: 可视化作业个数配额 - job-retention-enabled: 用户级作业自动老化开关 - job-num-quota-notify: 配额告警SMN通知配置 **默认取值**：不涉及。
        :type resource: str
        :param quota: **参数解释**：配额个数。 **约束限制**：取值约束因资源类型而异：job-retention-enabled取值0（关闭）或1（开启）；job-num-quota-notify固定为0，通知主题URN存于extra_info；其余资源类型要求不小于1。 **取值范围**：0 ~ 2147483647。 **默认取值**：不涉及。
        :type quota: int
        :param used: **参数解释**：已使用的个数。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type used: int
        :param extra_info: **参数解释**：配额的额外信息。 **约束限制**：当resource为job-num-quota-notify时，该字段存储SMN通知主题URN。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type extra_info: str
        """
        
        

        self._resource = None
        self._quota = None
        self._used = None
        self._extra_info = None
        self.discriminator = None

        self.resource = resource
        self.quota = quota
        if used is not None:
            self.used = used
        if extra_info is not None:
            self.extra_info = extra_info

    @property
    def resource(self):
        r"""Gets the resource of this ModifyTrainingQuotaItem.

        **参数解释**：配额的资源类型。 **约束限制**：不涉及。 **取值范围**：枚举值如下： - job-num: 作业个数配额 - visual-job-num: 可视化作业个数配额 - job-retention-enabled: 用户级作业自动老化开关 - job-num-quota-notify: 配额告警SMN通知配置 **默认取值**：不涉及。

        :return: The resource of this ModifyTrainingQuotaItem.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        r"""Sets the resource of this ModifyTrainingQuotaItem.

        **参数解释**：配额的资源类型。 **约束限制**：不涉及。 **取值范围**：枚举值如下： - job-num: 作业个数配额 - visual-job-num: 可视化作业个数配额 - job-retention-enabled: 用户级作业自动老化开关 - job-num-quota-notify: 配额告警SMN通知配置 **默认取值**：不涉及。

        :param resource: The resource of this ModifyTrainingQuotaItem.
        :type resource: str
        """
        self._resource = resource

    @property
    def quota(self):
        r"""Gets the quota of this ModifyTrainingQuotaItem.

        **参数解释**：配额个数。 **约束限制**：取值约束因资源类型而异：job-retention-enabled取值0（关闭）或1（开启）；job-num-quota-notify固定为0，通知主题URN存于extra_info；其余资源类型要求不小于1。 **取值范围**：0 ~ 2147483647。 **默认取值**：不涉及。

        :return: The quota of this ModifyTrainingQuotaItem.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        r"""Sets the quota of this ModifyTrainingQuotaItem.

        **参数解释**：配额个数。 **约束限制**：取值约束因资源类型而异：job-retention-enabled取值0（关闭）或1（开启）；job-num-quota-notify固定为0，通知主题URN存于extra_info；其余资源类型要求不小于1。 **取值范围**：0 ~ 2147483647。 **默认取值**：不涉及。

        :param quota: The quota of this ModifyTrainingQuotaItem.
        :type quota: int
        """
        self._quota = quota

    @property
    def used(self):
        r"""Gets the used of this ModifyTrainingQuotaItem.

        **参数解释**：已使用的个数。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The used of this ModifyTrainingQuotaItem.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        r"""Sets the used of this ModifyTrainingQuotaItem.

        **参数解释**：已使用的个数。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param used: The used of this ModifyTrainingQuotaItem.
        :type used: int
        """
        self._used = used

    @property
    def extra_info(self):
        r"""Gets the extra_info of this ModifyTrainingQuotaItem.

        **参数解释**：配额的额外信息。 **约束限制**：当resource为job-num-quota-notify时，该字段存储SMN通知主题URN。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The extra_info of this ModifyTrainingQuotaItem.
        :rtype: str
        """
        return self._extra_info

    @extra_info.setter
    def extra_info(self, extra_info):
        r"""Sets the extra_info of this ModifyTrainingQuotaItem.

        **参数解释**：配额的额外信息。 **约束限制**：当resource为job-num-quota-notify时，该字段存储SMN通知主题URN。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param extra_info: The extra_info of this ModifyTrainingQuotaItem.
        :type extra_info: str
        """
        self._extra_info = extra_info

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
        if not isinstance(other, ModifyTrainingQuotaItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
