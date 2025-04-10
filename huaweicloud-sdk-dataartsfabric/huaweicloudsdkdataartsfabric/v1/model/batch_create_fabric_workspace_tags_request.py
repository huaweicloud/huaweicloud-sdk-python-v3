# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateFabricWorkspaceTagsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace_id': 'str',
        'body': 'BatchCreateTagsRequestBody'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'body': 'body'
    }

    def __init__(self, workspace_id=None, body=None):
        r"""BatchCreateFabricWorkspaceTagsRequest

        The model defined in huaweicloud sdk

        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param body: Body of the BatchCreateFabricWorkspaceTagsRequest
        :type body: :class:`huaweicloudsdkdataartsfabric.v1.BatchCreateTagsRequestBody`
        """
        
        

        self._workspace_id = None
        self._body = None
        self.discriminator = None

        self.workspace_id = workspace_id
        if body is not None:
            self.body = body

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this BatchCreateFabricWorkspaceTagsRequest.

        工作空间ID

        :return: The workspace_id of this BatchCreateFabricWorkspaceTagsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this BatchCreateFabricWorkspaceTagsRequest.

        工作空间ID

        :param workspace_id: The workspace_id of this BatchCreateFabricWorkspaceTagsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def body(self):
        r"""Gets the body of this BatchCreateFabricWorkspaceTagsRequest.

        :return: The body of this BatchCreateFabricWorkspaceTagsRequest.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.BatchCreateTagsRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this BatchCreateFabricWorkspaceTagsRequest.

        :param body: The body of this BatchCreateFabricWorkspaceTagsRequest.
        :type body: :class:`huaweicloudsdkdataartsfabric.v1.BatchCreateTagsRequestBody`
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
        if not isinstance(other, BatchCreateFabricWorkspaceTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
