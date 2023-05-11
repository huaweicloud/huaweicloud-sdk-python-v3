# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecretObjectInSecretRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'secrets': 'list[Secret]',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'secrets': 'secrets',
        'tags': 'tags'
    }

    def __init__(self, name=None, description=None, secrets=None, tags=None):
        """SecretObjectInSecretRequestBody

        The model defined in huaweicloud sdk

        :param name: 密钥名称，以小写英文字母开头，4-64位，可以使用小写英文、数字、中划线（-），不能以中划线结尾。
        :type name: str
        :param description: 密钥描述,最大长度255，不允许^ ~ # $ % &amp; * &lt; &gt; ( ) [ ] { } &#39; \&quot; \\。
        :type description: str
        :param secrets: secrets是一个列表，由多个字典组成，数量上限为100个。字典的key和value均为字符串。key由大小写字母，中划线（&#x60;-&#x60;）开头，由数字、大小写字母、点号（&#x60;.&#x60;）、中划线（&#x60;-&#x60;）、下划线（&#x60;_&#x60;）组成，最小长度为1，最大长度63个字符, value不能含有字符不允许^ ~ # $ \\|% &amp; &lt; &gt; ( ) [ ] { } &#39; \&quot; \\，最大长度10000个字符。
        :type secrets: list[:class:`huaweicloudsdkhilens.v3.Secret`]
        :param tags: tags是一个列表，由多个字典组成，数量上限为20个。字典的key和value均为字符串。key由数字、大小写字母、点号（&#x60;.&#x60;）、中划线（&#x60;-&#x60;）、下划线（&#x60;_&#x60;）组成，最小长度为1，最大长度36个字符, value由数字、大小写字母、点号（&#x60;.&#x60;）、中划线（&#x60;-&#x60;）、下划线（&#x60;_&#x60;）, 斜线（&#x60;\\&#x60;）组成，最小长度为0，最大长度43个字符。
        :type tags: list[:class:`huaweicloudsdkhilens.v3.Tag`]
        """
        
        

        self._name = None
        self._description = None
        self._secrets = None
        self._tags = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.secrets = secrets
        self.tags = tags

    @property
    def name(self):
        """Gets the name of this SecretObjectInSecretRequestBody.

        密钥名称，以小写英文字母开头，4-64位，可以使用小写英文、数字、中划线（-），不能以中划线结尾。

        :return: The name of this SecretObjectInSecretRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SecretObjectInSecretRequestBody.

        密钥名称，以小写英文字母开头，4-64位，可以使用小写英文、数字、中划线（-），不能以中划线结尾。

        :param name: The name of this SecretObjectInSecretRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this SecretObjectInSecretRequestBody.

        密钥描述,最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\。

        :return: The description of this SecretObjectInSecretRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SecretObjectInSecretRequestBody.

        密钥描述,最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\。

        :param description: The description of this SecretObjectInSecretRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def secrets(self):
        """Gets the secrets of this SecretObjectInSecretRequestBody.

        secrets是一个列表，由多个字典组成，数量上限为100个。字典的key和value均为字符串。key由大小写字母，中划线（`-`）开头，由数字、大小写字母、点号（`.`）、中划线（`-`）、下划线（`_`）组成，最小长度为1，最大长度63个字符, value不能含有字符不允许^ ~ # $ \\|% & < > ( ) [ ] { } ' \" \\，最大长度10000个字符。

        :return: The secrets of this SecretObjectInSecretRequestBody.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.Secret`]
        """
        return self._secrets

    @secrets.setter
    def secrets(self, secrets):
        """Sets the secrets of this SecretObjectInSecretRequestBody.

        secrets是一个列表，由多个字典组成，数量上限为100个。字典的key和value均为字符串。key由大小写字母，中划线（`-`）开头，由数字、大小写字母、点号（`.`）、中划线（`-`）、下划线（`_`）组成，最小长度为1，最大长度63个字符, value不能含有字符不允许^ ~ # $ \\|% & < > ( ) [ ] { } ' \" \\，最大长度10000个字符。

        :param secrets: The secrets of this SecretObjectInSecretRequestBody.
        :type secrets: list[:class:`huaweicloudsdkhilens.v3.Secret`]
        """
        self._secrets = secrets

    @property
    def tags(self):
        """Gets the tags of this SecretObjectInSecretRequestBody.

        tags是一个列表，由多个字典组成，数量上限为20个。字典的key和value均为字符串。key由数字、大小写字母、点号（`.`）、中划线（`-`）、下划线（`_`）组成，最小长度为1，最大长度36个字符, value由数字、大小写字母、点号（`.`）、中划线（`-`）、下划线（`_`）, 斜线（`\\`）组成，最小长度为0，最大长度43个字符。

        :return: The tags of this SecretObjectInSecretRequestBody.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this SecretObjectInSecretRequestBody.

        tags是一个列表，由多个字典组成，数量上限为20个。字典的key和value均为字符串。key由数字、大小写字母、点号（`.`）、中划线（`-`）、下划线（`_`）组成，最小长度为1，最大长度36个字符, value由数字、大小写字母、点号（`.`）、中划线（`-`）、下划线（`_`）, 斜线（`\\`）组成，最小长度为0，最大长度43个字符。

        :param tags: The tags of this SecretObjectInSecretRequestBody.
        :type tags: list[:class:`huaweicloudsdkhilens.v3.Tag`]
        """
        self._tags = tags

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
        if not isinstance(other, SecretObjectInSecretRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
