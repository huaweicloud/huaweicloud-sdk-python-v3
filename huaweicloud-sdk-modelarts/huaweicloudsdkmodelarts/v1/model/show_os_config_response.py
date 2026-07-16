# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOsConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'network_cidrs': 'list[str]',
        'network_quota': 'int',
        'pool_quota': 'int',
        'pool_high_available': 'bool'
    }

    attribute_map = {
        'network_cidrs': 'networkCidrs',
        'network_quota': 'networkQuota',
        'pool_quota': 'poolQuota',
        'pool_high_available': 'poolHighAvailable'
    }

    def __init__(self, network_cidrs=None, network_quota=None, pool_quota=None, pool_high_available=None):
        r"""ShowOsConfigResponse

        The model defined in huaweicloud sdk

        :param network_cidrs: **参数解释**：网络配置项。
        :type network_cidrs: list[str]
        :param network_quota: **参数解释**：用户可创建网络个数配额。 **取值范围**：不涉及
        :type network_quota: int
        :param pool_quota: **参数解释**：用户可创建资源池个数配额。 **取值范围**：不涉及
        :type pool_quota: int
        :param pool_high_available: **参数解释**：当前环境/局点是否支持创建高可用资源池。 **取值范围**： - true：支持 - false：不支持
        :type pool_high_available: bool
        """
        
        super().__init__()

        self._network_cidrs = None
        self._network_quota = None
        self._pool_quota = None
        self._pool_high_available = None
        self.discriminator = None

        if network_cidrs is not None:
            self.network_cidrs = network_cidrs
        if network_quota is not None:
            self.network_quota = network_quota
        if pool_quota is not None:
            self.pool_quota = pool_quota
        if pool_high_available is not None:
            self.pool_high_available = pool_high_available

    @property
    def network_cidrs(self):
        r"""Gets the network_cidrs of this ShowOsConfigResponse.

        **参数解释**：网络配置项。

        :return: The network_cidrs of this ShowOsConfigResponse.
        :rtype: list[str]
        """
        return self._network_cidrs

    @network_cidrs.setter
    def network_cidrs(self, network_cidrs):
        r"""Sets the network_cidrs of this ShowOsConfigResponse.

        **参数解释**：网络配置项。

        :param network_cidrs: The network_cidrs of this ShowOsConfigResponse.
        :type network_cidrs: list[str]
        """
        self._network_cidrs = network_cidrs

    @property
    def network_quota(self):
        r"""Gets the network_quota of this ShowOsConfigResponse.

        **参数解释**：用户可创建网络个数配额。 **取值范围**：不涉及

        :return: The network_quota of this ShowOsConfigResponse.
        :rtype: int
        """
        return self._network_quota

    @network_quota.setter
    def network_quota(self, network_quota):
        r"""Sets the network_quota of this ShowOsConfigResponse.

        **参数解释**：用户可创建网络个数配额。 **取值范围**：不涉及

        :param network_quota: The network_quota of this ShowOsConfigResponse.
        :type network_quota: int
        """
        self._network_quota = network_quota

    @property
    def pool_quota(self):
        r"""Gets the pool_quota of this ShowOsConfigResponse.

        **参数解释**：用户可创建资源池个数配额。 **取值范围**：不涉及

        :return: The pool_quota of this ShowOsConfigResponse.
        :rtype: int
        """
        return self._pool_quota

    @pool_quota.setter
    def pool_quota(self, pool_quota):
        r"""Sets the pool_quota of this ShowOsConfigResponse.

        **参数解释**：用户可创建资源池个数配额。 **取值范围**：不涉及

        :param pool_quota: The pool_quota of this ShowOsConfigResponse.
        :type pool_quota: int
        """
        self._pool_quota = pool_quota

    @property
    def pool_high_available(self):
        r"""Gets the pool_high_available of this ShowOsConfigResponse.

        **参数解释**：当前环境/局点是否支持创建高可用资源池。 **取值范围**： - true：支持 - false：不支持

        :return: The pool_high_available of this ShowOsConfigResponse.
        :rtype: bool
        """
        return self._pool_high_available

    @pool_high_available.setter
    def pool_high_available(self, pool_high_available):
        r"""Sets the pool_high_available of this ShowOsConfigResponse.

        **参数解释**：当前环境/局点是否支持创建高可用资源池。 **取值范围**： - true：支持 - false：不支持

        :param pool_high_available: The pool_high_available of this ShowOsConfigResponse.
        :type pool_high_available: bool
        """
        self._pool_high_available = pool_high_available

    def to_dict(self):
        import warnings
        warnings.warn("ShowOsConfigResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowOsConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
