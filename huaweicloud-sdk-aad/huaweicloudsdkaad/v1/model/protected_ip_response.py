# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProtectedIpResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'ip': 'str',
        'type': 'str',
        'name': 'str',
        'status': 'int',
        'status_detail': 'IpStatusDetail',
        'policy_name': 'str',
        'region': 'str',
        'package_id': 'str',
        'package_name': 'str',
        'tags': 'str',
        'tag': 'str',
        'is_resale': 'bool',
        'package_version': 'str'
    }

    attribute_map = {
        'id': 'id',
        'ip': 'ip',
        'type': 'type',
        'name': 'name',
        'status': 'status',
        'status_detail': 'status_detail',
        'policy_name': 'policy_name',
        'region': 'region',
        'package_id': 'package_id',
        'package_name': 'package_name',
        'tags': 'tags',
        'tag': 'tag',
        'is_resale': 'is_resale',
        'package_version': 'package_version'
    }

    def __init__(self, id=None, ip=None, type=None, name=None, status=None, status_detail=None, policy_name=None, region=None, package_id=None, package_name=None, tags=None, tag=None, is_resale=None, package_version=None):
        """ProtectedIpResponse

        The model defined in huaweicloud sdk

        :param id: 防护IP的Id
        :type id: str
        :param ip: 防护IP
        :type ip: str
        :param type: 类型。VPN：VPN；NAT：NAT；VIP：VIP；CCI：CCI；EIP：弹性公网IP；ELB：弹性负载均衡；REROUTING_IP：REROUTING_IP；SubEni：SubEni；NetInterFace：NetInterFace；
        :type type: str
        :param name: 名字
        :type name: str
        :param status: 状态：0 - 正常， 1 - 清洗中， 2 - 黑洞中
        :type status: int
        :param status_detail: 
        :type status_detail: :class:`huaweicloudsdkaad.v1.IpStatusDetail`
        :param policy_name: 策略名
        :type policy_name: str
        :param region: 所属region
        :type region: str
        :param package_id: 防护包id
        :type package_id: str
        :param package_name: 防护包名
        :type package_name: str
        :param tags: TMS标签
        :type tags: str
        :param tag: 本地标签
        :type tag: str
        :param is_resale: 默认false，表示是否转售版的IP，不需要展示策略和报表
        :type is_resale: bool
        :param package_version: package_version。cnad_pro：专业版；cnad_ip：标准版；cnad_ep：铂金版；cnad_full_high：全力防高级版；cnad_vic：按需版；cnad_intl_ep：国际站铂金版
        :type package_version: str
        """
        
        

        self._id = None
        self._ip = None
        self._type = None
        self._name = None
        self._status = None
        self._status_detail = None
        self._policy_name = None
        self._region = None
        self._package_id = None
        self._package_name = None
        self._tags = None
        self._tag = None
        self._is_resale = None
        self._package_version = None
        self.discriminator = None

        self.id = id
        self.ip = ip
        self.type = type
        if name is not None:
            self.name = name
        self.status = status
        if status_detail is not None:
            self.status_detail = status_detail
        self.policy_name = policy_name
        self.region = region
        self.package_id = package_id
        self.package_name = package_name
        if tags is not None:
            self.tags = tags
        if tag is not None:
            self.tag = tag
        self.is_resale = is_resale
        self.package_version = package_version

    @property
    def id(self):
        """Gets the id of this ProtectedIpResponse.

        防护IP的Id

        :return: The id of this ProtectedIpResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProtectedIpResponse.

        防护IP的Id

        :param id: The id of this ProtectedIpResponse.
        :type id: str
        """
        self._id = id

    @property
    def ip(self):
        """Gets the ip of this ProtectedIpResponse.

        防护IP

        :return: The ip of this ProtectedIpResponse.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this ProtectedIpResponse.

        防护IP

        :param ip: The ip of this ProtectedIpResponse.
        :type ip: str
        """
        self._ip = ip

    @property
    def type(self):
        """Gets the type of this ProtectedIpResponse.

        类型。VPN：VPN；NAT：NAT；VIP：VIP；CCI：CCI；EIP：弹性公网IP；ELB：弹性负载均衡；REROUTING_IP：REROUTING_IP；SubEni：SubEni；NetInterFace：NetInterFace；

        :return: The type of this ProtectedIpResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProtectedIpResponse.

        类型。VPN：VPN；NAT：NAT；VIP：VIP；CCI：CCI；EIP：弹性公网IP；ELB：弹性负载均衡；REROUTING_IP：REROUTING_IP；SubEni：SubEni；NetInterFace：NetInterFace；

        :param type: The type of this ProtectedIpResponse.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        """Gets the name of this ProtectedIpResponse.

        名字

        :return: The name of this ProtectedIpResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProtectedIpResponse.

        名字

        :param name: The name of this ProtectedIpResponse.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this ProtectedIpResponse.

        状态：0 - 正常， 1 - 清洗中， 2 - 黑洞中

        :return: The status of this ProtectedIpResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ProtectedIpResponse.

        状态：0 - 正常， 1 - 清洗中， 2 - 黑洞中

        :param status: The status of this ProtectedIpResponse.
        :type status: int
        """
        self._status = status

    @property
    def status_detail(self):
        """Gets the status_detail of this ProtectedIpResponse.

        :return: The status_detail of this ProtectedIpResponse.
        :rtype: :class:`huaweicloudsdkaad.v1.IpStatusDetail`
        """
        return self._status_detail

    @status_detail.setter
    def status_detail(self, status_detail):
        """Sets the status_detail of this ProtectedIpResponse.

        :param status_detail: The status_detail of this ProtectedIpResponse.
        :type status_detail: :class:`huaweicloudsdkaad.v1.IpStatusDetail`
        """
        self._status_detail = status_detail

    @property
    def policy_name(self):
        """Gets the policy_name of this ProtectedIpResponse.

        策略名

        :return: The policy_name of this ProtectedIpResponse.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this ProtectedIpResponse.

        策略名

        :param policy_name: The policy_name of this ProtectedIpResponse.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def region(self):
        """Gets the region of this ProtectedIpResponse.

        所属region

        :return: The region of this ProtectedIpResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ProtectedIpResponse.

        所属region

        :param region: The region of this ProtectedIpResponse.
        :type region: str
        """
        self._region = region

    @property
    def package_id(self):
        """Gets the package_id of this ProtectedIpResponse.

        防护包id

        :return: The package_id of this ProtectedIpResponse.
        :rtype: str
        """
        return self._package_id

    @package_id.setter
    def package_id(self, package_id):
        """Sets the package_id of this ProtectedIpResponse.

        防护包id

        :param package_id: The package_id of this ProtectedIpResponse.
        :type package_id: str
        """
        self._package_id = package_id

    @property
    def package_name(self):
        """Gets the package_name of this ProtectedIpResponse.

        防护包名

        :return: The package_name of this ProtectedIpResponse.
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        """Sets the package_name of this ProtectedIpResponse.

        防护包名

        :param package_name: The package_name of this ProtectedIpResponse.
        :type package_name: str
        """
        self._package_name = package_name

    @property
    def tags(self):
        """Gets the tags of this ProtectedIpResponse.

        TMS标签

        :return: The tags of this ProtectedIpResponse.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ProtectedIpResponse.

        TMS标签

        :param tags: The tags of this ProtectedIpResponse.
        :type tags: str
        """
        self._tags = tags

    @property
    def tag(self):
        """Gets the tag of this ProtectedIpResponse.

        本地标签

        :return: The tag of this ProtectedIpResponse.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ProtectedIpResponse.

        本地标签

        :param tag: The tag of this ProtectedIpResponse.
        :type tag: str
        """
        self._tag = tag

    @property
    def is_resale(self):
        """Gets the is_resale of this ProtectedIpResponse.

        默认false，表示是否转售版的IP，不需要展示策略和报表

        :return: The is_resale of this ProtectedIpResponse.
        :rtype: bool
        """
        return self._is_resale

    @is_resale.setter
    def is_resale(self, is_resale):
        """Sets the is_resale of this ProtectedIpResponse.

        默认false，表示是否转售版的IP，不需要展示策略和报表

        :param is_resale: The is_resale of this ProtectedIpResponse.
        :type is_resale: bool
        """
        self._is_resale = is_resale

    @property
    def package_version(self):
        """Gets the package_version of this ProtectedIpResponse.

        package_version。cnad_pro：专业版；cnad_ip：标准版；cnad_ep：铂金版；cnad_full_high：全力防高级版；cnad_vic：按需版；cnad_intl_ep：国际站铂金版

        :return: The package_version of this ProtectedIpResponse.
        :rtype: str
        """
        return self._package_version

    @package_version.setter
    def package_version(self, package_version):
        """Sets the package_version of this ProtectedIpResponse.

        package_version。cnad_pro：专业版；cnad_ip：标准版；cnad_ep：铂金版；cnad_full_high：全力防高级版；cnad_vic：按需版；cnad_intl_ep：国际站铂金版

        :param package_version: The package_version of this ProtectedIpResponse.
        :type package_version: str
        """
        self._package_version = package_version

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
        if not isinstance(other, ProtectedIpResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
