# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PropertiesSchema:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'context': 'str',
        'docstring': 'str',
        'ide_type': 'str',
        'ide_version': 'str',
        'language': 'str',
        'plugin_version': 'str',
        'signature': 'str',
        'above_text': 'str',
        'following_text': 'str'
    }

    attribute_map = {
        'context': 'context',
        'docstring': 'docstring',
        'ide_type': 'ide_type',
        'ide_version': 'ide_version',
        'language': 'language',
        'plugin_version': 'plugin_version',
        'signature': 'signature',
        'above_text': 'above_text',
        'following_text': 'following_text'
    }

    def __init__(self, context=None, docstring=None, ide_type=None, ide_version=None, language=None, plugin_version=None, signature=None, above_text=None, following_text=None):
        """PropertiesSchema

        The model defined in huaweicloud sdk

        :param context: context
        :type context: str
        :param docstring: docstring
        :type docstring: str
        :param ide_type: the type of ide
        :type ide_type: str
        :param ide_version: the version of ide
        :type ide_version: str
        :param language: code language
        :type language: str
        :param plugin_version: the version of plugin
        :type plugin_version: str
        :param signature: signature
        :type signature: str
        :param above_text: the text above the cursor
        :type above_text: str
        :param following_text: the text following the cursor
        :type following_text: str
        """
        
        

        self._context = None
        self._docstring = None
        self._ide_type = None
        self._ide_version = None
        self._language = None
        self._plugin_version = None
        self._signature = None
        self._above_text = None
        self._following_text = None
        self.discriminator = None

        if context is not None:
            self.context = context
        if docstring is not None:
            self.docstring = docstring
        if ide_type is not None:
            self.ide_type = ide_type
        if ide_version is not None:
            self.ide_version = ide_version
        self.language = language
        if plugin_version is not None:
            self.plugin_version = plugin_version
        if signature is not None:
            self.signature = signature
        if above_text is not None:
            self.above_text = above_text
        if following_text is not None:
            self.following_text = following_text

    @property
    def context(self):
        """Gets the context of this PropertiesSchema.

        context

        :return: The context of this PropertiesSchema.
        :rtype: str
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this PropertiesSchema.

        context

        :param context: The context of this PropertiesSchema.
        :type context: str
        """
        self._context = context

    @property
    def docstring(self):
        """Gets the docstring of this PropertiesSchema.

        docstring

        :return: The docstring of this PropertiesSchema.
        :rtype: str
        """
        return self._docstring

    @docstring.setter
    def docstring(self, docstring):
        """Sets the docstring of this PropertiesSchema.

        docstring

        :param docstring: The docstring of this PropertiesSchema.
        :type docstring: str
        """
        self._docstring = docstring

    @property
    def ide_type(self):
        """Gets the ide_type of this PropertiesSchema.

        the type of ide

        :return: The ide_type of this PropertiesSchema.
        :rtype: str
        """
        return self._ide_type

    @ide_type.setter
    def ide_type(self, ide_type):
        """Sets the ide_type of this PropertiesSchema.

        the type of ide

        :param ide_type: The ide_type of this PropertiesSchema.
        :type ide_type: str
        """
        self._ide_type = ide_type

    @property
    def ide_version(self):
        """Gets the ide_version of this PropertiesSchema.

        the version of ide

        :return: The ide_version of this PropertiesSchema.
        :rtype: str
        """
        return self._ide_version

    @ide_version.setter
    def ide_version(self, ide_version):
        """Sets the ide_version of this PropertiesSchema.

        the version of ide

        :param ide_version: The ide_version of this PropertiesSchema.
        :type ide_version: str
        """
        self._ide_version = ide_version

    @property
    def language(self):
        """Gets the language of this PropertiesSchema.

        code language

        :return: The language of this PropertiesSchema.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this PropertiesSchema.

        code language

        :param language: The language of this PropertiesSchema.
        :type language: str
        """
        self._language = language

    @property
    def plugin_version(self):
        """Gets the plugin_version of this PropertiesSchema.

        the version of plugin

        :return: The plugin_version of this PropertiesSchema.
        :rtype: str
        """
        return self._plugin_version

    @plugin_version.setter
    def plugin_version(self, plugin_version):
        """Sets the plugin_version of this PropertiesSchema.

        the version of plugin

        :param plugin_version: The plugin_version of this PropertiesSchema.
        :type plugin_version: str
        """
        self._plugin_version = plugin_version

    @property
    def signature(self):
        """Gets the signature of this PropertiesSchema.

        signature

        :return: The signature of this PropertiesSchema.
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this PropertiesSchema.

        signature

        :param signature: The signature of this PropertiesSchema.
        :type signature: str
        """
        self._signature = signature

    @property
    def above_text(self):
        """Gets the above_text of this PropertiesSchema.

        the text above the cursor

        :return: The above_text of this PropertiesSchema.
        :rtype: str
        """
        return self._above_text

    @above_text.setter
    def above_text(self, above_text):
        """Sets the above_text of this PropertiesSchema.

        the text above the cursor

        :param above_text: The above_text of this PropertiesSchema.
        :type above_text: str
        """
        self._above_text = above_text

    @property
    def following_text(self):
        """Gets the following_text of this PropertiesSchema.

        the text following the cursor

        :return: The following_text of this PropertiesSchema.
        :rtype: str
        """
        return self._following_text

    @following_text.setter
    def following_text(self, following_text):
        """Sets the following_text of this PropertiesSchema.

        the text following the cursor

        :param following_text: The following_text of this PropertiesSchema.
        :type following_text: str
        """
        self._following_text = following_text

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
        if not isinstance(other, PropertiesSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
