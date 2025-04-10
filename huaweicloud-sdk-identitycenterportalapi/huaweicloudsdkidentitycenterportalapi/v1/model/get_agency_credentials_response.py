# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetAgencyCredentialsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agency_credentials': 'AgencyCredentials'
    }

    attribute_map = {
        'agency_credentials': 'agency_credentials'
    }

    def __init__(self, agency_credentials=None):
        r"""GetAgencyCredentialsResponse

        The model defined in huaweicloud sdk

        :param agency_credentials: 
        :type agency_credentials: :class:`huaweicloudsdkidentitycenterportalapi.v1.AgencyCredentials`
        """
        
        super(GetAgencyCredentialsResponse, self).__init__()

        self._agency_credentials = None
        self.discriminator = None

        if agency_credentials is not None:
            self.agency_credentials = agency_credentials

    @property
    def agency_credentials(self):
        r"""Gets the agency_credentials of this GetAgencyCredentialsResponse.

        :return: The agency_credentials of this GetAgencyCredentialsResponse.
        :rtype: :class:`huaweicloudsdkidentitycenterportalapi.v1.AgencyCredentials`
        """
        return self._agency_credentials

    @agency_credentials.setter
    def agency_credentials(self, agency_credentials):
        r"""Sets the agency_credentials of this GetAgencyCredentialsResponse.

        :param agency_credentials: The agency_credentials of this GetAgencyCredentialsResponse.
        :type agency_credentials: :class:`huaweicloudsdkidentitycenterportalapi.v1.AgencyCredentials`
        """
        self._agency_credentials = agency_credentials

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
        if not isinstance(other, GetAgencyCredentialsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
