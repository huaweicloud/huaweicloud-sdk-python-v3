# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetupLandingZoneReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('identity_store_email')

    openapi_types = {
        'identity_store_email': 'str',
        'home_region': 'str',
        'setup_landing_zone_action_type': 'str',
        'region_configuration_list': 'list[RegionConfigurationList]',
        'organization_structure': 'list[OrganizationStructureBaseLine]',
        'deny_ungoverned_regions': 'bool',
        'cloud_trail_type': 'bool',
        'kms_key_id': 'str',
        'logging_configuration': 'SetupLandingZoneReqBodyLoggingConfiguration'
    }

    attribute_map = {
        'identity_store_email': 'identity_store_email',
        'home_region': 'home_region',
        'setup_landing_zone_action_type': 'setup_landing_zone_action_type',
        'region_configuration_list': 'region_configuration_list',
        'organization_structure': 'organization_structure',
        'deny_ungoverned_regions': 'deny_ungoverned_regions',
        'cloud_trail_type': 'cloud_trail_type',
        'kms_key_id': 'kms_key_id',
        'logging_configuration': 'logging_configuration'
    }

    def __init__(self, identity_store_email=None, home_region=None, setup_landing_zone_action_type=None, region_configuration_list=None, organization_structure=None, deny_ungoverned_regions=None, cloud_trail_type=None, kms_key_id=None, logging_configuration=None):
        """SetupLandingZoneReqBody

        The model defined in huaweicloud sdk

        :param identity_store_email: 管理员纳管账号创建Identity Center用户所用邮箱。
        :type identity_store_email: str
        :param home_region: 主区域。
        :type home_region: str
        :param setup_landing_zone_action_type: 设置Landing Zone的类型。包括CREATE、REPAIR以及UPDATE。
        :type setup_landing_zone_action_type: str
        :param region_configuration_list: 当前纳管账号纳管的区域。
        :type region_configuration_list: list[:class:`huaweicloudsdkrgc.v1.RegionConfigurationList`]
        :param organization_structure: 基础环境的纳管账号体系。
        :type organization_structure: list[:class:`huaweicloudsdkrgc.v1.OrganizationStructureBaseLine`]
        :param deny_ungoverned_regions: 是否允许区域拒绝，默认false。
        :type deny_ungoverned_regions: bool
        :param cloud_trail_type: 是否允许设置组织汇聚。
        :type cloud_trail_type: bool
        :param kms_key_id: 加密字段。
        :type kms_key_id: str
        :param logging_configuration: 
        :type logging_configuration: :class:`huaweicloudsdkrgc.v1.SetupLandingZoneReqBodyLoggingConfiguration`
        """
        
        

        self._identity_store_email = None
        self._home_region = None
        self._setup_landing_zone_action_type = None
        self._region_configuration_list = None
        self._organization_structure = None
        self._deny_ungoverned_regions = None
        self._cloud_trail_type = None
        self._kms_key_id = None
        self._logging_configuration = None
        self.discriminator = None

        self.identity_store_email = identity_store_email
        self.home_region = home_region
        self.setup_landing_zone_action_type = setup_landing_zone_action_type
        self.region_configuration_list = region_configuration_list
        self.organization_structure = organization_structure
        if deny_ungoverned_regions is not None:
            self.deny_ungoverned_regions = deny_ungoverned_regions
        if cloud_trail_type is not None:
            self.cloud_trail_type = cloud_trail_type
        if kms_key_id is not None:
            self.kms_key_id = kms_key_id
        self.logging_configuration = logging_configuration

    @property
    def identity_store_email(self):
        """Gets the identity_store_email of this SetupLandingZoneReqBody.

        管理员纳管账号创建Identity Center用户所用邮箱。

        :return: The identity_store_email of this SetupLandingZoneReqBody.
        :rtype: str
        """
        return self._identity_store_email

    @identity_store_email.setter
    def identity_store_email(self, identity_store_email):
        """Sets the identity_store_email of this SetupLandingZoneReqBody.

        管理员纳管账号创建Identity Center用户所用邮箱。

        :param identity_store_email: The identity_store_email of this SetupLandingZoneReqBody.
        :type identity_store_email: str
        """
        self._identity_store_email = identity_store_email

    @property
    def home_region(self):
        """Gets the home_region of this SetupLandingZoneReqBody.

        主区域。

        :return: The home_region of this SetupLandingZoneReqBody.
        :rtype: str
        """
        return self._home_region

    @home_region.setter
    def home_region(self, home_region):
        """Sets the home_region of this SetupLandingZoneReqBody.

        主区域。

        :param home_region: The home_region of this SetupLandingZoneReqBody.
        :type home_region: str
        """
        self._home_region = home_region

    @property
    def setup_landing_zone_action_type(self):
        """Gets the setup_landing_zone_action_type of this SetupLandingZoneReqBody.

        设置Landing Zone的类型。包括CREATE、REPAIR以及UPDATE。

        :return: The setup_landing_zone_action_type of this SetupLandingZoneReqBody.
        :rtype: str
        """
        return self._setup_landing_zone_action_type

    @setup_landing_zone_action_type.setter
    def setup_landing_zone_action_type(self, setup_landing_zone_action_type):
        """Sets the setup_landing_zone_action_type of this SetupLandingZoneReqBody.

        设置Landing Zone的类型。包括CREATE、REPAIR以及UPDATE。

        :param setup_landing_zone_action_type: The setup_landing_zone_action_type of this SetupLandingZoneReqBody.
        :type setup_landing_zone_action_type: str
        """
        self._setup_landing_zone_action_type = setup_landing_zone_action_type

    @property
    def region_configuration_list(self):
        """Gets the region_configuration_list of this SetupLandingZoneReqBody.

        当前纳管账号纳管的区域。

        :return: The region_configuration_list of this SetupLandingZoneReqBody.
        :rtype: list[:class:`huaweicloudsdkrgc.v1.RegionConfigurationList`]
        """
        return self._region_configuration_list

    @region_configuration_list.setter
    def region_configuration_list(self, region_configuration_list):
        """Sets the region_configuration_list of this SetupLandingZoneReqBody.

        当前纳管账号纳管的区域。

        :param region_configuration_list: The region_configuration_list of this SetupLandingZoneReqBody.
        :type region_configuration_list: list[:class:`huaweicloudsdkrgc.v1.RegionConfigurationList`]
        """
        self._region_configuration_list = region_configuration_list

    @property
    def organization_structure(self):
        """Gets the organization_structure of this SetupLandingZoneReqBody.

        基础环境的纳管账号体系。

        :return: The organization_structure of this SetupLandingZoneReqBody.
        :rtype: list[:class:`huaweicloudsdkrgc.v1.OrganizationStructureBaseLine`]
        """
        return self._organization_structure

    @organization_structure.setter
    def organization_structure(self, organization_structure):
        """Sets the organization_structure of this SetupLandingZoneReqBody.

        基础环境的纳管账号体系。

        :param organization_structure: The organization_structure of this SetupLandingZoneReqBody.
        :type organization_structure: list[:class:`huaweicloudsdkrgc.v1.OrganizationStructureBaseLine`]
        """
        self._organization_structure = organization_structure

    @property
    def deny_ungoverned_regions(self):
        """Gets the deny_ungoverned_regions of this SetupLandingZoneReqBody.

        是否允许区域拒绝，默认false。

        :return: The deny_ungoverned_regions of this SetupLandingZoneReqBody.
        :rtype: bool
        """
        return self._deny_ungoverned_regions

    @deny_ungoverned_regions.setter
    def deny_ungoverned_regions(self, deny_ungoverned_regions):
        """Sets the deny_ungoverned_regions of this SetupLandingZoneReqBody.

        是否允许区域拒绝，默认false。

        :param deny_ungoverned_regions: The deny_ungoverned_regions of this SetupLandingZoneReqBody.
        :type deny_ungoverned_regions: bool
        """
        self._deny_ungoverned_regions = deny_ungoverned_regions

    @property
    def cloud_trail_type(self):
        """Gets the cloud_trail_type of this SetupLandingZoneReqBody.

        是否允许设置组织汇聚。

        :return: The cloud_trail_type of this SetupLandingZoneReqBody.
        :rtype: bool
        """
        return self._cloud_trail_type

    @cloud_trail_type.setter
    def cloud_trail_type(self, cloud_trail_type):
        """Sets the cloud_trail_type of this SetupLandingZoneReqBody.

        是否允许设置组织汇聚。

        :param cloud_trail_type: The cloud_trail_type of this SetupLandingZoneReqBody.
        :type cloud_trail_type: bool
        """
        self._cloud_trail_type = cloud_trail_type

    @property
    def kms_key_id(self):
        """Gets the kms_key_id of this SetupLandingZoneReqBody.

        加密字段。

        :return: The kms_key_id of this SetupLandingZoneReqBody.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """Sets the kms_key_id of this SetupLandingZoneReqBody.

        加密字段。

        :param kms_key_id: The kms_key_id of this SetupLandingZoneReqBody.
        :type kms_key_id: str
        """
        self._kms_key_id = kms_key_id

    @property
    def logging_configuration(self):
        """Gets the logging_configuration of this SetupLandingZoneReqBody.

        :return: The logging_configuration of this SetupLandingZoneReqBody.
        :rtype: :class:`huaweicloudsdkrgc.v1.SetupLandingZoneReqBodyLoggingConfiguration`
        """
        return self._logging_configuration

    @logging_configuration.setter
    def logging_configuration(self, logging_configuration):
        """Sets the logging_configuration of this SetupLandingZoneReqBody.

        :param logging_configuration: The logging_configuration of this SetupLandingZoneReqBody.
        :type logging_configuration: :class:`huaweicloudsdkrgc.v1.SetupLandingZoneReqBodyLoggingConfiguration`
        """
        self._logging_configuration = logging_configuration

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
        if not isinstance(other, SetupLandingZoneReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
