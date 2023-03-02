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
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, name=None, is_default=None, create_by=None, script_id=None, page_num=None, page_size=None, project_id=None, order_by_column=None, sort_order=None, enterprise_project_id=None):
        """SearchScriptsRequestBody

        The model defined in huaweicloud sdk

        :param name: 查询接收的参数，版本管理时，name为脚本名称（版本管理查询时name不能为空），脚本管理页面查询时，name为接收模糊查询的参数，name是null，表示查询所有默认脚本。
        :type name: str
        :param is_default: 查询规则，如果是类型为default，则为模糊查询和脚本管理主页展示，no_default为版本管理。
        :type is_default: str
        :param create_by: 创建人，默认按照创建人搜索脚本。
        :type create_by: str
        :param script_id: 版本管理时需要查询的脚本id。
        :type script_id: str
        :param page_num: page_num为正整数。
        :type page_num: int
        :param page_size: 每页显示的条数，默认值是10。
        :type page_size: int
        :param project_id: 项目id。
        :type project_id: str
        :param order_by_column: 需要排序的字段(默认为更新时间),支持字段有name,create_time和update_time。
        :type order_by_column: str
        :param sort_order: 排序规则(默认降序) 传入升序或降序，升序：ASC，降序：DESC。
        :type sort_order: str
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
        if project_id is not None:
            self.project_id = project_id
        self.order_by_column = order_by_column
        if sort_order is not None:
            self.sort_order = sort_order
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def name(self):
        """Gets the name of this SearchScriptsRequestBody.

        查询接收的参数，版本管理时，name为脚本名称（版本管理查询时name不能为空），脚本管理页面查询时，name为接收模糊查询的参数，name是null，表示查询所有默认脚本。

        :return: The name of this SearchScriptsRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SearchScriptsRequestBody.

        查询接收的参数，版本管理时，name为脚本名称（版本管理查询时name不能为空），脚本管理页面查询时，name为接收模糊查询的参数，name是null，表示查询所有默认脚本。

        :param name: The name of this SearchScriptsRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def is_default(self):
        """Gets the is_default of this SearchScriptsRequestBody.

        查询规则，如果是类型为default，则为模糊查询和脚本管理主页展示，no_default为版本管理。

        :return: The is_default of this SearchScriptsRequestBody.
        :rtype: str
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this SearchScriptsRequestBody.

        查询规则，如果是类型为default，则为模糊查询和脚本管理主页展示，no_default为版本管理。

        :param is_default: The is_default of this SearchScriptsRequestBody.
        :type is_default: str
        """
        self._is_default = is_default

    @property
    def create_by(self):
        """Gets the create_by of this SearchScriptsRequestBody.

        创建人，默认按照创建人搜索脚本。

        :return: The create_by of this SearchScriptsRequestBody.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this SearchScriptsRequestBody.

        创建人，默认按照创建人搜索脚本。

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

        page_num为正整数。

        :return: The page_num of this SearchScriptsRequestBody.
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        """Sets the page_num of this SearchScriptsRequestBody.

        page_num为正整数。

        :param page_num: The page_num of this SearchScriptsRequestBody.
        :type page_num: int
        """
        self._page_num = page_num

    @property
    def page_size(self):
        """Gets the page_size of this SearchScriptsRequestBody.

        每页显示的条数，默认值是10。

        :return: The page_size of this SearchScriptsRequestBody.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this SearchScriptsRequestBody.

        每页显示的条数，默认值是10。

        :param page_size: The page_size of this SearchScriptsRequestBody.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def project_id(self):
        """Gets the project_id of this SearchScriptsRequestBody.

        项目id。

        :return: The project_id of this SearchScriptsRequestBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this SearchScriptsRequestBody.

        项目id。

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
