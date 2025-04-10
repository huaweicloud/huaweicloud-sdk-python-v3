# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLatestPublishedAgreementResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'case_agreement': 'AgreementVO'
    }

    attribute_map = {
        'case_agreement': 'case_agreement'
    }

    def __init__(self, case_agreement=None):
        r"""ShowLatestPublishedAgreementResponse

        The model defined in huaweicloud sdk

        :param case_agreement: 
        :type case_agreement: :class:`huaweicloudsdkosm.v2.AgreementVO`
        """
        
        super(ShowLatestPublishedAgreementResponse, self).__init__()

        self._case_agreement = None
        self.discriminator = None

        if case_agreement is not None:
            self.case_agreement = case_agreement

    @property
    def case_agreement(self):
        r"""Gets the case_agreement of this ShowLatestPublishedAgreementResponse.

        :return: The case_agreement of this ShowLatestPublishedAgreementResponse.
        :rtype: :class:`huaweicloudsdkosm.v2.AgreementVO`
        """
        return self._case_agreement

    @case_agreement.setter
    def case_agreement(self, case_agreement):
        r"""Sets the case_agreement of this ShowLatestPublishedAgreementResponse.

        :param case_agreement: The case_agreement of this ShowLatestPublishedAgreementResponse.
        :type case_agreement: :class:`huaweicloudsdkosm.v2.AgreementVO`
        """
        self._case_agreement = case_agreement

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
        if not isinstance(other, ShowLatestPublishedAgreementResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
