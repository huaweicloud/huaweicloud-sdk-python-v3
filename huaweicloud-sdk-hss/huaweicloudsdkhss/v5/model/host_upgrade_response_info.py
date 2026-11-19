# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HostUpgradeResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'upgrade_status': 'str'
    }

    attribute_map = {
        'host_id': 'host_id',
        'upgrade_status': 'upgrade_status'
    }

    def __init__(self, host_id=None, upgrade_status=None):
        r"""HostUpgradeResponseInfo

        The model defined in huaweicloud sdk

        :param host_id: **参数解释**: 服务器ID **取值范围**: 字符长度0-128位 
        :type host_id: str
        :param upgrade_status: **参数解释**: 升级状态 **取值范围**: - not_upgrade：未升级，默认状态，客户还没有给这台机器下发过升级 - upgrading：正在升级到2.0中 - upgrade_failed：升级到2.0失败 - upgrade_succeed：已经成功升级到2.0 
        :type upgrade_status: str
        """
        
        

        self._host_id = None
        self._upgrade_status = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if upgrade_status is not None:
            self.upgrade_status = upgrade_status

    @property
    def host_id(self):
        r"""Gets the host_id of this HostUpgradeResponseInfo.

        **参数解释**: 服务器ID **取值范围**: 字符长度0-128位 

        :return: The host_id of this HostUpgradeResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this HostUpgradeResponseInfo.

        **参数解释**: 服务器ID **取值范围**: 字符长度0-128位 

        :param host_id: The host_id of this HostUpgradeResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def upgrade_status(self):
        r"""Gets the upgrade_status of this HostUpgradeResponseInfo.

        **参数解释**: 升级状态 **取值范围**: - not_upgrade：未升级，默认状态，客户还没有给这台机器下发过升级 - upgrading：正在升级到2.0中 - upgrade_failed：升级到2.0失败 - upgrade_succeed：已经成功升级到2.0 

        :return: The upgrade_status of this HostUpgradeResponseInfo.
        :rtype: str
        """
        return self._upgrade_status

    @upgrade_status.setter
    def upgrade_status(self, upgrade_status):
        r"""Sets the upgrade_status of this HostUpgradeResponseInfo.

        **参数解释**: 升级状态 **取值范围**: - not_upgrade：未升级，默认状态，客户还没有给这台机器下发过升级 - upgrading：正在升级到2.0中 - upgrade_failed：升级到2.0失败 - upgrade_succeed：已经成功升级到2.0 

        :param upgrade_status: The upgrade_status of this HostUpgradeResponseInfo.
        :type upgrade_status: str
        """
        self._upgrade_status = upgrade_status

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
        if not isinstance(other, HostUpgradeResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
