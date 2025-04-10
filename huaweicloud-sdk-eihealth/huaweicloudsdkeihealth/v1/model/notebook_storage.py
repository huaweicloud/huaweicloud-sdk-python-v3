# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NotebookStorage:

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
        'mount_path': 'str'
    }

    attribute_map = {
        'path': 'path',
        'mount_path': 'mount_path'
    }

    def __init__(self, path=None, mount_path=None):
        r"""NotebookStorage

        The model defined in huaweicloud sdk

        :param path: notebook存储路径
        :type path: str
        :param mount_path: 挂载路径，由于目前暂不支持自定义挂载，暂不开放
        :type mount_path: str
        """
        
        

        self._path = None
        self._mount_path = None
        self.discriminator = None

        self.path = path
        if mount_path is not None:
            self.mount_path = mount_path

    @property
    def path(self):
        r"""Gets the path of this NotebookStorage.

        notebook存储路径

        :return: The path of this NotebookStorage.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this NotebookStorage.

        notebook存储路径

        :param path: The path of this NotebookStorage.
        :type path: str
        """
        self._path = path

    @property
    def mount_path(self):
        r"""Gets the mount_path of this NotebookStorage.

        挂载路径，由于目前暂不支持自定义挂载，暂不开放

        :return: The mount_path of this NotebookStorage.
        :rtype: str
        """
        return self._mount_path

    @mount_path.setter
    def mount_path(self, mount_path):
        r"""Sets the mount_path of this NotebookStorage.

        挂载路径，由于目前暂不支持自定义挂载，暂不开放

        :param mount_path: The mount_path of this NotebookStorage.
        :type mount_path: str
        """
        self._mount_path = mount_path

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
        if not isinstance(other, NotebookStorage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
