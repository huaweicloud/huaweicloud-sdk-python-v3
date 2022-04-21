# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCredentialResult:

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
        'access': 'str',
        'status': 'str',
        'create_time': 'str',
        'description': 'str'
    }

    attribute_map = {
        'user_id': 'user_id',
        'access': 'access',
        'status': 'status',
        'create_time': 'create_time',
        'description': 'description'
    }

    def __init__(self, user_id=None, access=None, status=None, create_time=None, description=None):
        """UpdateCredentialResult

        The model defined in huaweicloud sdk

        :param user_id: IAM用户ID。
        :type user_id: str
        :param access: 修改的AK。
        :type access: str
        :param status: 访问密钥状态。
        :type status: str
        :param create_time: 访问密钥创建时间。
        :type create_time: str
        :param description: 访问密钥描述信息。
        :type description: str
        """
        
        

        self._user_id = None
        self._access = None
        self._status = None
        self._create_time = None
        self._description = None
        self.discriminator = None

        self.user_id = user_id
        self.access = access
        self.status = status
        self.create_time = create_time
        self.description = description

    @property
    def user_id(self):
        """Gets the user_id of this UpdateCredentialResult.

        IAM用户ID。

        :return: The user_id of this UpdateCredentialResult.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UpdateCredentialResult.

        IAM用户ID。

        :param user_id: The user_id of this UpdateCredentialResult.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def access(self):
        """Gets the access of this UpdateCredentialResult.

        修改的AK。

        :return: The access of this UpdateCredentialResult.
        :rtype: str
        """
        return self._access

    @access.setter
    def access(self, access):
        """Sets the access of this UpdateCredentialResult.

        修改的AK。

        :param access: The access of this UpdateCredentialResult.
        :type access: str
        """
        self._access = access

    @property
    def status(self):
        """Gets the status of this UpdateCredentialResult.

        访问密钥状态。

        :return: The status of this UpdateCredentialResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateCredentialResult.

        访问密钥状态。

        :param status: The status of this UpdateCredentialResult.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this UpdateCredentialResult.

        访问密钥创建时间。

        :return: The create_time of this UpdateCredentialResult.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this UpdateCredentialResult.

        访问密钥创建时间。

        :param create_time: The create_time of this UpdateCredentialResult.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def description(self):
        """Gets the description of this UpdateCredentialResult.

        访问密钥描述信息。

        :return: The description of this UpdateCredentialResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateCredentialResult.

        访问密钥描述信息。

        :param description: The description of this UpdateCredentialResult.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, UpdateCredentialResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
