# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateModelAssetReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_desc': 'str',
        'asset_name': 'str'
    }

    attribute_map = {
        'asset_desc': 'asset_desc',
        'asset_name': 'asset_name'
    }

    def __init__(self, asset_desc=None, asset_name=None):
        r"""UpdateModelAssetReq

        The model defined in huaweicloud sdk

        :param asset_desc: **参数解释**： 资产描述。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type asset_desc: str
        :param asset_name: **参数解释**： 资产名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type asset_name: str
        """
        
        

        self._asset_desc = None
        self._asset_name = None
        self.discriminator = None

        if asset_desc is not None:
            self.asset_desc = asset_desc
        if asset_name is not None:
            self.asset_name = asset_name

    @property
    def asset_desc(self):
        r"""Gets the asset_desc of this UpdateModelAssetReq.

        **参数解释**： 资产描述。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The asset_desc of this UpdateModelAssetReq.
        :rtype: str
        """
        return self._asset_desc

    @asset_desc.setter
    def asset_desc(self, asset_desc):
        r"""Sets the asset_desc of this UpdateModelAssetReq.

        **参数解释**： 资产描述。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param asset_desc: The asset_desc of this UpdateModelAssetReq.
        :type asset_desc: str
        """
        self._asset_desc = asset_desc

    @property
    def asset_name(self):
        r"""Gets the asset_name of this UpdateModelAssetReq.

        **参数解释**： 资产名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The asset_name of this UpdateModelAssetReq.
        :rtype: str
        """
        return self._asset_name

    @asset_name.setter
    def asset_name(self, asset_name):
        r"""Sets the asset_name of this UpdateModelAssetReq.

        **参数解释**： 资产名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param asset_name: The asset_name of this UpdateModelAssetReq.
        :type asset_name: str
        """
        self._asset_name = asset_name

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
        if not isinstance(other, UpdateModelAssetReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
