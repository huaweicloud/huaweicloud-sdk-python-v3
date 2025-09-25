# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSecurityCheckConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'int',
        'status': 'bool',
        'check_period_type': 'str',
        'day_period': 'int',
        'week_period': 'list[str]',
        'hour': 'int',
        'content': 'list[str]',
        'host_id_list': 'list[str]'
    }

    attribute_map = {
        'task_id': 'task_id',
        'status': 'status',
        'check_period_type': 'check_period_type',
        'day_period': 'day_period',
        'week_period': 'week_period',
        'hour': 'hour',
        'content': 'content',
        'host_id_list': 'host_id_list'
    }

    def __init__(self, task_id=None, status=None, check_period_type=None, day_period=None, week_period=None, hour=None, content=None, host_id_list=None):
        r"""ShowSecurityCheckConfigResponse

        The model defined in huaweicloud sdk

        :param task_id: 定时任务ID，前台只保存，不显示
        :type task_id: int
        :param status: 体检状态，是否开启
        :type status: bool
        :param check_period_type: 体检周期类型：day-按天，week-按周
        :type check_period_type: str
        :param day_period: 按天的周期
        :type day_period: int
        :param week_period: 按周的周期,选中的日期放入此列表，取值包含：mon,tue,wed,thu,fri,sat,sun
        :type week_period: list[str]
        :param hour: 体检时间：小时
        :type hour: int
        :param content: 体检内容，取值包含：asset,vul,baseline,event
        :type content: list[str]
        :param host_id_list: 已选服务器ID列表
        :type host_id_list: list[str]
        """
        
        super(ShowSecurityCheckConfigResponse, self).__init__()

        self._task_id = None
        self._status = None
        self._check_period_type = None
        self._day_period = None
        self._week_period = None
        self._hour = None
        self._content = None
        self._host_id_list = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if status is not None:
            self.status = status
        if check_period_type is not None:
            self.check_period_type = check_period_type
        if day_period is not None:
            self.day_period = day_period
        if week_period is not None:
            self.week_period = week_period
        if hour is not None:
            self.hour = hour
        if content is not None:
            self.content = content
        if host_id_list is not None:
            self.host_id_list = host_id_list

    @property
    def task_id(self):
        r"""Gets the task_id of this ShowSecurityCheckConfigResponse.

        定时任务ID，前台只保存，不显示

        :return: The task_id of this ShowSecurityCheckConfigResponse.
        :rtype: int
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ShowSecurityCheckConfigResponse.

        定时任务ID，前台只保存，不显示

        :param task_id: The task_id of this ShowSecurityCheckConfigResponse.
        :type task_id: int
        """
        self._task_id = task_id

    @property
    def status(self):
        r"""Gets the status of this ShowSecurityCheckConfigResponse.

        体检状态，是否开启

        :return: The status of this ShowSecurityCheckConfigResponse.
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowSecurityCheckConfigResponse.

        体检状态，是否开启

        :param status: The status of this ShowSecurityCheckConfigResponse.
        :type status: bool
        """
        self._status = status

    @property
    def check_period_type(self):
        r"""Gets the check_period_type of this ShowSecurityCheckConfigResponse.

        体检周期类型：day-按天，week-按周

        :return: The check_period_type of this ShowSecurityCheckConfigResponse.
        :rtype: str
        """
        return self._check_period_type

    @check_period_type.setter
    def check_period_type(self, check_period_type):
        r"""Sets the check_period_type of this ShowSecurityCheckConfigResponse.

        体检周期类型：day-按天，week-按周

        :param check_period_type: The check_period_type of this ShowSecurityCheckConfigResponse.
        :type check_period_type: str
        """
        self._check_period_type = check_period_type

    @property
    def day_period(self):
        r"""Gets the day_period of this ShowSecurityCheckConfigResponse.

        按天的周期

        :return: The day_period of this ShowSecurityCheckConfigResponse.
        :rtype: int
        """
        return self._day_period

    @day_period.setter
    def day_period(self, day_period):
        r"""Sets the day_period of this ShowSecurityCheckConfigResponse.

        按天的周期

        :param day_period: The day_period of this ShowSecurityCheckConfigResponse.
        :type day_period: int
        """
        self._day_period = day_period

    @property
    def week_period(self):
        r"""Gets the week_period of this ShowSecurityCheckConfigResponse.

        按周的周期,选中的日期放入此列表，取值包含：mon,tue,wed,thu,fri,sat,sun

        :return: The week_period of this ShowSecurityCheckConfigResponse.
        :rtype: list[str]
        """
        return self._week_period

    @week_period.setter
    def week_period(self, week_period):
        r"""Sets the week_period of this ShowSecurityCheckConfigResponse.

        按周的周期,选中的日期放入此列表，取值包含：mon,tue,wed,thu,fri,sat,sun

        :param week_period: The week_period of this ShowSecurityCheckConfigResponse.
        :type week_period: list[str]
        """
        self._week_period = week_period

    @property
    def hour(self):
        r"""Gets the hour of this ShowSecurityCheckConfigResponse.

        体检时间：小时

        :return: The hour of this ShowSecurityCheckConfigResponse.
        :rtype: int
        """
        return self._hour

    @hour.setter
    def hour(self, hour):
        r"""Sets the hour of this ShowSecurityCheckConfigResponse.

        体检时间：小时

        :param hour: The hour of this ShowSecurityCheckConfigResponse.
        :type hour: int
        """
        self._hour = hour

    @property
    def content(self):
        r"""Gets the content of this ShowSecurityCheckConfigResponse.

        体检内容，取值包含：asset,vul,baseline,event

        :return: The content of this ShowSecurityCheckConfigResponse.
        :rtype: list[str]
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this ShowSecurityCheckConfigResponse.

        体检内容，取值包含：asset,vul,baseline,event

        :param content: The content of this ShowSecurityCheckConfigResponse.
        :type content: list[str]
        """
        self._content = content

    @property
    def host_id_list(self):
        r"""Gets the host_id_list of this ShowSecurityCheckConfigResponse.

        已选服务器ID列表

        :return: The host_id_list of this ShowSecurityCheckConfigResponse.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        r"""Sets the host_id_list of this ShowSecurityCheckConfigResponse.

        已选服务器ID列表

        :param host_id_list: The host_id_list of this ShowSecurityCheckConfigResponse.
        :type host_id_list: list[str]
        """
        self._host_id_list = host_id_list

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
        if not isinstance(other, ShowSecurityCheckConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
