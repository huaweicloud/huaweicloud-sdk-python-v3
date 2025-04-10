# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnvironmentBaseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'os': 'str',
        'uuid': 'str',
        'group_id': 'str',
        'host_count': 'int'
    }

    attribute_map = {
        'name': 'name',
        'os': 'os',
        'uuid': 'uuid',
        'group_id': 'group_id',
        'host_count': 'host_count'
    }

    def __init__(self, name=None, os=None, uuid=None, group_id=None, host_count=None):
        r"""EnvironmentBaseInfo

        The model defined in huaweicloud sdk

        :param name: 环境名称
        :type name: str
        :param os: 操作系统：windows|linux
        :type os: str
        :param uuid: 环境id
        :type uuid: str
        :param group_id: 主机集群id
        :type group_id: str
        :param host_count: 环境下主机数量
        :type host_count: int
        """
        
        

        self._name = None
        self._os = None
        self._uuid = None
        self._group_id = None
        self._host_count = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if os is not None:
            self.os = os
        if uuid is not None:
            self.uuid = uuid
        if group_id is not None:
            self.group_id = group_id
        if host_count is not None:
            self.host_count = host_count

    @property
    def name(self):
        r"""Gets the name of this EnvironmentBaseInfo.

        环境名称

        :return: The name of this EnvironmentBaseInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EnvironmentBaseInfo.

        环境名称

        :param name: The name of this EnvironmentBaseInfo.
        :type name: str
        """
        self._name = name

    @property
    def os(self):
        r"""Gets the os of this EnvironmentBaseInfo.

        操作系统：windows|linux

        :return: The os of this EnvironmentBaseInfo.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        r"""Sets the os of this EnvironmentBaseInfo.

        操作系统：windows|linux

        :param os: The os of this EnvironmentBaseInfo.
        :type os: str
        """
        self._os = os

    @property
    def uuid(self):
        r"""Gets the uuid of this EnvironmentBaseInfo.

        环境id

        :return: The uuid of this EnvironmentBaseInfo.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        r"""Sets the uuid of this EnvironmentBaseInfo.

        环境id

        :param uuid: The uuid of this EnvironmentBaseInfo.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def group_id(self):
        r"""Gets the group_id of this EnvironmentBaseInfo.

        主机集群id

        :return: The group_id of this EnvironmentBaseInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this EnvironmentBaseInfo.

        主机集群id

        :param group_id: The group_id of this EnvironmentBaseInfo.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def host_count(self):
        r"""Gets the host_count of this EnvironmentBaseInfo.

        环境下主机数量

        :return: The host_count of this EnvironmentBaseInfo.
        :rtype: int
        """
        return self._host_count

    @host_count.setter
    def host_count(self, host_count):
        r"""Sets the host_count of this EnvironmentBaseInfo.

        环境下主机数量

        :param host_count: The host_count of this EnvironmentBaseInfo.
        :type host_count: int
        """
        self._host_count = host_count

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
        if not isinstance(other, EnvironmentBaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
