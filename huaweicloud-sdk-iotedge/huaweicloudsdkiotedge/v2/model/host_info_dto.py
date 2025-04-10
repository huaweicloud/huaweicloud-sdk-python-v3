# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HostInfoDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_tag': 'str',
        'host_status': 'str',
        'os_name': 'str',
        'host_name': 'str',
        'container_version': 'str',
        'nics': 'list[Nic]',
        'specification': 'str',
        'npu_details': 'list[NPUDetailsDTO]'
    }

    attribute_map = {
        'host_tag': 'host_tag',
        'host_status': 'host_status',
        'os_name': 'os_name',
        'host_name': 'host_name',
        'container_version': 'container_version',
        'nics': 'nics',
        'specification': 'specification',
        'npu_details': 'npu_details'
    }

    def __init__(self, host_tag=None, host_status=None, os_name=None, host_name=None, container_version=None, nics=None, specification=None, npu_details=None):
        r"""HostInfoDTO

        The model defined in huaweicloud sdk

        :param host_tag: 主机标签DEFAULT|MASTER|SLAVE
        :type host_tag: str
        :param host_status: 主机工作状态(ONLINE|OFFLINE)
        :type host_status: str
        :param os_name: 边缘节点操作系统。例如：Ubuntu 20.04；CentOS 7.9。不同于os_type边缘节点系统类型。
        :type os_name: str
        :param host_name: 边缘节点主机名
        :type host_name: str
        :param container_version: 容器运行时版本
        :type container_version: str
        :param nics: 边缘节点网络网卡信息
        :type nics: list[:class:`huaweicloudsdkiotedge.v2.Nic`]
        :param specification: 网络规格，如4 cores | 3867 MB
        :type specification: str
        :param npu_details: NPU设备详细信息，包括硬件信息和使用情况。
        :type npu_details: list[:class:`huaweicloudsdkiotedge.v2.NPUDetailsDTO`]
        """
        
        

        self._host_tag = None
        self._host_status = None
        self._os_name = None
        self._host_name = None
        self._container_version = None
        self._nics = None
        self._specification = None
        self._npu_details = None
        self.discriminator = None

        if host_tag is not None:
            self.host_tag = host_tag
        if host_status is not None:
            self.host_status = host_status
        if os_name is not None:
            self.os_name = os_name
        if host_name is not None:
            self.host_name = host_name
        if container_version is not None:
            self.container_version = container_version
        if nics is not None:
            self.nics = nics
        if specification is not None:
            self.specification = specification
        if npu_details is not None:
            self.npu_details = npu_details

    @property
    def host_tag(self):
        r"""Gets the host_tag of this HostInfoDTO.

        主机标签DEFAULT|MASTER|SLAVE

        :return: The host_tag of this HostInfoDTO.
        :rtype: str
        """
        return self._host_tag

    @host_tag.setter
    def host_tag(self, host_tag):
        r"""Sets the host_tag of this HostInfoDTO.

        主机标签DEFAULT|MASTER|SLAVE

        :param host_tag: The host_tag of this HostInfoDTO.
        :type host_tag: str
        """
        self._host_tag = host_tag

    @property
    def host_status(self):
        r"""Gets the host_status of this HostInfoDTO.

        主机工作状态(ONLINE|OFFLINE)

        :return: The host_status of this HostInfoDTO.
        :rtype: str
        """
        return self._host_status

    @host_status.setter
    def host_status(self, host_status):
        r"""Sets the host_status of this HostInfoDTO.

        主机工作状态(ONLINE|OFFLINE)

        :param host_status: The host_status of this HostInfoDTO.
        :type host_status: str
        """
        self._host_status = host_status

    @property
    def os_name(self):
        r"""Gets the os_name of this HostInfoDTO.

        边缘节点操作系统。例如：Ubuntu 20.04；CentOS 7.9。不同于os_type边缘节点系统类型。

        :return: The os_name of this HostInfoDTO.
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        r"""Sets the os_name of this HostInfoDTO.

        边缘节点操作系统。例如：Ubuntu 20.04；CentOS 7.9。不同于os_type边缘节点系统类型。

        :param os_name: The os_name of this HostInfoDTO.
        :type os_name: str
        """
        self._os_name = os_name

    @property
    def host_name(self):
        r"""Gets the host_name of this HostInfoDTO.

        边缘节点主机名

        :return: The host_name of this HostInfoDTO.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this HostInfoDTO.

        边缘节点主机名

        :param host_name: The host_name of this HostInfoDTO.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def container_version(self):
        r"""Gets the container_version of this HostInfoDTO.

        容器运行时版本

        :return: The container_version of this HostInfoDTO.
        :rtype: str
        """
        return self._container_version

    @container_version.setter
    def container_version(self, container_version):
        r"""Sets the container_version of this HostInfoDTO.

        容器运行时版本

        :param container_version: The container_version of this HostInfoDTO.
        :type container_version: str
        """
        self._container_version = container_version

    @property
    def nics(self):
        r"""Gets the nics of this HostInfoDTO.

        边缘节点网络网卡信息

        :return: The nics of this HostInfoDTO.
        :rtype: list[:class:`huaweicloudsdkiotedge.v2.Nic`]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        r"""Sets the nics of this HostInfoDTO.

        边缘节点网络网卡信息

        :param nics: The nics of this HostInfoDTO.
        :type nics: list[:class:`huaweicloudsdkiotedge.v2.Nic`]
        """
        self._nics = nics

    @property
    def specification(self):
        r"""Gets the specification of this HostInfoDTO.

        网络规格，如4 cores | 3867 MB

        :return: The specification of this HostInfoDTO.
        :rtype: str
        """
        return self._specification

    @specification.setter
    def specification(self, specification):
        r"""Sets the specification of this HostInfoDTO.

        网络规格，如4 cores | 3867 MB

        :param specification: The specification of this HostInfoDTO.
        :type specification: str
        """
        self._specification = specification

    @property
    def npu_details(self):
        r"""Gets the npu_details of this HostInfoDTO.

        NPU设备详细信息，包括硬件信息和使用情况。

        :return: The npu_details of this HostInfoDTO.
        :rtype: list[:class:`huaweicloudsdkiotedge.v2.NPUDetailsDTO`]
        """
        return self._npu_details

    @npu_details.setter
    def npu_details(self, npu_details):
        r"""Sets the npu_details of this HostInfoDTO.

        NPU设备详细信息，包括硬件信息和使用情况。

        :param npu_details: The npu_details of this HostInfoDTO.
        :type npu_details: list[:class:`huaweicloudsdkiotedge.v2.NPUDetailsDTO`]
        """
        self._npu_details = npu_details

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
        if not isinstance(other, HostInfoDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
