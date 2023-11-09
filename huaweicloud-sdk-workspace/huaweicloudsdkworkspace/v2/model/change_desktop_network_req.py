# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeDesktopNetworkReq:

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
        'subnet_id': 'str',
        'private_ip': 'str',
        'security_group_ids': 'list[str]'
    }

    attribute_map = {
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'private_ip': 'private_ip',
        'security_group_ids': 'security_group_ids'
    }

    def __init__(self, vpc_id=None, subnet_id=None, private_ip=None, security_group_ids=None):
        """ChangeDesktopNetworkReq

        The model defined in huaweicloud sdk

        :param vpc_id: 待切换VPC的ID
        :type vpc_id: str
        :param subnet_id: 待切换子网的ID
        :type subnet_id: str
        :param private_ip: 指定私有IP地址
        :type private_ip: str
        :param security_group_ids: 安全组ID列表
        :type security_group_ids: list[str]
        """
        
        

        self._vpc_id = None
        self._subnet_id = None
        self._private_ip = None
        self._security_group_ids = None
        self.discriminator = None

        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        if private_ip is not None:
            self.private_ip = private_ip
        self.security_group_ids = security_group_ids

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ChangeDesktopNetworkReq.

        待切换VPC的ID

        :return: The vpc_id of this ChangeDesktopNetworkReq.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ChangeDesktopNetworkReq.

        待切换VPC的ID

        :param vpc_id: The vpc_id of this ChangeDesktopNetworkReq.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this ChangeDesktopNetworkReq.

        待切换子网的ID

        :return: The subnet_id of this ChangeDesktopNetworkReq.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this ChangeDesktopNetworkReq.

        待切换子网的ID

        :param subnet_id: The subnet_id of this ChangeDesktopNetworkReq.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def private_ip(self):
        """Gets the private_ip of this ChangeDesktopNetworkReq.

        指定私有IP地址

        :return: The private_ip of this ChangeDesktopNetworkReq.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this ChangeDesktopNetworkReq.

        指定私有IP地址

        :param private_ip: The private_ip of this ChangeDesktopNetworkReq.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def security_group_ids(self):
        """Gets the security_group_ids of this ChangeDesktopNetworkReq.

        安全组ID列表

        :return: The security_group_ids of this ChangeDesktopNetworkReq.
        :rtype: list[str]
        """
        return self._security_group_ids

    @security_group_ids.setter
    def security_group_ids(self, security_group_ids):
        """Sets the security_group_ids of this ChangeDesktopNetworkReq.

        安全组ID列表

        :param security_group_ids: The security_group_ids of this ChangeDesktopNetworkReq.
        :type security_group_ids: list[str]
        """
        self._security_group_ids = security_group_ids

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
        if not isinstance(other, ChangeDesktopNetworkReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
