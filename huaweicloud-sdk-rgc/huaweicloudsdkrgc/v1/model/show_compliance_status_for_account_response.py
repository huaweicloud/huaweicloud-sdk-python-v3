# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowComplianceStatusForAccountResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'compliance_status': 'str'
    }

    attribute_map = {
        'compliance_status': 'compliance_status'
    }

    def __init__(self, compliance_status=None):
        r"""ShowComplianceStatusForAccountResponse

        The model defined in huaweicloud sdk

        :param compliance_status: 合规状态。
        :type compliance_status: str
        """
        
        super(ShowComplianceStatusForAccountResponse, self).__init__()

        self._compliance_status = None
        self.discriminator = None

        if compliance_status is not None:
            self.compliance_status = compliance_status

    @property
    def compliance_status(self):
        r"""Gets the compliance_status of this ShowComplianceStatusForAccountResponse.

        合规状态。

        :return: The compliance_status of this ShowComplianceStatusForAccountResponse.
        :rtype: str
        """
        return self._compliance_status

    @compliance_status.setter
    def compliance_status(self, compliance_status):
        r"""Sets the compliance_status of this ShowComplianceStatusForAccountResponse.

        合规状态。

        :param compliance_status: The compliance_status of this ShowComplianceStatusForAccountResponse.
        :type compliance_status: str
        """
        self._compliance_status = compliance_status

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
        if not isinstance(other, ShowComplianceStatusForAccountResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
