# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScheduleVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'schedule_id': 'str',
        'name': 'str',
        'description': 'str',
        'ref_count': 'int',
        'periodic': 'list[ScheduleVOPeriodic]',
        'absolute': 'ScheduleVOAbsolute'
    }

    attribute_map = {
        'schedule_id': 'schedule_id',
        'name': 'name',
        'description': 'description',
        'ref_count': 'ref_count',
        'periodic': 'periodic',
        'absolute': 'absolute'
    }

    def __init__(self, schedule_id=None, name=None, description=None, ref_count=None, periodic=None, absolute=None):
        r"""ScheduleVO

        The model defined in huaweicloud sdk

        :param schedule_id: **参数解释**： 时间表ID **取值范围**： 不涉及
        :type schedule_id: str
        :param name: **参数解释**： 时间表名称 **取值范围**： 不涉及
        :type name: str
        :param description: **参数解释**： 时间表描述 **取值范围**： 不涉及
        :type description: str
        :param ref_count: **参数解释**： 引用次数 **取值范围**： 不涉及
        :type ref_count: int
        :param periodic: **参数解释**： 周期计划 **取值范围**： 不涉及
        :type periodic: list[:class:`huaweicloudsdkcfw.v1.ScheduleVOPeriodic`]
        :param absolute: 
        :type absolute: :class:`huaweicloudsdkcfw.v1.ScheduleVOAbsolute`
        """
        
        

        self._schedule_id = None
        self._name = None
        self._description = None
        self._ref_count = None
        self._periodic = None
        self._absolute = None
        self.discriminator = None

        if schedule_id is not None:
            self.schedule_id = schedule_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if ref_count is not None:
            self.ref_count = ref_count
        if periodic is not None:
            self.periodic = periodic
        if absolute is not None:
            self.absolute = absolute

    @property
    def schedule_id(self):
        r"""Gets the schedule_id of this ScheduleVO.

        **参数解释**： 时间表ID **取值范围**： 不涉及

        :return: The schedule_id of this ScheduleVO.
        :rtype: str
        """
        return self._schedule_id

    @schedule_id.setter
    def schedule_id(self, schedule_id):
        r"""Sets the schedule_id of this ScheduleVO.

        **参数解释**： 时间表ID **取值范围**： 不涉及

        :param schedule_id: The schedule_id of this ScheduleVO.
        :type schedule_id: str
        """
        self._schedule_id = schedule_id

    @property
    def name(self):
        r"""Gets the name of this ScheduleVO.

        **参数解释**： 时间表名称 **取值范围**： 不涉及

        :return: The name of this ScheduleVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ScheduleVO.

        **参数解释**： 时间表名称 **取值范围**： 不涉及

        :param name: The name of this ScheduleVO.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ScheduleVO.

        **参数解释**： 时间表描述 **取值范围**： 不涉及

        :return: The description of this ScheduleVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ScheduleVO.

        **参数解释**： 时间表描述 **取值范围**： 不涉及

        :param description: The description of this ScheduleVO.
        :type description: str
        """
        self._description = description

    @property
    def ref_count(self):
        r"""Gets the ref_count of this ScheduleVO.

        **参数解释**： 引用次数 **取值范围**： 不涉及

        :return: The ref_count of this ScheduleVO.
        :rtype: int
        """
        return self._ref_count

    @ref_count.setter
    def ref_count(self, ref_count):
        r"""Sets the ref_count of this ScheduleVO.

        **参数解释**： 引用次数 **取值范围**： 不涉及

        :param ref_count: The ref_count of this ScheduleVO.
        :type ref_count: int
        """
        self._ref_count = ref_count

    @property
    def periodic(self):
        r"""Gets the periodic of this ScheduleVO.

        **参数解释**： 周期计划 **取值范围**： 不涉及

        :return: The periodic of this ScheduleVO.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.ScheduleVOPeriodic`]
        """
        return self._periodic

    @periodic.setter
    def periodic(self, periodic):
        r"""Sets the periodic of this ScheduleVO.

        **参数解释**： 周期计划 **取值范围**： 不涉及

        :param periodic: The periodic of this ScheduleVO.
        :type periodic: list[:class:`huaweicloudsdkcfw.v1.ScheduleVOPeriodic`]
        """
        self._periodic = periodic

    @property
    def absolute(self):
        r"""Gets the absolute of this ScheduleVO.

        :return: The absolute of this ScheduleVO.
        :rtype: :class:`huaweicloudsdkcfw.v1.ScheduleVOAbsolute`
        """
        return self._absolute

    @absolute.setter
    def absolute(self, absolute):
        r"""Sets the absolute of this ScheduleVO.

        :param absolute: The absolute of this ScheduleVO.
        :type absolute: :class:`huaweicloudsdkcfw.v1.ScheduleVOAbsolute`
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
        if not isinstance(other, ScheduleVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
