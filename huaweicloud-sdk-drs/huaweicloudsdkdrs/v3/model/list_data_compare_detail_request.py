# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDataCompareDetailRequest:

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
        'status': 'int',
        'type': 'str',
        'db_name': 'str',
        'target_db_name': 'str',
        'query_tb_name': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'job_id': 'job_id',
        'compare_job_id': 'compare_job_id',
        'status': 'status',
        'type': 'type',
        'db_name': 'db_name',
        'target_db_name': 'target_db_name',
        'query_tb_name': 'query_tb_name',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, x_language=None, job_id=None, compare_job_id=None, status=None, type=None, db_name=None, target_db_name=None, query_tb_name=None, limit=None, offset=None):
        """ListDataCompareDetailRequest

        The model defined in huaweicloud sdk

        :param x_language: 请求语言类型。
        :type x_language: str
        :param job_id: 任务ID。
        :type job_id: str
        :param compare_job_id: 对比任务ID。
        :type compare_job_id: str
        :param status: 对比状态。 - 0：对比不一致 - 2：对比一致 - 3：目标库表不存在 - 4：对比失败 - 5：正在对比中 - 6：等待对比中 - 7：任务已取消 - 8：源库为空 - 9：目标库为空 - 10：源库和目标库都为空 - 11：源表不存在 - 12：目标表不存在 - 13：原表和目标表都不存在 - 14：源数据库连接失败 - 15：目标库数据库连接失败 - 16：源数据库执行SQL超时 - 17：目标数据库执行SQL超时 - 18：源数据库执行SQL错误 - 19：目标数据库执行SQL错误 - 20：源库和目标库都不存在 - 21：源库不存在 - 22：目标库不存在 - 23：行数为亿行，未进行对比 - 27：超时
        :type status: int
        :param type: 类型。 - compare：查询正常对比的项 - unCompare：查询无法对比的项
        :type type: str
        :param db_name: 源数据库名。
        :type db_name: str
        :param target_db_name: 目标数据库名。
        :type target_db_name: str
        :param query_tb_name: 表名过滤关键字。
        :type query_tb_name: str
        :param limit: 每页显示的条目数量，最大值1000。
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0。
        :type offset: int
        """
        
        

        self._x_language = None
        self._job_id = None
        self._compare_job_id = None
        self._status = None
        self._type = None
        self._db_name = None
        self._target_db_name = None
        self._query_tb_name = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.job_id = job_id
        self.compare_job_id = compare_job_id
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if db_name is not None:
            self.db_name = db_name
        if target_db_name is not None:
            self.target_db_name = target_db_name
        if query_tb_name is not None:
            self.query_tb_name = query_tb_name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def x_language(self):
        """Gets the x_language of this ListDataCompareDetailRequest.

        请求语言类型。

        :return: The x_language of this ListDataCompareDetailRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListDataCompareDetailRequest.

        请求语言类型。

        :param x_language: The x_language of this ListDataCompareDetailRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def job_id(self):
        """Gets the job_id of this ListDataCompareDetailRequest.

        任务ID。

        :return: The job_id of this ListDataCompareDetailRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ListDataCompareDetailRequest.

        任务ID。

        :param job_id: The job_id of this ListDataCompareDetailRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def compare_job_id(self):
        """Gets the compare_job_id of this ListDataCompareDetailRequest.

        对比任务ID。

        :return: The compare_job_id of this ListDataCompareDetailRequest.
        :rtype: str
        """
        return self._compare_job_id

    @compare_job_id.setter
    def compare_job_id(self, compare_job_id):
        """Sets the compare_job_id of this ListDataCompareDetailRequest.

        对比任务ID。

        :param compare_job_id: The compare_job_id of this ListDataCompareDetailRequest.
        :type compare_job_id: str
        """
        self._compare_job_id = compare_job_id

    @property
    def status(self):
        """Gets the status of this ListDataCompareDetailRequest.

        对比状态。 - 0：对比不一致 - 2：对比一致 - 3：目标库表不存在 - 4：对比失败 - 5：正在对比中 - 6：等待对比中 - 7：任务已取消 - 8：源库为空 - 9：目标库为空 - 10：源库和目标库都为空 - 11：源表不存在 - 12：目标表不存在 - 13：原表和目标表都不存在 - 14：源数据库连接失败 - 15：目标库数据库连接失败 - 16：源数据库执行SQL超时 - 17：目标数据库执行SQL超时 - 18：源数据库执行SQL错误 - 19：目标数据库执行SQL错误 - 20：源库和目标库都不存在 - 21：源库不存在 - 22：目标库不存在 - 23：行数为亿行，未进行对比 - 27：超时

        :return: The status of this ListDataCompareDetailRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListDataCompareDetailRequest.

        对比状态。 - 0：对比不一致 - 2：对比一致 - 3：目标库表不存在 - 4：对比失败 - 5：正在对比中 - 6：等待对比中 - 7：任务已取消 - 8：源库为空 - 9：目标库为空 - 10：源库和目标库都为空 - 11：源表不存在 - 12：目标表不存在 - 13：原表和目标表都不存在 - 14：源数据库连接失败 - 15：目标库数据库连接失败 - 16：源数据库执行SQL超时 - 17：目标数据库执行SQL超时 - 18：源数据库执行SQL错误 - 19：目标数据库执行SQL错误 - 20：源库和目标库都不存在 - 21：源库不存在 - 22：目标库不存在 - 23：行数为亿行，未进行对比 - 27：超时

        :param status: The status of this ListDataCompareDetailRequest.
        :type status: int
        """
        self._status = status

    @property
    def type(self):
        """Gets the type of this ListDataCompareDetailRequest.

        类型。 - compare：查询正常对比的项 - unCompare：查询无法对比的项

        :return: The type of this ListDataCompareDetailRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListDataCompareDetailRequest.

        类型。 - compare：查询正常对比的项 - unCompare：查询无法对比的项

        :param type: The type of this ListDataCompareDetailRequest.
        :type type: str
        """
        self._type = type

    @property
    def db_name(self):
        """Gets the db_name of this ListDataCompareDetailRequest.

        源数据库名。

        :return: The db_name of this ListDataCompareDetailRequest.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this ListDataCompareDetailRequest.

        源数据库名。

        :param db_name: The db_name of this ListDataCompareDetailRequest.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def target_db_name(self):
        """Gets the target_db_name of this ListDataCompareDetailRequest.

        目标数据库名。

        :return: The target_db_name of this ListDataCompareDetailRequest.
        :rtype: str
        """
        return self._target_db_name

    @target_db_name.setter
    def target_db_name(self, target_db_name):
        """Sets the target_db_name of this ListDataCompareDetailRequest.

        目标数据库名。

        :param target_db_name: The target_db_name of this ListDataCompareDetailRequest.
        :type target_db_name: str
        """
        self._target_db_name = target_db_name

    @property
    def query_tb_name(self):
        """Gets the query_tb_name of this ListDataCompareDetailRequest.

        表名过滤关键字。

        :return: The query_tb_name of this ListDataCompareDetailRequest.
        :rtype: str
        """
        return self._query_tb_name

    @query_tb_name.setter
    def query_tb_name(self, query_tb_name):
        """Sets the query_tb_name of this ListDataCompareDetailRequest.

        表名过滤关键字。

        :param query_tb_name: The query_tb_name of this ListDataCompareDetailRequest.
        :type query_tb_name: str
        """
        self._query_tb_name = query_tb_name

    @property
    def limit(self):
        """Gets the limit of this ListDataCompareDetailRequest.

        每页显示的条目数量，最大值1000。

        :return: The limit of this ListDataCompareDetailRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDataCompareDetailRequest.

        每页显示的条目数量，最大值1000。

        :param limit: The limit of this ListDataCompareDetailRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListDataCompareDetailRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0。

        :return: The offset of this ListDataCompareDetailRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDataCompareDetailRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0。

        :param offset: The offset of this ListDataCompareDetailRequest.
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
        if not isinstance(other, ListDataCompareDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
