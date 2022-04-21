# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NovaDisassociateSecurityGroupRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'remove_security_group': 'NovaRemoveSecurityGroupOption'
    }

    attribute_map = {
        'remove_security_group': 'removeSecurityGroup'
    }

    def __init__(self, remove_security_group=None):
        """NovaDisassociateSecurityGroupRequestBody

        The model defined in huaweicloud sdk

        :param remove_security_group: 
        :type remove_security_group: :class:`huaweicloudsdkecs.v2.NovaRemoveSecurityGroupOption`
        """
        
        

        self._remove_security_group = None
        self.discriminator = None

        self.remove_security_group = remove_security_group

    @property
    def remove_security_group(self):
        """Gets the remove_security_group of this NovaDisassociateSecurityGroupRequestBody.


        :return: The remove_security_group of this NovaDisassociateSecurityGroupRequestBody.
        :rtype: :class:`huaweicloudsdkecs.v2.NovaRemoveSecurityGroupOption`
        """
        return self._remove_security_group

    @remove_security_group.setter
    def remove_security_group(self, remove_security_group):
        """Sets the remove_security_group of this NovaDisassociateSecurityGroupRequestBody.


        :param remove_security_group: The remove_security_group of this NovaDisassociateSecurityGroupRequestBody.
        :type remove_security_group: :class:`huaweicloudsdkecs.v2.NovaRemoveSecurityGroupOption`
        """
        self._remove_security_group = remove_security_group

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
        if not isinstance(other, NovaDisassociateSecurityGroupRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
