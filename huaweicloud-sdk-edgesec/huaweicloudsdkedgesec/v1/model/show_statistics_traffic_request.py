# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStatisticsTrafficRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'int',
        'end_time': 'int',
        'type': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'type': 'type',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, start_time=None, end_time=None, type=None, enterprise_project_id=None):
        """ShowStatisticsTrafficRequest

        The model defined in huaweicloud sdk

        :param start_time: 开始时间（13位时间戳），需要和end_time同时使用
        :type start_time: int
        :param end_time: 结束时间（13位时间戳），需要和start_time同时使用
        :type end_time: int
        :param type: 类型：  - max_flow_bandwidth——DDos入流量带宽峰值   - max_drop_bandwidth——DDos入流量带宽峰值   - ddos_flow——DDos入流量   - flow_drop_traffic——入流量与清洗流量   - attack_traffic——不同类型攻击流量
        :type type: str
        :param enterprise_project_id: 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id
        :type enterprise_project_id: str
        """
        
        

        self._start_time = None
        self._end_time = None
        self._type = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        self.type = type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def start_time(self):
        """Gets the start_time of this ShowStatisticsTrafficRequest.

        开始时间（13位时间戳），需要和end_time同时使用

        :return: The start_time of this ShowStatisticsTrafficRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowStatisticsTrafficRequest.

        开始时间（13位时间戳），需要和end_time同时使用

        :param start_time: The start_time of this ShowStatisticsTrafficRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowStatisticsTrafficRequest.

        结束时间（13位时间戳），需要和start_time同时使用

        :return: The end_time of this ShowStatisticsTrafficRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowStatisticsTrafficRequest.

        结束时间（13位时间戳），需要和start_time同时使用

        :param end_time: The end_time of this ShowStatisticsTrafficRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def type(self):
        """Gets the type of this ShowStatisticsTrafficRequest.

        类型：  - max_flow_bandwidth——DDos入流量带宽峰值   - max_drop_bandwidth——DDos入流量带宽峰值   - ddos_flow——DDos入流量   - flow_drop_traffic——入流量与清洗流量   - attack_traffic——不同类型攻击流量

        :return: The type of this ShowStatisticsTrafficRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowStatisticsTrafficRequest.

        类型：  - max_flow_bandwidth——DDos入流量带宽峰值   - max_drop_bandwidth——DDos入流量带宽峰值   - ddos_flow——DDos入流量   - flow_drop_traffic——入流量与清洗流量   - attack_traffic——不同类型攻击流量

        :param type: The type of this ShowStatisticsTrafficRequest.
        :type type: str
        """
        self._type = type

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowStatisticsTrafficRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :return: The enterprise_project_id of this ShowStatisticsTrafficRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowStatisticsTrafficRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ShowStatisticsTrafficRequest.
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
        if not isinstance(other, ShowStatisticsTrafficRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
