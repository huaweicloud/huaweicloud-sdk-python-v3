# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateRepository:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'name': 'str',
        'template_name': 'str',
        'tags': 'list[str]',
        'description': 'str',
        'brief_introduction': 'str',
        'auto_pending_pipelines': 'int',
        'language': 'str',
        'created_at': 'str',
        'used_times': 'int',
        'liked_times': 'int',
        'creator_name': 'str',
        'https_url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'template_name': 'template_name',
        'tags': 'tags',
        'description': 'description',
        'brief_introduction': 'brief_introduction',
        'auto_pending_pipelines': 'auto_pending_pipelines',
        'language': 'language',
        'created_at': 'created_at',
        'used_times': 'used_times',
        'liked_times': 'liked_times',
        'creator_name': 'creator_name',
        'https_url': 'https_url'
    }

    def __init__(self, id=None, name=None, template_name=None, tags=None, description=None, brief_introduction=None, auto_pending_pipelines=None, language=None, created_at=None, used_times=None, liked_times=None, creator_name=None, https_url=None):
        """TemplateRepository

        The model defined in huaweicloud sdk

        :param id: 模板唯一标识
        :type id: int
        :param name: 模板名称
        :type name: str
        :param template_name: 模板关联仓库名称
        :type template_name: str
        :param tags: 模板标签
        :type tags: list[str]
        :param description: 模板描述
        :type description: str
        :param brief_introduction: 模板简介
        :type brief_introduction: str
        :param auto_pending_pipelines: 是否自动创建流水线
        :type auto_pending_pipelines: int
        :param language: 模板语言分类
        :type language: str
        :param created_at: 模板创建时间
        :type created_at: str
        :param used_times: 模板引用次数
        :type used_times: int
        :param liked_times: 模板被点赞次数
        :type liked_times: int
        :param creator_name: 模板创建人
        :type creator_name: str
        :param https_url: 模板https链接
        :type https_url: str
        """
        
        

        self._id = None
        self._name = None
        self._template_name = None
        self._tags = None
        self._description = None
        self._brief_introduction = None
        self._auto_pending_pipelines = None
        self._language = None
        self._created_at = None
        self._used_times = None
        self._liked_times = None
        self._creator_name = None
        self._https_url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if template_name is not None:
            self.template_name = template_name
        if tags is not None:
            self.tags = tags
        if description is not None:
            self.description = description
        if brief_introduction is not None:
            self.brief_introduction = brief_introduction
        if auto_pending_pipelines is not None:
            self.auto_pending_pipelines = auto_pending_pipelines
        if language is not None:
            self.language = language
        if created_at is not None:
            self.created_at = created_at
        if used_times is not None:
            self.used_times = used_times
        if liked_times is not None:
            self.liked_times = liked_times
        if creator_name is not None:
            self.creator_name = creator_name
        if https_url is not None:
            self.https_url = https_url

    @property
    def id(self):
        """Gets the id of this TemplateRepository.

        模板唯一标识

        :return: The id of this TemplateRepository.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TemplateRepository.

        模板唯一标识

        :param id: The id of this TemplateRepository.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this TemplateRepository.

        模板名称

        :return: The name of this TemplateRepository.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TemplateRepository.

        模板名称

        :param name: The name of this TemplateRepository.
        :type name: str
        """
        self._name = name

    @property
    def template_name(self):
        """Gets the template_name of this TemplateRepository.

        模板关联仓库名称

        :return: The template_name of this TemplateRepository.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this TemplateRepository.

        模板关联仓库名称

        :param template_name: The template_name of this TemplateRepository.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def tags(self):
        """Gets the tags of this TemplateRepository.

        模板标签

        :return: The tags of this TemplateRepository.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TemplateRepository.

        模板标签

        :param tags: The tags of this TemplateRepository.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def description(self):
        """Gets the description of this TemplateRepository.

        模板描述

        :return: The description of this TemplateRepository.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TemplateRepository.

        模板描述

        :param description: The description of this TemplateRepository.
        :type description: str
        """
        self._description = description

    @property
    def brief_introduction(self):
        """Gets the brief_introduction of this TemplateRepository.

        模板简介

        :return: The brief_introduction of this TemplateRepository.
        :rtype: str
        """
        return self._brief_introduction

    @brief_introduction.setter
    def brief_introduction(self, brief_introduction):
        """Sets the brief_introduction of this TemplateRepository.

        模板简介

        :param brief_introduction: The brief_introduction of this TemplateRepository.
        :type brief_introduction: str
        """
        self._brief_introduction = brief_introduction

    @property
    def auto_pending_pipelines(self):
        """Gets the auto_pending_pipelines of this TemplateRepository.

        是否自动创建流水线

        :return: The auto_pending_pipelines of this TemplateRepository.
        :rtype: int
        """
        return self._auto_pending_pipelines

    @auto_pending_pipelines.setter
    def auto_pending_pipelines(self, auto_pending_pipelines):
        """Sets the auto_pending_pipelines of this TemplateRepository.

        是否自动创建流水线

        :param auto_pending_pipelines: The auto_pending_pipelines of this TemplateRepository.
        :type auto_pending_pipelines: int
        """
        self._auto_pending_pipelines = auto_pending_pipelines

    @property
    def language(self):
        """Gets the language of this TemplateRepository.

        模板语言分类

        :return: The language of this TemplateRepository.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this TemplateRepository.

        模板语言分类

        :param language: The language of this TemplateRepository.
        :type language: str
        """
        self._language = language

    @property
    def created_at(self):
        """Gets the created_at of this TemplateRepository.

        模板创建时间

        :return: The created_at of this TemplateRepository.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TemplateRepository.

        模板创建时间

        :param created_at: The created_at of this TemplateRepository.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def used_times(self):
        """Gets the used_times of this TemplateRepository.

        模板引用次数

        :return: The used_times of this TemplateRepository.
        :rtype: int
        """
        return self._used_times

    @used_times.setter
    def used_times(self, used_times):
        """Sets the used_times of this TemplateRepository.

        模板引用次数

        :param used_times: The used_times of this TemplateRepository.
        :type used_times: int
        """
        self._used_times = used_times

    @property
    def liked_times(self):
        """Gets the liked_times of this TemplateRepository.

        模板被点赞次数

        :return: The liked_times of this TemplateRepository.
        :rtype: int
        """
        return self._liked_times

    @liked_times.setter
    def liked_times(self, liked_times):
        """Sets the liked_times of this TemplateRepository.

        模板被点赞次数

        :param liked_times: The liked_times of this TemplateRepository.
        :type liked_times: int
        """
        self._liked_times = liked_times

    @property
    def creator_name(self):
        """Gets the creator_name of this TemplateRepository.

        模板创建人

        :return: The creator_name of this TemplateRepository.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        """Sets the creator_name of this TemplateRepository.

        模板创建人

        :param creator_name: The creator_name of this TemplateRepository.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def https_url(self):
        """Gets the https_url of this TemplateRepository.

        模板https链接

        :return: The https_url of this TemplateRepository.
        :rtype: str
        """
        return self._https_url

    @https_url.setter
    def https_url(self, https_url):
        """Sets the https_url of this TemplateRepository.

        模板https链接

        :param https_url: The https_url of this TemplateRepository.
        :type https_url: str
        """
        self._https_url = https_url

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
        if not isinstance(other, TemplateRepository):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
