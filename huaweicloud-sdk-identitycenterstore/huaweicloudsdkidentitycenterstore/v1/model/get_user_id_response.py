# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetUserIdResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'identity_store_id': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'identity_store_id': 'identity_store_id',
        'user_id': 'user_id'
    }

    def __init__(self, identity_store_id=None, user_id=None):
        """GetUserIdResponse

        The model defined in huaweicloud sdk

        :param identity_store_id: 身份源的全局唯一标识符（ID）
        :type identity_store_id: str
        :param user_id: 身份源中IAM身份中心用户的全局唯一标识符（ID）
        :type user_id: str
        """
        
        super(GetUserIdResponse, self).__init__()

        self._identity_store_id = None
        self._user_id = None
        self.discriminator = None

        if identity_store_id is not None:
            self.identity_store_id = identity_store_id
        if user_id is not None:
            self.user_id = user_id

    @property
    def identity_store_id(self):
        """Gets the identity_store_id of this GetUserIdResponse.

        身份源的全局唯一标识符（ID）

        :return: The identity_store_id of this GetUserIdResponse.
        :rtype: str
        """
        return self._identity_store_id

    @identity_store_id.setter
    def identity_store_id(self, identity_store_id):
        """Sets the identity_store_id of this GetUserIdResponse.

        身份源的全局唯一标识符（ID）

        :param identity_store_id: The identity_store_id of this GetUserIdResponse.
        :type identity_store_id: str
        """
        self._identity_store_id = identity_store_id

    @property
    def user_id(self):
        """Gets the user_id of this GetUserIdResponse.

        身份源中IAM身份中心用户的全局唯一标识符（ID）

        :return: The user_id of this GetUserIdResponse.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this GetUserIdResponse.

        身份源中IAM身份中心用户的全局唯一标识符（ID）

        :param user_id: The user_id of this GetUserIdResponse.
        :type user_id: str
        """
        self._user_id = user_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GetUserIdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
