# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmsContent:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "SmsContent"

    sensitive_list = []

    openapi_types = {
        'to': 'list[str]',
        'template_id': 'str',
        'template_paras': 'list[str]',
        'signature': 'str'
    }

    attribute_map = {
        'to': 'to',
        'template_id': 'templateId',
        'template_paras': 'templateParas',
        'signature': 'signature'
    }

    def __init__(self, to=None, template_id=None, template_paras=None, signature=None):
        r"""SmsContent

        The model defined in huaweicloud sdk

        :param to: 群发短信接收方的号码
        :type to: list[str]
        :param template_id: 短信模板ID
        :type template_id: str
        :param template_paras: 短信模板的变量值列表
        :type template_paras: list[str]
        :param signature: 短信签名
        :type signature: str
        """
        
        

        self._to = None
        self._template_id = None
        self._template_paras = None
        self._signature = None
        self.discriminator = None

        if to is not None:
            self.to = to
        if template_id is not None:
            self.template_id = template_id
        if template_paras is not None:
            self.template_paras = template_paras
        if signature is not None:
            self.signature = signature

    @property
    def to(self):
        r"""Gets the to of this SmsContent.

        群发短信接收方的号码

        :return: The to of this SmsContent.
        :rtype: list[str]
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this SmsContent.

        群发短信接收方的号码

        :param to: The to of this SmsContent.
        :type to: list[str]
        """
        self._to = to

    @property
    def template_id(self):
        r"""Gets the template_id of this SmsContent.

        短信模板ID

        :return: The template_id of this SmsContent.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this SmsContent.

        短信模板ID

        :param template_id: The template_id of this SmsContent.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def template_paras(self):
        r"""Gets the template_paras of this SmsContent.

        短信模板的变量值列表

        :return: The template_paras of this SmsContent.
        :rtype: list[str]
        """
        return self._template_paras

    @template_paras.setter
    def template_paras(self, template_paras):
        r"""Sets the template_paras of this SmsContent.

        短信模板的变量值列表

        :param template_paras: The template_paras of this SmsContent.
        :type template_paras: list[str]
        """
        self._template_paras = template_paras

    @property
    def signature(self):
        r"""Gets the signature of this SmsContent.

        短信签名

        :return: The signature of this SmsContent.
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        r"""Sets the signature of this SmsContent.

        短信签名

        :param signature: The signature of this SmsContent.
        :type signature: str
        """
        self._signature = signature

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
        if not isinstance(other, SmsContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
