# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PreviewTemplateBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'templates': 'str',
        'language': 'str',
        'source': 'str'
    }

    attribute_map = {
        'templates': 'templates',
        'language': 'language',
        'source': 'source'
    }

    def __init__(self, templates=None, language=None, source=None):
        """PreviewTemplateBody

        The model defined in huaweicloud sdk

        :param templates: 邮件模板内容
        :type templates: str
        :param language: 语言 zh-cn中文，en-us英文
        :type language: str
        :param source: 来源，只能填LTS
        :type source: str
        """
        
        

        self._templates = None
        self._language = None
        self._source = None
        self.discriminator = None

        self.templates = templates
        self.language = language
        self.source = source

    @property
    def templates(self):
        """Gets the templates of this PreviewTemplateBody.

        邮件模板内容

        :return: The templates of this PreviewTemplateBody.
        :rtype: str
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        """Sets the templates of this PreviewTemplateBody.

        邮件模板内容

        :param templates: The templates of this PreviewTemplateBody.
        :type templates: str
        """
        self._templates = templates

    @property
    def language(self):
        """Gets the language of this PreviewTemplateBody.

        语言 zh-cn中文，en-us英文

        :return: The language of this PreviewTemplateBody.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this PreviewTemplateBody.

        语言 zh-cn中文，en-us英文

        :param language: The language of this PreviewTemplateBody.
        :type language: str
        """
        self._language = language

    @property
    def source(self):
        """Gets the source of this PreviewTemplateBody.

        来源，只能填LTS

        :return: The source of this PreviewTemplateBody.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this PreviewTemplateBody.

        来源，只能填LTS

        :param source: The source of this PreviewTemplateBody.
        :type source: str
        """
        self._source = source

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
        if not isinstance(other, PreviewTemplateBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
