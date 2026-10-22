# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteAiAppRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_id': 'str',
        'keep_policy': 'bool'
    }

    attribute_map = {
        'app_id': 'app_id',
        'keep_policy': 'keep_policy'
    }

    def __init__(self, app_id=None, keep_policy=None):
        r"""DeleteAiAppRequest

        The model defined in huaweicloud sdk

        :param app_id: **参数解释：** AI应用ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type app_id: str
        :param keep_policy: **参数解释：** 是否保留关联的策略 **约束限制：** 不涉及 **取值范围：** true, false **默认取值：** 不涉及
        :type keep_policy: bool
        """
        
        

        self._app_id = None
        self._keep_policy = None
        self.discriminator = None

        self.app_id = app_id
        self.keep_policy = keep_policy

    @property
    def app_id(self):
        r"""Gets the app_id of this DeleteAiAppRequest.

        **参数解释：** AI应用ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The app_id of this DeleteAiAppRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this DeleteAiAppRequest.

        **参数解释：** AI应用ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param app_id: The app_id of this DeleteAiAppRequest.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def keep_policy(self):
        r"""Gets the keep_policy of this DeleteAiAppRequest.

        **参数解释：** 是否保留关联的策略 **约束限制：** 不涉及 **取值范围：** true, false **默认取值：** 不涉及

        :return: The keep_policy of this DeleteAiAppRequest.
        :rtype: bool
        """
        return self._keep_policy

    @keep_policy.setter
    def keep_policy(self, keep_policy):
        r"""Sets the keep_policy of this DeleteAiAppRequest.

        **参数解释：** 是否保留关联的策略 **约束限制：** 不涉及 **取值范围：** true, false **默认取值：** 不涉及

        :param keep_policy: The keep_policy of this DeleteAiAppRequest.
        :type keep_policy: bool
        """
        self._keep_policy = keep_policy

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
        if not isinstance(other, DeleteAiAppRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
