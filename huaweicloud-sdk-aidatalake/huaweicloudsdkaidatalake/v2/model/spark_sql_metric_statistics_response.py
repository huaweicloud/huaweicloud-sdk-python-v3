# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SparkSqlMetricStatisticsResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bad_records': 'int',
        'input_bytes': 'int',
        'input_records': 'int',
        'output_bytes': 'int',
        'output_records': 'int',
        'cpu_time': 'int'
    }

    attribute_map = {
        'bad_records': 'bad_records',
        'input_bytes': 'input_bytes',
        'input_records': 'input_records',
        'output_bytes': 'output_bytes',
        'output_records': 'output_records',
        'cpu_time': 'cpu_time'
    }

    def __init__(self, bad_records=None, input_bytes=None, input_records=None, output_bytes=None, output_records=None, cpu_time=None):
        r"""SparkSqlMetricStatisticsResponse

        The model defined in huaweicloud sdk

        :param bad_records: **参数解释**：脏数据行数，用于标识处理过程中发现的错误数据行数。 **取值范围**：大于等于0的整数。 
        :type bad_records: int
        :param input_bytes: **参数解释**：读取数据字节数，用于标识作业读取的数据量。 **取值范围**：大于等于0的整数，单位为字节。 
        :type input_bytes: int
        :param input_records: **参数解释**：读取数据行数，用于标识作业读取的数据记录数。 **取值范围**：大于等于0的整数。 
        :type input_records: int
        :param output_bytes: **参数解释**：输出数据字节数，用于标识作业输出的数据量。 **取值范围**：大于等于0的整数，单位为字节。 
        :type output_bytes: int
        :param output_records: **参数解释**：输出数据行数，用于标识作业输出的数据记录数。 **取值范围**：大于等于0的整数。 
        :type output_records: int
        :param cpu_time: **参数解释**：计算使用CPU秒数，用于标识作业消耗的计算资源。 **取值范围**：大于等于0的整数，单位为秒。 
        :type cpu_time: int
        """
        
        

        self._bad_records = None
        self._input_bytes = None
        self._input_records = None
        self._output_bytes = None
        self._output_records = None
        self._cpu_time = None
        self.discriminator = None

        if bad_records is not None:
            self.bad_records = bad_records
        if input_bytes is not None:
            self.input_bytes = input_bytes
        if input_records is not None:
            self.input_records = input_records
        if output_bytes is not None:
            self.output_bytes = output_bytes
        if output_records is not None:
            self.output_records = output_records
        if cpu_time is not None:
            self.cpu_time = cpu_time

    @property
    def bad_records(self):
        r"""Gets the bad_records of this SparkSqlMetricStatisticsResponse.

        **参数解释**：脏数据行数，用于标识处理过程中发现的错误数据行数。 **取值范围**：大于等于0的整数。 

        :return: The bad_records of this SparkSqlMetricStatisticsResponse.
        :rtype: int
        """
        return self._bad_records

    @bad_records.setter
    def bad_records(self, bad_records):
        r"""Sets the bad_records of this SparkSqlMetricStatisticsResponse.

        **参数解释**：脏数据行数，用于标识处理过程中发现的错误数据行数。 **取值范围**：大于等于0的整数。 

        :param bad_records: The bad_records of this SparkSqlMetricStatisticsResponse.
        :type bad_records: int
        """
        self._bad_records = bad_records

    @property
    def input_bytes(self):
        r"""Gets the input_bytes of this SparkSqlMetricStatisticsResponse.

        **参数解释**：读取数据字节数，用于标识作业读取的数据量。 **取值范围**：大于等于0的整数，单位为字节。 

        :return: The input_bytes of this SparkSqlMetricStatisticsResponse.
        :rtype: int
        """
        return self._input_bytes

    @input_bytes.setter
    def input_bytes(self, input_bytes):
        r"""Sets the input_bytes of this SparkSqlMetricStatisticsResponse.

        **参数解释**：读取数据字节数，用于标识作业读取的数据量。 **取值范围**：大于等于0的整数，单位为字节。 

        :param input_bytes: The input_bytes of this SparkSqlMetricStatisticsResponse.
        :type input_bytes: int
        """
        self._input_bytes = input_bytes

    @property
    def input_records(self):
        r"""Gets the input_records of this SparkSqlMetricStatisticsResponse.

        **参数解释**：读取数据行数，用于标识作业读取的数据记录数。 **取值范围**：大于等于0的整数。 

        :return: The input_records of this SparkSqlMetricStatisticsResponse.
        :rtype: int
        """
        return self._input_records

    @input_records.setter
    def input_records(self, input_records):
        r"""Sets the input_records of this SparkSqlMetricStatisticsResponse.

        **参数解释**：读取数据行数，用于标识作业读取的数据记录数。 **取值范围**：大于等于0的整数。 

        :param input_records: The input_records of this SparkSqlMetricStatisticsResponse.
        :type input_records: int
        """
        self._input_records = input_records

    @property
    def output_bytes(self):
        r"""Gets the output_bytes of this SparkSqlMetricStatisticsResponse.

        **参数解释**：输出数据字节数，用于标识作业输出的数据量。 **取值范围**：大于等于0的整数，单位为字节。 

        :return: The output_bytes of this SparkSqlMetricStatisticsResponse.
        :rtype: int
        """
        return self._output_bytes

    @output_bytes.setter
    def output_bytes(self, output_bytes):
        r"""Sets the output_bytes of this SparkSqlMetricStatisticsResponse.

        **参数解释**：输出数据字节数，用于标识作业输出的数据量。 **取值范围**：大于等于0的整数，单位为字节。 

        :param output_bytes: The output_bytes of this SparkSqlMetricStatisticsResponse.
        :type output_bytes: int
        """
        self._output_bytes = output_bytes

    @property
    def output_records(self):
        r"""Gets the output_records of this SparkSqlMetricStatisticsResponse.

        **参数解释**：输出数据行数，用于标识作业输出的数据记录数。 **取值范围**：大于等于0的整数。 

        :return: The output_records of this SparkSqlMetricStatisticsResponse.
        :rtype: int
        """
        return self._output_records

    @output_records.setter
    def output_records(self, output_records):
        r"""Sets the output_records of this SparkSqlMetricStatisticsResponse.

        **参数解释**：输出数据行数，用于标识作业输出的数据记录数。 **取值范围**：大于等于0的整数。 

        :param output_records: The output_records of this SparkSqlMetricStatisticsResponse.
        :type output_records: int
        """
        self._output_records = output_records

    @property
    def cpu_time(self):
        r"""Gets the cpu_time of this SparkSqlMetricStatisticsResponse.

        **参数解释**：计算使用CPU秒数，用于标识作业消耗的计算资源。 **取值范围**：大于等于0的整数，单位为秒。 

        :return: The cpu_time of this SparkSqlMetricStatisticsResponse.
        :rtype: int
        """
        return self._cpu_time

    @cpu_time.setter
    def cpu_time(self, cpu_time):
        r"""Sets the cpu_time of this SparkSqlMetricStatisticsResponse.

        **参数解释**：计算使用CPU秒数，用于标识作业消耗的计算资源。 **取值范围**：大于等于0的整数，单位为秒。 

        :param cpu_time: The cpu_time of this SparkSqlMetricStatisticsResponse.
        :type cpu_time: int
        """
        self._cpu_time = cpu_time

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
        if not isinstance(other, SparkSqlMetricStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
