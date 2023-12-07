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
        'organization_structure': 'list[OrganizationStructureBaseLine]',
        'regions': 'list[RegionConfigurationList]',
        'identity_store_email': 'str'
    }

    attribute_map = {
        'common_configuration': 'common_configuration',
        'logging_configuration': 'logging_configuration',
        'organization_structure': 'organization_structure',
        'regions': 'regions',
        'identity_store_email': 'identity_store_email'
    }

    def __init__(self, common_configuration=None, logging_configuration=None, organization_structure=None, regions=None, identity_store_email=None):
        """ShowLandingZoneConfigurationResponse

        The model defined in huaweicloud sdk

        :param common_configuration: 
        :type common_configuration: :class:`huaweicloudsdkrgc.v1.CommonConfiguration`
        :param logging_configuration: 
        :type logging_configuration: :class:`huaweicloudsdkrgc.v1.LoggingConfiguration`
        :param organization_structure: 
        :type organization_structure: list[:class:`huaweicloudsdkrgc.v1.OrganizationStructureBaseLine`]
        :param regions: 纳管的区域
        :type regions: list[:class:`huaweicloudsdkrgc.v1.RegionConfigurationList`]
        :param identity_store_email: 管理员账号创建Identity Center用户所用邮箱
        :type identity_store_email: str
        """
        
        super(ShowLandingZoneConfigurationResponse, self).__init__()

        self._common_configuration = None
        self._logging_configuration = None
        self._organization_structure = None
        self._regions = None
        self._identity_store_email = None
        self.discriminator = None

        if common_configuration is not None:
            self.common_configuration = common_configuration
        if logging_configuration is not None:
            self.logging_configuration = logging_configuration
        if organization_structure is not None:
            self.organization_structure = organization_structure
        if regions is not None:
            self.regions = regions
        if identity_store_email is not None:
            self.identity_store_email = identity_store_email

    @property
    def common_configuration(self):
        """Gets the common_configuration of this ShowLandingZoneConfigurationResponse.

        :return: The common_configuration of this ShowLandingZoneConfigurationResponse.
        :rtype: :class:`huaweicloudsdkrgc.v1.CommonConfiguration`
        """
        return self._common_configuration

    @common_configuration.setter
    def common_configuration(self, common_configuration):
        """Sets the common_configuration of this ShowLandingZoneConfigurationResponse.

        :param common_configuration: The common_configuration of this ShowLandingZoneConfigurationResponse.
        :type common_configuration: :class:`huaweicloudsdkrgc.v1.CommonConfiguration`
        """
        self._common_configuration = common_configuration

    @property
    def logging_configuration(self):
        """Gets the logging_configuration of this ShowLandingZoneConfigurationResponse.

        :return: The logging_configuration of this ShowLandingZoneConfigurationResponse.
        :rtype: :class:`huaweicloudsdkrgc.v1.LoggingConfiguration`
        """
        return self._logging_configuration

    @logging_configuration.setter
    def logging_configuration(self, logging_configuration):
        """Sets the logging_configuration of this ShowLandingZoneConfigurationResponse.

        :param logging_configuration: The logging_configuration of this ShowLandingZoneConfigurationResponse.
        :type logging_configuration: :class:`huaweicloudsdkrgc.v1.LoggingConfiguration`
        """
        self._logging_configuration = logging_configuration

    @property
    def organization_structure(self):
        """Gets the organization_structure of this ShowLandingZoneConfigurationResponse.

        :return: The organization_structure of this ShowLandingZoneConfigurationResponse.
        :rtype: list[:class:`huaweicloudsdkrgc.v1.OrganizationStructureBaseLine`]
        """
        return self._organization_structure

    @organization_structure.setter
    def organization_structure(self, organization_structure):
        """Sets the organization_structure of this ShowLandingZoneConfigurationResponse.

        :param organization_structure: The organization_structure of this ShowLandingZoneConfigurationResponse.
        :type organization_structure: list[:class:`huaweicloudsdkrgc.v1.OrganizationStructureBaseLine`]
        """
        self._organization_structure = organization_structure

    @property
    def regions(self):
        """Gets the regions of this ShowLandingZoneConfigurationResponse.

        纳管的区域

        :return: The regions of this ShowLandingZoneConfigurationResponse.
        :rtype: list[:class:`huaweicloudsdkrgc.v1.RegionConfigurationList`]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        """Sets the regions of this ShowLandingZoneConfigurationResponse.

        纳管的区域

        :param regions: The regions of this ShowLandingZoneConfigurationResponse.
        :type regions: list[:class:`huaweicloudsdkrgc.v1.RegionConfigurationList`]
        """
        self._regions = regions

    @property
    def identity_store_email(self):
        """Gets the identity_store_email of this ShowLandingZoneConfigurationResponse.

        管理员账号创建Identity Center用户所用邮箱

        :return: The identity_store_email of this ShowLandingZoneConfigurationResponse.
        :rtype: str
        """
        return self._identity_store_email

    @identity_store_email.setter
    def identity_store_email(self, identity_store_email):
        """Sets the identity_store_email of this ShowLandingZoneConfigurationResponse.

        管理员账号创建Identity Center用户所用邮箱

        :param identity_store_email: The identity_store_email of this ShowLandingZoneConfigurationResponse.
        :type identity_store_email: str
        """
        self._identity_store_email = identity_store_email

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
