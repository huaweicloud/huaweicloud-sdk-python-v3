# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetDevServerJobServiceResponse(SdkResponse):

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
        'status': 'str',
        'spec': 'dict(str, str)',
        'instances': 'list[AIServiceInstance]',
        'model': 'Model'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'spec': 'spec',
        'instances': 'instances',
        'model': 'model'
    }

    def __init__(self, id=None, name=None, status=None, spec=None, instances=None, model=None):
        r"""GetDevServerJobServiceResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释**：部署服务的id。 **取值范围**：不涉及。
        :type id: str
        :param name: **参数解释**：部署服务名称。 **取值范围**：不涉及。
        :type name: str
        :param status: **参数解释**：部署实例状态。 **取值范围**：- CREATING  - RUNNING  - FAILED  -DELETED  - ERROR。
        :type status: str
        :param spec: **参数解释**：部署服务特性参数。 **取值范围**：不涉及。
        :type spec: dict(str, str)
        :param instances: **参数解释**：部署服务实例。
        :type instances: list[:class:`huaweicloudsdkmodelarts.v1.AIServiceInstance`]
        :param model: 
        :type model: :class:`huaweicloudsdkmodelarts.v1.Model`
        """
        
        super().__init__()

        self._id = None
        self._name = None
        self._status = None
        self._spec = None
        self._instances = None
        self._model = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if spec is not None:
            self.spec = spec
        if instances is not None:
            self.instances = instances
        if model is not None:
            self.model = model

    @property
    def id(self):
        r"""Gets the id of this GetDevServerJobServiceResponse.

        **参数解释**：部署服务的id。 **取值范围**：不涉及。

        :return: The id of this GetDevServerJobServiceResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GetDevServerJobServiceResponse.

        **参数解释**：部署服务的id。 **取值范围**：不涉及。

        :param id: The id of this GetDevServerJobServiceResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this GetDevServerJobServiceResponse.

        **参数解释**：部署服务名称。 **取值范围**：不涉及。

        :return: The name of this GetDevServerJobServiceResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GetDevServerJobServiceResponse.

        **参数解释**：部署服务名称。 **取值范围**：不涉及。

        :param name: The name of this GetDevServerJobServiceResponse.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this GetDevServerJobServiceResponse.

        **参数解释**：部署实例状态。 **取值范围**：- CREATING  - RUNNING  - FAILED  -DELETED  - ERROR。

        :return: The status of this GetDevServerJobServiceResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this GetDevServerJobServiceResponse.

        **参数解释**：部署实例状态。 **取值范围**：- CREATING  - RUNNING  - FAILED  -DELETED  - ERROR。

        :param status: The status of this GetDevServerJobServiceResponse.
        :type status: str
        """
        self._status = status

    @property
    def spec(self):
        r"""Gets the spec of this GetDevServerJobServiceResponse.

        **参数解释**：部署服务特性参数。 **取值范围**：不涉及。

        :return: The spec of this GetDevServerJobServiceResponse.
        :rtype: dict(str, str)
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this GetDevServerJobServiceResponse.

        **参数解释**：部署服务特性参数。 **取值范围**：不涉及。

        :param spec: The spec of this GetDevServerJobServiceResponse.
        :type spec: dict(str, str)
        """
        self._spec = spec

    @property
    def instances(self):
        r"""Gets the instances of this GetDevServerJobServiceResponse.

        **参数解释**：部署服务实例。

        :return: The instances of this GetDevServerJobServiceResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.AIServiceInstance`]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        r"""Sets the instances of this GetDevServerJobServiceResponse.

        **参数解释**：部署服务实例。

        :param instances: The instances of this GetDevServerJobServiceResponse.
        :type instances: list[:class:`huaweicloudsdkmodelarts.v1.AIServiceInstance`]
        """
        self._instances = instances

    @property
    def model(self):
        r"""Gets the model of this GetDevServerJobServiceResponse.

        :return: The model of this GetDevServerJobServiceResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Model`
        """
        return self._model

    @model.setter
    def model(self, model):
        r"""Sets the model of this GetDevServerJobServiceResponse.

        :param model: The model of this GetDevServerJobServiceResponse.
        :type model: :class:`huaweicloudsdkmodelarts.v1.Model`
        """
        self._model = model

    def to_dict(self):
        import warnings
        warnings.warn("GetDevServerJobServiceResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, GetDevServerJobServiceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
