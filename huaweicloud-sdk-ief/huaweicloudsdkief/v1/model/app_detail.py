# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppDetail:

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
        'alias': 'str',
        'description': 'str',
        'icon_url': 'str',
        'tags': 'list[NodeResTag]'
    }

    attribute_map = {
        'name': 'name',
        'alias': 'alias',
        'description': 'description',
        'icon_url': 'icon_url',
        'tags': 'tags'
    }

    def __init__(self, name=None, alias=None, description=None, icon_url=None, tags=None):
        """AppDetail

        The model defined in huaweicloud sdk

        :param name: 应用模板名称，只允许英文小写字母、数字、中划线，最大长度32， 英文小写字母或数字开头和结尾 Name为必填字段，且本租户中唯一
        :type name: str
        :param alias: 应用模板别名，中文英文字母、数字、中划线、下划线，最大64字符
        :type alias: str
        :param description: 应用模板描述，最大长度255，不允许^ ~ # $ % &amp; * &lt; &gt; ( ) [ ] { } &#39; \&quot; \\
        :type description: str
        :param icon_url: 应用图标存储url地址，最大长度2083
        :type icon_url: str
        :param tags: 应用模板标签
        :type tags: list[:class:`huaweicloudsdkief.v1.NodeResTag`]
        """
        
        

        self._name = None
        self._alias = None
        self._description = None
        self._icon_url = None
        self._tags = None
        self.discriminator = None

        self.name = name
        if alias is not None:
            self.alias = alias
        if description is not None:
            self.description = description
        if icon_url is not None:
            self.icon_url = icon_url
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        """Gets the name of this AppDetail.

        应用模板名称，只允许英文小写字母、数字、中划线，最大长度32， 英文小写字母或数字开头和结尾 Name为必填字段，且本租户中唯一

        :return: The name of this AppDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AppDetail.

        应用模板名称，只允许英文小写字母、数字、中划线，最大长度32， 英文小写字母或数字开头和结尾 Name为必填字段，且本租户中唯一

        :param name: The name of this AppDetail.
        :type name: str
        """
        self._name = name

    @property
    def alias(self):
        """Gets the alias of this AppDetail.

        应用模板别名，中文英文字母、数字、中划线、下划线，最大64字符

        :return: The alias of this AppDetail.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this AppDetail.

        应用模板别名，中文英文字母、数字、中划线、下划线，最大64字符

        :param alias: The alias of this AppDetail.
        :type alias: str
        """
        self._alias = alias

    @property
    def description(self):
        """Gets the description of this AppDetail.

        应用模板描述，最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :return: The description of this AppDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AppDetail.

        应用模板描述，最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :param description: The description of this AppDetail.
        :type description: str
        """
        self._description = description

    @property
    def icon_url(self):
        """Gets the icon_url of this AppDetail.

        应用图标存储url地址，最大长度2083

        :return: The icon_url of this AppDetail.
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        """Sets the icon_url of this AppDetail.

        应用图标存储url地址，最大长度2083

        :param icon_url: The icon_url of this AppDetail.
        :type icon_url: str
        """
        self._icon_url = icon_url

    @property
    def tags(self):
        """Gets the tags of this AppDetail.

        应用模板标签

        :return: The tags of this AppDetail.
        :rtype: list[:class:`huaweicloudsdkief.v1.NodeResTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this AppDetail.

        应用模板标签

        :param tags: The tags of this AppDetail.
        :type tags: list[:class:`huaweicloudsdkief.v1.NodeResTag`]
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
        if not isinstance(other, AppDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
