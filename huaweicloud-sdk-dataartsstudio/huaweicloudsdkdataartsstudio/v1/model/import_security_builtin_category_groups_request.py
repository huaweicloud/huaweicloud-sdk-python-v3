# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportSecurityBuiltinCategoryGroupsRequest:

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
        'x_language': 'str',
        'body': 'ImportBuiltinCategoryParam'
    }

    attribute_map = {
        'workspace': 'workspace',
        'x_language': 'X-Language',
        'body': 'body'
    }

    def __init__(self, workspace=None, x_language=None, body=None):
        r"""ImportSecurityBuiltinCategoryGroupsRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param x_language: 请求语言 * zh-cn 中文 * en-us 英文
        :type x_language: str
        :param body: Body of the ImportSecurityBuiltinCategoryGroupsRequest
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.ImportBuiltinCategoryParam`
        """
        
        

        self._workspace = None
        self._x_language = None
        self._body = None
        self.discriminator = None

        self.workspace = workspace
        self.x_language = x_language
        if body is not None:
            self.body = body

    @property
    def workspace(self):
        r"""Gets the workspace of this ImportSecurityBuiltinCategoryGroupsRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ImportSecurityBuiltinCategoryGroupsRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ImportSecurityBuiltinCategoryGroupsRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ImportSecurityBuiltinCategoryGroupsRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def x_language(self):
        r"""Gets the x_language of this ImportSecurityBuiltinCategoryGroupsRequest.

        请求语言 * zh-cn 中文 * en-us 英文

        :return: The x_language of this ImportSecurityBuiltinCategoryGroupsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ImportSecurityBuiltinCategoryGroupsRequest.

        请求语言 * zh-cn 中文 * en-us 英文

        :param x_language: The x_language of this ImportSecurityBuiltinCategoryGroupsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def body(self):
        r"""Gets the body of this ImportSecurityBuiltinCategoryGroupsRequest.

        :return: The body of this ImportSecurityBuiltinCategoryGroupsRequest.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ImportBuiltinCategoryParam`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ImportSecurityBuiltinCategoryGroupsRequest.

        :param body: The body of this ImportSecurityBuiltinCategoryGroupsRequest.
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.ImportBuiltinCategoryParam`
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
        if not isinstance(other, ImportSecurityBuiltinCategoryGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
