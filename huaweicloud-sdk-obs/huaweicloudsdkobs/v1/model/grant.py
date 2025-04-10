# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Grant:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "Grant"

    sensitive_list = []

    openapi_types = {
        'grantee': 'Grantee',
        'permission': 'str',
        'delivered': 'bool'
    }

    attribute_map = {
        'grantee': 'Grantee',
        'permission': 'Permission',
        'delivered': 'Delivered'
    }

    def __init__(self, grantee=None, permission=None, delivered=None):
        r"""Grant

        The model defined in huaweicloud sdk

        :param grantee: 
        :type grantee: :class:`huaweicloudsdkobs.v1.Grantee`
        :param permission: Permissions granted
        :type permission: str
        :param delivered: Indicates whether the bucket ACL is applied to objects in the bucket.
        :type delivered: bool
        """
        
        

        self._grantee = None
        self._permission = None
        self._delivered = None
        self.discriminator = None

        if grantee is not None:
            self.grantee = grantee
        if permission is not None:
            self.permission = permission
        if delivered is not None:
            self.delivered = delivered

    @property
    def grantee(self):
        r"""Gets the grantee of this Grant.

        :return: The grantee of this Grant.
        :rtype: :class:`huaweicloudsdkobs.v1.Grantee`
        """
        return self._grantee

    @grantee.setter
    def grantee(self, grantee):
        r"""Sets the grantee of this Grant.

        :param grantee: The grantee of this Grant.
        :type grantee: :class:`huaweicloudsdkobs.v1.Grantee`
        """
        self._grantee = grantee

    @property
    def permission(self):
        r"""Gets the permission of this Grant.

        Permissions granted

        :return: The permission of this Grant.
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        r"""Sets the permission of this Grant.

        Permissions granted

        :param permission: The permission of this Grant.
        :type permission: str
        """
        self._permission = permission

    @property
    def delivered(self):
        r"""Gets the delivered of this Grant.

        Indicates whether the bucket ACL is applied to objects in the bucket.

        :return: The delivered of this Grant.
        :rtype: bool
        """
        return self._delivered

    @delivered.setter
    def delivered(self, delivered):
        r"""Sets the delivered of this Grant.

        Indicates whether the bucket ACL is applied to objects in the bucket.

        :param delivered: The delivered of this Grant.
        :type delivered: bool
        """
        self._delivered = delivered

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
        if not isinstance(other, Grant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
