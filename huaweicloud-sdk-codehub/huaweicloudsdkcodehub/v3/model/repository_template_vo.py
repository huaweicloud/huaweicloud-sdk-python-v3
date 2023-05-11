# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepositoryTemplateVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_type': 'str',
        'code_title': 'str',
        'creator_name': 'str',
        'code_description': 'str',
        'languages': 'list[str]',
        'plateform': 'list[str]',
        'entertype': 'list[str]'
    }

    attribute_map = {
        'template_type': 'templateType',
        'code_title': 'codeTitle',
        'creator_name': 'creatorName',
        'code_description': 'codeDescription',
        'languages': 'languages',
        'plateform': 'plateform',
        'entertype': 'entertype'
    }

    def __init__(self, template_type=None, code_title=None, creator_name=None, code_description=None, languages=None, plateform=None, entertype=None):
        """RepositoryTemplateVO

        The model defined in huaweicloud sdk

        :param template_type: 模板类型
        :type template_type: str
        :param code_title: 代码模板名称
        :type code_title: str
        :param creator_name: 创建者名称
        :type creator_name: str
        :param code_description: 代码模板描述
        :type code_description: str
        :param languages: 模板语言
        :type languages: list[str]
        :param plateform: 模板平台
        :type plateform: list[str]
        :param entertype: 模板类型
        :type entertype: list[str]
        """
        
        

        self._template_type = None
        self._code_title = None
        self._creator_name = None
        self._code_description = None
        self._languages = None
        self._plateform = None
        self._entertype = None
        self.discriminator = None

        self.template_type = template_type
        if code_title is not None:
            self.code_title = code_title
        if creator_name is not None:
            self.creator_name = creator_name
        if code_description is not None:
            self.code_description = code_description
        if languages is not None:
            self.languages = languages
        if plateform is not None:
            self.plateform = plateform
        if entertype is not None:
            self.entertype = entertype

    @property
    def template_type(self):
        """Gets the template_type of this RepositoryTemplateVO.

        模板类型

        :return: The template_type of this RepositoryTemplateVO.
        :rtype: str
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        """Sets the template_type of this RepositoryTemplateVO.

        模板类型

        :param template_type: The template_type of this RepositoryTemplateVO.
        :type template_type: str
        """
        self._template_type = template_type

    @property
    def code_title(self):
        """Gets the code_title of this RepositoryTemplateVO.

        代码模板名称

        :return: The code_title of this RepositoryTemplateVO.
        :rtype: str
        """
        return self._code_title

    @code_title.setter
    def code_title(self, code_title):
        """Sets the code_title of this RepositoryTemplateVO.

        代码模板名称

        :param code_title: The code_title of this RepositoryTemplateVO.
        :type code_title: str
        """
        self._code_title = code_title

    @property
    def creator_name(self):
        """Gets the creator_name of this RepositoryTemplateVO.

        创建者名称

        :return: The creator_name of this RepositoryTemplateVO.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        """Sets the creator_name of this RepositoryTemplateVO.

        创建者名称

        :param creator_name: The creator_name of this RepositoryTemplateVO.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def code_description(self):
        """Gets the code_description of this RepositoryTemplateVO.

        代码模板描述

        :return: The code_description of this RepositoryTemplateVO.
        :rtype: str
        """
        return self._code_description

    @code_description.setter
    def code_description(self, code_description):
        """Sets the code_description of this RepositoryTemplateVO.

        代码模板描述

        :param code_description: The code_description of this RepositoryTemplateVO.
        :type code_description: str
        """
        self._code_description = code_description

    @property
    def languages(self):
        """Gets the languages of this RepositoryTemplateVO.

        模板语言

        :return: The languages of this RepositoryTemplateVO.
        :rtype: list[str]
        """
        return self._languages

    @languages.setter
    def languages(self, languages):
        """Sets the languages of this RepositoryTemplateVO.

        模板语言

        :param languages: The languages of this RepositoryTemplateVO.
        :type languages: list[str]
        """
        self._languages = languages

    @property
    def plateform(self):
        """Gets the plateform of this RepositoryTemplateVO.

        模板平台

        :return: The plateform of this RepositoryTemplateVO.
        :rtype: list[str]
        """
        return self._plateform

    @plateform.setter
    def plateform(self, plateform):
        """Sets the plateform of this RepositoryTemplateVO.

        模板平台

        :param plateform: The plateform of this RepositoryTemplateVO.
        :type plateform: list[str]
        """
        self._plateform = plateform

    @property
    def entertype(self):
        """Gets the entertype of this RepositoryTemplateVO.

        模板类型

        :return: The entertype of this RepositoryTemplateVO.
        :rtype: list[str]
        """
        return self._entertype

    @entertype.setter
    def entertype(self, entertype):
        """Sets the entertype of this RepositoryTemplateVO.

        模板类型

        :param entertype: The entertype of this RepositoryTemplateVO.
        :type entertype: list[str]
        """
        self._entertype = entertype

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
        if not isinstance(other, RepositoryTemplateVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
