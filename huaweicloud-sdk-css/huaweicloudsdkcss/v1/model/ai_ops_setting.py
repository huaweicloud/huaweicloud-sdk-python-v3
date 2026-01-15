# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AiOpsSetting:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'check_type': 'str',
        'check_items': 'list[str]',
        'period': 'str'
    }

    attribute_map = {
        'check_type': 'check_type',
        'check_items': 'check_items',
        'period': 'period'
    }

    def __init__(self, check_type=None, check_items=None, period=None):
        r"""AiOpsSetting

        The model defined in huaweicloud sdk

        :param check_type: **参数解释**： 检测类型。 **约束限制**： 不涉及 **取值范围**： - full_detection：  全量检测项。 - unavailability_detection： 集群不可用检测项。 - partial_detection： 全量检测项中选取其中部分检测项进行检测，具体检测项需要设置check_items。 **默认取值**： 不涉及
        :type check_type: str
        :param check_items: **参数解释**： 全量检测项中选取其中部分检测项进行检测，输入检测项列表。 **约束限制**： 当check_type为partial_detection时有效 **取值范围**： 通过智能运维ShowAiOpsDetector获取最新支持的检测项，输入检测项id字符串列表 **默认取值**： 不涉及
        :type check_items: list[str]
        :param period: **参数解释**： 智能运维自动检测时间，格式为时间加时区，例如：\&quot;00:00 GMT+08:00\&quot;。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type period: str
        """
        
        

        self._check_type = None
        self._check_items = None
        self._period = None
        self.discriminator = None

        self.check_type = check_type
        if check_items is not None:
            self.check_items = check_items
        self.period = period

    @property
    def check_type(self):
        r"""Gets the check_type of this AiOpsSetting.

        **参数解释**： 检测类型。 **约束限制**： 不涉及 **取值范围**： - full_detection：  全量检测项。 - unavailability_detection： 集群不可用检测项。 - partial_detection： 全量检测项中选取其中部分检测项进行检测，具体检测项需要设置check_items。 **默认取值**： 不涉及

        :return: The check_type of this AiOpsSetting.
        :rtype: str
        """
        return self._check_type

    @check_type.setter
    def check_type(self, check_type):
        r"""Sets the check_type of this AiOpsSetting.

        **参数解释**： 检测类型。 **约束限制**： 不涉及 **取值范围**： - full_detection：  全量检测项。 - unavailability_detection： 集群不可用检测项。 - partial_detection： 全量检测项中选取其中部分检测项进行检测，具体检测项需要设置check_items。 **默认取值**： 不涉及

        :param check_type: The check_type of this AiOpsSetting.
        :type check_type: str
        """
        self._check_type = check_type

    @property
    def check_items(self):
        r"""Gets the check_items of this AiOpsSetting.

        **参数解释**： 全量检测项中选取其中部分检测项进行检测，输入检测项列表。 **约束限制**： 当check_type为partial_detection时有效 **取值范围**： 通过智能运维ShowAiOpsDetector获取最新支持的检测项，输入检测项id字符串列表 **默认取值**： 不涉及

        :return: The check_items of this AiOpsSetting.
        :rtype: list[str]
        """
        return self._check_items

    @check_items.setter
    def check_items(self, check_items):
        r"""Sets the check_items of this AiOpsSetting.

        **参数解释**： 全量检测项中选取其中部分检测项进行检测，输入检测项列表。 **约束限制**： 当check_type为partial_detection时有效 **取值范围**： 通过智能运维ShowAiOpsDetector获取最新支持的检测项，输入检测项id字符串列表 **默认取值**： 不涉及

        :param check_items: The check_items of this AiOpsSetting.
        :type check_items: list[str]
        """
        self._check_items = check_items

    @property
    def period(self):
        r"""Gets the period of this AiOpsSetting.

        **参数解释**： 智能运维自动检测时间，格式为时间加时区，例如：\"00:00 GMT+08:00\"。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The period of this AiOpsSetting.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this AiOpsSetting.

        **参数解释**： 智能运维自动检测时间，格式为时间加时区，例如：\"00:00 GMT+08:00\"。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param period: The period of this AiOpsSetting.
        :type period: str
        """
        self._period = period

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
        if not isinstance(other, AiOpsSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
