# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VendorAuthInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ak': 'str',
        'sk': 'str',
        'api_key': 'str'
    }

    attribute_map = {
        'ak': 'ak',
        'sk': 'sk',
        'api_key': 'api_key'
    }

    def __init__(self, ak=None, sk=None, api_key=None):
        r"""VendorAuthInfo

        The model defined in huaweicloud sdk

        :param ak: **参数解释**： ak。 **约束限制**： 不涉及 **取值范围**： 字符长度为[1-1024]。 **默认取值**： 不涉及 
        :type ak: str
        :param sk: **参数解释**： sk。 **约束限制**： 不涉及 **取值范围**： 字符长度为[1-1024]。 **默认取值**： 不涉及 
        :type sk: str
        :param api_key: **参数解释**： api_key。 **约束限制**： 不涉及 **取值范围**： 字符长度为[1-1024]。 **默认取值**： 不涉及 
        :type api_key: str
        """
        
        

        self._ak = None
        self._sk = None
        self._api_key = None
        self.discriminator = None

        if ak is not None:
            self.ak = ak
        if sk is not None:
            self.sk = sk
        if api_key is not None:
            self.api_key = api_key

    @property
    def ak(self):
        r"""Gets the ak of this VendorAuthInfo.

        **参数解释**： ak。 **约束限制**： 不涉及 **取值范围**： 字符长度为[1-1024]。 **默认取值**： 不涉及 

        :return: The ak of this VendorAuthInfo.
        :rtype: str
        """
        return self._ak

    @ak.setter
    def ak(self, ak):
        r"""Sets the ak of this VendorAuthInfo.

        **参数解释**： ak。 **约束限制**： 不涉及 **取值范围**： 字符长度为[1-1024]。 **默认取值**： 不涉及 

        :param ak: The ak of this VendorAuthInfo.
        :type ak: str
        """
        self._ak = ak

    @property
    def sk(self):
        r"""Gets the sk of this VendorAuthInfo.

        **参数解释**： sk。 **约束限制**： 不涉及 **取值范围**： 字符长度为[1-1024]。 **默认取值**： 不涉及 

        :return: The sk of this VendorAuthInfo.
        :rtype: str
        """
        return self._sk

    @sk.setter
    def sk(self, sk):
        r"""Sets the sk of this VendorAuthInfo.

        **参数解释**： sk。 **约束限制**： 不涉及 **取值范围**： 字符长度为[1-1024]。 **默认取值**： 不涉及 

        :param sk: The sk of this VendorAuthInfo.
        :type sk: str
        """
        self._sk = sk

    @property
    def api_key(self):
        r"""Gets the api_key of this VendorAuthInfo.

        **参数解释**： api_key。 **约束限制**： 不涉及 **取值范围**： 字符长度为[1-1024]。 **默认取值**： 不涉及 

        :return: The api_key of this VendorAuthInfo.
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        r"""Sets the api_key of this VendorAuthInfo.

        **参数解释**： api_key。 **约束限制**： 不涉及 **取值范围**： 字符长度为[1-1024]。 **默认取值**： 不涉及 

        :param api_key: The api_key of this VendorAuthInfo.
        :type api_key: str
        """
        self._api_key = api_key

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
        if not isinstance(other, VendorAuthInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
