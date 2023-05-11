# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTemplateRulesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'ruleset_id': 'str',
        'types': 'str',
        'languages': 'str',
        'tags': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'ruleset_id': 'ruleset_id',
        'types': 'types',
        'languages': 'languages',
        'tags': 'tags',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, project_id=None, ruleset_id=None, types=None, languages=None, tags=None, offset=None, limit=None):
        """ListTemplateRulesRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目ID
        :type project_id: str
        :param ruleset_id: 规则集ID
        :type ruleset_id: str
        :param types: 规则状态  &#39;1查询全部，2已启动，3未启用&#39;
        :type types: str
        :param languages: 规则语言
        :type languages: str
        :param tags: 规则所属标签
        :type tags: str
        :param offset: 分页索引，偏移量
        :type offset: int
        :param limit: 每页显示的数量
        :type limit: int
        """
        
        

        self._project_id = None
        self._ruleset_id = None
        self._types = None
        self._languages = None
        self._tags = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.project_id = project_id
        self.ruleset_id = ruleset_id
        self.types = types
        if languages is not None:
            self.languages = languages
        if tags is not None:
            self.tags = tags
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def project_id(self):
        """Gets the project_id of this ListTemplateRulesRequest.

        项目ID

        :return: The project_id of this ListTemplateRulesRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListTemplateRulesRequest.

        项目ID

        :param project_id: The project_id of this ListTemplateRulesRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def ruleset_id(self):
        """Gets the ruleset_id of this ListTemplateRulesRequest.

        规则集ID

        :return: The ruleset_id of this ListTemplateRulesRequest.
        :rtype: str
        """
        return self._ruleset_id

    @ruleset_id.setter
    def ruleset_id(self, ruleset_id):
        """Sets the ruleset_id of this ListTemplateRulesRequest.

        规则集ID

        :param ruleset_id: The ruleset_id of this ListTemplateRulesRequest.
        :type ruleset_id: str
        """
        self._ruleset_id = ruleset_id

    @property
    def types(self):
        """Gets the types of this ListTemplateRulesRequest.

        规则状态  '1查询全部，2已启动，3未启用'

        :return: The types of this ListTemplateRulesRequest.
        :rtype: str
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this ListTemplateRulesRequest.

        规则状态  '1查询全部，2已启动，3未启用'

        :param types: The types of this ListTemplateRulesRequest.
        :type types: str
        """
        self._types = types

    @property
    def languages(self):
        """Gets the languages of this ListTemplateRulesRequest.

        规则语言

        :return: The languages of this ListTemplateRulesRequest.
        :rtype: str
        """
        return self._languages

    @languages.setter
    def languages(self, languages):
        """Sets the languages of this ListTemplateRulesRequest.

        规则语言

        :param languages: The languages of this ListTemplateRulesRequest.
        :type languages: str
        """
        self._languages = languages

    @property
    def tags(self):
        """Gets the tags of this ListTemplateRulesRequest.

        规则所属标签

        :return: The tags of this ListTemplateRulesRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListTemplateRulesRequest.

        规则所属标签

        :param tags: The tags of this ListTemplateRulesRequest.
        :type tags: str
        """
        self._tags = tags

    @property
    def offset(self):
        """Gets the offset of this ListTemplateRulesRequest.

        分页索引，偏移量

        :return: The offset of this ListTemplateRulesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListTemplateRulesRequest.

        分页索引，偏移量

        :param offset: The offset of this ListTemplateRulesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListTemplateRulesRequest.

        每页显示的数量

        :return: The limit of this ListTemplateRulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListTemplateRulesRequest.

        每页显示的数量

        :param limit: The limit of this ListTemplateRulesRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListTemplateRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
