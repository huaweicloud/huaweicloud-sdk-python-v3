# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Share:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'availability_zone': 'str',
        'description': 'str',
        'enterprise_project_id': 'str',
        'metadata': 'Metadata',
        'name': 'str',
        'security_group_id': 'str',
        'share_proto': 'str',
        'share_type': 'str',
        'size': 'int',
        'subnet_id': 'str',
        'vpc_id': 'str',
        'backup_id': 'str',
        'tags': 'list[ResourceTag]'
    }

    attribute_map = {
        'availability_zone': 'availability_zone',
        'description': 'description',
        'enterprise_project_id': 'enterprise_project_id',
        'metadata': 'metadata',
        'name': 'name',
        'security_group_id': 'security_group_id',
        'share_proto': 'share_proto',
        'share_type': 'share_type',
        'size': 'size',
        'subnet_id': 'subnet_id',
        'vpc_id': 'vpc_id',
        'backup_id': 'backup_id',
        'tags': 'tags'
    }

    def __init__(self, availability_zone=None, description=None, enterprise_project_id=None, metadata=None, name=None, security_group_id=None, share_proto=None, share_type=None, size=None, subnet_id=None, vpc_id=None, backup_id=None, tags=None):
        r"""Share

        The model defined in huaweicloud sdk

        :param availability_zone: 文件系统所在可用区(az)的编码
        :type availability_zone: str
        :param description: 文件系统描述信息，长度为0~255。当前不支持。
        :type description: str
        :param enterprise_project_id: 创建文件系统时，给文件系统绑定的企业项目ID。
        :type enterprise_project_id: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdksfsturbo.v1.Metadata`
        :param name: SFS Turbo文件系统的名称。长度为4~64位，必须以字母开头，可以包含字母、数字、中划线、下划线，不能包含其他的特殊字符，不区分大小写。
        :type name: str
        :param security_group_id: 用户在某一区域下的安全组ID。
        :type security_group_id: str
        :param share_proto: - NFS（Network File System），即网络文件系统。一种使用于分散式文件系统的协议，通过网络让不同的机器、不同的操作系统能够彼此分享数据。Linux系统建议使用NFS协议类型的文件系统。 - CIFS（Common Internet File System），通用Internet文件系统，是一种网络文件系统访问协议。CIFS协议是SMB协议的方言（定义特定版本的协议的消息数据包集称为方言），CIFS协议也是公共的或开放的SMB协议版本，它使程序可以访问远程Internet计算机上的文件并要求此计算机提供服务。通过CIFS协议，可实现Windows系统主机之间的网络文件共享。CIFS类型的文件系统不支持使用Linux操作系统的云服务器进行挂载。Windows系统建议使用CIFS协议类型的文件系统。 
        :type share_proto: str
        :param share_type: 文件系统类型，有效值为STANDARD或者PERFORMANCE。当文件系统正在创建时，该字段不返回。  - SFS Turbo上一代文件系统规格类型：标准型和标准型增强版填写STANDARD，性能型和性能型增强版填写PERFORMANCE。  - 20MB/s/TiB、40MB/s/TiB、125MB/s/TiB、250MB/s/TiB、500MB/s/TiB、1000MB/TiB：不校验该字段，填写STANDARD或者PERFORMANCE。  - HPC缓存型：不校验该字段，填写STANDARD或者PERFORMANCE。 
        :type share_type: str
        :param size: - SFS Turbo上一代文件系统规格类型-文件系统容量：取值范围为500~32768，单位为GiB。  - SFS Turbo上一代文件系统规格类型-增强版文件系统：在“metadata”字段中设置了expand_type&#x3D;\&quot;bandwidth\&quot;，则容量范围为10240~327680，单位为GiB。  - 20MB/s/TiB：在“metadata”字段中设置了expand_type&#x3D;\&quot;hpc\&quot;、hpc_bw&#x3D;\&quot;20M\&quot;，则容量范围为3686~1048576，单位为GiB。容量必须为1.2TiB的倍数，换算为GiB后需要向下取整。如3.6TiB-&gt;3686GiB, 4.8TiB-&gt;4915GiB，8.4TiB-&gt;8601GiB。  - 40MB/s/TiB：在“metadata”字段中设置了expand_type&#x3D;\&quot;hpc\&quot;、hpc_bw&#x3D;\&quot;40M\&quot;，则容量范围为1228~1048576，单位为GiB。容量必须为1.2TiB的倍数，换算为GiB后需要向下取整。如3.6TiB-&gt;3686GiB, 4.8TiB-&gt;4915GiB，8.4TiB-&gt;8601GiB。  - 125MB/s/TiB：在“metadata”字段中设置了expand_type&#x3D;\&quot;hpc\&quot;、hpc_bw&#x3D;\&quot;125M\&quot;，则容量范围为1228~1048576，单位为GiB。容量必须为1.2TiB的倍数，换算为GiB后需要向下取整。如3.6TiB-&gt;3686GiB, 4.8TiB-&gt;4915GiB，8.4TiB-&gt;8601GiB。  - 250MB/s/TiB：在“metadata”字段中设置了expand_type&#x3D;\&quot;hpc\&quot;、hpc_bw&#x3D;\&quot;250M\&quot;，则容量范围为1228~1048576，单位为GiB。容量必须为1.2TiB的倍数，换算为GiB后需要向下取整。如3.6TiB-&gt;3686GiB, 4.8TiB-&gt;4915GiB，8.4TiB-&gt;8601GiB。  - 500MB/s/TiB：在“metadata”字段中设置了expand_type&#x3D;\&quot;hpc\&quot;、hpc_bw&#x3D;\&quot;500M\&quot;，则容量范围为1228~1048576，单位为GiB。容量必须为1.2TiB的倍数，换算为GiB后需要向下取整。如3.6TiB-&gt;3686GiB, 4.8TiB-&gt;4915GiB，8.4TiB-&gt;8601GiB。  - 1000MB/s/TiB：在“metadata”字段中设置了expand_type&#x3D;\&quot;hpc\&quot;、hpc_bw&#x3D;\&quot;1000M\&quot;，则容量范围为1228~1048576，单位为GiB。容量必须为1.2TiB的倍数，换算为GiB后需要向下取整。如3.6TiB-&gt;3686GiB, 4.8TiB-&gt;4915GiB，8.4TiB-&gt;8601GiB。  - HPC缓存型文件系统：在“metadata”字段中设置了expand_type&#x3D;\&quot;hpc_cache\&quot;，则容量范围为4096~1048576，单位为GiB。不同带宽，起步容量不一样，步长均为1TiB。如2GB/s带宽，起步容量为4TiB，即4096GiB；4GB/s带宽，起步容量为8TiB，即8192GiB；8GB/s带宽，起步容量为16TiB，即16384GiB。 
        :type size: int
        :param subnet_id: 用户在VPC下面的子网的网络ID。
        :type subnet_id: str
        :param vpc_id: 用户在某一区域下的VPC ID。
        :type vpc_id: str
        :param backup_id: 备份ID，从备份创建文件系统时为必选。
        :type backup_id: str
        :param tags: tag标签的列表。
        :type tags: list[:class:`huaweicloudsdksfsturbo.v1.ResourceTag`]
        """
        
        

        self._availability_zone = None
        self._description = None
        self._enterprise_project_id = None
        self._metadata = None
        self._name = None
        self._security_group_id = None
        self._share_proto = None
        self._share_type = None
        self._size = None
        self._subnet_id = None
        self._vpc_id = None
        self._backup_id = None
        self._tags = None
        self.discriminator = None

        self.availability_zone = availability_zone
        if description is not None:
            self.description = description
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if metadata is not None:
            self.metadata = metadata
        self.name = name
        self.security_group_id = security_group_id
        self.share_proto = share_proto
        self.share_type = share_type
        self.size = size
        self.subnet_id = subnet_id
        self.vpc_id = vpc_id
        if backup_id is not None:
            self.backup_id = backup_id
        if tags is not None:
            self.tags = tags

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this Share.

        文件系统所在可用区(az)的编码

        :return: The availability_zone of this Share.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this Share.

        文件系统所在可用区(az)的编码

        :param availability_zone: The availability_zone of this Share.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def description(self):
        r"""Gets the description of this Share.

        文件系统描述信息，长度为0~255。当前不支持。

        :return: The description of this Share.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Share.

        文件系统描述信息，长度为0~255。当前不支持。

        :param description: The description of this Share.
        :type description: str
        """
        self._description = description

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this Share.

        创建文件系统时，给文件系统绑定的企业项目ID。

        :return: The enterprise_project_id of this Share.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this Share.

        创建文件系统时，给文件系统绑定的企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this Share.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def metadata(self):
        r"""Gets the metadata of this Share.

        :return: The metadata of this Share.
        :rtype: :class:`huaweicloudsdksfsturbo.v1.Metadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this Share.

        :param metadata: The metadata of this Share.
        :type metadata: :class:`huaweicloudsdksfsturbo.v1.Metadata`
        """
        self._metadata = metadata

    @property
    def name(self):
        r"""Gets the name of this Share.

        SFS Turbo文件系统的名称。长度为4~64位，必须以字母开头，可以包含字母、数字、中划线、下划线，不能包含其他的特殊字符，不区分大小写。

        :return: The name of this Share.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Share.

        SFS Turbo文件系统的名称。长度为4~64位，必须以字母开头，可以包含字母、数字、中划线、下划线，不能包含其他的特殊字符，不区分大小写。

        :param name: The name of this Share.
        :type name: str
        """
        self._name = name

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this Share.

        用户在某一区域下的安全组ID。

        :return: The security_group_id of this Share.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this Share.

        用户在某一区域下的安全组ID。

        :param security_group_id: The security_group_id of this Share.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def share_proto(self):
        r"""Gets the share_proto of this Share.

        - NFS（Network File System），即网络文件系统。一种使用于分散式文件系统的协议，通过网络让不同的机器、不同的操作系统能够彼此分享数据。Linux系统建议使用NFS协议类型的文件系统。 - CIFS（Common Internet File System），通用Internet文件系统，是一种网络文件系统访问协议。CIFS协议是SMB协议的方言（定义特定版本的协议的消息数据包集称为方言），CIFS协议也是公共的或开放的SMB协议版本，它使程序可以访问远程Internet计算机上的文件并要求此计算机提供服务。通过CIFS协议，可实现Windows系统主机之间的网络文件共享。CIFS类型的文件系统不支持使用Linux操作系统的云服务器进行挂载。Windows系统建议使用CIFS协议类型的文件系统。 

        :return: The share_proto of this Share.
        :rtype: str
        """
        return self._share_proto

    @share_proto.setter
    def share_proto(self, share_proto):
        r"""Sets the share_proto of this Share.

        - NFS（Network File System），即网络文件系统。一种使用于分散式文件系统的协议，通过网络让不同的机器、不同的操作系统能够彼此分享数据。Linux系统建议使用NFS协议类型的文件系统。 - CIFS（Common Internet File System），通用Internet文件系统，是一种网络文件系统访问协议。CIFS协议是SMB协议的方言（定义特定版本的协议的消息数据包集称为方言），CIFS协议也是公共的或开放的SMB协议版本，它使程序可以访问远程Internet计算机上的文件并要求此计算机提供服务。通过CIFS协议，可实现Windows系统主机之间的网络文件共享。CIFS类型的文件系统不支持使用Linux操作系统的云服务器进行挂载。Windows系统建议使用CIFS协议类型的文件系统。 

        :param share_proto: The share_proto of this Share.
        :type share_proto: str
        """
        self._share_proto = share_proto

    @property
    def share_type(self):
        r"""Gets the share_type of this Share.

        文件系统类型，有效值为STANDARD或者PERFORMANCE。当文件系统正在创建时，该字段不返回。  - SFS Turbo上一代文件系统规格类型：标准型和标准型增强版填写STANDARD，性能型和性能型增强版填写PERFORMANCE。  - 20MB/s/TiB、40MB/s/TiB、125MB/s/TiB、250MB/s/TiB、500MB/s/TiB、1000MB/TiB：不校验该字段，填写STANDARD或者PERFORMANCE。  - HPC缓存型：不校验该字段，填写STANDARD或者PERFORMANCE。 

        :return: The share_type of this Share.
        :rtype: str
        """
        return self._share_type

    @share_type.setter
    def share_type(self, share_type):
        r"""Sets the share_type of this Share.

        文件系统类型，有效值为STANDARD或者PERFORMANCE。当文件系统正在创建时，该字段不返回。  - SFS Turbo上一代文件系统规格类型：标准型和标准型增强版填写STANDARD，性能型和性能型增强版填写PERFORMANCE。  - 20MB/s/TiB、40MB/s/TiB、125MB/s/TiB、250MB/s/TiB、500MB/s/TiB、1000MB/TiB：不校验该字段，填写STANDARD或者PERFORMANCE。  - HPC缓存型：不校验该字段，填写STANDARD或者PERFORMANCE。 

        :param share_type: The share_type of this Share.
        :type share_type: str
        """
        self._share_type = share_type

    @property
    def size(self):
        r"""Gets the size of this Share.

        - SFS Turbo上一代文件系统规格类型-文件系统容量：取值范围为500~32768，单位为GiB。  - SFS Turbo上一代文件系统规格类型-增强版文件系统：在“metadata”字段中设置了expand_type=\"bandwidth\"，则容量范围为10240~327680，单位为GiB。  - 20MB/s/TiB：在“metadata”字段中设置了expand_type=\"hpc\"、hpc_bw=\"20M\"，则容量范围为3686~1048576，单位为GiB。容量必须为1.2TiB的倍数，换算为GiB后需要向下取整。如3.6TiB->3686GiB, 4.8TiB->4915GiB，8.4TiB->8601GiB。  - 40MB/s/TiB：在“metadata”字段中设置了expand_type=\"hpc\"、hpc_bw=\"40M\"，则容量范围为1228~1048576，单位为GiB。容量必须为1.2TiB的倍数，换算为GiB后需要向下取整。如3.6TiB->3686GiB, 4.8TiB->4915GiB，8.4TiB->8601GiB。  - 125MB/s/TiB：在“metadata”字段中设置了expand_type=\"hpc\"、hpc_bw=\"125M\"，则容量范围为1228~1048576，单位为GiB。容量必须为1.2TiB的倍数，换算为GiB后需要向下取整。如3.6TiB->3686GiB, 4.8TiB->4915GiB，8.4TiB->8601GiB。  - 250MB/s/TiB：在“metadata”字段中设置了expand_type=\"hpc\"、hpc_bw=\"250M\"，则容量范围为1228~1048576，单位为GiB。容量必须为1.2TiB的倍数，换算为GiB后需要向下取整。如3.6TiB->3686GiB, 4.8TiB->4915GiB，8.4TiB->8601GiB。  - 500MB/s/TiB：在“metadata”字段中设置了expand_type=\"hpc\"、hpc_bw=\"500M\"，则容量范围为1228~1048576，单位为GiB。容量必须为1.2TiB的倍数，换算为GiB后需要向下取整。如3.6TiB->3686GiB, 4.8TiB->4915GiB，8.4TiB->8601GiB。  - 1000MB/s/TiB：在“metadata”字段中设置了expand_type=\"hpc\"、hpc_bw=\"1000M\"，则容量范围为1228~1048576，单位为GiB。容量必须为1.2TiB的倍数，换算为GiB后需要向下取整。如3.6TiB->3686GiB, 4.8TiB->4915GiB，8.4TiB->8601GiB。  - HPC缓存型文件系统：在“metadata”字段中设置了expand_type=\"hpc_cache\"，则容量范围为4096~1048576，单位为GiB。不同带宽，起步容量不一样，步长均为1TiB。如2GB/s带宽，起步容量为4TiB，即4096GiB；4GB/s带宽，起步容量为8TiB，即8192GiB；8GB/s带宽，起步容量为16TiB，即16384GiB。 

        :return: The size of this Share.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this Share.

        - SFS Turbo上一代文件系统规格类型-文件系统容量：取值范围为500~32768，单位为GiB。  - SFS Turbo上一代文件系统规格类型-增强版文件系统：在“metadata”字段中设置了expand_type=\"bandwidth\"，则容量范围为10240~327680，单位为GiB。  - 20MB/s/TiB：在“metadata”字段中设置了expand_type=\"hpc\"、hpc_bw=\"20M\"，则容量范围为3686~1048576，单位为GiB。容量必须为1.2TiB的倍数，换算为GiB后需要向下取整。如3.6TiB->3686GiB, 4.8TiB->4915GiB，8.4TiB->8601GiB。  - 40MB/s/TiB：在“metadata”字段中设置了expand_type=\"hpc\"、hpc_bw=\"40M\"，则容量范围为1228~1048576，单位为GiB。容量必须为1.2TiB的倍数，换算为GiB后需要向下取整。如3.6TiB->3686GiB, 4.8TiB->4915GiB，8.4TiB->8601GiB。  - 125MB/s/TiB：在“metadata”字段中设置了expand_type=\"hpc\"、hpc_bw=\"125M\"，则容量范围为1228~1048576，单位为GiB。容量必须为1.2TiB的倍数，换算为GiB后需要向下取整。如3.6TiB->3686GiB, 4.8TiB->4915GiB，8.4TiB->8601GiB。  - 250MB/s/TiB：在“metadata”字段中设置了expand_type=\"hpc\"、hpc_bw=\"250M\"，则容量范围为1228~1048576，单位为GiB。容量必须为1.2TiB的倍数，换算为GiB后需要向下取整。如3.6TiB->3686GiB, 4.8TiB->4915GiB，8.4TiB->8601GiB。  - 500MB/s/TiB：在“metadata”字段中设置了expand_type=\"hpc\"、hpc_bw=\"500M\"，则容量范围为1228~1048576，单位为GiB。容量必须为1.2TiB的倍数，换算为GiB后需要向下取整。如3.6TiB->3686GiB, 4.8TiB->4915GiB，8.4TiB->8601GiB。  - 1000MB/s/TiB：在“metadata”字段中设置了expand_type=\"hpc\"、hpc_bw=\"1000M\"，则容量范围为1228~1048576，单位为GiB。容量必须为1.2TiB的倍数，换算为GiB后需要向下取整。如3.6TiB->3686GiB, 4.8TiB->4915GiB，8.4TiB->8601GiB。  - HPC缓存型文件系统：在“metadata”字段中设置了expand_type=\"hpc_cache\"，则容量范围为4096~1048576，单位为GiB。不同带宽，起步容量不一样，步长均为1TiB。如2GB/s带宽，起步容量为4TiB，即4096GiB；4GB/s带宽，起步容量为8TiB，即8192GiB；8GB/s带宽，起步容量为16TiB，即16384GiB。 

        :param size: The size of this Share.
        :type size: int
        """
        self._size = size

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this Share.

        用户在VPC下面的子网的网络ID。

        :return: The subnet_id of this Share.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this Share.

        用户在VPC下面的子网的网络ID。

        :param subnet_id: The subnet_id of this Share.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this Share.

        用户在某一区域下的VPC ID。

        :return: The vpc_id of this Share.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this Share.

        用户在某一区域下的VPC ID。

        :param vpc_id: The vpc_id of this Share.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def backup_id(self):
        r"""Gets the backup_id of this Share.

        备份ID，从备份创建文件系统时为必选。

        :return: The backup_id of this Share.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        r"""Sets the backup_id of this Share.

        备份ID，从备份创建文件系统时为必选。

        :param backup_id: The backup_id of this Share.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def tags(self):
        r"""Gets the tags of this Share.

        tag标签的列表。

        :return: The tags of this Share.
        :rtype: list[:class:`huaweicloudsdksfsturbo.v1.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this Share.

        tag标签的列表。

        :param tags: The tags of this Share.
        :type tags: list[:class:`huaweicloudsdksfsturbo.v1.ResourceTag`]
        """
        self._tags = tags

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
        if not isinstance(other, Share):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
