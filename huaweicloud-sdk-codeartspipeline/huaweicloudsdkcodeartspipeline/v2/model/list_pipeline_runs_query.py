# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPipelineRunsQuery:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'list[str]',
        'start_time': 'str',
        'end_time': 'str',
        'offset': 'int',
        'limit': 'int',
        'sort_key': 'str',
        'sort_dir': 'str'
    }

    attribute_map = {
        'status': 'status',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'offset': 'offset',
        'limit': 'limit',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, status=None, start_time=None, end_time=None, offset=None, limit=None, sort_key=None, sort_dir=None):
        r"""ListPipelineRunsQuery

        The model defined in huaweicloud sdk

        :param status: 状态
        :type status: list[str]
        :param start_time: 开始时间
        :type start_time: str
        :param end_time: 结束时间
        :type end_time: str
        :param offset: 起始偏移
        :type offset: int
        :param limit: 查询大小
        :type limit: int
        :param sort_key: 排序字段名称
        :type sort_key: str
        :param sort_dir: 排序规则
        :type sort_dir: str
        """
        
        

        self._status = None
        self._start_time = None
        self._end_time = None
        self._offset = None
        self._limit = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir

    @property
    def status(self):
        r"""Gets the status of this ListPipelineRunsQuery.

        状态

        :return: The status of this ListPipelineRunsQuery.
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListPipelineRunsQuery.

        状态

        :param status: The status of this ListPipelineRunsQuery.
        :type status: list[str]
        """
        self._status = status

    @property
    def start_time(self):
        r"""Gets the start_time of this ListPipelineRunsQuery.

        开始时间

        :return: The start_time of this ListPipelineRunsQuery.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListPipelineRunsQuery.

        开始时间

        :param start_time: The start_time of this ListPipelineRunsQuery.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListPipelineRunsQuery.

        结束时间

        :return: The end_time of this ListPipelineRunsQuery.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListPipelineRunsQuery.

        结束时间

        :param end_time: The end_time of this ListPipelineRunsQuery.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def offset(self):
        r"""Gets the offset of this ListPipelineRunsQuery.

        起始偏移

        :return: The offset of this ListPipelineRunsQuery.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListPipelineRunsQuery.

        起始偏移

        :param offset: The offset of this ListPipelineRunsQuery.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListPipelineRunsQuery.

        查询大小

        :return: The limit of this ListPipelineRunsQuery.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPipelineRunsQuery.

        查询大小

        :param limit: The limit of this ListPipelineRunsQuery.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListPipelineRunsQuery.

        排序字段名称

        :return: The sort_key of this ListPipelineRunsQuery.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListPipelineRunsQuery.

        排序字段名称

        :param sort_key: The sort_key of this ListPipelineRunsQuery.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListPipelineRunsQuery.

        排序规则

        :return: The sort_dir of this ListPipelineRunsQuery.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListPipelineRunsQuery.

        排序规则

        :param sort_dir: The sort_dir of this ListPipelineRunsQuery.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

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
        if not isinstance(other, ListPipelineRunsQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
