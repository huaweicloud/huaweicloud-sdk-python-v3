# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RegisterDbUserResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_user_id': 'str'
    }

    attribute_map = {
        'db_user_id': 'db_user_id'
    }

    def __init__(self, db_user_id=None):
        r"""RegisterDbUserResponse

        The model defined in huaweicloud sdk

        :param db_user_id: 数据库用户ID
        :type db_user_id: str
        """
        
        super(RegisterDbUserResponse, self).__init__()

        self._db_user_id = None
        self.discriminator = None

        if db_user_id is not None:
            self.db_user_id = db_user_id

    @property
    def db_user_id(self):
        r"""Gets the db_user_id of this RegisterDbUserResponse.

        数据库用户ID

        :return: The db_user_id of this RegisterDbUserResponse.
        :rtype: str
        """
        return self._db_user_id

    @db_user_id.setter
    def db_user_id(self, db_user_id):
        r"""Sets the db_user_id of this RegisterDbUserResponse.

        数据库用户ID

        :param db_user_id: The db_user_id of this RegisterDbUserResponse.
        :type db_user_id: str
        """
        self._db_user_id = db_user_id

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
        if not isinstance(other, RegisterDbUserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
