# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchChangeDesktopNetworkReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_ids': 'list[str]',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_ids': 'list[str]'
    }

    attribute_map = {
        'desktop_ids': 'desktop_ids',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_ids': 'security_group_ids'
    }

    def __init__(self, desktop_ids=None, vpc_id=None, subnet_id=None, security_group_ids=None):
        r"""BatchChangeDesktopNetworkReq

        The model defined in huaweicloud sdk

        :param desktop_ids: 桌面id列表，最小为1，最大为100。
        :type desktop_ids: list[str]
        :param vpc_id: 待切换VPC的ID。
        :type vpc_id: str
        :param subnet_id: 待切换子网的ID。
        :type subnet_id: str
        :param security_group_ids: 安全组ID列表。
        :type security_group_ids: list[str]
        """
        
        

        self._desktop_ids = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_ids = None
        self.discriminator = None

        self.desktop_ids = desktop_ids
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        if security_group_ids is not None:
            self.security_group_ids = security_group_ids

    @property
    def desktop_ids(self):
        r"""Gets the desktop_ids of this BatchChangeDesktopNetworkReq.

        桌面id列表，最小为1，最大为100。

        :return: The desktop_ids of this BatchChangeDesktopNetworkReq.
        :rtype: list[str]
        """
        return self._desktop_ids

    @desktop_ids.setter
    def desktop_ids(self, desktop_ids):
        r"""Sets the desktop_ids of this BatchChangeDesktopNetworkReq.

        桌面id列表，最小为1，最大为100。

        :param desktop_ids: The desktop_ids of this BatchChangeDesktopNetworkReq.
        :type desktop_ids: list[str]
        """
        self._desktop_ids = desktop_ids

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this BatchChangeDesktopNetworkReq.

        待切换VPC的ID。

        :return: The vpc_id of this BatchChangeDesktopNetworkReq.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this BatchChangeDesktopNetworkReq.

        待切换VPC的ID。

        :param vpc_id: The vpc_id of this BatchChangeDesktopNetworkReq.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this BatchChangeDesktopNetworkReq.

        待切换子网的ID。

        :return: The subnet_id of this BatchChangeDesktopNetworkReq.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this BatchChangeDesktopNetworkReq.

        待切换子网的ID。

        :param subnet_id: The subnet_id of this BatchChangeDesktopNetworkReq.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_ids(self):
        r"""Gets the security_group_ids of this BatchChangeDesktopNetworkReq.

        安全组ID列表。

        :return: The security_group_ids of this BatchChangeDesktopNetworkReq.
        :rtype: list[str]
        """
        return self._security_group_ids

    @security_group_ids.setter
    def security_group_ids(self, security_group_ids):
        r"""Sets the security_group_ids of this BatchChangeDesktopNetworkReq.

        安全组ID列表。

        :param security_group_ids: The security_group_ids of this BatchChangeDesktopNetworkReq.
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
        if not isinstance(other, BatchChangeDesktopNetworkReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
