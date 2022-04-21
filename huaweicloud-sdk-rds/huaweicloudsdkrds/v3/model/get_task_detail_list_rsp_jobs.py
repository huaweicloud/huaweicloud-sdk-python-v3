# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetTaskDetailListRspJobs:

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
        'status': 'str',
        'created': 'str',
        'ended': 'str',
        'process': 'str',
        'task_detail': 'str',
        'instance': 'GetTaskDetailListRspJobsInstance',
        'entities': 'object',
        'fail_reason': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'created': 'created',
        'ended': 'ended',
        'process': 'process',
        'task_detail': 'task_detail',
        'instance': 'instance',
        'entities': 'entities',
        'fail_reason': 'fail_reason'
    }

    def __init__(self, id=None, name=None, status=None, created=None, ended=None, process=None, task_detail=None, instance=None, entities=None, fail_reason=None):
        """GetTaskDetailListRspJobs

        The model defined in huaweicloud sdk

        :param id: 任务ID。
        :type id: str
        :param name: 任务名称。
        :type name: str
        :param status: 任务执行状态。  取值： - 值为“Running”，表示任务正在执行。 - 值为“Completed”，表示任务执行成功。 - 值为“Failed”，表示任务执行失败。
        :type status: str
        :param created: 创建时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type created: str
        :param ended: 结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type ended: str
        :param process: 任务执行进度。执行中状态才返回执行进度，例如60%，否则返回“”。
        :type process: str
        :param task_detail: 任务执行的具体的参数信息，为空则不返回该字段。
        :type task_detail: str
        :param instance: 
        :type instance: :class:`huaweicloudsdkrds.v3.GetTaskDetailListRspJobsInstance`
        :param entities: 根据不同的任务，显示不同的内容。
        :type entities: object
        :param fail_reason: 任务执行失败时的错误信息。
        :type fail_reason: str
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._created = None
        self._ended = None
        self._process = None
        self._task_detail = None
        self._instance = None
        self._entities = None
        self._fail_reason = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.status = status
        self.created = created
        if ended is not None:
            self.ended = ended
        if process is not None:
            self.process = process
        if task_detail is not None:
            self.task_detail = task_detail
        self.instance = instance
        if entities is not None:
            self.entities = entities
        if fail_reason is not None:
            self.fail_reason = fail_reason

    @property
    def id(self):
        """Gets the id of this GetTaskDetailListRspJobs.

        任务ID。

        :return: The id of this GetTaskDetailListRspJobs.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetTaskDetailListRspJobs.

        任务ID。

        :param id: The id of this GetTaskDetailListRspJobs.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this GetTaskDetailListRspJobs.

        任务名称。

        :return: The name of this GetTaskDetailListRspJobs.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetTaskDetailListRspJobs.

        任务名称。

        :param name: The name of this GetTaskDetailListRspJobs.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this GetTaskDetailListRspJobs.

        任务执行状态。  取值： - 值为“Running”，表示任务正在执行。 - 值为“Completed”，表示任务执行成功。 - 值为“Failed”，表示任务执行失败。

        :return: The status of this GetTaskDetailListRspJobs.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetTaskDetailListRspJobs.

        任务执行状态。  取值： - 值为“Running”，表示任务正在执行。 - 值为“Completed”，表示任务执行成功。 - 值为“Failed”，表示任务执行失败。

        :param status: The status of this GetTaskDetailListRspJobs.
        :type status: str
        """
        self._status = status

    @property
    def created(self):
        """Gets the created of this GetTaskDetailListRspJobs.

        创建时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The created of this GetTaskDetailListRspJobs.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this GetTaskDetailListRspJobs.

        创建时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param created: The created of this GetTaskDetailListRspJobs.
        :type created: str
        """
        self._created = created

    @property
    def ended(self):
        """Gets the ended of this GetTaskDetailListRspJobs.

        结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The ended of this GetTaskDetailListRspJobs.
        :rtype: str
        """
        return self._ended

    @ended.setter
    def ended(self, ended):
        """Sets the ended of this GetTaskDetailListRspJobs.

        结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param ended: The ended of this GetTaskDetailListRspJobs.
        :type ended: str
        """
        self._ended = ended

    @property
    def process(self):
        """Gets the process of this GetTaskDetailListRspJobs.

        任务执行进度。执行中状态才返回执行进度，例如60%，否则返回“”。

        :return: The process of this GetTaskDetailListRspJobs.
        :rtype: str
        """
        return self._process

    @process.setter
    def process(self, process):
        """Sets the process of this GetTaskDetailListRspJobs.

        任务执行进度。执行中状态才返回执行进度，例如60%，否则返回“”。

        :param process: The process of this GetTaskDetailListRspJobs.
        :type process: str
        """
        self._process = process

    @property
    def task_detail(self):
        """Gets the task_detail of this GetTaskDetailListRspJobs.

        任务执行的具体的参数信息，为空则不返回该字段。

        :return: The task_detail of this GetTaskDetailListRspJobs.
        :rtype: str
        """
        return self._task_detail

    @task_detail.setter
    def task_detail(self, task_detail):
        """Sets the task_detail of this GetTaskDetailListRspJobs.

        任务执行的具体的参数信息，为空则不返回该字段。

        :param task_detail: The task_detail of this GetTaskDetailListRspJobs.
        :type task_detail: str
        """
        self._task_detail = task_detail

    @property
    def instance(self):
        """Gets the instance of this GetTaskDetailListRspJobs.


        :return: The instance of this GetTaskDetailListRspJobs.
        :rtype: :class:`huaweicloudsdkrds.v3.GetTaskDetailListRspJobsInstance`
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this GetTaskDetailListRspJobs.


        :param instance: The instance of this GetTaskDetailListRspJobs.
        :type instance: :class:`huaweicloudsdkrds.v3.GetTaskDetailListRspJobsInstance`
        """
        self._instance = instance

    @property
    def entities(self):
        """Gets the entities of this GetTaskDetailListRspJobs.

        根据不同的任务，显示不同的内容。

        :return: The entities of this GetTaskDetailListRspJobs.
        :rtype: object
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this GetTaskDetailListRspJobs.

        根据不同的任务，显示不同的内容。

        :param entities: The entities of this GetTaskDetailListRspJobs.
        :type entities: object
        """
        self._entities = entities

    @property
    def fail_reason(self):
        """Gets the fail_reason of this GetTaskDetailListRspJobs.

        任务执行失败时的错误信息。

        :return: The fail_reason of this GetTaskDetailListRspJobs.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        """Sets the fail_reason of this GetTaskDetailListRspJobs.

        任务执行失败时的错误信息。

        :param fail_reason: The fail_reason of this GetTaskDetailListRspJobs.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

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
        if not isinstance(other, GetTaskDetailListRspJobs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
