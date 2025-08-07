# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScheduleTaskInfo:

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
        'instance_id': 'str',
        'instance_name': 'str',
        'instance_status': 'str',
        'project_id': 'str',
        'create_time': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'order': 'str',
        'status': 'str',
        'datastore_type': 'str',
        'volume_type': 'str',
        'target_config': 'TargetConfig'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'instance_status': 'instance_status',
        'project_id': 'project_id',
        'create_time': 'create_time',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'order': 'order',
        'status': 'status',
        'datastore_type': 'datastore_type',
        'volume_type': 'volume_type',
        'target_config': 'target_config'
    }

    def __init__(self, id=None, name=None, instance_id=None, instance_name=None, instance_status=None, project_id=None, create_time=None, start_time=None, end_time=None, order=None, status=None, datastore_type=None, volume_type=None, target_config=None):
        r"""ScheduleTaskInfo

        The model defined in huaweicloud sdk

        :param id: 任务ID。
        :type id: str
        :param name: 任务名称。
        :type name: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param instance_name: 实例名称。
        :type instance_name: str
        :param instance_status: 实例状态。 - 值为“BUILD”，表示实例正在创建。 - 值为“CREATE FAIL”，表示实例创建失败。 - 值为“ACTIVE”，表示实例正常。 - 值为“FAILED”，表示实例异常。 - 值为“FROZEN”，表示实例冻结。 - 值为“MODIFYING”，表示实例正在扩容。 - 值为“REBOOTING”，表示实例正在重启。 - 值为“RESTORING”，表示实例正在恢复。 - 值为“MODIFYING INSTANCE TYPE”，表示实例正在转主备。 - 值为“SWITCHOVER”，表示实例正在主备切换。 - 值为“MIGRATING”，表示实例正在迁移。 - 值为“BACKING UP”，表示实例正在进行备份。 - 值为“MODIFYING DATABASE PORT”，表示实例正在修改数据库端口。 - 值为“STORAGE FULL”，表示实例磁盘空间满。
        :type instance_status: str
        :param project_id: 项目ID。
        :type project_id: str
        :param create_time: 任务创建时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type create_time: str
        :param start_time: 任务计划开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type start_time: str
        :param end_time: 任务计划结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type end_time: str
        :param order: 任务优先级，整数取值范围1-100，数值越小优先级越高。
        :type order: str
        :param status: 任务状态。取值范围如下： Initing:初始化中 Pending:挂起 Running:运行中 Completed:已完成 Failed:已失败 Unauthorized:未授权 Canceled:已取消
        :type status: str
        :param datastore_type: 数据库类型。
        :type datastore_type: str
        :param volume_type: 磁盘类型。
        :type volume_type: str
        :param target_config: 
        :type target_config: :class:`huaweicloudsdkrds.v3.TargetConfig`
        """
        
        

        self._id = None
        self._name = None
        self._instance_id = None
        self._instance_name = None
        self._instance_status = None
        self._project_id = None
        self._create_time = None
        self._start_time = None
        self._end_time = None
        self._order = None
        self._status = None
        self._datastore_type = None
        self._volume_type = None
        self._target_config = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if instance_status is not None:
            self.instance_status = instance_status
        if project_id is not None:
            self.project_id = project_id
        if create_time is not None:
            self.create_time = create_time
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if order is not None:
            self.order = order
        if status is not None:
            self.status = status
        if datastore_type is not None:
            self.datastore_type = datastore_type
        if volume_type is not None:
            self.volume_type = volume_type
        if target_config is not None:
            self.target_config = target_config

    @property
    def id(self):
        r"""Gets the id of this ScheduleTaskInfo.

        任务ID。

        :return: The id of this ScheduleTaskInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ScheduleTaskInfo.

        任务ID。

        :param id: The id of this ScheduleTaskInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ScheduleTaskInfo.

        任务名称。

        :return: The name of this ScheduleTaskInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ScheduleTaskInfo.

        任务名称。

        :param name: The name of this ScheduleTaskInfo.
        :type name: str
        """
        self._name = name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ScheduleTaskInfo.

        实例ID。

        :return: The instance_id of this ScheduleTaskInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ScheduleTaskInfo.

        实例ID。

        :param instance_id: The instance_id of this ScheduleTaskInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this ScheduleTaskInfo.

        实例名称。

        :return: The instance_name of this ScheduleTaskInfo.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this ScheduleTaskInfo.

        实例名称。

        :param instance_name: The instance_name of this ScheduleTaskInfo.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def instance_status(self):
        r"""Gets the instance_status of this ScheduleTaskInfo.

        实例状态。 - 值为“BUILD”，表示实例正在创建。 - 值为“CREATE FAIL”，表示实例创建失败。 - 值为“ACTIVE”，表示实例正常。 - 值为“FAILED”，表示实例异常。 - 值为“FROZEN”，表示实例冻结。 - 值为“MODIFYING”，表示实例正在扩容。 - 值为“REBOOTING”，表示实例正在重启。 - 值为“RESTORING”，表示实例正在恢复。 - 值为“MODIFYING INSTANCE TYPE”，表示实例正在转主备。 - 值为“SWITCHOVER”，表示实例正在主备切换。 - 值为“MIGRATING”，表示实例正在迁移。 - 值为“BACKING UP”，表示实例正在进行备份。 - 值为“MODIFYING DATABASE PORT”，表示实例正在修改数据库端口。 - 值为“STORAGE FULL”，表示实例磁盘空间满。

        :return: The instance_status of this ScheduleTaskInfo.
        :rtype: str
        """
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance_status):
        r"""Sets the instance_status of this ScheduleTaskInfo.

        实例状态。 - 值为“BUILD”，表示实例正在创建。 - 值为“CREATE FAIL”，表示实例创建失败。 - 值为“ACTIVE”，表示实例正常。 - 值为“FAILED”，表示实例异常。 - 值为“FROZEN”，表示实例冻结。 - 值为“MODIFYING”，表示实例正在扩容。 - 值为“REBOOTING”，表示实例正在重启。 - 值为“RESTORING”，表示实例正在恢复。 - 值为“MODIFYING INSTANCE TYPE”，表示实例正在转主备。 - 值为“SWITCHOVER”，表示实例正在主备切换。 - 值为“MIGRATING”，表示实例正在迁移。 - 值为“BACKING UP”，表示实例正在进行备份。 - 值为“MODIFYING DATABASE PORT”，表示实例正在修改数据库端口。 - 值为“STORAGE FULL”，表示实例磁盘空间满。

        :param instance_status: The instance_status of this ScheduleTaskInfo.
        :type instance_status: str
        """
        self._instance_status = instance_status

    @property
    def project_id(self):
        r"""Gets the project_id of this ScheduleTaskInfo.

        项目ID。

        :return: The project_id of this ScheduleTaskInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ScheduleTaskInfo.

        项目ID。

        :param project_id: The project_id of this ScheduleTaskInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def create_time(self):
        r"""Gets the create_time of this ScheduleTaskInfo.

        任务创建时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The create_time of this ScheduleTaskInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ScheduleTaskInfo.

        任务创建时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param create_time: The create_time of this ScheduleTaskInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def start_time(self):
        r"""Gets the start_time of this ScheduleTaskInfo.

        任务计划开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The start_time of this ScheduleTaskInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ScheduleTaskInfo.

        任务计划开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param start_time: The start_time of this ScheduleTaskInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ScheduleTaskInfo.

        任务计划结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The end_time of this ScheduleTaskInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ScheduleTaskInfo.

        任务计划结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param end_time: The end_time of this ScheduleTaskInfo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def order(self):
        r"""Gets the order of this ScheduleTaskInfo.

        任务优先级，整数取值范围1-100，数值越小优先级越高。

        :return: The order of this ScheduleTaskInfo.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ScheduleTaskInfo.

        任务优先级，整数取值范围1-100，数值越小优先级越高。

        :param order: The order of this ScheduleTaskInfo.
        :type order: str
        """
        self._order = order

    @property
    def status(self):
        r"""Gets the status of this ScheduleTaskInfo.

        任务状态。取值范围如下： Initing:初始化中 Pending:挂起 Running:运行中 Completed:已完成 Failed:已失败 Unauthorized:未授权 Canceled:已取消

        :return: The status of this ScheduleTaskInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ScheduleTaskInfo.

        任务状态。取值范围如下： Initing:初始化中 Pending:挂起 Running:运行中 Completed:已完成 Failed:已失败 Unauthorized:未授权 Canceled:已取消

        :param status: The status of this ScheduleTaskInfo.
        :type status: str
        """
        self._status = status

    @property
    def datastore_type(self):
        r"""Gets the datastore_type of this ScheduleTaskInfo.

        数据库类型。

        :return: The datastore_type of this ScheduleTaskInfo.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        r"""Sets the datastore_type of this ScheduleTaskInfo.

        数据库类型。

        :param datastore_type: The datastore_type of this ScheduleTaskInfo.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def volume_type(self):
        r"""Gets the volume_type of this ScheduleTaskInfo.

        磁盘类型。

        :return: The volume_type of this ScheduleTaskInfo.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        r"""Sets the volume_type of this ScheduleTaskInfo.

        磁盘类型。

        :param volume_type: The volume_type of this ScheduleTaskInfo.
        :type volume_type: str
        """
        self._volume_type = volume_type

    @property
    def target_config(self):
        r"""Gets the target_config of this ScheduleTaskInfo.

        :return: The target_config of this ScheduleTaskInfo.
        :rtype: :class:`huaweicloudsdkrds.v3.TargetConfig`
        """
        return self._target_config

    @target_config.setter
    def target_config(self, target_config):
        r"""Sets the target_config of this ScheduleTaskInfo.

        :param target_config: The target_config of this ScheduleTaskInfo.
        :type target_config: :class:`huaweicloudsdkrds.v3.TargetConfig`
        """
        self._target_config = target_config

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
        if not isinstance(other, ScheduleTaskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
