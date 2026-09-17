# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddIssuesToIteratorRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_uuid': 'str',
        'iterator_uri': 'str',
        'body': 'IssuesInfo'
    }

    attribute_map = {
        'project_uuid': 'project_uuid',
        'iterator_uri': 'iterator_uri',
        'body': 'body'
    }

    def __init__(self, project_uuid=None, iterator_uri=None, body=None):
        r"""AddIssuesToIteratorRequest

        The model defined in huaweicloud sdk

        :param project_uuid: 项目id
        :type project_uuid: str
        :param iterator_uri: 迭代uri
        :type iterator_uri: str
        :param body: Body of the AddIssuesToIteratorRequest
        :type body: :class:`huaweicloudsdkcloudtest.v1.IssuesInfo`
        """
        
        

        self._project_uuid = None
        self._iterator_uri = None
        self._body = None
        self.discriminator = None

        self.project_uuid = project_uuid
        self.iterator_uri = iterator_uri
        if body is not None:
            self.body = body

    @property
    def project_uuid(self):
        r"""Gets the project_uuid of this AddIssuesToIteratorRequest.

        项目id

        :return: The project_uuid of this AddIssuesToIteratorRequest.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        r"""Sets the project_uuid of this AddIssuesToIteratorRequest.

        项目id

        :param project_uuid: The project_uuid of this AddIssuesToIteratorRequest.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def iterator_uri(self):
        r"""Gets the iterator_uri of this AddIssuesToIteratorRequest.

        迭代uri

        :return: The iterator_uri of this AddIssuesToIteratorRequest.
        :rtype: str
        """
        return self._iterator_uri

    @iterator_uri.setter
    def iterator_uri(self, iterator_uri):
        r"""Sets the iterator_uri of this AddIssuesToIteratorRequest.

        迭代uri

        :param iterator_uri: The iterator_uri of this AddIssuesToIteratorRequest.
        :type iterator_uri: str
        """
        self._iterator_uri = iterator_uri

    @property
    def body(self):
        r"""Gets the body of this AddIssuesToIteratorRequest.

        :return: The body of this AddIssuesToIteratorRequest.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.IssuesInfo`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this AddIssuesToIteratorRequest.

        :param body: The body of this AddIssuesToIteratorRequest.
        :type body: :class:`huaweicloudsdkcloudtest.v1.IssuesInfo`
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
        if not isinstance(other, AddIssuesToIteratorRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
