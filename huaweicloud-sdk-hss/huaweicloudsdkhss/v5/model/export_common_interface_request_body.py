# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportCommonInterfaceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'export_type': 'str',
        'condition': 'str',
        'id_list': 'list[str]'
    }

    attribute_map = {
        'export_type': 'export_type',
        'condition': 'condition',
        'id_list': 'id_list'
    }

    def __init__(self, export_type=None, condition=None, id_list=None):
        r"""ExportCommonInterfaceRequestBody

        The model defined in huaweicloud sdk

        :param export_type: **参数解释**： 导出类型 **约束限制**: 不涉及 **取值范围**： 导出类型，取值为对应的查询接口的接口名。 - ListAntiVirusResult：病毒扫描结果列表导出。 - ListAntivirusHandleHistory：病毒扫描历史处置记录列表。 - ListAiInstances：AI实例记录列表。 - ListAiSessions：AI会话记录列表。 - ListAiTraceRiskDetail：AI行为轨迹风险详情列表。 - ListDefenderPlugins：智能体卫士插件列表。 - ListEventHandleHistory：告警事件历史处置记录列表。  **默认取值**: 不涉及
        :type export_type: str
        :param condition: **参数解释**: 查询条件信息，把对应的json转化成字符串，举例如下：当export_type&#x3D;ListAntiVirusResult，传递查询条件为：{\&quot;severities\&quot;:\&quot;Critical\&quot;,\&quot;handle_status\&quot;:\&quot;unhandled\&quot;,\&quot;asset_value\&quot;:\&quot;important\&quot;}，查询条件信息可以通过对应的查询接口获取。 **约束限制**: 不涉及 **取值范围**: 字符长度1-5000位 **默认取值**: 不涉及 
        :type condition: str
        :param id_list: 导出的数据的Id列表, 当id_list有值时，会忽略condition的信息: - export_type &#x3D; ListAiInstances时对应的是agent_id - export_type &#x3D; ListAiSessions时对应的是session_id - export_type &#x3D; ListAiTraceRiskDetail时对应的是规则详情记录id - export_type &#x3D; ListDefenderPlugins时对应的是instance_id 
        :type id_list: list[str]
        """
        
        

        self._export_type = None
        self._condition = None
        self._id_list = None
        self.discriminator = None

        self.export_type = export_type
        if condition is not None:
            self.condition = condition
        if id_list is not None:
            self.id_list = id_list

    @property
    def export_type(self):
        r"""Gets the export_type of this ExportCommonInterfaceRequestBody.

        **参数解释**： 导出类型 **约束限制**: 不涉及 **取值范围**： 导出类型，取值为对应的查询接口的接口名。 - ListAntiVirusResult：病毒扫描结果列表导出。 - ListAntivirusHandleHistory：病毒扫描历史处置记录列表。 - ListAiInstances：AI实例记录列表。 - ListAiSessions：AI会话记录列表。 - ListAiTraceRiskDetail：AI行为轨迹风险详情列表。 - ListDefenderPlugins：智能体卫士插件列表。 - ListEventHandleHistory：告警事件历史处置记录列表。  **默认取值**: 不涉及

        :return: The export_type of this ExportCommonInterfaceRequestBody.
        :rtype: str
        """
        return self._export_type

    @export_type.setter
    def export_type(self, export_type):
        r"""Sets the export_type of this ExportCommonInterfaceRequestBody.

        **参数解释**： 导出类型 **约束限制**: 不涉及 **取值范围**： 导出类型，取值为对应的查询接口的接口名。 - ListAntiVirusResult：病毒扫描结果列表导出。 - ListAntivirusHandleHistory：病毒扫描历史处置记录列表。 - ListAiInstances：AI实例记录列表。 - ListAiSessions：AI会话记录列表。 - ListAiTraceRiskDetail：AI行为轨迹风险详情列表。 - ListDefenderPlugins：智能体卫士插件列表。 - ListEventHandleHistory：告警事件历史处置记录列表。  **默认取值**: 不涉及

        :param export_type: The export_type of this ExportCommonInterfaceRequestBody.
        :type export_type: str
        """
        self._export_type = export_type

    @property
    def condition(self):
        r"""Gets the condition of this ExportCommonInterfaceRequestBody.

        **参数解释**: 查询条件信息，把对应的json转化成字符串，举例如下：当export_type=ListAntiVirusResult，传递查询条件为：{\"severities\":\"Critical\",\"handle_status\":\"unhandled\",\"asset_value\":\"important\"}，查询条件信息可以通过对应的查询接口获取。 **约束限制**: 不涉及 **取值范围**: 字符长度1-5000位 **默认取值**: 不涉及 

        :return: The condition of this ExportCommonInterfaceRequestBody.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        r"""Sets the condition of this ExportCommonInterfaceRequestBody.

        **参数解释**: 查询条件信息，把对应的json转化成字符串，举例如下：当export_type=ListAntiVirusResult，传递查询条件为：{\"severities\":\"Critical\",\"handle_status\":\"unhandled\",\"asset_value\":\"important\"}，查询条件信息可以通过对应的查询接口获取。 **约束限制**: 不涉及 **取值范围**: 字符长度1-5000位 **默认取值**: 不涉及 

        :param condition: The condition of this ExportCommonInterfaceRequestBody.
        :type condition: str
        """
        self._condition = condition

    @property
    def id_list(self):
        r"""Gets the id_list of this ExportCommonInterfaceRequestBody.

        导出的数据的Id列表, 当id_list有值时，会忽略condition的信息: - export_type = ListAiInstances时对应的是agent_id - export_type = ListAiSessions时对应的是session_id - export_type = ListAiTraceRiskDetail时对应的是规则详情记录id - export_type = ListDefenderPlugins时对应的是instance_id 

        :return: The id_list of this ExportCommonInterfaceRequestBody.
        :rtype: list[str]
        """
        return self._id_list

    @id_list.setter
    def id_list(self, id_list):
        r"""Sets the id_list of this ExportCommonInterfaceRequestBody.

        导出的数据的Id列表, 当id_list有值时，会忽略condition的信息: - export_type = ListAiInstances时对应的是agent_id - export_type = ListAiSessions时对应的是session_id - export_type = ListAiTraceRiskDetail时对应的是规则详情记录id - export_type = ListDefenderPlugins时对应的是instance_id 

        :param id_list: The id_list of this ExportCommonInterfaceRequestBody.
        :type id_list: list[str]
        """
        self._id_list = id_list

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
        if not isinstance(other, ExportCommonInterfaceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
