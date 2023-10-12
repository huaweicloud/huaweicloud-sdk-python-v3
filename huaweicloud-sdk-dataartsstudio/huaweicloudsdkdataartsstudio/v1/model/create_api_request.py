# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateApiRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'dlm_type': 'str',
        'body': 'Api'
    }

    attribute_map = {
        'workspace': 'workspace',
        'dlm_type': 'Dlm-Type',
        'body': 'body'
    }

    def __init__(self, workspace=None, dlm_type=None, body=None):
        """CreateApiRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间id
        :type workspace: str
        :param dlm_type: dlm版本类型
        :type dlm_type: str
        :param body: Body of the CreateApiRequest
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.Api`
        """
        
        

        self._workspace = None
        self._dlm_type = None
        self._body = None
        self.discriminator = None

        self.workspace = workspace
        self.dlm_type = dlm_type
        if body is not None:
            self.body = body

    @property
    def workspace(self):
        """Gets the workspace of this CreateApiRequest.

        工作空间id

        :return: The workspace of this CreateApiRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this CreateApiRequest.

        工作空间id

        :param workspace: The workspace of this CreateApiRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def dlm_type(self):
        """Gets the dlm_type of this CreateApiRequest.

        dlm版本类型

        :return: The dlm_type of this CreateApiRequest.
        :rtype: str
        """
        return self._dlm_type

    @dlm_type.setter
    def dlm_type(self, dlm_type):
        """Sets the dlm_type of this CreateApiRequest.

        dlm版本类型

        :param dlm_type: The dlm_type of this CreateApiRequest.
        :type dlm_type: str
        """
        self._dlm_type = dlm_type

    @property
    def body(self):
        """Gets the body of this CreateApiRequest.

        :return: The body of this CreateApiRequest.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.Api`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateApiRequest.

        :param body: The body of this CreateApiRequest.
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.Api`
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
        if not isinstance(other, CreateApiRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
