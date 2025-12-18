# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPackageProductsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'locale': 'str'
    }

    attribute_map = {
        'locale': 'locale'
    }

    def __init__(self, locale=None):
        r"""ListPackageProductsRequest

        The model defined in huaweicloud sdk

        :param locale: **参数解释**： 参数表示用户的语言/所在区域。根据 locale 参数，系统会返回适合该语言/区域的套餐包名称。 **约束限制：** 不涉及 **取值范围**： - zh-cn: 显示中文名称，例如：“Autopilot 通用型 1,000 核时CPU月包” - en-us: 显示英文名称，例如：“Autopilot General Computing 1,000 vCPU-hours CPU monthly package”  **默认取值：** zh-cn
        :type locale: str
        """
        
        

        self._locale = None
        self.discriminator = None

        if locale is not None:
            self.locale = locale

    @property
    def locale(self):
        r"""Gets the locale of this ListPackageProductsRequest.

        **参数解释**： 参数表示用户的语言/所在区域。根据 locale 参数，系统会返回适合该语言/区域的套餐包名称。 **约束限制：** 不涉及 **取值范围**： - zh-cn: 显示中文名称，例如：“Autopilot 通用型 1,000 核时CPU月包” - en-us: 显示英文名称，例如：“Autopilot General Computing 1,000 vCPU-hours CPU monthly package”  **默认取值：** zh-cn

        :return: The locale of this ListPackageProductsRequest.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        r"""Sets the locale of this ListPackageProductsRequest.

        **参数解释**： 参数表示用户的语言/所在区域。根据 locale 参数，系统会返回适合该语言/区域的套餐包名称。 **约束限制：** 不涉及 **取值范围**： - zh-cn: 显示中文名称，例如：“Autopilot 通用型 1,000 核时CPU月包” - en-us: 显示英文名称，例如：“Autopilot General Computing 1,000 vCPU-hours CPU monthly package”  **默认取值：** zh-cn

        :param locale: The locale of this ListPackageProductsRequest.
        :type locale: str
        """
        self._locale = locale

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
        if not isinstance(other, ListPackageProductsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
