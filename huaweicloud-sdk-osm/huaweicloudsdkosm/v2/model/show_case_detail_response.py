# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowCaseDetailResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'incident_detail_info': 'IncidentDetailInfoV2'
    }

    attribute_map = {
        'incident_detail_info': 'incident_detail_info'
    }

    def __init__(self, incident_detail_info=None):
        """ShowCaseDetailResponse - a model defined in huaweicloud sdk"""
        
        super(ShowCaseDetailResponse, self).__init__()

        self._incident_detail_info = None
        self.discriminator = None

        if incident_detail_info is not None:
            self.incident_detail_info = incident_detail_info

    @property
    def incident_detail_info(self):
        """Gets the incident_detail_info of this ShowCaseDetailResponse.


        :return: The incident_detail_info of this ShowCaseDetailResponse.
        :rtype: IncidentDetailInfoV2
        """
        return self._incident_detail_info

    @incident_detail_info.setter
    def incident_detail_info(self, incident_detail_info):
        """Sets the incident_detail_info of this ShowCaseDetailResponse.


        :param incident_detail_info: The incident_detail_info of this ShowCaseDetailResponse.
        :type: IncidentDetailInfoV2
        """
        self._incident_detail_info = incident_detail_info

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
        if not isinstance(other, ShowCaseDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other