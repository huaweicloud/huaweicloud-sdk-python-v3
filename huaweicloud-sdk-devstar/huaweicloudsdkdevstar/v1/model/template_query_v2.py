# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'has_notices': 'bool',
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
        'has_notices': 'has_notices',
        'productshorts': 'productshorts',
        'offset': 'offset',
        'limit': 'limit',
        'tag_ids': 'tag_ids',
        'types': 'types',
        'is_static': 'is_static',
        'platform_source': 'platform_source',
        'tag_names': 'tag_names'
    }

    def __init__(self, category=None, keyword=None, sort_by=None, label=None, my_templates=None, status=None, status_array=None, has_notices=None, productshorts=None, offset=None, limit=None, tag_ids=None, types=None, is_static=None, platform_source=None, tag_names=None):
        r"""TemplateQueryV2

        The model defined in huaweicloud sdk

        :param category: 模板分类数组。
        :type category: list[str]
        :param keyword: 搜索关键字，支持按名称和描述搜索，默认null。
        :type keyword: str
        :param sort_by: 排序字段和排序顺序指定。比如： - desc(created_at)：根据创建时间降序 - desc(usage_count)：根据引用次数降序 
        :type sort_by: str
        :param label: 标签： - all：全部 - new：最新 - hot：热门 - recommend：推荐 
        :type label: str
        :param my_templates: 是否查询用户自己创建的模板，默认查所有模板。
        :type my_templates: bool
        :param status: 查所有模板时只处理上架的；查用户模板，需支持按状态查询，状态： - 0：审核中 - 1：上架 - 2：下架 不传表示查所有的（默认） 
        :type status: int
        :param status_array: 模板状态数组。
        :type status_array: list[int]
        :param has_notices: 是否查询有消息的模板，默认查所有模板。
        :type has_notices: bool
        :param productshorts: 模板关联的云产品(产品短名)列表。
        :type productshorts: list[str]
        :param offset: 偏移量，表示从此偏移量开始查询，offset大于等于0。
        :type offset: int
        :param limit: 每页的模板条数。
        :type limit: int
        :param tag_ids: 模板关联的自定义标签列表。
        :type tag_ids: list[str]
        :param types: 模板类型： - 0：doc - 1：code - 2：pipeline - 3：devops 
        :type types: list[int]
        :param is_static: 动、静态代码模板标识： - 0：动态模板codetemplate - 1：静态模板codesample 
        :type is_static: int
        :param platform_source: 平台来源： - 0：codelabs - 1：devstar 
        :type platform_source: list[int]
        :param tag_names: 模板关联的标签名称列表。
        :type tag_names: list[str]
        """
        
        

        self._category = None
        self._keyword = None
        self._sort_by = None
        self._label = None
        self._my_templates = None
        self._status = None
        self._status_array = None
        self._has_notices = None
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
        if has_notices is not None:
            self.has_notices = has_notices
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
        r"""Gets the category of this TemplateQueryV2.

        模板分类数组。

        :return: The category of this TemplateQueryV2.
        :rtype: list[str]
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this TemplateQueryV2.

        模板分类数组。

        :param category: The category of this TemplateQueryV2.
        :type category: list[str]
        """
        self._category = category

    @property
    def keyword(self):
        r"""Gets the keyword of this TemplateQueryV2.

        搜索关键字，支持按名称和描述搜索，默认null。

        :return: The keyword of this TemplateQueryV2.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        r"""Sets the keyword of this TemplateQueryV2.

        搜索关键字，支持按名称和描述搜索，默认null。

        :param keyword: The keyword of this TemplateQueryV2.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def sort_by(self):
        r"""Gets the sort_by of this TemplateQueryV2.

        排序字段和排序顺序指定。比如： - desc(created_at)：根据创建时间降序 - desc(usage_count)：根据引用次数降序 

        :return: The sort_by of this TemplateQueryV2.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        r"""Sets the sort_by of this TemplateQueryV2.

        排序字段和排序顺序指定。比如： - desc(created_at)：根据创建时间降序 - desc(usage_count)：根据引用次数降序 

        :param sort_by: The sort_by of this TemplateQueryV2.
        :type sort_by: str
        """
        self._sort_by = sort_by

    @property
    def label(self):
        r"""Gets the label of this TemplateQueryV2.

        标签： - all：全部 - new：最新 - hot：热门 - recommend：推荐 

        :return: The label of this TemplateQueryV2.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        r"""Sets the label of this TemplateQueryV2.

        标签： - all：全部 - new：最新 - hot：热门 - recommend：推荐 

        :param label: The label of this TemplateQueryV2.
        :type label: str
        """
        self._label = label

    @property
    def my_templates(self):
        r"""Gets the my_templates of this TemplateQueryV2.

        是否查询用户自己创建的模板，默认查所有模板。

        :return: The my_templates of this TemplateQueryV2.
        :rtype: bool
        """
        return self._my_templates

    @my_templates.setter
    def my_templates(self, my_templates):
        r"""Sets the my_templates of this TemplateQueryV2.

        是否查询用户自己创建的模板，默认查所有模板。

        :param my_templates: The my_templates of this TemplateQueryV2.
        :type my_templates: bool
        """
        self._my_templates = my_templates

    @property
    def status(self):
        r"""Gets the status of this TemplateQueryV2.

        查所有模板时只处理上架的；查用户模板，需支持按状态查询，状态： - 0：审核中 - 1：上架 - 2：下架 不传表示查所有的（默认） 

        :return: The status of this TemplateQueryV2.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this TemplateQueryV2.

        查所有模板时只处理上架的；查用户模板，需支持按状态查询，状态： - 0：审核中 - 1：上架 - 2：下架 不传表示查所有的（默认） 

        :param status: The status of this TemplateQueryV2.
        :type status: int
        """
        self._status = status

    @property
    def status_array(self):
        r"""Gets the status_array of this TemplateQueryV2.

        模板状态数组。

        :return: The status_array of this TemplateQueryV2.
        :rtype: list[int]
        """
        return self._status_array

    @status_array.setter
    def status_array(self, status_array):
        r"""Sets the status_array of this TemplateQueryV2.

        模板状态数组。

        :param status_array: The status_array of this TemplateQueryV2.
        :type status_array: list[int]
        """
        self._status_array = status_array

    @property
    def has_notices(self):
        r"""Gets the has_notices of this TemplateQueryV2.

        是否查询有消息的模板，默认查所有模板。

        :return: The has_notices of this TemplateQueryV2.
        :rtype: bool
        """
        return self._has_notices

    @has_notices.setter
    def has_notices(self, has_notices):
        r"""Sets the has_notices of this TemplateQueryV2.

        是否查询有消息的模板，默认查所有模板。

        :param has_notices: The has_notices of this TemplateQueryV2.
        :type has_notices: bool
        """
        self._has_notices = has_notices

    @property
    def productshorts(self):
        r"""Gets the productshorts of this TemplateQueryV2.

        模板关联的云产品(产品短名)列表。

        :return: The productshorts of this TemplateQueryV2.
        :rtype: list[str]
        """
        return self._productshorts

    @productshorts.setter
    def productshorts(self, productshorts):
        r"""Sets the productshorts of this TemplateQueryV2.

        模板关联的云产品(产品短名)列表。

        :param productshorts: The productshorts of this TemplateQueryV2.
        :type productshorts: list[str]
        """
        self._productshorts = productshorts

    @property
    def offset(self):
        r"""Gets the offset of this TemplateQueryV2.

        偏移量，表示从此偏移量开始查询，offset大于等于0。

        :return: The offset of this TemplateQueryV2.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this TemplateQueryV2.

        偏移量，表示从此偏移量开始查询，offset大于等于0。

        :param offset: The offset of this TemplateQueryV2.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this TemplateQueryV2.

        每页的模板条数。

        :return: The limit of this TemplateQueryV2.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this TemplateQueryV2.

        每页的模板条数。

        :param limit: The limit of this TemplateQueryV2.
        :type limit: int
        """
        self._limit = limit

    @property
    def tag_ids(self):
        r"""Gets the tag_ids of this TemplateQueryV2.

        模板关联的自定义标签列表。

        :return: The tag_ids of this TemplateQueryV2.
        :rtype: list[str]
        """
        return self._tag_ids

    @tag_ids.setter
    def tag_ids(self, tag_ids):
        r"""Sets the tag_ids of this TemplateQueryV2.

        模板关联的自定义标签列表。

        :param tag_ids: The tag_ids of this TemplateQueryV2.
        :type tag_ids: list[str]
        """
        self._tag_ids = tag_ids

    @property
    def types(self):
        r"""Gets the types of this TemplateQueryV2.

        模板类型： - 0：doc - 1：code - 2：pipeline - 3：devops 

        :return: The types of this TemplateQueryV2.
        :rtype: list[int]
        """
        return self._types

    @types.setter
    def types(self, types):
        r"""Sets the types of this TemplateQueryV2.

        模板类型： - 0：doc - 1：code - 2：pipeline - 3：devops 

        :param types: The types of this TemplateQueryV2.
        :type types: list[int]
        """
        self._types = types

    @property
    def is_static(self):
        r"""Gets the is_static of this TemplateQueryV2.

        动、静态代码模板标识： - 0：动态模板codetemplate - 1：静态模板codesample 

        :return: The is_static of this TemplateQueryV2.
        :rtype: int
        """
        return self._is_static

    @is_static.setter
    def is_static(self, is_static):
        r"""Sets the is_static of this TemplateQueryV2.

        动、静态代码模板标识： - 0：动态模板codetemplate - 1：静态模板codesample 

        :param is_static: The is_static of this TemplateQueryV2.
        :type is_static: int
        """
        self._is_static = is_static

    @property
    def platform_source(self):
        r"""Gets the platform_source of this TemplateQueryV2.

        平台来源： - 0：codelabs - 1：devstar 

        :return: The platform_source of this TemplateQueryV2.
        :rtype: list[int]
        """
        return self._platform_source

    @platform_source.setter
    def platform_source(self, platform_source):
        r"""Sets the platform_source of this TemplateQueryV2.

        平台来源： - 0：codelabs - 1：devstar 

        :param platform_source: The platform_source of this TemplateQueryV2.
        :type platform_source: list[int]
        """
        self._platform_source = platform_source

    @property
    def tag_names(self):
        r"""Gets the tag_names of this TemplateQueryV2.

        模板关联的标签名称列表。

        :return: The tag_names of this TemplateQueryV2.
        :rtype: list[str]
        """
        return self._tag_names

    @tag_names.setter
    def tag_names(self, tag_names):
        r"""Sets the tag_names of this TemplateQueryV2.

        模板关联的标签名称列表。

        :param tag_names: The tag_names of this TemplateQueryV2.
        :type tag_names: list[str]
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
        if not isinstance(other, TemplateQueryV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
