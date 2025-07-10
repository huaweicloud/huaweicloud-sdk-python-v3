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
        'identity_center_status': 'str',
        'organization_structure_type': 'str',
        'organization_structure': 'list[OrganizationStructureBaseLine]',
        'deny_ungoverned_regions': 'bool',
        'cloud_trail_type': 'bool',
        'kms_key_id': 'str',
        'logging_configuration': 'LoggingConfiguration',
        'baseline_version': 'str'
    }

    attribute_map = {
        'identity_store_email': 'identity_store_email',
        'home_region': 'home_region',
        'setup_landing_zone_action_type': 'setup_landing_zone_action_type',
        'region_configuration_list': 'region_configuration_list',
        'identity_center_status': 'identity_center_status',
        'organization_structure_type': 'organization_structure_type',
        'organization_structure': 'organization_structure',
        'deny_ungoverned_regions': 'deny_ungoverned_regions',
        'cloud_trail_type': 'cloud_trail_type',
        'kms_key_id': 'kms_key_id',
        'logging_configuration': 'logging_configuration',
        'baseline_version': 'baseline_version'
    }

    def __init__(self, identity_store_email=None, home_region=None, setup_landing_zone_action_type=None, region_configuration_list=None, identity_center_status=None, organization_structure_type=None, organization_structure=None, deny_ungoverned_regions=None, cloud_trail_type=None, kms_key_id=None, logging_configuration=None, baseline_version=None):
        r"""SetupLandingZoneReqBody

        The model defined in huaweicloud sdk

        :param identity_store_email: 管理员纳管账号创建Identity Center用户所用邮箱。
        :type identity_store_email: str
        :param home_region: 主区域。
        :type home_region: str
        :param setup_landing_zone_action_type: 设置Landing Zone的类型。包括CREATE、REPAIR以及UPDATE。
        :type setup_landing_zone_action_type: str
        :param region_configuration_list: 当前纳管账号纳管的区域。
        :type region_configuration_list: list[:class:`huaweicloudsdkrgc.v1.RegionConfigurationList`]
        :param identity_center_status: 是否设置Landing Zone的identity center。
        :type identity_center_status: str
        :param organization_structure_type: 设置organization的类型。STANDARD和NON_STANDARD。
        :type organization_structure_type: str
        :param organization_structure: 基础环境的纳管账号体系。
        :type organization_structure: list[:class:`huaweicloudsdkrgc.v1.OrganizationStructureBaseLine`]
        :param deny_ungoverned_regions: 是否允许区域拒绝，默认false。
        :type deny_ungoverned_regions: bool
        :param cloud_trail_type: 是否允许设置组织汇聚。
        :type cloud_trail_type: bool
        :param kms_key_id: 加密字段。
        :type kms_key_id: str
        :param logging_configuration: 
        :type logging_configuration: :class:`huaweicloudsdkrgc.v1.LoggingConfiguration`
        :param baseline_version: 基线版本
        :type baseline_version: str
        """
        
        

        self._identity_store_email = None
        self._home_region = None
        self._setup_landing_zone_action_type = None
        self._region_configuration_list = None
        self._identity_center_status = None
        self._organization_structure_type = None
        self._organization_structure = None
        self._deny_ungoverned_regions = None
        self._cloud_trail_type = None
        self._kms_key_id = None
        self._logging_configuration = None
        self._baseline_version = None
        self.discriminator = None

        if identity_store_email is not None:
            self.identity_store_email = identity_store_email
        self.home_region = home_region
        self.setup_landing_zone_action_type = setup_landing_zone_action_type
        self.region_configuration_list = region_configuration_list
        if identity_center_status is not None:
            self.identity_center_status = identity_center_status
        if organization_structure_type is not None:
            self.organization_structure_type = organization_structure_type
        self.organization_structure = organization_structure
        if deny_ungoverned_regions is not None:
            self.deny_ungoverned_regions = deny_ungoverned_regions
        if cloud_trail_type is not None:
            self.cloud_trail_type = cloud_trail_type
        if kms_key_id is not None:
            self.kms_key_id = kms_key_id
        self.logging_configuration = logging_configuration
        if baseline_version is not None:
            self.baseline_version = baseline_version

    @property
    def identity_store_email(self):
        r"""Gets the identity_store_email of this SetupLandingZoneReqBody.

        管理员纳管账号创建Identity Center用户所用邮箱。

        :return: The identity_store_email of this SetupLandingZoneReqBody.
        :rtype: str
        """
        return self._identity_store_email

    @identity_store_email.setter
    def identity_store_email(self, identity_store_email):
        r"""Sets the identity_store_email of this SetupLandingZoneReqBody.

        管理员纳管账号创建Identity Center用户所用邮箱。

        :param identity_store_email: The identity_store_email of this SetupLandingZoneReqBody.
        :type identity_store_email: str
        """
        self._identity_store_email = identity_store_email

    @property
    def home_region(self):
        r"""Gets the home_region of this SetupLandingZoneReqBody.

        主区域。

        :return: The home_region of this SetupLandingZoneReqBody.
        :rtype: str
        """
        return self._home_region

    @home_region.setter
    def home_region(self, home_region):
        r"""Sets the home_region of this SetupLandingZoneReqBody.

        主区域。

        :param home_region: The home_region of this SetupLandingZoneReqBody.
        :type home_region: str
        """
        self._home_region = home_region

    @property
    def setup_landing_zone_action_type(self):
        r"""Gets the setup_landing_zone_action_type of this SetupLandingZoneReqBody.

        设置Landing Zone的类型。包括CREATE、REPAIR以及UPDATE。

        :return: The setup_landing_zone_action_type of this SetupLandingZoneReqBody.
        :rtype: str
        """
        return self._setup_landing_zone_action_type

    @setup_landing_zone_action_type.setter
    def setup_landing_zone_action_type(self, setup_landing_zone_action_type):
        r"""Sets the setup_landing_zone_action_type of this SetupLandingZoneReqBody.

        设置Landing Zone的类型。包括CREATE、REPAIR以及UPDATE。

        :param setup_landing_zone_action_type: The setup_landing_zone_action_type of this SetupLandingZoneReqBody.
        :type setup_landing_zone_action_type: str
        """
        self._setup_landing_zone_action_type = setup_landing_zone_action_type

    @property
    def region_configuration_list(self):
        r"""Gets the region_configuration_list of this SetupLandingZoneReqBody.

        当前纳管账号纳管的区域。

        :return: The region_configuration_list of this SetupLandingZoneReqBody.
        :rtype: list[:class:`huaweicloudsdkrgc.v1.RegionConfigurationList`]
        """
        return self._region_configuration_list

    @region_configuration_list.setter
    def region_configuration_list(self, region_configuration_list):
        r"""Sets the region_configuration_list of this SetupLandingZoneReqBody.

        当前纳管账号纳管的区域。

        :param region_configuration_list: The region_configuration_list of this SetupLandingZoneReqBody.
        :type region_configuration_list: list[:class:`huaweicloudsdkrgc.v1.RegionConfigurationList`]
        """
        self._region_configuration_list = region_configuration_list

    @property
    def identity_center_status(self):
        r"""Gets the identity_center_status of this SetupLandingZoneReqBody.

        是否设置Landing Zone的identity center。

        :return: The identity_center_status of this SetupLandingZoneReqBody.
        :rtype: str
        """
        return self._identity_center_status

    @identity_center_status.setter
    def identity_center_status(self, identity_center_status):
        r"""Sets the identity_center_status of this SetupLandingZoneReqBody.

        是否设置Landing Zone的identity center。

        :param identity_center_status: The identity_center_status of this SetupLandingZoneReqBody.
        :type identity_center_status: str
        """
        self._identity_center_status = identity_center_status

    @property
    def organization_structure_type(self):
        r"""Gets the organization_structure_type of this SetupLandingZoneReqBody.

        设置organization的类型。STANDARD和NON_STANDARD。

        :return: The organization_structure_type of this SetupLandingZoneReqBody.
        :rtype: str
        """
        return self._organization_structure_type

    @organization_structure_type.setter
    def organization_structure_type(self, organization_structure_type):
        r"""Sets the organization_structure_type of this SetupLandingZoneReqBody.

        设置organization的类型。STANDARD和NON_STANDARD。

        :param organization_structure_type: The organization_structure_type of this SetupLandingZoneReqBody.
        :type organization_structure_type: str
        """
        self._organization_structure_type = organization_structure_type

    @property
    def organization_structure(self):
        r"""Gets the organization_structure of this SetupLandingZoneReqBody.

        基础环境的纳管账号体系。

        :return: The organization_structure of this SetupLandingZoneReqBody.
        :rtype: list[:class:`huaweicloudsdkrgc.v1.OrganizationStructureBaseLine`]
        """
        return self._organization_structure

    @organization_structure.setter
    def organization_structure(self, organization_structure):
        r"""Sets the organization_structure of this SetupLandingZoneReqBody.

        基础环境的纳管账号体系。

        :param organization_structure: The organization_structure of this SetupLandingZoneReqBody.
        :type organization_structure: list[:class:`huaweicloudsdkrgc.v1.OrganizationStructureBaseLine`]
        """
        self._organization_structure = organization_structure

    @property
    def deny_ungoverned_regions(self):
        r"""Gets the deny_ungoverned_regions of this SetupLandingZoneReqBody.

        是否允许区域拒绝，默认false。

        :return: The deny_ungoverned_regions of this SetupLandingZoneReqBody.
        :rtype: bool
        """
        return self._deny_ungoverned_regions

    @deny_ungoverned_regions.setter
    def deny_ungoverned_regions(self, deny_ungoverned_regions):
        r"""Sets the deny_ungoverned_regions of this SetupLandingZoneReqBody.

        是否允许区域拒绝，默认false。

        :param deny_ungoverned_regions: The deny_ungoverned_regions of this SetupLandingZoneReqBody.
        :type deny_ungoverned_regions: bool
        """
        self._deny_ungoverned_regions = deny_ungoverned_regions

    @property
    def cloud_trail_type(self):
        r"""Gets the cloud_trail_type of this SetupLandingZoneReqBody.

        是否允许设置组织汇聚。

        :return: The cloud_trail_type of this SetupLandingZoneReqBody.
        :rtype: bool
        """
        return self._cloud_trail_type

    @cloud_trail_type.setter
    def cloud_trail_type(self, cloud_trail_type):
        r"""Sets the cloud_trail_type of this SetupLandingZoneReqBody.

        是否允许设置组织汇聚。

        :param cloud_trail_type: The cloud_trail_type of this SetupLandingZoneReqBody.
        :type cloud_trail_type: bool
        """
        self._cloud_trail_type = cloud_trail_type

    @property
    def kms_key_id(self):
        r"""Gets the kms_key_id of this SetupLandingZoneReqBody.

        加密字段。

        :return: The kms_key_id of this SetupLandingZoneReqBody.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        r"""Sets the kms_key_id of this SetupLandingZoneReqBody.

        加密字段。

        :param kms_key_id: The kms_key_id of this SetupLandingZoneReqBody.
        :type kms_key_id: str
        """
        self._kms_key_id = kms_key_id

    @property
    def logging_configuration(self):
        r"""Gets the logging_configuration of this SetupLandingZoneReqBody.

        :return: The logging_configuration of this SetupLandingZoneReqBody.
        :rtype: :class:`huaweicloudsdkrgc.v1.LoggingConfiguration`
        """
        return self._logging_configuration

    @logging_configuration.setter
    def logging_configuration(self, logging_configuration):
        r"""Sets the logging_configuration of this SetupLandingZoneReqBody.

        :param logging_configuration: The logging_configuration of this SetupLandingZoneReqBody.
        :type logging_configuration: :class:`huaweicloudsdkrgc.v1.LoggingConfiguration`
        """
        self._logging_configuration = logging_configuration

    @property
    def baseline_version(self):
        r"""Gets the baseline_version of this SetupLandingZoneReqBody.

        基线版本

        :return: The baseline_version of this SetupLandingZoneReqBody.
        :rtype: str
        """
        return self._baseline_version

    @baseline_version.setter
    def baseline_version(self, baseline_version):
        r"""Sets the baseline_version of this SetupLandingZoneReqBody.

        基线版本

        :param baseline_version: The baseline_version of this SetupLandingZoneReqBody.
        :type baseline_version: str
        """
        self._baseline_version = baseline_version

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
