# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TargetServerAssociatedWithTask:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'vm_id': 'str',
        'name': 'str',
        'ip': 'str',
        'os_type': 'str',
        'os_version': 'str'
    }

    attribute_map = {
        'id': 'id',
        'vm_id': 'vm_id',
        'name': 'name',
        'ip': 'ip',
        'os_type': 'os_type',
        'os_version': 'os_version'
    }

    def __init__(self, id=None, vm_id=None, name=None, ip=None, os_type=None, os_version=None):
        r"""TargetServerAssociatedWithTask

        The model defined in huaweicloud sdk

        :param id: 目的端在SMS数据库中的ID
        :type id: str
        :param vm_id: 目的端虚机ID
        :type vm_id: str
        :param name: 目的端服务器名称
        :type name: str
        :param ip: 目的端服务器IP
        :type ip: str
        :param os_type: 目的端服务器的OS类型 WINDOWS:WINDOWS系统 LINUX:LINUX系统 
        :type os_type: str
        :param os_version: 操作系统版本
        :type os_version: str
        """
        
        

        self._id = None
        self._vm_id = None
        self._name = None
        self._ip = None
        self._os_type = None
        self._os_version = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if vm_id is not None:
            self.vm_id = vm_id
        if name is not None:
            self.name = name
        if ip is not None:
            self.ip = ip
        if os_type is not None:
            self.os_type = os_type
        if os_version is not None:
            self.os_version = os_version

    @property
    def id(self):
        r"""Gets the id of this TargetServerAssociatedWithTask.

        目的端在SMS数据库中的ID

        :return: The id of this TargetServerAssociatedWithTask.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TargetServerAssociatedWithTask.

        目的端在SMS数据库中的ID

        :param id: The id of this TargetServerAssociatedWithTask.
        :type id: str
        """
        self._id = id

    @property
    def vm_id(self):
        r"""Gets the vm_id of this TargetServerAssociatedWithTask.

        目的端虚机ID

        :return: The vm_id of this TargetServerAssociatedWithTask.
        :rtype: str
        """
        return self._vm_id

    @vm_id.setter
    def vm_id(self, vm_id):
        r"""Sets the vm_id of this TargetServerAssociatedWithTask.

        目的端虚机ID

        :param vm_id: The vm_id of this TargetServerAssociatedWithTask.
        :type vm_id: str
        """
        self._vm_id = vm_id

    @property
    def name(self):
        r"""Gets the name of this TargetServerAssociatedWithTask.

        目的端服务器名称

        :return: The name of this TargetServerAssociatedWithTask.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TargetServerAssociatedWithTask.

        目的端服务器名称

        :param name: The name of this TargetServerAssociatedWithTask.
        :type name: str
        """
        self._name = name

    @property
    def ip(self):
        r"""Gets the ip of this TargetServerAssociatedWithTask.

        目的端服务器IP

        :return: The ip of this TargetServerAssociatedWithTask.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this TargetServerAssociatedWithTask.

        目的端服务器IP

        :param ip: The ip of this TargetServerAssociatedWithTask.
        :type ip: str
        """
        self._ip = ip

    @property
    def os_type(self):
        r"""Gets the os_type of this TargetServerAssociatedWithTask.

        目的端服务器的OS类型 WINDOWS:WINDOWS系统 LINUX:LINUX系统 

        :return: The os_type of this TargetServerAssociatedWithTask.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this TargetServerAssociatedWithTask.

        目的端服务器的OS类型 WINDOWS:WINDOWS系统 LINUX:LINUX系统 

        :param os_type: The os_type of this TargetServerAssociatedWithTask.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def os_version(self):
        r"""Gets the os_version of this TargetServerAssociatedWithTask.

        操作系统版本

        :return: The os_version of this TargetServerAssociatedWithTask.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        r"""Sets the os_version of this TargetServerAssociatedWithTask.

        操作系统版本

        :param os_version: The os_version of this TargetServerAssociatedWithTask.
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
        if not isinstance(other, TargetServerAssociatedWithTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
