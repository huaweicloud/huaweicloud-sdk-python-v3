# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerHpsGroupCapacity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'availability_zone': 'str',
        'hyperinstance_group_id': 'str',
        'hyperinstance_group_name': 'str',
        'hyperinstance_cluster_id': 'str',
        'resource_flavor': 'str',
        'is_sold_out': 'bool'
    }

    attribute_map = {
        'availability_zone': 'availability_zone',
        'hyperinstance_group_id': 'hyperinstance_group_id',
        'hyperinstance_group_name': 'hyperinstance_group_name',
        'hyperinstance_cluster_id': 'hyperinstance_cluster_id',
        'resource_flavor': 'resource_flavor',
        'is_sold_out': 'is_sold_out'
    }

    def __init__(self, availability_zone=None, hyperinstance_group_id=None, hyperinstance_group_name=None, hyperinstance_cluster_id=None, resource_flavor=None, is_sold_out=None):
        r"""ServerHpsGroupCapacity

        The model defined in huaweicloud sdk

        :param availability_zone: **参数解释**：可用区。 **默认取值**：不涉及。
        :type availability_zone: str
        :param hyperinstance_group_id: **参数解释**：hyperinstance-group ID。 **默认取值**：不涉及。
        :type hyperinstance_group_id: str
        :param hyperinstance_group_name: **参数解释**：hyperinstance-group名称。 **默认取值**：不涉及。
        :type hyperinstance_group_name: str
        :param hyperinstance_cluster_id: **参数解释**：超节点集群ID。 **默认取值**：不涉及。
        :type hyperinstance_cluster_id: str
        :param resource_flavor: **参数解释**：规格名称。 **默认取值**：不涉及。
        :type resource_flavor: str
        :param is_sold_out: **参数解释**：是否售罄。 **默认取值**：不涉及。
        :type is_sold_out: bool
        """
        
        

        self._availability_zone = None
        self._hyperinstance_group_id = None
        self._hyperinstance_group_name = None
        self._hyperinstance_cluster_id = None
        self._resource_flavor = None
        self._is_sold_out = None
        self.discriminator = None

        if availability_zone is not None:
            self.availability_zone = availability_zone
        if hyperinstance_group_id is not None:
            self.hyperinstance_group_id = hyperinstance_group_id
        if hyperinstance_group_name is not None:
            self.hyperinstance_group_name = hyperinstance_group_name
        if hyperinstance_cluster_id is not None:
            self.hyperinstance_cluster_id = hyperinstance_cluster_id
        if resource_flavor is not None:
            self.resource_flavor = resource_flavor
        if is_sold_out is not None:
            self.is_sold_out = is_sold_out

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this ServerHpsGroupCapacity.

        **参数解释**：可用区。 **默认取值**：不涉及。

        :return: The availability_zone of this ServerHpsGroupCapacity.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this ServerHpsGroupCapacity.

        **参数解释**：可用区。 **默认取值**：不涉及。

        :param availability_zone: The availability_zone of this ServerHpsGroupCapacity.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def hyperinstance_group_id(self):
        r"""Gets the hyperinstance_group_id of this ServerHpsGroupCapacity.

        **参数解释**：hyperinstance-group ID。 **默认取值**：不涉及。

        :return: The hyperinstance_group_id of this ServerHpsGroupCapacity.
        :rtype: str
        """
        return self._hyperinstance_group_id

    @hyperinstance_group_id.setter
    def hyperinstance_group_id(self, hyperinstance_group_id):
        r"""Sets the hyperinstance_group_id of this ServerHpsGroupCapacity.

        **参数解释**：hyperinstance-group ID。 **默认取值**：不涉及。

        :param hyperinstance_group_id: The hyperinstance_group_id of this ServerHpsGroupCapacity.
        :type hyperinstance_group_id: str
        """
        self._hyperinstance_group_id = hyperinstance_group_id

    @property
    def hyperinstance_group_name(self):
        r"""Gets the hyperinstance_group_name of this ServerHpsGroupCapacity.

        **参数解释**：hyperinstance-group名称。 **默认取值**：不涉及。

        :return: The hyperinstance_group_name of this ServerHpsGroupCapacity.
        :rtype: str
        """
        return self._hyperinstance_group_name

    @hyperinstance_group_name.setter
    def hyperinstance_group_name(self, hyperinstance_group_name):
        r"""Sets the hyperinstance_group_name of this ServerHpsGroupCapacity.

        **参数解释**：hyperinstance-group名称。 **默认取值**：不涉及。

        :param hyperinstance_group_name: The hyperinstance_group_name of this ServerHpsGroupCapacity.
        :type hyperinstance_group_name: str
        """
        self._hyperinstance_group_name = hyperinstance_group_name

    @property
    def hyperinstance_cluster_id(self):
        r"""Gets the hyperinstance_cluster_id of this ServerHpsGroupCapacity.

        **参数解释**：超节点集群ID。 **默认取值**：不涉及。

        :return: The hyperinstance_cluster_id of this ServerHpsGroupCapacity.
        :rtype: str
        """
        return self._hyperinstance_cluster_id

    @hyperinstance_cluster_id.setter
    def hyperinstance_cluster_id(self, hyperinstance_cluster_id):
        r"""Sets the hyperinstance_cluster_id of this ServerHpsGroupCapacity.

        **参数解释**：超节点集群ID。 **默认取值**：不涉及。

        :param hyperinstance_cluster_id: The hyperinstance_cluster_id of this ServerHpsGroupCapacity.
        :type hyperinstance_cluster_id: str
        """
        self._hyperinstance_cluster_id = hyperinstance_cluster_id

    @property
    def resource_flavor(self):
        r"""Gets the resource_flavor of this ServerHpsGroupCapacity.

        **参数解释**：规格名称。 **默认取值**：不涉及。

        :return: The resource_flavor of this ServerHpsGroupCapacity.
        :rtype: str
        """
        return self._resource_flavor

    @resource_flavor.setter
    def resource_flavor(self, resource_flavor):
        r"""Sets the resource_flavor of this ServerHpsGroupCapacity.

        **参数解释**：规格名称。 **默认取值**：不涉及。

        :param resource_flavor: The resource_flavor of this ServerHpsGroupCapacity.
        :type resource_flavor: str
        """
        self._resource_flavor = resource_flavor

    @property
    def is_sold_out(self):
        r"""Gets the is_sold_out of this ServerHpsGroupCapacity.

        **参数解释**：是否售罄。 **默认取值**：不涉及。

        :return: The is_sold_out of this ServerHpsGroupCapacity.
        :rtype: bool
        """
        return self._is_sold_out

    @is_sold_out.setter
    def is_sold_out(self, is_sold_out):
        r"""Sets the is_sold_out of this ServerHpsGroupCapacity.

        **参数解释**：是否售罄。 **默认取值**：不涉及。

        :param is_sold_out: The is_sold_out of this ServerHpsGroupCapacity.
        :type is_sold_out: bool
        """
        self._is_sold_out = is_sold_out

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
        if not isinstance(other, ServerHpsGroupCapacity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
