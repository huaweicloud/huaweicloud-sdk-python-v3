# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KernelModuleHostInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_id': 'str',
        'host_id': 'str',
        'host_name': 'str',
        'host_ip': 'str',
        'kernel_module_info': 'KernelModuleInfo'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'host_id': 'host_id',
        'host_name': 'host_name',
        'host_ip': 'host_ip',
        'kernel_module_info': 'kernel_module_info'
    }

    def __init__(self, agent_id=None, host_id=None, host_name=None, host_ip=None, kernel_module_info=None):
        r"""KernelModuleHostInfo

        The model defined in huaweicloud sdk

        :param agent_id: agent_id
        :type agent_id: str
        :param host_id: 主机id
        :type host_id: str
        :param host_name: 服务器名称
        :type host_name: str
        :param host_ip: 服务器ip
        :type host_ip: str
        :param kernel_module_info: 
        :type kernel_module_info: :class:`huaweicloudsdkhss.v5.KernelModuleInfo`
        """
        
        

        self._agent_id = None
        self._host_id = None
        self._host_name = None
        self._host_ip = None
        self._kernel_module_info = None
        self.discriminator = None

        if agent_id is not None:
            self.agent_id = agent_id
        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if host_ip is not None:
            self.host_ip = host_ip
        if kernel_module_info is not None:
            self.kernel_module_info = kernel_module_info

    @property
    def agent_id(self):
        r"""Gets the agent_id of this KernelModuleHostInfo.

        agent_id

        :return: The agent_id of this KernelModuleHostInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this KernelModuleHostInfo.

        agent_id

        :param agent_id: The agent_id of this KernelModuleHostInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def host_id(self):
        r"""Gets the host_id of this KernelModuleHostInfo.

        主机id

        :return: The host_id of this KernelModuleHostInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this KernelModuleHostInfo.

        主机id

        :param host_id: The host_id of this KernelModuleHostInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this KernelModuleHostInfo.

        服务器名称

        :return: The host_name of this KernelModuleHostInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this KernelModuleHostInfo.

        服务器名称

        :param host_name: The host_name of this KernelModuleHostInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ip(self):
        r"""Gets the host_ip of this KernelModuleHostInfo.

        服务器ip

        :return: The host_ip of this KernelModuleHostInfo.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this KernelModuleHostInfo.

        服务器ip

        :param host_ip: The host_ip of this KernelModuleHostInfo.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def kernel_module_info(self):
        r"""Gets the kernel_module_info of this KernelModuleHostInfo.

        :return: The kernel_module_info of this KernelModuleHostInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.KernelModuleInfo`
        """
        return self._kernel_module_info

    @kernel_module_info.setter
    def kernel_module_info(self, kernel_module_info):
        r"""Sets the kernel_module_info of this KernelModuleHostInfo.

        :param kernel_module_info: The kernel_module_info of this KernelModuleHostInfo.
        :type kernel_module_info: :class:`huaweicloudsdkhss.v5.KernelModuleInfo`
        """
        self._kernel_module_info = kernel_module_info

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
        if not isinstance(other, KernelModuleHostInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
