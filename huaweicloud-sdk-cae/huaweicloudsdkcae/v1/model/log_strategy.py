# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogStrategy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'collect_path': 'str',
        'mount_path': 'str'
    }

    attribute_map = {
        'collect_path': 'collect_path',
        'mount_path': 'mount_path'
    }

    def __init__(self, collect_path=None, mount_path=None):
        """LogStrategy

        The model defined in huaweicloud sdk

        :param collect_path: 收集路径。
        :type collect_path: str
        :param mount_path: 挂载路径。
        :type mount_path: str
        """
        
        

        self._collect_path = None
        self._mount_path = None
        self.discriminator = None

        if collect_path is not None:
            self.collect_path = collect_path
        if mount_path is not None:
            self.mount_path = mount_path

    @property
    def collect_path(self):
        """Gets the collect_path of this LogStrategy.

        收集路径。

        :return: The collect_path of this LogStrategy.
        :rtype: str
        """
        return self._collect_path

    @collect_path.setter
    def collect_path(self, collect_path):
        """Sets the collect_path of this LogStrategy.

        收集路径。

        :param collect_path: The collect_path of this LogStrategy.
        :type collect_path: str
        """
        self._collect_path = collect_path

    @property
    def mount_path(self):
        """Gets the mount_path of this LogStrategy.

        挂载路径。

        :return: The mount_path of this LogStrategy.
        :rtype: str
        """
        return self._mount_path

    @mount_path.setter
    def mount_path(self, mount_path):
        """Sets the mount_path of this LogStrategy.

        挂载路径。

        :param mount_path: The mount_path of this LogStrategy.
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
        if not isinstance(other, LogStrategy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
