# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CceIntegrationProtectionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_type': 'str',
        'cluster_id': 'str',
        'cluster_name': 'str',
        'charging_mode': 'str',
        'cce_protection_type': 'str',
        'prefer_packet_cycle': 'bool'
    }

    attribute_map = {
        'cluster_type': 'cluster_type',
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'charging_mode': 'charging_mode',
        'cce_protection_type': 'cce_protection_type',
        'prefer_packet_cycle': 'prefer_packet_cycle'
    }

    def __init__(self, cluster_type=None, cluster_id=None, cluster_name=None, charging_mode=None, cce_protection_type=None, prefer_packet_cycle=None):
        r"""CceIntegrationProtectionRequestBody

        The model defined in huaweicloud sdk

        :param cluster_type: **参数解释**: cce集群类型 **约束限制**: 不涉及 **取值范围**: 包含如下两种： - existing：存量集群。 - adding：新增集群。  **默认取值**: 不涉及 
        :type cluster_type: str
        :param cluster_id: 集群id
        :type cluster_id: str
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param charging_mode: **参数解释**: 付费模式 **约束限制**: 不涉及 **取值范围**: 包含如下两种： - on_demand：按需。 - free_security_check：免费安全体检。  **默认取值**: 不涉及 
        :type charging_mode: str
        :param cce_protection_type: **参数解释**: cce防护类型 **约束限制**: 不涉及 **取值范围**: 包含如下两种： - cluster_level：集群级别防护。 - node_level：节点级别防护。  **默认取值**: 不涉及 
        :type cce_protection_type: str
        :param prefer_packet_cycle: 优先使用包周期配额；默认false
        :type prefer_packet_cycle: bool
        """
        
        

        self._cluster_type = None
        self._cluster_id = None
        self._cluster_name = None
        self._charging_mode = None
        self._cce_protection_type = None
        self._prefer_packet_cycle = None
        self.discriminator = None

        if cluster_type is not None:
            self.cluster_type = cluster_type
        if cluster_id is not None:
            self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if cce_protection_type is not None:
            self.cce_protection_type = cce_protection_type
        if prefer_packet_cycle is not None:
            self.prefer_packet_cycle = prefer_packet_cycle

    @property
    def cluster_type(self):
        r"""Gets the cluster_type of this CceIntegrationProtectionRequestBody.

        **参数解释**: cce集群类型 **约束限制**: 不涉及 **取值范围**: 包含如下两种： - existing：存量集群。 - adding：新增集群。  **默认取值**: 不涉及 

        :return: The cluster_type of this CceIntegrationProtectionRequestBody.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        r"""Sets the cluster_type of this CceIntegrationProtectionRequestBody.

        **参数解释**: cce集群类型 **约束限制**: 不涉及 **取值范围**: 包含如下两种： - existing：存量集群。 - adding：新增集群。  **默认取值**: 不涉及 

        :param cluster_type: The cluster_type of this CceIntegrationProtectionRequestBody.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this CceIntegrationProtectionRequestBody.

        集群id

        :return: The cluster_id of this CceIntegrationProtectionRequestBody.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this CceIntegrationProtectionRequestBody.

        集群id

        :param cluster_id: The cluster_id of this CceIntegrationProtectionRequestBody.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this CceIntegrationProtectionRequestBody.

        集群名称

        :return: The cluster_name of this CceIntegrationProtectionRequestBody.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this CceIntegrationProtectionRequestBody.

        集群名称

        :param cluster_name: The cluster_name of this CceIntegrationProtectionRequestBody.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this CceIntegrationProtectionRequestBody.

        **参数解释**: 付费模式 **约束限制**: 不涉及 **取值范围**: 包含如下两种： - on_demand：按需。 - free_security_check：免费安全体检。  **默认取值**: 不涉及 

        :return: The charging_mode of this CceIntegrationProtectionRequestBody.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this CceIntegrationProtectionRequestBody.

        **参数解释**: 付费模式 **约束限制**: 不涉及 **取值范围**: 包含如下两种： - on_demand：按需。 - free_security_check：免费安全体检。  **默认取值**: 不涉及 

        :param charging_mode: The charging_mode of this CceIntegrationProtectionRequestBody.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def cce_protection_type(self):
        r"""Gets the cce_protection_type of this CceIntegrationProtectionRequestBody.

        **参数解释**: cce防护类型 **约束限制**: 不涉及 **取值范围**: 包含如下两种： - cluster_level：集群级别防护。 - node_level：节点级别防护。  **默认取值**: 不涉及 

        :return: The cce_protection_type of this CceIntegrationProtectionRequestBody.
        :rtype: str
        """
        return self._cce_protection_type

    @cce_protection_type.setter
    def cce_protection_type(self, cce_protection_type):
        r"""Sets the cce_protection_type of this CceIntegrationProtectionRequestBody.

        **参数解释**: cce防护类型 **约束限制**: 不涉及 **取值范围**: 包含如下两种： - cluster_level：集群级别防护。 - node_level：节点级别防护。  **默认取值**: 不涉及 

        :param cce_protection_type: The cce_protection_type of this CceIntegrationProtectionRequestBody.
        :type cce_protection_type: str
        """
        self._cce_protection_type = cce_protection_type

    @property
    def prefer_packet_cycle(self):
        r"""Gets the prefer_packet_cycle of this CceIntegrationProtectionRequestBody.

        优先使用包周期配额；默认false

        :return: The prefer_packet_cycle of this CceIntegrationProtectionRequestBody.
        :rtype: bool
        """
        return self._prefer_packet_cycle

    @prefer_packet_cycle.setter
    def prefer_packet_cycle(self, prefer_packet_cycle):
        r"""Sets the prefer_packet_cycle of this CceIntegrationProtectionRequestBody.

        优先使用包周期配额；默认false

        :param prefer_packet_cycle: The prefer_packet_cycle of this CceIntegrationProtectionRequestBody.
        :type prefer_packet_cycle: bool
        """
        self._prefer_packet_cycle = prefer_packet_cycle

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
        if not isinstance(other, CceIntegrationProtectionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
