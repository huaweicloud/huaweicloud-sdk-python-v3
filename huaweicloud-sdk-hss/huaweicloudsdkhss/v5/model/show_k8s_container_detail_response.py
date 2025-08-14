# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowK8sContainerDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_name': 'str',
        'service_username': 'str',
        'service_password': 'str',
        'service_port_list': 'list[ServicePortInfo]',
        'enable_simulate': 'str',
        'hosts': 'str',
        'extra': 'ContainerExtraInfo'
    }

    attribute_map = {
        'service_name': 'service_name',
        'service_username': 'service_username',
        'service_password': 'service_password',
        'service_port_list': 'service_port_list',
        'enable_simulate': 'enable_simulate',
        'hosts': 'hosts',
        'extra': 'extra'
    }

    def __init__(self, service_name=None, service_username=None, service_password=None, service_port_list=None, enable_simulate=None, hosts=None, extra=None):
        r"""ShowK8sContainerDetailResponse

        The model defined in huaweicloud sdk

        :param service_name: 服务名称
        :type service_name: str
        :param service_username: 服务用户名
        :type service_username: str
        :param service_password: 服务密码
        :type service_password: str
        :param service_port_list: 容器各服务端口信息
        :type service_port_list: list[:class:`huaweicloudsdkhss.v5.ServicePortInfo`]
        :param enable_simulate: 数据仿真，默认关闭。开启后将在沙箱中注入仿真数据 - open : 开启 - close : 关闭
        :type enable_simulate: str
        :param hosts: 沙箱域名，域名之间使用 &#39;,&#39; 隔开
        :type hosts: str
        :param extra: 
        :type extra: :class:`huaweicloudsdkhss.v5.ContainerExtraInfo`
        """
        
        super(ShowK8sContainerDetailResponse, self).__init__()

        self._service_name = None
        self._service_username = None
        self._service_password = None
        self._service_port_list = None
        self._enable_simulate = None
        self._hosts = None
        self._extra = None
        self.discriminator = None

        if service_name is not None:
            self.service_name = service_name
        if service_username is not None:
            self.service_username = service_username
        if service_password is not None:
            self.service_password = service_password
        if service_port_list is not None:
            self.service_port_list = service_port_list
        if enable_simulate is not None:
            self.enable_simulate = enable_simulate
        if hosts is not None:
            self.hosts = hosts
        if extra is not None:
            self.extra = extra

    @property
    def service_name(self):
        r"""Gets the service_name of this ShowK8sContainerDetailResponse.

        服务名称

        :return: The service_name of this ShowK8sContainerDetailResponse.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        r"""Sets the service_name of this ShowK8sContainerDetailResponse.

        服务名称

        :param service_name: The service_name of this ShowK8sContainerDetailResponse.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def service_username(self):
        r"""Gets the service_username of this ShowK8sContainerDetailResponse.

        服务用户名

        :return: The service_username of this ShowK8sContainerDetailResponse.
        :rtype: str
        """
        return self._service_username

    @service_username.setter
    def service_username(self, service_username):
        r"""Sets the service_username of this ShowK8sContainerDetailResponse.

        服务用户名

        :param service_username: The service_username of this ShowK8sContainerDetailResponse.
        :type service_username: str
        """
        self._service_username = service_username

    @property
    def service_password(self):
        r"""Gets the service_password of this ShowK8sContainerDetailResponse.

        服务密码

        :return: The service_password of this ShowK8sContainerDetailResponse.
        :rtype: str
        """
        return self._service_password

    @service_password.setter
    def service_password(self, service_password):
        r"""Sets the service_password of this ShowK8sContainerDetailResponse.

        服务密码

        :param service_password: The service_password of this ShowK8sContainerDetailResponse.
        :type service_password: str
        """
        self._service_password = service_password

    @property
    def service_port_list(self):
        r"""Gets the service_port_list of this ShowK8sContainerDetailResponse.

        容器各服务端口信息

        :return: The service_port_list of this ShowK8sContainerDetailResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ServicePortInfo`]
        """
        return self._service_port_list

    @service_port_list.setter
    def service_port_list(self, service_port_list):
        r"""Sets the service_port_list of this ShowK8sContainerDetailResponse.

        容器各服务端口信息

        :param service_port_list: The service_port_list of this ShowK8sContainerDetailResponse.
        :type service_port_list: list[:class:`huaweicloudsdkhss.v5.ServicePortInfo`]
        """
        self._service_port_list = service_port_list

    @property
    def enable_simulate(self):
        r"""Gets the enable_simulate of this ShowK8sContainerDetailResponse.

        数据仿真，默认关闭。开启后将在沙箱中注入仿真数据 - open : 开启 - close : 关闭

        :return: The enable_simulate of this ShowK8sContainerDetailResponse.
        :rtype: str
        """
        return self._enable_simulate

    @enable_simulate.setter
    def enable_simulate(self, enable_simulate):
        r"""Sets the enable_simulate of this ShowK8sContainerDetailResponse.

        数据仿真，默认关闭。开启后将在沙箱中注入仿真数据 - open : 开启 - close : 关闭

        :param enable_simulate: The enable_simulate of this ShowK8sContainerDetailResponse.
        :type enable_simulate: str
        """
        self._enable_simulate = enable_simulate

    @property
    def hosts(self):
        r"""Gets the hosts of this ShowK8sContainerDetailResponse.

        沙箱域名，域名之间使用 ',' 隔开

        :return: The hosts of this ShowK8sContainerDetailResponse.
        :rtype: str
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        r"""Sets the hosts of this ShowK8sContainerDetailResponse.

        沙箱域名，域名之间使用 ',' 隔开

        :param hosts: The hosts of this ShowK8sContainerDetailResponse.
        :type hosts: str
        """
        self._hosts = hosts

    @property
    def extra(self):
        r"""Gets the extra of this ShowK8sContainerDetailResponse.

        :return: The extra of this ShowK8sContainerDetailResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.ContainerExtraInfo`
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        r"""Sets the extra of this ShowK8sContainerDetailResponse.

        :param extra: The extra of this ShowK8sContainerDetailResponse.
        :type extra: :class:`huaweicloudsdkhss.v5.ContainerExtraInfo`
        """
        self._extra = extra

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
        if not isinstance(other, ShowK8sContainerDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
