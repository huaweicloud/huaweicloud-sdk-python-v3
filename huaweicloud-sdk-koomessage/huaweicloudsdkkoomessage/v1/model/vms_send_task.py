# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VmsSendTask:

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
        'task_state': 'str',
        'tpl_id': 'str',
        'tpl_name': 'str',
        'operator': 'str',
        'create_time': 'str',
        'send_time': 'str',
        'total_count': 'int',
        'success_count': 'int',
        'failed_count': 'int',
        'timeout_count': 'int',
        'exdata': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'task_name': 'task_name',
        'task_state': 'task_state',
        'tpl_id': 'tpl_id',
        'tpl_name': 'tpl_name',
        'operator': 'operator',
        'create_time': 'create_time',
        'send_time': 'send_time',
        'total_count': 'total_count',
        'success_count': 'success_count',
        'failed_count': 'failed_count',
        'timeout_count': 'timeout_count',
        'exdata': 'exdata'
    }

    def __init__(self, task_id=None, task_name=None, task_state=None, tpl_id=None, tpl_name=None, operator=None, create_time=None, send_time=None, total_count=None, success_count=None, failed_count=None, timeout_count=None, exdata=None):
        """VmsSendTask

        The model defined in huaweicloud sdk

        :param task_id: 智能信息基础版任务ID。
        :type task_id: str
        :param task_name: 智能信息基础版任务名称。
        :type task_name: str
        :param task_state: 智能信息基础版任务状态。
        :type task_state: str
        :param tpl_id: 智能信息基础版模板ID。
        :type tpl_id: str
        :param tpl_name: 智能信息基础版模板名称。
        :type tpl_name: str
        :param operator: 操作员。
        :type operator: str
        :param create_time: 智能信息基础版任务创建时间。
        :type create_time: str
        :param send_time: 智能信息基础版任务发送时间。
        :type send_time: str
        :param total_count: 需要发送的手机号码总数（有效号码总数）。
        :type total_count: int
        :param success_count: 已经发送成功的手机号码总数。
        :type success_count: int
        :param failed_count: 已经发送失败的手机号码总数。
        :type failed_count: int
        :param timeout_count: 已经发送超时失败的手机号码总数（72小时没接收到状态认定为超时失败）。
        :type timeout_count: int
        :param exdata: 扩展字段。  &gt; 预留字段。 
        :type exdata: str
        """
        
        

        self._task_id = None
        self._task_name = None
        self._task_state = None
        self._tpl_id = None
        self._tpl_name = None
        self._operator = None
        self._create_time = None
        self._send_time = None
        self._total_count = None
        self._success_count = None
        self._failed_count = None
        self._timeout_count = None
        self._exdata = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if task_state is not None:
            self.task_state = task_state
        if tpl_id is not None:
            self.tpl_id = tpl_id
        if tpl_name is not None:
            self.tpl_name = tpl_name
        if operator is not None:
            self.operator = operator
        if create_time is not None:
            self.create_time = create_time
        if send_time is not None:
            self.send_time = send_time
        if total_count is not None:
            self.total_count = total_count
        if success_count is not None:
            self.success_count = success_count
        if failed_count is not None:
            self.failed_count = failed_count
        if timeout_count is not None:
            self.timeout_count = timeout_count
        if exdata is not None:
            self.exdata = exdata

    @property
    def task_id(self):
        """Gets the task_id of this VmsSendTask.

        智能信息基础版任务ID。

        :return: The task_id of this VmsSendTask.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this VmsSendTask.

        智能信息基础版任务ID。

        :param task_id: The task_id of this VmsSendTask.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        """Gets the task_name of this VmsSendTask.

        智能信息基础版任务名称。

        :return: The task_name of this VmsSendTask.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this VmsSendTask.

        智能信息基础版任务名称。

        :param task_name: The task_name of this VmsSendTask.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def task_state(self):
        """Gets the task_state of this VmsSendTask.

        智能信息基础版任务状态。

        :return: The task_state of this VmsSendTask.
        :rtype: str
        """
        return self._task_state

    @task_state.setter
    def task_state(self, task_state):
        """Sets the task_state of this VmsSendTask.

        智能信息基础版任务状态。

        :param task_state: The task_state of this VmsSendTask.
        :type task_state: str
        """
        self._task_state = task_state

    @property
    def tpl_id(self):
        """Gets the tpl_id of this VmsSendTask.

        智能信息基础版模板ID。

        :return: The tpl_id of this VmsSendTask.
        :rtype: str
        """
        return self._tpl_id

    @tpl_id.setter
    def tpl_id(self, tpl_id):
        """Sets the tpl_id of this VmsSendTask.

        智能信息基础版模板ID。

        :param tpl_id: The tpl_id of this VmsSendTask.
        :type tpl_id: str
        """
        self._tpl_id = tpl_id

    @property
    def tpl_name(self):
        """Gets the tpl_name of this VmsSendTask.

        智能信息基础版模板名称。

        :return: The tpl_name of this VmsSendTask.
        :rtype: str
        """
        return self._tpl_name

    @tpl_name.setter
    def tpl_name(self, tpl_name):
        """Sets the tpl_name of this VmsSendTask.

        智能信息基础版模板名称。

        :param tpl_name: The tpl_name of this VmsSendTask.
        :type tpl_name: str
        """
        self._tpl_name = tpl_name

    @property
    def operator(self):
        """Gets the operator of this VmsSendTask.

        操作员。

        :return: The operator of this VmsSendTask.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this VmsSendTask.

        操作员。

        :param operator: The operator of this VmsSendTask.
        :type operator: str
        """
        self._operator = operator

    @property
    def create_time(self):
        """Gets the create_time of this VmsSendTask.

        智能信息基础版任务创建时间。

        :return: The create_time of this VmsSendTask.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this VmsSendTask.

        智能信息基础版任务创建时间。

        :param create_time: The create_time of this VmsSendTask.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def send_time(self):
        """Gets the send_time of this VmsSendTask.

        智能信息基础版任务发送时间。

        :return: The send_time of this VmsSendTask.
        :rtype: str
        """
        return self._send_time

    @send_time.setter
    def send_time(self, send_time):
        """Sets the send_time of this VmsSendTask.

        智能信息基础版任务发送时间。

        :param send_time: The send_time of this VmsSendTask.
        :type send_time: str
        """
        self._send_time = send_time

    @property
    def total_count(self):
        """Gets the total_count of this VmsSendTask.

        需要发送的手机号码总数（有效号码总数）。

        :return: The total_count of this VmsSendTask.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this VmsSendTask.

        需要发送的手机号码总数（有效号码总数）。

        :param total_count: The total_count of this VmsSendTask.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def success_count(self):
        """Gets the success_count of this VmsSendTask.

        已经发送成功的手机号码总数。

        :return: The success_count of this VmsSendTask.
        :rtype: int
        """
        return self._success_count

    @success_count.setter
    def success_count(self, success_count):
        """Sets the success_count of this VmsSendTask.

        已经发送成功的手机号码总数。

        :param success_count: The success_count of this VmsSendTask.
        :type success_count: int
        """
        self._success_count = success_count

    @property
    def failed_count(self):
        """Gets the failed_count of this VmsSendTask.

        已经发送失败的手机号码总数。

        :return: The failed_count of this VmsSendTask.
        :rtype: int
        """
        return self._failed_count

    @failed_count.setter
    def failed_count(self, failed_count):
        """Sets the failed_count of this VmsSendTask.

        已经发送失败的手机号码总数。

        :param failed_count: The failed_count of this VmsSendTask.
        :type failed_count: int
        """
        self._failed_count = failed_count

    @property
    def timeout_count(self):
        """Gets the timeout_count of this VmsSendTask.

        已经发送超时失败的手机号码总数（72小时没接收到状态认定为超时失败）。

        :return: The timeout_count of this VmsSendTask.
        :rtype: int
        """
        return self._timeout_count

    @timeout_count.setter
    def timeout_count(self, timeout_count):
        """Sets the timeout_count of this VmsSendTask.

        已经发送超时失败的手机号码总数（72小时没接收到状态认定为超时失败）。

        :param timeout_count: The timeout_count of this VmsSendTask.
        :type timeout_count: int
        """
        self._timeout_count = timeout_count

    @property
    def exdata(self):
        """Gets the exdata of this VmsSendTask.

        扩展字段。  > 预留字段。 

        :return: The exdata of this VmsSendTask.
        :rtype: str
        """
        return self._exdata

    @exdata.setter
    def exdata(self, exdata):
        """Sets the exdata of this VmsSendTask.

        扩展字段。  > 预留字段。 

        :param exdata: The exdata of this VmsSendTask.
        :type exdata: str
        """
        self._exdata = exdata

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
        if not isinstance(other, VmsSendTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
