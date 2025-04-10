# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteGrantRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'grantee_user': 'str',
        'resource_id': 'str'
    }

    attribute_map = {
        'grantee_user': 'grantee_user',
        'resource_id': 'resource_id'
    }

    def __init__(self, grantee_user=None, resource_id=None):
        r"""DeleteGrantRequest

        The model defined in huaweicloud sdk

        :param grantee_user: 被授权用户ID
        :type grantee_user: str
        :param resource_id: 被授权资源ID
        :type resource_id: str
        """
        
        

        self._grantee_user = None
        self._resource_id = None
        self.discriminator = None

        if grantee_user is not None:
            self.grantee_user = grantee_user
        self.resource_id = resource_id

    @property
    def grantee_user(self):
        r"""Gets the grantee_user of this DeleteGrantRequest.

        被授权用户ID

        :return: The grantee_user of this DeleteGrantRequest.
        :rtype: str
        """
        return self._grantee_user

    @grantee_user.setter
    def grantee_user(self, grantee_user):
        r"""Sets the grantee_user of this DeleteGrantRequest.

        被授权用户ID

        :param grantee_user: The grantee_user of this DeleteGrantRequest.
        :type grantee_user: str
        """
        self._grantee_user = grantee_user

    @property
    def resource_id(self):
        r"""Gets the resource_id of this DeleteGrantRequest.

        被授权资源ID

        :return: The resource_id of this DeleteGrantRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this DeleteGrantRequest.

        被授权资源ID

        :param resource_id: The resource_id of this DeleteGrantRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

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
        if not isinstance(other, DeleteGrantRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
