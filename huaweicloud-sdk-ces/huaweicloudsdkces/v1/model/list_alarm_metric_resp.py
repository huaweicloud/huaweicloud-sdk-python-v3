# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlarmMetricResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'namespace': 'str',
        'dimensions': 'list[DimensionResp]',
        'metric_name': 'str',
        'resource_group_id': 'str',
        'resource_group_name': 'str'
    }

    attribute_map = {
        'namespace': 'namespace',
        'dimensions': 'dimensions',
        'metric_name': 'metric_name',
        'resource_group_id': 'resource_group_id',
        'resource_group_name': 'resource_group_name'
    }

    def __init__(self, namespace=None, dimensions=None, metric_name=None, resource_group_id=None, resource_group_name=None):
        r"""ListAlarmMetricResp

        The model defined in huaweicloud sdk

        :param namespace: **参数解释**： 服务指标命名空间。如：弹性云服务器的命名空间为SYS.ECS，文档数据库的命名空间为SYS.DDS，各服务的命名空间可查看：“[服务命名空间](ces_03_0059.xml)”。 **取值范围**： 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_，字符总长度最短为3，最大为32。 
        :type namespace: str
        :param dimensions: **参数解释**： 指标维度，目前最大为4个维度。 
        :type dimensions: list[:class:`huaweicloudsdkces.v1.DimensionResp`]
        :param metric_name: **参数解释**： 资源的监控指标名称。如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率；各服务的指标名称可查看：“[服务指标名称](ces_03_0059.xml)”。 **取值范围**： 必须以字母开头，只能包含0-9/a-z/A-Z/_，长度为[1,96]个字符。 
        :type metric_name: str
        :param resource_group_id: **参数解释**： 创建告警规则时选择的资源分组ID，如：rg1603786526428bWbVmk4rP **取值范围**： 只能包含字母、数字、“-”、“_”，字符长度为[1,64] 
        :type resource_group_id: str
        :param resource_group_name: **参数解释**： 创建告警规则时选择的资源分组名称，如：Resource-Group-ECS-01 **取值范围**： 字符长度为[0,128] 
        :type resource_group_name: str
        """
        
        

        self._namespace = None
        self._dimensions = None
        self._metric_name = None
        self._resource_group_id = None
        self._resource_group_name = None
        self.discriminator = None

        if namespace is not None:
            self.namespace = namespace
        if dimensions is not None:
            self.dimensions = dimensions
        if metric_name is not None:
            self.metric_name = metric_name
        if resource_group_id is not None:
            self.resource_group_id = resource_group_id
        if resource_group_name is not None:
            self.resource_group_name = resource_group_name

    @property
    def namespace(self):
        r"""Gets the namespace of this ListAlarmMetricResp.

        **参数解释**： 服务指标命名空间。如：弹性云服务器的命名空间为SYS.ECS，文档数据库的命名空间为SYS.DDS，各服务的命名空间可查看：“[服务命名空间](ces_03_0059.xml)”。 **取值范围**： 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_，字符总长度最短为3，最大为32。 

        :return: The namespace of this ListAlarmMetricResp.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ListAlarmMetricResp.

        **参数解释**： 服务指标命名空间。如：弹性云服务器的命名空间为SYS.ECS，文档数据库的命名空间为SYS.DDS，各服务的命名空间可查看：“[服务命名空间](ces_03_0059.xml)”。 **取值范围**： 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_，字符总长度最短为3，最大为32。 

        :param namespace: The namespace of this ListAlarmMetricResp.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def dimensions(self):
        r"""Gets the dimensions of this ListAlarmMetricResp.

        **参数解释**： 指标维度，目前最大为4个维度。 

        :return: The dimensions of this ListAlarmMetricResp.
        :rtype: list[:class:`huaweicloudsdkces.v1.DimensionResp`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        r"""Sets the dimensions of this ListAlarmMetricResp.

        **参数解释**： 指标维度，目前最大为4个维度。 

        :param dimensions: The dimensions of this ListAlarmMetricResp.
        :type dimensions: list[:class:`huaweicloudsdkces.v1.DimensionResp`]
        """
        self._dimensions = dimensions

    @property
    def metric_name(self):
        r"""Gets the metric_name of this ListAlarmMetricResp.

        **参数解释**： 资源的监控指标名称。如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率；各服务的指标名称可查看：“[服务指标名称](ces_03_0059.xml)”。 **取值范围**： 必须以字母开头，只能包含0-9/a-z/A-Z/_，长度为[1,96]个字符。 

        :return: The metric_name of this ListAlarmMetricResp.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this ListAlarmMetricResp.

        **参数解释**： 资源的监控指标名称。如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率；各服务的指标名称可查看：“[服务指标名称](ces_03_0059.xml)”。 **取值范围**： 必须以字母开头，只能包含0-9/a-z/A-Z/_，长度为[1,96]个字符。 

        :param metric_name: The metric_name of this ListAlarmMetricResp.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def resource_group_id(self):
        r"""Gets the resource_group_id of this ListAlarmMetricResp.

        **参数解释**： 创建告警规则时选择的资源分组ID，如：rg1603786526428bWbVmk4rP **取值范围**： 只能包含字母、数字、“-”、“_”，字符长度为[1,64] 

        :return: The resource_group_id of this ListAlarmMetricResp.
        :rtype: str
        """
        return self._resource_group_id

    @resource_group_id.setter
    def resource_group_id(self, resource_group_id):
        r"""Sets the resource_group_id of this ListAlarmMetricResp.

        **参数解释**： 创建告警规则时选择的资源分组ID，如：rg1603786526428bWbVmk4rP **取值范围**： 只能包含字母、数字、“-”、“_”，字符长度为[1,64] 

        :param resource_group_id: The resource_group_id of this ListAlarmMetricResp.
        :type resource_group_id: str
        """
        self._resource_group_id = resource_group_id

    @property
    def resource_group_name(self):
        r"""Gets the resource_group_name of this ListAlarmMetricResp.

        **参数解释**： 创建告警规则时选择的资源分组名称，如：Resource-Group-ECS-01 **取值范围**： 字符长度为[0,128] 

        :return: The resource_group_name of this ListAlarmMetricResp.
        :rtype: str
        """
        return self._resource_group_name

    @resource_group_name.setter
    def resource_group_name(self, resource_group_name):
        r"""Sets the resource_group_name of this ListAlarmMetricResp.

        **参数解释**： 创建告警规则时选择的资源分组名称，如：Resource-Group-ECS-01 **取值范围**： 字符长度为[0,128] 

        :param resource_group_name: The resource_group_name of this ListAlarmMetricResp.
        :type resource_group_name: str
        """
        self._resource_group_name = resource_group_name

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
        if not isinstance(other, ListAlarmMetricResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
