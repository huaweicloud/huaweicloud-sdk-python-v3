# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeInstanceNetworkResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'security_grp_status': 'str',
        'firewall_status': 'bool',
        'public_eip_status': 'bool',
        'nics': 'bool',
        'public_eip_statu': 'bool'
    }

    attribute_map = {
        'status': 'status',
        'security_grp_status': 'security_grp_status',
        'firewall_status': 'firewall_status',
        'public_eip_status': 'public_eip_status',
        'nics': 'nics',
        'public_eip_statu': 'public_eip_statu'
    }

    def __init__(self, status=None, security_grp_status=None, firewall_status=None, public_eip_status=None, nics=None, public_eip_statu=None):
        """ChangeInstanceNetworkResponse

        The model defined in huaweicloud sdk

        :param status: 状态
        :type status: str
        :param security_grp_status: 安全组
        :type security_grp_status: str
        :param firewall_status: 防火墙状态
        :type firewall_status: bool
        :param public_eip_status: 公共EIP状态
        :type public_eip_status: bool
        :param nics: 防火墙状态(兼容)
        :type nics: bool
        :param public_eip_statu: 公共EIP状态(兼容)
        :type public_eip_statu: bool
        """
        
        super(ChangeInstanceNetworkResponse, self).__init__()

        self._status = None
        self._security_grp_status = None
        self._firewall_status = None
        self._public_eip_status = None
        self._nics = None
        self._public_eip_statu = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if security_grp_status is not None:
            self.security_grp_status = security_grp_status
        if firewall_status is not None:
            self.firewall_status = firewall_status
        if public_eip_status is not None:
            self.public_eip_status = public_eip_status
        if nics is not None:
            self.nics = nics
        if public_eip_statu is not None:
            self.public_eip_statu = public_eip_statu

    @property
    def status(self):
        """Gets the status of this ChangeInstanceNetworkResponse.

        状态

        :return: The status of this ChangeInstanceNetworkResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ChangeInstanceNetworkResponse.

        状态

        :param status: The status of this ChangeInstanceNetworkResponse.
        :type status: str
        """
        self._status = status

    @property
    def security_grp_status(self):
        """Gets the security_grp_status of this ChangeInstanceNetworkResponse.

        安全组

        :return: The security_grp_status of this ChangeInstanceNetworkResponse.
        :rtype: str
        """
        return self._security_grp_status

    @security_grp_status.setter
    def security_grp_status(self, security_grp_status):
        """Sets the security_grp_status of this ChangeInstanceNetworkResponse.

        安全组

        :param security_grp_status: The security_grp_status of this ChangeInstanceNetworkResponse.
        :type security_grp_status: str
        """
        self._security_grp_status = security_grp_status

    @property
    def firewall_status(self):
        """Gets the firewall_status of this ChangeInstanceNetworkResponse.

        防火墙状态

        :return: The firewall_status of this ChangeInstanceNetworkResponse.
        :rtype: bool
        """
        return self._firewall_status

    @firewall_status.setter
    def firewall_status(self, firewall_status):
        """Sets the firewall_status of this ChangeInstanceNetworkResponse.

        防火墙状态

        :param firewall_status: The firewall_status of this ChangeInstanceNetworkResponse.
        :type firewall_status: bool
        """
        self._firewall_status = firewall_status

    @property
    def public_eip_status(self):
        """Gets the public_eip_status of this ChangeInstanceNetworkResponse.

        公共EIP状态

        :return: The public_eip_status of this ChangeInstanceNetworkResponse.
        :rtype: bool
        """
        return self._public_eip_status

    @public_eip_status.setter
    def public_eip_status(self, public_eip_status):
        """Sets the public_eip_status of this ChangeInstanceNetworkResponse.

        公共EIP状态

        :param public_eip_status: The public_eip_status of this ChangeInstanceNetworkResponse.
        :type public_eip_status: bool
        """
        self._public_eip_status = public_eip_status

    @property
    def nics(self):
        """Gets the nics of this ChangeInstanceNetworkResponse.

        防火墙状态(兼容)

        :return: The nics of this ChangeInstanceNetworkResponse.
        :rtype: bool
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this ChangeInstanceNetworkResponse.

        防火墙状态(兼容)

        :param nics: The nics of this ChangeInstanceNetworkResponse.
        :type nics: bool
        """
        self._nics = nics

    @property
    def public_eip_statu(self):
        """Gets the public_eip_statu of this ChangeInstanceNetworkResponse.

        公共EIP状态(兼容)

        :return: The public_eip_statu of this ChangeInstanceNetworkResponse.
        :rtype: bool
        """
        return self._public_eip_statu

    @public_eip_statu.setter
    def public_eip_statu(self, public_eip_statu):
        """Sets the public_eip_statu of this ChangeInstanceNetworkResponse.

        公共EIP状态(兼容)

        :param public_eip_statu: The public_eip_statu of this ChangeInstanceNetworkResponse.
        :type public_eip_statu: bool
        """
        self._public_eip_statu = public_eip_statu

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
        if not isinstance(other, ChangeInstanceNetworkResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
