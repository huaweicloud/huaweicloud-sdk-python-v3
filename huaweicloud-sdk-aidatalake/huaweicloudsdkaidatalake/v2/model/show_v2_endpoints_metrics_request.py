# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowV2EndpointsMetricsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace_id': 'str',
        'step': 'int',
        'metric_name': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'endpoint_id': 'str'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'step': 'step',
        'metric_name': 'metric_name',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'endpoint_id': 'endpoint_id'
    }

    def __init__(self, workspace_id=None, step=None, metric_name=None, start_time=None, end_time=None, endpoint_id=None):
        r"""ShowV2EndpointsMetricsRequest

        The model defined in huaweicloud sdk

        :param workspace_id: **参数解释**：**参数解释**：工作空间ID，可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。  **取值范围**：长度为32-36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。
        :type workspace_id: str
        :param step: **参数解释**：查询时间步长。 **约束限制**：不涉及。 **取值范围**：单位秒。   - 60：每分钟一个点。   - 3600：每1小时一个点。   - 86400：每天一个点。 **默认取值**：60。 
        :type step: int
        :param metric_name: **参数解释**：指标名称，可以取值多个，多个值用逗号分隔。 **约束限制**：   - aura_job：[[端点监控指标](https://support.huaweicloud.com/usermanual-aidatalake/aidatalake_01_0075.html)](tag:HEC)[[端点监控指标](https://support.huaweicloud.com/intl/zh-cn/usermanual-aidatalake/aidatalake_01_0075.html)](tag:hws_hk)。   - spark（SPARK_JOB / SPARK_SQL）：[[端点监控指标](https://support.huaweicloud.com/usermanual-aidatalake/aidatalake_01_0067.html)](tag:HEC)[[端点监控指标](https://support.huaweicloud.com/intl/zh-cn/usermanual-aidatalake/aidatalake_01_0067.html)](tag:hws_hk)。 **取值范围**：不涉及。 **默认取值**：不涉及。 
        :type metric_name: str
        :param start_time: **参数解释**：开始时间。 **约束限制**：不涉及。 **取值范围**：时间戳，单位秒。 **默认取值**：不涉及。 
        :type start_time: int
        :param end_time: **参数解释**：结束时间。 **约束限制**：不涉及。 **取值范围**：时间戳，单位秒。 **默认取值**：不涉及。 
        :type end_time: int
        :param endpoint_id: **参数解释**：端点ID，可通过[查询端点列表](ListV2Endpoints.xml)获取端点ID。 **约束限制**：不涉及。  **取值范围**：长度为32-36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。
        :type endpoint_id: str
        """
        
        

        self._workspace_id = None
        self._step = None
        self._metric_name = None
        self._start_time = None
        self._end_time = None
        self._endpoint_id = None
        self.discriminator = None

        self.workspace_id = workspace_id
        self.step = step
        self.metric_name = metric_name
        self.start_time = start_time
        self.end_time = end_time
        self.endpoint_id = endpoint_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ShowV2EndpointsMetricsRequest.

        **参数解释**：**参数解释**：工作空间ID，可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。  **取值范围**：长度为32-36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :return: The workspace_id of this ShowV2EndpointsMetricsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ShowV2EndpointsMetricsRequest.

        **参数解释**：**参数解释**：工作空间ID，可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。  **取值范围**：长度为32-36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :param workspace_id: The workspace_id of this ShowV2EndpointsMetricsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def step(self):
        r"""Gets the step of this ShowV2EndpointsMetricsRequest.

        **参数解释**：查询时间步长。 **约束限制**：不涉及。 **取值范围**：单位秒。   - 60：每分钟一个点。   - 3600：每1小时一个点。   - 86400：每天一个点。 **默认取值**：60。 

        :return: The step of this ShowV2EndpointsMetricsRequest.
        :rtype: int
        """
        return self._step

    @step.setter
    def step(self, step):
        r"""Sets the step of this ShowV2EndpointsMetricsRequest.

        **参数解释**：查询时间步长。 **约束限制**：不涉及。 **取值范围**：单位秒。   - 60：每分钟一个点。   - 3600：每1小时一个点。   - 86400：每天一个点。 **默认取值**：60。 

        :param step: The step of this ShowV2EndpointsMetricsRequest.
        :type step: int
        """
        self._step = step

    @property
    def metric_name(self):
        r"""Gets the metric_name of this ShowV2EndpointsMetricsRequest.

        **参数解释**：指标名称，可以取值多个，多个值用逗号分隔。 **约束限制**：   - aura_job：[[端点监控指标](https://support.huaweicloud.com/usermanual-aidatalake/aidatalake_01_0075.html)](tag:HEC)[[端点监控指标](https://support.huaweicloud.com/intl/zh-cn/usermanual-aidatalake/aidatalake_01_0075.html)](tag:hws_hk)。   - spark（SPARK_JOB / SPARK_SQL）：[[端点监控指标](https://support.huaweicloud.com/usermanual-aidatalake/aidatalake_01_0067.html)](tag:HEC)[[端点监控指标](https://support.huaweicloud.com/intl/zh-cn/usermanual-aidatalake/aidatalake_01_0067.html)](tag:hws_hk)。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :return: The metric_name of this ShowV2EndpointsMetricsRequest.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this ShowV2EndpointsMetricsRequest.

        **参数解释**：指标名称，可以取值多个，多个值用逗号分隔。 **约束限制**：   - aura_job：[[端点监控指标](https://support.huaweicloud.com/usermanual-aidatalake/aidatalake_01_0075.html)](tag:HEC)[[端点监控指标](https://support.huaweicloud.com/intl/zh-cn/usermanual-aidatalake/aidatalake_01_0075.html)](tag:hws_hk)。   - spark（SPARK_JOB / SPARK_SQL）：[[端点监控指标](https://support.huaweicloud.com/usermanual-aidatalake/aidatalake_01_0067.html)](tag:HEC)[[端点监控指标](https://support.huaweicloud.com/intl/zh-cn/usermanual-aidatalake/aidatalake_01_0067.html)](tag:hws_hk)。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :param metric_name: The metric_name of this ShowV2EndpointsMetricsRequest.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowV2EndpointsMetricsRequest.

        **参数解释**：开始时间。 **约束限制**：不涉及。 **取值范围**：时间戳，单位秒。 **默认取值**：不涉及。 

        :return: The start_time of this ShowV2EndpointsMetricsRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowV2EndpointsMetricsRequest.

        **参数解释**：开始时间。 **约束限制**：不涉及。 **取值范围**：时间戳，单位秒。 **默认取值**：不涉及。 

        :param start_time: The start_time of this ShowV2EndpointsMetricsRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowV2EndpointsMetricsRequest.

        **参数解释**：结束时间。 **约束限制**：不涉及。 **取值范围**：时间戳，单位秒。 **默认取值**：不涉及。 

        :return: The end_time of this ShowV2EndpointsMetricsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowV2EndpointsMetricsRequest.

        **参数解释**：结束时间。 **约束限制**：不涉及。 **取值范围**：时间戳，单位秒。 **默认取值**：不涉及。 

        :param end_time: The end_time of this ShowV2EndpointsMetricsRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def endpoint_id(self):
        r"""Gets the endpoint_id of this ShowV2EndpointsMetricsRequest.

        **参数解释**：端点ID，可通过[查询端点列表](ListV2Endpoints.xml)获取端点ID。 **约束限制**：不涉及。  **取值范围**：长度为32-36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :return: The endpoint_id of this ShowV2EndpointsMetricsRequest.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        r"""Sets the endpoint_id of this ShowV2EndpointsMetricsRequest.

        **参数解释**：端点ID，可通过[查询端点列表](ListV2Endpoints.xml)获取端点ID。 **约束限制**：不涉及。  **取值范围**：长度为32-36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :param endpoint_id: The endpoint_id of this ShowV2EndpointsMetricsRequest.
        :type endpoint_id: str
        """
        self._endpoint_id = endpoint_id

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
        if not isinstance(other, ShowV2EndpointsMetricsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
