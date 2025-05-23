# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SqlSampleTemplate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'lang': 'str',
        'name': 'str',
        'sql': 'str',
        'description': 'str',
        'group': 'str'
    }

    attribute_map = {
        'lang': 'lang',
        'name': 'name',
        'sql': 'sql',
        'description': 'description',
        'group': 'group'
    }

    def __init__(self, lang=None, name=None, sql=None, description=None, group=None):
        r"""SqlSampleTemplate

        The model defined in huaweicloud sdk

        :param lang: 语言。
        :type lang: str
        :param name: 样例模板名称。
        :type name: str
        :param sql: 样例模板内容。
        :type sql: str
        :param description: 样例模板描述。
        :type description: str
        :param group: 样例模板分组。
        :type group: str
        """
        
        

        self._lang = None
        self._name = None
        self._sql = None
        self._description = None
        self._group = None
        self.discriminator = None

        if lang is not None:
            self.lang = lang
        if name is not None:
            self.name = name
        if sql is not None:
            self.sql = sql
        if description is not None:
            self.description = description
        if group is not None:
            self.group = group

    @property
    def lang(self):
        r"""Gets the lang of this SqlSampleTemplate.

        语言。

        :return: The lang of this SqlSampleTemplate.
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, lang):
        r"""Sets the lang of this SqlSampleTemplate.

        语言。

        :param lang: The lang of this SqlSampleTemplate.
        :type lang: str
        """
        self._lang = lang

    @property
    def name(self):
        r"""Gets the name of this SqlSampleTemplate.

        样例模板名称。

        :return: The name of this SqlSampleTemplate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SqlSampleTemplate.

        样例模板名称。

        :param name: The name of this SqlSampleTemplate.
        :type name: str
        """
        self._name = name

    @property
    def sql(self):
        r"""Gets the sql of this SqlSampleTemplate.

        样例模板内容。

        :return: The sql of this SqlSampleTemplate.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        r"""Sets the sql of this SqlSampleTemplate.

        样例模板内容。

        :param sql: The sql of this SqlSampleTemplate.
        :type sql: str
        """
        self._sql = sql

    @property
    def description(self):
        r"""Gets the description of this SqlSampleTemplate.

        样例模板描述。

        :return: The description of this SqlSampleTemplate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this SqlSampleTemplate.

        样例模板描述。

        :param description: The description of this SqlSampleTemplate.
        :type description: str
        """
        self._description = description

    @property
    def group(self):
        r"""Gets the group of this SqlSampleTemplate.

        样例模板分组。

        :return: The group of this SqlSampleTemplate.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        r"""Sets the group of this SqlSampleTemplate.

        样例模板分组。

        :param group: The group of this SqlSampleTemplate.
        :type group: str
        """
        self._group = group

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
        if not isinstance(other, SqlSampleTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
