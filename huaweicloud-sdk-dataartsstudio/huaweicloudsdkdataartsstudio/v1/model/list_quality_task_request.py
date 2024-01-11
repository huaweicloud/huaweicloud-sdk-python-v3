# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListQualityTaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category_id': 'int',
        'name': 'str',
        'schedule_status': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'creator': 'str',
        'limit': 'int',
        'offset': 'int',
        'workspace': 'str'
    }

    attribute_map = {
        'category_id': 'category_id',
        'name': 'name',
        'schedule_status': 'schedule_status',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'creator': 'creator',
        'limit': 'limit',
        'offset': 'offset',
        'workspace': 'workspace'
    }

    def __init__(self, category_id=None, name=None, schedule_status=None, start_time=None, end_time=None, creator=None, limit=None, offset=None, workspace=None):
        """ListQualityTaskRequest

        The model defined in huaweicloud sdk

        :param category_id: 目录ID
        :type category_id: int
        :param name: name
        :type name: str
        :param schedule_status: 调度状态 UNKNOWN:未知,NOT_START:未启动,SCHEDULING:调度中,FINISH_SUCCESS:正常结束,KILL:手动停止,RUNNING_EXCEPTION:运行失败
        :type schedule_status: str
        :param start_time: 最近运行时间查询区间的开始时间,13位时间戳(精确到毫秒)
        :type start_time: int
        :param end_time: 最近运行时间查询区间的结束时间,13位时间戳(精确到毫秒)
        :type end_time: int
        :param creator: 创建人
        :type creator: str
        :param limit: 分页条数,最大值为100
        :type limit: int
        :param offset: 分页偏移量,最小值0
        :type offset: int
        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        """
        
        

        self._category_id = None
        self._name = None
        self._schedule_status = None
        self._start_time = None
        self._end_time = None
        self._creator = None
        self._limit = None
        self._offset = None
        self._workspace = None
        self.discriminator = None

        if category_id is not None:
            self.category_id = category_id
        if name is not None:
            self.name = name
        if schedule_status is not None:
            self.schedule_status = schedule_status
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if creator is not None:
            self.creator = creator
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        self.workspace = workspace

    @property
    def category_id(self):
        """Gets the category_id of this ListQualityTaskRequest.

        目录ID

        :return: The category_id of this ListQualityTaskRequest.
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this ListQualityTaskRequest.

        目录ID

        :param category_id: The category_id of this ListQualityTaskRequest.
        :type category_id: int
        """
        self._category_id = category_id

    @property
    def name(self):
        """Gets the name of this ListQualityTaskRequest.

        name

        :return: The name of this ListQualityTaskRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListQualityTaskRequest.

        name

        :param name: The name of this ListQualityTaskRequest.
        :type name: str
        """
        self._name = name

    @property
    def schedule_status(self):
        """Gets the schedule_status of this ListQualityTaskRequest.

        调度状态 UNKNOWN:未知,NOT_START:未启动,SCHEDULING:调度中,FINISH_SUCCESS:正常结束,KILL:手动停止,RUNNING_EXCEPTION:运行失败

        :return: The schedule_status of this ListQualityTaskRequest.
        :rtype: str
        """
        return self._schedule_status

    @schedule_status.setter
    def schedule_status(self, schedule_status):
        """Sets the schedule_status of this ListQualityTaskRequest.

        调度状态 UNKNOWN:未知,NOT_START:未启动,SCHEDULING:调度中,FINISH_SUCCESS:正常结束,KILL:手动停止,RUNNING_EXCEPTION:运行失败

        :param schedule_status: The schedule_status of this ListQualityTaskRequest.
        :type schedule_status: str
        """
        self._schedule_status = schedule_status

    @property
    def start_time(self):
        """Gets the start_time of this ListQualityTaskRequest.

        最近运行时间查询区间的开始时间,13位时间戳(精确到毫秒)

        :return: The start_time of this ListQualityTaskRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListQualityTaskRequest.

        最近运行时间查询区间的开始时间,13位时间戳(精确到毫秒)

        :param start_time: The start_time of this ListQualityTaskRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListQualityTaskRequest.

        最近运行时间查询区间的结束时间,13位时间戳(精确到毫秒)

        :return: The end_time of this ListQualityTaskRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListQualityTaskRequest.

        最近运行时间查询区间的结束时间,13位时间戳(精确到毫秒)

        :param end_time: The end_time of this ListQualityTaskRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def creator(self):
        """Gets the creator of this ListQualityTaskRequest.

        创建人

        :return: The creator of this ListQualityTaskRequest.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this ListQualityTaskRequest.

        创建人

        :param creator: The creator of this ListQualityTaskRequest.
        :type creator: str
        """
        self._creator = creator

    @property
    def limit(self):
        """Gets the limit of this ListQualityTaskRequest.

        分页条数,最大值为100

        :return: The limit of this ListQualityTaskRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListQualityTaskRequest.

        分页条数,最大值为100

        :param limit: The limit of this ListQualityTaskRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListQualityTaskRequest.

        分页偏移量,最小值0

        :return: The offset of this ListQualityTaskRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListQualityTaskRequest.

        分页偏移量,最小值0

        :param offset: The offset of this ListQualityTaskRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def workspace(self):
        """Gets the workspace of this ListQualityTaskRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ListQualityTaskRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ListQualityTaskRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ListQualityTaskRequest.
        :type workspace: str
        """
        self._workspace = workspace

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
        if not isinstance(other, ListQualityTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
