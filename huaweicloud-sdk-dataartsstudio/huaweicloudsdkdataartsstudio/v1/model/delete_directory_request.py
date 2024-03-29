# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteDirectoryRequest:

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
        'ids': 'list[int]'
    }

    attribute_map = {
        'workspace': 'workspace',
        'ids': 'ids'
    }

    def __init__(self, workspace=None, ids=None):
        """DeleteDirectoryRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param ids: 实体id数组
        :type ids: list[int]
        """
        
        

        self._workspace = None
        self._ids = None
        self.discriminator = None

        self.workspace = workspace
        self.ids = ids

    @property
    def workspace(self):
        """Gets the workspace of this DeleteDirectoryRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this DeleteDirectoryRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this DeleteDirectoryRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this DeleteDirectoryRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def ids(self):
        """Gets the ids of this DeleteDirectoryRequest.

        实体id数组

        :return: The ids of this DeleteDirectoryRequest.
        :rtype: list[int]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this DeleteDirectoryRequest.

        实体id数组

        :param ids: The ids of this DeleteDirectoryRequest.
        :type ids: list[int]
        """
        self._ids = ids

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
        if not isinstance(other, DeleteDirectoryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
