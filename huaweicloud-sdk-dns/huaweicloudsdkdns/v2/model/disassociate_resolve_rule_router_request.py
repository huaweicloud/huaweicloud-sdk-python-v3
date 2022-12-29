# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisassociateResolveRuleRouterRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resolverrule_id': 'str',
        'body': 'DisassociaterouterReq'
    }

    attribute_map = {
        'resolverrule_id': 'resolverrule_id',
        'body': 'body'
    }

    def __init__(self, resolverrule_id=None, body=None):
        """DisassociateResolveRuleRouterRequest

        The model defined in huaweicloud sdk

        :param resolverrule_id: 待解关联resolverrule的ID。
        :type resolverrule_id: str
        :param body: Body of the DisassociateResolveRuleRouterRequest
        :type body: :class:`huaweicloudsdkdns.v2.DisassociaterouterReq`
        """
        
        

        self._resolverrule_id = None
        self._body = None
        self.discriminator = None

        self.resolverrule_id = resolverrule_id
        if body is not None:
            self.body = body

    @property
    def resolverrule_id(self):
        """Gets the resolverrule_id of this DisassociateResolveRuleRouterRequest.

        待解关联resolverrule的ID。

        :return: The resolverrule_id of this DisassociateResolveRuleRouterRequest.
        :rtype: str
        """
        return self._resolverrule_id

    @resolverrule_id.setter
    def resolverrule_id(self, resolverrule_id):
        """Sets the resolverrule_id of this DisassociateResolveRuleRouterRequest.

        待解关联resolverrule的ID。

        :param resolverrule_id: The resolverrule_id of this DisassociateResolveRuleRouterRequest.
        :type resolverrule_id: str
        """
        self._resolverrule_id = resolverrule_id

    @property
    def body(self):
        """Gets the body of this DisassociateResolveRuleRouterRequest.

        :return: The body of this DisassociateResolveRuleRouterRequest.
        :rtype: :class:`huaweicloudsdkdns.v2.DisassociaterouterReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this DisassociateResolveRuleRouterRequest.

        :param body: The body of this DisassociateResolveRuleRouterRequest.
        :type body: :class:`huaweicloudsdkdns.v2.DisassociaterouterReq`
        """
        self._body = body

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
        if not isinstance(other, DisassociateResolveRuleRouterRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
