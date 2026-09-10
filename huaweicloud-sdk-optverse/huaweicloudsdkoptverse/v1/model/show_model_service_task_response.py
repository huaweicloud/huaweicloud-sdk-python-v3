# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowModelServiceTaskResponse(SdkResponse):

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
        'type': 'str',
        'status': 'str',
        'error_msg': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'outputs': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'status': 'status',
        'error_msg': 'error_msg',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'outputs': 'outputs'
    }

    def __init__(self, id=None, type=None, status=None, error_msg=None, create_time=None, update_time=None, outputs=None):
        r"""ShowModelServiceTaskResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 任务ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type id: str
        :param type: **参数解释**： 任务类型。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type type: str
        :param status: **参数解释**： 任务状态。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type status: str
        :param error_msg: **参数解释**： 错误信息。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type error_msg: str
        :param create_time: **参数解释**： 创建时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type create_time: str
        :param update_time: **参数解释**： 更新时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type update_time: str
        :param outputs: **参数解释**： 任务输出。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type outputs: dict(str, object)
        """
        
        super().__init__()

        self._id = None
        self._type = None
        self._status = None
        self._error_msg = None
        self._create_time = None
        self._update_time = None
        self._outputs = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if error_msg is not None:
            self.error_msg = error_msg
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if outputs is not None:
            self.outputs = outputs

    @property
    def id(self):
        r"""Gets the id of this ShowModelServiceTaskResponse.

        **参数解释**： 任务ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The id of this ShowModelServiceTaskResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowModelServiceTaskResponse.

        **参数解释**： 任务ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param id: The id of this ShowModelServiceTaskResponse.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this ShowModelServiceTaskResponse.

        **参数解释**： 任务类型。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The type of this ShowModelServiceTaskResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowModelServiceTaskResponse.

        **参数解释**： 任务类型。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param type: The type of this ShowModelServiceTaskResponse.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this ShowModelServiceTaskResponse.

        **参数解释**： 任务状态。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The status of this ShowModelServiceTaskResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowModelServiceTaskResponse.

        **参数解释**： 任务状态。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param status: The status of this ShowModelServiceTaskResponse.
        :type status: str
        """
        self._status = status

    @property
    def error_msg(self):
        r"""Gets the error_msg of this ShowModelServiceTaskResponse.

        **参数解释**： 错误信息。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The error_msg of this ShowModelServiceTaskResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this ShowModelServiceTaskResponse.

        **参数解释**： 错误信息。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param error_msg: The error_msg of this ShowModelServiceTaskResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowModelServiceTaskResponse.

        **参数解释**： 创建时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The create_time of this ShowModelServiceTaskResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowModelServiceTaskResponse.

        **参数解释**： 创建时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param create_time: The create_time of this ShowModelServiceTaskResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowModelServiceTaskResponse.

        **参数解释**： 更新时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The update_time of this ShowModelServiceTaskResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowModelServiceTaskResponse.

        **参数解释**： 更新时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param update_time: The update_time of this ShowModelServiceTaskResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def outputs(self):
        r"""Gets the outputs of this ShowModelServiceTaskResponse.

        **参数解释**： 任务输出。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The outputs of this ShowModelServiceTaskResponse.
        :rtype: dict(str, object)
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        r"""Sets the outputs of this ShowModelServiceTaskResponse.

        **参数解释**： 任务输出。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param outputs: The outputs of this ShowModelServiceTaskResponse.
        :type outputs: dict(str, object)
        """
        self._outputs = outputs

    def to_dict(self):
        import warnings
        warnings.warn("ShowModelServiceTaskResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowModelServiceTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
