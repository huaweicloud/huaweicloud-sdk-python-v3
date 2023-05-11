# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePolicyReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content': 'str',
        'description': 'str',
        'name': 'str',
        'type': 'str',
        'tags': 'list[TagDto]'
    }

    attribute_map = {
        'content': 'content',
        'description': 'description',
        'name': 'name',
        'type': 'type',
        'tags': 'tags'
    }

    def __init__(self, content=None, description=None, name=None, type=None, tags=None):
        """CreatePolicyReqBody

        The model defined in huaweicloud sdk

        :param content: 要添加到新策略的策略文本内容。
        :type content: str
        :param description: 要分配给策略的可选说明。
        :type description: str
        :param name: 要分配给策略的名称。
        :type name: str
        :param type: 要创建的策略类型,service_control_policy服务控制策略；tag_policy：标签策略。
        :type type: str
        :param tags: 要附加到新创建的策略的标签列表。
        :type tags: list[:class:`huaweicloudsdkorganizations.v1.TagDto`]
        """
        
        

        self._content = None
        self._description = None
        self._name = None
        self._type = None
        self._tags = None
        self.discriminator = None

        self.content = content
        self.description = description
        self.name = name
        self.type = type
        if tags is not None:
            self.tags = tags

    @property
    def content(self):
        """Gets the content of this CreatePolicyReqBody.

        要添加到新策略的策略文本内容。

        :return: The content of this CreatePolicyReqBody.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this CreatePolicyReqBody.

        要添加到新策略的策略文本内容。

        :param content: The content of this CreatePolicyReqBody.
        :type content: str
        """
        self._content = content

    @property
    def description(self):
        """Gets the description of this CreatePolicyReqBody.

        要分配给策略的可选说明。

        :return: The description of this CreatePolicyReqBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreatePolicyReqBody.

        要分配给策略的可选说明。

        :param description: The description of this CreatePolicyReqBody.
        :type description: str
        """
        self._description = description

    @property
    def name(self):
        """Gets the name of this CreatePolicyReqBody.

        要分配给策略的名称。

        :return: The name of this CreatePolicyReqBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreatePolicyReqBody.

        要分配给策略的名称。

        :param name: The name of this CreatePolicyReqBody.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this CreatePolicyReqBody.

        要创建的策略类型,service_control_policy服务控制策略；tag_policy：标签策略。

        :return: The type of this CreatePolicyReqBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreatePolicyReqBody.

        要创建的策略类型,service_control_policy服务控制策略；tag_policy：标签策略。

        :param type: The type of this CreatePolicyReqBody.
        :type type: str
        """
        self._type = type

    @property
    def tags(self):
        """Gets the tags of this CreatePolicyReqBody.

        要附加到新创建的策略的标签列表。

        :return: The tags of this CreatePolicyReqBody.
        :rtype: list[:class:`huaweicloudsdkorganizations.v1.TagDto`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreatePolicyReqBody.

        要附加到新创建的策略的标签列表。

        :param tags: The tags of this CreatePolicyReqBody.
        :type tags: list[:class:`huaweicloudsdkorganizations.v1.TagDto`]
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
        if not isinstance(other, CreatePolicyReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
