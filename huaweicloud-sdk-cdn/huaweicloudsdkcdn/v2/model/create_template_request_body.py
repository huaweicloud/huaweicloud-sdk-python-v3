# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTemplateRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tml_name': 'str',
        'remark': 'str',
        'configs': 'TemplateConfigs'
    }

    attribute_map = {
        'tml_name': 'tml_name',
        'remark': 'remark',
        'configs': 'configs'
    }

    def __init__(self, tml_name=None, remark=None, configs=None):
        r"""CreateTemplateRequestBody

        The model defined in huaweicloud sdk

        :param tml_name: **参数解释：** 域名模板名称 **约束限制：** 不涉及 **取值范围：** - 1-100个字符 - 仅支持字母、数字、中文、下划线（_）、中横线（-） **默认取值：** 不涉及
        :type tml_name: str
        :param remark: **参数解释：** 域名模板描述 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type remark: str
        :param configs: 
        :type configs: :class:`huaweicloudsdkcdn.v2.TemplateConfigs`
        """
        
        

        self._tml_name = None
        self._remark = None
        self._configs = None
        self.discriminator = None

        self.tml_name = tml_name
        if remark is not None:
            self.remark = remark
        self.configs = configs

    @property
    def tml_name(self):
        r"""Gets the tml_name of this CreateTemplateRequestBody.

        **参数解释：** 域名模板名称 **约束限制：** 不涉及 **取值范围：** - 1-100个字符 - 仅支持字母、数字、中文、下划线（_）、中横线（-） **默认取值：** 不涉及

        :return: The tml_name of this CreateTemplateRequestBody.
        :rtype: str
        """
        return self._tml_name

    @tml_name.setter
    def tml_name(self, tml_name):
        r"""Sets the tml_name of this CreateTemplateRequestBody.

        **参数解释：** 域名模板名称 **约束限制：** 不涉及 **取值范围：** - 1-100个字符 - 仅支持字母、数字、中文、下划线（_）、中横线（-） **默认取值：** 不涉及

        :param tml_name: The tml_name of this CreateTemplateRequestBody.
        :type tml_name: str
        """
        self._tml_name = tml_name

    @property
    def remark(self):
        r"""Gets the remark of this CreateTemplateRequestBody.

        **参数解释：** 域名模板描述 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The remark of this CreateTemplateRequestBody.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this CreateTemplateRequestBody.

        **参数解释：** 域名模板描述 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param remark: The remark of this CreateTemplateRequestBody.
        :type remark: str
        """
        self._remark = remark

    @property
    def configs(self):
        r"""Gets the configs of this CreateTemplateRequestBody.

        :return: The configs of this CreateTemplateRequestBody.
        :rtype: :class:`huaweicloudsdkcdn.v2.TemplateConfigs`
        """
        return self._configs

    @configs.setter
    def configs(self, configs):
        r"""Sets the configs of this CreateTemplateRequestBody.

        :param configs: The configs of this CreateTemplateRequestBody.
        :type configs: :class:`huaweicloudsdkcdn.v2.TemplateConfigs`
        """
        self._configs = configs

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
        if not isinstance(other, CreateTemplateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
