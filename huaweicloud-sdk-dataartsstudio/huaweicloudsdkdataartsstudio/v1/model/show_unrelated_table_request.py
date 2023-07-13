# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowUnrelatedTableRequest:

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
        'body': 'SearchParametersExt'
    }

    attribute_map = {
        'workspace': 'workspace',
        'body': 'body'
    }

    def __init__(self, workspace=None, body=None):
        """ShowUnrelatedTableRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param body: Body of the ShowUnrelatedTableRequest
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.SearchParametersExt`
        """
        
        

        self._workspace = None
        self._body = None
        self.discriminator = None

        self.workspace = workspace
        if body is not None:
            self.body = body

    @property
    def workspace(self):
        """Gets the workspace of this ShowUnrelatedTableRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ShowUnrelatedTableRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ShowUnrelatedTableRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ShowUnrelatedTableRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def body(self):
        """Gets the body of this ShowUnrelatedTableRequest.

        :return: The body of this ShowUnrelatedTableRequest.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SearchParametersExt`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ShowUnrelatedTableRequest.

        :param body: The body of this ShowUnrelatedTableRequest.
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.SearchParametersExt`
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
        if not isinstance(other, ShowUnrelatedTableRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
