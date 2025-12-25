# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricMetaDataDerivedMetrics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric_dimension': 'int',
        'max_query_range': 'int',
        'date_start': 'str',
        'date_end': 'str',
        'date_format': 'str',
        'query_type': 'str',
        'query_function': 'str'
    }

    attribute_map = {
        'metric_dimension': 'metric_dimension',
        'max_query_range': 'max_query_range',
        'date_start': 'date_start',
        'date_end': 'date_end',
        'date_format': 'date_format',
        'query_type': 'query_type',
        'query_function': 'query_function'
    }

    def __init__(self, metric_dimension=None, max_query_range=None, date_start=None, date_end=None, date_format=None, query_type=None, query_function=None):
        r"""MetricMetaDataDerivedMetrics

        The model defined in huaweicloud sdk

        :param metric_dimension: 衍生指标结果维度，0维：单个数字，2维：图表或表格，3+维：多标签图表
        :type metric_dimension: int
        :param max_query_range: 指标支持的最大检索范围，单位：天；
        :type max_query_range: int
        :param date_start: 指标查询范围相对起始时间 datemath表达式
        :type date_start: str
        :param date_end: 指标查询范围相对截止时间 datemath表达式
        :type date_end: str
        :param date_format: 时间格式，epoch_millis;epoch_second;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ
        :type date_format: str
        :param query_type: 获取指标结果方式，cbsl, api, dsl, sql
        :type query_type: str
        :param query_function: 获取指标结果的方法，转义成字符串, 共四种query方式：CBSL、API、DSL、SQL - query_type为&#x60;CBSL&#x60;时，function传入dataspace_id，pipe_id，query，sort, from, to   样例：     &#x60;&#x60;&#x60;     {\\\&quot;dataspace_id\\\&quot;:\\\&quot;3939573a-12a0-436f-b0e5-ab2872a1fde9\\\&quot;,\\\&quot;pipe_id\\\&quot;:\\\&quot;9db9d8a6-d9e6-4b32-990e-40f0afe4655d\\\&quot;,\\\&quot;query\\\&quot;:\\\&quot;* | select ack_pps, device_type as type\\\&quot;,\\\&quot;sort\\\&quot;:\\\&quot;desc\\\&quot;,\\\&quot;from\\\&quot;:${date_from},\\\&quot;to\\\&quot;:${date_to}}     &#x60;&#x60;&#x60;      转义前：     &#x60;&#x60;&#x60;json     {         \&quot;dataspace_id\&quot;:\&quot;3939573a-12a0-436f-b0e5-ab2872a1fde9\&quot;,         \&quot;pipe_id\&quot;:\&quot;9db9d8a6-d9e6-4b32-990e-40f0afe4655d\&quot;,         \&quot;query\&quot;:\&quot;* | select ack_pps, device_type as type\&quot;,         \&quot;sort\&quot;:\&quot;desc\&quot;,         \&quot;from\&quot;: ${date_from},         \&quot;to\&quot;: ${date_to}     }     &#x60;&#x60;&#x60; - query_type为&#x60;API&#x60;时，function传入api method、url、path_params、headers、response_parser（解析API返回值所需，定义label和json_path将返回值解析为二维表格，label为表头，json_path为字段提取路径）   样例：     &#x60;&#x60;&#x60;     {\\\&quot;method\\\&quot;:\\\&quot;POST\\\&quot;,\\\&quot;uri\\\&quot;:\\\&quot;/v1/${project_id}/只填写uri/不带域名/xxx\\\&quot;,\\\&quot;headers\\\&quot;:{\\\&quot;X-Auth-Token\\\&quot;:\\\&quot;${project_token}\\\&quot;},\\\&quot;response_parser\\\&quot;:{\\\&quot;labels\\\&quot;:[\\\&quot;攻击类型\\\&quot;,\\\&quot;攻击源\\\&quot;,\\\&quot;时间\\\&quot;],\\\&quot;json_path\\\&quot;:[\\\&quot;$.data[:].type\\\&quot;,\\\&quot;$.data[:].source\\\&quot;,\\\&quot;$.data[:].time\\\&quot;]}}     &#x60;&#x60;&#x60;      转义前：     &#x60;&#x60;&#x60;json     {         \&quot;method\&quot;:\&quot;POST\&quot;,         \&quot;uri\&quot;:\&quot;/v1/${project_id}/只填写uri/不带域名/xxx\&quot;,         \&quot;headers\&quot;:{             \&quot;X-Auth-Token\&quot;: \&quot;${project_token}\&quot;         },         \&quot;response_parser\&quot;:{             \&quot;labels\&quot;:[                 \&quot;攻击类型\&quot;,                 \&quot;攻击源\&quot;,                 \&quot;时间\&quot;             ],             \&quot;json_path\&quot;:[                 \&quot;$.data[:].type\&quot;,                 \&quot;$.data[:].source\&quot;,                 \&quot;$.data[:].time\&quot;             ]         }     }     &#x60;&#x60;&#x60; - query_type为&#x60;DSL&#x60;时，指定index, dsl(转义成字符串), response_parser   样例：     &#x60;&#x60;&#x60;     {\\\&quot;index\\\&quot;:\\\&quot;index_xxx_*\\\&quot;,\\\&quot;dsl\\\&quot;:\\\&quot;{\\\\\\\&quot;query\\\\\\\&quot;:{\\\\\\\&quot;match_all\\\\\\\&quot;:{}}}\\\&quot;,\\\&quot;response_parser\\\&quot;:{\\\&quot;labels\\\&quot;:[\\\&quot;攻击类型\\\&quot;,\\\&quot;攻击源\\\&quot;,\\\&quot;时间\\\&quot;],\\\&quot;json_path\\\&quot;:[\\\&quot;$.data[:].type\\\&quot;,\\\&quot;$.data[:].source\\\&quot;,\\\&quot;$.data[:].time\\\&quot;]}}     &#x60;&#x60;&#x60;      转义前：      &#x60;&#x60;&#x60;json     {         \&quot;index\&quot;:\&quot;index_xxx_*\&quot;,         \&quot;dsl\&quot;:\&quot;{\\\&quot;query\\\&quot;:{\\\&quot;match_all\\\&quot;:{}}}\&quot;,         \&quot;response_parser\&quot;:{             \&quot;labels\&quot;:[                 \&quot;攻击类型\&quot;,                 \&quot;攻击源\&quot;,                 \&quot;时间\&quot;             ],             \&quot;json_path\&quot;:[                 \&quot;$.data[:].type\&quot;,                 \&quot;$.data[:].source\&quot;,                 \&quot;$.data[:].time\&quot;             ]         }     }     &#x60;&#x60;&#x60; - query_type为&#x60;sql&#x60;时，指定opendistro sql插件查询json(转义成字符串)   样例：     &#x60;&#x60;&#x60;    {\\\&quot;query\\\&quot;:\\\&quot;SELECT count(1) as count , msg.DstPort FROM isap_log_nip_ttl* where oct &gt;&#x3D; TIMESTAMP(\\\\\\\&quot;${date_from}\\\\\\\&quot;) and oct &lt;&#x3D; TIMESTAMP(\\\\\\\&quot;${date_to}\\\\\\\&quot;) group by msg.DstPort order by count desc limit 5\\\&quot;}     &#x60;&#x60;&#x60;           转义前：      &#x60;&#x60;&#x60;json     {         \&quot;query\&quot;:\&quot;SELECT count(1) as count , msg.DstPort FROM isap_log_nip_ttl* where oct &gt;&#x3D; TIMESTAMP(\\\&quot;${date_from}\\\&quot;) and oct &lt;&#x3D; TIMESTAMP(\\\&quot;${date_to}\\\&quot;) group by msg.DstPort order by count desc limit 5\&quot;     }     &#x60;&#x60;&#x60;
        :type query_function: str
        """
        
        

        self._metric_dimension = None
        self._max_query_range = None
        self._date_start = None
        self._date_end = None
        self._date_format = None
        self._query_type = None
        self._query_function = None
        self.discriminator = None

        self.metric_dimension = metric_dimension
        if max_query_range is not None:
            self.max_query_range = max_query_range
        if date_start is not None:
            self.date_start = date_start
        if date_end is not None:
            self.date_end = date_end
        if date_format is not None:
            self.date_format = date_format
        self.query_type = query_type
        self.query_function = query_function

    @property
    def metric_dimension(self):
        r"""Gets the metric_dimension of this MetricMetaDataDerivedMetrics.

        衍生指标结果维度，0维：单个数字，2维：图表或表格，3+维：多标签图表

        :return: The metric_dimension of this MetricMetaDataDerivedMetrics.
        :rtype: int
        """
        return self._metric_dimension

    @metric_dimension.setter
    def metric_dimension(self, metric_dimension):
        r"""Sets the metric_dimension of this MetricMetaDataDerivedMetrics.

        衍生指标结果维度，0维：单个数字，2维：图表或表格，3+维：多标签图表

        :param metric_dimension: The metric_dimension of this MetricMetaDataDerivedMetrics.
        :type metric_dimension: int
        """
        self._metric_dimension = metric_dimension

    @property
    def max_query_range(self):
        r"""Gets the max_query_range of this MetricMetaDataDerivedMetrics.

        指标支持的最大检索范围，单位：天；

        :return: The max_query_range of this MetricMetaDataDerivedMetrics.
        :rtype: int
        """
        return self._max_query_range

    @max_query_range.setter
    def max_query_range(self, max_query_range):
        r"""Sets the max_query_range of this MetricMetaDataDerivedMetrics.

        指标支持的最大检索范围，单位：天；

        :param max_query_range: The max_query_range of this MetricMetaDataDerivedMetrics.
        :type max_query_range: int
        """
        self._max_query_range = max_query_range

    @property
    def date_start(self):
        r"""Gets the date_start of this MetricMetaDataDerivedMetrics.

        指标查询范围相对起始时间 datemath表达式

        :return: The date_start of this MetricMetaDataDerivedMetrics.
        :rtype: str
        """
        return self._date_start

    @date_start.setter
    def date_start(self, date_start):
        r"""Sets the date_start of this MetricMetaDataDerivedMetrics.

        指标查询范围相对起始时间 datemath表达式

        :param date_start: The date_start of this MetricMetaDataDerivedMetrics.
        :type date_start: str
        """
        self._date_start = date_start

    @property
    def date_end(self):
        r"""Gets the date_end of this MetricMetaDataDerivedMetrics.

        指标查询范围相对截止时间 datemath表达式

        :return: The date_end of this MetricMetaDataDerivedMetrics.
        :rtype: str
        """
        return self._date_end

    @date_end.setter
    def date_end(self, date_end):
        r"""Sets the date_end of this MetricMetaDataDerivedMetrics.

        指标查询范围相对截止时间 datemath表达式

        :param date_end: The date_end of this MetricMetaDataDerivedMetrics.
        :type date_end: str
        """
        self._date_end = date_end

    @property
    def date_format(self):
        r"""Gets the date_format of this MetricMetaDataDerivedMetrics.

        时间格式，epoch_millis;epoch_second;yyyy-MM-dd'T'HH:mm:ss.SSSZ

        :return: The date_format of this MetricMetaDataDerivedMetrics.
        :rtype: str
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        r"""Sets the date_format of this MetricMetaDataDerivedMetrics.

        时间格式，epoch_millis;epoch_second;yyyy-MM-dd'T'HH:mm:ss.SSSZ

        :param date_format: The date_format of this MetricMetaDataDerivedMetrics.
        :type date_format: str
        """
        self._date_format = date_format

    @property
    def query_type(self):
        r"""Gets the query_type of this MetricMetaDataDerivedMetrics.

        获取指标结果方式，cbsl, api, dsl, sql

        :return: The query_type of this MetricMetaDataDerivedMetrics.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        r"""Sets the query_type of this MetricMetaDataDerivedMetrics.

        获取指标结果方式，cbsl, api, dsl, sql

        :param query_type: The query_type of this MetricMetaDataDerivedMetrics.
        :type query_type: str
        """
        self._query_type = query_type

    @property
    def query_function(self):
        r"""Gets the query_function of this MetricMetaDataDerivedMetrics.

        获取指标结果的方法，转义成字符串, 共四种query方式：CBSL、API、DSL、SQL - query_type为`CBSL`时，function传入dataspace_id，pipe_id，query，sort, from, to   样例：     ```     {\\\"dataspace_id\\\":\\\"3939573a-12a0-436f-b0e5-ab2872a1fde9\\\",\\\"pipe_id\\\":\\\"9db9d8a6-d9e6-4b32-990e-40f0afe4655d\\\",\\\"query\\\":\\\"* | select ack_pps, device_type as type\\\",\\\"sort\\\":\\\"desc\\\",\\\"from\\\":${date_from},\\\"to\\\":${date_to}}     ```      转义前：     ```json     {         \"dataspace_id\":\"3939573a-12a0-436f-b0e5-ab2872a1fde9\",         \"pipe_id\":\"9db9d8a6-d9e6-4b32-990e-40f0afe4655d\",         \"query\":\"* | select ack_pps, device_type as type\",         \"sort\":\"desc\",         \"from\": ${date_from},         \"to\": ${date_to}     }     ``` - query_type为`API`时，function传入api method、url、path_params、headers、response_parser（解析API返回值所需，定义label和json_path将返回值解析为二维表格，label为表头，json_path为字段提取路径）   样例：     ```     {\\\"method\\\":\\\"POST\\\",\\\"uri\\\":\\\"/v1/${project_id}/只填写uri/不带域名/xxx\\\",\\\"headers\\\":{\\\"X-Auth-Token\\\":\\\"${project_token}\\\"},\\\"response_parser\\\":{\\\"labels\\\":[\\\"攻击类型\\\",\\\"攻击源\\\",\\\"时间\\\"],\\\"json_path\\\":[\\\"$.data[:].type\\\",\\\"$.data[:].source\\\",\\\"$.data[:].time\\\"]}}     ```      转义前：     ```json     {         \"method\":\"POST\",         \"uri\":\"/v1/${project_id}/只填写uri/不带域名/xxx\",         \"headers\":{             \"X-Auth-Token\": \"${project_token}\"         },         \"response_parser\":{             \"labels\":[                 \"攻击类型\",                 \"攻击源\",                 \"时间\"             ],             \"json_path\":[                 \"$.data[:].type\",                 \"$.data[:].source\",                 \"$.data[:].time\"             ]         }     }     ``` - query_type为`DSL`时，指定index, dsl(转义成字符串), response_parser   样例：     ```     {\\\"index\\\":\\\"index_xxx_*\\\",\\\"dsl\\\":\\\"{\\\\\\\"query\\\\\\\":{\\\\\\\"match_all\\\\\\\":{}}}\\\",\\\"response_parser\\\":{\\\"labels\\\":[\\\"攻击类型\\\",\\\"攻击源\\\",\\\"时间\\\"],\\\"json_path\\\":[\\\"$.data[:].type\\\",\\\"$.data[:].source\\\",\\\"$.data[:].time\\\"]}}     ```      转义前：      ```json     {         \"index\":\"index_xxx_*\",         \"dsl\":\"{\\\"query\\\":{\\\"match_all\\\":{}}}\",         \"response_parser\":{             \"labels\":[                 \"攻击类型\",                 \"攻击源\",                 \"时间\"             ],             \"json_path\":[                 \"$.data[:].type\",                 \"$.data[:].source\",                 \"$.data[:].time\"             ]         }     }     ``` - query_type为`sql`时，指定opendistro sql插件查询json(转义成字符串)   样例：     ```    {\\\"query\\\":\\\"SELECT count(1) as count , msg.DstPort FROM isap_log_nip_ttl* where oct >= TIMESTAMP(\\\\\\\"${date_from}\\\\\\\") and oct <= TIMESTAMP(\\\\\\\"${date_to}\\\\\\\") group by msg.DstPort order by count desc limit 5\\\"}     ```           转义前：      ```json     {         \"query\":\"SELECT count(1) as count , msg.DstPort FROM isap_log_nip_ttl* where oct >= TIMESTAMP(\\\"${date_from}\\\") and oct <= TIMESTAMP(\\\"${date_to}\\\") group by msg.DstPort order by count desc limit 5\"     }     ```

        :return: The query_function of this MetricMetaDataDerivedMetrics.
        :rtype: str
        """
        return self._query_function

    @query_function.setter
    def query_function(self, query_function):
        r"""Sets the query_function of this MetricMetaDataDerivedMetrics.

        获取指标结果的方法，转义成字符串, 共四种query方式：CBSL、API、DSL、SQL - query_type为`CBSL`时，function传入dataspace_id，pipe_id，query，sort, from, to   样例：     ```     {\\\"dataspace_id\\\":\\\"3939573a-12a0-436f-b0e5-ab2872a1fde9\\\",\\\"pipe_id\\\":\\\"9db9d8a6-d9e6-4b32-990e-40f0afe4655d\\\",\\\"query\\\":\\\"* | select ack_pps, device_type as type\\\",\\\"sort\\\":\\\"desc\\\",\\\"from\\\":${date_from},\\\"to\\\":${date_to}}     ```      转义前：     ```json     {         \"dataspace_id\":\"3939573a-12a0-436f-b0e5-ab2872a1fde9\",         \"pipe_id\":\"9db9d8a6-d9e6-4b32-990e-40f0afe4655d\",         \"query\":\"* | select ack_pps, device_type as type\",         \"sort\":\"desc\",         \"from\": ${date_from},         \"to\": ${date_to}     }     ``` - query_type为`API`时，function传入api method、url、path_params、headers、response_parser（解析API返回值所需，定义label和json_path将返回值解析为二维表格，label为表头，json_path为字段提取路径）   样例：     ```     {\\\"method\\\":\\\"POST\\\",\\\"uri\\\":\\\"/v1/${project_id}/只填写uri/不带域名/xxx\\\",\\\"headers\\\":{\\\"X-Auth-Token\\\":\\\"${project_token}\\\"},\\\"response_parser\\\":{\\\"labels\\\":[\\\"攻击类型\\\",\\\"攻击源\\\",\\\"时间\\\"],\\\"json_path\\\":[\\\"$.data[:].type\\\",\\\"$.data[:].source\\\",\\\"$.data[:].time\\\"]}}     ```      转义前：     ```json     {         \"method\":\"POST\",         \"uri\":\"/v1/${project_id}/只填写uri/不带域名/xxx\",         \"headers\":{             \"X-Auth-Token\": \"${project_token}\"         },         \"response_parser\":{             \"labels\":[                 \"攻击类型\",                 \"攻击源\",                 \"时间\"             ],             \"json_path\":[                 \"$.data[:].type\",                 \"$.data[:].source\",                 \"$.data[:].time\"             ]         }     }     ``` - query_type为`DSL`时，指定index, dsl(转义成字符串), response_parser   样例：     ```     {\\\"index\\\":\\\"index_xxx_*\\\",\\\"dsl\\\":\\\"{\\\\\\\"query\\\\\\\":{\\\\\\\"match_all\\\\\\\":{}}}\\\",\\\"response_parser\\\":{\\\"labels\\\":[\\\"攻击类型\\\",\\\"攻击源\\\",\\\"时间\\\"],\\\"json_path\\\":[\\\"$.data[:].type\\\",\\\"$.data[:].source\\\",\\\"$.data[:].time\\\"]}}     ```      转义前：      ```json     {         \"index\":\"index_xxx_*\",         \"dsl\":\"{\\\"query\\\":{\\\"match_all\\\":{}}}\",         \"response_parser\":{             \"labels\":[                 \"攻击类型\",                 \"攻击源\",                 \"时间\"             ],             \"json_path\":[                 \"$.data[:].type\",                 \"$.data[:].source\",                 \"$.data[:].time\"             ]         }     }     ``` - query_type为`sql`时，指定opendistro sql插件查询json(转义成字符串)   样例：     ```    {\\\"query\\\":\\\"SELECT count(1) as count , msg.DstPort FROM isap_log_nip_ttl* where oct >= TIMESTAMP(\\\\\\\"${date_from}\\\\\\\") and oct <= TIMESTAMP(\\\\\\\"${date_to}\\\\\\\") group by msg.DstPort order by count desc limit 5\\\"}     ```           转义前：      ```json     {         \"query\":\"SELECT count(1) as count , msg.DstPort FROM isap_log_nip_ttl* where oct >= TIMESTAMP(\\\"${date_from}\\\") and oct <= TIMESTAMP(\\\"${date_to}\\\") group by msg.DstPort order by count desc limit 5\"     }     ```

        :param query_function: The query_function of this MetricMetaDataDerivedMetrics.
        :type query_function: str
        """
        self._query_function = query_function

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
        if not isinstance(other, MetricMetaDataDerivedMetrics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
