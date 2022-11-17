# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTemplatesTwoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repository_uuid': 'str',
        'body': 'RepositoryTemplateVO2'
    }

    attribute_map = {
        'repository_uuid': 'repository_uuid',
        'body': 'body'
    }

    def __init__(self, repository_uuid=None, body=None):
        """ListTemplatesTwoRequest

        The model defined in huaweicloud sdk

        :param repository_uuid: 仓库id
        :type repository_uuid: str
        :param body: Body of the ListTemplatesTwoRequest
        :type body: :class:`huaweicloudsdkcodehub.v3.RepositoryTemplateVO2`
        """
        
        

        self._repository_uuid = None
        self._body = None
        self.discriminator = None

        self.repository_uuid = repository_uuid
        if body is not None:
            self.body = body

    @property
    def repository_uuid(self):
        """Gets the repository_uuid of this ListTemplatesTwoRequest.

        仓库id

        :return: The repository_uuid of this ListTemplatesTwoRequest.
        :rtype: str
        """
        return self._repository_uuid

    @repository_uuid.setter
    def repository_uuid(self, repository_uuid):
        """Sets the repository_uuid of this ListTemplatesTwoRequest.

        仓库id

        :param repository_uuid: The repository_uuid of this ListTemplatesTwoRequest.
        :type repository_uuid: str
        """
        self._repository_uuid = repository_uuid

    @property
    def body(self):
        """Gets the body of this ListTemplatesTwoRequest.

        :return: The body of this ListTemplatesTwoRequest.
        :rtype: :class:`huaweicloudsdkcodehub.v3.RepositoryTemplateVO2`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ListTemplatesTwoRequest.

        :param body: The body of this ListTemplatesTwoRequest.
        :type body: :class:`huaweicloudsdkcodehub.v3.RepositoryTemplateVO2`
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
        if not isinstance(other, ListTemplatesTwoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
