# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateHostAssetValueRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_value': 'str',
        'host_id_list': 'list[str]'
    }

    attribute_map = {
        'asset_value': 'asset_value',
        'host_id_list': 'host_id_list'
    }

    def __init__(self, asset_value=None, host_id_list=None):
        r"""AssociateHostAssetValueRequestInfo

        The model defined in huaweicloud sdk

        :param asset_value: **参数解释**： 资产重要性 **约束限制**： 不涉及 **取值范围**： - important：重要资产 - common：一般资产 - test：测试资产 **默认取值**： 不涉及 
        :type asset_value: str
        :param host_id_list: **参数解释**： 主机ID列表 **约束限制**： 不涉及 **取值范围**： 列表大小为1-200条 **默认取值**： 不涉及 
        :type host_id_list: list[str]
        """
        
        

        self._asset_value = None
        self._host_id_list = None
        self.discriminator = None

        self.asset_value = asset_value
        self.host_id_list = host_id_list

    @property
    def asset_value(self):
        r"""Gets the asset_value of this AssociateHostAssetValueRequestInfo.

        **参数解释**： 资产重要性 **约束限制**： 不涉及 **取值范围**： - important：重要资产 - common：一般资产 - test：测试资产 **默认取值**： 不涉及 

        :return: The asset_value of this AssociateHostAssetValueRequestInfo.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this AssociateHostAssetValueRequestInfo.

        **参数解释**： 资产重要性 **约束限制**： 不涉及 **取值范围**： - important：重要资产 - common：一般资产 - test：测试资产 **默认取值**： 不涉及 

        :param asset_value: The asset_value of this AssociateHostAssetValueRequestInfo.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def host_id_list(self):
        r"""Gets the host_id_list of this AssociateHostAssetValueRequestInfo.

        **参数解释**： 主机ID列表 **约束限制**： 不涉及 **取值范围**： 列表大小为1-200条 **默认取值**： 不涉及 

        :return: The host_id_list of this AssociateHostAssetValueRequestInfo.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        r"""Sets the host_id_list of this AssociateHostAssetValueRequestInfo.

        **参数解释**： 主机ID列表 **约束限制**： 不涉及 **取值范围**： 列表大小为1-200条 **默认取值**： 不涉及 

        :param host_id_list: The host_id_list of this AssociateHostAssetValueRequestInfo.
        :type host_id_list: list[str]
        """
        self._host_id_list = host_id_list

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
        if not isinstance(other, AssociateHostAssetValueRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
