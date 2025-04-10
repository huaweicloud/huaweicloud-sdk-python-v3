# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScheduledTaskHistory:

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
        'task_type': 'str',
        'execution_id': 'str',
        'associated_task_name': 'str',
        'associated_task_name_en': 'str',
        'region': 'str',
        'created_by': 'str',
        'started_time': 'int',
        'finished_time': 'int',
        'status': 'str',
        'execution_msg': 'str'
    }

    attribute_map = {
        'id': 'id',
        'task_type': 'task_type',
        'execution_id': 'execution_id',
        'associated_task_name': 'associated_task_name',
        'associated_task_name_en': 'associated_task_name_en',
        'region': 'region',
        'created_by': 'created_by',
        'started_time': 'started_time',
        'finished_time': 'finished_time',
        'status': 'status',
        'execution_msg': 'execution_msg'
    }

    def __init__(self, id=None, task_type=None, execution_id=None, associated_task_name=None, associated_task_name_en=None, region=None, created_by=None, started_time=None, finished_time=None, status=None, execution_msg=None):
        r"""ScheduledTaskHistory

        The model defined in huaweicloud sdk

        :param id: 历史记录ID
        :type id: str
        :param task_type: 引用任务类型
        :type task_type: str
        :param execution_id: 执行ID
        :type execution_id: str
        :param associated_task_name: 引用任务名称
        :type associated_task_name: str
        :param associated_task_name_en: 引用任务名称(英文)
        :type associated_task_name_en: str
        :param region: 区域
        :type region: str
        :param created_by: 创建人
        :type created_by: str
        :param started_time: 开始时间时间戳
        :type started_time: int
        :param finished_time: 结束时间时间戳
        :type finished_time: int
        :param status: 状态
        :type status: str
        :param execution_msg: 执行结果描述
        :type execution_msg: str
        """
        
        

        self._id = None
        self._task_type = None
        self._execution_id = None
        self._associated_task_name = None
        self._associated_task_name_en = None
        self._region = None
        self._created_by = None
        self._started_time = None
        self._finished_time = None
        self._status = None
        self._execution_msg = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if task_type is not None:
            self.task_type = task_type
        if execution_id is not None:
            self.execution_id = execution_id
        if associated_task_name is not None:
            self.associated_task_name = associated_task_name
        if associated_task_name_en is not None:
            self.associated_task_name_en = associated_task_name_en
        if region is not None:
            self.region = region
        if created_by is not None:
            self.created_by = created_by
        if started_time is not None:
            self.started_time = started_time
        if finished_time is not None:
            self.finished_time = finished_time
        if status is not None:
            self.status = status
        if execution_msg is not None:
            self.execution_msg = execution_msg

    @property
    def id(self):
        r"""Gets the id of this ScheduledTaskHistory.

        历史记录ID

        :return: The id of this ScheduledTaskHistory.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ScheduledTaskHistory.

        历史记录ID

        :param id: The id of this ScheduledTaskHistory.
        :type id: str
        """
        self._id = id

    @property
    def task_type(self):
        r"""Gets the task_type of this ScheduledTaskHistory.

        引用任务类型

        :return: The task_type of this ScheduledTaskHistory.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this ScheduledTaskHistory.

        引用任务类型

        :param task_type: The task_type of this ScheduledTaskHistory.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def execution_id(self):
        r"""Gets the execution_id of this ScheduledTaskHistory.

        执行ID

        :return: The execution_id of this ScheduledTaskHistory.
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        r"""Sets the execution_id of this ScheduledTaskHistory.

        执行ID

        :param execution_id: The execution_id of this ScheduledTaskHistory.
        :type execution_id: str
        """
        self._execution_id = execution_id

    @property
    def associated_task_name(self):
        r"""Gets the associated_task_name of this ScheduledTaskHistory.

        引用任务名称

        :return: The associated_task_name of this ScheduledTaskHistory.
        :rtype: str
        """
        return self._associated_task_name

    @associated_task_name.setter
    def associated_task_name(self, associated_task_name):
        r"""Sets the associated_task_name of this ScheduledTaskHistory.

        引用任务名称

        :param associated_task_name: The associated_task_name of this ScheduledTaskHistory.
        :type associated_task_name: str
        """
        self._associated_task_name = associated_task_name

    @property
    def associated_task_name_en(self):
        r"""Gets the associated_task_name_en of this ScheduledTaskHistory.

        引用任务名称(英文)

        :return: The associated_task_name_en of this ScheduledTaskHistory.
        :rtype: str
        """
        return self._associated_task_name_en

    @associated_task_name_en.setter
    def associated_task_name_en(self, associated_task_name_en):
        r"""Sets the associated_task_name_en of this ScheduledTaskHistory.

        引用任务名称(英文)

        :param associated_task_name_en: The associated_task_name_en of this ScheduledTaskHistory.
        :type associated_task_name_en: str
        """
        self._associated_task_name_en = associated_task_name_en

    @property
    def region(self):
        r"""Gets the region of this ScheduledTaskHistory.

        区域

        :return: The region of this ScheduledTaskHistory.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ScheduledTaskHistory.

        区域

        :param region: The region of this ScheduledTaskHistory.
        :type region: str
        """
        self._region = region

    @property
    def created_by(self):
        r"""Gets the created_by of this ScheduledTaskHistory.

        创建人

        :return: The created_by of this ScheduledTaskHistory.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this ScheduledTaskHistory.

        创建人

        :param created_by: The created_by of this ScheduledTaskHistory.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def started_time(self):
        r"""Gets the started_time of this ScheduledTaskHistory.

        开始时间时间戳

        :return: The started_time of this ScheduledTaskHistory.
        :rtype: int
        """
        return self._started_time

    @started_time.setter
    def started_time(self, started_time):
        r"""Sets the started_time of this ScheduledTaskHistory.

        开始时间时间戳

        :param started_time: The started_time of this ScheduledTaskHistory.
        :type started_time: int
        """
        self._started_time = started_time

    @property
    def finished_time(self):
        r"""Gets the finished_time of this ScheduledTaskHistory.

        结束时间时间戳

        :return: The finished_time of this ScheduledTaskHistory.
        :rtype: int
        """
        return self._finished_time

    @finished_time.setter
    def finished_time(self, finished_time):
        r"""Sets the finished_time of this ScheduledTaskHistory.

        结束时间时间戳

        :param finished_time: The finished_time of this ScheduledTaskHistory.
        :type finished_time: int
        """
        self._finished_time = finished_time

    @property
    def status(self):
        r"""Gets the status of this ScheduledTaskHistory.

        状态

        :return: The status of this ScheduledTaskHistory.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ScheduledTaskHistory.

        状态

        :param status: The status of this ScheduledTaskHistory.
        :type status: str
        """
        self._status = status

    @property
    def execution_msg(self):
        r"""Gets the execution_msg of this ScheduledTaskHistory.

        执行结果描述

        :return: The execution_msg of this ScheduledTaskHistory.
        :rtype: str
        """
        return self._execution_msg

    @execution_msg.setter
    def execution_msg(self, execution_msg):
        r"""Sets the execution_msg of this ScheduledTaskHistory.

        执行结果描述

        :param execution_msg: The execution_msg of this ScheduledTaskHistory.
        :type execution_msg: str
        """
        self._execution_msg = execution_msg

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
        if not isinstance(other, ScheduledTaskHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
