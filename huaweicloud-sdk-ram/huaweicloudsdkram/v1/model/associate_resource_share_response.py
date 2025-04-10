# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateResourceShareResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_share_associations': 'list[ResourceShareAssociation]'
    }

    attribute_map = {
        'resource_share_associations': 'resource_share_associations'
    }

    def __init__(self, resource_share_associations=None):
        r"""AssociateResourceShareResponse

        The model defined in huaweicloud sdk

        :param resource_share_associations: 
        :type resource_share_associations: list[:class:`huaweicloudsdkram.v1.ResourceShareAssociation`]
        """
        
        super(AssociateResourceShareResponse, self).__init__()

        self._resource_share_associations = None
        self.discriminator = None

        if resource_share_associations is not None:
            self.resource_share_associations = resource_share_associations

    @property
    def resource_share_associations(self):
        r"""Gets the resource_share_associations of this AssociateResourceShareResponse.

        :return: The resource_share_associations of this AssociateResourceShareResponse.
        :rtype: list[:class:`huaweicloudsdkram.v1.ResourceShareAssociation`]
        """
        return self._resource_share_associations

    @resource_share_associations.setter
    def resource_share_associations(self, resource_share_associations):
        r"""Sets the resource_share_associations of this AssociateResourceShareResponse.

        :param resource_share_associations: The resource_share_associations of this AssociateResourceShareResponse.
        :type resource_share_associations: list[:class:`huaweicloudsdkram.v1.ResourceShareAssociation`]
        """
        self._resource_share_associations = resource_share_associations

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
        if not isinstance(other, AssociateResourceShareResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
