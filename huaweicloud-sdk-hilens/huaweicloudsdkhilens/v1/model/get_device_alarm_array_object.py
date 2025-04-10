# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetDeviceAlarmArrayObject:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'alarm_id': 'int',
        'level': 'str',
        'platform': 'str',
        'impact': 'str',
        'detail': 'str',
        'reason': 'str',
        'deal_suggestion': 'str',
        'create_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'alarm_id': 'alarm_id',
        'level': 'level',
        'platform': 'platform',
        'impact': 'impact',
        'detail': 'detail',
        'reason': 'reason',
        'deal_suggestion': 'deal_suggestion',
        'create_time': 'create_time'
    }

    def __init__(self, id=None, name=None, alarm_id=None, level=None, platform=None, impact=None, detail=None, reason=None, deal_suggestion=None, create_time=None):
        r"""GetDeviceAlarmArrayObject

        The model defined in huaweicloud sdk

        :param id: 设备告警记录ID
        :type id: str
        :param name: 设备告警名称
        :type name: str
        :param alarm_id: 设备告警ID
        :type alarm_id: int
        :param level: 设备告警等级，紧急告警(critical)，严重告警(major)，一般告警(minor)
        :type level: str
        :param platform: 设备平台
        :type platform: str
        :param impact: 设备告警的影响
        :type impact: str
        :param detail: 设备告警详情内容
        :type detail: str
        :param reason: 设备告警原因
        :type reason: str
        :param deal_suggestion: 设备告警处理建议
        :type deal_suggestion: str
        :param create_time: 创建时间（时间戳）
        :type create_time: int
        """
        
        

        self._id = None
        self._name = None
        self._alarm_id = None
        self._level = None
        self._platform = None
        self._impact = None
        self._detail = None
        self._reason = None
        self._deal_suggestion = None
        self._create_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if alarm_id is not None:
            self.alarm_id = alarm_id
        if level is not None:
            self.level = level
        if platform is not None:
            self.platform = platform
        if impact is not None:
            self.impact = impact
        if detail is not None:
            self.detail = detail
        if reason is not None:
            self.reason = reason
        if deal_suggestion is not None:
            self.deal_suggestion = deal_suggestion
        if create_time is not None:
            self.create_time = create_time

    @property
    def id(self):
        r"""Gets the id of this GetDeviceAlarmArrayObject.

        设备告警记录ID

        :return: The id of this GetDeviceAlarmArrayObject.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GetDeviceAlarmArrayObject.

        设备告警记录ID

        :param id: The id of this GetDeviceAlarmArrayObject.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this GetDeviceAlarmArrayObject.

        设备告警名称

        :return: The name of this GetDeviceAlarmArrayObject.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GetDeviceAlarmArrayObject.

        设备告警名称

        :param name: The name of this GetDeviceAlarmArrayObject.
        :type name: str
        """
        self._name = name

    @property
    def alarm_id(self):
        r"""Gets the alarm_id of this GetDeviceAlarmArrayObject.

        设备告警ID

        :return: The alarm_id of this GetDeviceAlarmArrayObject.
        :rtype: int
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        r"""Sets the alarm_id of this GetDeviceAlarmArrayObject.

        设备告警ID

        :param alarm_id: The alarm_id of this GetDeviceAlarmArrayObject.
        :type alarm_id: int
        """
        self._alarm_id = alarm_id

    @property
    def level(self):
        r"""Gets the level of this GetDeviceAlarmArrayObject.

        设备告警等级，紧急告警(critical)，严重告警(major)，一般告警(minor)

        :return: The level of this GetDeviceAlarmArrayObject.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this GetDeviceAlarmArrayObject.

        设备告警等级，紧急告警(critical)，严重告警(major)，一般告警(minor)

        :param level: The level of this GetDeviceAlarmArrayObject.
        :type level: str
        """
        self._level = level

    @property
    def platform(self):
        r"""Gets the platform of this GetDeviceAlarmArrayObject.

        设备平台

        :return: The platform of this GetDeviceAlarmArrayObject.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        r"""Sets the platform of this GetDeviceAlarmArrayObject.

        设备平台

        :param platform: The platform of this GetDeviceAlarmArrayObject.
        :type platform: str
        """
        self._platform = platform

    @property
    def impact(self):
        r"""Gets the impact of this GetDeviceAlarmArrayObject.

        设备告警的影响

        :return: The impact of this GetDeviceAlarmArrayObject.
        :rtype: str
        """
        return self._impact

    @impact.setter
    def impact(self, impact):
        r"""Sets the impact of this GetDeviceAlarmArrayObject.

        设备告警的影响

        :param impact: The impact of this GetDeviceAlarmArrayObject.
        :type impact: str
        """
        self._impact = impact

    @property
    def detail(self):
        r"""Gets the detail of this GetDeviceAlarmArrayObject.

        设备告警详情内容

        :return: The detail of this GetDeviceAlarmArrayObject.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        r"""Sets the detail of this GetDeviceAlarmArrayObject.

        设备告警详情内容

        :param detail: The detail of this GetDeviceAlarmArrayObject.
        :type detail: str
        """
        self._detail = detail

    @property
    def reason(self):
        r"""Gets the reason of this GetDeviceAlarmArrayObject.

        设备告警原因

        :return: The reason of this GetDeviceAlarmArrayObject.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this GetDeviceAlarmArrayObject.

        设备告警原因

        :param reason: The reason of this GetDeviceAlarmArrayObject.
        :type reason: str
        """
        self._reason = reason

    @property
    def deal_suggestion(self):
        r"""Gets the deal_suggestion of this GetDeviceAlarmArrayObject.

        设备告警处理建议

        :return: The deal_suggestion of this GetDeviceAlarmArrayObject.
        :rtype: str
        """
        return self._deal_suggestion

    @deal_suggestion.setter
    def deal_suggestion(self, deal_suggestion):
        r"""Sets the deal_suggestion of this GetDeviceAlarmArrayObject.

        设备告警处理建议

        :param deal_suggestion: The deal_suggestion of this GetDeviceAlarmArrayObject.
        :type deal_suggestion: str
        """
        self._deal_suggestion = deal_suggestion

    @property
    def create_time(self):
        r"""Gets the create_time of this GetDeviceAlarmArrayObject.

        创建时间（时间戳）

        :return: The create_time of this GetDeviceAlarmArrayObject.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this GetDeviceAlarmArrayObject.

        创建时间（时间戳）

        :param create_time: The create_time of this GetDeviceAlarmArrayObject.
        :type create_time: int
        """
        self._create_time = create_time

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
        if not isinstance(other, GetDeviceAlarmArrayObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
