# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtDevice:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source': 'str',
        'destination': 'str',
        'cgroup_permissions': 'str'
    }

    attribute_map = {
        'source': 'source',
        'destination': 'destination',
        'cgroup_permissions': 'cgroup_permissions'
    }

    def __init__(self, source=None, destination=None, cgroup_permissions=None):
        """ExtDevice

        The model defined in huaweicloud sdk

        :param source: 源路径
        :type source: str
        :param destination: 卷挂载路径
        :type destination: str
        :param cgroup_permissions: 只读，默认MRW
        :type cgroup_permissions: str
        """
        
        

        self._source = None
        self._destination = None
        self._cgroup_permissions = None
        self.discriminator = None

        self.source = source
        self.destination = destination
        if cgroup_permissions is not None:
            self.cgroup_permissions = cgroup_permissions

    @property
    def source(self):
        """Gets the source of this ExtDevice.

        源路径

        :return: The source of this ExtDevice.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ExtDevice.

        源路径

        :param source: The source of this ExtDevice.
        :type source: str
        """
        self._source = source

    @property
    def destination(self):
        """Gets the destination of this ExtDevice.

        卷挂载路径

        :return: The destination of this ExtDevice.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this ExtDevice.

        卷挂载路径

        :param destination: The destination of this ExtDevice.
        :type destination: str
        """
        self._destination = destination

    @property
    def cgroup_permissions(self):
        """Gets the cgroup_permissions of this ExtDevice.

        只读，默认MRW

        :return: The cgroup_permissions of this ExtDevice.
        :rtype: str
        """
        return self._cgroup_permissions

    @cgroup_permissions.setter
    def cgroup_permissions(self, cgroup_permissions):
        """Sets the cgroup_permissions of this ExtDevice.

        只读，默认MRW

        :param cgroup_permissions: The cgroup_permissions of this ExtDevice.
        :type cgroup_permissions: str
        """
        self._cgroup_permissions = cgroup_permissions

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
        if not isinstance(other, ExtDevice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
