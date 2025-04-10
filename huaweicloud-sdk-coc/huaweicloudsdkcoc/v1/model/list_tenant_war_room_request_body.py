# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTenantWarRoomRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'current_users': 'list[str]',
        'war_room_nums': 'list[str]',
        'incident_num': 'str',
        'title': 'str',
        'region_code_list': 'list[str]',
        'incident_levels': 'list[str]',
        'impacted_application_ids': 'list[str]',
        'admin': 'list[str]',
        'status': 'list[str]',
        'triggered_start_time': 'int',
        'triggered_end_time': 'int',
        'occur_start_time': 'int',
        'occur_end_time': 'int',
        'recover_start_time': 'int',
        'recover_end_time': 'int',
        'notification_level': 'list[str]',
        'enterprise_project_ids': 'list[str]',
        'war_room_num': 'str',
        'statistic_flag': 'bool'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'current_users': 'current_users',
        'war_room_nums': 'war_room_nums',
        'incident_num': 'incident_num',
        'title': 'title',
        'region_code_list': 'region_code_list',
        'incident_levels': 'incident_levels',
        'impacted_application_ids': 'impacted_application_ids',
        'admin': 'admin',
        'status': 'status',
        'triggered_start_time': 'triggered_start_time',
        'triggered_end_time': 'triggered_end_time',
        'occur_start_time': 'occur_start_time',
        'occur_end_time': 'occur_end_time',
        'recover_start_time': 'recover_start_time',
        'recover_end_time': 'recover_end_time',
        'notification_level': 'notification_level',
        'enterprise_project_ids': 'enterprise_project_ids',
        'war_room_num': 'war_room_num',
        'statistic_flag': 'statistic_flag'
    }

    def __init__(self, limit=None, offset=None, current_users=None, war_room_nums=None, incident_num=None, title=None, region_code_list=None, incident_levels=None, impacted_application_ids=None, admin=None, status=None, triggered_start_time=None, triggered_end_time=None, occur_start_time=None, occur_end_time=None, recover_start_time=None, recover_end_time=None, notification_level=None, enterprise_project_ids=None, war_room_num=None, statistic_flag=None):
        r"""ListTenantWarRoomRequestBody

        The model defined in huaweicloud sdk

        :param limit: limit
        :type limit: int
        :param offset: 查询数量 最小值0 最大值1000
        :type offset: int
        :param current_users: 用户id
        :type current_users: list[str]
        :param war_room_nums: WarRoom单号，当有这个筛选条件时，其他筛选条件忽略
        :type war_room_nums: list[str]
        :param incident_num: 事件单号 精确查询
        :type incident_num: str
        :param title: WarRoom名称 模糊查询
        :type title: str
        :param region_code_list: 区域 多选
        :type region_code_list: list[str]
        :param incident_levels: 事件级别 多选
        :type incident_levels: list[str]
        :param impacted_application_ids: 影响应用id
        :type impacted_application_ids: list[str]
        :param admin: WarRoom管理员
        :type admin: list[str]
        :param status: WarRoom状态
        :type status: list[str]
        :param triggered_start_time: 拉起开始时间 默认前30天
        :type triggered_start_time: int
        :param triggered_end_time: 拉起结束时间 默认当前时间
        :type triggered_end_time: int
        :param occur_start_time: 发生开始时间
        :type occur_start_time: int
        :param occur_end_time: 发生结束时间
        :type occur_end_time: int
        :param recover_start_time: 恢复开始时间
        :type recover_start_time: int
        :param recover_end_time: 恢复结束时间
        :type recover_end_time: int
        :param notification_level: 通报级别
        :type notification_level: list[str]
        :param enterprise_project_ids: 企业项目id
        :type enterprise_project_ids: list[str]
        :param war_room_num: WarRoom 单号 前端使用
        :type war_room_num: str
        :param statistic_flag: 是否统计,false 返回基本信息;true接口只返回统计结果：total_num,running_num,closed_num
        :type statistic_flag: bool
        """
        
        

        self._limit = None
        self._offset = None
        self._current_users = None
        self._war_room_nums = None
        self._incident_num = None
        self._title = None
        self._region_code_list = None
        self._incident_levels = None
        self._impacted_application_ids = None
        self._admin = None
        self._status = None
        self._triggered_start_time = None
        self._triggered_end_time = None
        self._occur_start_time = None
        self._occur_end_time = None
        self._recover_start_time = None
        self._recover_end_time = None
        self._notification_level = None
        self._enterprise_project_ids = None
        self._war_room_num = None
        self._statistic_flag = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if current_users is not None:
            self.current_users = current_users
        if war_room_nums is not None:
            self.war_room_nums = war_room_nums
        if incident_num is not None:
            self.incident_num = incident_num
        if title is not None:
            self.title = title
        if region_code_list is not None:
            self.region_code_list = region_code_list
        if incident_levels is not None:
            self.incident_levels = incident_levels
        if impacted_application_ids is not None:
            self.impacted_application_ids = impacted_application_ids
        if admin is not None:
            self.admin = admin
        if status is not None:
            self.status = status
        if triggered_start_time is not None:
            self.triggered_start_time = triggered_start_time
        if triggered_end_time is not None:
            self.triggered_end_time = triggered_end_time
        if occur_start_time is not None:
            self.occur_start_time = occur_start_time
        if occur_end_time is not None:
            self.occur_end_time = occur_end_time
        if recover_start_time is not None:
            self.recover_start_time = recover_start_time
        if recover_end_time is not None:
            self.recover_end_time = recover_end_time
        if notification_level is not None:
            self.notification_level = notification_level
        if enterprise_project_ids is not None:
            self.enterprise_project_ids = enterprise_project_ids
        if war_room_num is not None:
            self.war_room_num = war_room_num
        if statistic_flag is not None:
            self.statistic_flag = statistic_flag

    @property
    def limit(self):
        r"""Gets the limit of this ListTenantWarRoomRequestBody.

        limit

        :return: The limit of this ListTenantWarRoomRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTenantWarRoomRequestBody.

        limit

        :param limit: The limit of this ListTenantWarRoomRequestBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListTenantWarRoomRequestBody.

        查询数量 最小值0 最大值1000

        :return: The offset of this ListTenantWarRoomRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListTenantWarRoomRequestBody.

        查询数量 最小值0 最大值1000

        :param offset: The offset of this ListTenantWarRoomRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def current_users(self):
        r"""Gets the current_users of this ListTenantWarRoomRequestBody.

        用户id

        :return: The current_users of this ListTenantWarRoomRequestBody.
        :rtype: list[str]
        """
        return self._current_users

    @current_users.setter
    def current_users(self, current_users):
        r"""Sets the current_users of this ListTenantWarRoomRequestBody.

        用户id

        :param current_users: The current_users of this ListTenantWarRoomRequestBody.
        :type current_users: list[str]
        """
        self._current_users = current_users

    @property
    def war_room_nums(self):
        r"""Gets the war_room_nums of this ListTenantWarRoomRequestBody.

        WarRoom单号，当有这个筛选条件时，其他筛选条件忽略

        :return: The war_room_nums of this ListTenantWarRoomRequestBody.
        :rtype: list[str]
        """
        return self._war_room_nums

    @war_room_nums.setter
    def war_room_nums(self, war_room_nums):
        r"""Sets the war_room_nums of this ListTenantWarRoomRequestBody.

        WarRoom单号，当有这个筛选条件时，其他筛选条件忽略

        :param war_room_nums: The war_room_nums of this ListTenantWarRoomRequestBody.
        :type war_room_nums: list[str]
        """
        self._war_room_nums = war_room_nums

    @property
    def incident_num(self):
        r"""Gets the incident_num of this ListTenantWarRoomRequestBody.

        事件单号 精确查询

        :return: The incident_num of this ListTenantWarRoomRequestBody.
        :rtype: str
        """
        return self._incident_num

    @incident_num.setter
    def incident_num(self, incident_num):
        r"""Sets the incident_num of this ListTenantWarRoomRequestBody.

        事件单号 精确查询

        :param incident_num: The incident_num of this ListTenantWarRoomRequestBody.
        :type incident_num: str
        """
        self._incident_num = incident_num

    @property
    def title(self):
        r"""Gets the title of this ListTenantWarRoomRequestBody.

        WarRoom名称 模糊查询

        :return: The title of this ListTenantWarRoomRequestBody.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this ListTenantWarRoomRequestBody.

        WarRoom名称 模糊查询

        :param title: The title of this ListTenantWarRoomRequestBody.
        :type title: str
        """
        self._title = title

    @property
    def region_code_list(self):
        r"""Gets the region_code_list of this ListTenantWarRoomRequestBody.

        区域 多选

        :return: The region_code_list of this ListTenantWarRoomRequestBody.
        :rtype: list[str]
        """
        return self._region_code_list

    @region_code_list.setter
    def region_code_list(self, region_code_list):
        r"""Sets the region_code_list of this ListTenantWarRoomRequestBody.

        区域 多选

        :param region_code_list: The region_code_list of this ListTenantWarRoomRequestBody.
        :type region_code_list: list[str]
        """
        self._region_code_list = region_code_list

    @property
    def incident_levels(self):
        r"""Gets the incident_levels of this ListTenantWarRoomRequestBody.

        事件级别 多选

        :return: The incident_levels of this ListTenantWarRoomRequestBody.
        :rtype: list[str]
        """
        return self._incident_levels

    @incident_levels.setter
    def incident_levels(self, incident_levels):
        r"""Sets the incident_levels of this ListTenantWarRoomRequestBody.

        事件级别 多选

        :param incident_levels: The incident_levels of this ListTenantWarRoomRequestBody.
        :type incident_levels: list[str]
        """
        self._incident_levels = incident_levels

    @property
    def impacted_application_ids(self):
        r"""Gets the impacted_application_ids of this ListTenantWarRoomRequestBody.

        影响应用id

        :return: The impacted_application_ids of this ListTenantWarRoomRequestBody.
        :rtype: list[str]
        """
        return self._impacted_application_ids

    @impacted_application_ids.setter
    def impacted_application_ids(self, impacted_application_ids):
        r"""Sets the impacted_application_ids of this ListTenantWarRoomRequestBody.

        影响应用id

        :param impacted_application_ids: The impacted_application_ids of this ListTenantWarRoomRequestBody.
        :type impacted_application_ids: list[str]
        """
        self._impacted_application_ids = impacted_application_ids

    @property
    def admin(self):
        r"""Gets the admin of this ListTenantWarRoomRequestBody.

        WarRoom管理员

        :return: The admin of this ListTenantWarRoomRequestBody.
        :rtype: list[str]
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        r"""Sets the admin of this ListTenantWarRoomRequestBody.

        WarRoom管理员

        :param admin: The admin of this ListTenantWarRoomRequestBody.
        :type admin: list[str]
        """
        self._admin = admin

    @property
    def status(self):
        r"""Gets the status of this ListTenantWarRoomRequestBody.

        WarRoom状态

        :return: The status of this ListTenantWarRoomRequestBody.
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListTenantWarRoomRequestBody.

        WarRoom状态

        :param status: The status of this ListTenantWarRoomRequestBody.
        :type status: list[str]
        """
        self._status = status

    @property
    def triggered_start_time(self):
        r"""Gets the triggered_start_time of this ListTenantWarRoomRequestBody.

        拉起开始时间 默认前30天

        :return: The triggered_start_time of this ListTenantWarRoomRequestBody.
        :rtype: int
        """
        return self._triggered_start_time

    @triggered_start_time.setter
    def triggered_start_time(self, triggered_start_time):
        r"""Sets the triggered_start_time of this ListTenantWarRoomRequestBody.

        拉起开始时间 默认前30天

        :param triggered_start_time: The triggered_start_time of this ListTenantWarRoomRequestBody.
        :type triggered_start_time: int
        """
        self._triggered_start_time = triggered_start_time

    @property
    def triggered_end_time(self):
        r"""Gets the triggered_end_time of this ListTenantWarRoomRequestBody.

        拉起结束时间 默认当前时间

        :return: The triggered_end_time of this ListTenantWarRoomRequestBody.
        :rtype: int
        """
        return self._triggered_end_time

    @triggered_end_time.setter
    def triggered_end_time(self, triggered_end_time):
        r"""Sets the triggered_end_time of this ListTenantWarRoomRequestBody.

        拉起结束时间 默认当前时间

        :param triggered_end_time: The triggered_end_time of this ListTenantWarRoomRequestBody.
        :type triggered_end_time: int
        """
        self._triggered_end_time = triggered_end_time

    @property
    def occur_start_time(self):
        r"""Gets the occur_start_time of this ListTenantWarRoomRequestBody.

        发生开始时间

        :return: The occur_start_time of this ListTenantWarRoomRequestBody.
        :rtype: int
        """
        return self._occur_start_time

    @occur_start_time.setter
    def occur_start_time(self, occur_start_time):
        r"""Sets the occur_start_time of this ListTenantWarRoomRequestBody.

        发生开始时间

        :param occur_start_time: The occur_start_time of this ListTenantWarRoomRequestBody.
        :type occur_start_time: int
        """
        self._occur_start_time = occur_start_time

    @property
    def occur_end_time(self):
        r"""Gets the occur_end_time of this ListTenantWarRoomRequestBody.

        发生结束时间

        :return: The occur_end_time of this ListTenantWarRoomRequestBody.
        :rtype: int
        """
        return self._occur_end_time

    @occur_end_time.setter
    def occur_end_time(self, occur_end_time):
        r"""Sets the occur_end_time of this ListTenantWarRoomRequestBody.

        发生结束时间

        :param occur_end_time: The occur_end_time of this ListTenantWarRoomRequestBody.
        :type occur_end_time: int
        """
        self._occur_end_time = occur_end_time

    @property
    def recover_start_time(self):
        r"""Gets the recover_start_time of this ListTenantWarRoomRequestBody.

        恢复开始时间

        :return: The recover_start_time of this ListTenantWarRoomRequestBody.
        :rtype: int
        """
        return self._recover_start_time

    @recover_start_time.setter
    def recover_start_time(self, recover_start_time):
        r"""Sets the recover_start_time of this ListTenantWarRoomRequestBody.

        恢复开始时间

        :param recover_start_time: The recover_start_time of this ListTenantWarRoomRequestBody.
        :type recover_start_time: int
        """
        self._recover_start_time = recover_start_time

    @property
    def recover_end_time(self):
        r"""Gets the recover_end_time of this ListTenantWarRoomRequestBody.

        恢复结束时间

        :return: The recover_end_time of this ListTenantWarRoomRequestBody.
        :rtype: int
        """
        return self._recover_end_time

    @recover_end_time.setter
    def recover_end_time(self, recover_end_time):
        r"""Sets the recover_end_time of this ListTenantWarRoomRequestBody.

        恢复结束时间

        :param recover_end_time: The recover_end_time of this ListTenantWarRoomRequestBody.
        :type recover_end_time: int
        """
        self._recover_end_time = recover_end_time

    @property
    def notification_level(self):
        r"""Gets the notification_level of this ListTenantWarRoomRequestBody.

        通报级别

        :return: The notification_level of this ListTenantWarRoomRequestBody.
        :rtype: list[str]
        """
        return self._notification_level

    @notification_level.setter
    def notification_level(self, notification_level):
        r"""Sets the notification_level of this ListTenantWarRoomRequestBody.

        通报级别

        :param notification_level: The notification_level of this ListTenantWarRoomRequestBody.
        :type notification_level: list[str]
        """
        self._notification_level = notification_level

    @property
    def enterprise_project_ids(self):
        r"""Gets the enterprise_project_ids of this ListTenantWarRoomRequestBody.

        企业项目id

        :return: The enterprise_project_ids of this ListTenantWarRoomRequestBody.
        :rtype: list[str]
        """
        return self._enterprise_project_ids

    @enterprise_project_ids.setter
    def enterprise_project_ids(self, enterprise_project_ids):
        r"""Sets the enterprise_project_ids of this ListTenantWarRoomRequestBody.

        企业项目id

        :param enterprise_project_ids: The enterprise_project_ids of this ListTenantWarRoomRequestBody.
        :type enterprise_project_ids: list[str]
        """
        self._enterprise_project_ids = enterprise_project_ids

    @property
    def war_room_num(self):
        r"""Gets the war_room_num of this ListTenantWarRoomRequestBody.

        WarRoom 单号 前端使用

        :return: The war_room_num of this ListTenantWarRoomRequestBody.
        :rtype: str
        """
        return self._war_room_num

    @war_room_num.setter
    def war_room_num(self, war_room_num):
        r"""Sets the war_room_num of this ListTenantWarRoomRequestBody.

        WarRoom 单号 前端使用

        :param war_room_num: The war_room_num of this ListTenantWarRoomRequestBody.
        :type war_room_num: str
        """
        self._war_room_num = war_room_num

    @property
    def statistic_flag(self):
        r"""Gets the statistic_flag of this ListTenantWarRoomRequestBody.

        是否统计,false 返回基本信息;true接口只返回统计结果：total_num,running_num,closed_num

        :return: The statistic_flag of this ListTenantWarRoomRequestBody.
        :rtype: bool
        """
        return self._statistic_flag

    @statistic_flag.setter
    def statistic_flag(self, statistic_flag):
        r"""Sets the statistic_flag of this ListTenantWarRoomRequestBody.

        是否统计,false 返回基本信息;true接口只返回统计结果：total_num,running_num,closed_num

        :param statistic_flag: The statistic_flag of this ListTenantWarRoomRequestBody.
        :type statistic_flag: bool
        """
        self._statistic_flag = statistic_flag

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
        if not isinstance(other, ListTenantWarRoomRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
