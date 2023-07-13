# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StorageParameter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'path': 'str',
        'name': 'str',
        'default_mode': 'int',
        'medium': 'str'
    }

    attribute_map = {
        'path': 'path',
        'name': 'name',
        'default_mode': 'defaultMode',
        'medium': 'medium'
    }

    def __init__(self, path=None, name=None, default_mode=None, medium=None):
        """StorageParameter

        The model defined in huaweicloud sdk

        :param path: 主机路径， 适用于HostPath的存储类型
        :type path: str
        :param name: 配置项、密钥或者PVC的名字， 适用于ConfigMap、Secret和PersistentVolumeClaim的存储类型
        :type name: str
        :param default_mode: 挂载的权限，十进制格式，如384
        :type default_mode: int
        :param medium: 适用于EmptyDir类型的存储。不传参数为默认的磁盘介质，传参为memory则开启内存存储。
        :type medium: str
        """
        
        

        self._path = None
        self._name = None
        self._default_mode = None
        self._medium = None
        self.discriminator = None

        if path is not None:
            self.path = path
        if name is not None:
            self.name = name
        if default_mode is not None:
            self.default_mode = default_mode
        if medium is not None:
            self.medium = medium

    @property
    def path(self):
        """Gets the path of this StorageParameter.

        主机路径， 适用于HostPath的存储类型

        :return: The path of this StorageParameter.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this StorageParameter.

        主机路径， 适用于HostPath的存储类型

        :param path: The path of this StorageParameter.
        :type path: str
        """
        self._path = path

    @property
    def name(self):
        """Gets the name of this StorageParameter.

        配置项、密钥或者PVC的名字， 适用于ConfigMap、Secret和PersistentVolumeClaim的存储类型

        :return: The name of this StorageParameter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StorageParameter.

        配置项、密钥或者PVC的名字， 适用于ConfigMap、Secret和PersistentVolumeClaim的存储类型

        :param name: The name of this StorageParameter.
        :type name: str
        """
        self._name = name

    @property
    def default_mode(self):
        """Gets the default_mode of this StorageParameter.

        挂载的权限，十进制格式，如384

        :return: The default_mode of this StorageParameter.
        :rtype: int
        """
        return self._default_mode

    @default_mode.setter
    def default_mode(self, default_mode):
        """Sets the default_mode of this StorageParameter.

        挂载的权限，十进制格式，如384

        :param default_mode: The default_mode of this StorageParameter.
        :type default_mode: int
        """
        self._default_mode = default_mode

    @property
    def medium(self):
        """Gets the medium of this StorageParameter.

        适用于EmptyDir类型的存储。不传参数为默认的磁盘介质，传参为memory则开启内存存储。

        :return: The medium of this StorageParameter.
        :rtype: str
        """
        return self._medium

    @medium.setter
    def medium(self, medium):
        """Sets the medium of this StorageParameter.

        适用于EmptyDir类型的存储。不传参数为默认的磁盘介质，传参为memory则开启内存存储。

        :param medium: The medium of this StorageParameter.
        :type medium: str
        """
        self._medium = medium

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
        if not isinstance(other, StorageParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
