# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobMetadataResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'workspace_id': 'str',
        'description': 'str',
        'create_time': 'int',
        'user_name': 'str',
        'annotations': 'dict(str, str)',
        'training_experiment_reference': 'TrainingExperimentResp'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'workspace_id': 'workspace_id',
        'description': 'description',
        'create_time': 'create_time',
        'user_name': 'user_name',
        'annotations': 'annotations',
        'training_experiment_reference': 'training_experiment_reference'
    }

    def __init__(self, id=None, name=None, workspace_id=None, description=None, create_time=None, user_name=None, annotations=None, training_experiment_reference=None):
        r"""JobMetadataResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释**：训练作业ID，创建成功后由ModelArts生成返回，无需填写。 **取值范围**：不涉及。
        :type id: str
        :param name: **参数解释**：训练作业名称。 **取值范围**：限制为1-64位只含数字、字母、下划线和中划线的名称。
        :type name: str
        :param workspace_id: **参数解释**：指定作业所处的工作空间。 **取值范围**：不涉及。
        :type workspace_id: str
        :param description: **参数解释**：对训练作业的描述。 **取值范围**：不涉及。
        :type description: str
        :param create_time: **参数解释**：训练作业创建时间戳，单位为毫秒，创建成功后由ModelArts生成返回，无需填写。 **取值范围**：不涉及。
        :type create_time: int
        :param user_name: **参数解释**：训练作业创建用户的用户名，创建成功后由ModelArts生成返回，无需填写。 **取值范围**：不涉及。
        :type user_name: str
        :param annotations: **参数解释**：训练作业高级功能配置。
        :type annotations: dict(str, str)
        :param training_experiment_reference: 
        :type training_experiment_reference: :class:`huaweicloudsdkmodelarts.v1.TrainingExperimentResp`
        """
        
        

        self._id = None
        self._name = None
        self._workspace_id = None
        self._description = None
        self._create_time = None
        self._user_name = None
        self._annotations = None
        self._training_experiment_reference = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if description is not None:
            self.description = description
        if create_time is not None:
            self.create_time = create_time
        if user_name is not None:
            self.user_name = user_name
        if annotations is not None:
            self.annotations = annotations
        if training_experiment_reference is not None:
            self.training_experiment_reference = training_experiment_reference

    @property
    def id(self):
        r"""Gets the id of this JobMetadataResponse.

        **参数解释**：训练作业ID，创建成功后由ModelArts生成返回，无需填写。 **取值范围**：不涉及。

        :return: The id of this JobMetadataResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this JobMetadataResponse.

        **参数解释**：训练作业ID，创建成功后由ModelArts生成返回，无需填写。 **取值范围**：不涉及。

        :param id: The id of this JobMetadataResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this JobMetadataResponse.

        **参数解释**：训练作业名称。 **取值范围**：限制为1-64位只含数字、字母、下划线和中划线的名称。

        :return: The name of this JobMetadataResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this JobMetadataResponse.

        **参数解释**：训练作业名称。 **取值范围**：限制为1-64位只含数字、字母、下划线和中划线的名称。

        :param name: The name of this JobMetadataResponse.
        :type name: str
        """
        self._name = name

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this JobMetadataResponse.

        **参数解释**：指定作业所处的工作空间。 **取值范围**：不涉及。

        :return: The workspace_id of this JobMetadataResponse.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this JobMetadataResponse.

        **参数解释**：指定作业所处的工作空间。 **取值范围**：不涉及。

        :param workspace_id: The workspace_id of this JobMetadataResponse.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def description(self):
        r"""Gets the description of this JobMetadataResponse.

        **参数解释**：对训练作业的描述。 **取值范围**：不涉及。

        :return: The description of this JobMetadataResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this JobMetadataResponse.

        **参数解释**：对训练作业的描述。 **取值范围**：不涉及。

        :param description: The description of this JobMetadataResponse.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        r"""Gets the create_time of this JobMetadataResponse.

        **参数解释**：训练作业创建时间戳，单位为毫秒，创建成功后由ModelArts生成返回，无需填写。 **取值范围**：不涉及。

        :return: The create_time of this JobMetadataResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this JobMetadataResponse.

        **参数解释**：训练作业创建时间戳，单位为毫秒，创建成功后由ModelArts生成返回，无需填写。 **取值范围**：不涉及。

        :param create_time: The create_time of this JobMetadataResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def user_name(self):
        r"""Gets the user_name of this JobMetadataResponse.

        **参数解释**：训练作业创建用户的用户名，创建成功后由ModelArts生成返回，无需填写。 **取值范围**：不涉及。

        :return: The user_name of this JobMetadataResponse.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this JobMetadataResponse.

        **参数解释**：训练作业创建用户的用户名，创建成功后由ModelArts生成返回，无需填写。 **取值范围**：不涉及。

        :param user_name: The user_name of this JobMetadataResponse.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def annotations(self):
        r"""Gets the annotations of this JobMetadataResponse.

        **参数解释**：训练作业高级功能配置。

        :return: The annotations of this JobMetadataResponse.
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        r"""Sets the annotations of this JobMetadataResponse.

        **参数解释**：训练作业高级功能配置。

        :param annotations: The annotations of this JobMetadataResponse.
        :type annotations: dict(str, str)
        """
        self._annotations = annotations

    @property
    def training_experiment_reference(self):
        r"""Gets the training_experiment_reference of this JobMetadataResponse.

        :return: The training_experiment_reference of this JobMetadataResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.TrainingExperimentResp`
        """
        return self._training_experiment_reference

    @training_experiment_reference.setter
    def training_experiment_reference(self, training_experiment_reference):
        r"""Sets the training_experiment_reference of this JobMetadataResponse.

        :param training_experiment_reference: The training_experiment_reference of this JobMetadataResponse.
        :type training_experiment_reference: :class:`huaweicloudsdkmodelarts.v1.TrainingExperimentResp`
        """
        self._training_experiment_reference = training_experiment_reference

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
        if not isinstance(other, JobMetadataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
