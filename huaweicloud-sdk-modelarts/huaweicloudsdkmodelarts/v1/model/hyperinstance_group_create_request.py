# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HyperinstanceGroupCreateRequest:

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
        'hyperinstance_cluster_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'hyperinstance_cluster_id': 'hyperinstance_cluster_id'
    }

    def __init__(self, name=None, hyperinstance_cluster_id=None):
        r"""HyperinstanceGroupCreateRequest

        The model defined in huaweicloud sdk

        :param name: **参数解释**：hyperinstance-group名称。 **默认取值**：不涉及。
        :type name: str
        :param hyperinstance_cluster_id: **参数解释**：超节点集群ID。 **默认取值**：不涉及。
        :type hyperinstance_cluster_id: str
        """
        
        

        self._name = None
        self._hyperinstance_cluster_id = None
        self.discriminator = None

        self.name = name
        self.hyperinstance_cluster_id = hyperinstance_cluster_id

    @property
    def name(self):
        r"""Gets the name of this HyperinstanceGroupCreateRequest.

        **参数解释**：hyperinstance-group名称。 **默认取值**：不涉及。

        :return: The name of this HyperinstanceGroupCreateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this HyperinstanceGroupCreateRequest.

        **参数解释**：hyperinstance-group名称。 **默认取值**：不涉及。

        :param name: The name of this HyperinstanceGroupCreateRequest.
        :type name: str
        """
        self._name = name

    @property
    def hyperinstance_cluster_id(self):
        r"""Gets the hyperinstance_cluster_id of this HyperinstanceGroupCreateRequest.

        **参数解释**：超节点集群ID。 **默认取值**：不涉及。

        :return: The hyperinstance_cluster_id of this HyperinstanceGroupCreateRequest.
        :rtype: str
        """
        return self._hyperinstance_cluster_id

    @hyperinstance_cluster_id.setter
    def hyperinstance_cluster_id(self, hyperinstance_cluster_id):
        r"""Sets the hyperinstance_cluster_id of this HyperinstanceGroupCreateRequest.

        **参数解释**：超节点集群ID。 **默认取值**：不涉及。

        :param hyperinstance_cluster_id: The hyperinstance_cluster_id of this HyperinstanceGroupCreateRequest.
        :type hyperinstance_cluster_id: str
        """
        self._hyperinstance_cluster_id = hyperinstance_cluster_id

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
        if not isinstance(other, HyperinstanceGroupCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
