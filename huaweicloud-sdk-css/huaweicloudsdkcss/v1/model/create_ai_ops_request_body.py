# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAiOpsRequestBody:

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
        'name': 'str',
        'description': 'str',
        'alarm': 'CreateAiOpsRequestBodyAlarm'
    }

    attribute_map = {
        'check_type': 'check_type',
        'check_items': 'check_items',
        'name': 'name',
        'description': 'description',
        'alarm': 'alarm'
    }

    def __init__(self, check_type=None, check_items=None, name=None, description=None, alarm=None):
        r"""CreateAiOpsRequestBody

        The model defined in huaweicloud sdk

        :param check_type: **参数解释**： 检测类型 **约束限制**： 不涉及 **取值范围**： - full_detection  全量检测项 - unavailability_detection 集群不可用检测项 - partial_detection 全量检测项中选取其中部分检测项进行检测，具体检测项需要设置check_items  **默认取值**： 不涉及
        :type check_type: str
        :param check_items: **参数解释**： 全量检测项中选取其中部分检测项进行检测，输入检测项列表。 **约束限制**： 当check_type为partial_detection时有效 **取值范围**： 通过智能运维ShowAiOpsDetector获取最新支持的检测项，输入检测项id字符串列表 **默认取值**： 不涉及
        :type check_items: list[str]
        :param name: **参数解释**： 检测报告名称，支持自定义检测名。 **约束限制**： 不涉及 **取值范围**： 4～64个字符，只能包含数字、字母、中划线和下划线，且必须以字母开头。 **默认取值**： 不涉及
        :type name: str
        :param description: **参数解释**： 检测报告描述，支持自定义检测描述 **约束限制**： 不涉及 **取值范围**： 0~255个字符 **默认取值**： 不涉及
        :type description: str
        :param alarm: 
        :type alarm: :class:`huaweicloudsdkcss.v1.CreateAiOpsRequestBodyAlarm`
        """
        
        

        self._check_type = None
        self._check_items = None
        self._name = None
        self._description = None
        self._alarm = None
        self.discriminator = None

        if check_type is not None:
            self.check_type = check_type
        if check_items is not None:
            self.check_items = check_items
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if alarm is not None:
            self.alarm = alarm

    @property
    def check_type(self):
        r"""Gets the check_type of this CreateAiOpsRequestBody.

        **参数解释**： 检测类型 **约束限制**： 不涉及 **取值范围**： - full_detection  全量检测项 - unavailability_detection 集群不可用检测项 - partial_detection 全量检测项中选取其中部分检测项进行检测，具体检测项需要设置check_items  **默认取值**： 不涉及

        :return: The check_type of this CreateAiOpsRequestBody.
        :rtype: str
        """
        return self._check_type

    @check_type.setter
    def check_type(self, check_type):
        r"""Sets the check_type of this CreateAiOpsRequestBody.

        **参数解释**： 检测类型 **约束限制**： 不涉及 **取值范围**： - full_detection  全量检测项 - unavailability_detection 集群不可用检测项 - partial_detection 全量检测项中选取其中部分检测项进行检测，具体检测项需要设置check_items  **默认取值**： 不涉及

        :param check_type: The check_type of this CreateAiOpsRequestBody.
        :type check_type: str
        """
        self._check_type = check_type

    @property
    def check_items(self):
        r"""Gets the check_items of this CreateAiOpsRequestBody.

        **参数解释**： 全量检测项中选取其中部分检测项进行检测，输入检测项列表。 **约束限制**： 当check_type为partial_detection时有效 **取值范围**： 通过智能运维ShowAiOpsDetector获取最新支持的检测项，输入检测项id字符串列表 **默认取值**： 不涉及

        :return: The check_items of this CreateAiOpsRequestBody.
        :rtype: list[str]
        """
        return self._check_items

    @check_items.setter
    def check_items(self, check_items):
        r"""Sets the check_items of this CreateAiOpsRequestBody.

        **参数解释**： 全量检测项中选取其中部分检测项进行检测，输入检测项列表。 **约束限制**： 当check_type为partial_detection时有效 **取值范围**： 通过智能运维ShowAiOpsDetector获取最新支持的检测项，输入检测项id字符串列表 **默认取值**： 不涉及

        :param check_items: The check_items of this CreateAiOpsRequestBody.
        :type check_items: list[str]
        """
        self._check_items = check_items

    @property
    def name(self):
        r"""Gets the name of this CreateAiOpsRequestBody.

        **参数解释**： 检测报告名称，支持自定义检测名。 **约束限制**： 不涉及 **取值范围**： 4～64个字符，只能包含数字、字母、中划线和下划线，且必须以字母开头。 **默认取值**： 不涉及

        :return: The name of this CreateAiOpsRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateAiOpsRequestBody.

        **参数解释**： 检测报告名称，支持自定义检测名。 **约束限制**： 不涉及 **取值范围**： 4～64个字符，只能包含数字、字母、中划线和下划线，且必须以字母开头。 **默认取值**： 不涉及

        :param name: The name of this CreateAiOpsRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateAiOpsRequestBody.

        **参数解释**： 检测报告描述，支持自定义检测描述 **约束限制**： 不涉及 **取值范围**： 0~255个字符 **默认取值**： 不涉及

        :return: The description of this CreateAiOpsRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateAiOpsRequestBody.

        **参数解释**： 检测报告描述，支持自定义检测描述 **约束限制**： 不涉及 **取值范围**： 0~255个字符 **默认取值**： 不涉及

        :param description: The description of this CreateAiOpsRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def alarm(self):
        r"""Gets the alarm of this CreateAiOpsRequestBody.

        :return: The alarm of this CreateAiOpsRequestBody.
        :rtype: :class:`huaweicloudsdkcss.v1.CreateAiOpsRequestBodyAlarm`
        """
        return self._alarm

    @alarm.setter
    def alarm(self, alarm):
        r"""Sets the alarm of this CreateAiOpsRequestBody.

        :param alarm: The alarm of this CreateAiOpsRequestBody.
        :type alarm: :class:`huaweicloudsdkcss.v1.CreateAiOpsRequestBodyAlarm`
        """
        self._alarm = alarm

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
        if not isinstance(other, CreateAiOpsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
