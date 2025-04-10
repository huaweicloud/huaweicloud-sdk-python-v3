# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScheduleTaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'instance_id': 'str',
        'status': 'str',
        'name': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'status': 'status',
        'name': 'name',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, x_language=None, instance_id=None, status=None, name=None, start_time=None, end_time=None, offset=None, limit=None):
        r"""ListScheduleTaskRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言。
        :type x_language: str
        :param instance_id: 实例id。
        :type instance_id: str
        :param status: 任务状态。
        :type status: str
        :param name: 任务名称。
        :type name: str
        :param start_time: 开始时间，格式为yyyy-mm-ddThh:mm:ssZ。
        :type start_time: str
        :param end_time: 结束时间，格式为yyyy-mm-ddThh:mm:ssZ。
        :type end_time: str
        :param offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: int
        :param limit: 查询记录数。默认为100，不能为负数，最小值为1，最大值为100
        :type limit: int
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._status = None
        self._name = None
        self._start_time = None
        self._end_time = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if instance_id is not None:
            self.instance_id = instance_id
        if status is not None:
            self.status = status
        if name is not None:
            self.name = name
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def x_language(self):
        r"""Gets the x_language of this ListScheduleTaskRequest.

        语言。

        :return: The x_language of this ListScheduleTaskRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListScheduleTaskRequest.

        语言。

        :param x_language: The x_language of this ListScheduleTaskRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListScheduleTaskRequest.

        实例id。

        :return: The instance_id of this ListScheduleTaskRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListScheduleTaskRequest.

        实例id。

        :param instance_id: The instance_id of this ListScheduleTaskRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def status(self):
        r"""Gets the status of this ListScheduleTaskRequest.

        任务状态。

        :return: The status of this ListScheduleTaskRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListScheduleTaskRequest.

        任务状态。

        :param status: The status of this ListScheduleTaskRequest.
        :type status: str
        """
        self._status = status

    @property
    def name(self):
        r"""Gets the name of this ListScheduleTaskRequest.

        任务名称。

        :return: The name of this ListScheduleTaskRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListScheduleTaskRequest.

        任务名称。

        :param name: The name of this ListScheduleTaskRequest.
        :type name: str
        """
        self._name = name

    @property
    def start_time(self):
        r"""Gets the start_time of this ListScheduleTaskRequest.

        开始时间，格式为yyyy-mm-ddThh:mm:ssZ。

        :return: The start_time of this ListScheduleTaskRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListScheduleTaskRequest.

        开始时间，格式为yyyy-mm-ddThh:mm:ssZ。

        :param start_time: The start_time of this ListScheduleTaskRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListScheduleTaskRequest.

        结束时间，格式为yyyy-mm-ddThh:mm:ssZ。

        :return: The end_time of this ListScheduleTaskRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListScheduleTaskRequest.

        结束时间，格式为yyyy-mm-ddThh:mm:ssZ。

        :param end_time: The end_time of this ListScheduleTaskRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def offset(self):
        r"""Gets the offset of this ListScheduleTaskRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ListScheduleTaskRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListScheduleTaskRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ListScheduleTaskRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListScheduleTaskRequest.

        查询记录数。默认为100，不能为负数，最小值为1，最大值为100

        :return: The limit of this ListScheduleTaskRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListScheduleTaskRequest.

        查询记录数。默认为100，不能为负数，最小值为1，最大值为100

        :param limit: The limit of this ListScheduleTaskRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListScheduleTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
