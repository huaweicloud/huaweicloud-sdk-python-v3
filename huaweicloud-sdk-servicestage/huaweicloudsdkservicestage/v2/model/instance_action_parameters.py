# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceActionParameters:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'replica': 'int',
        'hosts': 'list[str]',
        'version': 'str'
    }

    attribute_map = {
        'replica': 'replica',
        'hosts': 'hosts',
        'version': 'version'
    }

    def __init__(self, replica=None, hosts=None, version=None):
        r"""InstanceActionParameters

        The model defined in huaweicloud sdk

        :param replica: 实例数，在scale操作时提供。
        :type replica: int
        :param hosts: ECS ID列表，指定虚机扩容时部署的ECS主机。
        :type hosts: list[str]
        :param version: 版本号，在rollback操作时提供，通过查询快照接口获取。
        :type version: str
        """
        
        

        self._replica = None
        self._hosts = None
        self._version = None
        self.discriminator = None

        if replica is not None:
            self.replica = replica
        if hosts is not None:
            self.hosts = hosts
        if version is not None:
            self.version = version

    @property
    def replica(self):
        r"""Gets the replica of this InstanceActionParameters.

        实例数，在scale操作时提供。

        :return: The replica of this InstanceActionParameters.
        :rtype: int
        """
        return self._replica

    @replica.setter
    def replica(self, replica):
        r"""Sets the replica of this InstanceActionParameters.

        实例数，在scale操作时提供。

        :param replica: The replica of this InstanceActionParameters.
        :type replica: int
        """
        self._replica = replica

    @property
    def hosts(self):
        r"""Gets the hosts of this InstanceActionParameters.

        ECS ID列表，指定虚机扩容时部署的ECS主机。

        :return: The hosts of this InstanceActionParameters.
        :rtype: list[str]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        r"""Sets the hosts of this InstanceActionParameters.

        ECS ID列表，指定虚机扩容时部署的ECS主机。

        :param hosts: The hosts of this InstanceActionParameters.
        :type hosts: list[str]
        """
        self._hosts = hosts

    @property
    def version(self):
        r"""Gets the version of this InstanceActionParameters.

        版本号，在rollback操作时提供，通过查询快照接口获取。

        :return: The version of this InstanceActionParameters.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this InstanceActionParameters.

        版本号，在rollback操作时提供，通过查询快照接口获取。

        :param version: The version of this InstanceActionParameters.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, InstanceActionParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
