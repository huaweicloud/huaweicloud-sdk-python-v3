# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobBaseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'job_type': 'str',
        'multi_write': 'bool',
        'engine_type': 'str',
        'job_direction': 'str',
        'task_type': 'str',
        'net_type': 'str',
        'charging_mode': 'str',
        'enterprise_project_id': 'str',
        'description': 'str',
        'start_time': 'str',
        'expired_days': 'str',
        'tags': 'list[ResourceTag]'
    }

    attribute_map = {
        'name': 'name',
        'job_type': 'job_type',
        'multi_write': 'multi_write',
        'engine_type': 'engine_type',
        'job_direction': 'job_direction',
        'task_type': 'task_type',
        'net_type': 'net_type',
        'charging_mode': 'charging_mode',
        'enterprise_project_id': 'enterprise_project_id',
        'description': 'description',
        'start_time': 'start_time',
        'expired_days': 'expired_days',
        'tags': 'tags'
    }

    def __init__(self, name=None, job_type=None, multi_write=None, engine_type=None, job_direction=None, task_type=None, net_type=None, charging_mode=None, enterprise_project_id=None, description=None, start_time=None, expired_days=None, tags=None):
        """JobBaseInfo

        The model defined in huaweicloud sdk

        :param name: 任务名称。 约束：任务名称在4位到50位之间，不区分大小写，可以包含字母、数字、中划线或下划线，不能包括其他特殊字符。 - 最小长度：4 - 最大长度：50
        :type name: str
        :param job_type: 任务场景。取值： - migration：实时迁移。 - sync：实时同步。 - cloudDataGuard：实时灾备。
        :type job_type: str
        :param multi_write: 灾备类型是否双主灾备。说明： - job_type 是cloudDataGuard时，必填，灾备类型是双主灾备时，multi_write取值true, 否则为false。 - job_type 是其他类型时，multi_write是非必选参数。
        :type multi_write: bool
        :param engine_type: 引擎类型。取值： - oracle-to-gaussdbv5：Oracle同步到GaussDB分布式版，实时同步场景使用。
        :type engine_type: str
        :param job_direction: 迁移方向。取值： - up：入云 ，灾备场景时对应本云为备。 - down：出云，灾备场景时对应本云为主。 - non-dbs：自建。
        :type job_direction: str
        :param task_type: 迁移模式。取值： - FULL_TRANS ：全量。 - FULL_INCR_TRANS：全量+增量。 - INCR_TRANS：增量。
        :type task_type: str
        :param net_type: 网络类型。取值： - eip：公网网络。 - vpc：VPC网络，灾备场景不支持选择VPC网络。 - vpn：VPN、专线网络。
        :type net_type: str
        :param charging_mode: 计费模式，默认按需。取值： - period：包周期。 - on_demand：按需。
        :type charging_mode: str
        :param enterprise_project_id: 企业项目ID。 缺省值：\&quot;0\&quot;，表示\&quot;default\&quot;企业项目。
        :type enterprise_project_id: str
        :param description: 任务描述。 约束：任务描述不能超过256位，且不能包含!&lt;&gt;&amp;&#39;\&quot;\\特殊字符。
        :type description: str
        :param start_time: 任务定时启动时间。
        :type start_time: str
        :param expired_days: 任务处于异常状态一段时间后，将会自动结束。单位为天。(范围14-100)，不传默认为14天。
        :type expired_days: str
        :param tags: 标签信息，最多添加10个标签。
        :type tags: list[:class:`huaweicloudsdkdrs.v5.ResourceTag`]
        """
        
        

        self._name = None
        self._job_type = None
        self._multi_write = None
        self._engine_type = None
        self._job_direction = None
        self._task_type = None
        self._net_type = None
        self._charging_mode = None
        self._enterprise_project_id = None
        self._description = None
        self._start_time = None
        self._expired_days = None
        self._tags = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if job_type is not None:
            self.job_type = job_type
        if multi_write is not None:
            self.multi_write = multi_write
        if engine_type is not None:
            self.engine_type = engine_type
        if job_direction is not None:
            self.job_direction = job_direction
        if task_type is not None:
            self.task_type = task_type
        if net_type is not None:
            self.net_type = net_type
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if description is not None:
            self.description = description
        if start_time is not None:
            self.start_time = start_time
        if expired_days is not None:
            self.expired_days = expired_days
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        """Gets the name of this JobBaseInfo.

        任务名称。 约束：任务名称在4位到50位之间，不区分大小写，可以包含字母、数字、中划线或下划线，不能包括其他特殊字符。 - 最小长度：4 - 最大长度：50

        :return: The name of this JobBaseInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobBaseInfo.

        任务名称。 约束：任务名称在4位到50位之间，不区分大小写，可以包含字母、数字、中划线或下划线，不能包括其他特殊字符。 - 最小长度：4 - 最大长度：50

        :param name: The name of this JobBaseInfo.
        :type name: str
        """
        self._name = name

    @property
    def job_type(self):
        """Gets the job_type of this JobBaseInfo.

        任务场景。取值： - migration：实时迁移。 - sync：实时同步。 - cloudDataGuard：实时灾备。

        :return: The job_type of this JobBaseInfo.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this JobBaseInfo.

        任务场景。取值： - migration：实时迁移。 - sync：实时同步。 - cloudDataGuard：实时灾备。

        :param job_type: The job_type of this JobBaseInfo.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def multi_write(self):
        """Gets the multi_write of this JobBaseInfo.

        灾备类型是否双主灾备。说明： - job_type 是cloudDataGuard时，必填，灾备类型是双主灾备时，multi_write取值true, 否则为false。 - job_type 是其他类型时，multi_write是非必选参数。

        :return: The multi_write of this JobBaseInfo.
        :rtype: bool
        """
        return self._multi_write

    @multi_write.setter
    def multi_write(self, multi_write):
        """Sets the multi_write of this JobBaseInfo.

        灾备类型是否双主灾备。说明： - job_type 是cloudDataGuard时，必填，灾备类型是双主灾备时，multi_write取值true, 否则为false。 - job_type 是其他类型时，multi_write是非必选参数。

        :param multi_write: The multi_write of this JobBaseInfo.
        :type multi_write: bool
        """
        self._multi_write = multi_write

    @property
    def engine_type(self):
        """Gets the engine_type of this JobBaseInfo.

        引擎类型。取值： - oracle-to-gaussdbv5：Oracle同步到GaussDB分布式版，实时同步场景使用。

        :return: The engine_type of this JobBaseInfo.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        """Sets the engine_type of this JobBaseInfo.

        引擎类型。取值： - oracle-to-gaussdbv5：Oracle同步到GaussDB分布式版，实时同步场景使用。

        :param engine_type: The engine_type of this JobBaseInfo.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def job_direction(self):
        """Gets the job_direction of this JobBaseInfo.

        迁移方向。取值： - up：入云 ，灾备场景时对应本云为备。 - down：出云，灾备场景时对应本云为主。 - non-dbs：自建。

        :return: The job_direction of this JobBaseInfo.
        :rtype: str
        """
        return self._job_direction

    @job_direction.setter
    def job_direction(self, job_direction):
        """Sets the job_direction of this JobBaseInfo.

        迁移方向。取值： - up：入云 ，灾备场景时对应本云为备。 - down：出云，灾备场景时对应本云为主。 - non-dbs：自建。

        :param job_direction: The job_direction of this JobBaseInfo.
        :type job_direction: str
        """
        self._job_direction = job_direction

    @property
    def task_type(self):
        """Gets the task_type of this JobBaseInfo.

        迁移模式。取值： - FULL_TRANS ：全量。 - FULL_INCR_TRANS：全量+增量。 - INCR_TRANS：增量。

        :return: The task_type of this JobBaseInfo.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this JobBaseInfo.

        迁移模式。取值： - FULL_TRANS ：全量。 - FULL_INCR_TRANS：全量+增量。 - INCR_TRANS：增量。

        :param task_type: The task_type of this JobBaseInfo.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def net_type(self):
        """Gets the net_type of this JobBaseInfo.

        网络类型。取值： - eip：公网网络。 - vpc：VPC网络，灾备场景不支持选择VPC网络。 - vpn：VPN、专线网络。

        :return: The net_type of this JobBaseInfo.
        :rtype: str
        """
        return self._net_type

    @net_type.setter
    def net_type(self, net_type):
        """Sets the net_type of this JobBaseInfo.

        网络类型。取值： - eip：公网网络。 - vpc：VPC网络，灾备场景不支持选择VPC网络。 - vpn：VPN、专线网络。

        :param net_type: The net_type of this JobBaseInfo.
        :type net_type: str
        """
        self._net_type = net_type

    @property
    def charging_mode(self):
        """Gets the charging_mode of this JobBaseInfo.

        计费模式，默认按需。取值： - period：包周期。 - on_demand：按需。

        :return: The charging_mode of this JobBaseInfo.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this JobBaseInfo.

        计费模式，默认按需。取值： - period：包周期。 - on_demand：按需。

        :param charging_mode: The charging_mode of this JobBaseInfo.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this JobBaseInfo.

        企业项目ID。 缺省值：\"0\"，表示\"default\"企业项目。

        :return: The enterprise_project_id of this JobBaseInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this JobBaseInfo.

        企业项目ID。 缺省值：\"0\"，表示\"default\"企业项目。

        :param enterprise_project_id: The enterprise_project_id of this JobBaseInfo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def description(self):
        """Gets the description of this JobBaseInfo.

        任务描述。 约束：任务描述不能超过256位，且不能包含!<>&'\"\\特殊字符。

        :return: The description of this JobBaseInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this JobBaseInfo.

        任务描述。 约束：任务描述不能超过256位，且不能包含!<>&'\"\\特殊字符。

        :param description: The description of this JobBaseInfo.
        :type description: str
        """
        self._description = description

    @property
    def start_time(self):
        """Gets the start_time of this JobBaseInfo.

        任务定时启动时间。

        :return: The start_time of this JobBaseInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this JobBaseInfo.

        任务定时启动时间。

        :param start_time: The start_time of this JobBaseInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def expired_days(self):
        """Gets the expired_days of this JobBaseInfo.

        任务处于异常状态一段时间后，将会自动结束。单位为天。(范围14-100)，不传默认为14天。

        :return: The expired_days of this JobBaseInfo.
        :rtype: str
        """
        return self._expired_days

    @expired_days.setter
    def expired_days(self, expired_days):
        """Sets the expired_days of this JobBaseInfo.

        任务处于异常状态一段时间后，将会自动结束。单位为天。(范围14-100)，不传默认为14天。

        :param expired_days: The expired_days of this JobBaseInfo.
        :type expired_days: str
        """
        self._expired_days = expired_days

    @property
    def tags(self):
        """Gets the tags of this JobBaseInfo.

        标签信息，最多添加10个标签。

        :return: The tags of this JobBaseInfo.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this JobBaseInfo.

        标签信息，最多添加10个标签。

        :param tags: The tags of this JobBaseInfo.
        :type tags: list[:class:`huaweicloudsdkdrs.v5.ResourceTag`]
        """
        self._tags = tags

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
        if not isinstance(other, JobBaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
