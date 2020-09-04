# coding: utf-8

import pprint
import re

import six





class ResourceResp:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'extra_info': 'ResourceExtraInfo',
        'id': 'str',
        'name': 'str',
        'protect_status': 'str',
        'size': 'int',
        'type': 'str',
        'backup_size': 'int',
        'backup_count': 'int'
    }

    attribute_map = {
        'extra_info': 'extra_info',
        'id': 'id',
        'name': 'name',
        'protect_status': 'protect_status',
        'size': 'size',
        'type': 'type',
        'backup_size': 'backup_size',
        'backup_count': 'backup_count'
    }

    def __init__(self, extra_info=None, id=None, name=None, protect_status=None, size=None, type=None, backup_size=None, backup_count=None):
        """ResourceResp - a model defined in huaweicloud sdk"""
        
        

        self._extra_info = None
        self._id = None
        self._name = None
        self._protect_status = None
        self._size = None
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
        if size is not None:
            self.size = size
        self.type = type
        if backup_size is not None:
            self.backup_size = backup_size
        if backup_count is not None:
            self.backup_count = backup_count

    @property
    def extra_info(self):
        """Gets the extra_info of this ResourceResp.


        :return: The extra_info of this ResourceResp.
        :rtype: ResourceExtraInfo
        """
        return self._extra_info

    @extra_info.setter
    def extra_info(self, extra_info):
        """Sets the extra_info of this ResourceResp.


        :param extra_info: The extra_info of this ResourceResp.
        :type: ResourceExtraInfo
        """
        self._extra_info = extra_info

    @property
    def id(self):
        """Gets the id of this ResourceResp.

        待备份资源id

        :return: The id of this ResourceResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResourceResp.

        待备份资源id

        :param id: The id of this ResourceResp.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ResourceResp.

        待备份资源名称

        :return: The name of this ResourceResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResourceResp.

        待备份资源名称

        :param name: The name of this ResourceResp.
        :type: str
        """
        self._name = name

    @property
    def protect_status(self):
        """Gets the protect_status of this ResourceResp.

        保护状态

        :return: The protect_status of this ResourceResp.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        """Sets the protect_status of this ResourceResp.

        保护状态

        :param protect_status: The protect_status of this ResourceResp.
        :type: str
        """
        self._protect_status = protect_status

    @property
    def size(self):
        """Gets the size of this ResourceResp.

        资源已分配容量,单位为GB

        :return: The size of this ResourceResp.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ResourceResp.

        资源已分配容量,单位为GB

        :param size: The size of this ResourceResp.
        :type: int
        """
        self._size = size

    @property
    def type(self):
        """Gets the type of this ResourceResp.

        [待备份资源的类型: OS::Nova::Server, OS::Cinder::Volume, OS::Ironic::BareMetalServer, OS::Native::Server, OS::Sfs::Turbo](tag:hws,hws_hk,fcs_vm,ctc) [待备份资源的类型: OS::Nova::Server,  OS::Cinder::Volume](tag:dt,ocb,tlf,sbc)

        :return: The type of this ResourceResp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ResourceResp.

        [待备份资源的类型: OS::Nova::Server, OS::Cinder::Volume, OS::Ironic::BareMetalServer, OS::Native::Server, OS::Sfs::Turbo](tag:hws,hws_hk,fcs_vm,ctc) [待备份资源的类型: OS::Nova::Server,  OS::Cinder::Volume](tag:dt,ocb,tlf,sbc)

        :param type: The type of this ResourceResp.
        :type: str
        """
        self._type = type

    @property
    def backup_size(self):
        """Gets the backup_size of this ResourceResp.

        副本大小

        :return: The backup_size of this ResourceResp.
        :rtype: int
        """
        return self._backup_size

    @backup_size.setter
    def backup_size(self, backup_size):
        """Sets the backup_size of this ResourceResp.

        副本大小

        :param backup_size: The backup_size of this ResourceResp.
        :type: int
        """
        self._backup_size = backup_size

    @property
    def backup_count(self):
        """Gets the backup_count of this ResourceResp.

        副本数量

        :return: The backup_count of this ResourceResp.
        :rtype: int
        """
        return self._backup_count

    @backup_count.setter
    def backup_count(self, backup_count):
        """Sets the backup_count of this ResourceResp.

        副本数量

        :param backup_count: The backup_count of this ResourceResp.
        :type: int
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResourceResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
