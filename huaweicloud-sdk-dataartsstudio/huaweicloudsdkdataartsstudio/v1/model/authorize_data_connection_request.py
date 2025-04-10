# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuthorizeDataConnectionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_connection_id': 'str',
        'workspace_id': 'str'
    }

    attribute_map = {
        'data_connection_id': 'data_connection_id',
        'workspace_id': 'workspace_id'
    }

    def __init__(self, data_connection_id=None, workspace_id=None):
        r"""AuthorizeDataConnectionRequest

        The model defined in huaweicloud sdk

        :param data_connection_id: 需要授权的数据连接id。
        :type data_connection_id: str
        :param workspace_id: 需要授权的工作空间id。
        :type workspace_id: str
        """
        
        

        self._data_connection_id = None
        self._workspace_id = None
        self.discriminator = None

        self.data_connection_id = data_connection_id
        if workspace_id is not None:
            self.workspace_id = workspace_id

    @property
    def data_connection_id(self):
        r"""Gets the data_connection_id of this AuthorizeDataConnectionRequest.

        需要授权的数据连接id。

        :return: The data_connection_id of this AuthorizeDataConnectionRequest.
        :rtype: str
        """
        return self._data_connection_id

    @data_connection_id.setter
    def data_connection_id(self, data_connection_id):
        r"""Sets the data_connection_id of this AuthorizeDataConnectionRequest.

        需要授权的数据连接id。

        :param data_connection_id: The data_connection_id of this AuthorizeDataConnectionRequest.
        :type data_connection_id: str
        """
        self._data_connection_id = data_connection_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this AuthorizeDataConnectionRequest.

        需要授权的工作空间id。

        :return: The workspace_id of this AuthorizeDataConnectionRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this AuthorizeDataConnectionRequest.

        需要授权的工作空间id。

        :param workspace_id: The workspace_id of this AuthorizeDataConnectionRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

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
        if not isinstance(other, AuthorizeDataConnectionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
