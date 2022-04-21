# coding: utf-8

import re
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
        'backup_id': 'str'
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
        'backup_id': 'backup_id'
    }

    def __init__(self, availability_zone=None, description=None, enterprise_project_id=None, metadata=None, name=None, security_group_id=None, share_proto=None, share_type=None, size=None, subnet_id=None, vpc_id=None, backup_id=None):
        """Share

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
        :param share_proto: 文件系统共享协议，有效值为NFS。NFS（Network File System），即网络文件系统。一种使用于分散式文件系统的协议，通过网络让不同的机器、不同的操作系统能够彼此分享数据。
        :type share_proto: str
        :param share_type: 文件系统类型，有效值为STANDARD或者PERFORMANCE。
        :type share_type: str
        :param size: 普通文件系统容量，单位GB，取值范围500~32768。 增强型文件系统，即在“metadata”字段中设置了expand_type字段，则容量范围是10240~327680
        :type size: int
        :param subnet_id: 用户在VPC下面的子网的网络ID。
        :type subnet_id: str
        :param vpc_id: 用户在某一区域下的VPC ID。
        :type vpc_id: str
        :param backup_id: 备份ID，从备份创建文件系统时为必选。
        :type backup_id: str
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

    @property
    def availability_zone(self):
        """Gets the availability_zone of this Share.

        文件系统所在可用区(az)的编码

        :return: The availability_zone of this Share.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this Share.

        文件系统所在可用区(az)的编码

        :param availability_zone: The availability_zone of this Share.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def description(self):
        """Gets the description of this Share.

        文件系统描述信息，长度为0~255。当前不支持。

        :return: The description of this Share.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Share.

        文件系统描述信息，长度为0~255。当前不支持。

        :param description: The description of this Share.
        :type description: str
        """
        self._description = description

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this Share.

        创建文件系统时，给文件系统绑定的企业项目ID。

        :return: The enterprise_project_id of this Share.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this Share.

        创建文件系统时，给文件系统绑定的企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this Share.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def metadata(self):
        """Gets the metadata of this Share.


        :return: The metadata of this Share.
        :rtype: :class:`huaweicloudsdksfsturbo.v1.Metadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Share.


        :param metadata: The metadata of this Share.
        :type metadata: :class:`huaweicloudsdksfsturbo.v1.Metadata`
        """
        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this Share.

        SFS Turbo文件系统的名称。长度为4~64位，必须以字母开头，可以包含字母、数字、中划线、下划线，不能包含其他的特殊字符，不区分大小写。

        :return: The name of this Share.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Share.

        SFS Turbo文件系统的名称。长度为4~64位，必须以字母开头，可以包含字母、数字、中划线、下划线，不能包含其他的特殊字符，不区分大小写。

        :param name: The name of this Share.
        :type name: str
        """
        self._name = name

    @property
    def security_group_id(self):
        """Gets the security_group_id of this Share.

        用户在某一区域下的安全组ID。

        :return: The security_group_id of this Share.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this Share.

        用户在某一区域下的安全组ID。

        :param security_group_id: The security_group_id of this Share.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def share_proto(self):
        """Gets the share_proto of this Share.

        文件系统共享协议，有效值为NFS。NFS（Network File System），即网络文件系统。一种使用于分散式文件系统的协议，通过网络让不同的机器、不同的操作系统能够彼此分享数据。

        :return: The share_proto of this Share.
        :rtype: str
        """
        return self._share_proto

    @share_proto.setter
    def share_proto(self, share_proto):
        """Sets the share_proto of this Share.

        文件系统共享协议，有效值为NFS。NFS（Network File System），即网络文件系统。一种使用于分散式文件系统的协议，通过网络让不同的机器、不同的操作系统能够彼此分享数据。

        :param share_proto: The share_proto of this Share.
        :type share_proto: str
        """
        self._share_proto = share_proto

    @property
    def share_type(self):
        """Gets the share_type of this Share.

        文件系统类型，有效值为STANDARD或者PERFORMANCE。

        :return: The share_type of this Share.
        :rtype: str
        """
        return self._share_type

    @share_type.setter
    def share_type(self, share_type):
        """Sets the share_type of this Share.

        文件系统类型，有效值为STANDARD或者PERFORMANCE。

        :param share_type: The share_type of this Share.
        :type share_type: str
        """
        self._share_type = share_type

    @property
    def size(self):
        """Gets the size of this Share.

        普通文件系统容量，单位GB，取值范围500~32768。 增强型文件系统，即在“metadata”字段中设置了expand_type字段，则容量范围是10240~327680

        :return: The size of this Share.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Share.

        普通文件系统容量，单位GB，取值范围500~32768。 增强型文件系统，即在“metadata”字段中设置了expand_type字段，则容量范围是10240~327680

        :param size: The size of this Share.
        :type size: int
        """
        self._size = size

    @property
    def subnet_id(self):
        """Gets the subnet_id of this Share.

        用户在VPC下面的子网的网络ID。

        :return: The subnet_id of this Share.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this Share.

        用户在VPC下面的子网的网络ID。

        :param subnet_id: The subnet_id of this Share.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this Share.

        用户在某一区域下的VPC ID。

        :return: The vpc_id of this Share.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this Share.

        用户在某一区域下的VPC ID。

        :param vpc_id: The vpc_id of this Share.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def backup_id(self):
        """Gets the backup_id of this Share.

        备份ID，从备份创建文件系统时为必选。

        :return: The backup_id of this Share.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """Sets the backup_id of this Share.

        备份ID，从备份创建文件系统时为必选。

        :param backup_id: The backup_id of this Share.
        :type backup_id: str
        """
        self._backup_id = backup_id

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
