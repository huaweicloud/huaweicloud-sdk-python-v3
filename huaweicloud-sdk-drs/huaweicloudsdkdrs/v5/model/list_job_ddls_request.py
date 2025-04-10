# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJobDdlsRequest:

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
        'offset': 'int',
        'limit': 'int',
        'start_seq_no': 'int',
        'end_seq_no': 'int',
        'status': 'int',
        'job_id': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'offset': 'offset',
        'limit': 'limit',
        'start_seq_no': 'start_seq_no',
        'end_seq_no': 'end_seq_no',
        'status': 'status',
        'job_id': 'job_id'
    }

    def __init__(self, x_language=None, offset=None, limit=None, start_seq_no=None, end_seq_no=None, status=None, job_id=None):
        r"""ListJobDdlsRequest

        The model defined in huaweicloud sdk

        :param x_language: 请求语言类型。
        :type x_language: str
        :param offset: 偏移量，默认值为0，表示查询该偏移量后面的记录。
        :type offset: int
        :param limit: 查询返回记录的数量限制.默认值为10。
        :type limit: int
        :param start_seq_no: DDL序列起始值。
        :type start_seq_no: int
        :param end_seq_no: DDL序列结束值。
        :type end_seq_no: int
        :param status: DDL状态，0为无告警，1为告警中。
        :type status: int
        :param job_id: 任务ID。
        :type job_id: str
        """
        
        

        self._x_language = None
        self._offset = None
        self._limit = None
        self._start_seq_no = None
        self._end_seq_no = None
        self._status = None
        self._job_id = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if start_seq_no is not None:
            self.start_seq_no = start_seq_no
        if end_seq_no is not None:
            self.end_seq_no = end_seq_no
        if status is not None:
            self.status = status
        self.job_id = job_id

    @property
    def x_language(self):
        r"""Gets the x_language of this ListJobDdlsRequest.

        请求语言类型。

        :return: The x_language of this ListJobDdlsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListJobDdlsRequest.

        请求语言类型。

        :param x_language: The x_language of this ListJobDdlsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def offset(self):
        r"""Gets the offset of this ListJobDdlsRequest.

        偏移量，默认值为0，表示查询该偏移量后面的记录。

        :return: The offset of this ListJobDdlsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListJobDdlsRequest.

        偏移量，默认值为0，表示查询该偏移量后面的记录。

        :param offset: The offset of this ListJobDdlsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListJobDdlsRequest.

        查询返回记录的数量限制.默认值为10。

        :return: The limit of this ListJobDdlsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListJobDdlsRequest.

        查询返回记录的数量限制.默认值为10。

        :param limit: The limit of this ListJobDdlsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def start_seq_no(self):
        r"""Gets the start_seq_no of this ListJobDdlsRequest.

        DDL序列起始值。

        :return: The start_seq_no of this ListJobDdlsRequest.
        :rtype: int
        """
        return self._start_seq_no

    @start_seq_no.setter
    def start_seq_no(self, start_seq_no):
        r"""Sets the start_seq_no of this ListJobDdlsRequest.

        DDL序列起始值。

        :param start_seq_no: The start_seq_no of this ListJobDdlsRequest.
        :type start_seq_no: int
        """
        self._start_seq_no = start_seq_no

    @property
    def end_seq_no(self):
        r"""Gets the end_seq_no of this ListJobDdlsRequest.

        DDL序列结束值。

        :return: The end_seq_no of this ListJobDdlsRequest.
        :rtype: int
        """
        return self._end_seq_no

    @end_seq_no.setter
    def end_seq_no(self, end_seq_no):
        r"""Sets the end_seq_no of this ListJobDdlsRequest.

        DDL序列结束值。

        :param end_seq_no: The end_seq_no of this ListJobDdlsRequest.
        :type end_seq_no: int
        """
        self._end_seq_no = end_seq_no

    @property
    def status(self):
        r"""Gets the status of this ListJobDdlsRequest.

        DDL状态，0为无告警，1为告警中。

        :return: The status of this ListJobDdlsRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListJobDdlsRequest.

        DDL状态，0为无告警，1为告警中。

        :param status: The status of this ListJobDdlsRequest.
        :type status: int
        """
        self._status = status

    @property
    def job_id(self):
        r"""Gets the job_id of this ListJobDdlsRequest.

        任务ID。

        :return: The job_id of this ListJobDdlsRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ListJobDdlsRequest.

        任务ID。

        :param job_id: The job_id of this ListJobDdlsRequest.
        :type job_id: str
        """
        self._job_id = job_id

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
        if not isinstance(other, ListJobDdlsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
