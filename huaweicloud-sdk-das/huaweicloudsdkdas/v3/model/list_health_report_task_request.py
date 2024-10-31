# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHealthReportTaskRequest:

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
        'start_at': 'int',
        'end_at': 'int',
        'offset': 'int',
        'limit': 'int',
        'x_language': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'start_at': 'start_at',
        'end_at': 'end_at',
        'offset': 'offset',
        'limit': 'limit',
        'x_language': 'X-Language'
    }

    def __init__(self, instance_id=None, start_at=None, end_at=None, offset=None, limit=None, x_language=None):
        """ListHealthReportTaskRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param start_at: 开始时间（Unix timestamp），单位：毫秒。
        :type start_at: int
        :param end_at: 结束时间（Unix timestamp），单位：毫秒。
        :type end_at: int
        :param offset: 偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: int
        :param limit: 每页记录数，默认为10，最大取值200。
        :type limit: int
        :param x_language: 请求语言类型。
        :type x_language: str
        """
        
        

        self._instance_id = None
        self._start_at = None
        self._end_at = None
        self._offset = None
        self._limit = None
        self._x_language = None
        self.discriminator = None

        self.instance_id = instance_id
        self.start_at = start_at
        self.end_at = end_at
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if x_language is not None:
            self.x_language = x_language

    @property
    def instance_id(self):
        """Gets the instance_id of this ListHealthReportTaskRequest.

        实例ID。

        :return: The instance_id of this ListHealthReportTaskRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListHealthReportTaskRequest.

        实例ID。

        :param instance_id: The instance_id of this ListHealthReportTaskRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def start_at(self):
        """Gets the start_at of this ListHealthReportTaskRequest.

        开始时间（Unix timestamp），单位：毫秒。

        :return: The start_at of this ListHealthReportTaskRequest.
        :rtype: int
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        """Sets the start_at of this ListHealthReportTaskRequest.

        开始时间（Unix timestamp），单位：毫秒。

        :param start_at: The start_at of this ListHealthReportTaskRequest.
        :type start_at: int
        """
        self._start_at = start_at

    @property
    def end_at(self):
        """Gets the end_at of this ListHealthReportTaskRequest.

        结束时间（Unix timestamp），单位：毫秒。

        :return: The end_at of this ListHealthReportTaskRequest.
        :rtype: int
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        """Sets the end_at of this ListHealthReportTaskRequest.

        结束时间（Unix timestamp），单位：毫秒。

        :param end_at: The end_at of this ListHealthReportTaskRequest.
        :type end_at: int
        """
        self._end_at = end_at

    @property
    def offset(self):
        """Gets the offset of this ListHealthReportTaskRequest.

        偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ListHealthReportTaskRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListHealthReportTaskRequest.

        偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ListHealthReportTaskRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListHealthReportTaskRequest.

        每页记录数，默认为10，最大取值200。

        :return: The limit of this ListHealthReportTaskRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListHealthReportTaskRequest.

        每页记录数，默认为10，最大取值200。

        :param limit: The limit of this ListHealthReportTaskRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def x_language(self):
        """Gets the x_language of this ListHealthReportTaskRequest.

        请求语言类型。

        :return: The x_language of this ListHealthReportTaskRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListHealthReportTaskRequest.

        请求语言类型。

        :param x_language: The x_language of this ListHealthReportTaskRequest.
        :type x_language: str
        """
        self._x_language = x_language

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
        if not isinstance(other, ListHealthReportTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
