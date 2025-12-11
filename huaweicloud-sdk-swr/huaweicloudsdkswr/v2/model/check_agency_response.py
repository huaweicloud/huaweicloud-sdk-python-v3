# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckAgencyResponse(SdkResponse):

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
        'is_agency': 'bool'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'is_agency': 'is_agency'
    }

    def __init__(self, domain_id=None, is_agency=None):
        r"""CheckAgencyResponse

        The model defined in huaweicloud sdk

        :param domain_id: 租户ID
        :type domain_id: str
        :param is_agency: 是否已创建委托
        :type is_agency: bool
        """
        
        super().__init__()

        self._domain_id = None
        self._is_agency = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if is_agency is not None:
            self.is_agency = is_agency

    @property
    def domain_id(self):
        r"""Gets the domain_id of this CheckAgencyResponse.

        租户ID

        :return: The domain_id of this CheckAgencyResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this CheckAgencyResponse.

        租户ID

        :param domain_id: The domain_id of this CheckAgencyResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def is_agency(self):
        r"""Gets the is_agency of this CheckAgencyResponse.

        是否已创建委托

        :return: The is_agency of this CheckAgencyResponse.
        :rtype: bool
        """
        return self._is_agency

    @is_agency.setter
    def is_agency(self, is_agency):
        r"""Sets the is_agency of this CheckAgencyResponse.

        是否已创建委托

        :param is_agency: The is_agency of this CheckAgencyResponse.
        :type is_agency: bool
        """
        self._is_agency = is_agency

    def to_dict(self):
        import warnings
        warnings.warn("CheckAgencyResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CheckAgencyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
