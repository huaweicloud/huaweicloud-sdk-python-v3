# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDataobjectRelationRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'workspace_id': 'str',
        'dataclass_type': 'str',
        'data_object_id': 'str',
        'related_dataclass_type': 'str',
        'body': 'DataobjectSearch'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'dataclass_type': 'dataclass_type',
        'data_object_id': 'data_object_id',
        'related_dataclass_type': 'related_dataclass_type',
        'body': 'body'
    }

    def __init__(self, project_id=None, workspace_id=None, dataclass_type=None, data_object_id=None, related_dataclass_type=None, body=None):
        r"""ListDataobjectRelationRequest

        The model defined in huaweicloud sdk

        :param project_id: ID of project
        :type project_id: str
        :param workspace_id: ID of workspace
        :type workspace_id: str
        :param dataclass_type: type of dataclass
        :type dataclass_type: str
        :param data_object_id: ID of dataobject
        :type data_object_id: str
        :param related_dataclass_type: type of related dataclass
        :type related_dataclass_type: str
        :param body: Body of the ListDataobjectRelationRequest
        :type body: :class:`huaweicloudsdksa.v2.DataobjectSearch`
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._dataclass_type = None
        self._data_object_id = None
        self._related_dataclass_type = None
        self._body = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        self.dataclass_type = dataclass_type
        self.data_object_id = data_object_id
        self.related_dataclass_type = related_dataclass_type
        if body is not None:
            self.body = body

    @property
    def project_id(self):
        r"""Gets the project_id of this ListDataobjectRelationRequest.

        ID of project

        :return: The project_id of this ListDataobjectRelationRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListDataobjectRelationRequest.

        ID of project

        :param project_id: The project_id of this ListDataobjectRelationRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListDataobjectRelationRequest.

        ID of workspace

        :return: The workspace_id of this ListDataobjectRelationRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListDataobjectRelationRequest.

        ID of workspace

        :param workspace_id: The workspace_id of this ListDataobjectRelationRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def dataclass_type(self):
        r"""Gets the dataclass_type of this ListDataobjectRelationRequest.

        type of dataclass

        :return: The dataclass_type of this ListDataobjectRelationRequest.
        :rtype: str
        """
        return self._dataclass_type

    @dataclass_type.setter
    def dataclass_type(self, dataclass_type):
        r"""Sets the dataclass_type of this ListDataobjectRelationRequest.

        type of dataclass

        :param dataclass_type: The dataclass_type of this ListDataobjectRelationRequest.
        :type dataclass_type: str
        """
        self._dataclass_type = dataclass_type

    @property
    def data_object_id(self):
        r"""Gets the data_object_id of this ListDataobjectRelationRequest.

        ID of dataobject

        :return: The data_object_id of this ListDataobjectRelationRequest.
        :rtype: str
        """
        return self._data_object_id

    @data_object_id.setter
    def data_object_id(self, data_object_id):
        r"""Sets the data_object_id of this ListDataobjectRelationRequest.

        ID of dataobject

        :param data_object_id: The data_object_id of this ListDataobjectRelationRequest.
        :type data_object_id: str
        """
        self._data_object_id = data_object_id

    @property
    def related_dataclass_type(self):
        r"""Gets the related_dataclass_type of this ListDataobjectRelationRequest.

        type of related dataclass

        :return: The related_dataclass_type of this ListDataobjectRelationRequest.
        :rtype: str
        """
        return self._related_dataclass_type

    @related_dataclass_type.setter
    def related_dataclass_type(self, related_dataclass_type):
        r"""Sets the related_dataclass_type of this ListDataobjectRelationRequest.

        type of related dataclass

        :param related_dataclass_type: The related_dataclass_type of this ListDataobjectRelationRequest.
        :type related_dataclass_type: str
        """
        self._related_dataclass_type = related_dataclass_type

    @property
    def body(self):
        r"""Gets the body of this ListDataobjectRelationRequest.

        :return: The body of this ListDataobjectRelationRequest.
        :rtype: :class:`huaweicloudsdksa.v2.DataobjectSearch`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ListDataobjectRelationRequest.

        :param body: The body of this ListDataobjectRelationRequest.
        :type body: :class:`huaweicloudsdksa.v2.DataobjectSearch`
        """
        self._body = body

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
        if not isinstance(other, ListDataobjectRelationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
