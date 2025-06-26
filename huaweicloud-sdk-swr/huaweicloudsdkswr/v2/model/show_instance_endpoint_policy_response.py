# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceEndpointPolicyResponse(SdkResponse):

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
        'ip_list': 'list[IpInfo]'
    }

    attribute_map = {
        'status': 'status',
        'ip_list': 'ip_list'
    }

    def __init__(self, status=None, ip_list=None):
        r"""ShowInstanceEndpointPolicyResponse

        The model defined in huaweicloud sdk

        :param status: 公网访问状态，Enable、Enabling、EnableFailed、Disable、Disabling、DisableFailed
        :type status: str
        :param ip_list: 白名单列表
        :type ip_list: list[:class:`huaweicloudsdkswr.v2.IpInfo`]
        """
        
        super(ShowInstanceEndpointPolicyResponse, self).__init__()

        self._status = None
        self._ip_list = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if ip_list is not None:
            self.ip_list = ip_list

    @property
    def status(self):
        r"""Gets the status of this ShowInstanceEndpointPolicyResponse.

        公网访问状态，Enable、Enabling、EnableFailed、Disable、Disabling、DisableFailed

        :return: The status of this ShowInstanceEndpointPolicyResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowInstanceEndpointPolicyResponse.

        公网访问状态，Enable、Enabling、EnableFailed、Disable、Disabling、DisableFailed

        :param status: The status of this ShowInstanceEndpointPolicyResponse.
        :type status: str
        """
        self._status = status

    @property
    def ip_list(self):
        r"""Gets the ip_list of this ShowInstanceEndpointPolicyResponse.

        白名单列表

        :return: The ip_list of this ShowInstanceEndpointPolicyResponse.
        :rtype: list[:class:`huaweicloudsdkswr.v2.IpInfo`]
        """
        return self._ip_list

    @ip_list.setter
    def ip_list(self, ip_list):
        r"""Sets the ip_list of this ShowInstanceEndpointPolicyResponse.

        白名单列表

        :param ip_list: The ip_list of this ShowInstanceEndpointPolicyResponse.
        :type ip_list: list[:class:`huaweicloudsdkswr.v2.IpInfo`]
        """
        self._ip_list = ip_list

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
        if not isinstance(other, ShowInstanceEndpointPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
