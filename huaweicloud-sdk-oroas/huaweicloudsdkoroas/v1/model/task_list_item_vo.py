# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskListItemVo:

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
        'status': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'create_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'create_time': 'create_time'
    }

    def __init__(self, id=None, status=None, start_time=None, end_time=None, create_time=None):
        """TaskListItemVo

        The model defined in huaweicloud sdk

        :param id: 任务编号
        :type id: str
        :param status: 状态
        :type status: str
        :param start_time: 开始时间（UTC）
        :type start_time: datetime
        :param end_time: 结束时间（UTC）
        :type end_time: datetime
        :param create_time: 创建时间（UTC）
        :type create_time: datetime
        """
        
        

        self._id = None
        self._status = None
        self._start_time = None
        self._end_time = None
        self._create_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if create_time is not None:
            self.create_time = create_time

    @property
    def id(self):
        """Gets the id of this TaskListItemVo.

        任务编号

        :return: The id of this TaskListItemVo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskListItemVo.

        任务编号

        :param id: The id of this TaskListItemVo.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this TaskListItemVo.

        状态

        :return: The status of this TaskListItemVo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TaskListItemVo.

        状态

        :param status: The status of this TaskListItemVo.
        :type status: str
        """
        self._status = status

    @property
    def start_time(self):
        """Gets the start_time of this TaskListItemVo.

        开始时间（UTC）

        :return: The start_time of this TaskListItemVo.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this TaskListItemVo.

        开始时间（UTC）

        :param start_time: The start_time of this TaskListItemVo.
        :type start_time: datetime
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this TaskListItemVo.

        结束时间（UTC）

        :return: The end_time of this TaskListItemVo.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this TaskListItemVo.

        结束时间（UTC）

        :param end_time: The end_time of this TaskListItemVo.
        :type end_time: datetime
        """
        self._end_time = end_time

    @property
    def create_time(self):
        """Gets the create_time of this TaskListItemVo.

        创建时间（UTC）

        :return: The create_time of this TaskListItemVo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this TaskListItemVo.

        创建时间（UTC）

        :param create_time: The create_time of this TaskListItemVo.
        :type create_time: datetime
        """
        self._create_time = create_time

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
        if not isinstance(other, TaskListItemVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
