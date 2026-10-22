# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateBotMTenantPolicyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_tag': 'UserTagDTO',
        'scenario_annotations': 'list[ScenarioAnnotationDTO]'
    }

    attribute_map = {
        'user_tag': 'user_tag',
        'scenario_annotations': 'scenario_annotations'
    }

    def __init__(self, user_tag=None, scenario_annotations=None):
        r"""UpdateBotMTenantPolicyRequestBody

        The model defined in huaweicloud sdk

        :param user_tag: 
        :type user_tag: :class:`huaweicloudsdkwaf.v1.UserTagDTO`
        :param scenario_annotations: 场景标注（登录/注册场景接口的语义标注列表）
        :type scenario_annotations: list[:class:`huaweicloudsdkwaf.v1.ScenarioAnnotationDTO`]
        """
        
        

        self._user_tag = None
        self._scenario_annotations = None
        self.discriminator = None

        if user_tag is not None:
            self.user_tag = user_tag
        if scenario_annotations is not None:
            self.scenario_annotations = scenario_annotations

    @property
    def user_tag(self):
        r"""Gets the user_tag of this UpdateBotMTenantPolicyRequestBody.

        :return: The user_tag of this UpdateBotMTenantPolicyRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.UserTagDTO`
        """
        return self._user_tag

    @user_tag.setter
    def user_tag(self, user_tag):
        r"""Sets the user_tag of this UpdateBotMTenantPolicyRequestBody.

        :param user_tag: The user_tag of this UpdateBotMTenantPolicyRequestBody.
        :type user_tag: :class:`huaweicloudsdkwaf.v1.UserTagDTO`
        """
        self._user_tag = user_tag

    @property
    def scenario_annotations(self):
        r"""Gets the scenario_annotations of this UpdateBotMTenantPolicyRequestBody.

        场景标注（登录/注册场景接口的语义标注列表）

        :return: The scenario_annotations of this UpdateBotMTenantPolicyRequestBody.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.ScenarioAnnotationDTO`]
        """
        return self._scenario_annotations

    @scenario_annotations.setter
    def scenario_annotations(self, scenario_annotations):
        r"""Sets the scenario_annotations of this UpdateBotMTenantPolicyRequestBody.

        场景标注（登录/注册场景接口的语义标注列表）

        :param scenario_annotations: The scenario_annotations of this UpdateBotMTenantPolicyRequestBody.
        :type scenario_annotations: list[:class:`huaweicloudsdkwaf.v1.ScenarioAnnotationDTO`]
        """
        self._scenario_annotations = scenario_annotations

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
        if not isinstance(other, UpdateBotMTenantPolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
