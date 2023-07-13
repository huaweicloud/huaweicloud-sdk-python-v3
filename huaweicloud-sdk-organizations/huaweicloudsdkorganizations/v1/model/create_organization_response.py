# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOrganizationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'organization': 'OrganizationDto'
    }

    attribute_map = {
        'organization': 'organization'
    }

    def __init__(self, organization=None):
        """CreateOrganizationResponse

        The model defined in huaweicloud sdk

        :param organization: 
        :type organization: :class:`huaweicloudsdkorganizations.v1.OrganizationDto`
        """
        
        super(CreateOrganizationResponse, self).__init__()

        self._organization = None
        self.discriminator = None

        if organization is not None:
            self.organization = organization

    @property
    def organization(self):
        """Gets the organization of this CreateOrganizationResponse.

        :return: The organization of this CreateOrganizationResponse.
        :rtype: :class:`huaweicloudsdkorganizations.v1.OrganizationDto`
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this CreateOrganizationResponse.

        :param organization: The organization of this CreateOrganizationResponse.
        :type organization: :class:`huaweicloudsdkorganizations.v1.OrganizationDto`
        """
        self._organization = organization

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
        if not isinstance(other, CreateOrganizationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
