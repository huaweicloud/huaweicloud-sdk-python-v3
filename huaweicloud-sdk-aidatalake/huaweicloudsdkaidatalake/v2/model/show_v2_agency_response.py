# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowV2AgencyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agency_name': 'str',
        'authorized': 'bool',
        'create_time': 'datetime',
        'agency_policies': 'list[V2AgencyPolicy]'
    }

    attribute_map = {
        'agency_name': 'agency_name',
        'authorized': 'authorized',
        'create_time': 'create_time',
        'agency_policies': 'agency_policies'
    }

    def __init__(self, agency_name=None, authorized=None, create_time=None, agency_policies=None):
        r"""ShowV2AgencyResponse

        The model defined in huaweicloud sdk

        :param agency_name: **参数解释**：委托名称。 **取值范围**：固定值ai_datalake_admin_trust。
        :type agency_name: str
        :param authorized: **参数解释**：授权与否。如果用户的服务委托权限包含系统所需要的委托权限则返回true，否则返回false。 **取值范围**：   - true：已授权。   - false：未授权。
        :type authorized: bool
        :param create_time: **参数解释**：资源创建时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ，UTC时间。 
        :type create_time: datetime
        :param agency_policies: **参数解释**：委托策略列表。
        :type agency_policies: list[:class:`huaweicloudsdkaidatalake.v2.V2AgencyPolicy`]
        """
        
        super().__init__()

        self._agency_name = None
        self._authorized = None
        self._create_time = None
        self._agency_policies = None
        self.discriminator = None

        if agency_name is not None:
            self.agency_name = agency_name
        if authorized is not None:
            self.authorized = authorized
        if create_time is not None:
            self.create_time = create_time
        if agency_policies is not None:
            self.agency_policies = agency_policies

    @property
    def agency_name(self):
        r"""Gets the agency_name of this ShowV2AgencyResponse.

        **参数解释**：委托名称。 **取值范围**：固定值ai_datalake_admin_trust。

        :return: The agency_name of this ShowV2AgencyResponse.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this ShowV2AgencyResponse.

        **参数解释**：委托名称。 **取值范围**：固定值ai_datalake_admin_trust。

        :param agency_name: The agency_name of this ShowV2AgencyResponse.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def authorized(self):
        r"""Gets the authorized of this ShowV2AgencyResponse.

        **参数解释**：授权与否。如果用户的服务委托权限包含系统所需要的委托权限则返回true，否则返回false。 **取值范围**：   - true：已授权。   - false：未授权。

        :return: The authorized of this ShowV2AgencyResponse.
        :rtype: bool
        """
        return self._authorized

    @authorized.setter
    def authorized(self, authorized):
        r"""Sets the authorized of this ShowV2AgencyResponse.

        **参数解释**：授权与否。如果用户的服务委托权限包含系统所需要的委托权限则返回true，否则返回false。 **取值范围**：   - true：已授权。   - false：未授权。

        :param authorized: The authorized of this ShowV2AgencyResponse.
        :type authorized: bool
        """
        self._authorized = authorized

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowV2AgencyResponse.

        **参数解释**：资源创建时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSZ，UTC时间。 

        :return: The create_time of this ShowV2AgencyResponse.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowV2AgencyResponse.

        **参数解释**：资源创建时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSZ，UTC时间。 

        :param create_time: The create_time of this ShowV2AgencyResponse.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def agency_policies(self):
        r"""Gets the agency_policies of this ShowV2AgencyResponse.

        **参数解释**：委托策略列表。

        :return: The agency_policies of this ShowV2AgencyResponse.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.V2AgencyPolicy`]
        """
        return self._agency_policies

    @agency_policies.setter
    def agency_policies(self, agency_policies):
        r"""Sets the agency_policies of this ShowV2AgencyResponse.

        **参数解释**：委托策略列表。

        :param agency_policies: The agency_policies of this ShowV2AgencyResponse.
        :type agency_policies: list[:class:`huaweicloudsdkaidatalake.v2.V2AgencyPolicy`]
        """
        self._agency_policies = agency_policies

    def to_dict(self):
        import warnings
        warnings.warn("ShowV2AgencyResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowV2AgencyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
