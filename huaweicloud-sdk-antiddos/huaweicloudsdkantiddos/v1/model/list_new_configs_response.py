# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNewConfigsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'traffic_limited_list': 'list[TriggerBpsDict]',
        'http_limited_list': 'list[TriggerQpsDict]',
        'connection_limited_list': 'list[CleanLimitDict]',
        'extend_ddos_config': 'list[ExtendDDoSSet]'
    }

    attribute_map = {
        'traffic_limited_list': 'traffic_limited_list',
        'http_limited_list': 'http_limited_list',
        'connection_limited_list': 'connection_limited_list',
        'extend_ddos_config': 'extend_ddos_config'
    }

    def __init__(self, traffic_limited_list=None, http_limited_list=None, connection_limited_list=None, extend_ddos_config=None):
        """ListNewConfigsResponse

        The model defined in huaweicloud sdk

        :param traffic_limited_list: 流量限制列表
        :type traffic_limited_list: list[:class:`huaweicloudsdkantiddos.v1.TriggerBpsDict`]
        :param http_limited_list: HTTP限制列表
        :type http_limited_list: list[:class:`huaweicloudsdkantiddos.v1.TriggerQpsDict`]
        :param connection_limited_list: 连接数限制列表
        :type connection_limited_list: list[:class:`huaweicloudsdkantiddos.v1.CleanLimitDict`]
        :param extend_ddos_config: 扩展配置列表
        :type extend_ddos_config: list[:class:`huaweicloudsdkantiddos.v1.ExtendDDoSSet`]
        """
        
        super(ListNewConfigsResponse, self).__init__()

        self._traffic_limited_list = None
        self._http_limited_list = None
        self._connection_limited_list = None
        self._extend_ddos_config = None
        self.discriminator = None

        if traffic_limited_list is not None:
            self.traffic_limited_list = traffic_limited_list
        if http_limited_list is not None:
            self.http_limited_list = http_limited_list
        if connection_limited_list is not None:
            self.connection_limited_list = connection_limited_list
        if extend_ddos_config is not None:
            self.extend_ddos_config = extend_ddos_config

    @property
    def traffic_limited_list(self):
        """Gets the traffic_limited_list of this ListNewConfigsResponse.

        流量限制列表

        :return: The traffic_limited_list of this ListNewConfigsResponse.
        :rtype: list[:class:`huaweicloudsdkantiddos.v1.TriggerBpsDict`]
        """
        return self._traffic_limited_list

    @traffic_limited_list.setter
    def traffic_limited_list(self, traffic_limited_list):
        """Sets the traffic_limited_list of this ListNewConfigsResponse.

        流量限制列表

        :param traffic_limited_list: The traffic_limited_list of this ListNewConfigsResponse.
        :type traffic_limited_list: list[:class:`huaweicloudsdkantiddos.v1.TriggerBpsDict`]
        """
        self._traffic_limited_list = traffic_limited_list

    @property
    def http_limited_list(self):
        """Gets the http_limited_list of this ListNewConfigsResponse.

        HTTP限制列表

        :return: The http_limited_list of this ListNewConfigsResponse.
        :rtype: list[:class:`huaweicloudsdkantiddos.v1.TriggerQpsDict`]
        """
        return self._http_limited_list

    @http_limited_list.setter
    def http_limited_list(self, http_limited_list):
        """Sets the http_limited_list of this ListNewConfigsResponse.

        HTTP限制列表

        :param http_limited_list: The http_limited_list of this ListNewConfigsResponse.
        :type http_limited_list: list[:class:`huaweicloudsdkantiddos.v1.TriggerQpsDict`]
        """
        self._http_limited_list = http_limited_list

    @property
    def connection_limited_list(self):
        """Gets the connection_limited_list of this ListNewConfigsResponse.

        连接数限制列表

        :return: The connection_limited_list of this ListNewConfigsResponse.
        :rtype: list[:class:`huaweicloudsdkantiddos.v1.CleanLimitDict`]
        """
        return self._connection_limited_list

    @connection_limited_list.setter
    def connection_limited_list(self, connection_limited_list):
        """Sets the connection_limited_list of this ListNewConfigsResponse.

        连接数限制列表

        :param connection_limited_list: The connection_limited_list of this ListNewConfigsResponse.
        :type connection_limited_list: list[:class:`huaweicloudsdkantiddos.v1.CleanLimitDict`]
        """
        self._connection_limited_list = connection_limited_list

    @property
    def extend_ddos_config(self):
        """Gets the extend_ddos_config of this ListNewConfigsResponse.

        扩展配置列表

        :return: The extend_ddos_config of this ListNewConfigsResponse.
        :rtype: list[:class:`huaweicloudsdkantiddos.v1.ExtendDDoSSet`]
        """
        return self._extend_ddos_config

    @extend_ddos_config.setter
    def extend_ddos_config(self, extend_ddos_config):
        """Sets the extend_ddos_config of this ListNewConfigsResponse.

        扩展配置列表

        :param extend_ddos_config: The extend_ddos_config of this ListNewConfigsResponse.
        :type extend_ddos_config: list[:class:`huaweicloudsdkantiddos.v1.ExtendDDoSSet`]
        """
        self._extend_ddos_config = extend_ddos_config

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
        if not isinstance(other, ListNewConfigsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
