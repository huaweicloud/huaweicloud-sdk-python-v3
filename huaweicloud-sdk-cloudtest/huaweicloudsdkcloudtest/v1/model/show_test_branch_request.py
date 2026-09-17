# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTestBranchRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'branch_uri': 'str',
        'project_uuid': 'str'
    }

    attribute_map = {
        'branch_uri': 'branch_uri',
        'project_uuid': 'project_uuid'
    }

    def __init__(self, branch_uri=None, project_uuid=None):
        r"""ShowTestBranchRequest

        The model defined in huaweicloud sdk

        :param branch_uri: 分支URI
        :type branch_uri: str
        :param project_uuid: 项目ID
        :type project_uuid: str
        """
        
        

        self._branch_uri = None
        self._project_uuid = None
        self.discriminator = None

        self.branch_uri = branch_uri
        if project_uuid is not None:
            self.project_uuid = project_uuid

    @property
    def branch_uri(self):
        r"""Gets the branch_uri of this ShowTestBranchRequest.

        分支URI

        :return: The branch_uri of this ShowTestBranchRequest.
        :rtype: str
        """
        return self._branch_uri

    @branch_uri.setter
    def branch_uri(self, branch_uri):
        r"""Sets the branch_uri of this ShowTestBranchRequest.

        分支URI

        :param branch_uri: The branch_uri of this ShowTestBranchRequest.
        :type branch_uri: str
        """
        self._branch_uri = branch_uri

    @property
    def project_uuid(self):
        r"""Gets the project_uuid of this ShowTestBranchRequest.

        项目ID

        :return: The project_uuid of this ShowTestBranchRequest.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        r"""Sets the project_uuid of this ShowTestBranchRequest.

        项目ID

        :param project_uuid: The project_uuid of this ShowTestBranchRequest.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

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
        if not isinstance(other, ShowTestBranchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
