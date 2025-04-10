# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowReplayResultsRequest:

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
        'type': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'offset': 'int',
        'limit': 'int',
        'sort_key': 'str',
        'sort_dir': 'str',
        'target_name': 'str',
        'is_sample': 'bool',
        'error_type': 'str',
        'sql_template_md5': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'x_language': 'X-Language',
        'type': 'type',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'offset': 'offset',
        'limit': 'limit',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'target_name': 'target_name',
        'is_sample': 'is_sample',
        'error_type': 'error_type',
        'sql_template_md5': 'sql_template_md5'
    }

    def __init__(self, job_id=None, x_language=None, type=None, start_time=None, end_time=None, offset=None, limit=None, sort_key=None, sort_dir=None, target_name=None, is_sample=None, error_type=None, sql_template_md5=None):
        r"""ShowReplayResultsRequest

        The model defined in huaweicloud sdk

        :param job_id: 任务ID。
        :type job_id: str
        :param x_language: 请求语言类型。
        :type x_language: str
        :param type: 结果类型。取值： - shard_statistics：回放概览基于时间维度统计信息。 - slow_sql：慢SQL详情。 - error_sql： 回放异常SQL详情。 - slow_sql_template：慢SQL统计信息。  - error_sql_template：异常SQL统计信息。 - replaying_sql：正在回放SQL详情。 - error_classification：回放异常SQL分类。
        :type type: str
        :param start_time: 查询数据的起始时间，在type为shard_statistics、slow_sql、error_sql时必填
        :type start_time: str
        :param end_time: 查询数据的结束时间，在type为shard_statistics、slow_sql、error_sql时必填
        :type end_time: str
        :param offset: 分页查询数据表当前超始偏移量, 在type为slow_sql、error_sql、slow_sql_template、error_sql_template必填
        :type offset: int
        :param limit: 分页查询数据表当前页数据总量，在type为slow_sql、error_sql、slow_sql_template、error_sql_template必填
        :type limit: int
        :param sort_key: 返回结果按该关键字排序（slow_sql_template支持count，maxLatency、avgLatency关键字，error_sql_template支持count关键字）
        :type sort_key: str
        :param sort_dir: 排序规则，取值如下： - asc：升序 - desc：降序
        :type sort_dir: str
        :param target_name: 回放数据库名称，用于在一致性回放策略场景，过滤目标库与源库镜像库回放结果。参数非必须，不提供则默认查询所有数据，其取值如下： - target：查询目标库回放结果 - target_mirror：查询源库镜像库回放结果
        :type target_name: str
        :param is_sample: 是否查询样例true/false，type&#x3D;slow_sql/error_sql时生效，值为true时只查询一条样例数据。
        :type is_sample: bool
        :param error_type: 错误分类，type&#x3D;error_sql/error_sql_template时生效，根据错误分类过滤数据。
        :type error_type: str
        :param sql_template_md5: sql模板md5，type&#x3D;slow_sql/error_sql时生效，根据模板过滤对应的异常SQL和慢SQL，该值为本接口type&#x3D;slow_sql_template/error_sql_template时的返回字段。
        :type sql_template_md5: str
        """
        
        

        self._job_id = None
        self._x_language = None
        self._type = None
        self._start_time = None
        self._end_time = None
        self._offset = None
        self._limit = None
        self._sort_key = None
        self._sort_dir = None
        self._target_name = None
        self._is_sample = None
        self._error_type = None
        self._sql_template_md5 = None
        self.discriminator = None

        self.job_id = job_id
        if x_language is not None:
            self.x_language = x_language
        self.type = type
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
        if target_name is not None:
            self.target_name = target_name
        if is_sample is not None:
            self.is_sample = is_sample
        if error_type is not None:
            self.error_type = error_type
        if sql_template_md5 is not None:
            self.sql_template_md5 = sql_template_md5

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowReplayResultsRequest.

        任务ID。

        :return: The job_id of this ShowReplayResultsRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowReplayResultsRequest.

        任务ID。

        :param job_id: The job_id of this ShowReplayResultsRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowReplayResultsRequest.

        请求语言类型。

        :return: The x_language of this ShowReplayResultsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowReplayResultsRequest.

        请求语言类型。

        :param x_language: The x_language of this ShowReplayResultsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def type(self):
        r"""Gets the type of this ShowReplayResultsRequest.

        结果类型。取值： - shard_statistics：回放概览基于时间维度统计信息。 - slow_sql：慢SQL详情。 - error_sql： 回放异常SQL详情。 - slow_sql_template：慢SQL统计信息。  - error_sql_template：异常SQL统计信息。 - replaying_sql：正在回放SQL详情。 - error_classification：回放异常SQL分类。

        :return: The type of this ShowReplayResultsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowReplayResultsRequest.

        结果类型。取值： - shard_statistics：回放概览基于时间维度统计信息。 - slow_sql：慢SQL详情。 - error_sql： 回放异常SQL详情。 - slow_sql_template：慢SQL统计信息。  - error_sql_template：异常SQL统计信息。 - replaying_sql：正在回放SQL详情。 - error_classification：回放异常SQL分类。

        :param type: The type of this ShowReplayResultsRequest.
        :type type: str
        """
        self._type = type

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowReplayResultsRequest.

        查询数据的起始时间，在type为shard_statistics、slow_sql、error_sql时必填

        :return: The start_time of this ShowReplayResultsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowReplayResultsRequest.

        查询数据的起始时间，在type为shard_statistics、slow_sql、error_sql时必填

        :param start_time: The start_time of this ShowReplayResultsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowReplayResultsRequest.

        查询数据的结束时间，在type为shard_statistics、slow_sql、error_sql时必填

        :return: The end_time of this ShowReplayResultsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowReplayResultsRequest.

        查询数据的结束时间，在type为shard_statistics、slow_sql、error_sql时必填

        :param end_time: The end_time of this ShowReplayResultsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def offset(self):
        r"""Gets the offset of this ShowReplayResultsRequest.

        分页查询数据表当前超始偏移量, 在type为slow_sql、error_sql、slow_sql_template、error_sql_template必填

        :return: The offset of this ShowReplayResultsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowReplayResultsRequest.

        分页查询数据表当前超始偏移量, 在type为slow_sql、error_sql、slow_sql_template、error_sql_template必填

        :param offset: The offset of this ShowReplayResultsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowReplayResultsRequest.

        分页查询数据表当前页数据总量，在type为slow_sql、error_sql、slow_sql_template、error_sql_template必填

        :return: The limit of this ShowReplayResultsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowReplayResultsRequest.

        分页查询数据表当前页数据总量，在type为slow_sql、error_sql、slow_sql_template、error_sql_template必填

        :param limit: The limit of this ShowReplayResultsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ShowReplayResultsRequest.

        返回结果按该关键字排序（slow_sql_template支持count，maxLatency、avgLatency关键字，error_sql_template支持count关键字）

        :return: The sort_key of this ShowReplayResultsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ShowReplayResultsRequest.

        返回结果按该关键字排序（slow_sql_template支持count，maxLatency、avgLatency关键字，error_sql_template支持count关键字）

        :param sort_key: The sort_key of this ShowReplayResultsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ShowReplayResultsRequest.

        排序规则，取值如下： - asc：升序 - desc：降序

        :return: The sort_dir of this ShowReplayResultsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ShowReplayResultsRequest.

        排序规则，取值如下： - asc：升序 - desc：降序

        :param sort_dir: The sort_dir of this ShowReplayResultsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def target_name(self):
        r"""Gets the target_name of this ShowReplayResultsRequest.

        回放数据库名称，用于在一致性回放策略场景，过滤目标库与源库镜像库回放结果。参数非必须，不提供则默认查询所有数据，其取值如下： - target：查询目标库回放结果 - target_mirror：查询源库镜像库回放结果

        :return: The target_name of this ShowReplayResultsRequest.
        :rtype: str
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        r"""Sets the target_name of this ShowReplayResultsRequest.

        回放数据库名称，用于在一致性回放策略场景，过滤目标库与源库镜像库回放结果。参数非必须，不提供则默认查询所有数据，其取值如下： - target：查询目标库回放结果 - target_mirror：查询源库镜像库回放结果

        :param target_name: The target_name of this ShowReplayResultsRequest.
        :type target_name: str
        """
        self._target_name = target_name

    @property
    def is_sample(self):
        r"""Gets the is_sample of this ShowReplayResultsRequest.

        是否查询样例true/false，type=slow_sql/error_sql时生效，值为true时只查询一条样例数据。

        :return: The is_sample of this ShowReplayResultsRequest.
        :rtype: bool
        """
        return self._is_sample

    @is_sample.setter
    def is_sample(self, is_sample):
        r"""Sets the is_sample of this ShowReplayResultsRequest.

        是否查询样例true/false，type=slow_sql/error_sql时生效，值为true时只查询一条样例数据。

        :param is_sample: The is_sample of this ShowReplayResultsRequest.
        :type is_sample: bool
        """
        self._is_sample = is_sample

    @property
    def error_type(self):
        r"""Gets the error_type of this ShowReplayResultsRequest.

        错误分类，type=error_sql/error_sql_template时生效，根据错误分类过滤数据。

        :return: The error_type of this ShowReplayResultsRequest.
        :rtype: str
        """
        return self._error_type

    @error_type.setter
    def error_type(self, error_type):
        r"""Sets the error_type of this ShowReplayResultsRequest.

        错误分类，type=error_sql/error_sql_template时生效，根据错误分类过滤数据。

        :param error_type: The error_type of this ShowReplayResultsRequest.
        :type error_type: str
        """
        self._error_type = error_type

    @property
    def sql_template_md5(self):
        r"""Gets the sql_template_md5 of this ShowReplayResultsRequest.

        sql模板md5，type=slow_sql/error_sql时生效，根据模板过滤对应的异常SQL和慢SQL，该值为本接口type=slow_sql_template/error_sql_template时的返回字段。

        :return: The sql_template_md5 of this ShowReplayResultsRequest.
        :rtype: str
        """
        return self._sql_template_md5

    @sql_template_md5.setter
    def sql_template_md5(self, sql_template_md5):
        r"""Sets the sql_template_md5 of this ShowReplayResultsRequest.

        sql模板md5，type=slow_sql/error_sql时生效，根据模板过滤对应的异常SQL和慢SQL，该值为本接口type=slow_sql_template/error_sql_template时的返回字段。

        :param sql_template_md5: The sql_template_md5 of this ShowReplayResultsRequest.
        :type sql_template_md5: str
        """
        self._sql_template_md5 = sql_template_md5

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
        if not isinstance(other, ShowReplayResultsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
