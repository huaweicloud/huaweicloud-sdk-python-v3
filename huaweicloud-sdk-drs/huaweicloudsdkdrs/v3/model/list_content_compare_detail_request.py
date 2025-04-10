# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListContentCompareDetailRequest:

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
        'compare_job_id': 'str',
        'target_db_name': 'str',
        'db_name': 'str',
        'type': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'job_id': 'job_id',
        'compare_job_id': 'compare_job_id',
        'target_db_name': 'target_db_name',
        'db_name': 'db_name',
        'type': 'type',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, x_language=None, job_id=None, compare_job_id=None, target_db_name=None, db_name=None, type=None, limit=None, offset=None):
        r"""ListContentCompareDetailRequest

        The model defined in huaweicloud sdk

        :param x_language: 请求语言类型。
        :type x_language: str
        :param job_id: 任务ID。
        :type job_id: str
        :param compare_job_id: 对比任务ID。
        :type compare_job_id: str
        :param target_db_name: 目标库名称。
        :type target_db_name: str
        :param db_name: 源库名称。
        :type db_name: str
        :param type: 类型。 compare：对比 unCompare：无法对比
        :type type: str
        :param limit: 每页显示的条目数量，最大值1000。
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0。
        :type offset: int
        """
        
        

        self._x_language = None
        self._job_id = None
        self._compare_job_id = None
        self._target_db_name = None
        self._db_name = None
        self._type = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.job_id = job_id
        self.compare_job_id = compare_job_id
        if target_db_name is not None:
            self.target_db_name = target_db_name
        if db_name is not None:
            self.db_name = db_name
        if type is not None:
            self.type = type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def x_language(self):
        r"""Gets the x_language of this ListContentCompareDetailRequest.

        请求语言类型。

        :return: The x_language of this ListContentCompareDetailRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListContentCompareDetailRequest.

        请求语言类型。

        :param x_language: The x_language of this ListContentCompareDetailRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def job_id(self):
        r"""Gets the job_id of this ListContentCompareDetailRequest.

        任务ID。

        :return: The job_id of this ListContentCompareDetailRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ListContentCompareDetailRequest.

        任务ID。

        :param job_id: The job_id of this ListContentCompareDetailRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def compare_job_id(self):
        r"""Gets the compare_job_id of this ListContentCompareDetailRequest.

        对比任务ID。

        :return: The compare_job_id of this ListContentCompareDetailRequest.
        :rtype: str
        """
        return self._compare_job_id

    @compare_job_id.setter
    def compare_job_id(self, compare_job_id):
        r"""Sets the compare_job_id of this ListContentCompareDetailRequest.

        对比任务ID。

        :param compare_job_id: The compare_job_id of this ListContentCompareDetailRequest.
        :type compare_job_id: str
        """
        self._compare_job_id = compare_job_id

    @property
    def target_db_name(self):
        r"""Gets the target_db_name of this ListContentCompareDetailRequest.

        目标库名称。

        :return: The target_db_name of this ListContentCompareDetailRequest.
        :rtype: str
        """
        return self._target_db_name

    @target_db_name.setter
    def target_db_name(self, target_db_name):
        r"""Sets the target_db_name of this ListContentCompareDetailRequest.

        目标库名称。

        :param target_db_name: The target_db_name of this ListContentCompareDetailRequest.
        :type target_db_name: str
        """
        self._target_db_name = target_db_name

    @property
    def db_name(self):
        r"""Gets the db_name of this ListContentCompareDetailRequest.

        源库名称。

        :return: The db_name of this ListContentCompareDetailRequest.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this ListContentCompareDetailRequest.

        源库名称。

        :param db_name: The db_name of this ListContentCompareDetailRequest.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def type(self):
        r"""Gets the type of this ListContentCompareDetailRequest.

        类型。 compare：对比 unCompare：无法对比

        :return: The type of this ListContentCompareDetailRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListContentCompareDetailRequest.

        类型。 compare：对比 unCompare：无法对比

        :param type: The type of this ListContentCompareDetailRequest.
        :type type: str
        """
        self._type = type

    @property
    def limit(self):
        r"""Gets the limit of this ListContentCompareDetailRequest.

        每页显示的条目数量，最大值1000。

        :return: The limit of this ListContentCompareDetailRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListContentCompareDetailRequest.

        每页显示的条目数量，最大值1000。

        :param limit: The limit of this ListContentCompareDetailRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListContentCompareDetailRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0。

        :return: The offset of this ListContentCompareDetailRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListContentCompareDetailRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0。

        :param offset: The offset of this ListContentCompareDetailRequest.
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
        if not isinstance(other, ListContentCompareDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
