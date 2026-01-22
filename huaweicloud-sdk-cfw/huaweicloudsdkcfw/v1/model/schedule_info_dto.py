# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScheduleInfoDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_id': 'str',
        'name': 'str',
        'description': 'str',
        'periodic': 'list[ScheduleInfoDTOPeriodic]',
        'absolute': 'ScheduleInfoDTOAbsolute'
    }

    attribute_map = {
        'object_id': 'object_id',
        'name': 'name',
        'description': 'description',
        'periodic': 'periodic',
        'absolute': 'absolute'
    }

    def __init__(self, object_id=None, name=None, description=None, periodic=None, absolute=None):
        r"""ScheduleInfoDTO

        The model defined in huaweicloud sdk

        :param object_id: **参数解释**： 防护对象ID，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及
        :type object_id: str
        :param name: **参数解释**： 时间表名称 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type name: str
        :param description: **参数解释**： 时间表描述 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type description: str
        :param periodic: **参数解释**： 周期计划 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type periodic: list[:class:`huaweicloudsdkcfw.v1.ScheduleInfoDTOPeriodic`]
        :param absolute: 
        :type absolute: :class:`huaweicloudsdkcfw.v1.ScheduleInfoDTOAbsolute`
        """
        
        

        self._object_id = None
        self._name = None
        self._description = None
        self._periodic = None
        self._absolute = None
        self.discriminator = None

        self.object_id = object_id
        self.name = name
        if description is not None:
            self.description = description
        if periodic is not None:
            self.periodic = periodic
        if absolute is not None:
            self.absolute = absolute

    @property
    def object_id(self):
        r"""Gets the object_id of this ScheduleInfoDTO.

        **参数解释**： 防护对象ID，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :return: The object_id of this ScheduleInfoDTO.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this ScheduleInfoDTO.

        **参数解释**： 防护对象ID，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :param object_id: The object_id of this ScheduleInfoDTO.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def name(self):
        r"""Gets the name of this ScheduleInfoDTO.

        **参数解释**： 时间表名称 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The name of this ScheduleInfoDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ScheduleInfoDTO.

        **参数解释**： 时间表名称 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param name: The name of this ScheduleInfoDTO.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ScheduleInfoDTO.

        **参数解释**： 时间表描述 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The description of this ScheduleInfoDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ScheduleInfoDTO.

        **参数解释**： 时间表描述 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param description: The description of this ScheduleInfoDTO.
        :type description: str
        """
        self._description = description

    @property
    def periodic(self):
        r"""Gets the periodic of this ScheduleInfoDTO.

        **参数解释**： 周期计划 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The periodic of this ScheduleInfoDTO.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.ScheduleInfoDTOPeriodic`]
        """
        return self._periodic

    @periodic.setter
    def periodic(self, periodic):
        r"""Sets the periodic of this ScheduleInfoDTO.

        **参数解释**： 周期计划 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param periodic: The periodic of this ScheduleInfoDTO.
        :type periodic: list[:class:`huaweicloudsdkcfw.v1.ScheduleInfoDTOPeriodic`]
        """
        self._periodic = periodic

    @property
    def absolute(self):
        r"""Gets the absolute of this ScheduleInfoDTO.

        :return: The absolute of this ScheduleInfoDTO.
        :rtype: :class:`huaweicloudsdkcfw.v1.ScheduleInfoDTOAbsolute`
        """
        return self._absolute

    @absolute.setter
    def absolute(self, absolute):
        r"""Sets the absolute of this ScheduleInfoDTO.

        :param absolute: The absolute of this ScheduleInfoDTO.
        :type absolute: :class:`huaweicloudsdkcfw.v1.ScheduleInfoDTOAbsolute`
        """
        self._absolute = absolute

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
        if not isinstance(other, ScheduleInfoDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
