# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateProjectProtectedTagsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'actions': 'list[ProjectProtectedTagActionDto]'
    }

    attribute_map = {
        'name': 'name',
        'actions': 'actions'
    }

    def __init__(self, name=None, actions=None):
        r"""CreateProjectProtectedTagsResponse

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 保护tag名称。 **取值范围** 字符串长度不少于1，不超过1000。
        :type name: str
        :param actions: **参数解释：** 事件列表。
        :type actions: list[:class:`huaweicloudsdkcodeartsrepo.v4.ProjectProtectedTagActionDto`]
        """
        
        super().__init__()

        self._name = None
        self._actions = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if actions is not None:
            self.actions = actions

    @property
    def name(self):
        r"""Gets the name of this CreateProjectProtectedTagsResponse.

        **参数解释：** 保护tag名称。 **取值范围** 字符串长度不少于1，不超过1000。

        :return: The name of this CreateProjectProtectedTagsResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateProjectProtectedTagsResponse.

        **参数解释：** 保护tag名称。 **取值范围** 字符串长度不少于1，不超过1000。

        :param name: The name of this CreateProjectProtectedTagsResponse.
        :type name: str
        """
        self._name = name

    @property
    def actions(self):
        r"""Gets the actions of this CreateProjectProtectedTagsResponse.

        **参数解释：** 事件列表。

        :return: The actions of this CreateProjectProtectedTagsResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartsrepo.v4.ProjectProtectedTagActionDto`]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this CreateProjectProtectedTagsResponse.

        **参数解释：** 事件列表。

        :param actions: The actions of this CreateProjectProtectedTagsResponse.
        :type actions: list[:class:`huaweicloudsdkcodeartsrepo.v4.ProjectProtectedTagActionDto`]
        """
        self._actions = actions

    def to_dict(self):
        import warnings
        warnings.warn("CreateProjectProtectedTagsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateProjectProtectedTagsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
