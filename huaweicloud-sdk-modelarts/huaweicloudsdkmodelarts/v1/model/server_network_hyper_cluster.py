# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerNetworkHyperCluster:

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
        'hyper_cluster_subnet_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'hyper_cluster_subnet_id': 'hyper_cluster_subnet_id'
    }

    def __init__(self, id=None, hyper_cluster_subnet_id=None):
        r"""ServerNetworkHyperCluster

        The model defined in huaweicloud sdk

        :param id: 参数解释：HyperCluster的id。 约束限制：不涉及。 取值范围：不涉及。 默认取值：不涉及。
        :type id: str
        :param hyper_cluster_subnet_id: 参数解释：HyperCluster的子网id。 约束限制：不涉及。 取值范围：不涉及。 默认取值：不涉及。
        :type hyper_cluster_subnet_id: str
        """
        
        

        self._id = None
        self._hyper_cluster_subnet_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if hyper_cluster_subnet_id is not None:
            self.hyper_cluster_subnet_id = hyper_cluster_subnet_id

    @property
    def id(self):
        r"""Gets the id of this ServerNetworkHyperCluster.

        参数解释：HyperCluster的id。 约束限制：不涉及。 取值范围：不涉及。 默认取值：不涉及。

        :return: The id of this ServerNetworkHyperCluster.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ServerNetworkHyperCluster.

        参数解释：HyperCluster的id。 约束限制：不涉及。 取值范围：不涉及。 默认取值：不涉及。

        :param id: The id of this ServerNetworkHyperCluster.
        :type id: str
        """
        self._id = id

    @property
    def hyper_cluster_subnet_id(self):
        r"""Gets the hyper_cluster_subnet_id of this ServerNetworkHyperCluster.

        参数解释：HyperCluster的子网id。 约束限制：不涉及。 取值范围：不涉及。 默认取值：不涉及。

        :return: The hyper_cluster_subnet_id of this ServerNetworkHyperCluster.
        :rtype: str
        """
        return self._hyper_cluster_subnet_id

    @hyper_cluster_subnet_id.setter
    def hyper_cluster_subnet_id(self, hyper_cluster_subnet_id):
        r"""Sets the hyper_cluster_subnet_id of this ServerNetworkHyperCluster.

        参数解释：HyperCluster的子网id。 约束限制：不涉及。 取值范围：不涉及。 默认取值：不涉及。

        :param hyper_cluster_subnet_id: The hyper_cluster_subnet_id of this ServerNetworkHyperCluster.
        :type hyper_cluster_subnet_id: str
        """
        self._hyper_cluster_subnet_id = hyper_cluster_subnet_id

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
        if not isinstance(other, ServerNetworkHyperCluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
