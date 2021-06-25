# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListCaseCountsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'incident_status_counts': 'list[IncidentStatusCount]'
    }

    attribute_map = {
        'incident_status_counts': 'incident_status_counts'
    }

    def __init__(self, incident_status_counts=None):
        """ListCaseCountsResponse - a model defined in huaweicloud sdk"""
        
        super(ListCaseCountsResponse, self).__init__()

        self._incident_status_counts = None
        self.discriminator = None

        if incident_status_counts is not None:
            self.incident_status_counts = incident_status_counts

    @property
    def incident_status_counts(self):
        """Gets the incident_status_counts of this ListCaseCountsResponse.

        状态数量统计列表

        :return: The incident_status_counts of this ListCaseCountsResponse.
        :rtype: list[IncidentStatusCount]
        """
        return self._incident_status_counts

    @incident_status_counts.setter
    def incident_status_counts(self, incident_status_counts):
        """Sets the incident_status_counts of this ListCaseCountsResponse.

        状态数量统计列表

        :param incident_status_counts: The incident_status_counts of this ListCaseCountsResponse.
        :type: list[IncidentStatusCount]
        """
        self._incident_status_counts = incident_status_counts

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListCaseCountsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other