# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Resource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'relation_id': 'str',
        'namespace': 'str',
        'dimensions': 'list[DimensionResp]',
        'status': 'str'
    }

    attribute_map = {
        'relation_id': 'relation_id',
        'namespace': 'namespace',
        'dimensions': 'dimensions',
        'status': 'status'
    }

    def __init__(self, relation_id=None, namespace=None, dimensions=None, status=None):
        r"""Resource

        The model defined in huaweicloud sdk

        :param relation_id: **参数解释**： 告警规则的ID或者资源分组ID。 **取值范围**： 不涉及
        :type relation_id: str
        :param namespace: **参数解释**： 服务指标命名空间。 **取值范围**： 不涉及
        :type namespace: str
        :param dimensions: **参数解释** 指标维度信息
        :type dimensions: list[:class:`huaweicloudsdkces.v1.DimensionResp`]
        :param status: **参数解释** 资源健康状态 **取值范围** - health: 表示无告警 - unhealth: 表示告警中 - no_alarm_rule: 表示未设置告警规则 
        :type status: str
        """
        
        

        self._relation_id = None
        self._namespace = None
        self._dimensions = None
        self._status = None
        self.discriminator = None

        if relation_id is not None:
            self.relation_id = relation_id
        if namespace is not None:
            self.namespace = namespace
        if dimensions is not None:
            self.dimensions = dimensions
        if status is not None:
            self.status = status

    @property
    def relation_id(self):
        r"""Gets the relation_id of this Resource.

        **参数解释**： 告警规则的ID或者资源分组ID。 **取值范围**： 不涉及

        :return: The relation_id of this Resource.
        :rtype: str
        """
        return self._relation_id

    @relation_id.setter
    def relation_id(self, relation_id):
        r"""Sets the relation_id of this Resource.

        **参数解释**： 告警规则的ID或者资源分组ID。 **取值范围**： 不涉及

        :param relation_id: The relation_id of this Resource.
        :type relation_id: str
        """
        self._relation_id = relation_id

    @property
    def namespace(self):
        r"""Gets the namespace of this Resource.

        **参数解释**： 服务指标命名空间。 **取值范围**： 不涉及

        :return: The namespace of this Resource.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this Resource.

        **参数解释**： 服务指标命名空间。 **取值范围**： 不涉及

        :param namespace: The namespace of this Resource.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def dimensions(self):
        r"""Gets the dimensions of this Resource.

        **参数解释** 指标维度信息

        :return: The dimensions of this Resource.
        :rtype: list[:class:`huaweicloudsdkces.v1.DimensionResp`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        r"""Sets the dimensions of this Resource.

        **参数解释** 指标维度信息

        :param dimensions: The dimensions of this Resource.
        :type dimensions: list[:class:`huaweicloudsdkces.v1.DimensionResp`]
        """
        self._dimensions = dimensions

    @property
    def status(self):
        r"""Gets the status of this Resource.

        **参数解释** 资源健康状态 **取值范围** - health: 表示无告警 - unhealth: 表示告警中 - no_alarm_rule: 表示未设置告警规则 

        :return: The status of this Resource.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Resource.

        **参数解释** 资源健康状态 **取值范围** - health: 表示无告警 - unhealth: 表示告警中 - no_alarm_rule: 表示未设置告警规则 

        :param status: The status of this Resource.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, Resource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
