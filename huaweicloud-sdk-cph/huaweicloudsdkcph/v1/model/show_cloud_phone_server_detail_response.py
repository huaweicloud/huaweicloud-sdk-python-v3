# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCloudPhoneServerDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'servers': 'list[object]',
        'band_widths': 'list[object]',
        'volumes': 'list[object]',
        'security_groups': 'list[str]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'servers': 'servers',
        'band_widths': 'band_widths',
        'volumes': 'volumes',
        'security_groups': 'security_groups'
    }

    def __init__(self, request_id=None, servers=None, band_widths=None, volumes=None, security_groups=None):
        """ShowCloudPhoneServerDetailResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求的唯一标识ID
        :type request_id: str
        :param servers: 云手机服务器信息
        :type servers: list[object]
        :param band_widths: 云手机服务器带宽信息的结构体数组
        :type band_widths: list[object]
        :param volumes: 云手机服务器卷信息的结构体数组
        :type volumes: list[object]
        :param security_groups: 服务器扩展网卡绑定的安全组信息 系统定义网络的服务器，该字段返回为空列表
        :type security_groups: list[str]
        """
        
        super(ShowCloudPhoneServerDetailResponse, self).__init__()

        self._request_id = None
        self._servers = None
        self._band_widths = None
        self._volumes = None
        self._security_groups = None
        self.discriminator = None

        self.request_id = request_id
        self.servers = servers
        self.band_widths = band_widths
        self.volumes = volumes
        self.security_groups = security_groups

    @property
    def request_id(self):
        """Gets the request_id of this ShowCloudPhoneServerDetailResponse.

        请求的唯一标识ID

        :return: The request_id of this ShowCloudPhoneServerDetailResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ShowCloudPhoneServerDetailResponse.

        请求的唯一标识ID

        :param request_id: The request_id of this ShowCloudPhoneServerDetailResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def servers(self):
        """Gets the servers of this ShowCloudPhoneServerDetailResponse.

        云手机服务器信息

        :return: The servers of this ShowCloudPhoneServerDetailResponse.
        :rtype: list[object]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """Sets the servers of this ShowCloudPhoneServerDetailResponse.

        云手机服务器信息

        :param servers: The servers of this ShowCloudPhoneServerDetailResponse.
        :type servers: list[object]
        """
        self._servers = servers

    @property
    def band_widths(self):
        """Gets the band_widths of this ShowCloudPhoneServerDetailResponse.

        云手机服务器带宽信息的结构体数组

        :return: The band_widths of this ShowCloudPhoneServerDetailResponse.
        :rtype: list[object]
        """
        return self._band_widths

    @band_widths.setter
    def band_widths(self, band_widths):
        """Sets the band_widths of this ShowCloudPhoneServerDetailResponse.

        云手机服务器带宽信息的结构体数组

        :param band_widths: The band_widths of this ShowCloudPhoneServerDetailResponse.
        :type band_widths: list[object]
        """
        self._band_widths = band_widths

    @property
    def volumes(self):
        """Gets the volumes of this ShowCloudPhoneServerDetailResponse.

        云手机服务器卷信息的结构体数组

        :return: The volumes of this ShowCloudPhoneServerDetailResponse.
        :rtype: list[object]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this ShowCloudPhoneServerDetailResponse.

        云手机服务器卷信息的结构体数组

        :param volumes: The volumes of this ShowCloudPhoneServerDetailResponse.
        :type volumes: list[object]
        """
        self._volumes = volumes

    @property
    def security_groups(self):
        """Gets the security_groups of this ShowCloudPhoneServerDetailResponse.

        服务器扩展网卡绑定的安全组信息 系统定义网络的服务器，该字段返回为空列表

        :return: The security_groups of this ShowCloudPhoneServerDetailResponse.
        :rtype: list[str]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this ShowCloudPhoneServerDetailResponse.

        服务器扩展网卡绑定的安全组信息 系统定义网络的服务器，该字段返回为空列表

        :param security_groups: The security_groups of this ShowCloudPhoneServerDetailResponse.
        :type security_groups: list[str]
        """
        self._security_groups = security_groups

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
        if not isinstance(other, ShowCloudPhoneServerDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
