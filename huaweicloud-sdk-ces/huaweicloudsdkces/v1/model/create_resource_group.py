# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateResourceGroup:

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
        'dimensions': 'list[MetricsDimension]',
        'relation_id': 'str'
    }

    attribute_map = {
        'namespace': 'namespace',
        'dimensions': 'dimensions',
        'relation_id': 'relation_id'
    }

    def __init__(self, namespace=None, dimensions=None, relation_id=None):
        r"""CreateResourceGroup

        The model defined in huaweicloud sdk

        :param namespace: **参数解释** 查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)” **约束限制** 不涉及 **取值范围** 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_。字符串的长度必须在 3 到 32个字符之间。 **默认取值** 不涉及 
        :type namespace: str
        :param dimensions: **参数解释** 资源的维度信息 **约束限制** 不超过4个维度 
        :type dimensions: list[:class:`huaweicloudsdkces.v1.MetricsDimension`]
        :param relation_id: **参数解释** 关联id **约束限制** 不涉及 **取值范围** 由数字、字母,_和-组成长度[1,128] **默认取值** 不涉及 
        :type relation_id: str
        """
        
        

        self._namespace = None
        self._dimensions = None
        self._relation_id = None
        self.discriminator = None

        self.namespace = namespace
        self.dimensions = dimensions
        if relation_id is not None:
            self.relation_id = relation_id

    @property
    def namespace(self):
        r"""Gets the namespace of this CreateResourceGroup.

        **参数解释** 查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)” **约束限制** 不涉及 **取值范围** 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_。字符串的长度必须在 3 到 32个字符之间。 **默认取值** 不涉及 

        :return: The namespace of this CreateResourceGroup.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this CreateResourceGroup.

        **参数解释** 查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)” **约束限制** 不涉及 **取值范围** 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_。字符串的长度必须在 3 到 32个字符之间。 **默认取值** 不涉及 

        :param namespace: The namespace of this CreateResourceGroup.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def dimensions(self):
        r"""Gets the dimensions of this CreateResourceGroup.

        **参数解释** 资源的维度信息 **约束限制** 不超过4个维度 

        :return: The dimensions of this CreateResourceGroup.
        :rtype: list[:class:`huaweicloudsdkces.v1.MetricsDimension`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        r"""Sets the dimensions of this CreateResourceGroup.

        **参数解释** 资源的维度信息 **约束限制** 不超过4个维度 

        :param dimensions: The dimensions of this CreateResourceGroup.
        :type dimensions: list[:class:`huaweicloudsdkces.v1.MetricsDimension`]
        """
        self._dimensions = dimensions

    @property
    def relation_id(self):
        r"""Gets the relation_id of this CreateResourceGroup.

        **参数解释** 关联id **约束限制** 不涉及 **取值范围** 由数字、字母,_和-组成长度[1,128] **默认取值** 不涉及 

        :return: The relation_id of this CreateResourceGroup.
        :rtype: str
        """
        return self._relation_id

    @relation_id.setter
    def relation_id(self, relation_id):
        r"""Sets the relation_id of this CreateResourceGroup.

        **参数解释** 关联id **约束限制** 不涉及 **取值范围** 由数字、字母,_和-组成长度[1,128] **默认取值** 不涉及 

        :param relation_id: The relation_id of this CreateResourceGroup.
        :type relation_id: str
        """
        self._relation_id = relation_id

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
        if not isinstance(other, CreateResourceGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
