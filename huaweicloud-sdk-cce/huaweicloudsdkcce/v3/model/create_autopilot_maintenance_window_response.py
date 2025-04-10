# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAutopilotMaintenanceWindowResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'weekly_period': 'str',
        'start_time': 'str',
        'duration_hours': 'int',
        'upgrade_scope': 'str'
    }

    attribute_map = {
        'weekly_period': 'weekly_period',
        'start_time': 'start_time',
        'duration_hours': 'duration_hours',
        'upgrade_scope': 'upgrade_scope'
    }

    def __init__(self, weekly_period=None, start_time=None, duration_hours=None, upgrade_scope=None):
        r"""CreateAutopilotMaintenanceWindowResponse

        The model defined in huaweicloud sdk

        :param weekly_period: 升级周期，从\&quot;Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday\&quot;中进行选择，以英文逗号分隔 如：\&quot;Friday,Saturday\&quot; 
        :type weekly_period: str
        :param start_time: 升级起始时间（UTC时间）
        :type start_time: str
        :param duration_hours: 升级时长
        :type duration_hours: int
        :param upgrade_scope: 升级版本范围，当前只支持小版本自动升级
        :type upgrade_scope: str
        """
        
        super(CreateAutopilotMaintenanceWindowResponse, self).__init__()

        self._weekly_period = None
        self._start_time = None
        self._duration_hours = None
        self._upgrade_scope = None
        self.discriminator = None

        if weekly_period is not None:
            self.weekly_period = weekly_period
        if start_time is not None:
            self.start_time = start_time
        if duration_hours is not None:
            self.duration_hours = duration_hours
        if upgrade_scope is not None:
            self.upgrade_scope = upgrade_scope

    @property
    def weekly_period(self):
        r"""Gets the weekly_period of this CreateAutopilotMaintenanceWindowResponse.

        升级周期，从\"Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday\"中进行选择，以英文逗号分隔 如：\"Friday,Saturday\" 

        :return: The weekly_period of this CreateAutopilotMaintenanceWindowResponse.
        :rtype: str
        """
        return self._weekly_period

    @weekly_period.setter
    def weekly_period(self, weekly_period):
        r"""Sets the weekly_period of this CreateAutopilotMaintenanceWindowResponse.

        升级周期，从\"Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday\"中进行选择，以英文逗号分隔 如：\"Friday,Saturday\" 

        :param weekly_period: The weekly_period of this CreateAutopilotMaintenanceWindowResponse.
        :type weekly_period: str
        """
        self._weekly_period = weekly_period

    @property
    def start_time(self):
        r"""Gets the start_time of this CreateAutopilotMaintenanceWindowResponse.

        升级起始时间（UTC时间）

        :return: The start_time of this CreateAutopilotMaintenanceWindowResponse.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this CreateAutopilotMaintenanceWindowResponse.

        升级起始时间（UTC时间）

        :param start_time: The start_time of this CreateAutopilotMaintenanceWindowResponse.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def duration_hours(self):
        r"""Gets the duration_hours of this CreateAutopilotMaintenanceWindowResponse.

        升级时长

        :return: The duration_hours of this CreateAutopilotMaintenanceWindowResponse.
        :rtype: int
        """
        return self._duration_hours

    @duration_hours.setter
    def duration_hours(self, duration_hours):
        r"""Sets the duration_hours of this CreateAutopilotMaintenanceWindowResponse.

        升级时长

        :param duration_hours: The duration_hours of this CreateAutopilotMaintenanceWindowResponse.
        :type duration_hours: int
        """
        self._duration_hours = duration_hours

    @property
    def upgrade_scope(self):
        r"""Gets the upgrade_scope of this CreateAutopilotMaintenanceWindowResponse.

        升级版本范围，当前只支持小版本自动升级

        :return: The upgrade_scope of this CreateAutopilotMaintenanceWindowResponse.
        :rtype: str
        """
        return self._upgrade_scope

    @upgrade_scope.setter
    def upgrade_scope(self, upgrade_scope):
        r"""Sets the upgrade_scope of this CreateAutopilotMaintenanceWindowResponse.

        升级版本范围，当前只支持小版本自动升级

        :param upgrade_scope: The upgrade_scope of this CreateAutopilotMaintenanceWindowResponse.
        :type upgrade_scope: str
        """
        self._upgrade_scope = upgrade_scope

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
        if not isinstance(other, CreateAutopilotMaintenanceWindowResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
