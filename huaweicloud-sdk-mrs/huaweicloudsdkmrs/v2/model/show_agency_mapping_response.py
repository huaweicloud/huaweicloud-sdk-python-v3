# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAgencyMappingResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agency_mappings': 'list[AgencyMapping]'
    }

    attribute_map = {
        'agency_mappings': 'agency_mappings'
    }

    def __init__(self, agency_mappings=None):
        """ShowAgencyMappingResponse

        The model defined in huaweicloud sdk

        :param agency_mappings: 用户（组）与委托之间的映射关系详细信息。
        :type agency_mappings: list[:class:`huaweicloudsdkmrs.v2.AgencyMapping`]
        """
        
        super(ShowAgencyMappingResponse, self).__init__()

        self._agency_mappings = None
        self.discriminator = None

        if agency_mappings is not None:
            self.agency_mappings = agency_mappings

    @property
    def agency_mappings(self):
        """Gets the agency_mappings of this ShowAgencyMappingResponse.

        用户（组）与委托之间的映射关系详细信息。

        :return: The agency_mappings of this ShowAgencyMappingResponse.
        :rtype: list[:class:`huaweicloudsdkmrs.v2.AgencyMapping`]
        """
        return self._agency_mappings

    @agency_mappings.setter
    def agency_mappings(self, agency_mappings):
        """Sets the agency_mappings of this ShowAgencyMappingResponse.

        用户（组）与委托之间的映射关系详细信息。

        :param agency_mappings: The agency_mappings of this ShowAgencyMappingResponse.
        :type agency_mappings: list[:class:`huaweicloudsdkmrs.v2.AgencyMapping`]
        """
        self._agency_mappings = agency_mappings

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
        if not isinstance(other, ShowAgencyMappingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
