# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCertificateAuthorityObsAgencyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'agency_granted': 'str'
    }

    attribute_map = {
        'agency_granted': 'agency_granted'
    }

    def __init__(self, agency_granted=None):
        """ShowCertificateAuthorityObsAgencyResponse

        The model defined in huaweicloud sdk

        :param agency_granted: OBS当前的授权结果。 - **true** - **false**
        :type agency_granted: str
        """
        
        super(ShowCertificateAuthorityObsAgencyResponse, self).__init__()

        self._agency_granted = None
        self.discriminator = None

        if agency_granted is not None:
            self.agency_granted = agency_granted

    @property
    def agency_granted(self):
        """Gets the agency_granted of this ShowCertificateAuthorityObsAgencyResponse.

        OBS当前的授权结果。 - **true** - **false**

        :return: The agency_granted of this ShowCertificateAuthorityObsAgencyResponse.
        :rtype: str
        """
        return self._agency_granted

    @agency_granted.setter
    def agency_granted(self, agency_granted):
        """Sets the agency_granted of this ShowCertificateAuthorityObsAgencyResponse.

        OBS当前的授权结果。 - **true** - **false**

        :param agency_granted: The agency_granted of this ShowCertificateAuthorityObsAgencyResponse.
        :type agency_granted: str
        """
        self._agency_granted = agency_granted

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
        if not isinstance(other, ShowCertificateAuthorityObsAgencyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
