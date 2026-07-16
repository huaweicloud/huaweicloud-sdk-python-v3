# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HyperClusterNetworkInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hyper_cluster_subnet_id': 'str',
        'is_default': 'bool'
    }

    attribute_map = {
        'hyper_cluster_subnet_id': 'hyper_cluster_subnet_id',
        'is_default': 'is_default'
    }

    def __init__(self, hyper_cluster_subnet_id=None, is_default=None):
        r"""HyperClusterNetworkInfo

        The model defined in huaweicloud sdk

        :param hyper_cluster_subnet_id: **参数解释**：hyper cluster的子网名称。 **取值范围**：^[-_.a-zA-Z0-9]{1,64}$。
        :type hyper_cluster_subnet_id: str
        :param is_default: **参数解释**：是否默认。 **约束限制**：不涉及。 **取值范围**： - true：默认网络 - false：非默认网络
        :type is_default: bool
        """
        
        

        self._hyper_cluster_subnet_id = None
        self._is_default = None
        self.discriminator = None

        if hyper_cluster_subnet_id is not None:
            self.hyper_cluster_subnet_id = hyper_cluster_subnet_id
        if is_default is not None:
            self.is_default = is_default

    @property
    def hyper_cluster_subnet_id(self):
        r"""Gets the hyper_cluster_subnet_id of this HyperClusterNetworkInfo.

        **参数解释**：hyper cluster的子网名称。 **取值范围**：^[-_.a-zA-Z0-9]{1,64}$。

        :return: The hyper_cluster_subnet_id of this HyperClusterNetworkInfo.
        :rtype: str
        """
        return self._hyper_cluster_subnet_id

    @hyper_cluster_subnet_id.setter
    def hyper_cluster_subnet_id(self, hyper_cluster_subnet_id):
        r"""Sets the hyper_cluster_subnet_id of this HyperClusterNetworkInfo.

        **参数解释**：hyper cluster的子网名称。 **取值范围**：^[-_.a-zA-Z0-9]{1,64}$。

        :param hyper_cluster_subnet_id: The hyper_cluster_subnet_id of this HyperClusterNetworkInfo.
        :type hyper_cluster_subnet_id: str
        """
        self._hyper_cluster_subnet_id = hyper_cluster_subnet_id

    @property
    def is_default(self):
        r"""Gets the is_default of this HyperClusterNetworkInfo.

        **参数解释**：是否默认。 **约束限制**：不涉及。 **取值范围**： - true：默认网络 - false：非默认网络

        :return: The is_default of this HyperClusterNetworkInfo.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        r"""Sets the is_default of this HyperClusterNetworkInfo.

        **参数解释**：是否默认。 **约束限制**：不涉及。 **取值范围**： - true：默认网络 - false：非默认网络

        :param is_default: The is_default of this HyperClusterNetworkInfo.
        :type is_default: bool
        """
        self._is_default = is_default

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
        if not isinstance(other, HyperClusterNetworkInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
