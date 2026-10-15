# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFlinkResourceConfigResponseBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parallelism': 'int',
        'jobmanager_resource_spec': 'ShowFlinkResourceSpecResponseBody',
        'taskmanager_resource_spec': 'ShowFlinkResourceSpecResponseBody',
        'sql_gateway_resource_spec': 'ShowFlinkSqlGatewayResourceSpecResponseBody'
    }

    attribute_map = {
        'parallelism': 'parallelism',
        'jobmanager_resource_spec': 'jobmanager_resource_spec',
        'taskmanager_resource_spec': 'taskmanager_resource_spec',
        'sql_gateway_resource_spec': 'sql_gateway_resource_spec'
    }

    def __init__(self, parallelism=None, jobmanager_resource_spec=None, taskmanager_resource_spec=None, sql_gateway_resource_spec=None):
        r"""ShowFlinkResourceConfigResponseBody

        The model defined in huaweicloud sdk

        :param parallelism: **参数解释**：作业并行度。 **取值范围**：1~1000。
        :type parallelism: int
        :param jobmanager_resource_spec: 
        :type jobmanager_resource_spec: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkResourceSpecResponseBody`
        :param taskmanager_resource_spec: 
        :type taskmanager_resource_spec: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkResourceSpecResponseBody`
        :param sql_gateway_resource_spec: 
        :type sql_gateway_resource_spec: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkSqlGatewayResourceSpecResponseBody`
        """
        
        

        self._parallelism = None
        self._jobmanager_resource_spec = None
        self._taskmanager_resource_spec = None
        self._sql_gateway_resource_spec = None
        self.discriminator = None

        self.parallelism = parallelism
        self.jobmanager_resource_spec = jobmanager_resource_spec
        self.taskmanager_resource_spec = taskmanager_resource_spec
        if sql_gateway_resource_spec is not None:
            self.sql_gateway_resource_spec = sql_gateway_resource_spec

    @property
    def parallelism(self):
        r"""Gets the parallelism of this ShowFlinkResourceConfigResponseBody.

        **参数解释**：作业并行度。 **取值范围**：1~1000。

        :return: The parallelism of this ShowFlinkResourceConfigResponseBody.
        :rtype: int
        """
        return self._parallelism

    @parallelism.setter
    def parallelism(self, parallelism):
        r"""Sets the parallelism of this ShowFlinkResourceConfigResponseBody.

        **参数解释**：作业并行度。 **取值范围**：1~1000。

        :param parallelism: The parallelism of this ShowFlinkResourceConfigResponseBody.
        :type parallelism: int
        """
        self._parallelism = parallelism

    @property
    def jobmanager_resource_spec(self):
        r"""Gets the jobmanager_resource_spec of this ShowFlinkResourceConfigResponseBody.

        :return: The jobmanager_resource_spec of this ShowFlinkResourceConfigResponseBody.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkResourceSpecResponseBody`
        """
        return self._jobmanager_resource_spec

    @jobmanager_resource_spec.setter
    def jobmanager_resource_spec(self, jobmanager_resource_spec):
        r"""Sets the jobmanager_resource_spec of this ShowFlinkResourceConfigResponseBody.

        :param jobmanager_resource_spec: The jobmanager_resource_spec of this ShowFlinkResourceConfigResponseBody.
        :type jobmanager_resource_spec: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkResourceSpecResponseBody`
        """
        self._jobmanager_resource_spec = jobmanager_resource_spec

    @property
    def taskmanager_resource_spec(self):
        r"""Gets the taskmanager_resource_spec of this ShowFlinkResourceConfigResponseBody.

        :return: The taskmanager_resource_spec of this ShowFlinkResourceConfigResponseBody.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkResourceSpecResponseBody`
        """
        return self._taskmanager_resource_spec

    @taskmanager_resource_spec.setter
    def taskmanager_resource_spec(self, taskmanager_resource_spec):
        r"""Sets the taskmanager_resource_spec of this ShowFlinkResourceConfigResponseBody.

        :param taskmanager_resource_spec: The taskmanager_resource_spec of this ShowFlinkResourceConfigResponseBody.
        :type taskmanager_resource_spec: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkResourceSpecResponseBody`
        """
        self._taskmanager_resource_spec = taskmanager_resource_spec

    @property
    def sql_gateway_resource_spec(self):
        r"""Gets the sql_gateway_resource_spec of this ShowFlinkResourceConfigResponseBody.

        :return: The sql_gateway_resource_spec of this ShowFlinkResourceConfigResponseBody.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkSqlGatewayResourceSpecResponseBody`
        """
        return self._sql_gateway_resource_spec

    @sql_gateway_resource_spec.setter
    def sql_gateway_resource_spec(self, sql_gateway_resource_spec):
        r"""Sets the sql_gateway_resource_spec of this ShowFlinkResourceConfigResponseBody.

        :param sql_gateway_resource_spec: The sql_gateway_resource_spec of this ShowFlinkResourceConfigResponseBody.
        :type sql_gateway_resource_spec: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkSqlGatewayResourceSpecResponseBody`
        """
        self._sql_gateway_resource_spec = sql_gateway_resource_spec

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
        if not isinstance(other, ShowFlinkResourceConfigResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
