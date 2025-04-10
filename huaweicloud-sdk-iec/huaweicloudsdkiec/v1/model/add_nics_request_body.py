# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddNicsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpc_id': 'str',
        'security_groups': 'list[BaseId]',
        'subnet_id': 'str',
        'nic_num': 'int',
        'ipv6_enable': 'bool',
        'ipv6_bandwidth': 'Ipv6BandwidthForNic'
    }

    attribute_map = {
        'vpc_id': 'vpc_id',
        'security_groups': 'security_groups',
        'subnet_id': 'subnet_id',
        'nic_num': 'nic_num',
        'ipv6_enable': 'ipv6_enable',
        'ipv6_bandwidth': 'ipv6_bandwidth'
    }

    def __init__(self, vpc_id=None, security_groups=None, subnet_id=None, nic_num=None, ipv6_enable=None, ipv6_bandwidth=None):
        r"""AddNicsRequestBody

        The model defined in huaweicloud sdk

        :param vpc_id: 虚拟私有云ID。
        :type vpc_id: str
        :param security_groups: 安全组ID列表。
        :type security_groups: list[:class:`huaweicloudsdkiec.v1.BaseId`]
        :param subnet_id: 子网ID。  当subnet_id提供时，则在该子网下创建nic_num个网卡； 不输入，则自动分配subnet。 当添加网卡的VPC为手动规划VPC时，subnet_id必填。
        :type subnet_id: str
        :param nic_num: 待添加网卡数量。
        :type nic_num: int
        :param ipv6_enable: 是否支持IPv6  取值为true时，标识此网卡支持IPv6。
        :type ipv6_enable: bool
        :param ipv6_bandwidth: 
        :type ipv6_bandwidth: :class:`huaweicloudsdkiec.v1.Ipv6BandwidthForNic`
        """
        
        

        self._vpc_id = None
        self._security_groups = None
        self._subnet_id = None
        self._nic_num = None
        self._ipv6_enable = None
        self._ipv6_bandwidth = None
        self.discriminator = None

        self.vpc_id = vpc_id
        self.security_groups = security_groups
        if subnet_id is not None:
            self.subnet_id = subnet_id
        self.nic_num = nic_num
        if ipv6_enable is not None:
            self.ipv6_enable = ipv6_enable
        if ipv6_bandwidth is not None:
            self.ipv6_bandwidth = ipv6_bandwidth

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this AddNicsRequestBody.

        虚拟私有云ID。

        :return: The vpc_id of this AddNicsRequestBody.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this AddNicsRequestBody.

        虚拟私有云ID。

        :param vpc_id: The vpc_id of this AddNicsRequestBody.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def security_groups(self):
        r"""Gets the security_groups of this AddNicsRequestBody.

        安全组ID列表。

        :return: The security_groups of this AddNicsRequestBody.
        :rtype: list[:class:`huaweicloudsdkiec.v1.BaseId`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        r"""Sets the security_groups of this AddNicsRequestBody.

        安全组ID列表。

        :param security_groups: The security_groups of this AddNicsRequestBody.
        :type security_groups: list[:class:`huaweicloudsdkiec.v1.BaseId`]
        """
        self._security_groups = security_groups

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this AddNicsRequestBody.

        子网ID。  当subnet_id提供时，则在该子网下创建nic_num个网卡； 不输入，则自动分配subnet。 当添加网卡的VPC为手动规划VPC时，subnet_id必填。

        :return: The subnet_id of this AddNicsRequestBody.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this AddNicsRequestBody.

        子网ID。  当subnet_id提供时，则在该子网下创建nic_num个网卡； 不输入，则自动分配subnet。 当添加网卡的VPC为手动规划VPC时，subnet_id必填。

        :param subnet_id: The subnet_id of this AddNicsRequestBody.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def nic_num(self):
        r"""Gets the nic_num of this AddNicsRequestBody.

        待添加网卡数量。

        :return: The nic_num of this AddNicsRequestBody.
        :rtype: int
        """
        return self._nic_num

    @nic_num.setter
    def nic_num(self, nic_num):
        r"""Sets the nic_num of this AddNicsRequestBody.

        待添加网卡数量。

        :param nic_num: The nic_num of this AddNicsRequestBody.
        :type nic_num: int
        """
        self._nic_num = nic_num

    @property
    def ipv6_enable(self):
        r"""Gets the ipv6_enable of this AddNicsRequestBody.

        是否支持IPv6  取值为true时，标识此网卡支持IPv6。

        :return: The ipv6_enable of this AddNicsRequestBody.
        :rtype: bool
        """
        return self._ipv6_enable

    @ipv6_enable.setter
    def ipv6_enable(self, ipv6_enable):
        r"""Sets the ipv6_enable of this AddNicsRequestBody.

        是否支持IPv6  取值为true时，标识此网卡支持IPv6。

        :param ipv6_enable: The ipv6_enable of this AddNicsRequestBody.
        :type ipv6_enable: bool
        """
        self._ipv6_enable = ipv6_enable

    @property
    def ipv6_bandwidth(self):
        r"""Gets the ipv6_bandwidth of this AddNicsRequestBody.

        :return: The ipv6_bandwidth of this AddNicsRequestBody.
        :rtype: :class:`huaweicloudsdkiec.v1.Ipv6BandwidthForNic`
        """
        return self._ipv6_bandwidth

    @ipv6_bandwidth.setter
    def ipv6_bandwidth(self, ipv6_bandwidth):
        r"""Sets the ipv6_bandwidth of this AddNicsRequestBody.

        :param ipv6_bandwidth: The ipv6_bandwidth of this AddNicsRequestBody.
        :type ipv6_bandwidth: :class:`huaweicloudsdkiec.v1.Ipv6BandwidthForNic`
        """
        self._ipv6_bandwidth = ipv6_bandwidth

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
        if not isinstance(other, AddNicsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
