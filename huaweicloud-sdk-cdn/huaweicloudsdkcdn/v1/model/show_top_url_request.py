# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTopUrlRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'domain_name': 'str',
        'service_area': 'str',
        'stat_type': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'domain_name': 'domain_name',
        'service_area': 'service_area',
        'stat_type': 'stat_type'
    }

    def __init__(self, enterprise_project_id=None, start_time=None, end_time=None, domain_name=None, service_area=None, stat_type=None):
        """ShowTopUrlRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\&quot;all\&quot;表示所有项目。注意：当使用子账号调用接口时，该参数必传。
        :type enterprise_project_id: str
        :param start_time: 查询起始时间戳（单位：毫秒）。该时间戳的取值在转化为日期格式后须满足以下格式：XXXX-XX-XX 00:00:00
        :type start_time: int
        :param end_time: 查询结束时间戳（单位：毫秒）。该时间戳的取值在转化为日期格式后须满足以下格式：XXXX-XX-XX 00:00:00
        :type end_time: int
        :param domain_name: 域名列表，多个域名以逗号（半角）分隔，如：www.test1.com,www.test2.com ，ALL表示查询名下全部域名。
        :type domain_name: str
        :param service_area: mainland_china(中国大陆)，outside_mainland_china(中国大陆境外)，默认为mainland_china。
        :type service_area: str
        :param stat_type: 参数类型支持：flux(流量),req_num(请求总数)。
        :type stat_type: str
        """
        
        

        self._enterprise_project_id = None
        self._start_time = None
        self._end_time = None
        self._domain_name = None
        self._service_area = None
        self._stat_type = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.start_time = start_time
        self.end_time = end_time
        self.domain_name = domain_name
        if service_area is not None:
            self.service_area = service_area
        self.stat_type = stat_type

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowTopUrlRequest.

        当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\"all\"表示所有项目。注意：当使用子账号调用接口时，该参数必传。

        :return: The enterprise_project_id of this ShowTopUrlRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowTopUrlRequest.

        当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\"all\"表示所有项目。注意：当使用子账号调用接口时，该参数必传。

        :param enterprise_project_id: The enterprise_project_id of this ShowTopUrlRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def start_time(self):
        """Gets the start_time of this ShowTopUrlRequest.

        查询起始时间戳（单位：毫秒）。该时间戳的取值在转化为日期格式后须满足以下格式：XXXX-XX-XX 00:00:00

        :return: The start_time of this ShowTopUrlRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowTopUrlRequest.

        查询起始时间戳（单位：毫秒）。该时间戳的取值在转化为日期格式后须满足以下格式：XXXX-XX-XX 00:00:00

        :param start_time: The start_time of this ShowTopUrlRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowTopUrlRequest.

        查询结束时间戳（单位：毫秒）。该时间戳的取值在转化为日期格式后须满足以下格式：XXXX-XX-XX 00:00:00

        :return: The end_time of this ShowTopUrlRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowTopUrlRequest.

        查询结束时间戳（单位：毫秒）。该时间戳的取值在转化为日期格式后须满足以下格式：XXXX-XX-XX 00:00:00

        :param end_time: The end_time of this ShowTopUrlRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def domain_name(self):
        """Gets the domain_name of this ShowTopUrlRequest.

        域名列表，多个域名以逗号（半角）分隔，如：www.test1.com,www.test2.com ，ALL表示查询名下全部域名。

        :return: The domain_name of this ShowTopUrlRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this ShowTopUrlRequest.

        域名列表，多个域名以逗号（半角）分隔，如：www.test1.com,www.test2.com ，ALL表示查询名下全部域名。

        :param domain_name: The domain_name of this ShowTopUrlRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def service_area(self):
        """Gets the service_area of this ShowTopUrlRequest.

        mainland_china(中国大陆)，outside_mainland_china(中国大陆境外)，默认为mainland_china。

        :return: The service_area of this ShowTopUrlRequest.
        :rtype: str
        """
        return self._service_area

    @service_area.setter
    def service_area(self, service_area):
        """Sets the service_area of this ShowTopUrlRequest.

        mainland_china(中国大陆)，outside_mainland_china(中国大陆境外)，默认为mainland_china。

        :param service_area: The service_area of this ShowTopUrlRequest.
        :type service_area: str
        """
        self._service_area = service_area

    @property
    def stat_type(self):
        """Gets the stat_type of this ShowTopUrlRequest.

        参数类型支持：flux(流量),req_num(请求总数)。

        :return: The stat_type of this ShowTopUrlRequest.
        :rtype: str
        """
        return self._stat_type

    @stat_type.setter
    def stat_type(self, stat_type):
        """Sets the stat_type of this ShowTopUrlRequest.

        参数类型支持：flux(流量),req_num(请求总数)。

        :param stat_type: The stat_type of this ShowTopUrlRequest.
        :type stat_type: str
        """
        self._stat_type = stat_type

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
        if not isinstance(other, ShowTopUrlRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
