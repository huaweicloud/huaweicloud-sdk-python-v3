# coding: utf-8

import pprint
import re

import six





class ServerSchedulerHints:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'group': 'list[str]',
        'tenancy': 'list[str]',
        'dedicated_host_id': 'list[str]'
    }

    attribute_map = {
        'group': 'group',
        'tenancy': 'tenancy',
        'dedicated_host_id': 'dedicated_host_id'
    }

    def __init__(self, group=None, tenancy=None, dedicated_host_id=None):
        """ServerSchedulerHints - a model defined in huaweicloud sdk"""
        
        

        self._group = None
        self._tenancy = None
        self._dedicated_host_id = None
        self.discriminator = None

        if group is not None:
            self.group = group
        if tenancy is not None:
            self.tenancy = tenancy
        if dedicated_host_id is not None:
            self.dedicated_host_id = dedicated_host_id

    @property
    def group(self):
        """Gets the group of this ServerSchedulerHints.

        反亲和性组信息。  UUID格式。

        :return: The group of this ServerSchedulerHints.
        :rtype: list[str]
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this ServerSchedulerHints.

        反亲和性组信息。  UUID格式。

        :param group: The group of this ServerSchedulerHints.
        :type: list[str]
        """
        self._group = group

    @property
    def tenancy(self):
        """Gets the tenancy of this ServerSchedulerHints.

        在专属主机或共享池中创建弹性云服务器。默认为在共享池创建。值为： shared或dedicated。  - shared：表示共享池。 - dedicated:表示专属主机。  创建与查询此值均有效。

        :return: The tenancy of this ServerSchedulerHints.
        :rtype: list[str]
        """
        return self._tenancy

    @tenancy.setter
    def tenancy(self, tenancy):
        """Sets the tenancy of this ServerSchedulerHints.

        在专属主机或共享池中创建弹性云服务器。默认为在共享池创建。值为： shared或dedicated。  - shared：表示共享池。 - dedicated:表示专属主机。  创建与查询此值均有效。

        :param tenancy: The tenancy of this ServerSchedulerHints.
        :type: list[str]
        """
        self._tenancy = tenancy

    @property
    def dedicated_host_id(self):
        """Gets the dedicated_host_id of this ServerSchedulerHints.

        专属主机ID。  此属性仅在tenancy值为dedicated时有效。  不指定此属性，系统将自动分配租户可自动放置弹性云服务器的专属主机。  创建与查询此值均有效。

        :return: The dedicated_host_id of this ServerSchedulerHints.
        :rtype: list[str]
        """
        return self._dedicated_host_id

    @dedicated_host_id.setter
    def dedicated_host_id(self, dedicated_host_id):
        """Sets the dedicated_host_id of this ServerSchedulerHints.

        专属主机ID。  此属性仅在tenancy值为dedicated时有效。  不指定此属性，系统将自动分配租户可自动放置弹性云服务器的专属主机。  创建与查询此值均有效。

        :param dedicated_host_id: The dedicated_host_id of this ServerSchedulerHints.
        :type: list[str]
        """
        self._dedicated_host_id = dedicated_host_id

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ServerSchedulerHints):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
