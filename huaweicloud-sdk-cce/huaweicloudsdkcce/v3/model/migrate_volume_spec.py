# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MigrateVolumeSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cmk_id': 'str'
    }

    attribute_map = {
        'cmk_id': 'cmkID'
    }

    def __init__(self, cmk_id=None):
        r"""MigrateVolumeSpec

        The model defined in huaweicloud sdk

        :param cmk_id: **参数解释**: 用户主密钥ID。 [&gt; 获取密钥ID的方法请参考：[查询密钥列表](https://support.huaweicloud.com/api-dew/ListKeys.html)](tag:hws) [&gt; 获取密钥ID的方法请参考：[查询密钥列表](https://support.huaweicloud.com/intl/zh-cn/api-dew/ListKeys.html)](tag:hws_hk)  **约束限制**: 不涉及 **取值范围**: 不涉及 **默认取值**: 默认为空，表示云硬盘不加密。 
        :type cmk_id: str
        """
        
        

        self._cmk_id = None
        self.discriminator = None

        if cmk_id is not None:
            self.cmk_id = cmk_id

    @property
    def cmk_id(self):
        r"""Gets the cmk_id of this MigrateVolumeSpec.

        **参数解释**: 用户主密钥ID。 [> 获取密钥ID的方法请参考：[查询密钥列表](https://support.huaweicloud.com/api-dew/ListKeys.html)](tag:hws) [> 获取密钥ID的方法请参考：[查询密钥列表](https://support.huaweicloud.com/intl/zh-cn/api-dew/ListKeys.html)](tag:hws_hk)  **约束限制**: 不涉及 **取值范围**: 不涉及 **默认取值**: 默认为空，表示云硬盘不加密。 

        :return: The cmk_id of this MigrateVolumeSpec.
        :rtype: str
        """
        return self._cmk_id

    @cmk_id.setter
    def cmk_id(self, cmk_id):
        r"""Sets the cmk_id of this MigrateVolumeSpec.

        **参数解释**: 用户主密钥ID。 [> 获取密钥ID的方法请参考：[查询密钥列表](https://support.huaweicloud.com/api-dew/ListKeys.html)](tag:hws) [> 获取密钥ID的方法请参考：[查询密钥列表](https://support.huaweicloud.com/intl/zh-cn/api-dew/ListKeys.html)](tag:hws_hk)  **约束限制**: 不涉及 **取值范围**: 不涉及 **默认取值**: 默认为空，表示云硬盘不加密。 

        :param cmk_id: The cmk_id of this MigrateVolumeSpec.
        :type cmk_id: str
        """
        self._cmk_id = cmk_id

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
        if not isinstance(other, MigrateVolumeSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
