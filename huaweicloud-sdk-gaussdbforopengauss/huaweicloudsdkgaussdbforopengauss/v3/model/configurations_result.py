# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigurationsResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'datastore_version': 'str',
        'datastore_name': 'str',
        'node_type': 'str',
        'ha_mode': 'str',
        'created': 'str',
        'updated': 'str',
        'user_defined': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'datastore_version': 'datastore_version',
        'datastore_name': 'datastore_name',
        'node_type': 'node_type',
        'ha_mode': 'ha_mode',
        'created': 'created',
        'updated': 'updated',
        'user_defined': 'user_defined'
    }

    def __init__(self, id=None, name=None, description=None, datastore_version=None, datastore_name=None, node_type=None, ha_mode=None, created=None, updated=None, user_defined=None):
        r"""ConfigurationsResult

        The model defined in huaweicloud sdk

        :param id: **参数解释**: 参数模板ID。参数模板的唯一标识。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。
        :type id: str
        :param name: **参数解释**: 参数模板名称。 **取值范围**: 参数模板名称在1到64个字符之间，区分大小写，可包含字母、数字、英文中划线、下划线或句点，不能包含其他特殊字符。
        :type name: str
        :param description: **参数解释**: 参数模板描述。 **取值范围**: 描述不能超过256个字符，且不能包含回车和 ! &lt; \&quot; &#x3D; &#39; &gt; &amp;这些特殊字符。
        :type description: str
        :param datastore_version: **参数解释**: 引擎版本。 **取值范围**: 不涉及。
        :type datastore_version: str
        :param datastore_name: **参数解释**: 引擎名称。 **取值范围**: GaussDB。
        :type datastore_name: str
        :param node_type: **参数解释**: 节点类型。 **取值范围**: - independent：独立部署。 - ha：集中式。 - combined：混合部署。
        :type node_type: str
        :param ha_mode: **参数解释**: 实例类型。 **取值范围**: - Enterprise：分布式实例（企业版）。 - centralization_standard：集中式版实例。  区分大小写。
        :type ha_mode: str
        :param created: **参数解释**: 创建时间，格式为\&quot;yyyy-MM-ddTHH:mm:ssZ\&quot;。例如：2024-07-03T14:18:55。 **取值范围**: 不涉及。
        :type created: str
        :param updated: **参数解释**: 更新时间，格式为\&quot;yyyy-MM-ddTHH:mm:ssZ\&quot;。例如：2024-07-03T14:18:55。 **取值范围**: 不涉及。
        :type updated: str
        :param user_defined: **参数解释**: 是否是用户自定义参数模板。 **取值范围**: - false：表示为系统默认参数模板。 - true：表示为用户自定义参数模板。
        :type user_defined: bool
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._datastore_version = None
        self._datastore_name = None
        self._node_type = None
        self._ha_mode = None
        self._created = None
        self._updated = None
        self._user_defined = None
        self.discriminator = None

        self.id = id
        self.name = name
        if description is not None:
            self.description = description
        self.datastore_version = datastore_version
        self.datastore_name = datastore_name
        self.node_type = node_type
        self.ha_mode = ha_mode
        self.created = created
        self.updated = updated
        self.user_defined = user_defined

    @property
    def id(self):
        r"""Gets the id of this ConfigurationsResult.

        **参数解释**: 参数模板ID。参数模板的唯一标识。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。

        :return: The id of this ConfigurationsResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ConfigurationsResult.

        **参数解释**: 参数模板ID。参数模板的唯一标识。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。

        :param id: The id of this ConfigurationsResult.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ConfigurationsResult.

        **参数解释**: 参数模板名称。 **取值范围**: 参数模板名称在1到64个字符之间，区分大小写，可包含字母、数字、英文中划线、下划线或句点，不能包含其他特殊字符。

        :return: The name of this ConfigurationsResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ConfigurationsResult.

        **参数解释**: 参数模板名称。 **取值范围**: 参数模板名称在1到64个字符之间，区分大小写，可包含字母、数字、英文中划线、下划线或句点，不能包含其他特殊字符。

        :param name: The name of this ConfigurationsResult.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ConfigurationsResult.

        **参数解释**: 参数模板描述。 **取值范围**: 描述不能超过256个字符，且不能包含回车和 ! < \" = ' > &这些特殊字符。

        :return: The description of this ConfigurationsResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ConfigurationsResult.

        **参数解释**: 参数模板描述。 **取值范围**: 描述不能超过256个字符，且不能包含回车和 ! < \" = ' > &这些特殊字符。

        :param description: The description of this ConfigurationsResult.
        :type description: str
        """
        self._description = description

    @property
    def datastore_version(self):
        r"""Gets the datastore_version of this ConfigurationsResult.

        **参数解释**: 引擎版本。 **取值范围**: 不涉及。

        :return: The datastore_version of this ConfigurationsResult.
        :rtype: str
        """
        return self._datastore_version

    @datastore_version.setter
    def datastore_version(self, datastore_version):
        r"""Sets the datastore_version of this ConfigurationsResult.

        **参数解释**: 引擎版本。 **取值范围**: 不涉及。

        :param datastore_version: The datastore_version of this ConfigurationsResult.
        :type datastore_version: str
        """
        self._datastore_version = datastore_version

    @property
    def datastore_name(self):
        r"""Gets the datastore_name of this ConfigurationsResult.

        **参数解释**: 引擎名称。 **取值范围**: GaussDB。

        :return: The datastore_name of this ConfigurationsResult.
        :rtype: str
        """
        return self._datastore_name

    @datastore_name.setter
    def datastore_name(self, datastore_name):
        r"""Sets the datastore_name of this ConfigurationsResult.

        **参数解释**: 引擎名称。 **取值范围**: GaussDB。

        :param datastore_name: The datastore_name of this ConfigurationsResult.
        :type datastore_name: str
        """
        self._datastore_name = datastore_name

    @property
    def node_type(self):
        r"""Gets the node_type of this ConfigurationsResult.

        **参数解释**: 节点类型。 **取值范围**: - independent：独立部署。 - ha：集中式。 - combined：混合部署。

        :return: The node_type of this ConfigurationsResult.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        r"""Sets the node_type of this ConfigurationsResult.

        **参数解释**: 节点类型。 **取值范围**: - independent：独立部署。 - ha：集中式。 - combined：混合部署。

        :param node_type: The node_type of this ConfigurationsResult.
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def ha_mode(self):
        r"""Gets the ha_mode of this ConfigurationsResult.

        **参数解释**: 实例类型。 **取值范围**: - Enterprise：分布式实例（企业版）。 - centralization_standard：集中式版实例。  区分大小写。

        :return: The ha_mode of this ConfigurationsResult.
        :rtype: str
        """
        return self._ha_mode

    @ha_mode.setter
    def ha_mode(self, ha_mode):
        r"""Sets the ha_mode of this ConfigurationsResult.

        **参数解释**: 实例类型。 **取值范围**: - Enterprise：分布式实例（企业版）。 - centralization_standard：集中式版实例。  区分大小写。

        :param ha_mode: The ha_mode of this ConfigurationsResult.
        :type ha_mode: str
        """
        self._ha_mode = ha_mode

    @property
    def created(self):
        r"""Gets the created of this ConfigurationsResult.

        **参数解释**: 创建时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。例如：2024-07-03T14:18:55。 **取值范围**: 不涉及。

        :return: The created of this ConfigurationsResult.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this ConfigurationsResult.

        **参数解释**: 创建时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。例如：2024-07-03T14:18:55。 **取值范围**: 不涉及。

        :param created: The created of this ConfigurationsResult.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        r"""Gets the updated of this ConfigurationsResult.

        **参数解释**: 更新时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。例如：2024-07-03T14:18:55。 **取值范围**: 不涉及。

        :return: The updated of this ConfigurationsResult.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this ConfigurationsResult.

        **参数解释**: 更新时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。例如：2024-07-03T14:18:55。 **取值范围**: 不涉及。

        :param updated: The updated of this ConfigurationsResult.
        :type updated: str
        """
        self._updated = updated

    @property
    def user_defined(self):
        r"""Gets the user_defined of this ConfigurationsResult.

        **参数解释**: 是否是用户自定义参数模板。 **取值范围**: - false：表示为系统默认参数模板。 - true：表示为用户自定义参数模板。

        :return: The user_defined of this ConfigurationsResult.
        :rtype: bool
        """
        return self._user_defined

    @user_defined.setter
    def user_defined(self, user_defined):
        r"""Sets the user_defined of this ConfigurationsResult.

        **参数解释**: 是否是用户自定义参数模板。 **取值范围**: - false：表示为系统默认参数模板。 - true：表示为用户自定义参数模板。

        :param user_defined: The user_defined of this ConfigurationsResult.
        :type user_defined: bool
        """
        self._user_defined = user_defined

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
        if not isinstance(other, ConfigurationsResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
