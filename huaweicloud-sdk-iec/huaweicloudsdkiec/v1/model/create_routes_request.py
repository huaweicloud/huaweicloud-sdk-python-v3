# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRoutesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'routetable_id': 'str',
        'body': 'CreateRoutesRequestBody'
    }

    attribute_map = {
        'routetable_id': 'routetable_id',
        'body': 'body'
    }

    def __init__(self, routetable_id=None, body=None):
        """CreateRoutesRequest

        The model defined in huaweicloud sdk

        :param routetable_id: 路由表ID
        :type routetable_id: str
        :param body: Body of the CreateRoutesRequest
        :type body: :class:`huaweicloudsdkiec.v1.CreateRoutesRequestBody`
        """
        
        

        self._routetable_id = None
        self._body = None
        self.discriminator = None

        self.routetable_id = routetable_id
        if body is not None:
            self.body = body

    @property
    def routetable_id(self):
        """Gets the routetable_id of this CreateRoutesRequest.

        路由表ID

        :return: The routetable_id of this CreateRoutesRequest.
        :rtype: str
        """
        return self._routetable_id

    @routetable_id.setter
    def routetable_id(self, routetable_id):
        """Sets the routetable_id of this CreateRoutesRequest.

        路由表ID

        :param routetable_id: The routetable_id of this CreateRoutesRequest.
        :type routetable_id: str
        """
        self._routetable_id = routetable_id

    @property
    def body(self):
        """Gets the body of this CreateRoutesRequest.

        :return: The body of this CreateRoutesRequest.
        :rtype: :class:`huaweicloudsdkiec.v1.CreateRoutesRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateRoutesRequest.

        :param body: The body of this CreateRoutesRequest.
        :type body: :class:`huaweicloudsdkiec.v1.CreateRoutesRequestBody`
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
        if not isinstance(other, CreateRoutesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
