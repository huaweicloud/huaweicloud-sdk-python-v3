# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateUserDefinedUrlKeyWordRequest:

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
        'body': 'CreateBasicAwReq'
    }

    attribute_map = {
        'project_id': 'project_id',
        'body': 'body'
    }

    def __init__(self, project_id=None, body=None):
        r"""CreateUserDefinedUrlKeyWordRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目ID，固定长度32位字符（字母和数字）。
        :type project_id: str
        :param body: Body of the CreateUserDefinedUrlKeyWordRequest
        :type body: :class:`huaweicloudsdkcloudtest.v1.CreateBasicAwReq`
        """
        
        

        self._project_id = None
        self._body = None
        self.discriminator = None

        self.project_id = project_id
        if body is not None:
            self.body = body

    @property
    def project_id(self):
        r"""Gets the project_id of this CreateUserDefinedUrlKeyWordRequest.

        项目ID，固定长度32位字符（字母和数字）。

        :return: The project_id of this CreateUserDefinedUrlKeyWordRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CreateUserDefinedUrlKeyWordRequest.

        项目ID，固定长度32位字符（字母和数字）。

        :param project_id: The project_id of this CreateUserDefinedUrlKeyWordRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def body(self):
        r"""Gets the body of this CreateUserDefinedUrlKeyWordRequest.

        :return: The body of this CreateUserDefinedUrlKeyWordRequest.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.CreateBasicAwReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateUserDefinedUrlKeyWordRequest.

        :param body: The body of this CreateUserDefinedUrlKeyWordRequest.
        :type body: :class:`huaweicloudsdkcloudtest.v1.CreateBasicAwReq`
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
        if not isinstance(other, CreateUserDefinedUrlKeyWordRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
