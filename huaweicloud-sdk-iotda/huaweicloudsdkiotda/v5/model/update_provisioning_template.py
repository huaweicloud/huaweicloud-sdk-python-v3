# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateProvisioningTemplate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'template_body': 'ProvisioningTemplateBody'
    }

    attribute_map = {
        'description': 'description',
        'template_body': 'template_body'
    }

    def __init__(self, description=None, template_body=None):
        r"""UpdateProvisioningTemplate

        The model defined in huaweicloud sdk

        :param description: **参数说明**：预调配模板的描述信息。 **取值范围**：长度不超过2048，只允许中文、字母、数字、以及_?&#39;#().,&amp;%@!-等字符的组合
        :type description: str
        :param template_body: 
        :type template_body: :class:`huaweicloudsdkiotda.v5.ProvisioningTemplateBody`
        """
        
        

        self._description = None
        self._template_body = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if template_body is not None:
            self.template_body = template_body

    @property
    def description(self):
        r"""Gets the description of this UpdateProvisioningTemplate.

        **参数说明**：预调配模板的描述信息。 **取值范围**：长度不超过2048，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合

        :return: The description of this UpdateProvisioningTemplate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateProvisioningTemplate.

        **参数说明**：预调配模板的描述信息。 **取值范围**：长度不超过2048，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合

        :param description: The description of this UpdateProvisioningTemplate.
        :type description: str
        """
        self._description = description

    @property
    def template_body(self):
        r"""Gets the template_body of this UpdateProvisioningTemplate.

        :return: The template_body of this UpdateProvisioningTemplate.
        :rtype: :class:`huaweicloudsdkiotda.v5.ProvisioningTemplateBody`
        """
        return self._template_body

    @template_body.setter
    def template_body(self, template_body):
        r"""Sets the template_body of this UpdateProvisioningTemplate.

        :param template_body: The template_body of this UpdateProvisioningTemplate.
        :type template_body: :class:`huaweicloudsdkiotda.v5.ProvisioningTemplateBody`
        """
        self._template_body = template_body

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
        if not isinstance(other, UpdateProvisioningTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
