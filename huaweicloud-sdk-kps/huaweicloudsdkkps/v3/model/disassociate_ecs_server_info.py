# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisassociateEcsServerInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'auth': 'Auth'
    }

    attribute_map = {
        'id': 'id',
        'auth': 'auth'
    }

    def __init__(self, id=None, auth=None):
        """DisassociateEcsServerInfo

        The model defined in huaweicloud sdk

        :param id: 需要绑定(替换或重置)SSH密钥对的虚拟机id
        :type id: str
        :param auth: 
        :type auth: :class:`huaweicloudsdkkps.v3.Auth`
        """
        
        

        self._id = None
        self._auth = None
        self.discriminator = None

        self.id = id
        if auth is not None:
            self.auth = auth

    @property
    def id(self):
        """Gets the id of this DisassociateEcsServerInfo.

        需要绑定(替换或重置)SSH密钥对的虚拟机id

        :return: The id of this DisassociateEcsServerInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DisassociateEcsServerInfo.

        需要绑定(替换或重置)SSH密钥对的虚拟机id

        :param id: The id of this DisassociateEcsServerInfo.
        :type id: str
        """
        self._id = id

    @property
    def auth(self):
        """Gets the auth of this DisassociateEcsServerInfo.


        :return: The auth of this DisassociateEcsServerInfo.
        :rtype: :class:`huaweicloudsdkkps.v3.Auth`
        """
        return self._auth

    @auth.setter
    def auth(self, auth):
        """Sets the auth of this DisassociateEcsServerInfo.


        :param auth: The auth of this DisassociateEcsServerInfo.
        :type auth: :class:`huaweicloudsdkkps.v3.Auth`
        """
        self._auth = auth

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
        if not isinstance(other, DisassociateEcsServerInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
