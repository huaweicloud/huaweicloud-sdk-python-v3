# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FuncMount:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mount_type': 'str',
        'mount_resource': 'str',
        'mount_share_path': 'str',
        'local_mount_path': 'str'
    }

    attribute_map = {
        'mount_type': 'mount_type',
        'mount_resource': 'mount_resource',
        'mount_share_path': 'mount_share_path',
        'local_mount_path': 'local_mount_path'
    }

    def __init__(self, mount_type=None, mount_resource=None, mount_share_path=None, local_mount_path=None):
        """FuncMount

        The model defined in huaweicloud sdk

        :param mount_type: 挂载类型(sfs/sfsTurbo/ecs)，func_mounts非空时必选。
        :type mount_type: str
        :param mount_resource: 挂载资源ID（对应云服务ID），func_mounts非空时必选。
        :type mount_resource: str
        :param mount_share_path: 远端挂载路径（例如192.168.0.12:/data），如果mount_type为ecs，必选。
        :type mount_share_path: str
        :param local_mount_path: 函数访问路径，func_mounts非空时必选。
        :type local_mount_path: str
        """
        
        

        self._mount_type = None
        self._mount_resource = None
        self._mount_share_path = None
        self._local_mount_path = None
        self.discriminator = None

        self.mount_type = mount_type
        self.mount_resource = mount_resource
        if mount_share_path is not None:
            self.mount_share_path = mount_share_path
        self.local_mount_path = local_mount_path

    @property
    def mount_type(self):
        """Gets the mount_type of this FuncMount.

        挂载类型(sfs/sfsTurbo/ecs)，func_mounts非空时必选。

        :return: The mount_type of this FuncMount.
        :rtype: str
        """
        return self._mount_type

    @mount_type.setter
    def mount_type(self, mount_type):
        """Sets the mount_type of this FuncMount.

        挂载类型(sfs/sfsTurbo/ecs)，func_mounts非空时必选。

        :param mount_type: The mount_type of this FuncMount.
        :type mount_type: str
        """
        self._mount_type = mount_type

    @property
    def mount_resource(self):
        """Gets the mount_resource of this FuncMount.

        挂载资源ID（对应云服务ID），func_mounts非空时必选。

        :return: The mount_resource of this FuncMount.
        :rtype: str
        """
        return self._mount_resource

    @mount_resource.setter
    def mount_resource(self, mount_resource):
        """Sets the mount_resource of this FuncMount.

        挂载资源ID（对应云服务ID），func_mounts非空时必选。

        :param mount_resource: The mount_resource of this FuncMount.
        :type mount_resource: str
        """
        self._mount_resource = mount_resource

    @property
    def mount_share_path(self):
        """Gets the mount_share_path of this FuncMount.

        远端挂载路径（例如192.168.0.12:/data），如果mount_type为ecs，必选。

        :return: The mount_share_path of this FuncMount.
        :rtype: str
        """
        return self._mount_share_path

    @mount_share_path.setter
    def mount_share_path(self, mount_share_path):
        """Sets the mount_share_path of this FuncMount.

        远端挂载路径（例如192.168.0.12:/data），如果mount_type为ecs，必选。

        :param mount_share_path: The mount_share_path of this FuncMount.
        :type mount_share_path: str
        """
        self._mount_share_path = mount_share_path

    @property
    def local_mount_path(self):
        """Gets the local_mount_path of this FuncMount.

        函数访问路径，func_mounts非空时必选。

        :return: The local_mount_path of this FuncMount.
        :rtype: str
        """
        return self._local_mount_path

    @local_mount_path.setter
    def local_mount_path(self, local_mount_path):
        """Sets the local_mount_path of this FuncMount.

        函数访问路径，func_mounts非空时必选。

        :param local_mount_path: The local_mount_path of this FuncMount.
        :type local_mount_path: str
        """
        self._local_mount_path = local_mount_path

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
        if not isinstance(other, FuncMount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
