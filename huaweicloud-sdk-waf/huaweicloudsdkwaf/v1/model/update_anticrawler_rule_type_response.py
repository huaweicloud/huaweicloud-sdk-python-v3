# coding: utf-8

import six

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
        """UpdateAnticrawlerRuleTypeResponse

        The model defined in huaweicloud sdk

        :param anticrawler_type: JS脚本反爬虫规则类型，指定防护路径：anticrawler_specific_url 排除防护路径：anticrawler_except_url
        :type anticrawler_type: str
        """
        
        super(UpdateAnticrawlerRuleTypeResponse, self).__init__()

        self._anticrawler_type = None
        self.discriminator = None

        if anticrawler_type is not None:
            self.anticrawler_type = anticrawler_type

    @property
    def anticrawler_type(self):
        """Gets the anticrawler_type of this UpdateAnticrawlerRuleTypeResponse.

        JS脚本反爬虫规则类型，指定防护路径：anticrawler_specific_url 排除防护路径：anticrawler_except_url

        :return: The anticrawler_type of this UpdateAnticrawlerRuleTypeResponse.
        :rtype: str
        """
        return self._anticrawler_type

    @anticrawler_type.setter
    def anticrawler_type(self, anticrawler_type):
        """Sets the anticrawler_type of this UpdateAnticrawlerRuleTypeResponse.

        JS脚本反爬虫规则类型，指定防护路径：anticrawler_specific_url 排除防护路径：anticrawler_except_url

        :param anticrawler_type: The anticrawler_type of this UpdateAnticrawlerRuleTypeResponse.
        :type anticrawler_type: str
        """
        self._anticrawler_type = anticrawler_type

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
        if not isinstance(other, UpdateAnticrawlerRuleTypeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
