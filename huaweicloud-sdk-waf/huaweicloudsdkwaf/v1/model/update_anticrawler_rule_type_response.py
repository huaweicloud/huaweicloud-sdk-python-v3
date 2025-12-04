# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAnticrawlerRuleTypeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'anticrawler_type': 'str'
    }

    attribute_map = {
        'anticrawler_type': 'anticrawler_type'
    }

    def __init__(self, anticrawler_type=None):
        r"""UpdateAnticrawlerRuleTypeResponse

        The model defined in huaweicloud sdk

        :param anticrawler_type: **参数解释：** JS脚本反爬虫规则类型 **约束限制：** 不涉及 **取值范围：**  - anticrawler_except_url: 防护所有路径模式，在该模式下，查询的JS脚本反爬虫规则为排除的防护路径规则  - anticrawler_specific_url: 防护指定路径模式，在该模式下，查询的JS脚本反爬虫规则为指定要防护的路径规则  **默认取值：** anticrawler_except_url
        :type anticrawler_type: str
        """
        
        super().__init__()

        self._anticrawler_type = None
        self.discriminator = None

        if anticrawler_type is not None:
            self.anticrawler_type = anticrawler_type

    @property
    def anticrawler_type(self):
        r"""Gets the anticrawler_type of this UpdateAnticrawlerRuleTypeResponse.

        **参数解释：** JS脚本反爬虫规则类型 **约束限制：** 不涉及 **取值范围：**  - anticrawler_except_url: 防护所有路径模式，在该模式下，查询的JS脚本反爬虫规则为排除的防护路径规则  - anticrawler_specific_url: 防护指定路径模式，在该模式下，查询的JS脚本反爬虫规则为指定要防护的路径规则  **默认取值：** anticrawler_except_url

        :return: The anticrawler_type of this UpdateAnticrawlerRuleTypeResponse.
        :rtype: str
        """
        return self._anticrawler_type

    @anticrawler_type.setter
    def anticrawler_type(self, anticrawler_type):
        r"""Sets the anticrawler_type of this UpdateAnticrawlerRuleTypeResponse.

        **参数解释：** JS脚本反爬虫规则类型 **约束限制：** 不涉及 **取值范围：**  - anticrawler_except_url: 防护所有路径模式，在该模式下，查询的JS脚本反爬虫规则为排除的防护路径规则  - anticrawler_specific_url: 防护指定路径模式，在该模式下，查询的JS脚本反爬虫规则为指定要防护的路径规则  **默认取值：** anticrawler_except_url

        :param anticrawler_type: The anticrawler_type of this UpdateAnticrawlerRuleTypeResponse.
        :type anticrawler_type: str
        """
        self._anticrawler_type = anticrawler_type

    def to_dict(self):
        import warnings
        warnings.warn("UpdateAnticrawlerRuleTypeResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, UpdateAnticrawlerRuleTypeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
