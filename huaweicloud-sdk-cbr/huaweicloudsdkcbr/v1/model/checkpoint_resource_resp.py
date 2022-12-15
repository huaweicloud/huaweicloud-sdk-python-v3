# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckpointResourceResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'extra_info': 'str',
        'id': 'str',
        'name': 'str',
        'protect_status': 'str',
        'resource_size': 'str',
        'type': 'str',
        'backup_size': 'str',
        'backup_count': 'str'
    }

    attribute_map = {
        'extra_info': 'extra_info',
        'id': 'id',
        'name': 'name',
        'protect_status': 'protect_status',
        'resource_size': 'resource_size',
        'type': 'type',
        'backup_size': 'backup_size',
        'backup_count': 'backup_count'
    }

    def __init__(self, extra_info=None, id=None, name=None, protect_status=None, resource_size=None, type=None, backup_size=None, backup_count=None):
        """CheckpointResourceResp

        The model defined in huaweicloud sdk

        :param extra_info: 资源附加信息
        :type extra_info: str
        :param id: 待备份资源id
        :type id: str
        :param name: 待备份资源名称
        :type name: str
        :param protect_status: 保护状态。available（可用），error（错误），protecting（备份中），restoring（恢复中），removing（删除中）。
        :type protect_status: str
        :param resource_size: 资源已分配容量,单位为GB
        :type resource_size: str
        :param type: 待备份资源的类型: OS::Nova::Server, OS::Cinder::Volume, OS::Ironic::BareMetalServer, OS::Native::Server, OS::Sfs::Turbo, OS::Workspace::DesktopV2
        :type type: str
        :param backup_size: 副本大小
        :type backup_size: str
        :param backup_count: 副本数量
        :type backup_count: str
        """
        
        

        self._extra_info = None
        self._id = None
        self._name = None
        self._protect_status = None
        self._resource_size = None
        self._type = None
        self._backup_size = None
        self._backup_count = None
        self.discriminator = None

        if extra_info is not None:
            self.extra_info = extra_info
        self.id = id
        self.name = name
        if protect_status is not None:
            self.protect_status = protect_status
        if resource_size is not None:
            self.resource_size = resource_size
        self.type = type
        if backup_size is not None:
            self.backup_size = backup_size
        if backup_count is not None:
            self.backup_count = backup_count

    @property
    def extra_info(self):
        """Gets the extra_info of this CheckpointResourceResp.

        资源附加信息

        :return: The extra_info of this CheckpointResourceResp.
        :rtype: str
        """
        return self._extra_info

    @extra_info.setter
    def extra_info(self, extra_info):
        """Sets the extra_info of this CheckpointResourceResp.

        资源附加信息

        :param extra_info: The extra_info of this CheckpointResourceResp.
        :type extra_info: str
        """
        self._extra_info = extra_info

    @property
    def id(self):
        """Gets the id of this CheckpointResourceResp.

        待备份资源id

        :return: The id of this CheckpointResourceResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CheckpointResourceResp.

        待备份资源id

        :param id: The id of this CheckpointResourceResp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CheckpointResourceResp.

        待备份资源名称

        :return: The name of this CheckpointResourceResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CheckpointResourceResp.

        待备份资源名称

        :param name: The name of this CheckpointResourceResp.
        :type name: str
        """
        self._name = name

    @property
    def protect_status(self):
        """Gets the protect_status of this CheckpointResourceResp.

        保护状态。available（可用），error（错误），protecting（备份中），restoring（恢复中），removing（删除中）。

        :return: The protect_status of this CheckpointResourceResp.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        """Sets the protect_status of this CheckpointResourceResp.

        保护状态。available（可用），error（错误），protecting（备份中），restoring（恢复中），removing（删除中）。

        :param protect_status: The protect_status of this CheckpointResourceResp.
        :type protect_status: str
        """
        self._protect_status = protect_status

    @property
    def resource_size(self):
        """Gets the resource_size of this CheckpointResourceResp.

        资源已分配容量,单位为GB

        :return: The resource_size of this CheckpointResourceResp.
        :rtype: str
        """
        return self._resource_size

    @resource_size.setter
    def resource_size(self, resource_size):
        """Sets the resource_size of this CheckpointResourceResp.

        资源已分配容量,单位为GB

        :param resource_size: The resource_size of this CheckpointResourceResp.
        :type resource_size: str
        """
        self._resource_size = resource_size

    @property
    def type(self):
        """Gets the type of this CheckpointResourceResp.

        待备份资源的类型: OS::Nova::Server, OS::Cinder::Volume, OS::Ironic::BareMetalServer, OS::Native::Server, OS::Sfs::Turbo, OS::Workspace::DesktopV2

        :return: The type of this CheckpointResourceResp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CheckpointResourceResp.

        待备份资源的类型: OS::Nova::Server, OS::Cinder::Volume, OS::Ironic::BareMetalServer, OS::Native::Server, OS::Sfs::Turbo, OS::Workspace::DesktopV2

        :param type: The type of this CheckpointResourceResp.
        :type type: str
        """
        self._type = type

    @property
    def backup_size(self):
        """Gets the backup_size of this CheckpointResourceResp.

        副本大小

        :return: The backup_size of this CheckpointResourceResp.
        :rtype: str
        """
        return self._backup_size

    @backup_size.setter
    def backup_size(self, backup_size):
        """Sets the backup_size of this CheckpointResourceResp.

        副本大小

        :param backup_size: The backup_size of this CheckpointResourceResp.
        :type backup_size: str
        """
        self._backup_size = backup_size

    @property
    def backup_count(self):
        """Gets the backup_count of this CheckpointResourceResp.

        副本数量

        :return: The backup_count of this CheckpointResourceResp.
        :rtype: str
        """
        return self._backup_count

    @backup_count.setter
    def backup_count(self, backup_count):
        """Sets the backup_count of this CheckpointResourceResp.

        副本数量

        :param backup_count: The backup_count of this CheckpointResourceResp.
        :type backup_count: str
        """
        self._backup_count = backup_count

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
        if not isinstance(other, CheckpointResourceResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
