# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RemoveIssuesFromIteratorRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'iterator_id': 'str',
        'body': 'RemoveIssuesInfo'
    }

    attribute_map = {
        'project_id': 'project_id',
        'iterator_id': 'iterator_id',
        'body': 'body'
    }

    def __init__(self, project_id=None, iterator_id=None, body=None):
        r"""RemoveIssuesFromIteratorRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目ID，固定长度32位字符（字母和数字）。
        :type project_id: str
        :param iterator_id: 迭代uri
        :type iterator_id: str
        :param body: Body of the RemoveIssuesFromIteratorRequest
        :type body: :class:`huaweicloudsdkcloudtest.v1.RemoveIssuesInfo`
        """
        
        

        self._project_id = None
        self._iterator_id = None
        self._body = None
        self.discriminator = None

        self.project_id = project_id
        self.iterator_id = iterator_id
        if body is not None:
            self.body = body

    @property
    def project_id(self):
        r"""Gets the project_id of this RemoveIssuesFromIteratorRequest.

        项目ID，固定长度32位字符（字母和数字）。

        :return: The project_id of this RemoveIssuesFromIteratorRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this RemoveIssuesFromIteratorRequest.

        项目ID，固定长度32位字符（字母和数字）。

        :param project_id: The project_id of this RemoveIssuesFromIteratorRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def iterator_id(self):
        r"""Gets the iterator_id of this RemoveIssuesFromIteratorRequest.

        迭代uri

        :return: The iterator_id of this RemoveIssuesFromIteratorRequest.
        :rtype: str
        """
        return self._iterator_id

    @iterator_id.setter
    def iterator_id(self, iterator_id):
        r"""Sets the iterator_id of this RemoveIssuesFromIteratorRequest.

        迭代uri

        :param iterator_id: The iterator_id of this RemoveIssuesFromIteratorRequest.
        :type iterator_id: str
        """
        self._iterator_id = iterator_id

    @property
    def body(self):
        r"""Gets the body of this RemoveIssuesFromIteratorRequest.

        :return: The body of this RemoveIssuesFromIteratorRequest.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.RemoveIssuesInfo`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this RemoveIssuesFromIteratorRequest.

        :param body: The body of this RemoveIssuesFromIteratorRequest.
        :type body: :class:`huaweicloudsdkcloudtest.v1.RemoveIssuesInfo`
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
        if not isinstance(other, RemoveIssuesFromIteratorRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
