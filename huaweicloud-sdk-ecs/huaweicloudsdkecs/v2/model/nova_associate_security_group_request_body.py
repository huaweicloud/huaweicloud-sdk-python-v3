# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NovaAssociateSecurityGroupRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'add_security_group': 'NovaAddSecurityGroupOption'
    }

    attribute_map = {
        'add_security_group': 'addSecurityGroup'
    }

    def __init__(self, add_security_group=None):
        """NovaAssociateSecurityGroupRequestBody

        The model defined in huaweicloud sdk

        :param add_security_group: 
        :type add_security_group: :class:`huaweicloudsdkecs.v2.NovaAddSecurityGroupOption`
        """
        
        

        self._add_security_group = None
        self.discriminator = None

        self.add_security_group = add_security_group

    @property
    def add_security_group(self):
        """Gets the add_security_group of this NovaAssociateSecurityGroupRequestBody.

        :return: The add_security_group of this NovaAssociateSecurityGroupRequestBody.
        :rtype: :class:`huaweicloudsdkecs.v2.NovaAddSecurityGroupOption`
        """
        return self._add_security_group

    @add_security_group.setter
    def add_security_group(self, add_security_group):
        """Sets the add_security_group of this NovaAssociateSecurityGroupRequestBody.

        :param add_security_group: The add_security_group of this NovaAssociateSecurityGroupRequestBody.
        :type add_security_group: :class:`huaweicloudsdkecs.v2.NovaAddSecurityGroupOption`
        """
        self._add_security_group = add_security_group

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
        if not isinstance(other, NovaAssociateSecurityGroupRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
