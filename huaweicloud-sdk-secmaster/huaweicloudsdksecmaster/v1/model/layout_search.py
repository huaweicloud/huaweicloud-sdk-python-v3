# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LayoutSearch:

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
        'used_by': 'str',
        'binding_code': 'str',
        'is_built_in': 'bool',
        'is_template': 'bool',
        'is_default': 'bool',
        'layout_type': 'str',
        'offset': 'int',
        'limit': 'int',
        'sort_key': 'str',
        'sort_dir': 'str',
        'search_txt': 'str',
        'from_date': 'str',
        'to_date': 'str'
    }

    attribute_map = {
        'name': 'name',
        'used_by': 'used_by',
        'binding_code': 'binding_code',
        'is_built_in': 'is_built_in',
        'is_template': 'is_template',
        'is_default': 'is_default',
        'layout_type': 'layout_type',
        'offset': 'offset',
        'limit': 'limit',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'search_txt': 'search_txt',
        'from_date': 'from_date',
        'to_date': 'to_date'
    }

    def __init__(self, name=None, used_by=None, binding_code=None, is_built_in=None, is_template=None, is_default=None, layout_type=None, offset=None, limit=None, sort_key=None, sort_dir=None, search_txt=None, from_date=None, to_date=None):
        r"""LayoutSearch

        The model defined in huaweicloud sdk

        :param name: 布局名称
        :type name: str
        :param used_by: 布局类型
        :type used_by: str
        :param binding_code: 创建布局选择的数据类的business_code
        :type binding_code: str
        :param is_built_in: 是否为系统内置
        :type is_built_in: bool
        :param is_template: 是否为模板
        :type is_template: bool
        :param is_default: 是否为默认布局
        :type is_default: bool
        :param layout_type: 布局页面类型
        :type layout_type: str
        :param offset: 分页
        :type offset: int
        :param limit: 每页个数
        :type limit: int
        :param sort_key: 排序字段
        :type sort_key: str
        :param sort_dir: 升序或者降序排列
        :type sort_dir: str
        :param search_txt: 搜索关键字
        :type search_txt: str
        :param from_date: 起始时间
        :type from_date: str
        :param to_date: 结束时间
        :type to_date: str
        """
        
        

        self._name = None
        self._used_by = None
        self._binding_code = None
        self._is_built_in = None
        self._is_template = None
        self._is_default = None
        self._layout_type = None
        self._offset = None
        self._limit = None
        self._sort_key = None
        self._sort_dir = None
        self._search_txt = None
        self._from_date = None
        self._to_date = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if used_by is not None:
            self.used_by = used_by
        if binding_code is not None:
            self.binding_code = binding_code
        if is_built_in is not None:
            self.is_built_in = is_built_in
        if is_template is not None:
            self.is_template = is_template
        if is_default is not None:
            self.is_default = is_default
        if layout_type is not None:
            self.layout_type = layout_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if search_txt is not None:
            self.search_txt = search_txt
        if from_date is not None:
            self.from_date = from_date
        if to_date is not None:
            self.to_date = to_date

    @property
    def name(self):
        r"""Gets the name of this LayoutSearch.

        布局名称

        :return: The name of this LayoutSearch.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this LayoutSearch.

        布局名称

        :param name: The name of this LayoutSearch.
        :type name: str
        """
        self._name = name

    @property
    def used_by(self):
        r"""Gets the used_by of this LayoutSearch.

        布局类型

        :return: The used_by of this LayoutSearch.
        :rtype: str
        """
        return self._used_by

    @used_by.setter
    def used_by(self, used_by):
        r"""Sets the used_by of this LayoutSearch.

        布局类型

        :param used_by: The used_by of this LayoutSearch.
        :type used_by: str
        """
        self._used_by = used_by

    @property
    def binding_code(self):
        r"""Gets the binding_code of this LayoutSearch.

        创建布局选择的数据类的business_code

        :return: The binding_code of this LayoutSearch.
        :rtype: str
        """
        return self._binding_code

    @binding_code.setter
    def binding_code(self, binding_code):
        r"""Sets the binding_code of this LayoutSearch.

        创建布局选择的数据类的business_code

        :param binding_code: The binding_code of this LayoutSearch.
        :type binding_code: str
        """
        self._binding_code = binding_code

    @property
    def is_built_in(self):
        r"""Gets the is_built_in of this LayoutSearch.

        是否为系统内置

        :return: The is_built_in of this LayoutSearch.
        :rtype: bool
        """
        return self._is_built_in

    @is_built_in.setter
    def is_built_in(self, is_built_in):
        r"""Sets the is_built_in of this LayoutSearch.

        是否为系统内置

        :param is_built_in: The is_built_in of this LayoutSearch.
        :type is_built_in: bool
        """
        self._is_built_in = is_built_in

    @property
    def is_template(self):
        r"""Gets the is_template of this LayoutSearch.

        是否为模板

        :return: The is_template of this LayoutSearch.
        :rtype: bool
        """
        return self._is_template

    @is_template.setter
    def is_template(self, is_template):
        r"""Sets the is_template of this LayoutSearch.

        是否为模板

        :param is_template: The is_template of this LayoutSearch.
        :type is_template: bool
        """
        self._is_template = is_template

    @property
    def is_default(self):
        r"""Gets the is_default of this LayoutSearch.

        是否为默认布局

        :return: The is_default of this LayoutSearch.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        r"""Sets the is_default of this LayoutSearch.

        是否为默认布局

        :param is_default: The is_default of this LayoutSearch.
        :type is_default: bool
        """
        self._is_default = is_default

    @property
    def layout_type(self):
        r"""Gets the layout_type of this LayoutSearch.

        布局页面类型

        :return: The layout_type of this LayoutSearch.
        :rtype: str
        """
        return self._layout_type

    @layout_type.setter
    def layout_type(self, layout_type):
        r"""Sets the layout_type of this LayoutSearch.

        布局页面类型

        :param layout_type: The layout_type of this LayoutSearch.
        :type layout_type: str
        """
        self._layout_type = layout_type

    @property
    def offset(self):
        r"""Gets the offset of this LayoutSearch.

        分页

        :return: The offset of this LayoutSearch.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this LayoutSearch.

        分页

        :param offset: The offset of this LayoutSearch.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this LayoutSearch.

        每页个数

        :return: The limit of this LayoutSearch.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this LayoutSearch.

        每页个数

        :param limit: The limit of this LayoutSearch.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_key(self):
        r"""Gets the sort_key of this LayoutSearch.

        排序字段

        :return: The sort_key of this LayoutSearch.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this LayoutSearch.

        排序字段

        :param sort_key: The sort_key of this LayoutSearch.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this LayoutSearch.

        升序或者降序排列

        :return: The sort_dir of this LayoutSearch.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this LayoutSearch.

        升序或者降序排列

        :param sort_dir: The sort_dir of this LayoutSearch.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def search_txt(self):
        r"""Gets the search_txt of this LayoutSearch.

        搜索关键字

        :return: The search_txt of this LayoutSearch.
        :rtype: str
        """
        return self._search_txt

    @search_txt.setter
    def search_txt(self, search_txt):
        r"""Sets the search_txt of this LayoutSearch.

        搜索关键字

        :param search_txt: The search_txt of this LayoutSearch.
        :type search_txt: str
        """
        self._search_txt = search_txt

    @property
    def from_date(self):
        r"""Gets the from_date of this LayoutSearch.

        起始时间

        :return: The from_date of this LayoutSearch.
        :rtype: str
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        r"""Sets the from_date of this LayoutSearch.

        起始时间

        :param from_date: The from_date of this LayoutSearch.
        :type from_date: str
        """
        self._from_date = from_date

    @property
    def to_date(self):
        r"""Gets the to_date of this LayoutSearch.

        结束时间

        :return: The to_date of this LayoutSearch.
        :rtype: str
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        r"""Sets the to_date of this LayoutSearch.

        结束时间

        :param to_date: The to_date of this LayoutSearch.
        :type to_date: str
        """
        self._to_date = to_date

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LayoutSearch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
