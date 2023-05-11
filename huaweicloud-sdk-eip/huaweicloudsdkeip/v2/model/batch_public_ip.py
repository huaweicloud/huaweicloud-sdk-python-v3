# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchPublicIp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'type': 'str',
        'ip_version': 'str',
        'enterprise_project_id': 'str',
        'tags': 'list[str]',
        'profile': 'BatchProfile'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'ip_version': 'ip_version',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags',
        'profile': 'profile'
    }

    def __init__(self, id=None, type=None, ip_version=None, enterprise_project_id=None, tags=None, profile=None):
        """BatchPublicIp

        The model defined in huaweicloud sdk

        :param id: 指定id创建EIP
        :type id: str
        :param type: 公网ip类型
        :type type: str
        :param ip_version: 公网EIP的版本，例如ipv4，ipv6，默认为ipv4
        :type ip_version: str
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        :param tags: 公网EIP标签
        :type tags: list[str]
        :param profile: 
        :type profile: :class:`huaweicloudsdkeip.v2.BatchProfile`
        """
        
        

        self._id = None
        self._type = None
        self._ip_version = None
        self._enterprise_project_id = None
        self._tags = None
        self._profile = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.type = type
        if ip_version is not None:
            self.ip_version = ip_version
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags
        if profile is not None:
            self.profile = profile

    @property
    def id(self):
        """Gets the id of this BatchPublicIp.

        指定id创建EIP

        :return: The id of this BatchPublicIp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BatchPublicIp.

        指定id创建EIP

        :param id: The id of this BatchPublicIp.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        """Gets the type of this BatchPublicIp.

        公网ip类型

        :return: The type of this BatchPublicIp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BatchPublicIp.

        公网ip类型

        :param type: The type of this BatchPublicIp.
        :type type: str
        """
        self._type = type

    @property
    def ip_version(self):
        """Gets the ip_version of this BatchPublicIp.

        公网EIP的版本，例如ipv4，ipv6，默认为ipv4

        :return: The ip_version of this BatchPublicIp.
        :rtype: str
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this BatchPublicIp.

        公网EIP的版本，例如ipv4，ipv6，默认为ipv4

        :param ip_version: The ip_version of this BatchPublicIp.
        :type ip_version: str
        """
        self._ip_version = ip_version

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this BatchPublicIp.

        企业项目id

        :return: The enterprise_project_id of this BatchPublicIp.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this BatchPublicIp.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this BatchPublicIp.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        """Gets the tags of this BatchPublicIp.

        公网EIP标签

        :return: The tags of this BatchPublicIp.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this BatchPublicIp.

        公网EIP标签

        :param tags: The tags of this BatchPublicIp.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def profile(self):
        """Gets the profile of this BatchPublicIp.

        :return: The profile of this BatchPublicIp.
        :rtype: :class:`huaweicloudsdkeip.v2.BatchProfile`
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this BatchPublicIp.

        :param profile: The profile of this BatchPublicIp.
        :type profile: :class:`huaweicloudsdkeip.v2.BatchProfile`
        """
        self._profile = profile

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
        if not isinstance(other, BatchPublicIp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
