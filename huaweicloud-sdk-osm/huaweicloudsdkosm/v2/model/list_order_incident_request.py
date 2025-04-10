# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOrderIncidentRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'search_key': 'list[str]',
        'label_id_list': 'list[int]',
        'app_key': 'str',
        'incident_id': 'str',
        'query_start_time': 'str',
        'query_end_time': 'str',
        'status': 'int',
        'incident_status': 'str',
        'x_customer_name': 'str',
        'group_id': 'str',
        'product_category_id': 'str',
        'business_type_id': 'str',
        'page_no': 'int',
        'page_size': 'int',
        'x_customer_id': 'str'
    }

    attribute_map = {
        'version': 'version',
        'search_key': 'searchKey',
        'label_id_list': 'labelIdList',
        'app_key': 'appKey',
        'incident_id': 'incidentId',
        'query_start_time': 'queryStartTime',
        'query_end_time': 'queryEndTime',
        'status': 'status',
        'incident_status': 'incidentStatus',
        'x_customer_name': 'xCustomerName',
        'group_id': 'groupId',
        'product_category_id': 'productCategoryId',
        'business_type_id': 'businessTypeId',
        'page_no': 'pageNo',
        'page_size': 'pageSize',
        'x_customer_id': 'xCustomerId'
    }

    def __init__(self, version=None, search_key=None, label_id_list=None, app_key=None, incident_id=None, query_start_time=None, query_end_time=None, status=None, incident_status=None, x_customer_name=None, group_id=None, product_category_id=None, business_type_id=None, page_no=None, page_size=None, x_customer_id=None):
        r"""ListOrderIncidentRequest

        The model defined in huaweicloud sdk

        :param version: 版本号
        :type version: str
        :param search_key: 关键字
        :type search_key: list[str]
        :param label_id_list: 标签列表
        :type label_id_list: list[int]
        :param app_key: appKey
        :type app_key: str
        :param incident_id: incidentId
        :type incident_id: str
        :param query_start_time: 查询开始时间
        :type query_start_time: str
        :param query_end_time: 查询结束时间
        :type query_end_time: str
        :param status: 状态
        :type status: int
        :param incident_status: 工单状态
        :type incident_status: str
        :param x_customer_name: 用户名称
        :type x_customer_name: str
        :param group_id: 分组
        :type group_id: str
        :param product_category_id: 产品分类
        :type product_category_id: str
        :param business_type_id: 类型
        :type business_type_id: str
        :param page_no: 页码
        :type page_no: int
        :param page_size: 分页大小
        :type page_size: int
        :param x_customer_id: 客户id
        :type x_customer_id: str
        """
        
        

        self._version = None
        self._search_key = None
        self._label_id_list = None
        self._app_key = None
        self._incident_id = None
        self._query_start_time = None
        self._query_end_time = None
        self._status = None
        self._incident_status = None
        self._x_customer_name = None
        self._group_id = None
        self._product_category_id = None
        self._business_type_id = None
        self._page_no = None
        self._page_size = None
        self._x_customer_id = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if search_key is not None:
            self.search_key = search_key
        if label_id_list is not None:
            self.label_id_list = label_id_list
        if app_key is not None:
            self.app_key = app_key
        if incident_id is not None:
            self.incident_id = incident_id
        if query_start_time is not None:
            self.query_start_time = query_start_time
        if query_end_time is not None:
            self.query_end_time = query_end_time
        if status is not None:
            self.status = status
        if incident_status is not None:
            self.incident_status = incident_status
        if x_customer_name is not None:
            self.x_customer_name = x_customer_name
        if group_id is not None:
            self.group_id = group_id
        if product_category_id is not None:
            self.product_category_id = product_category_id
        if business_type_id is not None:
            self.business_type_id = business_type_id
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size
        if x_customer_id is not None:
            self.x_customer_id = x_customer_id

    @property
    def version(self):
        r"""Gets the version of this ListOrderIncidentRequest.

        版本号

        :return: The version of this ListOrderIncidentRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ListOrderIncidentRequest.

        版本号

        :param version: The version of this ListOrderIncidentRequest.
        :type version: str
        """
        self._version = version

    @property
    def search_key(self):
        r"""Gets the search_key of this ListOrderIncidentRequest.

        关键字

        :return: The search_key of this ListOrderIncidentRequest.
        :rtype: list[str]
        """
        return self._search_key

    @search_key.setter
    def search_key(self, search_key):
        r"""Sets the search_key of this ListOrderIncidentRequest.

        关键字

        :param search_key: The search_key of this ListOrderIncidentRequest.
        :type search_key: list[str]
        """
        self._search_key = search_key

    @property
    def label_id_list(self):
        r"""Gets the label_id_list of this ListOrderIncidentRequest.

        标签列表

        :return: The label_id_list of this ListOrderIncidentRequest.
        :rtype: list[int]
        """
        return self._label_id_list

    @label_id_list.setter
    def label_id_list(self, label_id_list):
        r"""Sets the label_id_list of this ListOrderIncidentRequest.

        标签列表

        :param label_id_list: The label_id_list of this ListOrderIncidentRequest.
        :type label_id_list: list[int]
        """
        self._label_id_list = label_id_list

    @property
    def app_key(self):
        r"""Gets the app_key of this ListOrderIncidentRequest.

        appKey

        :return: The app_key of this ListOrderIncidentRequest.
        :rtype: str
        """
        return self._app_key

    @app_key.setter
    def app_key(self, app_key):
        r"""Sets the app_key of this ListOrderIncidentRequest.

        appKey

        :param app_key: The app_key of this ListOrderIncidentRequest.
        :type app_key: str
        """
        self._app_key = app_key

    @property
    def incident_id(self):
        r"""Gets the incident_id of this ListOrderIncidentRequest.

        incidentId

        :return: The incident_id of this ListOrderIncidentRequest.
        :rtype: str
        """
        return self._incident_id

    @incident_id.setter
    def incident_id(self, incident_id):
        r"""Sets the incident_id of this ListOrderIncidentRequest.

        incidentId

        :param incident_id: The incident_id of this ListOrderIncidentRequest.
        :type incident_id: str
        """
        self._incident_id = incident_id

    @property
    def query_start_time(self):
        r"""Gets the query_start_time of this ListOrderIncidentRequest.

        查询开始时间

        :return: The query_start_time of this ListOrderIncidentRequest.
        :rtype: str
        """
        return self._query_start_time

    @query_start_time.setter
    def query_start_time(self, query_start_time):
        r"""Sets the query_start_time of this ListOrderIncidentRequest.

        查询开始时间

        :param query_start_time: The query_start_time of this ListOrderIncidentRequest.
        :type query_start_time: str
        """
        self._query_start_time = query_start_time

    @property
    def query_end_time(self):
        r"""Gets the query_end_time of this ListOrderIncidentRequest.

        查询结束时间

        :return: The query_end_time of this ListOrderIncidentRequest.
        :rtype: str
        """
        return self._query_end_time

    @query_end_time.setter
    def query_end_time(self, query_end_time):
        r"""Sets the query_end_time of this ListOrderIncidentRequest.

        查询结束时间

        :param query_end_time: The query_end_time of this ListOrderIncidentRequest.
        :type query_end_time: str
        """
        self._query_end_time = query_end_time

    @property
    def status(self):
        r"""Gets the status of this ListOrderIncidentRequest.

        状态

        :return: The status of this ListOrderIncidentRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListOrderIncidentRequest.

        状态

        :param status: The status of this ListOrderIncidentRequest.
        :type status: int
        """
        self._status = status

    @property
    def incident_status(self):
        r"""Gets the incident_status of this ListOrderIncidentRequest.

        工单状态

        :return: The incident_status of this ListOrderIncidentRequest.
        :rtype: str
        """
        return self._incident_status

    @incident_status.setter
    def incident_status(self, incident_status):
        r"""Sets the incident_status of this ListOrderIncidentRequest.

        工单状态

        :param incident_status: The incident_status of this ListOrderIncidentRequest.
        :type incident_status: str
        """
        self._incident_status = incident_status

    @property
    def x_customer_name(self):
        r"""Gets the x_customer_name of this ListOrderIncidentRequest.

        用户名称

        :return: The x_customer_name of this ListOrderIncidentRequest.
        :rtype: str
        """
        return self._x_customer_name

    @x_customer_name.setter
    def x_customer_name(self, x_customer_name):
        r"""Sets the x_customer_name of this ListOrderIncidentRequest.

        用户名称

        :param x_customer_name: The x_customer_name of this ListOrderIncidentRequest.
        :type x_customer_name: str
        """
        self._x_customer_name = x_customer_name

    @property
    def group_id(self):
        r"""Gets the group_id of this ListOrderIncidentRequest.

        分组

        :return: The group_id of this ListOrderIncidentRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ListOrderIncidentRequest.

        分组

        :param group_id: The group_id of this ListOrderIncidentRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def product_category_id(self):
        r"""Gets the product_category_id of this ListOrderIncidentRequest.

        产品分类

        :return: The product_category_id of this ListOrderIncidentRequest.
        :rtype: str
        """
        return self._product_category_id

    @product_category_id.setter
    def product_category_id(self, product_category_id):
        r"""Sets the product_category_id of this ListOrderIncidentRequest.

        产品分类

        :param product_category_id: The product_category_id of this ListOrderIncidentRequest.
        :type product_category_id: str
        """
        self._product_category_id = product_category_id

    @property
    def business_type_id(self):
        r"""Gets the business_type_id of this ListOrderIncidentRequest.

        类型

        :return: The business_type_id of this ListOrderIncidentRequest.
        :rtype: str
        """
        return self._business_type_id

    @business_type_id.setter
    def business_type_id(self, business_type_id):
        r"""Sets the business_type_id of this ListOrderIncidentRequest.

        类型

        :param business_type_id: The business_type_id of this ListOrderIncidentRequest.
        :type business_type_id: str
        """
        self._business_type_id = business_type_id

    @property
    def page_no(self):
        r"""Gets the page_no of this ListOrderIncidentRequest.

        页码

        :return: The page_no of this ListOrderIncidentRequest.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        r"""Sets the page_no of this ListOrderIncidentRequest.

        页码

        :param page_no: The page_no of this ListOrderIncidentRequest.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def page_size(self):
        r"""Gets the page_size of this ListOrderIncidentRequest.

        分页大小

        :return: The page_size of this ListOrderIncidentRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListOrderIncidentRequest.

        分页大小

        :param page_size: The page_size of this ListOrderIncidentRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def x_customer_id(self):
        r"""Gets the x_customer_id of this ListOrderIncidentRequest.

        客户id

        :return: The x_customer_id of this ListOrderIncidentRequest.
        :rtype: str
        """
        return self._x_customer_id

    @x_customer_id.setter
    def x_customer_id(self, x_customer_id):
        r"""Sets the x_customer_id of this ListOrderIncidentRequest.

        客户id

        :param x_customer_id: The x_customer_id of this ListOrderIncidentRequest.
        :type x_customer_id: str
        """
        self._x_customer_id = x_customer_id

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
        if not isinstance(other, ListOrderIncidentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
