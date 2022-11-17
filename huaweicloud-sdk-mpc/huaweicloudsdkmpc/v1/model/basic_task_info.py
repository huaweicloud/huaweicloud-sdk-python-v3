# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BasicTaskInfo:

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
        'status': 'str',
        'create_time': 'str',
        'end_time': 'str',
        'output': 'ObsObjInfo',
        'description': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'status': 'status',
        'create_time': 'create_time',
        'end_time': 'end_time',
        'output': 'output',
        'description': 'description'
    }

    def __init__(self, task_id=None, status=None, create_time=None, end_time=None, output=None, description=None):
        """BasicTaskInfo

        The model defined in huaweicloud sdk

        :param task_id: 任务Id
        :type task_id: str
        :param status: 任务执行状态，取值如下。 \&quot;NO_TASK\&quot;      //无任务，task_id非法 \&quot;WAITING\&quot;      //等待启动 \&quot;PROCESSING\&quot;   //处理中 \&quot;SUCCEEDED\&quot;    //成功 \&quot;FAILED\&quot;       //失败 \&quot;CANCELED\&quot;     //已删除 
        :type status: str
        :param create_time: 任务启动时间 
        :type create_time: str
        :param end_time: 任务结束时间 
        :type end_time: str
        :param output: 
        :type output: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        :param description: 任务描述，当出现异常时，此字段为异常的原因。 
        :type description: str
        """
        
        

        self._task_id = None
        self._status = None
        self._create_time = None
        self._end_time = None
        self._output = None
        self._description = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if end_time is not None:
            self.end_time = end_time
        if output is not None:
            self.output = output
        if description is not None:
            self.description = description

    @property
    def task_id(self):
        """Gets the task_id of this BasicTaskInfo.

        任务Id

        :return: The task_id of this BasicTaskInfo.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this BasicTaskInfo.

        任务Id

        :param task_id: The task_id of this BasicTaskInfo.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def status(self):
        """Gets the status of this BasicTaskInfo.

        任务执行状态，取值如下。 \"NO_TASK\"      //无任务，task_id非法 \"WAITING\"      //等待启动 \"PROCESSING\"   //处理中 \"SUCCEEDED\"    //成功 \"FAILED\"       //失败 \"CANCELED\"     //已删除 

        :return: The status of this BasicTaskInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BasicTaskInfo.

        任务执行状态，取值如下。 \"NO_TASK\"      //无任务，task_id非法 \"WAITING\"      //等待启动 \"PROCESSING\"   //处理中 \"SUCCEEDED\"    //成功 \"FAILED\"       //失败 \"CANCELED\"     //已删除 

        :param status: The status of this BasicTaskInfo.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this BasicTaskInfo.

        任务启动时间 

        :return: The create_time of this BasicTaskInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this BasicTaskInfo.

        任务启动时间 

        :param create_time: The create_time of this BasicTaskInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def end_time(self):
        """Gets the end_time of this BasicTaskInfo.

        任务结束时间 

        :return: The end_time of this BasicTaskInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this BasicTaskInfo.

        任务结束时间 

        :param end_time: The end_time of this BasicTaskInfo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def output(self):
        """Gets the output of this BasicTaskInfo.

        :return: The output of this BasicTaskInfo.
        :rtype: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this BasicTaskInfo.

        :param output: The output of this BasicTaskInfo.
        :type output: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        self._output = output

    @property
    def description(self):
        """Gets the description of this BasicTaskInfo.

        任务描述，当出现异常时，此字段为异常的原因。 

        :return: The description of this BasicTaskInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BasicTaskInfo.

        任务描述，当出现异常时，此字段为异常的原因。 

        :param description: The description of this BasicTaskInfo.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, BasicTaskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
