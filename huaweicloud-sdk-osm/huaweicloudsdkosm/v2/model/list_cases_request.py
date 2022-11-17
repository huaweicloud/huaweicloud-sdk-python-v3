# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCasesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'search_key': 'list[str]',
        'label_id_list': 'list[str]',
        'app_key': 'str',
        'incident_id': 'str',
        'query_start_time': 'str',
        'query_end_time': 'str',
        'status': 'int',
        'incident_status': 'str',
        'x_customer_id': 'str',
        'x_customer_name': 'str',
        'group_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'x_site': 'int',
        'x_language': 'str',
        'x_time_zone': 'str'
    }

    attribute_map = {
        'search_key': 'search_key',
        'label_id_list': 'label_id_list',
        'app_key': 'app_key',
        'incident_id': 'incident_id',
        'query_start_time': 'query_start_time',
        'query_end_time': 'query_end_time',
        'status': 'status',
        'incident_status': 'incident_status',
        'x_customer_id': 'x_customer_id',
        'x_customer_name': 'x_customer_name',
        'group_id': 'group_id',
        'offset': 'offset',
        'limit': 'limit',
        'x_site': 'X-Site',
        'x_language': 'X-Language',
        'x_time_zone': 'X-Time-Zone'
    }

    def __init__(self, search_key=None, label_id_list=None, app_key=None, incident_id=None, query_start_time=None, query_end_time=None, status=None, incident_status=None, x_customer_id=None, x_customer_name=None, group_id=None, offset=None, limit=None, x_site=None, x_language=None, x_time_zone=None):
        """ListCasesRequest

        The model defined in huaweicloud sdk

        :param search_key: 关键字查询，支持多个空格隔开
        :type search_key: list[str]
        :param label_id_list: 标签列表，最多支持5个
        :type label_id_list: list[str]
        :param app_key: app关键字查询
        :type app_key: str
        :param incident_id: 工单id
        :type incident_id: str
        :param query_start_time: 查询开始时间
        :type query_start_time: str
        :param query_end_time: 查询结束时间
        :type query_end_time: str
        :param status: 状态 0：待受理 1：处理中 2：待确认结果 3：已完成 4：已撤销 12：无效 17： 待反馈
        :type status: int
        :param incident_status: 状态列表
        :type incident_status: str
        :param x_customer_id: 子用户id
        :type x_customer_id: str
        :param x_customer_name: 子用户名称
        :type x_customer_name: str
        :param group_id: 组id
        :type group_id: str
        :param offset: 查询偏移量
        :type offset: int
        :param limit: 查询限制数量
        :type limit: int
        :param x_site: 对接站点信息。  0（中国站） 1（国际站），不填的话默认为0。
        :type x_site: int
        :param x_language: 语言环境，值为通用的语言描述字符串，比如zh-cn等，默认为zh-cn。  会根据语言环境对应展示一些国际化的信息，比如工单类型名称等。
        :type x_language: str
        :param x_time_zone: 环境时区，值为通用的时区描述字符串，比如GMT+8等，默认为GMT+8。  涉及时间的数据会根据环境时区处理。
        :type x_time_zone: str
        """
        
        

        self._search_key = None
        self._label_id_list = None
        self._app_key = None
        self._incident_id = None
        self._query_start_time = None
        self._query_end_time = None
        self._status = None
        self._incident_status = None
        self._x_customer_id = None
        self._x_customer_name = None
        self._group_id = None
        self._offset = None
        self._limit = None
        self._x_site = None
        self._x_language = None
        self._x_time_zone = None
        self.discriminator = None

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
        if x_customer_id is not None:
            self.x_customer_id = x_customer_id
        if x_customer_name is not None:
            self.x_customer_name = x_customer_name
        if group_id is not None:
            self.group_id = group_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if x_site is not None:
            self.x_site = x_site
        if x_language is not None:
            self.x_language = x_language
        if x_time_zone is not None:
            self.x_time_zone = x_time_zone

    @property
    def search_key(self):
        """Gets the search_key of this ListCasesRequest.

        关键字查询，支持多个空格隔开

        :return: The search_key of this ListCasesRequest.
        :rtype: list[str]
        """
        return self._search_key

    @search_key.setter
    def search_key(self, search_key):
        """Sets the search_key of this ListCasesRequest.

        关键字查询，支持多个空格隔开

        :param search_key: The search_key of this ListCasesRequest.
        :type search_key: list[str]
        """
        self._search_key = search_key

    @property
    def label_id_list(self):
        """Gets the label_id_list of this ListCasesRequest.

        标签列表，最多支持5个

        :return: The label_id_list of this ListCasesRequest.
        :rtype: list[str]
        """
        return self._label_id_list

    @label_id_list.setter
    def label_id_list(self, label_id_list):
        """Sets the label_id_list of this ListCasesRequest.

        标签列表，最多支持5个

        :param label_id_list: The label_id_list of this ListCasesRequest.
        :type label_id_list: list[str]
        """
        self._label_id_list = label_id_list

    @property
    def app_key(self):
        """Gets the app_key of this ListCasesRequest.

        app关键字查询

        :return: The app_key of this ListCasesRequest.
        :rtype: str
        """
        return self._app_key

    @app_key.setter
    def app_key(self, app_key):
        """Sets the app_key of this ListCasesRequest.

        app关键字查询

        :param app_key: The app_key of this ListCasesRequest.
        :type app_key: str
        """
        self._app_key = app_key

    @property
    def incident_id(self):
        """Gets the incident_id of this ListCasesRequest.

        工单id

        :return: The incident_id of this ListCasesRequest.
        :rtype: str
        """
        return self._incident_id

    @incident_id.setter
    def incident_id(self, incident_id):
        """Sets the incident_id of this ListCasesRequest.

        工单id

        :param incident_id: The incident_id of this ListCasesRequest.
        :type incident_id: str
        """
        self._incident_id = incident_id

    @property
    def query_start_time(self):
        """Gets the query_start_time of this ListCasesRequest.

        查询开始时间

        :return: The query_start_time of this ListCasesRequest.
        :rtype: str
        """
        return self._query_start_time

    @query_start_time.setter
    def query_start_time(self, query_start_time):
        """Sets the query_start_time of this ListCasesRequest.

        查询开始时间

        :param query_start_time: The query_start_time of this ListCasesRequest.
        :type query_start_time: str
        """
        self._query_start_time = query_start_time

    @property
    def query_end_time(self):
        """Gets the query_end_time of this ListCasesRequest.

        查询结束时间

        :return: The query_end_time of this ListCasesRequest.
        :rtype: str
        """
        return self._query_end_time

    @query_end_time.setter
    def query_end_time(self, query_end_time):
        """Sets the query_end_time of this ListCasesRequest.

        查询结束时间

        :param query_end_time: The query_end_time of this ListCasesRequest.
        :type query_end_time: str
        """
        self._query_end_time = query_end_time

    @property
    def status(self):
        """Gets the status of this ListCasesRequest.

        状态 0：待受理 1：处理中 2：待确认结果 3：已完成 4：已撤销 12：无效 17： 待反馈

        :return: The status of this ListCasesRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListCasesRequest.

        状态 0：待受理 1：处理中 2：待确认结果 3：已完成 4：已撤销 12：无效 17： 待反馈

        :param status: The status of this ListCasesRequest.
        :type status: int
        """
        self._status = status

    @property
    def incident_status(self):
        """Gets the incident_status of this ListCasesRequest.

        状态列表

        :return: The incident_status of this ListCasesRequest.
        :rtype: str
        """
        return self._incident_status

    @incident_status.setter
    def incident_status(self, incident_status):
        """Sets the incident_status of this ListCasesRequest.

        状态列表

        :param incident_status: The incident_status of this ListCasesRequest.
        :type incident_status: str
        """
        self._incident_status = incident_status

    @property
    def x_customer_id(self):
        """Gets the x_customer_id of this ListCasesRequest.

        子用户id

        :return: The x_customer_id of this ListCasesRequest.
        :rtype: str
        """
        return self._x_customer_id

    @x_customer_id.setter
    def x_customer_id(self, x_customer_id):
        """Sets the x_customer_id of this ListCasesRequest.

        子用户id

        :param x_customer_id: The x_customer_id of this ListCasesRequest.
        :type x_customer_id: str
        """
        self._x_customer_id = x_customer_id

    @property
    def x_customer_name(self):
        """Gets the x_customer_name of this ListCasesRequest.

        子用户名称

        :return: The x_customer_name of this ListCasesRequest.
        :rtype: str
        """
        return self._x_customer_name

    @x_customer_name.setter
    def x_customer_name(self, x_customer_name):
        """Sets the x_customer_name of this ListCasesRequest.

        子用户名称

        :param x_customer_name: The x_customer_name of this ListCasesRequest.
        :type x_customer_name: str
        """
        self._x_customer_name = x_customer_name

    @property
    def group_id(self):
        """Gets the group_id of this ListCasesRequest.

        组id

        :return: The group_id of this ListCasesRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ListCasesRequest.

        组id

        :param group_id: The group_id of this ListCasesRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def offset(self):
        """Gets the offset of this ListCasesRequest.

        查询偏移量

        :return: The offset of this ListCasesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListCasesRequest.

        查询偏移量

        :param offset: The offset of this ListCasesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListCasesRequest.

        查询限制数量

        :return: The limit of this ListCasesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListCasesRequest.

        查询限制数量

        :param limit: The limit of this ListCasesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def x_site(self):
        """Gets the x_site of this ListCasesRequest.

        对接站点信息。  0（中国站） 1（国际站），不填的话默认为0。

        :return: The x_site of this ListCasesRequest.
        :rtype: int
        """
        return self._x_site

    @x_site.setter
    def x_site(self, x_site):
        """Sets the x_site of this ListCasesRequest.

        对接站点信息。  0（中国站） 1（国际站），不填的话默认为0。

        :param x_site: The x_site of this ListCasesRequest.
        :type x_site: int
        """
        self._x_site = x_site

    @property
    def x_language(self):
        """Gets the x_language of this ListCasesRequest.

        语言环境，值为通用的语言描述字符串，比如zh-cn等，默认为zh-cn。  会根据语言环境对应展示一些国际化的信息，比如工单类型名称等。

        :return: The x_language of this ListCasesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListCasesRequest.

        语言环境，值为通用的语言描述字符串，比如zh-cn等，默认为zh-cn。  会根据语言环境对应展示一些国际化的信息，比如工单类型名称等。

        :param x_language: The x_language of this ListCasesRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def x_time_zone(self):
        """Gets the x_time_zone of this ListCasesRequest.

        环境时区，值为通用的时区描述字符串，比如GMT+8等，默认为GMT+8。  涉及时间的数据会根据环境时区处理。

        :return: The x_time_zone of this ListCasesRequest.
        :rtype: str
        """
        return self._x_time_zone

    @x_time_zone.setter
    def x_time_zone(self, x_time_zone):
        """Sets the x_time_zone of this ListCasesRequest.

        环境时区，值为通用的时区描述字符串，比如GMT+8等，默认为GMT+8。  涉及时间的数据会根据环境时区处理。

        :param x_time_zone: The x_time_zone of this ListCasesRequest.
        :type x_time_zone: str
        """
        self._x_time_zone = x_time_zone

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
        if not isinstance(other, ListCasesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
