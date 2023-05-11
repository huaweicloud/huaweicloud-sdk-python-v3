# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateOrganizationalUnitResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'organizational_unit': 'OrganizationalUnitDto'
    }

    attribute_map = {
        'organizational_unit': 'organizational_unit'
    }

    def __init__(self, organizational_unit=None):
        """UpdateOrganizationalUnitResponse

        The model defined in huaweicloud sdk

        :param organizational_unit: 
        :type organizational_unit: :class:`huaweicloudsdkorganizations.v1.OrganizationalUnitDto`
        """
        
        super(UpdateOrganizationalUnitResponse, self).__init__()

        self._organizational_unit = None
        self.discriminator = None

        if organizational_unit is not None:
            self.organizational_unit = organizational_unit

    @property
    def organizational_unit(self):
        """Gets the organizational_unit of this UpdateOrganizationalUnitResponse.

        :return: The organizational_unit of this UpdateOrganizationalUnitResponse.
        :rtype: :class:`huaweicloudsdkorganizations.v1.OrganizationalUnitDto`
        """
        return self._organizational_unit

    @organizational_unit.setter
    def organizational_unit(self, organizational_unit):
        """Sets the organizational_unit of this UpdateOrganizationalUnitResponse.

        :param organizational_unit: The organizational_unit of this UpdateOrganizationalUnitResponse.
        :type organizational_unit: :class:`huaweicloudsdkorganizations.v1.OrganizationalUnitDto`
        """
        self._organizational_unit = organizational_unit

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
        if not isinstance(other, UpdateOrganizationalUnitResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
