# coding: utf-8

import re
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
        'attributes': 'GaussDBforOpenGaussUserForListAttributes',
        'memberof': 'str'
    }

    attribute_map = {
        'name': 'name',
        'attributes': 'attributes',
        'memberof': 'memberof'
    }

    def __init__(self, name=None, attributes=None, memberof=None):
        """GaussDBforOpenGaussUserForList

        The model defined in huaweicloud sdk

        :param name: 帐号名。
        :type name: str
        :param attributes: 
        :type attributes: :class:`huaweicloudsdkgaussdbforopengauss.v3.GaussDBforOpenGaussUserForListAttributes`
        :param memberof: 用户的默认权限。
        :type memberof: str
        """
        
        

        self._name = None
        self._attributes = None
        self._memberof = None
        self.discriminator = None

        self.name = name
        if attributes is not None:
            self.attributes = attributes
        if memberof is not None:
            self.memberof = memberof

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
    def attributes(self):
        """Gets the attributes of this GaussDBforOpenGaussUserForList.

        :return: The attributes of this GaussDBforOpenGaussUserForList.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.GaussDBforOpenGaussUserForListAttributes`
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this GaussDBforOpenGaussUserForList.

        :param attributes: The attributes of this GaussDBforOpenGaussUserForList.
        :type attributes: :class:`huaweicloudsdkgaussdbforopengauss.v3.GaussDBforOpenGaussUserForListAttributes`
        """
        self._attributes = attributes

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
