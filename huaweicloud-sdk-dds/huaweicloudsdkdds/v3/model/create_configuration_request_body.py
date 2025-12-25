# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateConfigurationRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'parameter_values': 'dict(str, str)',
        'datastore': 'DatastoreResult',
        'entity_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'parameter_values': 'parameter_values',
        'datastore': 'datastore',
        'entity_id': 'entity_id'
    }

    def __init__(self, name=None, description=None, parameter_values=None, datastore=None, entity_id=None):
        r"""CreateConfigurationRequestBody

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 参数模板名称。 **约束限制：** 长度1到64位之间，区分大小写字母，可包含字母、数字、中划线、下划线或句点，不能包含其他特殊字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type name: str
        :param description: **参数解释：** 参数模板描述。 **约束限制：** 长度不超过256位，且不能包含回车和&gt;!&lt;\&quot;&amp;&#39;&#x3D;特殊字符。 **取值范围：** 不涉及。 **默认取值：** 默认为空。
        :type description: str
        :param parameter_values: **参数解释：** 参数名和参数值映射关系。用户可以基于默认参数模板的参数，自定义的参数值。 **约束限制：** 当未传入entity_id参数时，此参数必选。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type parameter_values: dict(str, str)
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkdds.v3.DatastoreResult`
        :param entity_id: **参数解释：** 实例ID或组ID或节点ID。可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。 若传入此参数，则会基于此实例、组或节点的参数信息创建参数模板，将会忽略parameter_values和datastore传参。 **约束限制：** 不涉及。 **取值范围：** 当实例类型是集群，取值为shard组或config组的组ID、mongos节点的节点ID、只读节点的节点ID。 当实例类型是副本集，传值为实例ID或只读节点的节点ID。 当实例类型是单节点，传值为实例ID。 **默认取值：** 不涉及。
        :type entity_id: str
        """
        
        

        self._name = None
        self._description = None
        self._parameter_values = None
        self._datastore = None
        self._entity_id = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if parameter_values is not None:
            self.parameter_values = parameter_values
        if datastore is not None:
            self.datastore = datastore
        if entity_id is not None:
            self.entity_id = entity_id

    @property
    def name(self):
        r"""Gets the name of this CreateConfigurationRequestBody.

        **参数解释：** 参数模板名称。 **约束限制：** 长度1到64位之间，区分大小写字母，可包含字母、数字、中划线、下划线或句点，不能包含其他特殊字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The name of this CreateConfigurationRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateConfigurationRequestBody.

        **参数解释：** 参数模板名称。 **约束限制：** 长度1到64位之间，区分大小写字母，可包含字母、数字、中划线、下划线或句点，不能包含其他特殊字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param name: The name of this CreateConfigurationRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateConfigurationRequestBody.

        **参数解释：** 参数模板描述。 **约束限制：** 长度不超过256位，且不能包含回车和>!<\"&'=特殊字符。 **取值范围：** 不涉及。 **默认取值：** 默认为空。

        :return: The description of this CreateConfigurationRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateConfigurationRequestBody.

        **参数解释：** 参数模板描述。 **约束限制：** 长度不超过256位，且不能包含回车和>!<\"&'=特殊字符。 **取值范围：** 不涉及。 **默认取值：** 默认为空。

        :param description: The description of this CreateConfigurationRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def parameter_values(self):
        r"""Gets the parameter_values of this CreateConfigurationRequestBody.

        **参数解释：** 参数名和参数值映射关系。用户可以基于默认参数模板的参数，自定义的参数值。 **约束限制：** 当未传入entity_id参数时，此参数必选。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The parameter_values of this CreateConfigurationRequestBody.
        :rtype: dict(str, str)
        """
        return self._parameter_values

    @parameter_values.setter
    def parameter_values(self, parameter_values):
        r"""Sets the parameter_values of this CreateConfigurationRequestBody.

        **参数解释：** 参数名和参数值映射关系。用户可以基于默认参数模板的参数，自定义的参数值。 **约束限制：** 当未传入entity_id参数时，此参数必选。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param parameter_values: The parameter_values of this CreateConfigurationRequestBody.
        :type parameter_values: dict(str, str)
        """
        self._parameter_values = parameter_values

    @property
    def datastore(self):
        r"""Gets the datastore of this CreateConfigurationRequestBody.

        :return: The datastore of this CreateConfigurationRequestBody.
        :rtype: :class:`huaweicloudsdkdds.v3.DatastoreResult`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        r"""Sets the datastore of this CreateConfigurationRequestBody.

        :param datastore: The datastore of this CreateConfigurationRequestBody.
        :type datastore: :class:`huaweicloudsdkdds.v3.DatastoreResult`
        """
        self._datastore = datastore

    @property
    def entity_id(self):
        r"""Gets the entity_id of this CreateConfigurationRequestBody.

        **参数解释：** 实例ID或组ID或节点ID。可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。 若传入此参数，则会基于此实例、组或节点的参数信息创建参数模板，将会忽略parameter_values和datastore传参。 **约束限制：** 不涉及。 **取值范围：** 当实例类型是集群，取值为shard组或config组的组ID、mongos节点的节点ID、只读节点的节点ID。 当实例类型是副本集，传值为实例ID或只读节点的节点ID。 当实例类型是单节点，传值为实例ID。 **默认取值：** 不涉及。

        :return: The entity_id of this CreateConfigurationRequestBody.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        r"""Sets the entity_id of this CreateConfigurationRequestBody.

        **参数解释：** 实例ID或组ID或节点ID。可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。 若传入此参数，则会基于此实例、组或节点的参数信息创建参数模板，将会忽略parameter_values和datastore传参。 **约束限制：** 不涉及。 **取值范围：** 当实例类型是集群，取值为shard组或config组的组ID、mongos节点的节点ID、只读节点的节点ID。 当实例类型是副本集，传值为实例ID或只读节点的节点ID。 当实例类型是单节点，传值为实例ID。 **默认取值：** 不涉及。

        :param entity_id: The entity_id of this CreateConfigurationRequestBody.
        :type entity_id: str
        """
        self._entity_id = entity_id

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
        if not isinstance(other, CreateConfigurationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
