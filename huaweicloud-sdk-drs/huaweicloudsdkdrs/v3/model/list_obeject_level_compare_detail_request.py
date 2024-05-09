# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListObejectLevelCompareDetailRequest:

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
        'compare_type': 'str',
        'compare_job_id': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'job_id': 'job_id',
        'compare_type': 'compare_type',
        'compare_job_id': 'compare_job_id',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, x_language=None, job_id=None, compare_type=None, compare_job_id=None, limit=None, offset=None):
        """ListObejectLevelCompareDetailRequest

        The model defined in huaweicloud sdk

        :param x_language: 请求语言类型。
        :type x_language: str
        :param job_id: 任务ID。
        :type job_id: str
        :param compare_type: 对象类型： - DB：数据库。 - TABLE：表。 - VIEW：视图。 - EVENT：事件。 - ROUTINE：存储过程和函数。 - INDEX：索引。 - TRIGGER：触发器。 - SYNONYM：同义词。 - FUNCTION：函数。 - PROCEDURE：存储过程。 - TYPE：自定义类型。 - RULE：规则。 - DEFAULT_TYPE：缺省值。 - PLAN_GUIDE：执行计划。 - CONSTRAINT：约束。 - FILE_GROUP：文件组。 - PARTITION_FUNCTION：分区函数。 - PARTITION_SCHEME：分区方案。 - TABLE_COLLATION：表的排序规则。
        :type compare_type: str
        :param compare_job_id: 对比任务ID，不填写时默认返回最新的对比任务信息。
        :type compare_job_id: str
        :param limit: 每页显示的条目数量，最大值1000。
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0。
        :type offset: int
        """
        
        

        self._x_language = None
        self._job_id = None
        self._compare_type = None
        self._compare_job_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.job_id = job_id
        self.compare_type = compare_type
        if compare_job_id is not None:
            self.compare_job_id = compare_job_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def x_language(self):
        """Gets the x_language of this ListObejectLevelCompareDetailRequest.

        请求语言类型。

        :return: The x_language of this ListObejectLevelCompareDetailRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListObejectLevelCompareDetailRequest.

        请求语言类型。

        :param x_language: The x_language of this ListObejectLevelCompareDetailRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def job_id(self):
        """Gets the job_id of this ListObejectLevelCompareDetailRequest.

        任务ID。

        :return: The job_id of this ListObejectLevelCompareDetailRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ListObejectLevelCompareDetailRequest.

        任务ID。

        :param job_id: The job_id of this ListObejectLevelCompareDetailRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def compare_type(self):
        """Gets the compare_type of this ListObejectLevelCompareDetailRequest.

        对象类型： - DB：数据库。 - TABLE：表。 - VIEW：视图。 - EVENT：事件。 - ROUTINE：存储过程和函数。 - INDEX：索引。 - TRIGGER：触发器。 - SYNONYM：同义词。 - FUNCTION：函数。 - PROCEDURE：存储过程。 - TYPE：自定义类型。 - RULE：规则。 - DEFAULT_TYPE：缺省值。 - PLAN_GUIDE：执行计划。 - CONSTRAINT：约束。 - FILE_GROUP：文件组。 - PARTITION_FUNCTION：分区函数。 - PARTITION_SCHEME：分区方案。 - TABLE_COLLATION：表的排序规则。

        :return: The compare_type of this ListObejectLevelCompareDetailRequest.
        :rtype: str
        """
        return self._compare_type

    @compare_type.setter
    def compare_type(self, compare_type):
        """Sets the compare_type of this ListObejectLevelCompareDetailRequest.

        对象类型： - DB：数据库。 - TABLE：表。 - VIEW：视图。 - EVENT：事件。 - ROUTINE：存储过程和函数。 - INDEX：索引。 - TRIGGER：触发器。 - SYNONYM：同义词。 - FUNCTION：函数。 - PROCEDURE：存储过程。 - TYPE：自定义类型。 - RULE：规则。 - DEFAULT_TYPE：缺省值。 - PLAN_GUIDE：执行计划。 - CONSTRAINT：约束。 - FILE_GROUP：文件组。 - PARTITION_FUNCTION：分区函数。 - PARTITION_SCHEME：分区方案。 - TABLE_COLLATION：表的排序规则。

        :param compare_type: The compare_type of this ListObejectLevelCompareDetailRequest.
        :type compare_type: str
        """
        self._compare_type = compare_type

    @property
    def compare_job_id(self):
        """Gets the compare_job_id of this ListObejectLevelCompareDetailRequest.

        对比任务ID，不填写时默认返回最新的对比任务信息。

        :return: The compare_job_id of this ListObejectLevelCompareDetailRequest.
        :rtype: str
        """
        return self._compare_job_id

    @compare_job_id.setter
    def compare_job_id(self, compare_job_id):
        """Sets the compare_job_id of this ListObejectLevelCompareDetailRequest.

        对比任务ID，不填写时默认返回最新的对比任务信息。

        :param compare_job_id: The compare_job_id of this ListObejectLevelCompareDetailRequest.
        :type compare_job_id: str
        """
        self._compare_job_id = compare_job_id

    @property
    def limit(self):
        """Gets the limit of this ListObejectLevelCompareDetailRequest.

        每页显示的条目数量，最大值1000。

        :return: The limit of this ListObejectLevelCompareDetailRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListObejectLevelCompareDetailRequest.

        每页显示的条目数量，最大值1000。

        :param limit: The limit of this ListObejectLevelCompareDetailRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListObejectLevelCompareDetailRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0。

        :return: The offset of this ListObejectLevelCompareDetailRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListObejectLevelCompareDetailRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0。

        :param offset: The offset of this ListObejectLevelCompareDetailRequest.
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
        if not isinstance(other, ListObejectLevelCompareDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
