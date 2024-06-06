# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GaussDBforOpenGaussUserForList:

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
        'attribute': 'GaussDBforOpenGaussUserForListAttribute',
        'memberof': 'str',
        'lock_status': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'attribute': 'attribute',
        'memberof': 'memberof',
        'lock_status': 'lock_status'
    }

    def __init__(self, name=None, attribute=None, memberof=None, lock_status=None):
        """GaussDBforOpenGaussUserForList

        The model defined in huaweicloud sdk

        :param name: 帐号名。
        :type name: str
        :param attribute: 
        :type attribute: :class:`huaweicloudsdkgaussdbforopengauss.v3.GaussDBforOpenGaussUserForListAttribute`
        :param memberof: 用户的默认权限。
        :type memberof: str
        :param lock_status: 用户是否被锁，取值为“true”或“false”。
        :type lock_status: bool
        """
        
        

        self._name = None
        self._attribute = None
        self._memberof = None
        self._lock_status = None
        self.discriminator = None

        self.name = name
        if attribute is not None:
            self.attribute = attribute
        if memberof is not None:
            self.memberof = memberof
        if lock_status is not None:
            self.lock_status = lock_status

    @property
    def name(self):
        """Gets the name of this GaussDBforOpenGaussUserForList.

        帐号名。

        :return: The name of this GaussDBforOpenGaussUserForList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GaussDBforOpenGaussUserForList.

        帐号名。

        :param name: The name of this GaussDBforOpenGaussUserForList.
        :type name: str
        """
        self._name = name

    @property
    def attribute(self):
        """Gets the attribute of this GaussDBforOpenGaussUserForList.

        :return: The attribute of this GaussDBforOpenGaussUserForList.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.GaussDBforOpenGaussUserForListAttribute`
        """
        return self._attribute

    @attribute.setter
    def attribute(self, attribute):
        """Sets the attribute of this GaussDBforOpenGaussUserForList.

        :param attribute: The attribute of this GaussDBforOpenGaussUserForList.
        :type attribute: :class:`huaweicloudsdkgaussdbforopengauss.v3.GaussDBforOpenGaussUserForListAttribute`
        """
        self._attribute = attribute

    @property
    def memberof(self):
        """Gets the memberof of this GaussDBforOpenGaussUserForList.

        用户的默认权限。

        :return: The memberof of this GaussDBforOpenGaussUserForList.
        :rtype: str
        """
        return self._memberof

    @memberof.setter
    def memberof(self, memberof):
        """Sets the memberof of this GaussDBforOpenGaussUserForList.

        用户的默认权限。

        :param memberof: The memberof of this GaussDBforOpenGaussUserForList.
        :type memberof: str
        """
        self._memberof = memberof

    @property
    def lock_status(self):
        """Gets the lock_status of this GaussDBforOpenGaussUserForList.

        用户是否被锁，取值为“true”或“false”。

        :return: The lock_status of this GaussDBforOpenGaussUserForList.
        :rtype: bool
        """
        return self._lock_status

    @lock_status.setter
    def lock_status(self, lock_status):
        """Sets the lock_status of this GaussDBforOpenGaussUserForList.

        用户是否被锁，取值为“true”或“false”。

        :param lock_status: The lock_status of this GaussDBforOpenGaussUserForList.
        :type lock_status: bool
        """
        self._lock_status = lock_status

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
        if not isinstance(other, GaussDBforOpenGaussUserForList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
