# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLogsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_name': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'page_size': 'int',
        'page_number': 'int',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'page_size': 'page_size',
        'page_number': 'page_number',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, domain_name=None, start_time=None, end_time=None, page_size=None, page_number=None, enterprise_project_id=None):
        """ShowLogsRequest

        The model defined in huaweicloud sdk

        :param domain_name: 只支持单个域名，如：www.test1.com。
        :type domain_name: str
        :param start_time: 查询开始时间，时间格式为整点毫秒时间戳，此参数传空值时默认为当天0点。
        :type start_time: int
        :param end_time: 查询结束时间（不包含结束时间），时间格式为整点毫秒时间戳，与开始时间的最大跨度为30天，此参数传空值时默认为开始时间加1天。
        :type end_time: int
        :param page_size: 单页最大数量，取值范围为1-10000，默认值：10。
        :type page_size: int
        :param page_number: 当前查询第几页，取值范围为1-65535，默认值：1。
        :type page_number: int
        :param enterprise_project_id: 当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\&quot;all\&quot;表示所有项目。注意：当使用子帐号调用接口时，该参数必传。  您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。
        :type enterprise_project_id: str
        """
        
        

        self._domain_name = None
        self._start_time = None
        self._end_time = None
        self._page_size = None
        self._page_number = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.domain_name = domain_name
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if page_size is not None:
            self.page_size = page_size
        if page_number is not None:
            self.page_number = page_number
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def domain_name(self):
        """Gets the domain_name of this ShowLogsRequest.

        只支持单个域名，如：www.test1.com。

        :return: The domain_name of this ShowLogsRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this ShowLogsRequest.

        只支持单个域名，如：www.test1.com。

        :param domain_name: The domain_name of this ShowLogsRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def start_time(self):
        """Gets the start_time of this ShowLogsRequest.

        查询开始时间，时间格式为整点毫秒时间戳，此参数传空值时默认为当天0点。

        :return: The start_time of this ShowLogsRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowLogsRequest.

        查询开始时间，时间格式为整点毫秒时间戳，此参数传空值时默认为当天0点。

        :param start_time: The start_time of this ShowLogsRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowLogsRequest.

        查询结束时间（不包含结束时间），时间格式为整点毫秒时间戳，与开始时间的最大跨度为30天，此参数传空值时默认为开始时间加1天。

        :return: The end_time of this ShowLogsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowLogsRequest.

        查询结束时间（不包含结束时间），时间格式为整点毫秒时间戳，与开始时间的最大跨度为30天，此参数传空值时默认为开始时间加1天。

        :param end_time: The end_time of this ShowLogsRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def page_size(self):
        """Gets the page_size of this ShowLogsRequest.

        单页最大数量，取值范围为1-10000，默认值：10。

        :return: The page_size of this ShowLogsRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ShowLogsRequest.

        单页最大数量，取值范围为1-10000，默认值：10。

        :param page_size: The page_size of this ShowLogsRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def page_number(self):
        """Gets the page_number of this ShowLogsRequest.

        当前查询第几页，取值范围为1-65535，默认值：1。

        :return: The page_number of this ShowLogsRequest.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this ShowLogsRequest.

        当前查询第几页，取值范围为1-65535，默认值：1。

        :param page_number: The page_number of this ShowLogsRequest.
        :type page_number: int
        """
        self._page_number = page_number

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowLogsRequest.

        当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\"all\"表示所有项目。注意：当使用子帐号调用接口时，该参数必传。  您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。

        :return: The enterprise_project_id of this ShowLogsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowLogsRequest.

        当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\"all\"表示所有项目。注意：当使用子帐号调用接口时，该参数必传。  您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。

        :param enterprise_project_id: The enterprise_project_id of this ShowLogsRequest.
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
        if not isinstance(other, ShowLogsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
