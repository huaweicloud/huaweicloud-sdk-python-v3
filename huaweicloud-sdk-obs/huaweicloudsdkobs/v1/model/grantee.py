# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Grantee:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "Grantee"

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'canned': 'str'
    }

    attribute_map = {
        'id': 'ID',
        'canned': 'Canned'
    }

    def __init__(self, id=None, canned=None):
        """Grantee

        The model defined in huaweicloud sdk

        :param id: 被授权用户的租户Id 
        :type id: str
        :param canned: 向所有人授予权限。 
        :type canned: str
        """
        
        

        self._id = None
        self._canned = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if canned is not None:
            self.canned = canned

    @property
    def id(self):
        """Gets the id of this Grantee.

        被授权用户的租户Id 

        :return: The id of this Grantee.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Grantee.

        被授权用户的租户Id 

        :param id: The id of this Grantee.
        :type id: str
        """
        self._id = id

    @property
    def canned(self):
        """Gets the canned of this Grantee.

        向所有人授予权限。 

        :return: The canned of this Grantee.
        :rtype: str
        """
        return self._canned

    @canned.setter
    def canned(self, canned):
        """Sets the canned of this Grantee.

        向所有人授予权限。 

        :param canned: The canned of this Grantee.
        :type canned: str
        """
        self._canned = canned

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
        if not isinstance(other, Grantee):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
