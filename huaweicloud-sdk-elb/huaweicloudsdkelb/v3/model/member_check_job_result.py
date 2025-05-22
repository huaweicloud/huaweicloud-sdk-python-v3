# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MemberCheckJobResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'config': 'MemberCheckJobResultGroup',
        'acl': 'MemberCheckJobResultGroup',
        'security_group': 'MemberCheckJobResultGroup'
    }

    attribute_map = {
        'config': 'config',
        'acl': 'acl',
        'security_group': 'security_group'
    }

    def __init__(self, config=None, acl=None, security_group=None):
        r"""MemberCheckJobResult

        The model defined in huaweicloud sdk

        :param config: 
        :type config: :class:`huaweicloudsdkelb.v3.MemberCheckJobResultGroup`
        :param acl: 
        :type acl: :class:`huaweicloudsdkelb.v3.MemberCheckJobResultGroup`
        :param security_group: 
        :type security_group: :class:`huaweicloudsdkelb.v3.MemberCheckJobResultGroup`
        """
        
        

        self._config = None
        self._acl = None
        self._security_group = None
        self.discriminator = None

        if config is not None:
            self.config = config
        if acl is not None:
            self.acl = acl
        if security_group is not None:
            self.security_group = security_group

    @property
    def config(self):
        r"""Gets the config of this MemberCheckJobResult.

        :return: The config of this MemberCheckJobResult.
        :rtype: :class:`huaweicloudsdkelb.v3.MemberCheckJobResultGroup`
        """
        return self._config

    @config.setter
    def config(self, config):
        r"""Sets the config of this MemberCheckJobResult.

        :param config: The config of this MemberCheckJobResult.
        :type config: :class:`huaweicloudsdkelb.v3.MemberCheckJobResultGroup`
        """
        self._config = config

    @property
    def acl(self):
        r"""Gets the acl of this MemberCheckJobResult.

        :return: The acl of this MemberCheckJobResult.
        :rtype: :class:`huaweicloudsdkelb.v3.MemberCheckJobResultGroup`
        """
        return self._acl

    @acl.setter
    def acl(self, acl):
        r"""Sets the acl of this MemberCheckJobResult.

        :param acl: The acl of this MemberCheckJobResult.
        :type acl: :class:`huaweicloudsdkelb.v3.MemberCheckJobResultGroup`
        """
        self._acl = acl

    @property
    def security_group(self):
        r"""Gets the security_group of this MemberCheckJobResult.

        :return: The security_group of this MemberCheckJobResult.
        :rtype: :class:`huaweicloudsdkelb.v3.MemberCheckJobResultGroup`
        """
        return self._security_group

    @security_group.setter
    def security_group(self, security_group):
        r"""Sets the security_group of this MemberCheckJobResult.

        :param security_group: The security_group of this MemberCheckJobResult.
        :type security_group: :class:`huaweicloudsdkelb.v3.MemberCheckJobResultGroup`
        """
        self._security_group = security_group

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
        if not isinstance(other, MemberCheckJobResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
