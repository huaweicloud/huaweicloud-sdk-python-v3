# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyCicdConfigurationRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vulnerability_whitelist': 'list[str]',
        'vulnerability_blocklist': 'list[str]',
        'image_whitelist': 'list[str]'
    }

    attribute_map = {
        'vulnerability_whitelist': 'vulnerability_whitelist',
        'vulnerability_blocklist': 'vulnerability_blocklist',
        'image_whitelist': 'image_whitelist'
    }

    def __init__(self, vulnerability_whitelist=None, vulnerability_blocklist=None, image_whitelist=None):
        r"""ModifyCicdConfigurationRequestBody

        The model defined in huaweicloud sdk

        :param vulnerability_whitelist: **参数解释** 漏洞白名单 **约束限制** 不涉及 **取值范围** 白名单数量范围0-1000  **默认取值** 不涉及
        :type vulnerability_whitelist: list[str]
        :param vulnerability_blocklist: **参数解释** 漏洞黑名单 **约束限制** 不涉及 **取值范围** 黑名单数量范围0-1000  **默认取值** 不涉及
        :type vulnerability_blocklist: list[str]
        :param image_whitelist: **参数解释** 镜像白名单 **约束限制** 不涉及 **取值范围** 白名单数量范围0-1000  **默认取值** 不涉及
        :type image_whitelist: list[str]
        """
        
        

        self._vulnerability_whitelist = None
        self._vulnerability_blocklist = None
        self._image_whitelist = None
        self.discriminator = None

        if vulnerability_whitelist is not None:
            self.vulnerability_whitelist = vulnerability_whitelist
        if vulnerability_blocklist is not None:
            self.vulnerability_blocklist = vulnerability_blocklist
        if image_whitelist is not None:
            self.image_whitelist = image_whitelist

    @property
    def vulnerability_whitelist(self):
        r"""Gets the vulnerability_whitelist of this ModifyCicdConfigurationRequestBody.

        **参数解释** 漏洞白名单 **约束限制** 不涉及 **取值范围** 白名单数量范围0-1000  **默认取值** 不涉及

        :return: The vulnerability_whitelist of this ModifyCicdConfigurationRequestBody.
        :rtype: list[str]
        """
        return self._vulnerability_whitelist

    @vulnerability_whitelist.setter
    def vulnerability_whitelist(self, vulnerability_whitelist):
        r"""Sets the vulnerability_whitelist of this ModifyCicdConfigurationRequestBody.

        **参数解释** 漏洞白名单 **约束限制** 不涉及 **取值范围** 白名单数量范围0-1000  **默认取值** 不涉及

        :param vulnerability_whitelist: The vulnerability_whitelist of this ModifyCicdConfigurationRequestBody.
        :type vulnerability_whitelist: list[str]
        """
        self._vulnerability_whitelist = vulnerability_whitelist

    @property
    def vulnerability_blocklist(self):
        r"""Gets the vulnerability_blocklist of this ModifyCicdConfigurationRequestBody.

        **参数解释** 漏洞黑名单 **约束限制** 不涉及 **取值范围** 黑名单数量范围0-1000  **默认取值** 不涉及

        :return: The vulnerability_blocklist of this ModifyCicdConfigurationRequestBody.
        :rtype: list[str]
        """
        return self._vulnerability_blocklist

    @vulnerability_blocklist.setter
    def vulnerability_blocklist(self, vulnerability_blocklist):
        r"""Sets the vulnerability_blocklist of this ModifyCicdConfigurationRequestBody.

        **参数解释** 漏洞黑名单 **约束限制** 不涉及 **取值范围** 黑名单数量范围0-1000  **默认取值** 不涉及

        :param vulnerability_blocklist: The vulnerability_blocklist of this ModifyCicdConfigurationRequestBody.
        :type vulnerability_blocklist: list[str]
        """
        self._vulnerability_blocklist = vulnerability_blocklist

    @property
    def image_whitelist(self):
        r"""Gets the image_whitelist of this ModifyCicdConfigurationRequestBody.

        **参数解释** 镜像白名单 **约束限制** 不涉及 **取值范围** 白名单数量范围0-1000  **默认取值** 不涉及

        :return: The image_whitelist of this ModifyCicdConfigurationRequestBody.
        :rtype: list[str]
        """
        return self._image_whitelist

    @image_whitelist.setter
    def image_whitelist(self, image_whitelist):
        r"""Sets the image_whitelist of this ModifyCicdConfigurationRequestBody.

        **参数解释** 镜像白名单 **约束限制** 不涉及 **取值范围** 白名单数量范围0-1000  **默认取值** 不涉及

        :param image_whitelist: The image_whitelist of this ModifyCicdConfigurationRequestBody.
        :type image_whitelist: list[str]
        """
        self._image_whitelist = image_whitelist

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
        if not isinstance(other, ModifyCicdConfigurationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
