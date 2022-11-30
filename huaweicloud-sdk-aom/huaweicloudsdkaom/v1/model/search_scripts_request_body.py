# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchScriptsRequestBody:

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
        'is_default': 'str',
        'create_by': 'str',
        'script_id': 'str',
        'page_num': 'int',
        'page_size': 'int',
        'project_id': 'str',
        'order_by_column': 'str',
        'sort_order': 'str',
        'page_total': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'is_default': 'is_default',
        'create_by': 'create_by',
        'script_id': 'script_id',
        'page_num': 'page_num',
        'page_size': 'page_size',
        'project_id': 'project_id',
        'order_by_column': 'order_by_column',
        'sort_order': 'sort_order',
        'page_total': 'page_total',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, name=None, is_default=None, create_by=None, script_id=None, page_num=None, page_size=None, project_id=None, order_by_column=None, sort_order=None, page_total=None, enterprise_project_id=None):
        """SearchScriptsRequestBody

        The model defined in huaweicloud sdk

        :param name: 查询接收的的参数，版本管理时，name为脚本名称（版本管理查询时name不能为空），页面查询时，name为接收模糊查询的参数，name是null，表示查询所有默认脚本。
        :type name: str
        :param is_default: 查询规则，default表示脚本管理主页查询，包括模糊查询，no_default就是版本管理,当defalult不输入（参数为空）进行查询时，默认是页面查询,废弃字段，传入不影响使用。
        :type is_default: str
        :param create_by: 创建人，默认按照创建人搜说脚本。
        :type create_by: str
        :param script_id: 版本管理时需要查询的脚本id。
        :type script_id: str
        :param page_num: 当前页，查询的当前页，page_num为正整数，不能是0和负数，当输入参数为负数，0和大于1000，自动修正参数为1，默认值是1（用户不传，值是1）。
        :type page_num: int
        :param page_size: 每页显示的条数，每页查询的总条数，page_size为正整数，不能是0和负数，当输入参数为负数，0和大于101，自动修正参数为10，默认值是10（用户不传时，值是10）。
        :type page_size: int
        :param project_id: 项目id，版本管理参数，当时page_total为total,返回出改脚本名称下所有的脚本对象,传入其他参数无意义，，当前进行 版本管理时，需要分页显示脚本名称下所有对象，传入空值即可。
        :type project_id: str
        :param order_by_column: 需要排序的字段(默认为更新时间),支持字段有name,create_time和update_time。
        :type order_by_column: str
        :param sort_order: 排序规则(默认降序) 传入升序或降序，升序：ASC，降序：DESC。
        :type sort_order: str
        :param page_total: 版本管理参数，当时page_total为total,返回出改脚本名称下所有的脚本对象,传入其他参数无意义，，当前进行 版本管理时，需要分页显示脚本名称下所有对象，传入空值即可。
        :type page_total: str
        :param enterprise_project_id: 企业项目id，根据企业项目id搜索。
        :type enterprise_project_id: str
        """
        
        

        self._name = None
        self._is_default = None
        self._create_by = None
        self._script_id = None
        self._page_num = None
        self._page_size = None
        self._project_id = None
        self._order_by_column = None
        self._sort_order = None
        self._page_total = None
        self._enterprise_project_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if is_default is not None:
            self.is_default = is_default
        if create_by is not None:
            self.create_by = create_by
        if script_id is not None:
            self.script_id = script_id
        if page_num is not None:
            self.page_num = page_num
        if page_size is not None:
            self.page_size = page_size
        self.project_id = project_id
        if order_by_column is not None:
            self.order_by_column = order_by_column
        if sort_order is not None:
            self.sort_order = sort_order
        if page_total is not None:
            self.page_total = page_total
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def name(self):
        """Gets the name of this SearchScriptsRequestBody.

        查询接收的的参数，版本管理时，name为脚本名称（版本管理查询时name不能为空），页面查询时，name为接收模糊查询的参数，name是null，表示查询所有默认脚本。

        :return: The name of this SearchScriptsRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SearchScriptsRequestBody.

        查询接收的的参数，版本管理时，name为脚本名称（版本管理查询时name不能为空），页面查询时，name为接收模糊查询的参数，name是null，表示查询所有默认脚本。

        :param name: The name of this SearchScriptsRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def is_default(self):
        """Gets the is_default of this SearchScriptsRequestBody.

        查询规则，default表示脚本管理主页查询，包括模糊查询，no_default就是版本管理,当defalult不输入（参数为空）进行查询时，默认是页面查询,废弃字段，传入不影响使用。

        :return: The is_default of this SearchScriptsRequestBody.
        :rtype: str
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this SearchScriptsRequestBody.

        查询规则，default表示脚本管理主页查询，包括模糊查询，no_default就是版本管理,当defalult不输入（参数为空）进行查询时，默认是页面查询,废弃字段，传入不影响使用。

        :param is_default: The is_default of this SearchScriptsRequestBody.
        :type is_default: str
        """
        self._is_default = is_default

    @property
    def create_by(self):
        """Gets the create_by of this SearchScriptsRequestBody.

        创建人，默认按照创建人搜说脚本。

        :return: The create_by of this SearchScriptsRequestBody.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this SearchScriptsRequestBody.

        创建人，默认按照创建人搜说脚本。

        :param create_by: The create_by of this SearchScriptsRequestBody.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def script_id(self):
        """Gets the script_id of this SearchScriptsRequestBody.

        版本管理时需要查询的脚本id。

        :return: The script_id of this SearchScriptsRequestBody.
        :rtype: str
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id):
        """Sets the script_id of this SearchScriptsRequestBody.

        版本管理时需要查询的脚本id。

        :param script_id: The script_id of this SearchScriptsRequestBody.
        :type script_id: str
        """
        self._script_id = script_id

    @property
    def page_num(self):
        """Gets the page_num of this SearchScriptsRequestBody.

        当前页，查询的当前页，page_num为正整数，不能是0和负数，当输入参数为负数，0和大于1000，自动修正参数为1，默认值是1（用户不传，值是1）。

        :return: The page_num of this SearchScriptsRequestBody.
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        """Sets the page_num of this SearchScriptsRequestBody.

        当前页，查询的当前页，page_num为正整数，不能是0和负数，当输入参数为负数，0和大于1000，自动修正参数为1，默认值是1（用户不传，值是1）。

        :param page_num: The page_num of this SearchScriptsRequestBody.
        :type page_num: int
        """
        self._page_num = page_num

    @property
    def page_size(self):
        """Gets the page_size of this SearchScriptsRequestBody.

        每页显示的条数，每页查询的总条数，page_size为正整数，不能是0和负数，当输入参数为负数，0和大于101，自动修正参数为10，默认值是10（用户不传时，值是10）。

        :return: The page_size of this SearchScriptsRequestBody.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this SearchScriptsRequestBody.

        每页显示的条数，每页查询的总条数，page_size为正整数，不能是0和负数，当输入参数为负数，0和大于101，自动修正参数为10，默认值是10（用户不传时，值是10）。

        :param page_size: The page_size of this SearchScriptsRequestBody.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def project_id(self):
        """Gets the project_id of this SearchScriptsRequestBody.

        项目id，版本管理参数，当时page_total为total,返回出改脚本名称下所有的脚本对象,传入其他参数无意义，，当前进行 版本管理时，需要分页显示脚本名称下所有对象，传入空值即可。

        :return: The project_id of this SearchScriptsRequestBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this SearchScriptsRequestBody.

        项目id，版本管理参数，当时page_total为total,返回出改脚本名称下所有的脚本对象,传入其他参数无意义，，当前进行 版本管理时，需要分页显示脚本名称下所有对象，传入空值即可。

        :param project_id: The project_id of this SearchScriptsRequestBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def order_by_column(self):
        """Gets the order_by_column of this SearchScriptsRequestBody.

        需要排序的字段(默认为更新时间),支持字段有name,create_time和update_time。

        :return: The order_by_column of this SearchScriptsRequestBody.
        :rtype: str
        """
        return self._order_by_column

    @order_by_column.setter
    def order_by_column(self, order_by_column):
        """Sets the order_by_column of this SearchScriptsRequestBody.

        需要排序的字段(默认为更新时间),支持字段有name,create_time和update_time。

        :param order_by_column: The order_by_column of this SearchScriptsRequestBody.
        :type order_by_column: str
        """
        self._order_by_column = order_by_column

    @property
    def sort_order(self):
        """Gets the sort_order of this SearchScriptsRequestBody.

        排序规则(默认降序) 传入升序或降序，升序：ASC，降序：DESC。

        :return: The sort_order of this SearchScriptsRequestBody.
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this SearchScriptsRequestBody.

        排序规则(默认降序) 传入升序或降序，升序：ASC，降序：DESC。

        :param sort_order: The sort_order of this SearchScriptsRequestBody.
        :type sort_order: str
        """
        self._sort_order = sort_order

    @property
    def page_total(self):
        """Gets the page_total of this SearchScriptsRequestBody.

        版本管理参数，当时page_total为total,返回出改脚本名称下所有的脚本对象,传入其他参数无意义，，当前进行 版本管理时，需要分页显示脚本名称下所有对象，传入空值即可。

        :return: The page_total of this SearchScriptsRequestBody.
        :rtype: str
        """
        return self._page_total

    @page_total.setter
    def page_total(self, page_total):
        """Sets the page_total of this SearchScriptsRequestBody.

        版本管理参数，当时page_total为total,返回出改脚本名称下所有的脚本对象,传入其他参数无意义，，当前进行 版本管理时，需要分页显示脚本名称下所有对象，传入空值即可。

        :param page_total: The page_total of this SearchScriptsRequestBody.
        :type page_total: str
        """
        self._page_total = page_total

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this SearchScriptsRequestBody.

        企业项目id，根据企业项目id搜索。

        :return: The enterprise_project_id of this SearchScriptsRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this SearchScriptsRequestBody.

        企业项目id，根据企业项目id搜索。

        :param enterprise_project_id: The enterprise_project_id of this SearchScriptsRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, SearchScriptsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
