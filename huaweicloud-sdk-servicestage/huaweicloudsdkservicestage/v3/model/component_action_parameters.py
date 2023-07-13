# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentActionParameters:

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
        """ComponentActionParameters

        The model defined in huaweicloud sdk

        :param replica: use for sacle, scale to specified replica
        :type replica: int
        :param hosts: use for vmapp scale
        :type hosts: list[str]
        :param version: use for rollback, rollback to specified version
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
        """Gets the replica of this ComponentActionParameters.

        use for sacle, scale to specified replica

        :return: The replica of this ComponentActionParameters.
        :rtype: int
        """
        return self._replica

    @replica.setter
    def replica(self, replica):
        """Sets the replica of this ComponentActionParameters.

        use for sacle, scale to specified replica

        :param replica: The replica of this ComponentActionParameters.
        :type replica: int
        """
        self._replica = replica

    @property
    def hosts(self):
        """Gets the hosts of this ComponentActionParameters.

        use for vmapp scale

        :return: The hosts of this ComponentActionParameters.
        :rtype: list[str]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this ComponentActionParameters.

        use for vmapp scale

        :param hosts: The hosts of this ComponentActionParameters.
        :type hosts: list[str]
        """
        self._hosts = hosts

    @property
    def version(self):
        """Gets the version of this ComponentActionParameters.

        use for rollback, rollback to specified version

        :return: The version of this ComponentActionParameters.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ComponentActionParameters.

        use for rollback, rollback to specified version

        :param version: The version of this ComponentActionParameters.
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
        if not isinstance(other, ComponentActionParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
