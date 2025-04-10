# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCommitRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repo_id': 'int',
        'body': 'CreateCommitRequestBody'
    }

    attribute_map = {
        'repo_id': 'repo_id',
        'body': 'body'
    }

    def __init__(self, repo_id=None, body=None):
        r"""CreateCommitRequest

        The model defined in huaweicloud sdk

        :param repo_id: 仓库短id
        :type repo_id: int
        :param body: Body of the CreateCommitRequest
        :type body: :class:`huaweicloudsdkcodehub.v3.CreateCommitRequestBody`
        """
        
        

        self._repo_id = None
        self._body = None
        self.discriminator = None

        self.repo_id = repo_id
        if body is not None:
            self.body = body

    @property
    def repo_id(self):
        r"""Gets the repo_id of this CreateCommitRequest.

        仓库短id

        :return: The repo_id of this CreateCommitRequest.
        :rtype: int
        """
        return self._repo_id

    @repo_id.setter
    def repo_id(self, repo_id):
        r"""Sets the repo_id of this CreateCommitRequest.

        仓库短id

        :param repo_id: The repo_id of this CreateCommitRequest.
        :type repo_id: int
        """
        self._repo_id = repo_id

    @property
    def body(self):
        r"""Gets the body of this CreateCommitRequest.

        :return: The body of this CreateCommitRequest.
        :rtype: :class:`huaweicloudsdkcodehub.v3.CreateCommitRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateCommitRequest.

        :param body: The body of this CreateCommitRequest.
        :type body: :class:`huaweicloudsdkcodehub.v3.CreateCommitRequestBody`
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
        if not isinstance(other, CreateCommitRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
