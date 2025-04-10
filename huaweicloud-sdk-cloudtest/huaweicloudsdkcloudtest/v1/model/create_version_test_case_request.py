# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVersionTestCaseRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version_id': 'str',
        'body': 'TestCaseInfo'
    }

    attribute_map = {
        'version_id': 'version_id',
        'body': 'body'
    }

    def __init__(self, version_id=None, body=None):
        r"""CreateVersionTestCaseRequest

        The model defined in huaweicloud sdk

        :param version_id: 分支或者迭代uri
        :type version_id: str
        :param body: Body of the CreateVersionTestCaseRequest
        :type body: :class:`huaweicloudsdkcloudtest.v1.TestCaseInfo`
        """
        
        

        self._version_id = None
        self._body = None
        self.discriminator = None

        self.version_id = version_id
        if body is not None:
            self.body = body

    @property
    def version_id(self):
        r"""Gets the version_id of this CreateVersionTestCaseRequest.

        分支或者迭代uri

        :return: The version_id of this CreateVersionTestCaseRequest.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this CreateVersionTestCaseRequest.

        分支或者迭代uri

        :param version_id: The version_id of this CreateVersionTestCaseRequest.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def body(self):
        r"""Gets the body of this CreateVersionTestCaseRequest.

        :return: The body of this CreateVersionTestCaseRequest.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.TestCaseInfo`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateVersionTestCaseRequest.

        :param body: The body of this CreateVersionTestCaseRequest.
        :type body: :class:`huaweicloudsdkcloudtest.v1.TestCaseInfo`
        """
        self._body = body

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
        if not isinstance(other, CreateVersionTestCaseRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
