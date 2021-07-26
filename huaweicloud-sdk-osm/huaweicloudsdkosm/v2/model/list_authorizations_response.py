# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAuthorizationsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'incident_auth_list': 'list[IncidentOrderAuthV2]'
    }

    attribute_map = {
        'total': 'total',
        'incident_auth_list': 'incident_auth_list'
    }

    def __init__(self, total=None, incident_auth_list=None):
        """ListAuthorizationsResponse - a model defined in huaweicloud sdk"""
        
        super(ListAuthorizationsResponse, self).__init__()

        self._total = None
        self._incident_auth_list = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if incident_auth_list is not None:
            self.incident_auth_list = incident_auth_list

    @property
    def total(self):
        """Gets the total of this ListAuthorizationsResponse.

        总数

        :return: The total of this ListAuthorizationsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListAuthorizationsResponse.

        总数

        :param total: The total of this ListAuthorizationsResponse.
        :type: int
        """
        self._total = total

    @property
    def incident_auth_list(self):
        """Gets the incident_auth_list of this ListAuthorizationsResponse.

        授权列表

        :return: The incident_auth_list of this ListAuthorizationsResponse.
        :rtype: list[IncidentOrderAuthV2]
        """
        return self._incident_auth_list

    @incident_auth_list.setter
    def incident_auth_list(self, incident_auth_list):
        """Sets the incident_auth_list of this ListAuthorizationsResponse.

        授权列表

        :param incident_auth_list: The incident_auth_list of this ListAuthorizationsResponse.
        :type: list[IncidentOrderAuthV2]
        """
        self._incident_auth_list = incident_auth_list

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
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListAuthorizationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
