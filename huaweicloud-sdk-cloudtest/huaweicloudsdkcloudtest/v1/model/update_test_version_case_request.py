# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTestVersionCaseRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'case_uri': 'str',
        'body': 'TestCaseInfo'
    }

    attribute_map = {
        'case_uri': 'case_uri',
        'body': 'body'
    }

    def __init__(self, case_uri=None, body=None):
        r"""UpdateTestVersionCaseRequest

        The model defined in huaweicloud sdk

        :param case_uri: 用例uri
        :type case_uri: str
        :param body: Body of the UpdateTestVersionCaseRequest
        :type body: :class:`huaweicloudsdkcloudtest.v1.TestCaseInfo`
        """
        
        

        self._case_uri = None
        self._body = None
        self.discriminator = None

        self.case_uri = case_uri
        if body is not None:
            self.body = body

    @property
    def case_uri(self):
        r"""Gets the case_uri of this UpdateTestVersionCaseRequest.

        用例uri

        :return: The case_uri of this UpdateTestVersionCaseRequest.
        :rtype: str
        """
        return self._case_uri

    @case_uri.setter
    def case_uri(self, case_uri):
        r"""Sets the case_uri of this UpdateTestVersionCaseRequest.

        用例uri

        :param case_uri: The case_uri of this UpdateTestVersionCaseRequest.
        :type case_uri: str
        """
        self._case_uri = case_uri

    @property
    def body(self):
        r"""Gets the body of this UpdateTestVersionCaseRequest.

        :return: The body of this UpdateTestVersionCaseRequest.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.TestCaseInfo`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateTestVersionCaseRequest.

        :param body: The body of this UpdateTestVersionCaseRequest.
        :type body: :class:`huaweicloudsdkcloudtest.v1.TestCaseInfo`
        """
        self._body = body

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
        if not isinstance(other, UpdateTestVersionCaseRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
