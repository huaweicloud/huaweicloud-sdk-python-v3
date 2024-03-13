# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportModelsRequest:

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
        'action_id': 'str',
        'model_id': 'str',
        'directory_id': 'str',
        'skip_exist': 'bool',
        'body': 'ImportModelsRequestBody'
    }

    attribute_map = {
        'workspace': 'workspace',
        'action_id': 'action-id',
        'model_id': 'model_id',
        'directory_id': 'directory_id',
        'skip_exist': 'skip-exist',
        'body': 'body'
    }

    def __init__(self, workspace=None, action_id=None, model_id=None, directory_id=None, skip_exist=None, body=None):
        """ImportModelsRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param action_id: 需要执行的动作，根据导入的对象不同而选择不同的导入动作
        :type action_id: str
        :param model_id: 模型id，在导入模型（import_relation）时必填
        :type model_id: str
        :param directory_id: 导入的目录id，在导入码表（import_datastandard）和数据标准（import_datastandard）时生效，选填
        :type directory_id: str
        :param skip_exist: 是否需要覆盖更新已有的实体
        :type skip_exist: bool
        :param body: Body of the ImportModelsRequest
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.ImportModelsRequestBody`
        """
        
        

        self._workspace = None
        self._action_id = None
        self._model_id = None
        self._directory_id = None
        self._skip_exist = None
        self._body = None
        self.discriminator = None

        self.workspace = workspace
        self.action_id = action_id
        if model_id is not None:
            self.model_id = model_id
        if directory_id is not None:
            self.directory_id = directory_id
        if skip_exist is not None:
            self.skip_exist = skip_exist
        if body is not None:
            self.body = body

    @property
    def workspace(self):
        """Gets the workspace of this ImportModelsRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ImportModelsRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ImportModelsRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ImportModelsRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def action_id(self):
        """Gets the action_id of this ImportModelsRequest.

        需要执行的动作，根据导入的对象不同而选择不同的导入动作

        :return: The action_id of this ImportModelsRequest.
        :rtype: str
        """
        return self._action_id

    @action_id.setter
    def action_id(self, action_id):
        """Sets the action_id of this ImportModelsRequest.

        需要执行的动作，根据导入的对象不同而选择不同的导入动作

        :param action_id: The action_id of this ImportModelsRequest.
        :type action_id: str
        """
        self._action_id = action_id

    @property
    def model_id(self):
        """Gets the model_id of this ImportModelsRequest.

        模型id，在导入模型（import_relation）时必填

        :return: The model_id of this ImportModelsRequest.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """Sets the model_id of this ImportModelsRequest.

        模型id，在导入模型（import_relation）时必填

        :param model_id: The model_id of this ImportModelsRequest.
        :type model_id: str
        """
        self._model_id = model_id

    @property
    def directory_id(self):
        """Gets the directory_id of this ImportModelsRequest.

        导入的目录id，在导入码表（import_datastandard）和数据标准（import_datastandard）时生效，选填

        :return: The directory_id of this ImportModelsRequest.
        :rtype: str
        """
        return self._directory_id

    @directory_id.setter
    def directory_id(self, directory_id):
        """Sets the directory_id of this ImportModelsRequest.

        导入的目录id，在导入码表（import_datastandard）和数据标准（import_datastandard）时生效，选填

        :param directory_id: The directory_id of this ImportModelsRequest.
        :type directory_id: str
        """
        self._directory_id = directory_id

    @property
    def skip_exist(self):
        """Gets the skip_exist of this ImportModelsRequest.

        是否需要覆盖更新已有的实体

        :return: The skip_exist of this ImportModelsRequest.
        :rtype: bool
        """
        return self._skip_exist

    @skip_exist.setter
    def skip_exist(self, skip_exist):
        """Sets the skip_exist of this ImportModelsRequest.

        是否需要覆盖更新已有的实体

        :param skip_exist: The skip_exist of this ImportModelsRequest.
        :type skip_exist: bool
        """
        self._skip_exist = skip_exist

    @property
    def body(self):
        """Gets the body of this ImportModelsRequest.

        :return: The body of this ImportModelsRequest.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ImportModelsRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ImportModelsRequest.

        :param body: The body of this ImportModelsRequest.
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.ImportModelsRequestBody`
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
        if not isinstance(other, ImportModelsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
