# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TasksObject:

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
        'status': 'str',
        'processing': 'int',
        'succeed': 'int',
        'failed': 'int',
        'total': 'int',
        'create_time': 'int',
        'file_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'task_type': 'task_type',
        'status': 'status',
        'processing': 'processing',
        'succeed': 'succeed',
        'failed': 'failed',
        'total': 'total',
        'create_time': 'create_time',
        'file_type': 'file_type'
    }

    def __init__(self, id=None, task_type=None, status=None, processing=None, succeed=None, failed=None, total=None, create_time=None, file_type=None):
        """TasksObject

        The model defined in huaweicloud sdk

        :param id: 任务id。
        :type id: str
        :param task_type: 任务的类型， 其值可以为refresh或preheating。
        :type task_type: str
        :param status: 刷新结果。task_done表示刷新成功  ，task_inprocess表示刷新中。
        :type status: str
        :param processing: 处理中的url个数。
        :type processing: int
        :param succeed: 成功处理的url个数。
        :type succeed: int
        :param failed: 处理失败的url个数。
        :type failed: int
        :param total: url总数。
        :type total: int
        :param create_time: 任务的创建时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。
        :type create_time: int
        :param file_type: 默认是文件file。file：文件,directory：目录。
        :type file_type: str
        """
        
        

        self._id = None
        self._task_type = None
        self._status = None
        self._processing = None
        self._succeed = None
        self._failed = None
        self._total = None
        self._create_time = None
        self._file_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if task_type is not None:
            self.task_type = task_type
        if status is not None:
            self.status = status
        if processing is not None:
            self.processing = processing
        if succeed is not None:
            self.succeed = succeed
        if failed is not None:
            self.failed = failed
        if total is not None:
            self.total = total
        if create_time is not None:
            self.create_time = create_time
        if file_type is not None:
            self.file_type = file_type

    @property
    def id(self):
        """Gets the id of this TasksObject.

        任务id。

        :return: The id of this TasksObject.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TasksObject.

        任务id。

        :param id: The id of this TasksObject.
        :type id: str
        """
        self._id = id

    @property
    def task_type(self):
        """Gets the task_type of this TasksObject.

        任务的类型， 其值可以为refresh或preheating。

        :return: The task_type of this TasksObject.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this TasksObject.

        任务的类型， 其值可以为refresh或preheating。

        :param task_type: The task_type of this TasksObject.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def status(self):
        """Gets the status of this TasksObject.

        刷新结果。task_done表示刷新成功  ，task_inprocess表示刷新中。

        :return: The status of this TasksObject.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TasksObject.

        刷新结果。task_done表示刷新成功  ，task_inprocess表示刷新中。

        :param status: The status of this TasksObject.
        :type status: str
        """
        self._status = status

    @property
    def processing(self):
        """Gets the processing of this TasksObject.

        处理中的url个数。

        :return: The processing of this TasksObject.
        :rtype: int
        """
        return self._processing

    @processing.setter
    def processing(self, processing):
        """Sets the processing of this TasksObject.

        处理中的url个数。

        :param processing: The processing of this TasksObject.
        :type processing: int
        """
        self._processing = processing

    @property
    def succeed(self):
        """Gets the succeed of this TasksObject.

        成功处理的url个数。

        :return: The succeed of this TasksObject.
        :rtype: int
        """
        return self._succeed

    @succeed.setter
    def succeed(self, succeed):
        """Sets the succeed of this TasksObject.

        成功处理的url个数。

        :param succeed: The succeed of this TasksObject.
        :type succeed: int
        """
        self._succeed = succeed

    @property
    def failed(self):
        """Gets the failed of this TasksObject.

        处理失败的url个数。

        :return: The failed of this TasksObject.
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this TasksObject.

        处理失败的url个数。

        :param failed: The failed of this TasksObject.
        :type failed: int
        """
        self._failed = failed

    @property
    def total(self):
        """Gets the total of this TasksObject.

        url总数。

        :return: The total of this TasksObject.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this TasksObject.

        url总数。

        :param total: The total of this TasksObject.
        :type total: int
        """
        self._total = total

    @property
    def create_time(self):
        """Gets the create_time of this TasksObject.

        任务的创建时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。

        :return: The create_time of this TasksObject.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this TasksObject.

        任务的创建时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。

        :param create_time: The create_time of this TasksObject.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def file_type(self):
        """Gets the file_type of this TasksObject.

        默认是文件file。file：文件,directory：目录。

        :return: The file_type of this TasksObject.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this TasksObject.

        默认是文件file。file：文件,directory：目录。

        :param file_type: The file_type of this TasksObject.
        :type file_type: str
        """
        self._file_type = file_type

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
        if not isinstance(other, TasksObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
