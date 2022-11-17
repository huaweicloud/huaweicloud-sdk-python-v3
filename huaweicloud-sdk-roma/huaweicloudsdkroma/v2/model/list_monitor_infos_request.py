# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMonitorInfosRequest:

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
        'offset': 'int',
        'limit': 'int',
        'task_name': 'str',
        'execute_status': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit',
        'task_name': 'task_name',
        'execute_status': 'execute_status'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, task_name=None, execute_status=None):
        """ListMonitorInfosRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于1
        :type offset: int
        :param limit: 每页显示条目数量，最大数量999，超过999后只返回999
        :type limit: int
        :param task_name: 需要搜索的任务名称，支持模糊搜索，大小写敏感，非必填参数，如果为空，搜索所有任务
        :type task_name: str
        :param execute_status: 需要搜索任务的执行状态, 只允许如下枚举值：UNSTARTED-未启动, WAITING-等待执行,RUNNING-执行中, SUCCESS-执行成功, CANCELLED-任务取消, ERROR-执行异常&lt;/br&gt; 非必填参数，如果为空，搜索所有任务
        :type execute_status: str
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._task_name = None
        self._execute_status = None
        self.discriminator = None

        self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if task_name is not None:
            self.task_name = task_name
        if execute_status is not None:
            self.execute_status = execute_status

    @property
    def instance_id(self):
        """Gets the instance_id of this ListMonitorInfosRequest.

        实例ID

        :return: The instance_id of this ListMonitorInfosRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListMonitorInfosRequest.

        实例ID

        :param instance_id: The instance_id of this ListMonitorInfosRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        """Gets the offset of this ListMonitorInfosRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于1

        :return: The offset of this ListMonitorInfosRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListMonitorInfosRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于1

        :param offset: The offset of this ListMonitorInfosRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListMonitorInfosRequest.

        每页显示条目数量，最大数量999，超过999后只返回999

        :return: The limit of this ListMonitorInfosRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListMonitorInfosRequest.

        每页显示条目数量，最大数量999，超过999后只返回999

        :param limit: The limit of this ListMonitorInfosRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def task_name(self):
        """Gets the task_name of this ListMonitorInfosRequest.

        需要搜索的任务名称，支持模糊搜索，大小写敏感，非必填参数，如果为空，搜索所有任务

        :return: The task_name of this ListMonitorInfosRequest.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this ListMonitorInfosRequest.

        需要搜索的任务名称，支持模糊搜索，大小写敏感，非必填参数，如果为空，搜索所有任务

        :param task_name: The task_name of this ListMonitorInfosRequest.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def execute_status(self):
        """Gets the execute_status of this ListMonitorInfosRequest.

        需要搜索任务的执行状态, 只允许如下枚举值：UNSTARTED-未启动, WAITING-等待执行,RUNNING-执行中, SUCCESS-执行成功, CANCELLED-任务取消, ERROR-执行异常</br> 非必填参数，如果为空，搜索所有任务

        :return: The execute_status of this ListMonitorInfosRequest.
        :rtype: str
        """
        return self._execute_status

    @execute_status.setter
    def execute_status(self, execute_status):
        """Sets the execute_status of this ListMonitorInfosRequest.

        需要搜索任务的执行状态, 只允许如下枚举值：UNSTARTED-未启动, WAITING-等待执行,RUNNING-执行中, SUCCESS-执行成功, CANCELLED-任务取消, ERROR-执行异常</br> 非必填参数，如果为空，搜索所有任务

        :param execute_status: The execute_status of this ListMonitorInfosRequest.
        :type execute_status: str
        """
        self._execute_status = execute_status

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
        if not isinstance(other, ListMonitorInfosRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
