# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModelArtsAgencyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agency_name_suffix': 'str',
        'agency_services': 'list[AgencyServices]'
    }

    attribute_map = {
        'agency_name_suffix': 'agency_name_suffix',
        'agency_services': 'agency_services'
    }

    def __init__(self, agency_name_suffix=None, agency_services=None):
        r"""ModelArtsAgencyRequest

        The model defined in huaweicloud sdk

        :param agency_name_suffix: 委托名称后缀。  长度不大于50位。  委托名称前缀固定为ma_agency。  如该字段为iam-user01，则创建出来的委托名称为ma_agency_iam-user01。  默认为空，表示创建名称为modelarts_agency的委托。
        :type agency_name_suffix: str
        :param agency_services: **参数解释**：细粒度权限列表。
        :type agency_services: list[:class:`huaweicloudsdkmodelarts.v1.AgencyServices`]
        """
        
        

        self._agency_name_suffix = None
        self._agency_services = None
        self.discriminator = None

        if agency_name_suffix is not None:
            self.agency_name_suffix = agency_name_suffix
        if agency_services is not None:
            self.agency_services = agency_services

    @property
    def agency_name_suffix(self):
        r"""Gets the agency_name_suffix of this ModelArtsAgencyRequest.

        委托名称后缀。  长度不大于50位。  委托名称前缀固定为ma_agency。  如该字段为iam-user01，则创建出来的委托名称为ma_agency_iam-user01。  默认为空，表示创建名称为modelarts_agency的委托。

        :return: The agency_name_suffix of this ModelArtsAgencyRequest.
        :rtype: str
        """
        return self._agency_name_suffix

    @agency_name_suffix.setter
    def agency_name_suffix(self, agency_name_suffix):
        r"""Sets the agency_name_suffix of this ModelArtsAgencyRequest.

        委托名称后缀。  长度不大于50位。  委托名称前缀固定为ma_agency。  如该字段为iam-user01，则创建出来的委托名称为ma_agency_iam-user01。  默认为空，表示创建名称为modelarts_agency的委托。

        :param agency_name_suffix: The agency_name_suffix of this ModelArtsAgencyRequest.
        :type agency_name_suffix: str
        """
        self._agency_name_suffix = agency_name_suffix

    @property
    def agency_services(self):
        r"""Gets the agency_services of this ModelArtsAgencyRequest.

        **参数解释**：细粒度权限列表。

        :return: The agency_services of this ModelArtsAgencyRequest.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.AgencyServices`]
        """
        return self._agency_services

    @agency_services.setter
    def agency_services(self, agency_services):
        r"""Sets the agency_services of this ModelArtsAgencyRequest.

        **参数解释**：细粒度权限列表。

        :param agency_services: The agency_services of this ModelArtsAgencyRequest.
        :type agency_services: list[:class:`huaweicloudsdkmodelarts.v1.AgencyServices`]
        """
        self._agency_services = agency_services

    def to_dict(self):
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
        if not isinstance(other, ModelArtsAgencyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
