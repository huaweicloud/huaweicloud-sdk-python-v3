# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSecurityReportLogoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'logo_content': 'str',
        'logo_name': 'str'
    }

    attribute_map = {
        'logo_content': 'logo_content',
        'logo_name': 'logo_name'
    }

    def __init__(self, logo_content=None, logo_name=None):
        r"""ShowSecurityReportLogoResponse

        The model defined in huaweicloud sdk

        :param logo_content: **参数解释**： logo文件base64内容 **取值范围**： 字符长度32-36位 
        :type logo_content: str
        :param logo_name: **参数解释**： logo文件名称 **取值范围**： 字符长度0-128位 
        :type logo_name: str
        """
        
        super().__init__()

        self._logo_content = None
        self._logo_name = None
        self.discriminator = None

        if logo_content is not None:
            self.logo_content = logo_content
        if logo_name is not None:
            self.logo_name = logo_name

    @property
    def logo_content(self):
        r"""Gets the logo_content of this ShowSecurityReportLogoResponse.

        **参数解释**： logo文件base64内容 **取值范围**： 字符长度32-36位 

        :return: The logo_content of this ShowSecurityReportLogoResponse.
        :rtype: str
        """
        return self._logo_content

    @logo_content.setter
    def logo_content(self, logo_content):
        r"""Sets the logo_content of this ShowSecurityReportLogoResponse.

        **参数解释**： logo文件base64内容 **取值范围**： 字符长度32-36位 

        :param logo_content: The logo_content of this ShowSecurityReportLogoResponse.
        :type logo_content: str
        """
        self._logo_content = logo_content

    @property
    def logo_name(self):
        r"""Gets the logo_name of this ShowSecurityReportLogoResponse.

        **参数解释**： logo文件名称 **取值范围**： 字符长度0-128位 

        :return: The logo_name of this ShowSecurityReportLogoResponse.
        :rtype: str
        """
        return self._logo_name

    @logo_name.setter
    def logo_name(self, logo_name):
        r"""Sets the logo_name of this ShowSecurityReportLogoResponse.

        **参数解释**： logo文件名称 **取值范围**： 字符长度0-128位 

        :param logo_name: The logo_name of this ShowSecurityReportLogoResponse.
        :type logo_name: str
        """
        self._logo_name = logo_name

    def to_dict(self):
        import warnings
        warnings.warn("ShowSecurityReportLogoResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowSecurityReportLogoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
