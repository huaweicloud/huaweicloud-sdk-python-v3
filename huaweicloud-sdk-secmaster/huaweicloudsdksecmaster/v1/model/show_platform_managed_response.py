# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPlatformManagedResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_time': 'int',
        'dw_region': 'str',
        'platform_managed_domain_id': 'str',
        'publish_status': 'str',
        'tenant_managed_domain_id': 'str',
        'update_time': 'int',
        'whitelist': 'bool'
    }

    attribute_map = {
        'create_time': 'create_time',
        'dw_region': 'dw_region',
        'platform_managed_domain_id': 'platform_managed_domain_id',
        'publish_status': 'publish_status',
        'tenant_managed_domain_id': 'tenant_managed_domain_id',
        'update_time': 'update_time',
        'whitelist': 'whitelist'
    }

    def __init__(self, create_time=None, dw_region=None, platform_managed_domain_id=None, publish_status=None, tenant_managed_domain_id=None, update_time=None, whitelist=None):
        r"""ShowPlatformManagedResponse

        The model defined in huaweicloud sdk

        :param create_time: 创建时间.
        :type create_time: int
        :param dw_region: 区域.
        :type dw_region: str
        :param platform_managed_domain_id: 平台租户ID.
        :type platform_managed_domain_id: str
        :param publish_status: 发布状态.
        :type publish_status: str
        :param tenant_managed_domain_id: 业务租户ID.
        :type tenant_managed_domain_id: str
        :param update_time: 更新时间.
        :type update_time: int
        :param whitelist: 是否在白名单中.
        :type whitelist: bool
        """
        
        super().__init__()

        self._create_time = None
        self._dw_region = None
        self._platform_managed_domain_id = None
        self._publish_status = None
        self._tenant_managed_domain_id = None
        self._update_time = None
        self._whitelist = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if dw_region is not None:
            self.dw_region = dw_region
        if platform_managed_domain_id is not None:
            self.platform_managed_domain_id = platform_managed_domain_id
        if publish_status is not None:
            self.publish_status = publish_status
        if tenant_managed_domain_id is not None:
            self.tenant_managed_domain_id = tenant_managed_domain_id
        if update_time is not None:
            self.update_time = update_time
        if whitelist is not None:
            self.whitelist = whitelist

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowPlatformManagedResponse.

        创建时间.

        :return: The create_time of this ShowPlatformManagedResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowPlatformManagedResponse.

        创建时间.

        :param create_time: The create_time of this ShowPlatformManagedResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def dw_region(self):
        r"""Gets the dw_region of this ShowPlatformManagedResponse.

        区域.

        :return: The dw_region of this ShowPlatformManagedResponse.
        :rtype: str
        """
        return self._dw_region

    @dw_region.setter
    def dw_region(self, dw_region):
        r"""Sets the dw_region of this ShowPlatformManagedResponse.

        区域.

        :param dw_region: The dw_region of this ShowPlatformManagedResponse.
        :type dw_region: str
        """
        self._dw_region = dw_region

    @property
    def platform_managed_domain_id(self):
        r"""Gets the platform_managed_domain_id of this ShowPlatformManagedResponse.

        平台租户ID.

        :return: The platform_managed_domain_id of this ShowPlatformManagedResponse.
        :rtype: str
        """
        return self._platform_managed_domain_id

    @platform_managed_domain_id.setter
    def platform_managed_domain_id(self, platform_managed_domain_id):
        r"""Sets the platform_managed_domain_id of this ShowPlatformManagedResponse.

        平台租户ID.

        :param platform_managed_domain_id: The platform_managed_domain_id of this ShowPlatformManagedResponse.
        :type platform_managed_domain_id: str
        """
        self._platform_managed_domain_id = platform_managed_domain_id

    @property
    def publish_status(self):
        r"""Gets the publish_status of this ShowPlatformManagedResponse.

        发布状态.

        :return: The publish_status of this ShowPlatformManagedResponse.
        :rtype: str
        """
        return self._publish_status

    @publish_status.setter
    def publish_status(self, publish_status):
        r"""Sets the publish_status of this ShowPlatformManagedResponse.

        发布状态.

        :param publish_status: The publish_status of this ShowPlatformManagedResponse.
        :type publish_status: str
        """
        self._publish_status = publish_status

    @property
    def tenant_managed_domain_id(self):
        r"""Gets the tenant_managed_domain_id of this ShowPlatformManagedResponse.

        业务租户ID.

        :return: The tenant_managed_domain_id of this ShowPlatformManagedResponse.
        :rtype: str
        """
        return self._tenant_managed_domain_id

    @tenant_managed_domain_id.setter
    def tenant_managed_domain_id(self, tenant_managed_domain_id):
        r"""Sets the tenant_managed_domain_id of this ShowPlatformManagedResponse.

        业务租户ID.

        :param tenant_managed_domain_id: The tenant_managed_domain_id of this ShowPlatformManagedResponse.
        :type tenant_managed_domain_id: str
        """
        self._tenant_managed_domain_id = tenant_managed_domain_id

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowPlatformManagedResponse.

        更新时间.

        :return: The update_time of this ShowPlatformManagedResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowPlatformManagedResponse.

        更新时间.

        :param update_time: The update_time of this ShowPlatformManagedResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def whitelist(self):
        r"""Gets the whitelist of this ShowPlatformManagedResponse.

        是否在白名单中.

        :return: The whitelist of this ShowPlatformManagedResponse.
        :rtype: bool
        """
        return self._whitelist

    @whitelist.setter
    def whitelist(self, whitelist):
        r"""Sets the whitelist of this ShowPlatformManagedResponse.

        是否在白名单中.

        :param whitelist: The whitelist of this ShowPlatformManagedResponse.
        :type whitelist: bool
        """
        self._whitelist = whitelist

    def to_dict(self):
        import warnings
        warnings.warn("ShowPlatformManagedResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowPlatformManagedResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
