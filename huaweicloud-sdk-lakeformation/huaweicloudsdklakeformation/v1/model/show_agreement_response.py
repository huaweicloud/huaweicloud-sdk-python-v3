# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAgreementResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agreements': 'list[TenantAgreement]',
        'is_agency': 'bool',
        'x_request_id': 'str'
    }

    attribute_map = {
        'agreements': 'agreements',
        'is_agency': 'is_agency',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, agreements=None, is_agency=None, x_request_id=None):
        r"""ShowAgreementResponse

        The model defined in huaweicloud sdk

        :param agreements: 租户协议列表
        :type agreements: list[:class:`huaweicloudsdklakeformation.v1.TenantAgreement`]
        :param is_agency: 是否绑定了委托
        :type is_agency: bool
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowAgreementResponse, self).__init__()

        self._agreements = None
        self._is_agency = None
        self._x_request_id = None
        self.discriminator = None

        if agreements is not None:
            self.agreements = agreements
        if is_agency is not None:
            self.is_agency = is_agency
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def agreements(self):
        r"""Gets the agreements of this ShowAgreementResponse.

        租户协议列表

        :return: The agreements of this ShowAgreementResponse.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.TenantAgreement`]
        """
        return self._agreements

    @agreements.setter
    def agreements(self, agreements):
        r"""Sets the agreements of this ShowAgreementResponse.

        租户协议列表

        :param agreements: The agreements of this ShowAgreementResponse.
        :type agreements: list[:class:`huaweicloudsdklakeformation.v1.TenantAgreement`]
        """
        self._agreements = agreements

    @property
    def is_agency(self):
        r"""Gets the is_agency of this ShowAgreementResponse.

        是否绑定了委托

        :return: The is_agency of this ShowAgreementResponse.
        :rtype: bool
        """
        return self._is_agency

    @is_agency.setter
    def is_agency(self, is_agency):
        r"""Sets the is_agency of this ShowAgreementResponse.

        是否绑定了委托

        :param is_agency: The is_agency of this ShowAgreementResponse.
        :type is_agency: bool
        """
        self._is_agency = is_agency

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowAgreementResponse.

        :return: The x_request_id of this ShowAgreementResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowAgreementResponse.

        :param x_request_id: The x_request_id of this ShowAgreementResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ShowAgreementResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
