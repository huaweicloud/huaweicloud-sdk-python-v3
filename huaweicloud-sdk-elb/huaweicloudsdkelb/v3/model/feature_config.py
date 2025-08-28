# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FeatureConfig:

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
        'created_at': 'str',
        'updated_at': 'str',
        'service': 'str',
        'tenant_id': 'str',
        'feature': 'str',
        'switch': 'bool',
        'type': 'str',
        'value': 'str',
        'description': 'str',
        'caller': 'str'
    }

    attribute_map = {
        'id': 'id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'service': 'service',
        'tenant_id': 'tenant_id',
        'feature': 'feature',
        'switch': 'switch',
        'type': 'type',
        'value': 'value',
        'description': 'description',
        'caller': 'caller'
    }

    def __init__(self, id=None, created_at=None, updated_at=None, service=None, tenant_id=None, feature=None, switch=None, type=None, value=None, description=None, caller=None):
        r"""FeatureConfig

        The model defined in huaweicloud sdk

        :param id: **参数解释**：配置的ID。  **取值范围**：不涉及
        :type id: str
        :param created_at: **参数解释**：创建时间。  **取值范围**：不涉及
        :type created_at: str
        :param updated_at: **参数解释**：更新时间。  **取值范围**：不涉及
        :type updated_at: str
        :param service: **参数解释**：所属服务，固定ELB。  **取值范围**：不涉及
        :type service: str
        :param tenant_id: **参数解释**：租户ID，含义同project_id。  **取值范围**：不涉及
        :type tenant_id: str
        :param feature: **参数解释**：特性名称。  **取值范围**：不涉及
        :type feature: str
        :param switch: **参数解释**：特性配置启用开关，表示当前配置是否生效。  **取值范围**： - true：特性配置已生效。 - false: 特性配置未生效。
        :type switch: bool
        :param type: **参数解释**：特性配置值(value字段)的类型，如：INT，表示整型。  **取值范围**：不涉及
        :type type: str
        :param value: **参数解释**：特性配置值。如开关类型的特性配置取值true/false，表示特性开启关闭；配额类型的特性配置取值整数，表示限制配额。  **取值范围**：不涉及
        :type value: str
        :param description: **参数解释**：特性配置描述。  **取值范围**：不涉及
        :type description: str
        :param caller: **参数解释**：配置创建者。  **取值范围**：不涉及
        :type caller: str
        """
        
        

        self._id = None
        self._created_at = None
        self._updated_at = None
        self._service = None
        self._tenant_id = None
        self._feature = None
        self._switch = None
        self._type = None
        self._value = None
        self._description = None
        self._caller = None
        self.discriminator = None

        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        self.service = service
        self.tenant_id = tenant_id
        self.feature = feature
        self.switch = switch
        self.type = type
        self.value = value
        self.description = description
        self.caller = caller

    @property
    def id(self):
        r"""Gets the id of this FeatureConfig.

        **参数解释**：配置的ID。  **取值范围**：不涉及

        :return: The id of this FeatureConfig.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this FeatureConfig.

        **参数解释**：配置的ID。  **取值范围**：不涉及

        :param id: The id of this FeatureConfig.
        :type id: str
        """
        self._id = id

    @property
    def created_at(self):
        r"""Gets the created_at of this FeatureConfig.

        **参数解释**：创建时间。  **取值范围**：不涉及

        :return: The created_at of this FeatureConfig.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this FeatureConfig.

        **参数解释**：创建时间。  **取值范围**：不涉及

        :param created_at: The created_at of this FeatureConfig.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this FeatureConfig.

        **参数解释**：更新时间。  **取值范围**：不涉及

        :return: The updated_at of this FeatureConfig.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this FeatureConfig.

        **参数解释**：更新时间。  **取值范围**：不涉及

        :param updated_at: The updated_at of this FeatureConfig.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def service(self):
        r"""Gets the service of this FeatureConfig.

        **参数解释**：所属服务，固定ELB。  **取值范围**：不涉及

        :return: The service of this FeatureConfig.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        r"""Sets the service of this FeatureConfig.

        **参数解释**：所属服务，固定ELB。  **取值范围**：不涉及

        :param service: The service of this FeatureConfig.
        :type service: str
        """
        self._service = service

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this FeatureConfig.

        **参数解释**：租户ID，含义同project_id。  **取值范围**：不涉及

        :return: The tenant_id of this FeatureConfig.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this FeatureConfig.

        **参数解释**：租户ID，含义同project_id。  **取值范围**：不涉及

        :param tenant_id: The tenant_id of this FeatureConfig.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def feature(self):
        r"""Gets the feature of this FeatureConfig.

        **参数解释**：特性名称。  **取值范围**：不涉及

        :return: The feature of this FeatureConfig.
        :rtype: str
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        r"""Sets the feature of this FeatureConfig.

        **参数解释**：特性名称。  **取值范围**：不涉及

        :param feature: The feature of this FeatureConfig.
        :type feature: str
        """
        self._feature = feature

    @property
    def switch(self):
        r"""Gets the switch of this FeatureConfig.

        **参数解释**：特性配置启用开关，表示当前配置是否生效。  **取值范围**： - true：特性配置已生效。 - false: 特性配置未生效。

        :return: The switch of this FeatureConfig.
        :rtype: bool
        """
        return self._switch

    @switch.setter
    def switch(self, switch):
        r"""Sets the switch of this FeatureConfig.

        **参数解释**：特性配置启用开关，表示当前配置是否生效。  **取值范围**： - true：特性配置已生效。 - false: 特性配置未生效。

        :param switch: The switch of this FeatureConfig.
        :type switch: bool
        """
        self._switch = switch

    @property
    def type(self):
        r"""Gets the type of this FeatureConfig.

        **参数解释**：特性配置值(value字段)的类型，如：INT，表示整型。  **取值范围**：不涉及

        :return: The type of this FeatureConfig.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this FeatureConfig.

        **参数解释**：特性配置值(value字段)的类型，如：INT，表示整型。  **取值范围**：不涉及

        :param type: The type of this FeatureConfig.
        :type type: str
        """
        self._type = type

    @property
    def value(self):
        r"""Gets the value of this FeatureConfig.

        **参数解释**：特性配置值。如开关类型的特性配置取值true/false，表示特性开启关闭；配额类型的特性配置取值整数，表示限制配额。  **取值范围**：不涉及

        :return: The value of this FeatureConfig.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this FeatureConfig.

        **参数解释**：特性配置值。如开关类型的特性配置取值true/false，表示特性开启关闭；配额类型的特性配置取值整数，表示限制配额。  **取值范围**：不涉及

        :param value: The value of this FeatureConfig.
        :type value: str
        """
        self._value = value

    @property
    def description(self):
        r"""Gets the description of this FeatureConfig.

        **参数解释**：特性配置描述。  **取值范围**：不涉及

        :return: The description of this FeatureConfig.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this FeatureConfig.

        **参数解释**：特性配置描述。  **取值范围**：不涉及

        :param description: The description of this FeatureConfig.
        :type description: str
        """
        self._description = description

    @property
    def caller(self):
        r"""Gets the caller of this FeatureConfig.

        **参数解释**：配置创建者。  **取值范围**：不涉及

        :return: The caller of this FeatureConfig.
        :rtype: str
        """
        return self._caller

    @caller.setter
    def caller(self, caller):
        r"""Sets the caller of this FeatureConfig.

        **参数解释**：配置创建者。  **取值范围**：不涉及

        :param caller: The caller of this FeatureConfig.
        :type caller: str
        """
        self._caller = caller

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
        if not isinstance(other, FeatureConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
