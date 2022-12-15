# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBandwidthPackage:

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
        'description': 'str',
        'enterprise_project_id': 'str',
        'local_area_id': 'str',
        'remote_area_id': 'str',
        'charge_mode': 'str',
        'billing_mode': 'int',
        'bandwidth': 'int',
        'project_id': 'str',
        'resource_id': 'str',
        'resource_type': 'str',
        'interflow_mode': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'enterprise_project_id': 'enterprise_project_id',
        'local_area_id': 'local_area_id',
        'remote_area_id': 'remote_area_id',
        'charge_mode': 'charge_mode',
        'billing_mode': 'billing_mode',
        'bandwidth': 'bandwidth',
        'project_id': 'project_id',
        'resource_id': 'resource_id',
        'resource_type': 'resource_type',
        'interflow_mode': 'interflow_mode'
    }

    def __init__(self, name=None, description=None, enterprise_project_id=None, local_area_id=None, remote_area_id=None, charge_mode=None, billing_mode=None, bandwidth=None, project_id=None, resource_id=None, resource_type=None, interflow_mode=None):
        """CreateBandwidthPackage

        The model defined in huaweicloud sdk

        :param name: 带宽包实例的名字。
        :type name: str
        :param description: 带宽包实例的描述。
        :type description: str
        :param enterprise_project_id: 带宽包实例所属的企业项目ID。
        :type enterprise_project_id: str
        :param local_area_id: 本端大区。 云连接支持的大区有： | Chinese-Mainland | 中国大陆 | | Asia-Pacific | 亚太 | | Africa | 非洲 | | Western-Latin-America | 拉美西 | | Eastern-Latin-America | 拉美东 | | Northern-Latin-America | 拉美北 |
        :type local_area_id: str
        :param remote_area_id: 远端大区。 云连接支持的大区有： | Chinese-Mainland | 中国大陆 | | Asia-Pacific | 亚太 | | Africa | 非洲 | | Western-Latin-America | 拉美西 | | Eastern-Latin-America | 拉美东 | | Northern-Latin-America | 拉美北 |
        :type remote_area_id: str
        :param charge_mode: 带宽包实例的计费方式。 bandwidth是按带宽计费。
        :type charge_mode: str
        :param billing_mode: 带宽包实例在大陆站或国际站的计费方式： - 3：大陆站按需计费 - 4：国际站按需计费 - 5：大陆站按95方式计费 - 6：国际站按95方式计费
        :type billing_mode: int
        :param bandwidth: 带宽包实例中的带宽值。
        :type bandwidth: int
        :param project_id: 项目ID。
        :type project_id: str
        :param resource_id: 带宽包实例绑定的资源ID。
        :type resource_id: str
        :param resource_type: 带宽包实例绑定的资源类型。  cloud_connection: 云连接实例。
        :type resource_type: str
        :param interflow_mode: 互通类型: - Area: 大区互通 - Region: 城域互通
        :type interflow_mode: str
        """
        
        

        self._name = None
        self._description = None
        self._enterprise_project_id = None
        self._local_area_id = None
        self._remote_area_id = None
        self._charge_mode = None
        self._billing_mode = None
        self._bandwidth = None
        self._project_id = None
        self._resource_id = None
        self._resource_type = None
        self._interflow_mode = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.local_area_id = local_area_id
        self.remote_area_id = remote_area_id
        self.charge_mode = charge_mode
        self.billing_mode = billing_mode
        self.bandwidth = bandwidth
        self.project_id = project_id
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_type is not None:
            self.resource_type = resource_type
        if interflow_mode is not None:
            self.interflow_mode = interflow_mode

    @property
    def name(self):
        """Gets the name of this CreateBandwidthPackage.

        带宽包实例的名字。

        :return: The name of this CreateBandwidthPackage.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateBandwidthPackage.

        带宽包实例的名字。

        :param name: The name of this CreateBandwidthPackage.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateBandwidthPackage.

        带宽包实例的描述。

        :return: The description of this CreateBandwidthPackage.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateBandwidthPackage.

        带宽包实例的描述。

        :param description: The description of this CreateBandwidthPackage.
        :type description: str
        """
        self._description = description

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateBandwidthPackage.

        带宽包实例所属的企业项目ID。

        :return: The enterprise_project_id of this CreateBandwidthPackage.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateBandwidthPackage.

        带宽包实例所属的企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this CreateBandwidthPackage.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def local_area_id(self):
        """Gets the local_area_id of this CreateBandwidthPackage.

        本端大区。 云连接支持的大区有： | Chinese-Mainland | 中国大陆 | | Asia-Pacific | 亚太 | | Africa | 非洲 | | Western-Latin-America | 拉美西 | | Eastern-Latin-America | 拉美东 | | Northern-Latin-America | 拉美北 |

        :return: The local_area_id of this CreateBandwidthPackage.
        :rtype: str
        """
        return self._local_area_id

    @local_area_id.setter
    def local_area_id(self, local_area_id):
        """Sets the local_area_id of this CreateBandwidthPackage.

        本端大区。 云连接支持的大区有： | Chinese-Mainland | 中国大陆 | | Asia-Pacific | 亚太 | | Africa | 非洲 | | Western-Latin-America | 拉美西 | | Eastern-Latin-America | 拉美东 | | Northern-Latin-America | 拉美北 |

        :param local_area_id: The local_area_id of this CreateBandwidthPackage.
        :type local_area_id: str
        """
        self._local_area_id = local_area_id

    @property
    def remote_area_id(self):
        """Gets the remote_area_id of this CreateBandwidthPackage.

        远端大区。 云连接支持的大区有： | Chinese-Mainland | 中国大陆 | | Asia-Pacific | 亚太 | | Africa | 非洲 | | Western-Latin-America | 拉美西 | | Eastern-Latin-America | 拉美东 | | Northern-Latin-America | 拉美北 |

        :return: The remote_area_id of this CreateBandwidthPackage.
        :rtype: str
        """
        return self._remote_area_id

    @remote_area_id.setter
    def remote_area_id(self, remote_area_id):
        """Sets the remote_area_id of this CreateBandwidthPackage.

        远端大区。 云连接支持的大区有： | Chinese-Mainland | 中国大陆 | | Asia-Pacific | 亚太 | | Africa | 非洲 | | Western-Latin-America | 拉美西 | | Eastern-Latin-America | 拉美东 | | Northern-Latin-America | 拉美北 |

        :param remote_area_id: The remote_area_id of this CreateBandwidthPackage.
        :type remote_area_id: str
        """
        self._remote_area_id = remote_area_id

    @property
    def charge_mode(self):
        """Gets the charge_mode of this CreateBandwidthPackage.

        带宽包实例的计费方式。 bandwidth是按带宽计费。

        :return: The charge_mode of this CreateBandwidthPackage.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this CreateBandwidthPackage.

        带宽包实例的计费方式。 bandwidth是按带宽计费。

        :param charge_mode: The charge_mode of this CreateBandwidthPackage.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def billing_mode(self):
        """Gets the billing_mode of this CreateBandwidthPackage.

        带宽包实例在大陆站或国际站的计费方式： - 3：大陆站按需计费 - 4：国际站按需计费 - 5：大陆站按95方式计费 - 6：国际站按95方式计费

        :return: The billing_mode of this CreateBandwidthPackage.
        :rtype: int
        """
        return self._billing_mode

    @billing_mode.setter
    def billing_mode(self, billing_mode):
        """Sets the billing_mode of this CreateBandwidthPackage.

        带宽包实例在大陆站或国际站的计费方式： - 3：大陆站按需计费 - 4：国际站按需计费 - 5：大陆站按95方式计费 - 6：国际站按95方式计费

        :param billing_mode: The billing_mode of this CreateBandwidthPackage.
        :type billing_mode: int
        """
        self._billing_mode = billing_mode

    @property
    def bandwidth(self):
        """Gets the bandwidth of this CreateBandwidthPackage.

        带宽包实例中的带宽值。

        :return: The bandwidth of this CreateBandwidthPackage.
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this CreateBandwidthPackage.

        带宽包实例中的带宽值。

        :param bandwidth: The bandwidth of this CreateBandwidthPackage.
        :type bandwidth: int
        """
        self._bandwidth = bandwidth

    @property
    def project_id(self):
        """Gets the project_id of this CreateBandwidthPackage.

        项目ID。

        :return: The project_id of this CreateBandwidthPackage.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateBandwidthPackage.

        项目ID。

        :param project_id: The project_id of this CreateBandwidthPackage.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def resource_id(self):
        """Gets the resource_id of this CreateBandwidthPackage.

        带宽包实例绑定的资源ID。

        :return: The resource_id of this CreateBandwidthPackage.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this CreateBandwidthPackage.

        带宽包实例绑定的资源ID。

        :param resource_id: The resource_id of this CreateBandwidthPackage.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_type(self):
        """Gets the resource_type of this CreateBandwidthPackage.

        带宽包实例绑定的资源类型。  cloud_connection: 云连接实例。

        :return: The resource_type of this CreateBandwidthPackage.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this CreateBandwidthPackage.

        带宽包实例绑定的资源类型。  cloud_connection: 云连接实例。

        :param resource_type: The resource_type of this CreateBandwidthPackage.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def interflow_mode(self):
        """Gets the interflow_mode of this CreateBandwidthPackage.

        互通类型: - Area: 大区互通 - Region: 城域互通

        :return: The interflow_mode of this CreateBandwidthPackage.
        :rtype: str
        """
        return self._interflow_mode

    @interflow_mode.setter
    def interflow_mode(self, interflow_mode):
        """Sets the interflow_mode of this CreateBandwidthPackage.

        互通类型: - Area: 大区互通 - Region: 城域互通

        :param interflow_mode: The interflow_mode of this CreateBandwidthPackage.
        :type interflow_mode: str
        """
        self._interflow_mode = interflow_mode

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
        if not isinstance(other, CreateBandwidthPackage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
