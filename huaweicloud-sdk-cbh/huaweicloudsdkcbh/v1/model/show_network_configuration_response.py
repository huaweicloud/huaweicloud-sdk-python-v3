# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowNetworkConfigurationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'bool',
        'security_grp_status': 'bool',
        'firewall_status': 'bool',
        'public_eip_status': 'bool'
    }

    attribute_map = {
        'status': 'status',
        'security_grp_status': 'security_grp_status',
        'firewall_status': 'firewall_status',
        'public_eip_status': 'public_eip_status'
    }

    def __init__(self, status=None, security_grp_status=None, firewall_status=None, public_eip_status=None):
        r"""ShowNetworkConfigurationResponse

        The model defined in huaweicloud sdk

        :param status: 云堡垒机实例网络状态。下面3个正常则正常，有一个不正常，网络状态为失败。
        :type status: bool
        :param security_grp_status: 云堡垒机实例安全组状态。 - true  正常 - false 失败
        :type security_grp_status: bool
        :param firewall_status: 云堡垒机实例防火墙状态。 - true  正常 - false 失败
        :type firewall_status: bool
        :param public_eip_status: 云堡垒机实例公网IP状态。 - true  正常 - false 失败
        :type public_eip_status: bool
        """
        
        super(ShowNetworkConfigurationResponse, self).__init__()

        self._status = None
        self._security_grp_status = None
        self._firewall_status = None
        self._public_eip_status = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if security_grp_status is not None:
            self.security_grp_status = security_grp_status
        if firewall_status is not None:
            self.firewall_status = firewall_status
        if public_eip_status is not None:
            self.public_eip_status = public_eip_status

    @property
    def status(self):
        r"""Gets the status of this ShowNetworkConfigurationResponse.

        云堡垒机实例网络状态。下面3个正常则正常，有一个不正常，网络状态为失败。

        :return: The status of this ShowNetworkConfigurationResponse.
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowNetworkConfigurationResponse.

        云堡垒机实例网络状态。下面3个正常则正常，有一个不正常，网络状态为失败。

        :param status: The status of this ShowNetworkConfigurationResponse.
        :type status: bool
        """
        self._status = status

    @property
    def security_grp_status(self):
        r"""Gets the security_grp_status of this ShowNetworkConfigurationResponse.

        云堡垒机实例安全组状态。 - true  正常 - false 失败

        :return: The security_grp_status of this ShowNetworkConfigurationResponse.
        :rtype: bool
        """
        return self._security_grp_status

    @security_grp_status.setter
    def security_grp_status(self, security_grp_status):
        r"""Sets the security_grp_status of this ShowNetworkConfigurationResponse.

        云堡垒机实例安全组状态。 - true  正常 - false 失败

        :param security_grp_status: The security_grp_status of this ShowNetworkConfigurationResponse.
        :type security_grp_status: bool
        """
        self._security_grp_status = security_grp_status

    @property
    def firewall_status(self):
        r"""Gets the firewall_status of this ShowNetworkConfigurationResponse.

        云堡垒机实例防火墙状态。 - true  正常 - false 失败

        :return: The firewall_status of this ShowNetworkConfigurationResponse.
        :rtype: bool
        """
        return self._firewall_status

    @firewall_status.setter
    def firewall_status(self, firewall_status):
        r"""Sets the firewall_status of this ShowNetworkConfigurationResponse.

        云堡垒机实例防火墙状态。 - true  正常 - false 失败

        :param firewall_status: The firewall_status of this ShowNetworkConfigurationResponse.
        :type firewall_status: bool
        """
        self._firewall_status = firewall_status

    @property
    def public_eip_status(self):
        r"""Gets the public_eip_status of this ShowNetworkConfigurationResponse.

        云堡垒机实例公网IP状态。 - true  正常 - false 失败

        :return: The public_eip_status of this ShowNetworkConfigurationResponse.
        :rtype: bool
        """
        return self._public_eip_status

    @public_eip_status.setter
    def public_eip_status(self, public_eip_status):
        r"""Sets the public_eip_status of this ShowNetworkConfigurationResponse.

        云堡垒机实例公网IP状态。 - true  正常 - false 失败

        :param public_eip_status: The public_eip_status of this ShowNetworkConfigurationResponse.
        :type public_eip_status: bool
        """
        self._public_eip_status = public_eip_status

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
        if not isinstance(other, ShowNetworkConfigurationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
