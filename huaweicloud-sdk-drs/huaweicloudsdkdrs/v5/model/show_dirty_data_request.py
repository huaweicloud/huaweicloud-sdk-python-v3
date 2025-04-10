# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDirtyDataRequest:

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
        'job_id': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'job_id': 'job_id',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, x_language=None, job_id=None, begin_time=None, end_time=None, offset=None, limit=None):
        r"""ShowDirtyDataRequest

        The model defined in huaweicloud sdk

        :param x_language: 请求语言类型。
        :type x_language: str
        :param job_id: 任务ID。
        :type job_id: str
        :param begin_time: 开始时间，UTC时间，例如：2020-09-01T18:50:20Z
        :type begin_time: str
        :param end_time: 结束时间，UTC时间，例如：2020-09-01T19:50:20Z
        :type end_time: str
        :param offset: 偏移量，表示从此偏移量开始查询， offset 大于等于 0。默认为0
        :type offset: int
        :param limit: 每页显示的条目数量。默认为10，取值范围【1-1000】
        :type limit: int
        """
        
        

        self._x_language = None
        self._job_id = None
        self._begin_time = None
        self._end_time = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.job_id = job_id
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowDirtyDataRequest.

        请求语言类型。

        :return: The x_language of this ShowDirtyDataRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowDirtyDataRequest.

        请求语言类型。

        :param x_language: The x_language of this ShowDirtyDataRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowDirtyDataRequest.

        任务ID。

        :return: The job_id of this ShowDirtyDataRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowDirtyDataRequest.

        任务ID。

        :param job_id: The job_id of this ShowDirtyDataRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ShowDirtyDataRequest.

        开始时间，UTC时间，例如：2020-09-01T18:50:20Z

        :return: The begin_time of this ShowDirtyDataRequest.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ShowDirtyDataRequest.

        开始时间，UTC时间，例如：2020-09-01T18:50:20Z

        :param begin_time: The begin_time of this ShowDirtyDataRequest.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowDirtyDataRequest.

        结束时间，UTC时间，例如：2020-09-01T19:50:20Z

        :return: The end_time of this ShowDirtyDataRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowDirtyDataRequest.

        结束时间，UTC时间，例如：2020-09-01T19:50:20Z

        :param end_time: The end_time of this ShowDirtyDataRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def offset(self):
        r"""Gets the offset of this ShowDirtyDataRequest.

        偏移量，表示从此偏移量开始查询， offset 大于等于 0。默认为0

        :return: The offset of this ShowDirtyDataRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowDirtyDataRequest.

        偏移量，表示从此偏移量开始查询， offset 大于等于 0。默认为0

        :param offset: The offset of this ShowDirtyDataRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowDirtyDataRequest.

        每页显示的条目数量。默认为10，取值范围【1-1000】

        :return: The limit of this ShowDirtyDataRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowDirtyDataRequest.

        每页显示的条目数量。默认为10，取值范围【1-1000】

        :param limit: The limit of this ShowDirtyDataRequest.
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
        if not isinstance(other, ShowDirtyDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
