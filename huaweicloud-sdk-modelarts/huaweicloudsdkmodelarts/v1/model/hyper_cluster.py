# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HyperCluster:

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
        'network_info': 'list[HyperClusterNetworkInfo]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'network_info': 'network_info'
    }

    def __init__(self, id=None, name=None, network_info=None):
        r"""HyperCluster

        The model defined in huaweicloud sdk

        :param id: **参数解释**：hyper cluster的ID。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。
        :type id: str
        :param name: **参数解释**：hyper cluster的名称。 **取值范围**：^[-_.a-zA-Z0-9]{1,64}$。
        :type name: str
        :param network_info: **参数解释**：网络信息。
        :type network_info: list[:class:`huaweicloudsdkmodelarts.v1.HyperClusterNetworkInfo`]
        """
        
        

        self._id = None
        self._name = None
        self._network_info = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if network_info is not None:
            self.network_info = network_info

    @property
    def id(self):
        r"""Gets the id of this HyperCluster.

        **参数解释**：hyper cluster的ID。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。

        :return: The id of this HyperCluster.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this HyperCluster.

        **参数解释**：hyper cluster的ID。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。

        :param id: The id of this HyperCluster.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this HyperCluster.

        **参数解释**：hyper cluster的名称。 **取值范围**：^[-_.a-zA-Z0-9]{1,64}$。

        :return: The name of this HyperCluster.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this HyperCluster.

        **参数解释**：hyper cluster的名称。 **取值范围**：^[-_.a-zA-Z0-9]{1,64}$。

        :param name: The name of this HyperCluster.
        :type name: str
        """
        self._name = name

    @property
    def network_info(self):
        r"""Gets the network_info of this HyperCluster.

        **参数解释**：网络信息。

        :return: The network_info of this HyperCluster.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.HyperClusterNetworkInfo`]
        """
        return self._network_info

    @network_info.setter
    def network_info(self, network_info):
        r"""Sets the network_info of this HyperCluster.

        **参数解释**：网络信息。

        :param network_info: The network_info of this HyperCluster.
        :type network_info: list[:class:`huaweicloudsdkmodelarts.v1.HyperClusterNetworkInfo`]
        """
        self._network_info = network_info

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
        if not isinstance(other, HyperCluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
