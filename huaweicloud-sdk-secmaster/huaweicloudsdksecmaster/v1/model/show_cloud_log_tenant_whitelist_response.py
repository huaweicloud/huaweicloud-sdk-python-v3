# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCloudLogTenantWhitelistResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'dw_region': 'str',
        'enable': 'bool',
        'project_id': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'dw_region': 'dw_region',
        'enable': 'enable',
        'project_id': 'project_id'
    }

    def __init__(self, domain_id=None, dw_region=None, enable=None, project_id=None):
        r"""ShowCloudLogTenantWhitelistResponse

        The model defined in huaweicloud sdk

        :param domain_id: 租户Id
        :type domain_id: str
        :param dw_region: 数仓区域
        :type dw_region: str
        :param enable: 是否开启
        :type enable: bool
        :param project_id: 项目Id
        :type project_id: str
        """
        
        super().__init__()

        self._domain_id = None
        self._dw_region = None
        self._enable = None
        self._project_id = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if dw_region is not None:
            self.dw_region = dw_region
        if enable is not None:
            self.enable = enable
        if project_id is not None:
            self.project_id = project_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowCloudLogTenantWhitelistResponse.

        租户Id

        :return: The domain_id of this ShowCloudLogTenantWhitelistResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowCloudLogTenantWhitelistResponse.

        租户Id

        :param domain_id: The domain_id of this ShowCloudLogTenantWhitelistResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def dw_region(self):
        r"""Gets the dw_region of this ShowCloudLogTenantWhitelistResponse.

        数仓区域

        :return: The dw_region of this ShowCloudLogTenantWhitelistResponse.
        :rtype: str
        """
        return self._dw_region

    @dw_region.setter
    def dw_region(self, dw_region):
        r"""Sets the dw_region of this ShowCloudLogTenantWhitelistResponse.

        数仓区域

        :param dw_region: The dw_region of this ShowCloudLogTenantWhitelistResponse.
        :type dw_region: str
        """
        self._dw_region = dw_region

    @property
    def enable(self):
        r"""Gets the enable of this ShowCloudLogTenantWhitelistResponse.

        是否开启

        :return: The enable of this ShowCloudLogTenantWhitelistResponse.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this ShowCloudLogTenantWhitelistResponse.

        是否开启

        :param enable: The enable of this ShowCloudLogTenantWhitelistResponse.
        :type enable: bool
        """
        self._enable = enable

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowCloudLogTenantWhitelistResponse.

        项目Id

        :return: The project_id of this ShowCloudLogTenantWhitelistResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowCloudLogTenantWhitelistResponse.

        项目Id

        :param project_id: The project_id of this ShowCloudLogTenantWhitelistResponse.
        :type project_id: str
        """
        self._project_id = project_id

    def to_dict(self):
        import warnings
        warnings.warn("ShowCloudLogTenantWhitelistResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowCloudLogTenantWhitelistResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
