# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLandingZoneConfigurationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'common_configuration': 'CommonConfiguration',
        'logging_configuration': 'LoggingConfiguration',
        'organization_structure': 'list[OrganizationStructureBaseLineRsp]',
        'regions': 'list[RegionConfigurationList]'
    }

    attribute_map = {
        'common_configuration': 'common_configuration',
        'logging_configuration': 'logging_configuration',
        'organization_structure': 'organization_structure',
        'regions': 'regions'
    }

    def __init__(self, common_configuration=None, logging_configuration=None, organization_structure=None, regions=None):
        r"""ShowLandingZoneConfigurationResponse

        The model defined in huaweicloud sdk

        :param common_configuration: 
        :type common_configuration: :class:`huaweicloudsdkrgc.v1.CommonConfiguration`
        :param logging_configuration: 
        :type logging_configuration: :class:`huaweicloudsdkrgc.v1.LoggingConfiguration`
        :param organization_structure: 
        :type organization_structure: list[:class:`huaweicloudsdkrgc.v1.OrganizationStructureBaseLineRsp`]
        :param regions: 纳管的区域信息。
        :type regions: list[:class:`huaweicloudsdkrgc.v1.RegionConfigurationList`]
        """
        
        super(ShowLandingZoneConfigurationResponse, self).__init__()

        self._common_configuration = None
        self._logging_configuration = None
        self._organization_structure = None
        self._regions = None
        self.discriminator = None

        if common_configuration is not None:
            self.common_configuration = common_configuration
        if logging_configuration is not None:
            self.logging_configuration = logging_configuration
        if organization_structure is not None:
            self.organization_structure = organization_structure
        if regions is not None:
            self.regions = regions

    @property
    def common_configuration(self):
        r"""Gets the common_configuration of this ShowLandingZoneConfigurationResponse.

        :return: The common_configuration of this ShowLandingZoneConfigurationResponse.
        :rtype: :class:`huaweicloudsdkrgc.v1.CommonConfiguration`
        """
        return self._common_configuration

    @common_configuration.setter
    def common_configuration(self, common_configuration):
        r"""Sets the common_configuration of this ShowLandingZoneConfigurationResponse.

        :param common_configuration: The common_configuration of this ShowLandingZoneConfigurationResponse.
        :type common_configuration: :class:`huaweicloudsdkrgc.v1.CommonConfiguration`
        """
        self._common_configuration = common_configuration

    @property
    def logging_configuration(self):
        r"""Gets the logging_configuration of this ShowLandingZoneConfigurationResponse.

        :return: The logging_configuration of this ShowLandingZoneConfigurationResponse.
        :rtype: :class:`huaweicloudsdkrgc.v1.LoggingConfiguration`
        """
        return self._logging_configuration

    @logging_configuration.setter
    def logging_configuration(self, logging_configuration):
        r"""Sets the logging_configuration of this ShowLandingZoneConfigurationResponse.

        :param logging_configuration: The logging_configuration of this ShowLandingZoneConfigurationResponse.
        :type logging_configuration: :class:`huaweicloudsdkrgc.v1.LoggingConfiguration`
        """
        self._logging_configuration = logging_configuration

    @property
    def organization_structure(self):
        r"""Gets the organization_structure of this ShowLandingZoneConfigurationResponse.

        :return: The organization_structure of this ShowLandingZoneConfigurationResponse.
        :rtype: list[:class:`huaweicloudsdkrgc.v1.OrganizationStructureBaseLineRsp`]
        """
        return self._organization_structure

    @organization_structure.setter
    def organization_structure(self, organization_structure):
        r"""Sets the organization_structure of this ShowLandingZoneConfigurationResponse.

        :param organization_structure: The organization_structure of this ShowLandingZoneConfigurationResponse.
        :type organization_structure: list[:class:`huaweicloudsdkrgc.v1.OrganizationStructureBaseLineRsp`]
        """
        self._organization_structure = organization_structure

    @property
    def regions(self):
        r"""Gets the regions of this ShowLandingZoneConfigurationResponse.

        纳管的区域信息。

        :return: The regions of this ShowLandingZoneConfigurationResponse.
        :rtype: list[:class:`huaweicloudsdkrgc.v1.RegionConfigurationList`]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        r"""Sets the regions of this ShowLandingZoneConfigurationResponse.

        纳管的区域信息。

        :param regions: The regions of this ShowLandingZoneConfigurationResponse.
        :type regions: list[:class:`huaweicloudsdkrgc.v1.RegionConfigurationList`]
        """
        self._regions = regions

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
        if not isinstance(other, ShowLandingZoneConfigurationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
