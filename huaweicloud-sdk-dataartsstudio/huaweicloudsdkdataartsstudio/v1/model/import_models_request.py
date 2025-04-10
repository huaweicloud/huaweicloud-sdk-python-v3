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
        'x_project_id': 'str',
        'x_language': 'str',
        'action_id': 'str',
        'model_id': 'str',
        'directory_id': 'str',
        'skip_exist': 'bool',
        'body': 'ImportModelsRequestBody'
    }

    attribute_map = {
        'workspace': 'workspace',
        'x_project_id': 'X-Project-Id',
        'x_language': 'X-Language',
        'action_id': 'action-id',
        'model_id': 'model_id',
        'directory_id': 'directory_id',
        'skip_exist': 'skip-exist',
        'body': 'body'
    }

    def __init__(self, workspace=None, x_project_id=None, x_language=None, action_id=None, model_id=None, directory_id=None, skip_exist=None, body=None):
        r"""ImportModelsRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace: str
        :param x_project_id: 项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。
        :type x_project_id: str
        :param x_language: 默认值：en-us 可选，导入导出接口必填，可选值有：zh-cn、en-us，分别表示中文、英文。
        :type x_language: str
        :param action_id: 需要执行的动作，根据导入的对象不同而选择不同的导入动作。 枚举值：   - import_relation: 导入关系模型：逻辑实体/物理表   - import_dimension: 导入维度表、事实表   - import_codetable: 导入码表   - import_datastandard: 导入数据标准   - import_bizmetric: 导入业务指标   - import_bizcatalog: 导入流程架构   - import_atomic: 导入原子指标   - import_derivative: 导入衍生指标   - import_compound: 导入复合指标   - import_aggregation: 导入汇总表 
        :type action_id: str
        :param model_id: 关系建模的模型ID，在导入模型（import_relation）时必填。
        :type model_id: str
        :param directory_id: 导入的目录id，在导入码表（import_codetable）和数据标准（import_datastandard）时生效，选填。
        :type directory_id: str
        :param skip_exist: 是否需要覆盖更新已有的实体。
        :type skip_exist: bool
        :param body: Body of the ImportModelsRequest
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.ImportModelsRequestBody`
        """
        
        

        self._workspace = None
        self._x_project_id = None
        self._x_language = None
        self._action_id = None
        self._model_id = None
        self._directory_id = None
        self._skip_exist = None
        self._body = None
        self.discriminator = None

        self.workspace = workspace
        if x_project_id is not None:
            self.x_project_id = x_project_id
        if x_language is not None:
            self.x_language = x_language
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
        r"""Gets the workspace of this ImportModelsRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this ImportModelsRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ImportModelsRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this ImportModelsRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def x_project_id(self):
        r"""Gets the x_project_id of this ImportModelsRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :return: The x_project_id of this ImportModelsRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        r"""Sets the x_project_id of this ImportModelsRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :param x_project_id: The x_project_id of this ImportModelsRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def x_language(self):
        r"""Gets the x_language of this ImportModelsRequest.

        默认值：en-us 可选，导入导出接口必填，可选值有：zh-cn、en-us，分别表示中文、英文。

        :return: The x_language of this ImportModelsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ImportModelsRequest.

        默认值：en-us 可选，导入导出接口必填，可选值有：zh-cn、en-us，分别表示中文、英文。

        :param x_language: The x_language of this ImportModelsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def action_id(self):
        r"""Gets the action_id of this ImportModelsRequest.

        需要执行的动作，根据导入的对象不同而选择不同的导入动作。 枚举值：   - import_relation: 导入关系模型：逻辑实体/物理表   - import_dimension: 导入维度表、事实表   - import_codetable: 导入码表   - import_datastandard: 导入数据标准   - import_bizmetric: 导入业务指标   - import_bizcatalog: 导入流程架构   - import_atomic: 导入原子指标   - import_derivative: 导入衍生指标   - import_compound: 导入复合指标   - import_aggregation: 导入汇总表 

        :return: The action_id of this ImportModelsRequest.
        :rtype: str
        """
        return self._action_id

    @action_id.setter
    def action_id(self, action_id):
        r"""Sets the action_id of this ImportModelsRequest.

        需要执行的动作，根据导入的对象不同而选择不同的导入动作。 枚举值：   - import_relation: 导入关系模型：逻辑实体/物理表   - import_dimension: 导入维度表、事实表   - import_codetable: 导入码表   - import_datastandard: 导入数据标准   - import_bizmetric: 导入业务指标   - import_bizcatalog: 导入流程架构   - import_atomic: 导入原子指标   - import_derivative: 导入衍生指标   - import_compound: 导入复合指标   - import_aggregation: 导入汇总表 

        :param action_id: The action_id of this ImportModelsRequest.
        :type action_id: str
        """
        self._action_id = action_id

    @property
    def model_id(self):
        r"""Gets the model_id of this ImportModelsRequest.

        关系建模的模型ID，在导入模型（import_relation）时必填。

        :return: The model_id of this ImportModelsRequest.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        r"""Sets the model_id of this ImportModelsRequest.

        关系建模的模型ID，在导入模型（import_relation）时必填。

        :param model_id: The model_id of this ImportModelsRequest.
        :type model_id: str
        """
        self._model_id = model_id

    @property
    def directory_id(self):
        r"""Gets the directory_id of this ImportModelsRequest.

        导入的目录id，在导入码表（import_codetable）和数据标准（import_datastandard）时生效，选填。

        :return: The directory_id of this ImportModelsRequest.
        :rtype: str
        """
        return self._directory_id

    @directory_id.setter
    def directory_id(self, directory_id):
        r"""Sets the directory_id of this ImportModelsRequest.

        导入的目录id，在导入码表（import_codetable）和数据标准（import_datastandard）时生效，选填。

        :param directory_id: The directory_id of this ImportModelsRequest.
        :type directory_id: str
        """
        self._directory_id = directory_id

    @property
    def skip_exist(self):
        r"""Gets the skip_exist of this ImportModelsRequest.

        是否需要覆盖更新已有的实体。

        :return: The skip_exist of this ImportModelsRequest.
        :rtype: bool
        """
        return self._skip_exist

    @skip_exist.setter
    def skip_exist(self, skip_exist):
        r"""Sets the skip_exist of this ImportModelsRequest.

        是否需要覆盖更新已有的实体。

        :param skip_exist: The skip_exist of this ImportModelsRequest.
        :type skip_exist: bool
        """
        self._skip_exist = skip_exist

    @property
    def body(self):
        r"""Gets the body of this ImportModelsRequest.

        :return: The body of this ImportModelsRequest.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ImportModelsRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ImportModelsRequest.

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
