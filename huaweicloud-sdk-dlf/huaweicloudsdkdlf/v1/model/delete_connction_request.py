# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteConnctionRequest:

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
        'connection_name': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'connection_name': 'connection_name'
    }

    def __init__(self, workspace=None, connection_name=None):
        """DeleteConnctionRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间id
        :type workspace: str
        :param connection_name: 连接名称.
        :type connection_name: str
        """
        
        

        self._workspace = None
        self._connection_name = None
        self.discriminator = None

        if workspace is not None:
            self.workspace = workspace
        self.connection_name = connection_name

    @property
    def workspace(self):
        """Gets the workspace of this DeleteConnctionRequest.

        工作空间id

        :return: The workspace of this DeleteConnctionRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this DeleteConnctionRequest.

        工作空间id

        :param workspace: The workspace of this DeleteConnctionRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def connection_name(self):
        """Gets the connection_name of this DeleteConnctionRequest.

        连接名称.

        :return: The connection_name of this DeleteConnctionRequest.
        :rtype: str
        """
        return self._connection_name

    @connection_name.setter
    def connection_name(self, connection_name):
        """Sets the connection_name of this DeleteConnctionRequest.

        连接名称.

        :param connection_name: The connection_name of this DeleteConnctionRequest.
        :type connection_name: str
        """
        self._connection_name = connection_name

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
        if not isinstance(other, DeleteConnctionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
