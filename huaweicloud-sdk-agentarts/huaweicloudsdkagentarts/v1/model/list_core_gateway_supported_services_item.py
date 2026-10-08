# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCoreGatewaySupportedServicesItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description_zh': 'str',
        'description_en': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description_zh': 'description_zh',
        'description_en': 'description_en'
    }

    def __init__(self, name=None, description_zh=None, description_en=None):
        r"""ListCoreGatewaySupportedServicesItem

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 网关支持的主力核心服务名称英文缩写。 **取值范围：** 长度为1-36个字符。 
        :type name: str
        :param description_zh: **参数解释：** 网关支持的主力核心服务中文名称。 **取值范围：** 长度为1-36个字符。 
        :type description_zh: str
        :param description_en: **参数解释：** 网关支持的主力核心服务英文名称。 **取值范围：** 长度为1-36个字符。 
        :type description_en: str
        """
        
        

        self._name = None
        self._description_zh = None
        self._description_en = None
        self.discriminator = None

        self.name = name
        self.description_zh = description_zh
        self.description_en = description_en

    @property
    def name(self):
        r"""Gets the name of this ListCoreGatewaySupportedServicesItem.

        **参数解释：** 网关支持的主力核心服务名称英文缩写。 **取值范围：** 长度为1-36个字符。 

        :return: The name of this ListCoreGatewaySupportedServicesItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListCoreGatewaySupportedServicesItem.

        **参数解释：** 网关支持的主力核心服务名称英文缩写。 **取值范围：** 长度为1-36个字符。 

        :param name: The name of this ListCoreGatewaySupportedServicesItem.
        :type name: str
        """
        self._name = name

    @property
    def description_zh(self):
        r"""Gets the description_zh of this ListCoreGatewaySupportedServicesItem.

        **参数解释：** 网关支持的主力核心服务中文名称。 **取值范围：** 长度为1-36个字符。 

        :return: The description_zh of this ListCoreGatewaySupportedServicesItem.
        :rtype: str
        """
        return self._description_zh

    @description_zh.setter
    def description_zh(self, description_zh):
        r"""Sets the description_zh of this ListCoreGatewaySupportedServicesItem.

        **参数解释：** 网关支持的主力核心服务中文名称。 **取值范围：** 长度为1-36个字符。 

        :param description_zh: The description_zh of this ListCoreGatewaySupportedServicesItem.
        :type description_zh: str
        """
        self._description_zh = description_zh

    @property
    def description_en(self):
        r"""Gets the description_en of this ListCoreGatewaySupportedServicesItem.

        **参数解释：** 网关支持的主力核心服务英文名称。 **取值范围：** 长度为1-36个字符。 

        :return: The description_en of this ListCoreGatewaySupportedServicesItem.
        :rtype: str
        """
        return self._description_en

    @description_en.setter
    def description_en(self, description_en):
        r"""Sets the description_en of this ListCoreGatewaySupportedServicesItem.

        **参数解释：** 网关支持的主力核心服务英文名称。 **取值范围：** 长度为1-36个字符。 

        :param description_en: The description_en of this ListCoreGatewaySupportedServicesItem.
        :type description_en: str
        """
        self._description_en = description_en

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
        if not isinstance(other, ListCoreGatewaySupportedServicesItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
