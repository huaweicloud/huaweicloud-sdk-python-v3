# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScheduledTaskV3:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_time': 'int',
        'end_time': 'int',
        'instance_id': 'str',
        'project_id': 'str',
        'proxy_id': 'str',
        'proxy_name': 'str',
        'start_time': 'int',
        'task_id': 'str',
        'task_name': 'str',
        'task_status': 'str'
    }

    attribute_map = {
        'create_time': 'create_time',
        'end_time': 'end_time',
        'instance_id': 'instance_id',
        'project_id': 'project_id',
        'proxy_id': 'proxy_id',
        'proxy_name': 'proxy_name',
        'start_time': 'start_time',
        'task_id': 'task_id',
        'task_name': 'task_name',
        'task_status': 'task_status'
    }

    def __init__(self, create_time=None, end_time=None, instance_id=None, project_id=None, proxy_id=None, proxy_name=None, start_time=None, task_id=None, task_name=None, task_status=None):
        r"""ScheduledTaskV3

        The model defined in huaweicloud sdk

        :param create_time: **参数解释**：  任务创建时间。  **取值范围**： 不涉及。
        :type create_time: int
        :param end_time: **参数解释**：  任务结束时间。  **取值范围**： 不涉及。
        :type end_time: int
        :param instance_id: **参数解释**：  任务绑定的实例ID。  **取值范围**： 不涉及。
        :type instance_id: str
        :param project_id: **参数解释**：  租户项目ID。  **取值范围**： 不涉及。
        :type project_id: str
        :param proxy_id: **参数解释**：  任务使用的数据库代理ID。  **取值范围**： 不涉及。
        :type proxy_id: str
        :param proxy_name: **参数解释**：  任务使用的数据库代理名称。  **取值范围**： 不涉及。
        :type proxy_name: str
        :param start_time: **参数解释**：  任务开始时间。  **取值范围**： 不涉及。
        :type start_time: int
        :param task_id: **参数解释**：  任务ID，此参数是任务的唯一标识。  **取值范围**： 不涉及。
        :type task_id: str
        :param task_name: **参数解释**：  任务名称。  **取值范围**： 不涉及。
        :type task_name: str
        :param task_status: **参数解释**：  任务状态。  **取值范围**： - RUNNING：任务正在执行。 - SUCCESS：任务执行成功。 - FAIL：任务执行失败。 - CANCELED：任务被取消。 - WAITING：任务等待执行。
        :type task_status: str
        """
        
        

        self._create_time = None
        self._end_time = None
        self._instance_id = None
        self._project_id = None
        self._proxy_id = None
        self._proxy_name = None
        self._start_time = None
        self._task_id = None
        self._task_name = None
        self._task_status = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if end_time is not None:
            self.end_time = end_time
        if instance_id is not None:
            self.instance_id = instance_id
        if project_id is not None:
            self.project_id = project_id
        if proxy_id is not None:
            self.proxy_id = proxy_id
        if proxy_name is not None:
            self.proxy_name = proxy_name
        if start_time is not None:
            self.start_time = start_time
        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if task_status is not None:
            self.task_status = task_status

    @property
    def create_time(self):
        r"""Gets the create_time of this ScheduledTaskV3.

        **参数解释**：  任务创建时间。  **取值范围**： 不涉及。

        :return: The create_time of this ScheduledTaskV3.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ScheduledTaskV3.

        **参数解释**：  任务创建时间。  **取值范围**： 不涉及。

        :param create_time: The create_time of this ScheduledTaskV3.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ScheduledTaskV3.

        **参数解释**：  任务结束时间。  **取值范围**： 不涉及。

        :return: The end_time of this ScheduledTaskV3.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ScheduledTaskV3.

        **参数解释**：  任务结束时间。  **取值范围**： 不涉及。

        :param end_time: The end_time of this ScheduledTaskV3.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ScheduledTaskV3.

        **参数解释**：  任务绑定的实例ID。  **取值范围**： 不涉及。

        :return: The instance_id of this ScheduledTaskV3.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ScheduledTaskV3.

        **参数解释**：  任务绑定的实例ID。  **取值范围**： 不涉及。

        :param instance_id: The instance_id of this ScheduledTaskV3.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ScheduledTaskV3.

        **参数解释**：  租户项目ID。  **取值范围**： 不涉及。

        :return: The project_id of this ScheduledTaskV3.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ScheduledTaskV3.

        **参数解释**：  租户项目ID。  **取值范围**： 不涉及。

        :param project_id: The project_id of this ScheduledTaskV3.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def proxy_id(self):
        r"""Gets the proxy_id of this ScheduledTaskV3.

        **参数解释**：  任务使用的数据库代理ID。  **取值范围**： 不涉及。

        :return: The proxy_id of this ScheduledTaskV3.
        :rtype: str
        """
        return self._proxy_id

    @proxy_id.setter
    def proxy_id(self, proxy_id):
        r"""Sets the proxy_id of this ScheduledTaskV3.

        **参数解释**：  任务使用的数据库代理ID。  **取值范围**： 不涉及。

        :param proxy_id: The proxy_id of this ScheduledTaskV3.
        :type proxy_id: str
        """
        self._proxy_id = proxy_id

    @property
    def proxy_name(self):
        r"""Gets the proxy_name of this ScheduledTaskV3.

        **参数解释**：  任务使用的数据库代理名称。  **取值范围**： 不涉及。

        :return: The proxy_name of this ScheduledTaskV3.
        :rtype: str
        """
        return self._proxy_name

    @proxy_name.setter
    def proxy_name(self, proxy_name):
        r"""Sets the proxy_name of this ScheduledTaskV3.

        **参数解释**：  任务使用的数据库代理名称。  **取值范围**： 不涉及。

        :param proxy_name: The proxy_name of this ScheduledTaskV3.
        :type proxy_name: str
        """
        self._proxy_name = proxy_name

    @property
    def start_time(self):
        r"""Gets the start_time of this ScheduledTaskV3.

        **参数解释**：  任务开始时间。  **取值范围**： 不涉及。

        :return: The start_time of this ScheduledTaskV3.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ScheduledTaskV3.

        **参数解释**：  任务开始时间。  **取值范围**： 不涉及。

        :param start_time: The start_time of this ScheduledTaskV3.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def task_id(self):
        r"""Gets the task_id of this ScheduledTaskV3.

        **参数解释**：  任务ID，此参数是任务的唯一标识。  **取值范围**： 不涉及。

        :return: The task_id of this ScheduledTaskV3.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ScheduledTaskV3.

        **参数解释**：  任务ID，此参数是任务的唯一标识。  **取值范围**： 不涉及。

        :param task_id: The task_id of this ScheduledTaskV3.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        r"""Gets the task_name of this ScheduledTaskV3.

        **参数解释**：  任务名称。  **取值范围**： 不涉及。

        :return: The task_name of this ScheduledTaskV3.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this ScheduledTaskV3.

        **参数解释**：  任务名称。  **取值范围**： 不涉及。

        :param task_name: The task_name of this ScheduledTaskV3.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def task_status(self):
        r"""Gets the task_status of this ScheduledTaskV3.

        **参数解释**：  任务状态。  **取值范围**： - RUNNING：任务正在执行。 - SUCCESS：任务执行成功。 - FAIL：任务执行失败。 - CANCELED：任务被取消。 - WAITING：任务等待执行。

        :return: The task_status of this ScheduledTaskV3.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        r"""Sets the task_status of this ScheduledTaskV3.

        **参数解释**：  任务状态。  **取值范围**： - RUNNING：任务正在执行。 - SUCCESS：任务执行成功。 - FAIL：任务执行失败。 - CANCELED：任务被取消。 - WAITING：任务等待执行。

        :param task_status: The task_status of this ScheduledTaskV3.
        :type task_status: str
        """
        self._task_status = task_status

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ScheduledTaskV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
