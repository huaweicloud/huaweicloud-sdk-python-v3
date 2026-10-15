# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFederationResponse(SdkResponse):

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
        'display_name': 'str',
        'description': 'str',
        'status': 'str',
        'error': 'ErrorMessage',
        'ray_cluster_list': 'list[RayFederationRayClusterResponse]',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'creator': 'User'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'display_name': 'display_name',
        'description': 'description',
        'status': 'status',
        'error': 'error',
        'ray_cluster_list': 'ray_cluster_list',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'creator': 'creator'
    }

    def __init__(self, id=None, name=None, display_name=None, description=None, status=None, error=None, ray_cluster_list=None, create_time=None, update_time=None, creator=None):
        r"""CreateFederationResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释**：Ray联邦端点ID。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。
        :type id: str
        :param name: **参数解释**：Ray联邦端点名称。 **取值范围**：支持小写字母、数字、中划线，必须字母开头、字母或数字结尾，长度为1~63个字符。
        :type name: str
        :param display_name: **参数解释**：Ray联邦端点显示名称。 **取值范围**：长度为1~63个字符，支持字母、数字、中划线、汉字。
        :type display_name: str
        :param description: **参数解释**：Ray联邦端点描述。 **取值范围**：不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号、艾特符、井号、百分号、分号、左括号、右括号、竖线、星号、反斜杠。长度为0~1024个字符。
        :type description: str
        :param status: **参数解释**：Ray联邦端点状态。 **取值范围**：   - RUNNING：运行中。   - LIMITED_AVAILABLE：部分端点可用。   - FAULT：故障。   - WAITING：等待中。
        :type status: str
        :param error: 
        :type error: :class:`huaweicloudsdkaidatalake.v2.ErrorMessage`
        :param ray_cluster_list: **参数解释**：RayCluster端点信息列表。
        :type ray_cluster_list: list[:class:`huaweicloudsdkaidatalake.v2.RayFederationRayClusterResponse`]
        :param create_time: **参数解释**：创建时间。使用UTC时间格式，格式为yyyy-MM-ddTHH:mm:ssZ，例如2023-05-30T12:24:30.401Z。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 
        :type create_time: datetime
        :param update_time: **参数解释**：更新时间。使用UTC时间格式，格式为yyyy-MM-ddTHH:mm:ssZ，例如2023-05-30T12:24:30.401Z。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 
        :type update_time: datetime
        :param creator: 
        :type creator: :class:`huaweicloudsdkaidatalake.v2.User`
        """
        
        super().__init__()

        self._id = None
        self._name = None
        self._display_name = None
        self._description = None
        self._status = None
        self._error = None
        self._ray_cluster_list = None
        self._create_time = None
        self._update_time = None
        self._creator = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if display_name is not None:
            self.display_name = display_name
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if error is not None:
            self.error = error
        if ray_cluster_list is not None:
            self.ray_cluster_list = ray_cluster_list
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if creator is not None:
            self.creator = creator

    @property
    def id(self):
        r"""Gets the id of this CreateFederationResponse.

        **参数解释**：Ray联邦端点ID。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。

        :return: The id of this CreateFederationResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateFederationResponse.

        **参数解释**：Ray联邦端点ID。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。

        :param id: The id of this CreateFederationResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CreateFederationResponse.

        **参数解释**：Ray联邦端点名称。 **取值范围**：支持小写字母、数字、中划线，必须字母开头、字母或数字结尾，长度为1~63个字符。

        :return: The name of this CreateFederationResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateFederationResponse.

        **参数解释**：Ray联邦端点名称。 **取值范围**：支持小写字母、数字、中划线，必须字母开头、字母或数字结尾，长度为1~63个字符。

        :param name: The name of this CreateFederationResponse.
        :type name: str
        """
        self._name = name

    @property
    def display_name(self):
        r"""Gets the display_name of this CreateFederationResponse.

        **参数解释**：Ray联邦端点显示名称。 **取值范围**：长度为1~63个字符，支持字母、数字、中划线、汉字。

        :return: The display_name of this CreateFederationResponse.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this CreateFederationResponse.

        **参数解释**：Ray联邦端点显示名称。 **取值范围**：长度为1~63个字符，支持字母、数字、中划线、汉字。

        :param display_name: The display_name of this CreateFederationResponse.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def description(self):
        r"""Gets the description of this CreateFederationResponse.

        **参数解释**：Ray联邦端点描述。 **取值范围**：不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号、艾特符、井号、百分号、分号、左括号、右括号、竖线、星号、反斜杠。长度为0~1024个字符。

        :return: The description of this CreateFederationResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateFederationResponse.

        **参数解释**：Ray联邦端点描述。 **取值范围**：不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号、艾特符、井号、百分号、分号、左括号、右括号、竖线、星号、反斜杠。长度为0~1024个字符。

        :param description: The description of this CreateFederationResponse.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this CreateFederationResponse.

        **参数解释**：Ray联邦端点状态。 **取值范围**：   - RUNNING：运行中。   - LIMITED_AVAILABLE：部分端点可用。   - FAULT：故障。   - WAITING：等待中。

        :return: The status of this CreateFederationResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateFederationResponse.

        **参数解释**：Ray联邦端点状态。 **取值范围**：   - RUNNING：运行中。   - LIMITED_AVAILABLE：部分端点可用。   - FAULT：故障。   - WAITING：等待中。

        :param status: The status of this CreateFederationResponse.
        :type status: str
        """
        self._status = status

    @property
    def error(self):
        r"""Gets the error of this CreateFederationResponse.

        :return: The error of this CreateFederationResponse.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ErrorMessage`
        """
        return self._error

    @error.setter
    def error(self, error):
        r"""Sets the error of this CreateFederationResponse.

        :param error: The error of this CreateFederationResponse.
        :type error: :class:`huaweicloudsdkaidatalake.v2.ErrorMessage`
        """
        self._error = error

    @property
    def ray_cluster_list(self):
        r"""Gets the ray_cluster_list of this CreateFederationResponse.

        **参数解释**：RayCluster端点信息列表。

        :return: The ray_cluster_list of this CreateFederationResponse.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.RayFederationRayClusterResponse`]
        """
        return self._ray_cluster_list

    @ray_cluster_list.setter
    def ray_cluster_list(self, ray_cluster_list):
        r"""Sets the ray_cluster_list of this CreateFederationResponse.

        **参数解释**：RayCluster端点信息列表。

        :param ray_cluster_list: The ray_cluster_list of this CreateFederationResponse.
        :type ray_cluster_list: list[:class:`huaweicloudsdkaidatalake.v2.RayFederationRayClusterResponse`]
        """
        self._ray_cluster_list = ray_cluster_list

    @property
    def create_time(self):
        r"""Gets the create_time of this CreateFederationResponse.

        **参数解释**：创建时间。使用UTC时间格式，格式为yyyy-MM-ddTHH:mm:ssZ，例如2023-05-30T12:24:30.401Z。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :return: The create_time of this CreateFederationResponse.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CreateFederationResponse.

        **参数解释**：创建时间。使用UTC时间格式，格式为yyyy-MM-ddTHH:mm:ssZ，例如2023-05-30T12:24:30.401Z。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :param create_time: The create_time of this CreateFederationResponse.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this CreateFederationResponse.

        **参数解释**：更新时间。使用UTC时间格式，格式为yyyy-MM-ddTHH:mm:ssZ，例如2023-05-30T12:24:30.401Z。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :return: The update_time of this CreateFederationResponse.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this CreateFederationResponse.

        **参数解释**：更新时间。使用UTC时间格式，格式为yyyy-MM-ddTHH:mm:ssZ，例如2023-05-30T12:24:30.401Z。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :param update_time: The update_time of this CreateFederationResponse.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def creator(self):
        r"""Gets the creator of this CreateFederationResponse.

        :return: The creator of this CreateFederationResponse.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.User`
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this CreateFederationResponse.

        :param creator: The creator of this CreateFederationResponse.
        :type creator: :class:`huaweicloudsdkaidatalake.v2.User`
        """
        self._creator = creator

    def to_dict(self):
        import warnings
        warnings.warn("CreateFederationResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateFederationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
