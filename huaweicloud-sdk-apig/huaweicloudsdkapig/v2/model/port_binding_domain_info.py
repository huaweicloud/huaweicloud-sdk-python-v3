# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PortBindingDomainInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'group_name': 'str',
        'domain_name': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'group_name': 'group_name',
        'domain_name': 'domain_name'
    }

    def __init__(self, group_id=None, group_name=None, domain_name=None):
        r"""PortBindingDomainInfo

        The model defined in huaweicloud sdk

        :param group_id: 入方向端口绑定的API分组编号。
        :type group_id: str
        :param group_name: 入方向端口绑定的API分组名称。
        :type group_name: str
        :param domain_name: 入方向端口绑定的域名。
        :type domain_name: str
        """
        
        

        self._group_id = None
        self._group_name = None
        self._domain_name = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if domain_name is not None:
            self.domain_name = domain_name

    @property
    def group_id(self):
        r"""Gets the group_id of this PortBindingDomainInfo.

        入方向端口绑定的API分组编号。

        :return: The group_id of this PortBindingDomainInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this PortBindingDomainInfo.

        入方向端口绑定的API分组编号。

        :param group_id: The group_id of this PortBindingDomainInfo.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        r"""Gets the group_name of this PortBindingDomainInfo.

        入方向端口绑定的API分组名称。

        :return: The group_name of this PortBindingDomainInfo.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this PortBindingDomainInfo.

        入方向端口绑定的API分组名称。

        :param group_name: The group_name of this PortBindingDomainInfo.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def domain_name(self):
        r"""Gets the domain_name of this PortBindingDomainInfo.

        入方向端口绑定的域名。

        :return: The domain_name of this PortBindingDomainInfo.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this PortBindingDomainInfo.

        入方向端口绑定的域名。

        :param domain_name: The domain_name of this PortBindingDomainInfo.
        :type domain_name: str
        """
        self._domain_name = domain_name

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
        if not isinstance(other, PortBindingDomainInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
