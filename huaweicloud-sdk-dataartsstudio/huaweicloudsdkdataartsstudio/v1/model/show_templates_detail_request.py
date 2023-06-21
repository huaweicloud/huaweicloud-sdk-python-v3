# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTemplatesDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'workspace': 'str'
    }

    attribute_map = {
        'id': 'id',
        'workspace': 'workspace'
    }

    def __init__(self, id=None, workspace=None):
        """ShowTemplatesDetailRequest

        The model defined in huaweicloud sdk

        :param id: id
        :type id: int
        :param workspace: workspace 信息
        :type workspace: str
        """
        
        

        self._id = None
        self._workspace = None
        self.discriminator = None

        self.id = id
        self.workspace = workspace

    @property
    def id(self):
        """Gets the id of this ShowTemplatesDetailRequest.

        id

        :return: The id of this ShowTemplatesDetailRequest.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowTemplatesDetailRequest.

        id

        :param id: The id of this ShowTemplatesDetailRequest.
        :type id: int
        """
        self._id = id

    @property
    def workspace(self):
        """Gets the workspace of this ShowTemplatesDetailRequest.

        workspace 信息

        :return: The workspace of this ShowTemplatesDetailRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ShowTemplatesDetailRequest.

        workspace 信息

        :param workspace: The workspace of this ShowTemplatesDetailRequest.
        :type workspace: str
        """
        self._workspace = workspace

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
        if not isinstance(other, ShowTemplatesDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
