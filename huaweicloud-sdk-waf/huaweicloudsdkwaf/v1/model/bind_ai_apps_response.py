# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BindAiAppsResponse(SdkResponse):

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
        'bind_ai_apps': 'list[AiAppBasicInfo]',
        'create_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'bind_ai_apps': 'bind_ai_apps',
        'create_time': 'create_time'
    }

    def __init__(self, id=None, name=None, bind_ai_apps=None, create_time=None):
        r"""BindAiAppsResponse

        The model defined in huaweicloud sdk

        :param id: 策略 ID
        :type id: str
        :param name: 策略名称
        :type name: str
        :param bind_ai_apps: 绑定的 AI 应用列表
        :type bind_ai_apps: list[:class:`huaweicloudsdkwaf.v1.AiAppBasicInfo`]
        :param create_time: 创建时间
        :type create_time: int
        """
        
        super().__init__()

        self._id = None
        self._name = None
        self._bind_ai_apps = None
        self._create_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if bind_ai_apps is not None:
            self.bind_ai_apps = bind_ai_apps
        if create_time is not None:
            self.create_time = create_time

    @property
    def id(self):
        r"""Gets the id of this BindAiAppsResponse.

        策略 ID

        :return: The id of this BindAiAppsResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BindAiAppsResponse.

        策略 ID

        :param id: The id of this BindAiAppsResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this BindAiAppsResponse.

        策略名称

        :return: The name of this BindAiAppsResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BindAiAppsResponse.

        策略名称

        :param name: The name of this BindAiAppsResponse.
        :type name: str
        """
        self._name = name

    @property
    def bind_ai_apps(self):
        r"""Gets the bind_ai_apps of this BindAiAppsResponse.

        绑定的 AI 应用列表

        :return: The bind_ai_apps of this BindAiAppsResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.AiAppBasicInfo`]
        """
        return self._bind_ai_apps

    @bind_ai_apps.setter
    def bind_ai_apps(self, bind_ai_apps):
        r"""Sets the bind_ai_apps of this BindAiAppsResponse.

        绑定的 AI 应用列表

        :param bind_ai_apps: The bind_ai_apps of this BindAiAppsResponse.
        :type bind_ai_apps: list[:class:`huaweicloudsdkwaf.v1.AiAppBasicInfo`]
        """
        self._bind_ai_apps = bind_ai_apps

    @property
    def create_time(self):
        r"""Gets the create_time of this BindAiAppsResponse.

        创建时间

        :return: The create_time of this BindAiAppsResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this BindAiAppsResponse.

        创建时间

        :param create_time: The create_time of this BindAiAppsResponse.
        :type create_time: int
        """
        self._create_time = create_time

    def to_dict(self):
        import warnings
        warnings.warn("BindAiAppsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, BindAiAppsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
