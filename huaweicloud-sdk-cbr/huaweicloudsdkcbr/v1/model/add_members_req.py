# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddMembersReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'members': 'list[str]',
        'domains': 'list[str]'
    }

    attribute_map = {
        'members': 'members',
        'domains': 'domains'
    }

    def __init__(self, members=None, domains=None):
        r"""AddMembersReq

        The model defined in huaweicloud sdk

        :param members: 列表，待添加备份共享成员的project_id。
        :type members: list[str]
        :param domains: 列表，待添加备份共享成员的domain_id。 &gt; 该特性目前属于公测阶段，部分region可能无法使用.
        :type domains: list[str]
        """
        
        

        self._members = None
        self._domains = None
        self.discriminator = None

        if members is not None:
            self.members = members
        if domains is not None:
            self.domains = domains

    @property
    def members(self):
        r"""Gets the members of this AddMembersReq.

        列表，待添加备份共享成员的project_id。

        :return: The members of this AddMembersReq.
        :rtype: list[str]
        """
        return self._members

    @members.setter
    def members(self, members):
        r"""Sets the members of this AddMembersReq.

        列表，待添加备份共享成员的project_id。

        :param members: The members of this AddMembersReq.
        :type members: list[str]
        """
        self._members = members

    @property
    def domains(self):
        r"""Gets the domains of this AddMembersReq.

        列表，待添加备份共享成员的domain_id。 > 该特性目前属于公测阶段，部分region可能无法使用.

        :return: The domains of this AddMembersReq.
        :rtype: list[str]
        """
        return self._domains

    @domains.setter
    def domains(self, domains):
        r"""Sets the domains of this AddMembersReq.

        列表，待添加备份共享成员的domain_id。 > 该特性目前属于公测阶段，部分region可能无法使用.

        :param domains: The domains of this AddMembersReq.
        :type domains: list[str]
        """
        self._domains = domains

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
        if not isinstance(other, AddMembersReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
