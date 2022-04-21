# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePasswordAuthRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'repo_type': 'str',
        'body': 'AccessPassword'
    }

    attribute_map = {
        'repo_type': 'repo_type',
        'body': 'body'
    }

    def __init__(self, repo_type=None, body=None):
        """CreatePasswordAuthRequest

        The model defined in huaweicloud sdk

        :param repo_type: 仓库类型。 支持口令授权的仓库类型有：github、devcloud、bitbucket。
        :type repo_type: str
        :param body: Body of the CreatePasswordAuthRequest
        :type body: :class:`huaweicloudsdkservicestage.v2.AccessPassword`
        """
        
        

        self._repo_type = None
        self._body = None
        self.discriminator = None

        self.repo_type = repo_type
        if body is not None:
            self.body = body

    @property
    def repo_type(self):
        """Gets the repo_type of this CreatePasswordAuthRequest.

        仓库类型。 支持口令授权的仓库类型有：github、devcloud、bitbucket。

        :return: The repo_type of this CreatePasswordAuthRequest.
        :rtype: str
        """
        return self._repo_type

    @repo_type.setter
    def repo_type(self, repo_type):
        """Sets the repo_type of this CreatePasswordAuthRequest.

        仓库类型。 支持口令授权的仓库类型有：github、devcloud、bitbucket。

        :param repo_type: The repo_type of this CreatePasswordAuthRequest.
        :type repo_type: str
        """
        self._repo_type = repo_type

    @property
    def body(self):
        """Gets the body of this CreatePasswordAuthRequest.


        :return: The body of this CreatePasswordAuthRequest.
        :rtype: :class:`huaweicloudsdkservicestage.v2.AccessPassword`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreatePasswordAuthRequest.


        :param body: The body of this CreatePasswordAuthRequest.
        :type body: :class:`huaweicloudsdkservicestage.v2.AccessPassword`
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
        if not isinstance(other, CreatePasswordAuthRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
