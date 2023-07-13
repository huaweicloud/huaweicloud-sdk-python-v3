# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CountTableModelsRequest:

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
        'model_id': 'int'
    }

    attribute_map = {
        'workspace': 'workspace',
        'model_id': 'model_id'
    }

    def __init__(self, workspace=None, model_id=None):
        """CountTableModelsRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param model_id: 依据model_id查工作区
        :type model_id: int
        """
        
        

        self._workspace = None
        self._model_id = None
        self.discriminator = None

        self.workspace = workspace
        if model_id is not None:
            self.model_id = model_id

    @property
    def workspace(self):
        """Gets the workspace of this CountTableModelsRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this CountTableModelsRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this CountTableModelsRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this CountTableModelsRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def model_id(self):
        """Gets the model_id of this CountTableModelsRequest.

        依据model_id查工作区

        :return: The model_id of this CountTableModelsRequest.
        :rtype: int
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """Sets the model_id of this CountTableModelsRequest.

        依据model_id查工作区

        :param model_id: The model_id of this CountTableModelsRequest.
        :type model_id: int
        """
        self._model_id = model_id

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
        if not isinstance(other, CountTableModelsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
