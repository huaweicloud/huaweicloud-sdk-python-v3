# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociationRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'attachment_id': 'str',
        'route_policy': 'ExportRoutePolicy'
    }

    attribute_map = {
        'attachment_id': 'attachment_id',
        'route_policy': 'route_policy'
    }

    def __init__(self, attachment_id=None, route_policy=None):
        """AssociationRequestBody

        The model defined in huaweicloud sdk

        :param attachment_id: 连接唯一标识
        :type attachment_id: str
        :param route_policy: 
        :type route_policy: :class:`huaweicloudsdker.v3.ExportRoutePolicy`
        """
        
        

        self._attachment_id = None
        self._route_policy = None
        self.discriminator = None

        if attachment_id is not None:
            self.attachment_id = attachment_id
        if route_policy is not None:
            self.route_policy = route_policy

    @property
    def attachment_id(self):
        """Gets the attachment_id of this AssociationRequestBody.

        连接唯一标识

        :return: The attachment_id of this AssociationRequestBody.
        :rtype: str
        """
        return self._attachment_id

    @attachment_id.setter
    def attachment_id(self, attachment_id):
        """Sets the attachment_id of this AssociationRequestBody.

        连接唯一标识

        :param attachment_id: The attachment_id of this AssociationRequestBody.
        :type attachment_id: str
        """
        self._attachment_id = attachment_id

    @property
    def route_policy(self):
        """Gets the route_policy of this AssociationRequestBody.


        :return: The route_policy of this AssociationRequestBody.
        :rtype: :class:`huaweicloudsdker.v3.ExportRoutePolicy`
        """
        return self._route_policy

    @route_policy.setter
    def route_policy(self, route_policy):
        """Sets the route_policy of this AssociationRequestBody.


        :param route_policy: The route_policy of this AssociationRequestBody.
        :type route_policy: :class:`huaweicloudsdker.v3.ExportRoutePolicy`
        """
        self._route_policy = route_policy

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
        if not isinstance(other, AssociationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
