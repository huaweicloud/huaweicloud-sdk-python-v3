# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CountPreoccupyIpNumRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'l7_flavor_id': 'str',
        'ip_target_enable': 'bool',
        'ip_version': 'int',
        'loadbalancer_id': 'str',
        'availability_zone_id': 'list[str]'
    }

    attribute_map = {
        'l7_flavor_id': 'l7_flavor_id',
        'ip_target_enable': 'ip_target_enable',
        'ip_version': 'ip_version',
        'loadbalancer_id': 'loadbalancer_id',
        'availability_zone_id': 'availability_zone_id'
    }

    def __init__(self, l7_flavor_id=None, ip_target_enable=None, ip_version=None, loadbalancer_id=None, availability_zone_id=None):
        """CountPreoccupyIpNumRequest

        The model defined in huaweicloud sdk

        :param l7_flavor_id: 负载均衡器七层规格的ID。传入该字段表示计算创建该规格的LB，或变更LB的原七层规格到该规格所需要的预占IP。  适用场景：创建负LB，变更LB规格。
        :type l7_flavor_id: str
        :param ip_target_enable: 是否开启跨VPC转发。  取值true表示计算创建或变更为开启跨VPC转发的LB的预占IP。  取值false表示计算创建或变更为不开启跨VPC转发的LB的预占IP。不传等价false。  适用场景：创建LB，变更LB规格。
        :type ip_target_enable: bool
        :param ip_version: 负载均衡器IP地址类型，取值4，6 。  取值4表示计算创建支持IPv4地址的LB的预占IP。  取值6表示计算创建支持IPv6地址的LB的预占IP。  适用场景：创建LB。  [不支持IPv6，请勿设置为6。](tag:dt,dt_test)
        :type ip_version: int
        :param loadbalancer_id: 负载均衡器ID。计算LB规格变更或创建LB中的第一个七层监听器的预占IP。  适用场景：变更LB规格，创建LB中的第一个七层监听器。
        :type loadbalancer_id: str
        :param availability_zone_id: 计算创建AZ列表为availability_zone_id的负载局衡器实例的预占IP。  适用场景：创建LB。  使用说明：传入loadbalancer_id时，该参数无效。
        :type availability_zone_id: list[str]
        """
        
        

        self._l7_flavor_id = None
        self._ip_target_enable = None
        self._ip_version = None
        self._loadbalancer_id = None
        self._availability_zone_id = None
        self.discriminator = None

        if l7_flavor_id is not None:
            self.l7_flavor_id = l7_flavor_id
        if ip_target_enable is not None:
            self.ip_target_enable = ip_target_enable
        if ip_version is not None:
            self.ip_version = ip_version
        if loadbalancer_id is not None:
            self.loadbalancer_id = loadbalancer_id
        if availability_zone_id is not None:
            self.availability_zone_id = availability_zone_id

    @property
    def l7_flavor_id(self):
        """Gets the l7_flavor_id of this CountPreoccupyIpNumRequest.

        负载均衡器七层规格的ID。传入该字段表示计算创建该规格的LB，或变更LB的原七层规格到该规格所需要的预占IP。  适用场景：创建负LB，变更LB规格。

        :return: The l7_flavor_id of this CountPreoccupyIpNumRequest.
        :rtype: str
        """
        return self._l7_flavor_id

    @l7_flavor_id.setter
    def l7_flavor_id(self, l7_flavor_id):
        """Sets the l7_flavor_id of this CountPreoccupyIpNumRequest.

        负载均衡器七层规格的ID。传入该字段表示计算创建该规格的LB，或变更LB的原七层规格到该规格所需要的预占IP。  适用场景：创建负LB，变更LB规格。

        :param l7_flavor_id: The l7_flavor_id of this CountPreoccupyIpNumRequest.
        :type l7_flavor_id: str
        """
        self._l7_flavor_id = l7_flavor_id

    @property
    def ip_target_enable(self):
        """Gets the ip_target_enable of this CountPreoccupyIpNumRequest.

        是否开启跨VPC转发。  取值true表示计算创建或变更为开启跨VPC转发的LB的预占IP。  取值false表示计算创建或变更为不开启跨VPC转发的LB的预占IP。不传等价false。  适用场景：创建LB，变更LB规格。

        :return: The ip_target_enable of this CountPreoccupyIpNumRequest.
        :rtype: bool
        """
        return self._ip_target_enable

    @ip_target_enable.setter
    def ip_target_enable(self, ip_target_enable):
        """Sets the ip_target_enable of this CountPreoccupyIpNumRequest.

        是否开启跨VPC转发。  取值true表示计算创建或变更为开启跨VPC转发的LB的预占IP。  取值false表示计算创建或变更为不开启跨VPC转发的LB的预占IP。不传等价false。  适用场景：创建LB，变更LB规格。

        :param ip_target_enable: The ip_target_enable of this CountPreoccupyIpNumRequest.
        :type ip_target_enable: bool
        """
        self._ip_target_enable = ip_target_enable

    @property
    def ip_version(self):
        """Gets the ip_version of this CountPreoccupyIpNumRequest.

        负载均衡器IP地址类型，取值4，6 。  取值4表示计算创建支持IPv4地址的LB的预占IP。  取值6表示计算创建支持IPv6地址的LB的预占IP。  适用场景：创建LB。  [不支持IPv6，请勿设置为6。](tag:dt,dt_test)

        :return: The ip_version of this CountPreoccupyIpNumRequest.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this CountPreoccupyIpNumRequest.

        负载均衡器IP地址类型，取值4，6 。  取值4表示计算创建支持IPv4地址的LB的预占IP。  取值6表示计算创建支持IPv6地址的LB的预占IP。  适用场景：创建LB。  [不支持IPv6，请勿设置为6。](tag:dt,dt_test)

        :param ip_version: The ip_version of this CountPreoccupyIpNumRequest.
        :type ip_version: int
        """
        self._ip_version = ip_version

    @property
    def loadbalancer_id(self):
        """Gets the loadbalancer_id of this CountPreoccupyIpNumRequest.

        负载均衡器ID。计算LB规格变更或创建LB中的第一个七层监听器的预占IP。  适用场景：变更LB规格，创建LB中的第一个七层监听器。

        :return: The loadbalancer_id of this CountPreoccupyIpNumRequest.
        :rtype: str
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        """Sets the loadbalancer_id of this CountPreoccupyIpNumRequest.

        负载均衡器ID。计算LB规格变更或创建LB中的第一个七层监听器的预占IP。  适用场景：变更LB规格，创建LB中的第一个七层监听器。

        :param loadbalancer_id: The loadbalancer_id of this CountPreoccupyIpNumRequest.
        :type loadbalancer_id: str
        """
        self._loadbalancer_id = loadbalancer_id

    @property
    def availability_zone_id(self):
        """Gets the availability_zone_id of this CountPreoccupyIpNumRequest.

        计算创建AZ列表为availability_zone_id的负载局衡器实例的预占IP。  适用场景：创建LB。  使用说明：传入loadbalancer_id时，该参数无效。

        :return: The availability_zone_id of this CountPreoccupyIpNumRequest.
        :rtype: list[str]
        """
        return self._availability_zone_id

    @availability_zone_id.setter
    def availability_zone_id(self, availability_zone_id):
        """Sets the availability_zone_id of this CountPreoccupyIpNumRequest.

        计算创建AZ列表为availability_zone_id的负载局衡器实例的预占IP。  适用场景：创建LB。  使用说明：传入loadbalancer_id时，该参数无效。

        :param availability_zone_id: The availability_zone_id of this CountPreoccupyIpNumRequest.
        :type availability_zone_id: list[str]
        """
        self._availability_zone_id = availability_zone_id

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
        if not isinstance(other, CountPreoccupyIpNumRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
