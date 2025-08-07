# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Task:

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
        'order_id': 'str',
        'process': 'str',
        'fail_reason': 'str',
        'create_time': 'str',
        'end_time': 'str',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'instance_status': 'instance_status',
        'order_id': 'order_id',
        'process': 'process',
        'fail_reason': 'fail_reason',
        'create_time': 'create_time',
        'end_time': 'end_time',
        'status': 'status'
    }

    def __init__(self, id=None, name=None, instance_id=None, instance_name=None, instance_status=None, order_id=None, process=None, fail_reason=None, create_time=None, end_time=None, status=None):
        r"""Task

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
        :param order_id: 订单ID。
        :type order_id: str
        :param process: 任务进度，单位百分比，取值范围：0-100。当任务成功或者失败状态下，该值为空字符串。
        :type process: str
        :param fail_reason: 失败原因。
        :type fail_reason: str
        :param create_time: 任务创建时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type create_time: str
        :param end_time: 任务计划结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type end_time: str
        :param status: 任务状态。取值范围如下： Running:运行中 Completed:已完成 Failed:已失败
        :type status: str
        """
        
        

        self._id = None
        self._name = None
        self._instance_id = None
        self._instance_name = None
        self._instance_status = None
        self._order_id = None
        self._process = None
        self._fail_reason = None
        self._create_time = None
        self._end_time = None
        self._status = None
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
        if order_id is not None:
            self.order_id = order_id
        if process is not None:
            self.process = process
        if fail_reason is not None:
            self.fail_reason = fail_reason
        if create_time is not None:
            self.create_time = create_time
        if end_time is not None:
            self.end_time = end_time
        if status is not None:
            self.status = status

    @property
    def id(self):
        r"""Gets the id of this Task.

        任务ID。

        :return: The id of this Task.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Task.

        任务ID。

        :param id: The id of this Task.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this Task.

        任务名称。

        :return: The name of this Task.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Task.

        任务名称。

        :param name: The name of this Task.
        :type name: str
        """
        self._name = name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this Task.

        实例ID。

        :return: The instance_id of this Task.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this Task.

        实例ID。

        :param instance_id: The instance_id of this Task.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this Task.

        实例名称。

        :return: The instance_name of this Task.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this Task.

        实例名称。

        :param instance_name: The instance_name of this Task.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def instance_status(self):
        r"""Gets the instance_status of this Task.

        实例状态。 - 值为“BUILD”，表示实例正在创建。 - 值为“CREATE FAIL”，表示实例创建失败。 - 值为“ACTIVE”，表示实例正常。 - 值为“FAILED”，表示实例异常。 - 值为“FROZEN”，表示实例冻结。 - 值为“MODIFYING”，表示实例正在扩容。 - 值为“REBOOTING”，表示实例正在重启。 - 值为“RESTORING”，表示实例正在恢复。 - 值为“MODIFYING INSTANCE TYPE”，表示实例正在转主备。 - 值为“SWITCHOVER”，表示实例正在主备切换。 - 值为“MIGRATING”，表示实例正在迁移。 - 值为“BACKING UP”，表示实例正在进行备份。 - 值为“MODIFYING DATABASE PORT”，表示实例正在修改数据库端口。 - 值为“STORAGE FULL”，表示实例磁盘空间满。

        :return: The instance_status of this Task.
        :rtype: str
        """
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance_status):
        r"""Sets the instance_status of this Task.

        实例状态。 - 值为“BUILD”，表示实例正在创建。 - 值为“CREATE FAIL”，表示实例创建失败。 - 值为“ACTIVE”，表示实例正常。 - 值为“FAILED”，表示实例异常。 - 值为“FROZEN”，表示实例冻结。 - 值为“MODIFYING”，表示实例正在扩容。 - 值为“REBOOTING”，表示实例正在重启。 - 值为“RESTORING”，表示实例正在恢复。 - 值为“MODIFYING INSTANCE TYPE”，表示实例正在转主备。 - 值为“SWITCHOVER”，表示实例正在主备切换。 - 值为“MIGRATING”，表示实例正在迁移。 - 值为“BACKING UP”，表示实例正在进行备份。 - 值为“MODIFYING DATABASE PORT”，表示实例正在修改数据库端口。 - 值为“STORAGE FULL”，表示实例磁盘空间满。

        :param instance_status: The instance_status of this Task.
        :type instance_status: str
        """
        self._instance_status = instance_status

    @property
    def order_id(self):
        r"""Gets the order_id of this Task.

        订单ID。

        :return: The order_id of this Task.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this Task.

        订单ID。

        :param order_id: The order_id of this Task.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def process(self):
        r"""Gets the process of this Task.

        任务进度，单位百分比，取值范围：0-100。当任务成功或者失败状态下，该值为空字符串。

        :return: The process of this Task.
        :rtype: str
        """
        return self._process

    @process.setter
    def process(self, process):
        r"""Sets the process of this Task.

        任务进度，单位百分比，取值范围：0-100。当任务成功或者失败状态下，该值为空字符串。

        :param process: The process of this Task.
        :type process: str
        """
        self._process = process

    @property
    def fail_reason(self):
        r"""Gets the fail_reason of this Task.

        失败原因。

        :return: The fail_reason of this Task.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        r"""Sets the fail_reason of this Task.

        失败原因。

        :param fail_reason: The fail_reason of this Task.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

    @property
    def create_time(self):
        r"""Gets the create_time of this Task.

        任务创建时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The create_time of this Task.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this Task.

        任务创建时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param create_time: The create_time of this Task.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def end_time(self):
        r"""Gets the end_time of this Task.

        任务计划结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The end_time of this Task.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this Task.

        任务计划结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param end_time: The end_time of this Task.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def status(self):
        r"""Gets the status of this Task.

        任务状态。取值范围如下： Running:运行中 Completed:已完成 Failed:已失败

        :return: The status of this Task.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Task.

        任务状态。取值范围如下： Running:运行中 Completed:已完成 Failed:已失败

        :param status: The status of this Task.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, Task):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
