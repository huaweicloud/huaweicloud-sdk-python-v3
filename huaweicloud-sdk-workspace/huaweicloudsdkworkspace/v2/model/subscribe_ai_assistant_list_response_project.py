# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubscribeAiAssistantListResponseProject:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'ai_func': 'bool'
    }

    attribute_map = {
        'project_id': 'project_id',
        'ai_func': 'ai_func'
    }

    def __init__(self, project_id=None, ai_func=None):
        r"""SubscribeAiAssistantListResponseProject

        The model defined in huaweicloud sdk

        :param project_id: 项目ID。
        :type project_id: str
        :param ai_func: ai 功能是否启用。 * true： 启用 * false： 不启用
        :type ai_func: bool
        """
        
        

        self._project_id = None
        self._ai_func = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if ai_func is not None:
            self.ai_func = ai_func

    @property
    def project_id(self):
        r"""Gets the project_id of this SubscribeAiAssistantListResponseProject.

        项目ID。

        :return: The project_id of this SubscribeAiAssistantListResponseProject.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this SubscribeAiAssistantListResponseProject.

        项目ID。

        :param project_id: The project_id of this SubscribeAiAssistantListResponseProject.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def ai_func(self):
        r"""Gets the ai_func of this SubscribeAiAssistantListResponseProject.

        ai 功能是否启用。 * true： 启用 * false： 不启用

        :return: The ai_func of this SubscribeAiAssistantListResponseProject.
        :rtype: bool
        """
        return self._ai_func

    @ai_func.setter
    def ai_func(self, ai_func):
        r"""Sets the ai_func of this SubscribeAiAssistantListResponseProject.

        ai 功能是否启用。 * true： 启用 * false： 不启用

        :param ai_func: The ai_func of this SubscribeAiAssistantListResponseProject.
        :type ai_func: bool
        """
        self._ai_func = ai_func

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
        if not isinstance(other, SubscribeAiAssistantListResponseProject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
