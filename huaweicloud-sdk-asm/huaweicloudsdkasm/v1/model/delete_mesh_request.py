# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteMeshRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mesh_id': 'str',
        'content_type': 'str',
        'x_apply_project_id': 'str'
    }

    attribute_map = {
        'mesh_id': 'mesh_id',
        'content_type': 'Content-Type',
        'x_apply_project_id': 'X-Apply-ProjectID'
    }

    def __init__(self, mesh_id=None, content_type=None, x_apply_project_id=None):
        """DeleteMeshRequest

        The model defined in huaweicloud sdk

        :param mesh_id: 网格ID
        :type mesh_id: str
        :param content_type: 消息体的类型（格式）
        :type content_type: str
        :param x_apply_project_id: 网格所属ProjectID
        :type x_apply_project_id: str
        """
        
        

        self._mesh_id = None
        self._content_type = None
        self._x_apply_project_id = None
        self.discriminator = None

        self.mesh_id = mesh_id
        self.content_type = content_type
        if x_apply_project_id is not None:
            self.x_apply_project_id = x_apply_project_id

    @property
    def mesh_id(self):
        """Gets the mesh_id of this DeleteMeshRequest.

        网格ID

        :return: The mesh_id of this DeleteMeshRequest.
        :rtype: str
        """
        return self._mesh_id

    @mesh_id.setter
    def mesh_id(self, mesh_id):
        """Sets the mesh_id of this DeleteMeshRequest.

        网格ID

        :param mesh_id: The mesh_id of this DeleteMeshRequest.
        :type mesh_id: str
        """
        self._mesh_id = mesh_id

    @property
    def content_type(self):
        """Gets the content_type of this DeleteMeshRequest.

        消息体的类型（格式）

        :return: The content_type of this DeleteMeshRequest.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this DeleteMeshRequest.

        消息体的类型（格式）

        :param content_type: The content_type of this DeleteMeshRequest.
        :type content_type: str
        """
        self._content_type = content_type

    @property
    def x_apply_project_id(self):
        """Gets the x_apply_project_id of this DeleteMeshRequest.

        网格所属ProjectID

        :return: The x_apply_project_id of this DeleteMeshRequest.
        :rtype: str
        """
        return self._x_apply_project_id

    @x_apply_project_id.setter
    def x_apply_project_id(self, x_apply_project_id):
        """Sets the x_apply_project_id of this DeleteMeshRequest.

        网格所属ProjectID

        :param x_apply_project_id: The x_apply_project_id of this DeleteMeshRequest.
        :type x_apply_project_id: str
        """
        self._x_apply_project_id = x_apply_project_id

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
        if not isinstance(other, DeleteMeshRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
