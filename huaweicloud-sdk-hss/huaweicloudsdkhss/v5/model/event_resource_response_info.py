# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventResourceResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'project_id': 'str',
        'enterprise_project_id': 'str',
        'region_name': 'str',
        'vpc_id': 'str',
        'cloud_id': 'str',
        'vm_name': 'str',
        'vm_uuid': 'str',
        'container_id': 'str',
        'image_id': 'str',
        'image_name': 'str',
        'host_attr': 'str',
        'service': 'str',
        'micro_service': 'str',
        'sys_arch': 'str',
        'os_bit': 'str',
        'os_type': 'str',
        'os_name': 'str',
        'os_version': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'project_id': 'project_id',
        'enterprise_project_id': 'enterprise_project_id',
        'region_name': 'region_name',
        'vpc_id': 'vpc_id',
        'cloud_id': 'cloud_id',
        'vm_name': 'vm_name',
        'vm_uuid': 'vm_uuid',
        'container_id': 'container_id',
        'image_id': 'image_id',
        'image_name': 'image_name',
        'host_attr': 'host_attr',
        'service': 'service',
        'micro_service': 'micro_service',
        'sys_arch': 'sys_arch',
        'os_bit': 'os_bit',
        'os_type': 'os_type',
        'os_name': 'os_name',
        'os_version': 'os_version'
    }

    def __init__(self, domain_id=None, project_id=None, enterprise_project_id=None, region_name=None, vpc_id=None, cloud_id=None, vm_name=None, vm_uuid=None, container_id=None, image_id=None, image_name=None, host_attr=None, service=None, micro_service=None, sys_arch=None, os_bit=None, os_type=None, os_name=None, os_version=None):
        """EventResourceResponseInfo

        The model defined in huaweicloud sdk

        :param domain_id: 租户账号ID
        :type domain_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param region_name: Region名称
        :type region_name: str
        :param vpc_id: VPC ID
        :type vpc_id: str
        :param cloud_id: 云主机ID
        :type cloud_id: str
        :param vm_name: 虚拟机名称
        :type vm_name: str
        :param vm_uuid: 虚拟机UUID
        :type vm_uuid: str
        :param container_id: 容器ID
        :type container_id: str
        :param image_id: 镜像ID
        :type image_id: str
        :param image_name: 镜像名称
        :type image_name: str
        :param host_attr: 主机属性
        :type host_attr: str
        :param service: 业务服务
        :type service: str
        :param micro_service: 微服务
        :type micro_service: str
        :param sys_arch: 系统CPU架构
        :type sys_arch: str
        :param os_bit: 操作系统位数
        :type os_bit: str
        :param os_type: 操作系统类型
        :type os_type: str
        :param os_name: 操作系统名称
        :type os_name: str
        :param os_version: 操作系统版本
        :type os_version: str
        """
        
        

        self._domain_id = None
        self._project_id = None
        self._enterprise_project_id = None
        self._region_name = None
        self._vpc_id = None
        self._cloud_id = None
        self._vm_name = None
        self._vm_uuid = None
        self._container_id = None
        self._image_id = None
        self._image_name = None
        self._host_attr = None
        self._service = None
        self._micro_service = None
        self._sys_arch = None
        self._os_bit = None
        self._os_type = None
        self._os_name = None
        self._os_version = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if project_id is not None:
            self.project_id = project_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if region_name is not None:
            self.region_name = region_name
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if cloud_id is not None:
            self.cloud_id = cloud_id
        if vm_name is not None:
            self.vm_name = vm_name
        if vm_uuid is not None:
            self.vm_uuid = vm_uuid
        if container_id is not None:
            self.container_id = container_id
        if image_id is not None:
            self.image_id = image_id
        if image_name is not None:
            self.image_name = image_name
        if host_attr is not None:
            self.host_attr = host_attr
        if service is not None:
            self.service = service
        if micro_service is not None:
            self.micro_service = micro_service
        if sys_arch is not None:
            self.sys_arch = sys_arch
        if os_bit is not None:
            self.os_bit = os_bit
        if os_type is not None:
            self.os_type = os_type
        if os_name is not None:
            self.os_name = os_name
        if os_version is not None:
            self.os_version = os_version

    @property
    def domain_id(self):
        """Gets the domain_id of this EventResourceResponseInfo.

        租户账号ID

        :return: The domain_id of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this EventResourceResponseInfo.

        租户账号ID

        :param domain_id: The domain_id of this EventResourceResponseInfo.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def project_id(self):
        """Gets the project_id of this EventResourceResponseInfo.

        项目ID

        :return: The project_id of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this EventResourceResponseInfo.

        项目ID

        :param project_id: The project_id of this EventResourceResponseInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this EventResourceResponseInfo.

        企业项目ID

        :return: The enterprise_project_id of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this EventResourceResponseInfo.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this EventResourceResponseInfo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def region_name(self):
        """Gets the region_name of this EventResourceResponseInfo.

        Region名称

        :return: The region_name of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this EventResourceResponseInfo.

        Region名称

        :param region_name: The region_name of this EventResourceResponseInfo.
        :type region_name: str
        """
        self._region_name = region_name

    @property
    def vpc_id(self):
        """Gets the vpc_id of this EventResourceResponseInfo.

        VPC ID

        :return: The vpc_id of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this EventResourceResponseInfo.

        VPC ID

        :param vpc_id: The vpc_id of this EventResourceResponseInfo.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def cloud_id(self):
        """Gets the cloud_id of this EventResourceResponseInfo.

        云主机ID

        :return: The cloud_id of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._cloud_id

    @cloud_id.setter
    def cloud_id(self, cloud_id):
        """Sets the cloud_id of this EventResourceResponseInfo.

        云主机ID

        :param cloud_id: The cloud_id of this EventResourceResponseInfo.
        :type cloud_id: str
        """
        self._cloud_id = cloud_id

    @property
    def vm_name(self):
        """Gets the vm_name of this EventResourceResponseInfo.

        虚拟机名称

        :return: The vm_name of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._vm_name

    @vm_name.setter
    def vm_name(self, vm_name):
        """Sets the vm_name of this EventResourceResponseInfo.

        虚拟机名称

        :param vm_name: The vm_name of this EventResourceResponseInfo.
        :type vm_name: str
        """
        self._vm_name = vm_name

    @property
    def vm_uuid(self):
        """Gets the vm_uuid of this EventResourceResponseInfo.

        虚拟机UUID

        :return: The vm_uuid of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._vm_uuid

    @vm_uuid.setter
    def vm_uuid(self, vm_uuid):
        """Sets the vm_uuid of this EventResourceResponseInfo.

        虚拟机UUID

        :param vm_uuid: The vm_uuid of this EventResourceResponseInfo.
        :type vm_uuid: str
        """
        self._vm_uuid = vm_uuid

    @property
    def container_id(self):
        """Gets the container_id of this EventResourceResponseInfo.

        容器ID

        :return: The container_id of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        """Sets the container_id of this EventResourceResponseInfo.

        容器ID

        :param container_id: The container_id of this EventResourceResponseInfo.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def image_id(self):
        """Gets the image_id of this EventResourceResponseInfo.

        镜像ID

        :return: The image_id of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this EventResourceResponseInfo.

        镜像ID

        :param image_id: The image_id of this EventResourceResponseInfo.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_name(self):
        """Gets the image_name of this EventResourceResponseInfo.

        镜像名称

        :return: The image_name of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this EventResourceResponseInfo.

        镜像名称

        :param image_name: The image_name of this EventResourceResponseInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def host_attr(self):
        """Gets the host_attr of this EventResourceResponseInfo.

        主机属性

        :return: The host_attr of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._host_attr

    @host_attr.setter
    def host_attr(self, host_attr):
        """Sets the host_attr of this EventResourceResponseInfo.

        主机属性

        :param host_attr: The host_attr of this EventResourceResponseInfo.
        :type host_attr: str
        """
        self._host_attr = host_attr

    @property
    def service(self):
        """Gets the service of this EventResourceResponseInfo.

        业务服务

        :return: The service of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this EventResourceResponseInfo.

        业务服务

        :param service: The service of this EventResourceResponseInfo.
        :type service: str
        """
        self._service = service

    @property
    def micro_service(self):
        """Gets the micro_service of this EventResourceResponseInfo.

        微服务

        :return: The micro_service of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._micro_service

    @micro_service.setter
    def micro_service(self, micro_service):
        """Sets the micro_service of this EventResourceResponseInfo.

        微服务

        :param micro_service: The micro_service of this EventResourceResponseInfo.
        :type micro_service: str
        """
        self._micro_service = micro_service

    @property
    def sys_arch(self):
        """Gets the sys_arch of this EventResourceResponseInfo.

        系统CPU架构

        :return: The sys_arch of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._sys_arch

    @sys_arch.setter
    def sys_arch(self, sys_arch):
        """Sets the sys_arch of this EventResourceResponseInfo.

        系统CPU架构

        :param sys_arch: The sys_arch of this EventResourceResponseInfo.
        :type sys_arch: str
        """
        self._sys_arch = sys_arch

    @property
    def os_bit(self):
        """Gets the os_bit of this EventResourceResponseInfo.

        操作系统位数

        :return: The os_bit of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._os_bit

    @os_bit.setter
    def os_bit(self, os_bit):
        """Sets the os_bit of this EventResourceResponseInfo.

        操作系统位数

        :param os_bit: The os_bit of this EventResourceResponseInfo.
        :type os_bit: str
        """
        self._os_bit = os_bit

    @property
    def os_type(self):
        """Gets the os_type of this EventResourceResponseInfo.

        操作系统类型

        :return: The os_type of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this EventResourceResponseInfo.

        操作系统类型

        :param os_type: The os_type of this EventResourceResponseInfo.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def os_name(self):
        """Gets the os_name of this EventResourceResponseInfo.

        操作系统名称

        :return: The os_name of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        """Sets the os_name of this EventResourceResponseInfo.

        操作系统名称

        :param os_name: The os_name of this EventResourceResponseInfo.
        :type os_name: str
        """
        self._os_name = os_name

    @property
    def os_version(self):
        """Gets the os_version of this EventResourceResponseInfo.

        操作系统版本

        :return: The os_version of this EventResourceResponseInfo.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this EventResourceResponseInfo.

        操作系统版本

        :param os_version: The os_version of this EventResourceResponseInfo.
        :type os_version: str
        """
        self._os_version = os_version

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
        if not isinstance(other, EventResourceResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
