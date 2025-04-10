# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PipelineSchedule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uuid': 'str',
        'type': 'str',
        'name': 'str',
        'enable': 'str',
        'days_of_week': 'list[int]',
        'time_zone': 'str'
    }

    attribute_map = {
        'uuid': 'uuid',
        'type': 'type',
        'name': 'name',
        'enable': 'enable',
        'days_of_week': 'days_of_week',
        'time_zone': 'time_zone'
    }

    def __init__(self, uuid=None, type=None, name=None, enable=None, days_of_week=None, time_zone=None):
        r"""PipelineSchedule

        The model defined in huaweicloud sdk

        :param uuid: 任务ID
        :type uuid: str
        :param type: 任务类型
        :type type: str
        :param name: 任务名称
        :type name: str
        :param enable: 是否可用
        :type enable: str
        :param days_of_week: 一周内具体时间
        :type days_of_week: list[int]
        :param time_zone: 时区
        :type time_zone: str
        """
        
        

        self._uuid = None
        self._type = None
        self._name = None
        self._enable = None
        self._days_of_week = None
        self._time_zone = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if enable is not None:
            self.enable = enable
        if days_of_week is not None:
            self.days_of_week = days_of_week
        if time_zone is not None:
            self.time_zone = time_zone

    @property
    def uuid(self):
        r"""Gets the uuid of this PipelineSchedule.

        任务ID

        :return: The uuid of this PipelineSchedule.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        r"""Sets the uuid of this PipelineSchedule.

        任务ID

        :param uuid: The uuid of this PipelineSchedule.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def type(self):
        r"""Gets the type of this PipelineSchedule.

        任务类型

        :return: The type of this PipelineSchedule.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this PipelineSchedule.

        任务类型

        :param type: The type of this PipelineSchedule.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        r"""Gets the name of this PipelineSchedule.

        任务名称

        :return: The name of this PipelineSchedule.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PipelineSchedule.

        任务名称

        :param name: The name of this PipelineSchedule.
        :type name: str
        """
        self._name = name

    @property
    def enable(self):
        r"""Gets the enable of this PipelineSchedule.

        是否可用

        :return: The enable of this PipelineSchedule.
        :rtype: str
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this PipelineSchedule.

        是否可用

        :param enable: The enable of this PipelineSchedule.
        :type enable: str
        """
        self._enable = enable

    @property
    def days_of_week(self):
        r"""Gets the days_of_week of this PipelineSchedule.

        一周内具体时间

        :return: The days_of_week of this PipelineSchedule.
        :rtype: list[int]
        """
        return self._days_of_week

    @days_of_week.setter
    def days_of_week(self, days_of_week):
        r"""Sets the days_of_week of this PipelineSchedule.

        一周内具体时间

        :param days_of_week: The days_of_week of this PipelineSchedule.
        :type days_of_week: list[int]
        """
        self._days_of_week = days_of_week

    @property
    def time_zone(self):
        r"""Gets the time_zone of this PipelineSchedule.

        时区

        :return: The time_zone of this PipelineSchedule.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this PipelineSchedule.

        时区

        :param time_zone: The time_zone of this PipelineSchedule.
        :type time_zone: str
        """
        self._time_zone = time_zone

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
        if not isinstance(other, PipelineSchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
