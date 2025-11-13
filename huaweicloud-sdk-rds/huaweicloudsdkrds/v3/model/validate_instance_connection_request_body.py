# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValidateInstanceConnectionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_instance_id': 'str',
        'user_info': 'ValidateConnectionUserInfo'
    }

    attribute_map = {
        'target_instance_id': 'target_instance_id',
        'user_info': 'user_info'
    }

    def __init__(self, target_instance_id=None, user_info=None):
        r"""ValidateInstanceConnectionRequestBody

        The model defined in huaweicloud sdk

        :param target_instance_id: 连接目标实例id
        :type target_instance_id: str
        :param user_info: 
        :type user_info: :class:`huaweicloudsdkrds.v3.ValidateConnectionUserInfo`
        """
        
        

        self._target_instance_id = None
        self._user_info = None
        self.discriminator = None

        if target_instance_id is not None:
            self.target_instance_id = target_instance_id
        if user_info is not None:
            self.user_info = user_info

    @property
    def target_instance_id(self):
        r"""Gets the target_instance_id of this ValidateInstanceConnectionRequestBody.

        连接目标实例id

        :return: The target_instance_id of this ValidateInstanceConnectionRequestBody.
        :rtype: str
        """
        return self._target_instance_id

    @target_instance_id.setter
    def target_instance_id(self, target_instance_id):
        r"""Sets the target_instance_id of this ValidateInstanceConnectionRequestBody.

        连接目标实例id

        :param target_instance_id: The target_instance_id of this ValidateInstanceConnectionRequestBody.
        :type target_instance_id: str
        """
        self._target_instance_id = target_instance_id

    @property
    def user_info(self):
        r"""Gets the user_info of this ValidateInstanceConnectionRequestBody.

        :return: The user_info of this ValidateInstanceConnectionRequestBody.
        :rtype: :class:`huaweicloudsdkrds.v3.ValidateConnectionUserInfo`
        """
        return self._user_info

    @user_info.setter
    def user_info(self, user_info):
        r"""Sets the user_info of this ValidateInstanceConnectionRequestBody.

        :param user_info: The user_info of this ValidateInstanceConnectionRequestBody.
        :type user_info: :class:`huaweicloudsdkrds.v3.ValidateConnectionUserInfo`
        """
        self._user_info = user_info

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
        if not isinstance(other, ValidateInstanceConnectionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
