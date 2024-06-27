# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBranchRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'branch_id': 'str',
        'project_uuid': 'str'
    }

    attribute_map = {
        'branch_id': 'branch_id',
        'project_uuid': 'project_uuid'
    }

    def __init__(self, branch_id=None, project_uuid=None):
        """ShowBranchRequest

        The model defined in huaweicloud sdk

        :param branch_id: 分支URI
        :type branch_id: str
        :param project_uuid: 项目ID
        :type project_uuid: str
        """
        
        

        self._branch_id = None
        self._project_uuid = None
        self.discriminator = None

        self.branch_id = branch_id
        if project_uuid is not None:
            self.project_uuid = project_uuid

    @property
    def branch_id(self):
        """Gets the branch_id of this ShowBranchRequest.

        分支URI

        :return: The branch_id of this ShowBranchRequest.
        :rtype: str
        """
        return self._branch_id

    @branch_id.setter
    def branch_id(self, branch_id):
        """Sets the branch_id of this ShowBranchRequest.

        分支URI

        :param branch_id: The branch_id of this ShowBranchRequest.
        :type branch_id: str
        """
        self._branch_id = branch_id

    @property
    def project_uuid(self):
        """Gets the project_uuid of this ShowBranchRequest.

        项目ID

        :return: The project_uuid of this ShowBranchRequest.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        """Sets the project_uuid of this ShowBranchRequest.

        项目ID

        :param project_uuid: The project_uuid of this ShowBranchRequest.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

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
        if not isinstance(other, ShowBranchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
