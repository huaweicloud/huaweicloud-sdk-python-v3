# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OneHpcCacheTaskInfoResp:

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
        'type': 'str',
        'status': 'str',
        'src_target': 'str',
        'src_prefix': 'str',
        'dest_target': 'str',
        'dest_prefix': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'message': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'type': 'type',
        'status': 'status',
        'src_target': 'src_target',
        'src_prefix': 'src_prefix',
        'dest_target': 'dest_target',
        'dest_prefix': 'dest_prefix',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'message': 'message'
    }

    def __init__(self, task_id=None, type=None, status=None, src_target=None, src_prefix=None, dest_target=None, dest_prefix=None, start_time=None, end_time=None, message=None):
        r"""OneHpcCacheTaskInfoResp

        The model defined in huaweicloud sdk

        :param task_id: 任务ID
        :type task_id: str
        :param type: 任务类型
        :type type: str
        :param status: 任务状态
        :type status: str
        :param src_target: 联动目录名称
        :type src_target: str
        :param src_prefix: 导入导出任务的源端路径前缀
        :type src_prefix: str
        :param dest_target: 和src_target保持一致
        :type dest_target: str
        :param dest_prefix: 和src_prefix保持一致
        :type dest_prefix: str
        :param start_time: 任务开始时间
        :type start_time: str
        :param end_time: 任务结束时间
        :type end_time: str
        :param message: 任务执行结果信息
        :type message: str
        """
        
        

        self._task_id = None
        self._type = None
        self._status = None
        self._src_target = None
        self._src_prefix = None
        self._dest_target = None
        self._dest_prefix = None
        self._start_time = None
        self._end_time = None
        self._message = None
        self.discriminator = None

        self.task_id = task_id
        self.type = type
        self.status = status
        self.src_target = src_target
        self.src_prefix = src_prefix
        self.dest_target = dest_target
        self.dest_prefix = dest_prefix
        self.start_time = start_time
        self.end_time = end_time
        self.message = message

    @property
    def task_id(self):
        r"""Gets the task_id of this OneHpcCacheTaskInfoResp.

        任务ID

        :return: The task_id of this OneHpcCacheTaskInfoResp.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this OneHpcCacheTaskInfoResp.

        任务ID

        :param task_id: The task_id of this OneHpcCacheTaskInfoResp.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def type(self):
        r"""Gets the type of this OneHpcCacheTaskInfoResp.

        任务类型

        :return: The type of this OneHpcCacheTaskInfoResp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this OneHpcCacheTaskInfoResp.

        任务类型

        :param type: The type of this OneHpcCacheTaskInfoResp.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this OneHpcCacheTaskInfoResp.

        任务状态

        :return: The status of this OneHpcCacheTaskInfoResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this OneHpcCacheTaskInfoResp.

        任务状态

        :param status: The status of this OneHpcCacheTaskInfoResp.
        :type status: str
        """
        self._status = status

    @property
    def src_target(self):
        r"""Gets the src_target of this OneHpcCacheTaskInfoResp.

        联动目录名称

        :return: The src_target of this OneHpcCacheTaskInfoResp.
        :rtype: str
        """
        return self._src_target

    @src_target.setter
    def src_target(self, src_target):
        r"""Sets the src_target of this OneHpcCacheTaskInfoResp.

        联动目录名称

        :param src_target: The src_target of this OneHpcCacheTaskInfoResp.
        :type src_target: str
        """
        self._src_target = src_target

    @property
    def src_prefix(self):
        r"""Gets the src_prefix of this OneHpcCacheTaskInfoResp.

        导入导出任务的源端路径前缀

        :return: The src_prefix of this OneHpcCacheTaskInfoResp.
        :rtype: str
        """
        return self._src_prefix

    @src_prefix.setter
    def src_prefix(self, src_prefix):
        r"""Sets the src_prefix of this OneHpcCacheTaskInfoResp.

        导入导出任务的源端路径前缀

        :param src_prefix: The src_prefix of this OneHpcCacheTaskInfoResp.
        :type src_prefix: str
        """
        self._src_prefix = src_prefix

    @property
    def dest_target(self):
        r"""Gets the dest_target of this OneHpcCacheTaskInfoResp.

        和src_target保持一致

        :return: The dest_target of this OneHpcCacheTaskInfoResp.
        :rtype: str
        """
        return self._dest_target

    @dest_target.setter
    def dest_target(self, dest_target):
        r"""Sets the dest_target of this OneHpcCacheTaskInfoResp.

        和src_target保持一致

        :param dest_target: The dest_target of this OneHpcCacheTaskInfoResp.
        :type dest_target: str
        """
        self._dest_target = dest_target

    @property
    def dest_prefix(self):
        r"""Gets the dest_prefix of this OneHpcCacheTaskInfoResp.

        和src_prefix保持一致

        :return: The dest_prefix of this OneHpcCacheTaskInfoResp.
        :rtype: str
        """
        return self._dest_prefix

    @dest_prefix.setter
    def dest_prefix(self, dest_prefix):
        r"""Sets the dest_prefix of this OneHpcCacheTaskInfoResp.

        和src_prefix保持一致

        :param dest_prefix: The dest_prefix of this OneHpcCacheTaskInfoResp.
        :type dest_prefix: str
        """
        self._dest_prefix = dest_prefix

    @property
    def start_time(self):
        r"""Gets the start_time of this OneHpcCacheTaskInfoResp.

        任务开始时间

        :return: The start_time of this OneHpcCacheTaskInfoResp.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this OneHpcCacheTaskInfoResp.

        任务开始时间

        :param start_time: The start_time of this OneHpcCacheTaskInfoResp.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this OneHpcCacheTaskInfoResp.

        任务结束时间

        :return: The end_time of this OneHpcCacheTaskInfoResp.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this OneHpcCacheTaskInfoResp.

        任务结束时间

        :param end_time: The end_time of this OneHpcCacheTaskInfoResp.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def message(self):
        r"""Gets the message of this OneHpcCacheTaskInfoResp.

        任务执行结果信息

        :return: The message of this OneHpcCacheTaskInfoResp.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this OneHpcCacheTaskInfoResp.

        任务执行结果信息

        :param message: The message of this OneHpcCacheTaskInfoResp.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, OneHpcCacheTaskInfoResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
