# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTestVersionCaseRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version_uri': 'str',
        'body': 'TestCaseInfo'
    }

    attribute_map = {
        'version_uri': 'version_uri',
        'body': 'body'
    }

    def __init__(self, version_uri=None, body=None):
        r"""CreateTestVersionCaseRequest

        The model defined in huaweicloud sdk

        :param version_uri: 分支或者迭代uri
        :type version_uri: str
        :param body: Body of the CreateTestVersionCaseRequest
        :type body: :class:`huaweicloudsdkcloudtest.v1.TestCaseInfo`
        """
        
        

        self._version_uri = None
        self._body = None
        self.discriminator = None

        self.version_uri = version_uri
        if body is not None:
            self.body = body

    @property
    def version_uri(self):
        r"""Gets the version_uri of this CreateTestVersionCaseRequest.

        分支或者迭代uri

        :return: The version_uri of this CreateTestVersionCaseRequest.
        :rtype: str
        """
        return self._version_uri

    @version_uri.setter
    def version_uri(self, version_uri):
        r"""Sets the version_uri of this CreateTestVersionCaseRequest.

        分支或者迭代uri

        :param version_uri: The version_uri of this CreateTestVersionCaseRequest.
        :type version_uri: str
        """
        self._version_uri = version_uri

    @property
    def body(self):
        r"""Gets the body of this CreateTestVersionCaseRequest.

        :return: The body of this CreateTestVersionCaseRequest.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.TestCaseInfo`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateTestVersionCaseRequest.

        :param body: The body of this CreateTestVersionCaseRequest.
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
        if not isinstance(other, CreateTestVersionCaseRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
