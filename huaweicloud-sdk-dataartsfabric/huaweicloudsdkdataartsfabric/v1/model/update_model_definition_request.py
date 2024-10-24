# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateModelDefinitionRequest:

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
        'model_id': 'str',
        'body': 'UpdateModelInput'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'model_id': 'model_id',
        'body': 'body'
    }

    def __init__(self, workspace_id=None, model_id=None, body=None):
        """UpdateModelDefinitionRequest

        The model defined in huaweicloud sdk

        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param model_id: Service ID
        :type model_id: str
        :param body: Body of the UpdateModelDefinitionRequest
        :type body: :class:`huaweicloudsdkdataartsfabric.v1.UpdateModelInput`
        """
        
        

        self._workspace_id = None
        self._model_id = None
        self._body = None
        self.discriminator = None

        self.workspace_id = workspace_id
        self.model_id = model_id
        if body is not None:
            self.body = body

    @property
    def workspace_id(self):
        """Gets the workspace_id of this UpdateModelDefinitionRequest.

        工作空间ID

        :return: The workspace_id of this UpdateModelDefinitionRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this UpdateModelDefinitionRequest.

        工作空间ID

        :param workspace_id: The workspace_id of this UpdateModelDefinitionRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def model_id(self):
        """Gets the model_id of this UpdateModelDefinitionRequest.

        Service ID

        :return: The model_id of this UpdateModelDefinitionRequest.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """Sets the model_id of this UpdateModelDefinitionRequest.

        Service ID

        :param model_id: The model_id of this UpdateModelDefinitionRequest.
        :type model_id: str
        """
        self._model_id = model_id

    @property
    def body(self):
        """Gets the body of this UpdateModelDefinitionRequest.

        :return: The body of this UpdateModelDefinitionRequest.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.UpdateModelInput`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateModelDefinitionRequest.

        :param body: The body of this UpdateModelDefinitionRequest.
        :type body: :class:`huaweicloudsdkdataartsfabric.v1.UpdateModelInput`
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
        if not isinstance(other, UpdateModelDefinitionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
