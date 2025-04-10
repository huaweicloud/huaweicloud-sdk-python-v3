# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubTask:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'name': 'str',
        'progress': 'int',
        'start_date': 'int',
        'end_date': 'int',
        'migrate_speed': 'float',
        'user_op': 'str',
        'process_trace': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'progress': 'progress',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'migrate_speed': 'migrate_speed',
        'user_op': 'user_op',
        'process_trace': 'process_trace'
    }

    def __init__(self, id=None, name=None, progress=None, start_date=None, end_date=None, migrate_speed=None, user_op=None, process_trace=None):
        r"""SubTask

        The model defined in huaweicloud sdk

        :param id: 子任务ID
        :type id: int
        :param name: 子任务名称
        :type name: str
        :param progress: 子任务的进度，取值为0-100之间的整数
        :type progress: int
        :param start_date: 子任务开始时间
        :type start_date: int
        :param end_date: 子任务结束时间（如果子任务还没有结束，则为空）
        :type end_date: int
        :param migrate_speed: 迁移速率，Mbit/s
        :type migrate_speed: float
        :param user_op: 触发子任务的用户操作名称
        :type user_op: str
        :param process_trace: 迁移或同步时，具体的迁移详情
        :type process_trace: str
        """
        
        

        self._id = None
        self._name = None
        self._progress = None
        self._start_date = None
        self._end_date = None
        self._migrate_speed = None
        self._user_op = None
        self._process_trace = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        self.progress = progress
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if migrate_speed is not None:
            self.migrate_speed = migrate_speed
        if user_op is not None:
            self.user_op = user_op
        if process_trace is not None:
            self.process_trace = process_trace

    @property
    def id(self):
        r"""Gets the id of this SubTask.

        子任务ID

        :return: The id of this SubTask.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SubTask.

        子任务ID

        :param id: The id of this SubTask.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this SubTask.

        子任务名称

        :return: The name of this SubTask.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SubTask.

        子任务名称

        :param name: The name of this SubTask.
        :type name: str
        """
        self._name = name

    @property
    def progress(self):
        r"""Gets the progress of this SubTask.

        子任务的进度，取值为0-100之间的整数

        :return: The progress of this SubTask.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this SubTask.

        子任务的进度，取值为0-100之间的整数

        :param progress: The progress of this SubTask.
        :type progress: int
        """
        self._progress = progress

    @property
    def start_date(self):
        r"""Gets the start_date of this SubTask.

        子任务开始时间

        :return: The start_date of this SubTask.
        :rtype: int
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        r"""Sets the start_date of this SubTask.

        子任务开始时间

        :param start_date: The start_date of this SubTask.
        :type start_date: int
        """
        self._start_date = start_date

    @property
    def end_date(self):
        r"""Gets the end_date of this SubTask.

        子任务结束时间（如果子任务还没有结束，则为空）

        :return: The end_date of this SubTask.
        :rtype: int
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        r"""Sets the end_date of this SubTask.

        子任务结束时间（如果子任务还没有结束，则为空）

        :param end_date: The end_date of this SubTask.
        :type end_date: int
        """
        self._end_date = end_date

    @property
    def migrate_speed(self):
        r"""Gets the migrate_speed of this SubTask.

        迁移速率，Mbit/s

        :return: The migrate_speed of this SubTask.
        :rtype: float
        """
        return self._migrate_speed

    @migrate_speed.setter
    def migrate_speed(self, migrate_speed):
        r"""Sets the migrate_speed of this SubTask.

        迁移速率，Mbit/s

        :param migrate_speed: The migrate_speed of this SubTask.
        :type migrate_speed: float
        """
        self._migrate_speed = migrate_speed

    @property
    def user_op(self):
        r"""Gets the user_op of this SubTask.

        触发子任务的用户操作名称

        :return: The user_op of this SubTask.
        :rtype: str
        """
        return self._user_op

    @user_op.setter
    def user_op(self, user_op):
        r"""Sets the user_op of this SubTask.

        触发子任务的用户操作名称

        :param user_op: The user_op of this SubTask.
        :type user_op: str
        """
        self._user_op = user_op

    @property
    def process_trace(self):
        r"""Gets the process_trace of this SubTask.

        迁移或同步时，具体的迁移详情

        :return: The process_trace of this SubTask.
        :rtype: str
        """
        return self._process_trace

    @process_trace.setter
    def process_trace(self, process_trace):
        r"""Sets the process_trace of this SubTask.

        迁移或同步时，具体的迁移详情

        :param process_trace: The process_trace of this SubTask.
        :type process_trace: str
        """
        self._process_trace = process_trace

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
        if not isinstance(other, SubTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
