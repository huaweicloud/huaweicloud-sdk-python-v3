# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MsgTemplateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_id': 'str',
        'signature_id': 'str',
        'template_content': 'str',
        'template_desc': 'str',
        'template_name': 'str',
        'template_type': 'str',
        'universal_template': 'str',
        'variable_attributes': 'list[VariableAttributes]'
    }

    attribute_map = {
        'app_id': 'app_id',
        'signature_id': 'signature_id',
        'template_content': 'template_content',
        'template_desc': 'template_desc',
        'template_name': 'template_name',
        'template_type': 'template_type',
        'universal_template': 'universal_template',
        'variable_attributes': 'variable_attributes'
    }

    def __init__(self, app_id=None, signature_id=None, template_content=None, template_desc=None, template_name=None, template_type=None, universal_template=None, variable_attributes=None):
        r"""MsgTemplateRequest

        The model defined in huaweicloud sdk

        :param app_id: 应用ID，默认取签名所属的应用ID。
        :type app_id: str
        :param signature_id: 签名ID。
        :type signature_id: str
        :param template_content: 模板内容。
        :type template_content: str
        :param template_desc: 模板描述。
        :type template_desc: str
        :param template_name: 模板名称。
        :type template_name: str
        :param template_type: 模板类型。默认取所属签名的签名类型。PROMOTION_TYPE：营销类，NOTIFY_TYPE：通知类。
        :type template_type: str
        :param universal_template: 是否为通用模板(暂不支持通用模板)。0：非通用模板，1：通用模板。
        :type universal_template: str
        :param variable_attributes: 模板参数。
        :type variable_attributes: list[:class:`huaweicloudsdkkoomessage.v1.VariableAttributes`]
        """
        
        

        self._app_id = None
        self._signature_id = None
        self._template_content = None
        self._template_desc = None
        self._template_name = None
        self._template_type = None
        self._universal_template = None
        self._variable_attributes = None
        self.discriminator = None

        if app_id is not None:
            self.app_id = app_id
        self.signature_id = signature_id
        self.template_content = template_content
        if template_desc is not None:
            self.template_desc = template_desc
        self.template_name = template_name
        if template_type is not None:
            self.template_type = template_type
        if universal_template is not None:
            self.universal_template = universal_template
        self.variable_attributes = variable_attributes

    @property
    def app_id(self):
        r"""Gets the app_id of this MsgTemplateRequest.

        应用ID，默认取签名所属的应用ID。

        :return: The app_id of this MsgTemplateRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this MsgTemplateRequest.

        应用ID，默认取签名所属的应用ID。

        :param app_id: The app_id of this MsgTemplateRequest.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def signature_id(self):
        r"""Gets the signature_id of this MsgTemplateRequest.

        签名ID。

        :return: The signature_id of this MsgTemplateRequest.
        :rtype: str
        """
        return self._signature_id

    @signature_id.setter
    def signature_id(self, signature_id):
        r"""Sets the signature_id of this MsgTemplateRequest.

        签名ID。

        :param signature_id: The signature_id of this MsgTemplateRequest.
        :type signature_id: str
        """
        self._signature_id = signature_id

    @property
    def template_content(self):
        r"""Gets the template_content of this MsgTemplateRequest.

        模板内容。

        :return: The template_content of this MsgTemplateRequest.
        :rtype: str
        """
        return self._template_content

    @template_content.setter
    def template_content(self, template_content):
        r"""Sets the template_content of this MsgTemplateRequest.

        模板内容。

        :param template_content: The template_content of this MsgTemplateRequest.
        :type template_content: str
        """
        self._template_content = template_content

    @property
    def template_desc(self):
        r"""Gets the template_desc of this MsgTemplateRequest.

        模板描述。

        :return: The template_desc of this MsgTemplateRequest.
        :rtype: str
        """
        return self._template_desc

    @template_desc.setter
    def template_desc(self, template_desc):
        r"""Sets the template_desc of this MsgTemplateRequest.

        模板描述。

        :param template_desc: The template_desc of this MsgTemplateRequest.
        :type template_desc: str
        """
        self._template_desc = template_desc

    @property
    def template_name(self):
        r"""Gets the template_name of this MsgTemplateRequest.

        模板名称。

        :return: The template_name of this MsgTemplateRequest.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this MsgTemplateRequest.

        模板名称。

        :param template_name: The template_name of this MsgTemplateRequest.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def template_type(self):
        r"""Gets the template_type of this MsgTemplateRequest.

        模板类型。默认取所属签名的签名类型。PROMOTION_TYPE：营销类，NOTIFY_TYPE：通知类。

        :return: The template_type of this MsgTemplateRequest.
        :rtype: str
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        r"""Sets the template_type of this MsgTemplateRequest.

        模板类型。默认取所属签名的签名类型。PROMOTION_TYPE：营销类，NOTIFY_TYPE：通知类。

        :param template_type: The template_type of this MsgTemplateRequest.
        :type template_type: str
        """
        self._template_type = template_type

    @property
    def universal_template(self):
        r"""Gets the universal_template of this MsgTemplateRequest.

        是否为通用模板(暂不支持通用模板)。0：非通用模板，1：通用模板。

        :return: The universal_template of this MsgTemplateRequest.
        :rtype: str
        """
        return self._universal_template

    @universal_template.setter
    def universal_template(self, universal_template):
        r"""Sets the universal_template of this MsgTemplateRequest.

        是否为通用模板(暂不支持通用模板)。0：非通用模板，1：通用模板。

        :param universal_template: The universal_template of this MsgTemplateRequest.
        :type universal_template: str
        """
        self._universal_template = universal_template

    @property
    def variable_attributes(self):
        r"""Gets the variable_attributes of this MsgTemplateRequest.

        模板参数。

        :return: The variable_attributes of this MsgTemplateRequest.
        :rtype: list[:class:`huaweicloudsdkkoomessage.v1.VariableAttributes`]
        """
        return self._variable_attributes

    @variable_attributes.setter
    def variable_attributes(self, variable_attributes):
        r"""Sets the variable_attributes of this MsgTemplateRequest.

        模板参数。

        :param variable_attributes: The variable_attributes of this MsgTemplateRequest.
        :type variable_attributes: list[:class:`huaweicloudsdkkoomessage.v1.VariableAttributes`]
        """
        self._variable_attributes = variable_attributes

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
        if not isinstance(other, MsgTemplateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
