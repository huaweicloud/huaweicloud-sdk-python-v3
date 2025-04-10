# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFlinkSqlJobGraphRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sql_body': 'str',
        'flink_version': 'str',
        'cu_number': 'int',
        'manager_cu_number': 'int',
        'parallel_number': 'int',
        'tm_cus': 'int',
        'tm_slot_num': 'int',
        'operator_config': 'str',
        'static_estimator': 'bool',
        'job_type': 'str',
        'graph_type': 'str',
        'static_estimator_config': 'str'
    }

    attribute_map = {
        'sql_body': 'sql_body',
        'flink_version': 'flink_version',
        'cu_number': 'cu_number',
        'manager_cu_number': 'manager_cu_number',
        'parallel_number': 'parallel_number',
        'tm_cus': 'tm_cus',
        'tm_slot_num': 'tm_slot_num',
        'operator_config': 'operator_config',
        'static_estimator': 'static_estimator',
        'job_type': 'job_type',
        'graph_type': 'graph_type',
        'static_estimator_config': 'static_estimator_config'
    }

    def __init__(self, sql_body=None, flink_version=None, cu_number=None, manager_cu_number=None, parallel_number=None, tm_cus=None, tm_slot_num=None, operator_config=None, static_estimator=None, job_type=None, graph_type=None, static_estimator_config=None):
        r"""CreateFlinkSqlJobGraphRequestBody

        The model defined in huaweicloud sdk

        :param sql_body: SQL
        :type sql_body: str
        :param flink_version: Flink版本。当前只支持1.10和1.12。
        :type flink_version: str
        :param cu_number: CU总数
        :type cu_number: int
        :param manager_cu_number: 管理单元CU数量
        :type manager_cu_number: int
        :param parallel_number: 最大并行度
        :type parallel_number: int
        :param tm_cus: 单个taskManagerCU数量
        :type tm_cus: int
        :param tm_slot_num: 单个taskManager Slot数量
        :type tm_slot_num: int
        :param operator_config: 算子的配置
        :type operator_config: str
        :param static_estimator: 是否静态资源预估
        :type static_estimator: bool
        :param job_type: 作业类型
        :type job_type: str
        :param graph_type: 流图类型。当前支持以下两种流图类型。 简化流图：simple_graph 静态流图：job_graph。
        :type graph_type: str
        :param static_estimator_config: 每个算子的流量/命中率配置，json格式的字符串。
        :type static_estimator_config: str
        """
        
        

        self._sql_body = None
        self._flink_version = None
        self._cu_number = None
        self._manager_cu_number = None
        self._parallel_number = None
        self._tm_cus = None
        self._tm_slot_num = None
        self._operator_config = None
        self._static_estimator = None
        self._job_type = None
        self._graph_type = None
        self._static_estimator_config = None
        self.discriminator = None

        self.sql_body = sql_body
        if flink_version is not None:
            self.flink_version = flink_version
        if cu_number is not None:
            self.cu_number = cu_number
        if manager_cu_number is not None:
            self.manager_cu_number = manager_cu_number
        if parallel_number is not None:
            self.parallel_number = parallel_number
        if tm_cus is not None:
            self.tm_cus = tm_cus
        if tm_slot_num is not None:
            self.tm_slot_num = tm_slot_num
        if operator_config is not None:
            self.operator_config = operator_config
        if static_estimator is not None:
            self.static_estimator = static_estimator
        if job_type is not None:
            self.job_type = job_type
        if graph_type is not None:
            self.graph_type = graph_type
        if static_estimator_config is not None:
            self.static_estimator_config = static_estimator_config

    @property
    def sql_body(self):
        r"""Gets the sql_body of this CreateFlinkSqlJobGraphRequestBody.

        SQL

        :return: The sql_body of this CreateFlinkSqlJobGraphRequestBody.
        :rtype: str
        """
        return self._sql_body

    @sql_body.setter
    def sql_body(self, sql_body):
        r"""Sets the sql_body of this CreateFlinkSqlJobGraphRequestBody.

        SQL

        :param sql_body: The sql_body of this CreateFlinkSqlJobGraphRequestBody.
        :type sql_body: str
        """
        self._sql_body = sql_body

    @property
    def flink_version(self):
        r"""Gets the flink_version of this CreateFlinkSqlJobGraphRequestBody.

        Flink版本。当前只支持1.10和1.12。

        :return: The flink_version of this CreateFlinkSqlJobGraphRequestBody.
        :rtype: str
        """
        return self._flink_version

    @flink_version.setter
    def flink_version(self, flink_version):
        r"""Sets the flink_version of this CreateFlinkSqlJobGraphRequestBody.

        Flink版本。当前只支持1.10和1.12。

        :param flink_version: The flink_version of this CreateFlinkSqlJobGraphRequestBody.
        :type flink_version: str
        """
        self._flink_version = flink_version

    @property
    def cu_number(self):
        r"""Gets the cu_number of this CreateFlinkSqlJobGraphRequestBody.

        CU总数

        :return: The cu_number of this CreateFlinkSqlJobGraphRequestBody.
        :rtype: int
        """
        return self._cu_number

    @cu_number.setter
    def cu_number(self, cu_number):
        r"""Sets the cu_number of this CreateFlinkSqlJobGraphRequestBody.

        CU总数

        :param cu_number: The cu_number of this CreateFlinkSqlJobGraphRequestBody.
        :type cu_number: int
        """
        self._cu_number = cu_number

    @property
    def manager_cu_number(self):
        r"""Gets the manager_cu_number of this CreateFlinkSqlJobGraphRequestBody.

        管理单元CU数量

        :return: The manager_cu_number of this CreateFlinkSqlJobGraphRequestBody.
        :rtype: int
        """
        return self._manager_cu_number

    @manager_cu_number.setter
    def manager_cu_number(self, manager_cu_number):
        r"""Sets the manager_cu_number of this CreateFlinkSqlJobGraphRequestBody.

        管理单元CU数量

        :param manager_cu_number: The manager_cu_number of this CreateFlinkSqlJobGraphRequestBody.
        :type manager_cu_number: int
        """
        self._manager_cu_number = manager_cu_number

    @property
    def parallel_number(self):
        r"""Gets the parallel_number of this CreateFlinkSqlJobGraphRequestBody.

        最大并行度

        :return: The parallel_number of this CreateFlinkSqlJobGraphRequestBody.
        :rtype: int
        """
        return self._parallel_number

    @parallel_number.setter
    def parallel_number(self, parallel_number):
        r"""Sets the parallel_number of this CreateFlinkSqlJobGraphRequestBody.

        最大并行度

        :param parallel_number: The parallel_number of this CreateFlinkSqlJobGraphRequestBody.
        :type parallel_number: int
        """
        self._parallel_number = parallel_number

    @property
    def tm_cus(self):
        r"""Gets the tm_cus of this CreateFlinkSqlJobGraphRequestBody.

        单个taskManagerCU数量

        :return: The tm_cus of this CreateFlinkSqlJobGraphRequestBody.
        :rtype: int
        """
        return self._tm_cus

    @tm_cus.setter
    def tm_cus(self, tm_cus):
        r"""Sets the tm_cus of this CreateFlinkSqlJobGraphRequestBody.

        单个taskManagerCU数量

        :param tm_cus: The tm_cus of this CreateFlinkSqlJobGraphRequestBody.
        :type tm_cus: int
        """
        self._tm_cus = tm_cus

    @property
    def tm_slot_num(self):
        r"""Gets the tm_slot_num of this CreateFlinkSqlJobGraphRequestBody.

        单个taskManager Slot数量

        :return: The tm_slot_num of this CreateFlinkSqlJobGraphRequestBody.
        :rtype: int
        """
        return self._tm_slot_num

    @tm_slot_num.setter
    def tm_slot_num(self, tm_slot_num):
        r"""Sets the tm_slot_num of this CreateFlinkSqlJobGraphRequestBody.

        单个taskManager Slot数量

        :param tm_slot_num: The tm_slot_num of this CreateFlinkSqlJobGraphRequestBody.
        :type tm_slot_num: int
        """
        self._tm_slot_num = tm_slot_num

    @property
    def operator_config(self):
        r"""Gets the operator_config of this CreateFlinkSqlJobGraphRequestBody.

        算子的配置

        :return: The operator_config of this CreateFlinkSqlJobGraphRequestBody.
        :rtype: str
        """
        return self._operator_config

    @operator_config.setter
    def operator_config(self, operator_config):
        r"""Sets the operator_config of this CreateFlinkSqlJobGraphRequestBody.

        算子的配置

        :param operator_config: The operator_config of this CreateFlinkSqlJobGraphRequestBody.
        :type operator_config: str
        """
        self._operator_config = operator_config

    @property
    def static_estimator(self):
        r"""Gets the static_estimator of this CreateFlinkSqlJobGraphRequestBody.

        是否静态资源预估

        :return: The static_estimator of this CreateFlinkSqlJobGraphRequestBody.
        :rtype: bool
        """
        return self._static_estimator

    @static_estimator.setter
    def static_estimator(self, static_estimator):
        r"""Sets the static_estimator of this CreateFlinkSqlJobGraphRequestBody.

        是否静态资源预估

        :param static_estimator: The static_estimator of this CreateFlinkSqlJobGraphRequestBody.
        :type static_estimator: bool
        """
        self._static_estimator = static_estimator

    @property
    def job_type(self):
        r"""Gets the job_type of this CreateFlinkSqlJobGraphRequestBody.

        作业类型

        :return: The job_type of this CreateFlinkSqlJobGraphRequestBody.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this CreateFlinkSqlJobGraphRequestBody.

        作业类型

        :param job_type: The job_type of this CreateFlinkSqlJobGraphRequestBody.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def graph_type(self):
        r"""Gets the graph_type of this CreateFlinkSqlJobGraphRequestBody.

        流图类型。当前支持以下两种流图类型。 简化流图：simple_graph 静态流图：job_graph。

        :return: The graph_type of this CreateFlinkSqlJobGraphRequestBody.
        :rtype: str
        """
        return self._graph_type

    @graph_type.setter
    def graph_type(self, graph_type):
        r"""Sets the graph_type of this CreateFlinkSqlJobGraphRequestBody.

        流图类型。当前支持以下两种流图类型。 简化流图：simple_graph 静态流图：job_graph。

        :param graph_type: The graph_type of this CreateFlinkSqlJobGraphRequestBody.
        :type graph_type: str
        """
        self._graph_type = graph_type

    @property
    def static_estimator_config(self):
        r"""Gets the static_estimator_config of this CreateFlinkSqlJobGraphRequestBody.

        每个算子的流量/命中率配置，json格式的字符串。

        :return: The static_estimator_config of this CreateFlinkSqlJobGraphRequestBody.
        :rtype: str
        """
        return self._static_estimator_config

    @static_estimator_config.setter
    def static_estimator_config(self, static_estimator_config):
        r"""Sets the static_estimator_config of this CreateFlinkSqlJobGraphRequestBody.

        每个算子的流量/命中率配置，json格式的字符串。

        :param static_estimator_config: The static_estimator_config of this CreateFlinkSqlJobGraphRequestBody.
        :type static_estimator_config: str
        """
        self._static_estimator_config = static_estimator_config

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
        if not isinstance(other, CreateFlinkSqlJobGraphRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
