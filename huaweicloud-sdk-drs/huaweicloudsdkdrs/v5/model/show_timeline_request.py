# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTimelineRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'x_language': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'job_id': 'job_id',
        'x_language': 'X-Language',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, job_id=None, x_language=None, limit=None, offset=None):
        r"""ShowTimelineRequest

        The model defined in huaweicloud sdk

        :param job_id: 任务ID。
        :type job_id: str
        :param x_language: 请求语言类型。
        :type x_language: str
        :param limit: 每页显示的条目数量。默认为10，取值范围【1-1000】
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询， offset 大于等于 0。默认为0
        :type offset: int
        """
        
        

        self._job_id = None
        self._x_language = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.job_id = job_id
        self.x_language = x_language
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowTimelineRequest.

        任务ID。

        :return: The job_id of this ShowTimelineRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowTimelineRequest.

        任务ID。

        :param job_id: The job_id of this ShowTimelineRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowTimelineRequest.

        请求语言类型。

        :return: The x_language of this ShowTimelineRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowTimelineRequest.

        请求语言类型。

        :param x_language: The x_language of this ShowTimelineRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def limit(self):
        r"""Gets the limit of this ShowTimelineRequest.

        每页显示的条目数量。默认为10，取值范围【1-1000】

        :return: The limit of this ShowTimelineRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowTimelineRequest.

        每页显示的条目数量。默认为10，取值范围【1-1000】

        :param limit: The limit of this ShowTimelineRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowTimelineRequest.

        偏移量，表示从此偏移量开始查询， offset 大于等于 0。默认为0

        :return: The offset of this ShowTimelineRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowTimelineRequest.

        偏移量，表示从此偏移量开始查询， offset 大于等于 0。默认为0

        :param offset: The offset of this ShowTimelineRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ShowTimelineRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
