# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateJobTemplatesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'name': 'str',
        'body': 'str',
        'group': 'str',
        'description': 'str',
        'language': 'str'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'body': 'body',
        'group': 'group',
        'description': 'description',
        'language': 'language'
    }

    def __init__(self, type=None, name=None, body=None, group=None, description=None, language=None):
        """CreateJobTemplatesRequestBody

        The model defined in huaweicloud sdk

        :param type: 类型。SQL：sql模板。SPARK：spark模板。
        :type type: str
        :param name: 名字
        :type name: str
        :param body: 模板内容
        :type body: str
        :param group: 分组
        :type group: str
        :param description: 描述信息
        :type description: str
        :param language: 语言
        :type language: str
        """
        
        

        self._type = None
        self._name = None
        self._body = None
        self._group = None
        self._description = None
        self._language = None
        self.discriminator = None

        self.type = type
        self.name = name
        self.body = body
        if group is not None:
            self.group = group
        if description is not None:
            self.description = description
        if language is not None:
            self.language = language

    @property
    def type(self):
        """Gets the type of this CreateJobTemplatesRequestBody.

        类型。SQL：sql模板。SPARK：spark模板。

        :return: The type of this CreateJobTemplatesRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateJobTemplatesRequestBody.

        类型。SQL：sql模板。SPARK：spark模板。

        :param type: The type of this CreateJobTemplatesRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        """Gets the name of this CreateJobTemplatesRequestBody.

        名字

        :return: The name of this CreateJobTemplatesRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateJobTemplatesRequestBody.

        名字

        :param name: The name of this CreateJobTemplatesRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def body(self):
        """Gets the body of this CreateJobTemplatesRequestBody.

        模板内容

        :return: The body of this CreateJobTemplatesRequestBody.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateJobTemplatesRequestBody.

        模板内容

        :param body: The body of this CreateJobTemplatesRequestBody.
        :type body: str
        """
        self._body = body

    @property
    def group(self):
        """Gets the group of this CreateJobTemplatesRequestBody.

        分组

        :return: The group of this CreateJobTemplatesRequestBody.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this CreateJobTemplatesRequestBody.

        分组

        :param group: The group of this CreateJobTemplatesRequestBody.
        :type group: str
        """
        self._group = group

    @property
    def description(self):
        """Gets the description of this CreateJobTemplatesRequestBody.

        描述信息

        :return: The description of this CreateJobTemplatesRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateJobTemplatesRequestBody.

        描述信息

        :param description: The description of this CreateJobTemplatesRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def language(self):
        """Gets the language of this CreateJobTemplatesRequestBody.

        语言

        :return: The language of this CreateJobTemplatesRequestBody.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this CreateJobTemplatesRequestBody.

        语言

        :param language: The language of this CreateJobTemplatesRequestBody.
        :type language: str
        """
        self._language = language

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
        if not isinstance(other, CreateJobTemplatesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
