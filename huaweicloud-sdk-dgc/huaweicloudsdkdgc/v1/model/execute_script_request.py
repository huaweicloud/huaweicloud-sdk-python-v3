# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteScriptRequest:

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
        'script_name': 'str',
        'body': 'ExecuteScriptReq'
    }

    attribute_map = {
        'workspace': 'workspace',
        'script_name': 'script_name',
        'body': 'body'
    }

    def __init__(self, workspace=None, script_name=None, body=None):
        r"""ExecuteScriptRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间id
        :type workspace: str
        :param script_name: 
        :type script_name: str
        :param body: Body of the ExecuteScriptRequest
        :type body: :class:`huaweicloudsdkdgc.v1.ExecuteScriptReq`
        """
        
        

        self._workspace = None
        self._script_name = None
        self._body = None
        self.discriminator = None

        if workspace is not None:
            self.workspace = workspace
        self.script_name = script_name
        if body is not None:
            self.body = body

    @property
    def workspace(self):
        r"""Gets the workspace of this ExecuteScriptRequest.

        工作空间id

        :return: The workspace of this ExecuteScriptRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ExecuteScriptRequest.

        工作空间id

        :param workspace: The workspace of this ExecuteScriptRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def script_name(self):
        r"""Gets the script_name of this ExecuteScriptRequest.

        :return: The script_name of this ExecuteScriptRequest.
        :rtype: str
        """
        return self._script_name

    @script_name.setter
    def script_name(self, script_name):
        r"""Sets the script_name of this ExecuteScriptRequest.

        :param script_name: The script_name of this ExecuteScriptRequest.
        :type script_name: str
        """
        self._script_name = script_name

    @property
    def body(self):
        r"""Gets the body of this ExecuteScriptRequest.

        :return: The body of this ExecuteScriptRequest.
        :rtype: :class:`huaweicloudsdkdgc.v1.ExecuteScriptReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ExecuteScriptRequest.

        :param body: The body of this ExecuteScriptRequest.
        :type body: :class:`huaweicloudsdkdgc.v1.ExecuteScriptReq`
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
        if not isinstance(other, ExecuteScriptRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
