# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTasksRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'task_id': 'str',
        'name': 'str',
        'status': 'int',
        'task_type': 'str',
        'source_datasource_id': 'str',
        'target_datasource_id': 'str',
        'sort_field': 'str',
        'sort_type': 'str',
        'execute_status': 'str',
        'source_app_id': 'str',
        'target_app_id': 'str',
        'task_tag': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'limit': 'limit',
        'offset': 'offset',
        'task_id': 'task_id',
        'name': 'name',
        'status': 'status',
        'task_type': 'task_type',
        'source_datasource_id': 'source_datasource_id',
        'target_datasource_id': 'target_datasource_id',
        'sort_field': 'sort_field',
        'sort_type': 'sort_type',
        'execute_status': 'execute_status',
        'source_app_id': 'source_app_id',
        'target_app_id': 'target_app_id',
        'task_tag': 'task_tag'
    }

    def __init__(self, instance_id=None, limit=None, offset=None, task_id=None, name=None, status=None, task_type=None, source_datasource_id=None, target_datasource_id=None, sort_field=None, sort_type=None, execute_status=None, source_app_id=None, target_app_id=None, task_tag=None):
        """ListTasksRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param limit: 每页显示条目数量，最大数量999，超过999后只返回999
        :type limit: int
        :param offset: 分页查询，分页的偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0
        :type offset: int
        :param task_id: 任务ID，可为空
        :type task_id: str
        :param name: 模糊匹配任务名称，可为空
        :type name: str
        :param status: 任务状态，可为空 - 0 （停止/未启动） - 1 （运行中）
        :type status: int
        :param task_type: 任务类型 - realtime (实时) - timing (定时)
        :type task_type: str
        :param source_datasource_id: 源端数据源ID，可为空
        :type source_datasource_id: str
        :param target_datasource_id: 目标端数据源ID，可为空
        :type target_datasource_id: str
        :param sort_field: 查询排序的条件
        :type sort_field: str
        :param sort_type: 排序类型，可为空 - ASC (升序) - DESC (降序)
        :type sort_type: str
        :param execute_status: 执行状态，可为空 - UNSTARTED (未启动) - WAITING (等待执行) - RUNNING (执行中) - SUCCESS (执行成功) - CANCELLED (任务取消) - ERROR (执行异常)
        :type execute_status: str
        :param source_app_id: 源端数据源所属集成应用ID，可为空
        :type source_app_id: str
        :param target_app_id: 目标端数据源所属集成应用ID，可为空
        :type target_app_id: str
        :param task_tag: 任务标签，可为空
        :type task_tag: str
        """
        
        

        self._instance_id = None
        self._limit = None
        self._offset = None
        self._task_id = None
        self._name = None
        self._status = None
        self._task_type = None
        self._source_datasource_id = None
        self._target_datasource_id = None
        self._sort_field = None
        self._sort_type = None
        self._execute_status = None
        self._source_app_id = None
        self._target_app_id = None
        self._task_tag = None
        self.discriminator = None

        self.instance_id = instance_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if task_id is not None:
            self.task_id = task_id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if task_type is not None:
            self.task_type = task_type
        if source_datasource_id is not None:
            self.source_datasource_id = source_datasource_id
        if target_datasource_id is not None:
            self.target_datasource_id = target_datasource_id
        if sort_field is not None:
            self.sort_field = sort_field
        if sort_type is not None:
            self.sort_type = sort_type
        if execute_status is not None:
            self.execute_status = execute_status
        if source_app_id is not None:
            self.source_app_id = source_app_id
        if target_app_id is not None:
            self.target_app_id = target_app_id
        if task_tag is not None:
            self.task_tag = task_tag

    @property
    def instance_id(self):
        """Gets the instance_id of this ListTasksRequest.

        实例ID

        :return: The instance_id of this ListTasksRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListTasksRequest.

        实例ID

        :param instance_id: The instance_id of this ListTasksRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def limit(self):
        """Gets the limit of this ListTasksRequest.

        每页显示条目数量，最大数量999，超过999后只返回999

        :return: The limit of this ListTasksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListTasksRequest.

        每页显示条目数量，最大数量999，超过999后只返回999

        :param limit: The limit of this ListTasksRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListTasksRequest.

        分页查询，分页的偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :return: The offset of this ListTasksRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListTasksRequest.

        分页查询，分页的偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :param offset: The offset of this ListTasksRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def task_id(self):
        """Gets the task_id of this ListTasksRequest.

        任务ID，可为空

        :return: The task_id of this ListTasksRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ListTasksRequest.

        任务ID，可为空

        :param task_id: The task_id of this ListTasksRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def name(self):
        """Gets the name of this ListTasksRequest.

        模糊匹配任务名称，可为空

        :return: The name of this ListTasksRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListTasksRequest.

        模糊匹配任务名称，可为空

        :param name: The name of this ListTasksRequest.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this ListTasksRequest.

        任务状态，可为空 - 0 （停止/未启动） - 1 （运行中）

        :return: The status of this ListTasksRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListTasksRequest.

        任务状态，可为空 - 0 （停止/未启动） - 1 （运行中）

        :param status: The status of this ListTasksRequest.
        :type status: int
        """
        self._status = status

    @property
    def task_type(self):
        """Gets the task_type of this ListTasksRequest.

        任务类型 - realtime (实时) - timing (定时)

        :return: The task_type of this ListTasksRequest.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this ListTasksRequest.

        任务类型 - realtime (实时) - timing (定时)

        :param task_type: The task_type of this ListTasksRequest.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def source_datasource_id(self):
        """Gets the source_datasource_id of this ListTasksRequest.

        源端数据源ID，可为空

        :return: The source_datasource_id of this ListTasksRequest.
        :rtype: str
        """
        return self._source_datasource_id

    @source_datasource_id.setter
    def source_datasource_id(self, source_datasource_id):
        """Sets the source_datasource_id of this ListTasksRequest.

        源端数据源ID，可为空

        :param source_datasource_id: The source_datasource_id of this ListTasksRequest.
        :type source_datasource_id: str
        """
        self._source_datasource_id = source_datasource_id

    @property
    def target_datasource_id(self):
        """Gets the target_datasource_id of this ListTasksRequest.

        目标端数据源ID，可为空

        :return: The target_datasource_id of this ListTasksRequest.
        :rtype: str
        """
        return self._target_datasource_id

    @target_datasource_id.setter
    def target_datasource_id(self, target_datasource_id):
        """Sets the target_datasource_id of this ListTasksRequest.

        目标端数据源ID，可为空

        :param target_datasource_id: The target_datasource_id of this ListTasksRequest.
        :type target_datasource_id: str
        """
        self._target_datasource_id = target_datasource_id

    @property
    def sort_field(self):
        """Gets the sort_field of this ListTasksRequest.

        查询排序的条件

        :return: The sort_field of this ListTasksRequest.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        """Sets the sort_field of this ListTasksRequest.

        查询排序的条件

        :param sort_field: The sort_field of this ListTasksRequest.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def sort_type(self):
        """Gets the sort_type of this ListTasksRequest.

        排序类型，可为空 - ASC (升序) - DESC (降序)

        :return: The sort_type of this ListTasksRequest.
        :rtype: str
        """
        return self._sort_type

    @sort_type.setter
    def sort_type(self, sort_type):
        """Sets the sort_type of this ListTasksRequest.

        排序类型，可为空 - ASC (升序) - DESC (降序)

        :param sort_type: The sort_type of this ListTasksRequest.
        :type sort_type: str
        """
        self._sort_type = sort_type

    @property
    def execute_status(self):
        """Gets the execute_status of this ListTasksRequest.

        执行状态，可为空 - UNSTARTED (未启动) - WAITING (等待执行) - RUNNING (执行中) - SUCCESS (执行成功) - CANCELLED (任务取消) - ERROR (执行异常)

        :return: The execute_status of this ListTasksRequest.
        :rtype: str
        """
        return self._execute_status

    @execute_status.setter
    def execute_status(self, execute_status):
        """Sets the execute_status of this ListTasksRequest.

        执行状态，可为空 - UNSTARTED (未启动) - WAITING (等待执行) - RUNNING (执行中) - SUCCESS (执行成功) - CANCELLED (任务取消) - ERROR (执行异常)

        :param execute_status: The execute_status of this ListTasksRequest.
        :type execute_status: str
        """
        self._execute_status = execute_status

    @property
    def source_app_id(self):
        """Gets the source_app_id of this ListTasksRequest.

        源端数据源所属集成应用ID，可为空

        :return: The source_app_id of this ListTasksRequest.
        :rtype: str
        """
        return self._source_app_id

    @source_app_id.setter
    def source_app_id(self, source_app_id):
        """Sets the source_app_id of this ListTasksRequest.

        源端数据源所属集成应用ID，可为空

        :param source_app_id: The source_app_id of this ListTasksRequest.
        :type source_app_id: str
        """
        self._source_app_id = source_app_id

    @property
    def target_app_id(self):
        """Gets the target_app_id of this ListTasksRequest.

        目标端数据源所属集成应用ID，可为空

        :return: The target_app_id of this ListTasksRequest.
        :rtype: str
        """
        return self._target_app_id

    @target_app_id.setter
    def target_app_id(self, target_app_id):
        """Sets the target_app_id of this ListTasksRequest.

        目标端数据源所属集成应用ID，可为空

        :param target_app_id: The target_app_id of this ListTasksRequest.
        :type target_app_id: str
        """
        self._target_app_id = target_app_id

    @property
    def task_tag(self):
        """Gets the task_tag of this ListTasksRequest.

        任务标签，可为空

        :return: The task_tag of this ListTasksRequest.
        :rtype: str
        """
        return self._task_tag

    @task_tag.setter
    def task_tag(self, task_tag):
        """Sets the task_tag of this ListTasksRequest.

        任务标签，可为空

        :param task_tag: The task_tag of this ListTasksRequest.
        :type task_tag: str
        """
        self._task_tag = task_tag

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
        if not isinstance(other, ListTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
