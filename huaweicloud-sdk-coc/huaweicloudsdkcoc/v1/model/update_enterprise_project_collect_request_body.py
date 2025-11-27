# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEnterpriseProjectCollectRequestBody:

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
        'ep_id_list': 'list[str]',
        'user_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'ep_id_list': 'ep_id_list',
        'user_id': 'user_id'
    }

    def __init__(self, id=None, ep_id_list=None, user_id=None):
        r"""UpdateEnterpriseProjectCollectRequestBody

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 唯一标识id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type id: str
        :param ep_id_list: 
        :type ep_id_list: list[str]
        :param user_id: **参数解释：** 用户id。 **取值范围：** 不涉及。
        :type user_id: str
        """
        
        

        self._id = None
        self._ep_id_list = None
        self._user_id = None
        self.discriminator = None

        self.id = id
        self.ep_id_list = ep_id_list
        if user_id is not None:
            self.user_id = user_id

    @property
    def id(self):
        r"""Gets the id of this UpdateEnterpriseProjectCollectRequestBody.

        **参数解释：** 唯一标识id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The id of this UpdateEnterpriseProjectCollectRequestBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateEnterpriseProjectCollectRequestBody.

        **参数解释：** 唯一标识id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param id: The id of this UpdateEnterpriseProjectCollectRequestBody.
        :type id: str
        """
        self._id = id

    @property
    def ep_id_list(self):
        r"""Gets the ep_id_list of this UpdateEnterpriseProjectCollectRequestBody.

        :return: The ep_id_list of this UpdateEnterpriseProjectCollectRequestBody.
        :rtype: list[str]
        """
        return self._ep_id_list

    @ep_id_list.setter
    def ep_id_list(self, ep_id_list):
        r"""Sets the ep_id_list of this UpdateEnterpriseProjectCollectRequestBody.

        :param ep_id_list: The ep_id_list of this UpdateEnterpriseProjectCollectRequestBody.
        :type ep_id_list: list[str]
        """
        self._ep_id_list = ep_id_list

    @property
    def user_id(self):
        r"""Gets the user_id of this UpdateEnterpriseProjectCollectRequestBody.

        **参数解释：** 用户id。 **取值范围：** 不涉及。

        :return: The user_id of this UpdateEnterpriseProjectCollectRequestBody.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this UpdateEnterpriseProjectCollectRequestBody.

        **参数解释：** 用户id。 **取值范围：** 不涉及。

        :param user_id: The user_id of this UpdateEnterpriseProjectCollectRequestBody.
        :type user_id: str
        """
        self._user_id = user_id

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
        if not isinstance(other, UpdateEnterpriseProjectCollectRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
