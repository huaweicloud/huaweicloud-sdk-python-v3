# coding: utf-8

import pprint
import re

import six





class TemplateQueryV2:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'category': 'list[str]',
        'keyword': 'str',
        'sort_by': 'str',
        'label': 'str',
        'my_templates': 'bool',
        'status': 'int',
        'status_array': 'list[int]',
        'productshorts': 'list[str]',
        'offset': 'int',
        'limit': 'int',
        'tag_ids': 'list[str]',
        'types': 'list[int]',
        'is_static': 'int',
        'platform_source': 'list[int]',
        'tag_names': 'list[str]'
    }

    attribute_map = {
        'category': 'category',
        'keyword': 'keyword',
        'sort_by': 'sort_by',
        'label': 'label',
        'my_templates': 'my_templates',
        'status': 'status',
        'status_array': 'status_array',
        'productshorts': 'productshorts',
        'offset': 'offset',
        'limit': 'limit',
        'tag_ids': 'tag_ids',
        'types': 'types',
        'is_static': 'is_static',
        'platform_source': 'platform_source',
        'tag_names': 'tag_names'
    }

    def __init__(self, category=None, keyword=None, sort_by=None, label='all', my_templates=False, status=None, status_array=None, productshorts=None, offset=None, limit=None, tag_ids=None, types=None, is_static=None, platform_source=None, tag_names=None):
        """TemplateQueryV2 - a model defined in huaweicloud sdk"""
        
        

        self._category = None
        self._keyword = None
        self._sort_by = None
        self._label = None
        self._my_templates = None
        self._status = None
        self._status_array = None
        self._productshorts = None
        self._offset = None
        self._limit = None
        self._tag_ids = None
        self._types = None
        self._is_static = None
        self._platform_source = None
        self._tag_names = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if keyword is not None:
            self.keyword = keyword
        if sort_by is not None:
            self.sort_by = sort_by
        if label is not None:
            self.label = label
        if my_templates is not None:
            self.my_templates = my_templates
        if status is not None:
            self.status = status
        if status_array is not None:
            self.status_array = status_array
        if productshorts is not None:
            self.productshorts = productshorts
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if tag_ids is not None:
            self.tag_ids = tag_ids
        if types is not None:
            self.types = types
        if is_static is not None:
            self.is_static = is_static
        if platform_source is not None:
            self.platform_source = platform_source
        if tag_names is not None:
            self.tag_names = tag_names

    @property
    def category(self):
        """Gets the category of this TemplateQueryV2.

        模板分类数组

        :return: The category of this TemplateQueryV2.
        :rtype: list[str]
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this TemplateQueryV2.

        模板分类数组

        :param category: The category of this TemplateQueryV2.
        :type: list[str]
        """
        self._category = category

    @property
    def keyword(self):
        """Gets the keyword of this TemplateQueryV2.

        搜索关键字,支持按名称和描述搜索，默认null

        :return: The keyword of this TemplateQueryV2.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        """Sets the keyword of this TemplateQueryV2.

        搜索关键字,支持按名称和描述搜索，默认null

        :param keyword: The keyword of this TemplateQueryV2.
        :type: str
        """
        self._keyword = keyword

    @property
    def sort_by(self):
        """Gets the sort_by of this TemplateQueryV2.

        排序字段和排序顺序指定. 比如: desc(created_at),desc(usage_count)

        :return: The sort_by of this TemplateQueryV2.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """Sets the sort_by of this TemplateQueryV2.

        排序字段和排序顺序指定. 比如: desc(created_at),desc(usage_count)

        :param sort_by: The sort_by of this TemplateQueryV2.
        :type: str
        """
        self._sort_by = sort_by

    @property
    def label(self):
        """Gets the label of this TemplateQueryV2.

        标签（all，new，hot，推荐recommend）

        :return: The label of this TemplateQueryV2.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this TemplateQueryV2.

        标签（all，new，hot，推荐recommend）

        :param label: The label of this TemplateQueryV2.
        :type: str
        """
        self._label = label

    @property
    def my_templates(self):
        """Gets the my_templates of this TemplateQueryV2.

        是否查询用户自己创建的模板，默认查所有模板

        :return: The my_templates of this TemplateQueryV2.
        :rtype: bool
        """
        return self._my_templates

    @my_templates.setter
    def my_templates(self, my_templates):
        """Sets the my_templates of this TemplateQueryV2.

        是否查询用户自己创建的模板，默认查所有模板

        :param my_templates: The my_templates of this TemplateQueryV2.
        :type: bool
        """
        self._my_templates = my_templates

    @property
    def status(self):
        """Gets the status of this TemplateQueryV2.

        查所有模板时只处理上架的；查用户模板，需支持按状态查询，状态：0审核中，1上架，2下架，不传表示查所有的（默认）

        :return: The status of this TemplateQueryV2.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TemplateQueryV2.

        查所有模板时只处理上架的；查用户模板，需支持按状态查询，状态：0审核中，1上架，2下架，不传表示查所有的（默认）

        :param status: The status of this TemplateQueryV2.
        :type: int
        """
        self._status = status

    @property
    def status_array(self):
        """Gets the status_array of this TemplateQueryV2.

        模板状态数组

        :return: The status_array of this TemplateQueryV2.
        :rtype: list[int]
        """
        return self._status_array

    @status_array.setter
    def status_array(self, status_array):
        """Sets the status_array of this TemplateQueryV2.

        模板状态数组

        :param status_array: The status_array of this TemplateQueryV2.
        :type: list[int]
        """
        self._status_array = status_array

    @property
    def productshorts(self):
        """Gets the productshorts of this TemplateQueryV2.

        模板关联的云产品(产品短名)列表

        :return: The productshorts of this TemplateQueryV2.
        :rtype: list[str]
        """
        return self._productshorts

    @productshorts.setter
    def productshorts(self, productshorts):
        """Sets the productshorts of this TemplateQueryV2.

        模板关联的云产品(产品短名)列表

        :param productshorts: The productshorts of this TemplateQueryV2.
        :type: list[str]
        """
        self._productshorts = productshorts

    @property
    def offset(self):
        """Gets the offset of this TemplateQueryV2.

        偏移量, 表示从此偏移量开始查询, offset大于等于0

        :return: The offset of this TemplateQueryV2.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this TemplateQueryV2.

        偏移量, 表示从此偏移量开始查询, offset大于等于0

        :param offset: The offset of this TemplateQueryV2.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this TemplateQueryV2.

        每页的模板条数

        :return: The limit of this TemplateQueryV2.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this TemplateQueryV2.

        每页的模板条数

        :param limit: The limit of this TemplateQueryV2.
        :type: int
        """
        self._limit = limit

    @property
    def tag_ids(self):
        """Gets the tag_ids of this TemplateQueryV2.

        模板关联的自定义标签列表

        :return: The tag_ids of this TemplateQueryV2.
        :rtype: list[str]
        """
        return self._tag_ids

    @tag_ids.setter
    def tag_ids(self, tag_ids):
        """Sets the tag_ids of this TemplateQueryV2.

        模板关联的自定义标签列表

        :param tag_ids: The tag_ids of this TemplateQueryV2.
        :type: list[str]
        """
        self._tag_ids = tag_ids

    @property
    def types(self):
        """Gets the types of this TemplateQueryV2.

        模板类型（0:doc、1:code、2:pipeline、3:devops四种）

        :return: The types of this TemplateQueryV2.
        :rtype: list[int]
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this TemplateQueryV2.

        模板类型（0:doc、1:code、2:pipeline、3:devops四种）

        :param types: The types of this TemplateQueryV2.
        :type: list[int]
        """
        self._types = types

    @property
    def is_static(self):
        """Gets the is_static of this TemplateQueryV2.

        动、静态代码模板标识（0：动态模板codetemplate，1：静态模板codesample）

        :return: The is_static of this TemplateQueryV2.
        :rtype: int
        """
        return self._is_static

    @is_static.setter
    def is_static(self, is_static):
        """Sets the is_static of this TemplateQueryV2.

        动、静态代码模板标识（0：动态模板codetemplate，1：静态模板codesample）

        :param is_static: The is_static of this TemplateQueryV2.
        :type: int
        """
        self._is_static = is_static

    @property
    def platform_source(self):
        """Gets the platform_source of this TemplateQueryV2.

        平台来源（0:codelabs、1:devstar）

        :return: The platform_source of this TemplateQueryV2.
        :rtype: list[int]
        """
        return self._platform_source

    @platform_source.setter
    def platform_source(self, platform_source):
        """Sets the platform_source of this TemplateQueryV2.

        平台来源（0:codelabs、1:devstar）

        :param platform_source: The platform_source of this TemplateQueryV2.
        :type: list[int]
        """
        self._platform_source = platform_source

    @property
    def tag_names(self):
        """Gets the tag_names of this TemplateQueryV2.

        模板关联的标签名称列表

        :return: The tag_names of this TemplateQueryV2.
        :rtype: list[str]
        """
        return self._tag_names

    @tag_names.setter
    def tag_names(self, tag_names):
        """Sets the tag_names of this TemplateQueryV2.

        模板关联的标签名称列表

        :param tag_names: The tag_names of this TemplateQueryV2.
        :type: list[str]
        """
        self._tag_names = tag_names

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TemplateQueryV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
