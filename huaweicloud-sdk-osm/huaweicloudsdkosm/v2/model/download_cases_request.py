# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadCasesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'language': 'str',
        'timezone': 'str',
        'incident_id': 'str',
        'query_start_time': 'str',
        'query_end_time': 'str',
        'x_customer_name': 'str',
        'search_key': 'str',
        'status': 'int',
        'customer_id': 'str',
        'tenant_source_id_list': 'list[str]',
        'sub_customer_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'x_site': 'int',
        'x_language': 'str',
        'x_time_zone': 'str'
    }

    attribute_map = {
        'language': 'language',
        'timezone': 'timezone',
        'incident_id': 'incident_id',
        'query_start_time': 'query_start_time',
        'query_end_time': 'query_end_time',
        'x_customer_name': 'x_customer_name',
        'search_key': 'search_key',
        'status': 'status',
        'customer_id': 'customer_id',
        'tenant_source_id_list': 'tenant_source_id_list',
        'sub_customer_id': 'sub_customer_id',
        'offset': 'offset',
        'limit': 'limit',
        'x_site': 'X-Site',
        'x_language': 'X-Language',
        'x_time_zone': 'X-Time-Zone'
    }

    def __init__(self, language=None, timezone=None, incident_id=None, query_start_time=None, query_end_time=None, x_customer_name=None, search_key=None, status=None, customer_id=None, tenant_source_id_list=None, sub_customer_id=None, offset=None, limit=None, x_site=None, x_language=None, x_time_zone=None):
        """DownloadCasesRequest

        The model defined in huaweicloud sdk

        :param language: 语言
        :type language: str
        :param timezone: 时区
        :type timezone: str
        :param incident_id: 工单id
        :type incident_id: str
        :param query_start_time: 查询开始时间
        :type query_start_time: str
        :param query_end_time: 查询结束时间
        :type query_end_time: str
        :param x_customer_name: 子用户名称
        :type x_customer_name: str
        :param search_key: 搜索关键字
        :type search_key: str
        :param status: 状态 0：待受理 1：处理中 2：待确认结果 3：已完成 4：已撤销 12：无效 17： 待反馈
        :type status: int
        :param customer_id: 用户id
        :type customer_id: str
        :param tenant_source_id_list: 来源id
        :type tenant_source_id_list: list[str]
        :param sub_customer_id: 子用户id
        :type sub_customer_id: str
        :param offset: 查询偏移量
        :type offset: int
        :param limit: 查询数量
        :type limit: int
        :param x_site: 对接站点信息。  0（中国站） 1（国际站），不填的话默认为0。
        :type x_site: int
        :param x_language: 语言环境，值为通用的语言描述字符串，比如zh-cn等，默认为zh-cn。  会根据语言环境对应展示一些国际化的信息，比如工单类型名称等。
        :type x_language: str
        :param x_time_zone: 环境时区，值为通用的时区描述字符串，比如GMT+8等，默认为GMT+8。  涉及时间的数据会根据环境时区处理。
        :type x_time_zone: str
        """
        
        

        self._language = None
        self._timezone = None
        self._incident_id = None
        self._query_start_time = None
        self._query_end_time = None
        self._x_customer_name = None
        self._search_key = None
        self._status = None
        self._customer_id = None
        self._tenant_source_id_list = None
        self._sub_customer_id = None
        self._offset = None
        self._limit = None
        self._x_site = None
        self._x_language = None
        self._x_time_zone = None
        self.discriminator = None

        self.language = language
        self.timezone = timezone
        if incident_id is not None:
            self.incident_id = incident_id
        if query_start_time is not None:
            self.query_start_time = query_start_time
        if query_end_time is not None:
            self.query_end_time = query_end_time
        if x_customer_name is not None:
            self.x_customer_name = x_customer_name
        if search_key is not None:
            self.search_key = search_key
        if status is not None:
            self.status = status
        if customer_id is not None:
            self.customer_id = customer_id
        if tenant_source_id_list is not None:
            self.tenant_source_id_list = tenant_source_id_list
        if sub_customer_id is not None:
            self.sub_customer_id = sub_customer_id
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
    def language(self):
        """Gets the language of this DownloadCasesRequest.

        语言

        :return: The language of this DownloadCasesRequest.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this DownloadCasesRequest.

        语言

        :param language: The language of this DownloadCasesRequest.
        :type language: str
        """
        self._language = language

    @property
    def timezone(self):
        """Gets the timezone of this DownloadCasesRequest.

        时区

        :return: The timezone of this DownloadCasesRequest.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this DownloadCasesRequest.

        时区

        :param timezone: The timezone of this DownloadCasesRequest.
        :type timezone: str
        """
        self._timezone = timezone

    @property
    def incident_id(self):
        """Gets the incident_id of this DownloadCasesRequest.

        工单id

        :return: The incident_id of this DownloadCasesRequest.
        :rtype: str
        """
        return self._incident_id

    @incident_id.setter
    def incident_id(self, incident_id):
        """Sets the incident_id of this DownloadCasesRequest.

        工单id

        :param incident_id: The incident_id of this DownloadCasesRequest.
        :type incident_id: str
        """
        self._incident_id = incident_id

    @property
    def query_start_time(self):
        """Gets the query_start_time of this DownloadCasesRequest.

        查询开始时间

        :return: The query_start_time of this DownloadCasesRequest.
        :rtype: str
        """
        return self._query_start_time

    @query_start_time.setter
    def query_start_time(self, query_start_time):
        """Sets the query_start_time of this DownloadCasesRequest.

        查询开始时间

        :param query_start_time: The query_start_time of this DownloadCasesRequest.
        :type query_start_time: str
        """
        self._query_start_time = query_start_time

    @property
    def query_end_time(self):
        """Gets the query_end_time of this DownloadCasesRequest.

        查询结束时间

        :return: The query_end_time of this DownloadCasesRequest.
        :rtype: str
        """
        return self._query_end_time

    @query_end_time.setter
    def query_end_time(self, query_end_time):
        """Sets the query_end_time of this DownloadCasesRequest.

        查询结束时间

        :param query_end_time: The query_end_time of this DownloadCasesRequest.
        :type query_end_time: str
        """
        self._query_end_time = query_end_time

    @property
    def x_customer_name(self):
        """Gets the x_customer_name of this DownloadCasesRequest.

        子用户名称

        :return: The x_customer_name of this DownloadCasesRequest.
        :rtype: str
        """
        return self._x_customer_name

    @x_customer_name.setter
    def x_customer_name(self, x_customer_name):
        """Sets the x_customer_name of this DownloadCasesRequest.

        子用户名称

        :param x_customer_name: The x_customer_name of this DownloadCasesRequest.
        :type x_customer_name: str
        """
        self._x_customer_name = x_customer_name

    @property
    def search_key(self):
        """Gets the search_key of this DownloadCasesRequest.

        搜索关键字

        :return: The search_key of this DownloadCasesRequest.
        :rtype: str
        """
        return self._search_key

    @search_key.setter
    def search_key(self, search_key):
        """Sets the search_key of this DownloadCasesRequest.

        搜索关键字

        :param search_key: The search_key of this DownloadCasesRequest.
        :type search_key: str
        """
        self._search_key = search_key

    @property
    def status(self):
        """Gets the status of this DownloadCasesRequest.

        状态 0：待受理 1：处理中 2：待确认结果 3：已完成 4：已撤销 12：无效 17： 待反馈

        :return: The status of this DownloadCasesRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DownloadCasesRequest.

        状态 0：待受理 1：处理中 2：待确认结果 3：已完成 4：已撤销 12：无效 17： 待反馈

        :param status: The status of this DownloadCasesRequest.
        :type status: int
        """
        self._status = status

    @property
    def customer_id(self):
        """Gets the customer_id of this DownloadCasesRequest.

        用户id

        :return: The customer_id of this DownloadCasesRequest.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this DownloadCasesRequest.

        用户id

        :param customer_id: The customer_id of this DownloadCasesRequest.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def tenant_source_id_list(self):
        """Gets the tenant_source_id_list of this DownloadCasesRequest.

        来源id

        :return: The tenant_source_id_list of this DownloadCasesRequest.
        :rtype: list[str]
        """
        return self._tenant_source_id_list

    @tenant_source_id_list.setter
    def tenant_source_id_list(self, tenant_source_id_list):
        """Sets the tenant_source_id_list of this DownloadCasesRequest.

        来源id

        :param tenant_source_id_list: The tenant_source_id_list of this DownloadCasesRequest.
        :type tenant_source_id_list: list[str]
        """
        self._tenant_source_id_list = tenant_source_id_list

    @property
    def sub_customer_id(self):
        """Gets the sub_customer_id of this DownloadCasesRequest.

        子用户id

        :return: The sub_customer_id of this DownloadCasesRequest.
        :rtype: str
        """
        return self._sub_customer_id

    @sub_customer_id.setter
    def sub_customer_id(self, sub_customer_id):
        """Sets the sub_customer_id of this DownloadCasesRequest.

        子用户id

        :param sub_customer_id: The sub_customer_id of this DownloadCasesRequest.
        :type sub_customer_id: str
        """
        self._sub_customer_id = sub_customer_id

    @property
    def offset(self):
        """Gets the offset of this DownloadCasesRequest.

        查询偏移量

        :return: The offset of this DownloadCasesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this DownloadCasesRequest.

        查询偏移量

        :param offset: The offset of this DownloadCasesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this DownloadCasesRequest.

        查询数量

        :return: The limit of this DownloadCasesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this DownloadCasesRequest.

        查询数量

        :param limit: The limit of this DownloadCasesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def x_site(self):
        """Gets the x_site of this DownloadCasesRequest.

        对接站点信息。  0（中国站） 1（国际站），不填的话默认为0。

        :return: The x_site of this DownloadCasesRequest.
        :rtype: int
        """
        return self._x_site

    @x_site.setter
    def x_site(self, x_site):
        """Sets the x_site of this DownloadCasesRequest.

        对接站点信息。  0（中国站） 1（国际站），不填的话默认为0。

        :param x_site: The x_site of this DownloadCasesRequest.
        :type x_site: int
        """
        self._x_site = x_site

    @property
    def x_language(self):
        """Gets the x_language of this DownloadCasesRequest.

        语言环境，值为通用的语言描述字符串，比如zh-cn等，默认为zh-cn。  会根据语言环境对应展示一些国际化的信息，比如工单类型名称等。

        :return: The x_language of this DownloadCasesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this DownloadCasesRequest.

        语言环境，值为通用的语言描述字符串，比如zh-cn等，默认为zh-cn。  会根据语言环境对应展示一些国际化的信息，比如工单类型名称等。

        :param x_language: The x_language of this DownloadCasesRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def x_time_zone(self):
        """Gets the x_time_zone of this DownloadCasesRequest.

        环境时区，值为通用的时区描述字符串，比如GMT+8等，默认为GMT+8。  涉及时间的数据会根据环境时区处理。

        :return: The x_time_zone of this DownloadCasesRequest.
        :rtype: str
        """
        return self._x_time_zone

    @x_time_zone.setter
    def x_time_zone(self, x_time_zone):
        """Sets the x_time_zone of this DownloadCasesRequest.

        环境时区，值为通用的时区描述字符串，比如GMT+8等，默认为GMT+8。  涉及时间的数据会根据环境时区处理。

        :param x_time_zone: The x_time_zone of this DownloadCasesRequest.
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
        if not isinstance(other, DownloadCasesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
