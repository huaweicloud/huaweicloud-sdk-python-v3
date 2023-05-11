# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddDeployKeyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repository_id': 'int',
        'body': 'AddDeployKeyRequestBody'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'body': 'body'
    }

    def __init__(self, repository_id=None, body=None):
        """AddDeployKeyRequest

        The model defined in huaweicloud sdk

        :param repository_id: 仓库短id
        :type repository_id: int
        :param body: Body of the AddDeployKeyRequest
        :type body: :class:`huaweicloudsdkcodehub.v3.AddDeployKeyRequestBody`
        """
        
        

        self._repository_id = None
        self._body = None
        self.discriminator = None

        self.repository_id = repository_id
        if body is not None:
            self.body = body

    @property
    def repository_id(self):
        """Gets the repository_id of this AddDeployKeyRequest.

        仓库短id

        :return: The repository_id of this AddDeployKeyRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        """Sets the repository_id of this AddDeployKeyRequest.

        仓库短id

        :param repository_id: The repository_id of this AddDeployKeyRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def body(self):
        """Gets the body of this AddDeployKeyRequest.

        :return: The body of this AddDeployKeyRequest.
        :rtype: :class:`huaweicloudsdkcodehub.v3.AddDeployKeyRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this AddDeployKeyRequest.

        :param body: The body of this AddDeployKeyRequest.
        :type body: :class:`huaweicloudsdkcodehub.v3.AddDeployKeyRequestBody`
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
        if not isinstance(other, AddDeployKeyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
