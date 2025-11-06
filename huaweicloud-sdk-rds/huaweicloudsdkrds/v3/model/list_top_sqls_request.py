# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTopSqlsRequest:

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
        'x_language': 'str',
        'sort_key': 'str',
        'limit': 'int',
        'statement': 'str',
        'sort_dir': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'x_language': 'X-Language',
        'sort_key': 'sort_key',
        'limit': 'limit',
        'statement': 'statement',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, instance_id=None, x_language=None, sort_key=None, limit=None, statement=None, sort_dir=None):
        r"""ListTopSqlsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param x_language: 语言。
        :type x_language: str
        :param sort_key: 排序字段: avg_cpu_time:平均CPU耗时 total_cpu_time：总CPU耗时 total_duration_time：总执行时间 avg_duration_time：平均执行时间 total_rows：总行数 avg_rows：平均行数 total_logical_reads：总逻辑读 avg_logical_reads：平均逻辑读
        :type sort_key: str
        :param limit: TOP 数量，最大支持15个。
        :type limit: int
        :param statement: 搜索文本内容。
        :type statement: str
        :param sort_dir: 排序规则： desc： 降序 asc: 升序
        :type sort_dir: str
        """
        
        

        self._instance_id = None
        self._x_language = None
        self._sort_key = None
        self._limit = None
        self._statement = None
        self._sort_dir = None
        self.discriminator = None

        self.instance_id = instance_id
        if x_language is not None:
            self.x_language = x_language
        if sort_key is not None:
            self.sort_key = sort_key
        if limit is not None:
            self.limit = limit
        if statement is not None:
            self.statement = statement
        if sort_dir is not None:
            self.sort_dir = sort_dir

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListTopSqlsRequest.

        实例ID。

        :return: The instance_id of this ListTopSqlsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListTopSqlsRequest.

        实例ID。

        :param instance_id: The instance_id of this ListTopSqlsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def x_language(self):
        r"""Gets the x_language of this ListTopSqlsRequest.

        语言。

        :return: The x_language of this ListTopSqlsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListTopSqlsRequest.

        语言。

        :param x_language: The x_language of this ListTopSqlsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListTopSqlsRequest.

        排序字段: avg_cpu_time:平均CPU耗时 total_cpu_time：总CPU耗时 total_duration_time：总执行时间 avg_duration_time：平均执行时间 total_rows：总行数 avg_rows：平均行数 total_logical_reads：总逻辑读 avg_logical_reads：平均逻辑读

        :return: The sort_key of this ListTopSqlsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListTopSqlsRequest.

        排序字段: avg_cpu_time:平均CPU耗时 total_cpu_time：总CPU耗时 total_duration_time：总执行时间 avg_duration_time：平均执行时间 total_rows：总行数 avg_rows：平均行数 total_logical_reads：总逻辑读 avg_logical_reads：平均逻辑读

        :param sort_key: The sort_key of this ListTopSqlsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def limit(self):
        r"""Gets the limit of this ListTopSqlsRequest.

        TOP 数量，最大支持15个。

        :return: The limit of this ListTopSqlsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTopSqlsRequest.

        TOP 数量，最大支持15个。

        :param limit: The limit of this ListTopSqlsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def statement(self):
        r"""Gets the statement of this ListTopSqlsRequest.

        搜索文本内容。

        :return: The statement of this ListTopSqlsRequest.
        :rtype: str
        """
        return self._statement

    @statement.setter
    def statement(self, statement):
        r"""Sets the statement of this ListTopSqlsRequest.

        搜索文本内容。

        :param statement: The statement of this ListTopSqlsRequest.
        :type statement: str
        """
        self._statement = statement

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListTopSqlsRequest.

        排序规则： desc： 降序 asc: 升序

        :return: The sort_dir of this ListTopSqlsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListTopSqlsRequest.

        排序规则： desc： 降序 asc: 升序

        :param sort_dir: The sort_dir of this ListTopSqlsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListTopSqlsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
