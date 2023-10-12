# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VolumeConfigurationMountInfo:

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
        'sub_path': 'str',
        'access_mode': 'str'
    }

    attribute_map = {
        'path': 'path',
        'sub_path': 'sub_path',
        'access_mode': 'access_mode'
    }

    def __init__(self, path=None, sub_path=None, access_mode=None):
        """VolumeConfigurationMountInfo

        The model defined in huaweicloud sdk

        :param path: 容器挂载路径。
        :type path: str
        :param sub_path: 子路径。
        :type sub_path: str
        :param access_mode: 读写权限，支持读写、只读。
        :type access_mode: str
        """
        
        

        self._path = None
        self._sub_path = None
        self._access_mode = None
        self.discriminator = None

        if path is not None:
            self.path = path
        if sub_path is not None:
            self.sub_path = sub_path
        if access_mode is not None:
            self.access_mode = access_mode

    @property
    def path(self):
        """Gets the path of this VolumeConfigurationMountInfo.

        容器挂载路径。

        :return: The path of this VolumeConfigurationMountInfo.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this VolumeConfigurationMountInfo.

        容器挂载路径。

        :param path: The path of this VolumeConfigurationMountInfo.
        :type path: str
        """
        self._path = path

    @property
    def sub_path(self):
        """Gets the sub_path of this VolumeConfigurationMountInfo.

        子路径。

        :return: The sub_path of this VolumeConfigurationMountInfo.
        :rtype: str
        """
        return self._sub_path

    @sub_path.setter
    def sub_path(self, sub_path):
        """Sets the sub_path of this VolumeConfigurationMountInfo.

        子路径。

        :param sub_path: The sub_path of this VolumeConfigurationMountInfo.
        :type sub_path: str
        """
        self._sub_path = sub_path

    @property
    def access_mode(self):
        """Gets the access_mode of this VolumeConfigurationMountInfo.

        读写权限，支持读写、只读。

        :return: The access_mode of this VolumeConfigurationMountInfo.
        :rtype: str
        """
        return self._access_mode

    @access_mode.setter
    def access_mode(self, access_mode):
        """Sets the access_mode of this VolumeConfigurationMountInfo.

        读写权限，支持读写、只读。

        :param access_mode: The access_mode of this VolumeConfigurationMountInfo.
        :type access_mode: str
        """
        self._access_mode = access_mode

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
        if not isinstance(other, VolumeConfigurationMountInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
