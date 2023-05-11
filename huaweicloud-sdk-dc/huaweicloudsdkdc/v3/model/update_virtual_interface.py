# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateVirtualInterface:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'bandwidth': 'int',
        'remote_ep_group': 'list[str]',
        'service_ep_group': 'list[str]',
        'enable_bfd': 'bool',
        'enable_nqa': 'bool',
        'status': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'bandwidth': 'bandwidth',
        'remote_ep_group': 'remote_ep_group',
        'service_ep_group': 'service_ep_group',
        'enable_bfd': 'enable_bfd',
        'enable_nqa': 'enable_nqa',
        'status': 'status'
    }

    def __init__(self, name=None, description=None, bandwidth=None, remote_ep_group=None, service_ep_group=None, enable_bfd=None, enable_nqa=None, status=None):
        """UpdateVirtualInterface

        The model defined in huaweicloud sdk

        :param name: 虚拟接口名字
        :type name: str
        :param description: 虚拟接口描述信息
        :type description: str
        :param bandwidth: 虚拟接口带宽配置
        :type bandwidth: int
        :param remote_ep_group: 远端子网列表，记录租户侧的cidrs
        :type remote_ep_group: list[str]
        :param service_ep_group: 用于公网专线,用户访问公网服务地址列表
        :type service_ep_group: list[str]
        :param enable_bfd: 是否使能bfd功能：true或false
        :type enable_bfd: bool
        :param enable_nqa: 是否使能nqa功能：true或false
        :type enable_nqa: bool
        :param status: 对其他租户创建的虚拟接口进行确认,可以是ACCEPTED和REJECTED
        :type status: str
        """
        
        

        self._name = None
        self._description = None
        self._bandwidth = None
        self._remote_ep_group = None
        self._service_ep_group = None
        self._enable_bfd = None
        self._enable_nqa = None
        self._status = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if remote_ep_group is not None:
            self.remote_ep_group = remote_ep_group
        if service_ep_group is not None:
            self.service_ep_group = service_ep_group
        if enable_bfd is not None:
            self.enable_bfd = enable_bfd
        if enable_nqa is not None:
            self.enable_nqa = enable_nqa
        if status is not None:
            self.status = status

    @property
    def name(self):
        """Gets the name of this UpdateVirtualInterface.

        虚拟接口名字

        :return: The name of this UpdateVirtualInterface.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateVirtualInterface.

        虚拟接口名字

        :param name: The name of this UpdateVirtualInterface.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateVirtualInterface.

        虚拟接口描述信息

        :return: The description of this UpdateVirtualInterface.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateVirtualInterface.

        虚拟接口描述信息

        :param description: The description of this UpdateVirtualInterface.
        :type description: str
        """
        self._description = description

    @property
    def bandwidth(self):
        """Gets the bandwidth of this UpdateVirtualInterface.

        虚拟接口带宽配置

        :return: The bandwidth of this UpdateVirtualInterface.
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this UpdateVirtualInterface.

        虚拟接口带宽配置

        :param bandwidth: The bandwidth of this UpdateVirtualInterface.
        :type bandwidth: int
        """
        self._bandwidth = bandwidth

    @property
    def remote_ep_group(self):
        """Gets the remote_ep_group of this UpdateVirtualInterface.

        远端子网列表，记录租户侧的cidrs

        :return: The remote_ep_group of this UpdateVirtualInterface.
        :rtype: list[str]
        """
        return self._remote_ep_group

    @remote_ep_group.setter
    def remote_ep_group(self, remote_ep_group):
        """Sets the remote_ep_group of this UpdateVirtualInterface.

        远端子网列表，记录租户侧的cidrs

        :param remote_ep_group: The remote_ep_group of this UpdateVirtualInterface.
        :type remote_ep_group: list[str]
        """
        self._remote_ep_group = remote_ep_group

    @property
    def service_ep_group(self):
        """Gets the service_ep_group of this UpdateVirtualInterface.

        用于公网专线,用户访问公网服务地址列表

        :return: The service_ep_group of this UpdateVirtualInterface.
        :rtype: list[str]
        """
        return self._service_ep_group

    @service_ep_group.setter
    def service_ep_group(self, service_ep_group):
        """Sets the service_ep_group of this UpdateVirtualInterface.

        用于公网专线,用户访问公网服务地址列表

        :param service_ep_group: The service_ep_group of this UpdateVirtualInterface.
        :type service_ep_group: list[str]
        """
        self._service_ep_group = service_ep_group

    @property
    def enable_bfd(self):
        """Gets the enable_bfd of this UpdateVirtualInterface.

        是否使能bfd功能：true或false

        :return: The enable_bfd of this UpdateVirtualInterface.
        :rtype: bool
        """
        return self._enable_bfd

    @enable_bfd.setter
    def enable_bfd(self, enable_bfd):
        """Sets the enable_bfd of this UpdateVirtualInterface.

        是否使能bfd功能：true或false

        :param enable_bfd: The enable_bfd of this UpdateVirtualInterface.
        :type enable_bfd: bool
        """
        self._enable_bfd = enable_bfd

    @property
    def enable_nqa(self):
        """Gets the enable_nqa of this UpdateVirtualInterface.

        是否使能nqa功能：true或false

        :return: The enable_nqa of this UpdateVirtualInterface.
        :rtype: bool
        """
        return self._enable_nqa

    @enable_nqa.setter
    def enable_nqa(self, enable_nqa):
        """Sets the enable_nqa of this UpdateVirtualInterface.

        是否使能nqa功能：true或false

        :param enable_nqa: The enable_nqa of this UpdateVirtualInterface.
        :type enable_nqa: bool
        """
        self._enable_nqa = enable_nqa

    @property
    def status(self):
        """Gets the status of this UpdateVirtualInterface.

        对其他租户创建的虚拟接口进行确认,可以是ACCEPTED和REJECTED

        :return: The status of this UpdateVirtualInterface.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateVirtualInterface.

        对其他租户创建的虚拟接口进行确认,可以是ACCEPTED和REJECTED

        :param status: The status of this UpdateVirtualInterface.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, UpdateVirtualInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
