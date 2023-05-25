# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityContext:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'run_as_user': 'int',
        'run_as_group': 'int',
        'capabilities': 'SecurityContextCapabilities'
    }

    attribute_map = {
        'run_as_user': 'run_as_user',
        'run_as_group': 'run_as_group',
        'capabilities': 'capabilities'
    }

    def __init__(self, run_as_user=None, run_as_group=None, capabilities=None):
        """SecurityContext

        The model defined in huaweicloud sdk

        :param run_as_user: 
        :type run_as_user: int
        :param run_as_group: 
        :type run_as_group: int
        :param capabilities: 
        :type capabilities: :class:`huaweicloudsdkservicestage.v3.SecurityContextCapabilities`
        """
        
        

        self._run_as_user = None
        self._run_as_group = None
        self._capabilities = None
        self.discriminator = None

        if run_as_user is not None:
            self.run_as_user = run_as_user
        if run_as_group is not None:
            self.run_as_group = run_as_group
        if capabilities is not None:
            self.capabilities = capabilities

    @property
    def run_as_user(self):
        """Gets the run_as_user of this SecurityContext.

        :return: The run_as_user of this SecurityContext.
        :rtype: int
        """
        return self._run_as_user

    @run_as_user.setter
    def run_as_user(self, run_as_user):
        """Sets the run_as_user of this SecurityContext.

        :param run_as_user: The run_as_user of this SecurityContext.
        :type run_as_user: int
        """
        self._run_as_user = run_as_user

    @property
    def run_as_group(self):
        """Gets the run_as_group of this SecurityContext.

        :return: The run_as_group of this SecurityContext.
        :rtype: int
        """
        return self._run_as_group

    @run_as_group.setter
    def run_as_group(self, run_as_group):
        """Sets the run_as_group of this SecurityContext.

        :param run_as_group: The run_as_group of this SecurityContext.
        :type run_as_group: int
        """
        self._run_as_group = run_as_group

    @property
    def capabilities(self):
        """Gets the capabilities of this SecurityContext.

        :return: The capabilities of this SecurityContext.
        :rtype: :class:`huaweicloudsdkservicestage.v3.SecurityContextCapabilities`
        """
        return self._capabilities

    @capabilities.setter
    def capabilities(self, capabilities):
        """Sets the capabilities of this SecurityContext.

        :param capabilities: The capabilities of this SecurityContext.
        :type capabilities: :class:`huaweicloudsdkservicestage.v3.SecurityContextCapabilities`
        """
        self._capabilities = capabilities

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
        if not isinstance(other, SecurityContext):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
