# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEndpointRequest:

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
        'endpoint_id': 'str',
        'version': 'str'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'endpoint_id': 'endpoint_id',
        'version': 'version'
    }

    def __init__(self, workspace_id=None, endpoint_id=None, version=None):
        r"""ShowEndpointRequest

        The model defined in huaweicloud sdk

        :param workspace_id: Workspace的ID
        :type workspace_id: str
        :param endpoint_id: Endpoint的ID
        :type endpoint_id: str
        :param version: 查询endpoint信息的版本：CURRENT-当前版本，PREVIOUS-上个版本
        :type version: str
        """
        
        

        self._workspace_id = None
        self._endpoint_id = None
        self._version = None
        self.discriminator = None

        self.workspace_id = workspace_id
        self.endpoint_id = endpoint_id
        if version is not None:
            self.version = version

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ShowEndpointRequest.

        Workspace的ID

        :return: The workspace_id of this ShowEndpointRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ShowEndpointRequest.

        Workspace的ID

        :param workspace_id: The workspace_id of this ShowEndpointRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def endpoint_id(self):
        r"""Gets the endpoint_id of this ShowEndpointRequest.

        Endpoint的ID

        :return: The endpoint_id of this ShowEndpointRequest.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        r"""Sets the endpoint_id of this ShowEndpointRequest.

        Endpoint的ID

        :param endpoint_id: The endpoint_id of this ShowEndpointRequest.
        :type endpoint_id: str
        """
        self._endpoint_id = endpoint_id

    @property
    def version(self):
        r"""Gets the version of this ShowEndpointRequest.

        查询endpoint信息的版本：CURRENT-当前版本，PREVIOUS-上个版本

        :return: The version of this ShowEndpointRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ShowEndpointRequest.

        查询endpoint信息的版本：CURRENT-当前版本，PREVIOUS-上个版本

        :param version: The version of this ShowEndpointRequest.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, ShowEndpointRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
