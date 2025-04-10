# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BriefTaskRespBean:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'task_name': 'str',
        'task_type': 'str',
        'status': 'int',
        'created_date': 'date',
        'version': 'str',
        'last_modified_time': 'int',
        'execute_status': 'str',
        'source_app_id': 'str',
        'target_app_id': 'str',
        'source_instance_id': 'str',
        'target_instance_id': 'str',
        'ext_type': 'str',
        'enterprise_project_id': 'str',
        'task_tag': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'task_name': 'task_name',
        'task_type': 'task_type',
        'status': 'status',
        'created_date': 'created_date',
        'version': 'version',
        'last_modified_time': 'last_modified_time',
        'execute_status': 'execute_status',
        'source_app_id': 'source_app_id',
        'target_app_id': 'target_app_id',
        'source_instance_id': 'source_instance_id',
        'target_instance_id': 'target_instance_id',
        'ext_type': 'ext_type',
        'enterprise_project_id': 'enterprise_project_id',
        'task_tag': 'task_tag'
    }

    def __init__(self, task_id=None, task_name=None, task_type=None, status=None, created_date=None, version=None, last_modified_time=None, execute_status=None, source_app_id=None, target_app_id=None, source_instance_id=None, target_instance_id=None, ext_type=None, enterprise_project_id=None, task_tag=None):
        r"""BriefTaskRespBean

        The model defined in huaweicloud sdk

        :param task_id: 任务ID
        :type task_id: str
        :param task_name: 任务名称
        :type task_name: str
        :param task_type: 任务类型 - REALTIME (实时) - TIMING (定时)
        :type task_type: str
        :param status: 任务状态 - 0 (停止/未启动) - 1 (运行中)
        :type status: int
        :param created_date: 创建时间
        :type created_date: date
        :param version: 任务的版本
        :type version: str
        :param last_modified_time: 上次修改时间
        :type last_modified_time: int
        :param execute_status: 任务执行状态  - UNSTARTED (未启动)  - WAITING (等待执行)  - RUNNING (执行中)  - SUCCESS (执行成功)  - CANCELLED (任务取消)  - ERROR (执行异常)
        :type execute_status: str
        :param source_app_id: 源端数据源所属应用ID
        :type source_app_id: str
        :param target_app_id: 目标端数据源所属应用ID
        :type target_app_id: str
        :param source_instance_id: 源端实例ID
        :type source_instance_id: str
        :param target_instance_id: 目标端实例ID
        :type target_instance_id: str
        :param ext_type: 组合任务类型, 可为空
        :type ext_type: str
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        :param task_tag: 任务标签
        :type task_tag: str
        """
        
        

        self._task_id = None
        self._task_name = None
        self._task_type = None
        self._status = None
        self._created_date = None
        self._version = None
        self._last_modified_time = None
        self._execute_status = None
        self._source_app_id = None
        self._target_app_id = None
        self._source_instance_id = None
        self._target_instance_id = None
        self._ext_type = None
        self._enterprise_project_id = None
        self._task_tag = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if task_type is not None:
            self.task_type = task_type
        if status is not None:
            self.status = status
        if created_date is not None:
            self.created_date = created_date
        if version is not None:
            self.version = version
        if last_modified_time is not None:
            self.last_modified_time = last_modified_time
        if execute_status is not None:
            self.execute_status = execute_status
        if source_app_id is not None:
            self.source_app_id = source_app_id
        if target_app_id is not None:
            self.target_app_id = target_app_id
        if source_instance_id is not None:
            self.source_instance_id = source_instance_id
        if target_instance_id is not None:
            self.target_instance_id = target_instance_id
        if ext_type is not None:
            self.ext_type = ext_type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if task_tag is not None:
            self.task_tag = task_tag

    @property
    def task_id(self):
        r"""Gets the task_id of this BriefTaskRespBean.

        任务ID

        :return: The task_id of this BriefTaskRespBean.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this BriefTaskRespBean.

        任务ID

        :param task_id: The task_id of this BriefTaskRespBean.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        r"""Gets the task_name of this BriefTaskRespBean.

        任务名称

        :return: The task_name of this BriefTaskRespBean.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this BriefTaskRespBean.

        任务名称

        :param task_name: The task_name of this BriefTaskRespBean.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def task_type(self):
        r"""Gets the task_type of this BriefTaskRespBean.

        任务类型 - REALTIME (实时) - TIMING (定时)

        :return: The task_type of this BriefTaskRespBean.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this BriefTaskRespBean.

        任务类型 - REALTIME (实时) - TIMING (定时)

        :param task_type: The task_type of this BriefTaskRespBean.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def status(self):
        r"""Gets the status of this BriefTaskRespBean.

        任务状态 - 0 (停止/未启动) - 1 (运行中)

        :return: The status of this BriefTaskRespBean.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BriefTaskRespBean.

        任务状态 - 0 (停止/未启动) - 1 (运行中)

        :param status: The status of this BriefTaskRespBean.
        :type status: int
        """
        self._status = status

    @property
    def created_date(self):
        r"""Gets the created_date of this BriefTaskRespBean.

        创建时间

        :return: The created_date of this BriefTaskRespBean.
        :rtype: date
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        r"""Sets the created_date of this BriefTaskRespBean.

        创建时间

        :param created_date: The created_date of this BriefTaskRespBean.
        :type created_date: date
        """
        self._created_date = created_date

    @property
    def version(self):
        r"""Gets the version of this BriefTaskRespBean.

        任务的版本

        :return: The version of this BriefTaskRespBean.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this BriefTaskRespBean.

        任务的版本

        :param version: The version of this BriefTaskRespBean.
        :type version: str
        """
        self._version = version

    @property
    def last_modified_time(self):
        r"""Gets the last_modified_time of this BriefTaskRespBean.

        上次修改时间

        :return: The last_modified_time of this BriefTaskRespBean.
        :rtype: int
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        r"""Sets the last_modified_time of this BriefTaskRespBean.

        上次修改时间

        :param last_modified_time: The last_modified_time of this BriefTaskRespBean.
        :type last_modified_time: int
        """
        self._last_modified_time = last_modified_time

    @property
    def execute_status(self):
        r"""Gets the execute_status of this BriefTaskRespBean.

        任务执行状态  - UNSTARTED (未启动)  - WAITING (等待执行)  - RUNNING (执行中)  - SUCCESS (执行成功)  - CANCELLED (任务取消)  - ERROR (执行异常)

        :return: The execute_status of this BriefTaskRespBean.
        :rtype: str
        """
        return self._execute_status

    @execute_status.setter
    def execute_status(self, execute_status):
        r"""Sets the execute_status of this BriefTaskRespBean.

        任务执行状态  - UNSTARTED (未启动)  - WAITING (等待执行)  - RUNNING (执行中)  - SUCCESS (执行成功)  - CANCELLED (任务取消)  - ERROR (执行异常)

        :param execute_status: The execute_status of this BriefTaskRespBean.
        :type execute_status: str
        """
        self._execute_status = execute_status

    @property
    def source_app_id(self):
        r"""Gets the source_app_id of this BriefTaskRespBean.

        源端数据源所属应用ID

        :return: The source_app_id of this BriefTaskRespBean.
        :rtype: str
        """
        return self._source_app_id

    @source_app_id.setter
    def source_app_id(self, source_app_id):
        r"""Sets the source_app_id of this BriefTaskRespBean.

        源端数据源所属应用ID

        :param source_app_id: The source_app_id of this BriefTaskRespBean.
        :type source_app_id: str
        """
        self._source_app_id = source_app_id

    @property
    def target_app_id(self):
        r"""Gets the target_app_id of this BriefTaskRespBean.

        目标端数据源所属应用ID

        :return: The target_app_id of this BriefTaskRespBean.
        :rtype: str
        """
        return self._target_app_id

    @target_app_id.setter
    def target_app_id(self, target_app_id):
        r"""Sets the target_app_id of this BriefTaskRespBean.

        目标端数据源所属应用ID

        :param target_app_id: The target_app_id of this BriefTaskRespBean.
        :type target_app_id: str
        """
        self._target_app_id = target_app_id

    @property
    def source_instance_id(self):
        r"""Gets the source_instance_id of this BriefTaskRespBean.

        源端实例ID

        :return: The source_instance_id of this BriefTaskRespBean.
        :rtype: str
        """
        return self._source_instance_id

    @source_instance_id.setter
    def source_instance_id(self, source_instance_id):
        r"""Sets the source_instance_id of this BriefTaskRespBean.

        源端实例ID

        :param source_instance_id: The source_instance_id of this BriefTaskRespBean.
        :type source_instance_id: str
        """
        self._source_instance_id = source_instance_id

    @property
    def target_instance_id(self):
        r"""Gets the target_instance_id of this BriefTaskRespBean.

        目标端实例ID

        :return: The target_instance_id of this BriefTaskRespBean.
        :rtype: str
        """
        return self._target_instance_id

    @target_instance_id.setter
    def target_instance_id(self, target_instance_id):
        r"""Sets the target_instance_id of this BriefTaskRespBean.

        目标端实例ID

        :param target_instance_id: The target_instance_id of this BriefTaskRespBean.
        :type target_instance_id: str
        """
        self._target_instance_id = target_instance_id

    @property
    def ext_type(self):
        r"""Gets the ext_type of this BriefTaskRespBean.

        组合任务类型, 可为空

        :return: The ext_type of this BriefTaskRespBean.
        :rtype: str
        """
        return self._ext_type

    @ext_type.setter
    def ext_type(self, ext_type):
        r"""Sets the ext_type of this BriefTaskRespBean.

        组合任务类型, 可为空

        :param ext_type: The ext_type of this BriefTaskRespBean.
        :type ext_type: str
        """
        self._ext_type = ext_type

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this BriefTaskRespBean.

        企业项目id

        :return: The enterprise_project_id of this BriefTaskRespBean.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this BriefTaskRespBean.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this BriefTaskRespBean.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def task_tag(self):
        r"""Gets the task_tag of this BriefTaskRespBean.

        任务标签

        :return: The task_tag of this BriefTaskRespBean.
        :rtype: str
        """
        return self._task_tag

    @task_tag.setter
    def task_tag(self, task_tag):
        r"""Sets the task_tag of this BriefTaskRespBean.

        任务标签

        :param task_tag: The task_tag of this BriefTaskRespBean.
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
        if not isinstance(other, BriefTaskRespBean):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
