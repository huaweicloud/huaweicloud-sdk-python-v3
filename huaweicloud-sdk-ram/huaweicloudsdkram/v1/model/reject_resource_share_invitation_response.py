# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RejectResourceShareInvitationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_share_invitation': 'ResourceShareInvitation'
    }

    attribute_map = {
        'resource_share_invitation': 'resource_share_invitation'
    }

    def __init__(self, resource_share_invitation=None):
        """RejectResourceShareInvitationResponse

        The model defined in huaweicloud sdk

        :param resource_share_invitation: 
        :type resource_share_invitation: :class:`huaweicloudsdkram.v1.ResourceShareInvitation`
        """
        
        super(RejectResourceShareInvitationResponse, self).__init__()

        self._resource_share_invitation = None
        self.discriminator = None

        if resource_share_invitation is not None:
            self.resource_share_invitation = resource_share_invitation

    @property
    def resource_share_invitation(self):
        """Gets the resource_share_invitation of this RejectResourceShareInvitationResponse.

        :return: The resource_share_invitation of this RejectResourceShareInvitationResponse.
        :rtype: :class:`huaweicloudsdkram.v1.ResourceShareInvitation`
        """
        return self._resource_share_invitation

    @resource_share_invitation.setter
    def resource_share_invitation(self, resource_share_invitation):
        """Sets the resource_share_invitation of this RejectResourceShareInvitationResponse.

        :param resource_share_invitation: The resource_share_invitation of this RejectResourceShareInvitationResponse.
        :type resource_share_invitation: :class:`huaweicloudsdkram.v1.ResourceShareInvitation`
        """
        self._resource_share_invitation = resource_share_invitation

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
        if not isinstance(other, RejectResourceShareInvitationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
