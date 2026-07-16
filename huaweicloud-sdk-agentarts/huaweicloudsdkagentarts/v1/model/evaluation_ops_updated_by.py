# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EvaluationOpsUpdatedBy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_id': 'str',
        'name': 'str',
        'avatar_url': 'str'
    }

    attribute_map = {
        'user_id': 'user_id',
        'name': 'name',
        'avatar_url': 'avatar_url'
    }

    def __init__(self, user_id=None, name=None, avatar_url=None):
        r"""EvaluationOpsUpdatedBy

        The model defined in huaweicloud sdk

        :param user_id: **参数解释：** 最后一次更新资源的用户的ID。 
        :type user_id: str
        :param name: **参数解释：** 更新者的显示名称。 
        :type name: str
        :param avatar_url: **参数解释：** 更新者的头像链接。 
        :type avatar_url: str
        """
        
        

        self._user_id = None
        self._name = None
        self._avatar_url = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if name is not None:
            self.name = name
        if avatar_url is not None:
            self.avatar_url = avatar_url

    @property
    def user_id(self):
        r"""Gets the user_id of this EvaluationOpsUpdatedBy.

        **参数解释：** 最后一次更新资源的用户的ID。 

        :return: The user_id of this EvaluationOpsUpdatedBy.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this EvaluationOpsUpdatedBy.

        **参数解释：** 最后一次更新资源的用户的ID。 

        :param user_id: The user_id of this EvaluationOpsUpdatedBy.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def name(self):
        r"""Gets the name of this EvaluationOpsUpdatedBy.

        **参数解释：** 更新者的显示名称。 

        :return: The name of this EvaluationOpsUpdatedBy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EvaluationOpsUpdatedBy.

        **参数解释：** 更新者的显示名称。 

        :param name: The name of this EvaluationOpsUpdatedBy.
        :type name: str
        """
        self._name = name

    @property
    def avatar_url(self):
        r"""Gets the avatar_url of this EvaluationOpsUpdatedBy.

        **参数解释：** 更新者的头像链接。 

        :return: The avatar_url of this EvaluationOpsUpdatedBy.
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        r"""Sets the avatar_url of this EvaluationOpsUpdatedBy.

        **参数解释：** 更新者的头像链接。 

        :param avatar_url: The avatar_url of this EvaluationOpsUpdatedBy.
        :type avatar_url: str
        """
        self._avatar_url = avatar_url

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
        if not isinstance(other, EvaluationOpsUpdatedBy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
