# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePubInfoRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pub_request_body': 'PubInfoRequestBody',
        'portal_request_body': 'PortalInfoRequestBody',
        'menu_request_body': 'MenuInfoRequestBody'
    }

    attribute_map = {
        'pub_request_body': 'pub_request_body',
        'portal_request_body': 'portal_request_body',
        'menu_request_body': 'menu_request_body'
    }

    def __init__(self, pub_request_body=None, portal_request_body=None, menu_request_body=None):
        """CreatePubInfoRequestBody

        The model defined in huaweicloud sdk

        :param pub_request_body: 
        :type pub_request_body: :class:`huaweicloudsdkkoomessage.v1.PubInfoRequestBody`
        :param portal_request_body: 
        :type portal_request_body: :class:`huaweicloudsdkkoomessage.v1.PortalInfoRequestBody`
        :param menu_request_body: 
        :type menu_request_body: :class:`huaweicloudsdkkoomessage.v1.MenuInfoRequestBody`
        """
        
        

        self._pub_request_body = None
        self._portal_request_body = None
        self._menu_request_body = None
        self.discriminator = None

        self.pub_request_body = pub_request_body
        self.portal_request_body = portal_request_body
        self.menu_request_body = menu_request_body

    @property
    def pub_request_body(self):
        """Gets the pub_request_body of this CreatePubInfoRequestBody.

        :return: The pub_request_body of this CreatePubInfoRequestBody.
        :rtype: :class:`huaweicloudsdkkoomessage.v1.PubInfoRequestBody`
        """
        return self._pub_request_body

    @pub_request_body.setter
    def pub_request_body(self, pub_request_body):
        """Sets the pub_request_body of this CreatePubInfoRequestBody.

        :param pub_request_body: The pub_request_body of this CreatePubInfoRequestBody.
        :type pub_request_body: :class:`huaweicloudsdkkoomessage.v1.PubInfoRequestBody`
        """
        self._pub_request_body = pub_request_body

    @property
    def portal_request_body(self):
        """Gets the portal_request_body of this CreatePubInfoRequestBody.

        :return: The portal_request_body of this CreatePubInfoRequestBody.
        :rtype: :class:`huaweicloudsdkkoomessage.v1.PortalInfoRequestBody`
        """
        return self._portal_request_body

    @portal_request_body.setter
    def portal_request_body(self, portal_request_body):
        """Sets the portal_request_body of this CreatePubInfoRequestBody.

        :param portal_request_body: The portal_request_body of this CreatePubInfoRequestBody.
        :type portal_request_body: :class:`huaweicloudsdkkoomessage.v1.PortalInfoRequestBody`
        """
        self._portal_request_body = portal_request_body

    @property
    def menu_request_body(self):
        """Gets the menu_request_body of this CreatePubInfoRequestBody.

        :return: The menu_request_body of this CreatePubInfoRequestBody.
        :rtype: :class:`huaweicloudsdkkoomessage.v1.MenuInfoRequestBody`
        """
        return self._menu_request_body

    @menu_request_body.setter
    def menu_request_body(self, menu_request_body):
        """Sets the menu_request_body of this CreatePubInfoRequestBody.

        :param menu_request_body: The menu_request_body of this CreatePubInfoRequestBody.
        :type menu_request_body: :class:`huaweicloudsdkkoomessage.v1.MenuInfoRequestBody`
        """
        self._menu_request_body = menu_request_body

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
        if not isinstance(other, CreatePubInfoRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
