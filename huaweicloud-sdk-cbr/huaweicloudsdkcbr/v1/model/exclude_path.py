# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExcludePath:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'path_name': 'str',
        'exclude_path_name': 'list[str]'
    }

    attribute_map = {
        'path_name': 'path_name',
        'exclude_path_name': 'exclude_path_name'
    }

    def __init__(self, path_name=None, exclude_path_name=None):
        r"""ExcludePath

        The model defined in huaweicloud sdk

        :param path_name: 备份目录
        :type path_name: str
        :param exclude_path_name: 排除目录列表
        :type exclude_path_name: list[str]
        """
        
        

        self._path_name = None
        self._exclude_path_name = None
        self.discriminator = None

        if path_name is not None:
            self.path_name = path_name
        if exclude_path_name is not None:
            self.exclude_path_name = exclude_path_name

    @property
    def path_name(self):
        r"""Gets the path_name of this ExcludePath.

        备份目录

        :return: The path_name of this ExcludePath.
        :rtype: str
        """
        return self._path_name

    @path_name.setter
    def path_name(self, path_name):
        r"""Sets the path_name of this ExcludePath.

        备份目录

        :param path_name: The path_name of this ExcludePath.
        :type path_name: str
        """
        self._path_name = path_name

    @property
    def exclude_path_name(self):
        r"""Gets the exclude_path_name of this ExcludePath.

        排除目录列表

        :return: The exclude_path_name of this ExcludePath.
        :rtype: list[str]
        """
        return self._exclude_path_name

    @exclude_path_name.setter
    def exclude_path_name(self, exclude_path_name):
        r"""Sets the exclude_path_name of this ExcludePath.

        排除目录列表

        :param exclude_path_name: The exclude_path_name of this ExcludePath.
        :type exclude_path_name: list[str]
        """
        self._exclude_path_name = exclude_path_name

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
        if not isinstance(other, ExcludePath):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
