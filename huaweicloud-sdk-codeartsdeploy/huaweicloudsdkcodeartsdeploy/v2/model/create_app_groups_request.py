# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAppGroupsRequest:

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
        'body': 'CreateAppGroupsRequestBody'
    }

    attribute_map = {
        'project_id': 'project_id',
        'body': 'body'
    }

    def __init__(self, project_id=None, body=None):
        r"""CreateAppGroupsRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目Id
        :type project_id: str
        :param body: Body of the CreateAppGroupsRequest
        :type body: :class:`huaweicloudsdkcodeartsdeploy.v2.CreateAppGroupsRequestBody`
        """
        
        

        self._project_id = None
        self._body = None
        self.discriminator = None

        self.project_id = project_id
        if body is not None:
            self.body = body

    @property
    def project_id(self):
        r"""Gets the project_id of this CreateAppGroupsRequest.

        项目Id

        :return: The project_id of this CreateAppGroupsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CreateAppGroupsRequest.

        项目Id

        :param project_id: The project_id of this CreateAppGroupsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def body(self):
        r"""Gets the body of this CreateAppGroupsRequest.

        :return: The body of this CreateAppGroupsRequest.
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.CreateAppGroupsRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateAppGroupsRequest.

        :param body: The body of this CreateAppGroupsRequest.
        :type body: :class:`huaweicloudsdkcodeartsdeploy.v2.CreateAppGroupsRequestBody`
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
        if not isinstance(other, CreateAppGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
