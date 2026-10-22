# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class V2EndpointMetric:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric_name': 'str',
        'metric_value': 'float'
    }

    attribute_map = {
        'metric_name': 'metric_name',
        'metric_value': 'metric_value'
    }

    def __init__(self, metric_name=None, metric_value=None):
        r"""V2EndpointMetric

        The model defined in huaweicloud sdk

        :param metric_name: **参数解释**：指标名称。 **取值范围**：监控指标与端点引擎类型相关，具体支持的指标如下：   - aura_job类型端点支持的指标参见：[[端点监控指标](https://support.huaweicloud.com/usermanual-aidatalake/aidatalake_01_0075.html)](tag:HEC)[[端点监控指标](https://support.huaweicloud.com/intl/zh-cn/usermanual-aidatalake/aidatalake_01_0075.html)](tag:hws_hk)。   - spark（SPARK_JOB / SPARK_SQL）类型端点支持的指标参见：[[端点监控指标](https://support.huaweicloud.com/usermanual-aidatalake/aidatalake_01_0067.html)](tag:HEC)[[端点监控指标](https://support.huaweicloud.com/intl/zh-cn/usermanual-aidatalake/aidatalake_01_0067.html)](tag:hws_hk)。 
        :type metric_name: str
        :param metric_value: **参数解释**：指标值。 **取值范围**：不涉及。 
        :type metric_value: float
        """
        
        

        self._metric_name = None
        self._metric_value = None
        self.discriminator = None

        if metric_name is not None:
            self.metric_name = metric_name
        if metric_value is not None:
            self.metric_value = metric_value

    @property
    def metric_name(self):
        r"""Gets the metric_name of this V2EndpointMetric.

        **参数解释**：指标名称。 **取值范围**：监控指标与端点引擎类型相关，具体支持的指标如下：   - aura_job类型端点支持的指标参见：[[端点监控指标](https://support.huaweicloud.com/usermanual-aidatalake/aidatalake_01_0075.html)](tag:HEC)[[端点监控指标](https://support.huaweicloud.com/intl/zh-cn/usermanual-aidatalake/aidatalake_01_0075.html)](tag:hws_hk)。   - spark（SPARK_JOB / SPARK_SQL）类型端点支持的指标参见：[[端点监控指标](https://support.huaweicloud.com/usermanual-aidatalake/aidatalake_01_0067.html)](tag:HEC)[[端点监控指标](https://support.huaweicloud.com/intl/zh-cn/usermanual-aidatalake/aidatalake_01_0067.html)](tag:hws_hk)。 

        :return: The metric_name of this V2EndpointMetric.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this V2EndpointMetric.

        **参数解释**：指标名称。 **取值范围**：监控指标与端点引擎类型相关，具体支持的指标如下：   - aura_job类型端点支持的指标参见：[[端点监控指标](https://support.huaweicloud.com/usermanual-aidatalake/aidatalake_01_0075.html)](tag:HEC)[[端点监控指标](https://support.huaweicloud.com/intl/zh-cn/usermanual-aidatalake/aidatalake_01_0075.html)](tag:hws_hk)。   - spark（SPARK_JOB / SPARK_SQL）类型端点支持的指标参见：[[端点监控指标](https://support.huaweicloud.com/usermanual-aidatalake/aidatalake_01_0067.html)](tag:HEC)[[端点监控指标](https://support.huaweicloud.com/intl/zh-cn/usermanual-aidatalake/aidatalake_01_0067.html)](tag:hws_hk)。 

        :param metric_name: The metric_name of this V2EndpointMetric.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def metric_value(self):
        r"""Gets the metric_value of this V2EndpointMetric.

        **参数解释**：指标值。 **取值范围**：不涉及。 

        :return: The metric_value of this V2EndpointMetric.
        :rtype: float
        """
        return self._metric_value

    @metric_value.setter
    def metric_value(self, metric_value):
        r"""Sets the metric_value of this V2EndpointMetric.

        **参数解释**：指标值。 **取值范围**：不涉及。 

        :param metric_value: The metric_value of this V2EndpointMetric.
        :type metric_value: float
        """
        self._metric_value = metric_value

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
        if not isinstance(other, V2EndpointMetric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
