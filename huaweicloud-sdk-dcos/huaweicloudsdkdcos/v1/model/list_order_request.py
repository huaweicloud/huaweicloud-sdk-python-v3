# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOrderRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'sub_type': 'str',
        'stage': 'str',
        'status': 'str',
        'applicant': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'key_word': 'str',
        'limit': 'int',
        'offset': 'int',
        'sort_key': 'str',
        'sort_dir': 'str'
    }

    attribute_map = {
        'type': 'type',
        'sub_type': 'sub_type',
        'stage': 'stage',
        'status': 'status',
        'applicant': 'applicant',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'key_word': 'key_word',
        'limit': 'limit',
        'offset': 'offset',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, type=None, sub_type=None, stage=None, status=None, applicant=None, start_time=None, end_time=None, key_word=None, limit=None, offset=None, sort_key=None, sort_dir=None):
        r"""ListOrderRequest

        The model defined in huaweicloud sdk

        :param type: 服务类型
        :type type: str
        :param sub_type: 服务条目
        :type sub_type: str
        :param stage: 阶段
        :type stage: str
        :param status: 状态
        :type status: str
        :param applicant: 申请人
        :type applicant: str
        :param start_time: 时间范围-开始
        :type start_time: str
        :param end_time: 时间范围-结束
        :type end_time: str
        :param key_word: 关键字
        :type key_word: str
        :param limit: 单页大小
        :type limit: int
        :param offset: 横移量
        :type offset: int
        :param sort_key: 排序字段
        :type sort_key: str
        :param sort_dir: 排序方式
        :type sort_dir: str
        """
        
        

        self._type = None
        self._sub_type = None
        self._stage = None
        self._status = None
        self._applicant = None
        self._start_time = None
        self._end_time = None
        self._key_word = None
        self._limit = None
        self._offset = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if sub_type is not None:
            self.sub_type = sub_type
        if stage is not None:
            self.stage = stage
        if status is not None:
            self.status = status
        if applicant is not None:
            self.applicant = applicant
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if key_word is not None:
            self.key_word = key_word
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir

    @property
    def type(self):
        r"""Gets the type of this ListOrderRequest.

        服务类型

        :return: The type of this ListOrderRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListOrderRequest.

        服务类型

        :param type: The type of this ListOrderRequest.
        :type type: str
        """
        self._type = type

    @property
    def sub_type(self):
        r"""Gets the sub_type of this ListOrderRequest.

        服务条目

        :return: The sub_type of this ListOrderRequest.
        :rtype: str
        """
        return self._sub_type

    @sub_type.setter
    def sub_type(self, sub_type):
        r"""Sets the sub_type of this ListOrderRequest.

        服务条目

        :param sub_type: The sub_type of this ListOrderRequest.
        :type sub_type: str
        """
        self._sub_type = sub_type

    @property
    def stage(self):
        r"""Gets the stage of this ListOrderRequest.

        阶段

        :return: The stage of this ListOrderRequest.
        :rtype: str
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        r"""Sets the stage of this ListOrderRequest.

        阶段

        :param stage: The stage of this ListOrderRequest.
        :type stage: str
        """
        self._stage = stage

    @property
    def status(self):
        r"""Gets the status of this ListOrderRequest.

        状态

        :return: The status of this ListOrderRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListOrderRequest.

        状态

        :param status: The status of this ListOrderRequest.
        :type status: str
        """
        self._status = status

    @property
    def applicant(self):
        r"""Gets the applicant of this ListOrderRequest.

        申请人

        :return: The applicant of this ListOrderRequest.
        :rtype: str
        """
        return self._applicant

    @applicant.setter
    def applicant(self, applicant):
        r"""Sets the applicant of this ListOrderRequest.

        申请人

        :param applicant: The applicant of this ListOrderRequest.
        :type applicant: str
        """
        self._applicant = applicant

    @property
    def start_time(self):
        r"""Gets the start_time of this ListOrderRequest.

        时间范围-开始

        :return: The start_time of this ListOrderRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListOrderRequest.

        时间范围-开始

        :param start_time: The start_time of this ListOrderRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListOrderRequest.

        时间范围-结束

        :return: The end_time of this ListOrderRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListOrderRequest.

        时间范围-结束

        :param end_time: The end_time of this ListOrderRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def key_word(self):
        r"""Gets the key_word of this ListOrderRequest.

        关键字

        :return: The key_word of this ListOrderRequest.
        :rtype: str
        """
        return self._key_word

    @key_word.setter
    def key_word(self, key_word):
        r"""Sets the key_word of this ListOrderRequest.

        关键字

        :param key_word: The key_word of this ListOrderRequest.
        :type key_word: str
        """
        self._key_word = key_word

    @property
    def limit(self):
        r"""Gets the limit of this ListOrderRequest.

        单页大小

        :return: The limit of this ListOrderRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListOrderRequest.

        单页大小

        :param limit: The limit of this ListOrderRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListOrderRequest.

        横移量

        :return: The offset of this ListOrderRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListOrderRequest.

        横移量

        :param offset: The offset of this ListOrderRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListOrderRequest.

        排序字段

        :return: The sort_key of this ListOrderRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListOrderRequest.

        排序字段

        :param sort_key: The sort_key of this ListOrderRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListOrderRequest.

        排序方式

        :return: The sort_dir of this ListOrderRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListOrderRequest.

        排序方式

        :param sort_dir: The sort_dir of this ListOrderRequest.
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
        if not isinstance(other, ListOrderRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
