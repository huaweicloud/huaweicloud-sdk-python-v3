# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateProcessInstanceReqOpinions:

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
        'curr_owner': 'str'
    }

    attribute_map = {
        'user_id': 'user_id',
        'curr_owner': 'curr_owner'
    }

    def __init__(self, user_id=None, curr_owner=None):
        r"""CreateProcessInstanceReqOpinions

        The model defined in huaweicloud sdk

        :param user_id: 用户ID
        :type user_id: str
        :param curr_owner: 当前责任人
        :type curr_owner: str
        """
        
        

        self._user_id = None
        self._curr_owner = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if curr_owner is not None:
            self.curr_owner = curr_owner

    @property
    def user_id(self):
        r"""Gets the user_id of this CreateProcessInstanceReqOpinions.

        用户ID

        :return: The user_id of this CreateProcessInstanceReqOpinions.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this CreateProcessInstanceReqOpinions.

        用户ID

        :param user_id: The user_id of this CreateProcessInstanceReqOpinions.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def curr_owner(self):
        r"""Gets the curr_owner of this CreateProcessInstanceReqOpinions.

        当前责任人

        :return: The curr_owner of this CreateProcessInstanceReqOpinions.
        :rtype: str
        """
        return self._curr_owner

    @curr_owner.setter
    def curr_owner(self, curr_owner):
        r"""Sets the curr_owner of this CreateProcessInstanceReqOpinions.

        当前责任人

        :param curr_owner: The curr_owner of this CreateProcessInstanceReqOpinions.
        :type curr_owner: str
        """
        self._curr_owner = curr_owner

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
        if not isinstance(other, CreateProcessInstanceReqOpinions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
