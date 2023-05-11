# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScriptResultsRequest:

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
        'instance_id': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'script_name': 'script_name',
        'instance_id': 'instance_id'
    }

    def __init__(self, workspace=None, script_name=None, instance_id=None):
        """ListScriptResultsRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间id
        :type workspace: str
        :param script_name: 
        :type script_name: str
        :param instance_id: 
        :type instance_id: str
        """
        
        

        self._workspace = None
        self._script_name = None
        self._instance_id = None
        self.discriminator = None

        if workspace is not None:
            self.workspace = workspace
        self.script_name = script_name
        self.instance_id = instance_id

    @property
    def workspace(self):
        """Gets the workspace of this ListScriptResultsRequest.

        工作空间id

        :return: The workspace of this ListScriptResultsRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ListScriptResultsRequest.

        工作空间id

        :param workspace: The workspace of this ListScriptResultsRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def script_name(self):
        """Gets the script_name of this ListScriptResultsRequest.

        :return: The script_name of this ListScriptResultsRequest.
        :rtype: str
        """
        return self._script_name

    @script_name.setter
    def script_name(self, script_name):
        """Sets the script_name of this ListScriptResultsRequest.

        :param script_name: The script_name of this ListScriptResultsRequest.
        :type script_name: str
        """
        self._script_name = script_name

    @property
    def instance_id(self):
        """Gets the instance_id of this ListScriptResultsRequest.

        :return: The instance_id of this ListScriptResultsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListScriptResultsRequest.

        :param instance_id: The instance_id of this ListScriptResultsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

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
        if not isinstance(other, ListScriptResultsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
