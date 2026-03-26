# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteJobRunRequest:

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
        'run_id': 'str'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'run_id': 'run_id'
    }

    def __init__(self, workspace_id=None, run_id=None):
        r"""DeleteJobRunRequest

        The model defined in huaweicloud sdk

        :param workspace_id: Workspace的ID
        :type workspace_id: str
        :param run_id: 作业运行的ID
        :type run_id: str
        """
        
        

        self._workspace_id = None
        self._run_id = None
        self.discriminator = None

        self.workspace_id = workspace_id
        self.run_id = run_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this DeleteJobRunRequest.

        Workspace的ID

        :return: The workspace_id of this DeleteJobRunRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this DeleteJobRunRequest.

        Workspace的ID

        :param workspace_id: The workspace_id of this DeleteJobRunRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def run_id(self):
        r"""Gets the run_id of this DeleteJobRunRequest.

        作业运行的ID

        :return: The run_id of this DeleteJobRunRequest.
        :rtype: str
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        r"""Sets the run_id of this DeleteJobRunRequest.

        作业运行的ID

        :param run_id: The run_id of this DeleteJobRunRequest.
        :type run_id: str
        """
        self._run_id = run_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DeleteJobRunRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
