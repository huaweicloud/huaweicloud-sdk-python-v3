# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class CreateCertificateAuthorityObsAgencyResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'agency_id': 'str'
    }

    attribute_map = {
        'agency_id': 'agency_id'
    }

    def __init__(self, agency_id=None):
        """CreateCertificateAuthorityObsAgencyResponse - a model defined in huaweicloud sdk"""
        
        super(CreateCertificateAuthorityObsAgencyResponse, self).__init__()

        self._agency_id = None
        self.discriminator = None

        if agency_id is not None:
            self.agency_id = agency_id

    @property
    def agency_id(self):
        """Gets the agency_id of this CreateCertificateAuthorityObsAgencyResponse.

        授权ID

        :return: The agency_id of this CreateCertificateAuthorityObsAgencyResponse.
        :rtype: str
        """
        return self._agency_id

    @agency_id.setter
    def agency_id(self, agency_id):
        """Sets the agency_id of this CreateCertificateAuthorityObsAgencyResponse.

        授权ID

        :param agency_id: The agency_id of this CreateCertificateAuthorityObsAgencyResponse.
        :type: str
        """
        self._agency_id = agency_id

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
        import simplejson as json
        return json.dumps(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateCertificateAuthorityObsAgencyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
