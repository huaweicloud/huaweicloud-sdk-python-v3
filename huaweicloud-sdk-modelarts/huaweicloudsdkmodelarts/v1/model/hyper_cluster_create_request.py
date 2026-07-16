# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HyperClusterCreateRequest:

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
        'hyper_cluster_subnet_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'hyper_cluster_subnet_id': 'hyper_cluster_subnet_id',
        'type': 'type'
    }

    def __init__(self, name=None, hyper_cluster_subnet_id=None, type=None):
        r"""HyperClusterCreateRequest

        The model defined in huaweicloud sdk

        :param name: **参数解释**：hyper cluster的名称。 **取值范围**：^[-_.a-zA-Z0-9]{1,64}$。
        :type name: str
        :param hyper_cluster_subnet_id: **参数解释**：hyper cluster的ID。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。
        :type hyper_cluster_subnet_id: str
        :param type: **参数解释**：服务器类型。 **约束限制**：不涉及。 **取值范围**： - HPS：超节点服务 - ECS：弹性云服务 **默认取值**：不涉及。
        :type type: str
        """
        
        

        self._name = None
        self._hyper_cluster_subnet_id = None
        self._type = None
        self.discriminator = None

        self.name = name
        if hyper_cluster_subnet_id is not None:
            self.hyper_cluster_subnet_id = hyper_cluster_subnet_id
        if type is not None:
            self.type = type

    @property
    def name(self):
        r"""Gets the name of this HyperClusterCreateRequest.

        **参数解释**：hyper cluster的名称。 **取值范围**：^[-_.a-zA-Z0-9]{1,64}$。

        :return: The name of this HyperClusterCreateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this HyperClusterCreateRequest.

        **参数解释**：hyper cluster的名称。 **取值范围**：^[-_.a-zA-Z0-9]{1,64}$。

        :param name: The name of this HyperClusterCreateRequest.
        :type name: str
        """
        self._name = name

    @property
    def hyper_cluster_subnet_id(self):
        r"""Gets the hyper_cluster_subnet_id of this HyperClusterCreateRequest.

        **参数解释**：hyper cluster的ID。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。

        :return: The hyper_cluster_subnet_id of this HyperClusterCreateRequest.
        :rtype: str
        """
        return self._hyper_cluster_subnet_id

    @hyper_cluster_subnet_id.setter
    def hyper_cluster_subnet_id(self, hyper_cluster_subnet_id):
        r"""Sets the hyper_cluster_subnet_id of this HyperClusterCreateRequest.

        **参数解释**：hyper cluster的ID。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。

        :param hyper_cluster_subnet_id: The hyper_cluster_subnet_id of this HyperClusterCreateRequest.
        :type hyper_cluster_subnet_id: str
        """
        self._hyper_cluster_subnet_id = hyper_cluster_subnet_id

    @property
    def type(self):
        r"""Gets the type of this HyperClusterCreateRequest.

        **参数解释**：服务器类型。 **约束限制**：不涉及。 **取值范围**： - HPS：超节点服务 - ECS：弹性云服务 **默认取值**：不涉及。

        :return: The type of this HyperClusterCreateRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this HyperClusterCreateRequest.

        **参数解释**：服务器类型。 **约束限制**：不涉及。 **取值范围**： - HPS：超节点服务 - ECS：弹性云服务 **默认取值**：不涉及。

        :param type: The type of this HyperClusterCreateRequest.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, HyperClusterCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
