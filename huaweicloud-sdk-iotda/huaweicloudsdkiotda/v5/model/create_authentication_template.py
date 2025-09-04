# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAuthenticationTemplate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_name': 'str',
        'description': 'str',
        'status': 'str',
        'template_body': 'AuthenticationTemplateBody'
    }

    attribute_map = {
        'template_name': 'template_name',
        'description': 'description',
        'status': 'status',
        'template_body': 'template_body'
    }

    def __init__(self, template_name=None, description=None, status=None, template_body=None):
        r"""CreateAuthenticationTemplate

        The model defined in huaweicloud sdk

        :param template_name: **参数说明**：鉴权模板名称。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type template_name: str
        :param description: **参数说明**：鉴权模板的描述信息。 **取值范围**：长度不超过2048，只允许中文、字母、数字、以及_?&#39;#().,&amp;%@!-等字符的组合
        :type description: str
        :param status: **参数说明**：是否激活该鉴权模板，默认状态为未激活，只能有一个激活状态模板 - ACTIVE：该鉴权模板为激活状态。 - INACTIVE：该鉴权模板为停用状态。
        :type status: str
        :param template_body: 
        :type template_body: :class:`huaweicloudsdkiotda.v5.AuthenticationTemplateBody`
        """
        
        

        self._template_name = None
        self._description = None
        self._status = None
        self._template_body = None
        self.discriminator = None

        self.template_name = template_name
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        self.template_body = template_body

    @property
    def template_name(self):
        r"""Gets the template_name of this CreateAuthenticationTemplate.

        **参数说明**：鉴权模板名称。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The template_name of this CreateAuthenticationTemplate.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this CreateAuthenticationTemplate.

        **参数说明**：鉴权模板名称。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param template_name: The template_name of this CreateAuthenticationTemplate.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def description(self):
        r"""Gets the description of this CreateAuthenticationTemplate.

        **参数说明**：鉴权模板的描述信息。 **取值范围**：长度不超过2048，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合

        :return: The description of this CreateAuthenticationTemplate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateAuthenticationTemplate.

        **参数说明**：鉴权模板的描述信息。 **取值范围**：长度不超过2048，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合

        :param description: The description of this CreateAuthenticationTemplate.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this CreateAuthenticationTemplate.

        **参数说明**：是否激活该鉴权模板，默认状态为未激活，只能有一个激活状态模板 - ACTIVE：该鉴权模板为激活状态。 - INACTIVE：该鉴权模板为停用状态。

        :return: The status of this CreateAuthenticationTemplate.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateAuthenticationTemplate.

        **参数说明**：是否激活该鉴权模板，默认状态为未激活，只能有一个激活状态模板 - ACTIVE：该鉴权模板为激活状态。 - INACTIVE：该鉴权模板为停用状态。

        :param status: The status of this CreateAuthenticationTemplate.
        :type status: str
        """
        self._status = status

    @property
    def template_body(self):
        r"""Gets the template_body of this CreateAuthenticationTemplate.

        :return: The template_body of this CreateAuthenticationTemplate.
        :rtype: :class:`huaweicloudsdkiotda.v5.AuthenticationTemplateBody`
        """
        return self._template_body

    @template_body.setter
    def template_body(self, template_body):
        r"""Sets the template_body of this CreateAuthenticationTemplate.

        :param template_body: The template_body of this CreateAuthenticationTemplate.
        :type template_body: :class:`huaweicloudsdkiotda.v5.AuthenticationTemplateBody`
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
        if not isinstance(other, CreateAuthenticationTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
