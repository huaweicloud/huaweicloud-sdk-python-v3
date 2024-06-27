# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateIteratorRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'branch_uri': 'str',
        'body': 'IteratorVersionInfo'
    }

    attribute_map = {
        'branch_uri': 'branch_uri',
        'body': 'body'
    }

    def __init__(self, branch_uri=None, body=None):
        """CreateIteratorRequest

        The model defined in huaweicloud sdk

        :param branch_uri: 分支URI
        :type branch_uri: str
        :param body: Body of the CreateIteratorRequest
        :type body: :class:`huaweicloudsdkcloudtest.v1.IteratorVersionInfo`
        """
        
        

        self._branch_uri = None
        self._body = None
        self.discriminator = None

        self.branch_uri = branch_uri
        if body is not None:
            self.body = body

    @property
    def branch_uri(self):
        """Gets the branch_uri of this CreateIteratorRequest.

        分支URI

        :return: The branch_uri of this CreateIteratorRequest.
        :rtype: str
        """
        return self._branch_uri

    @branch_uri.setter
    def branch_uri(self, branch_uri):
        """Sets the branch_uri of this CreateIteratorRequest.

        分支URI

        :param branch_uri: The branch_uri of this CreateIteratorRequest.
        :type branch_uri: str
        """
        self._branch_uri = branch_uri

    @property
    def body(self):
        """Gets the body of this CreateIteratorRequest.

        :return: The body of this CreateIteratorRequest.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.IteratorVersionInfo`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateIteratorRequest.

        :param body: The body of this CreateIteratorRequest.
        :type body: :class:`huaweicloudsdkcloudtest.v1.IteratorVersionInfo`
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
        if not isinstance(other, CreateIteratorRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
