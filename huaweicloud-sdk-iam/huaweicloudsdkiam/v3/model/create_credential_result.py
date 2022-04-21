# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCredentialResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'create_time': 'str',
        'access': 'str',
        'secret': 'str',
        'status': 'str',
        'user_id': 'str',
        'description': 'str'
    }

    attribute_map = {
        'create_time': 'create_time',
        'access': 'access',
        'secret': 'secret',
        'status': 'status',
        'user_id': 'user_id',
        'description': 'description'
    }

    def __init__(self, create_time=None, access=None, secret=None, status=None, user_id=None, description=None):
        """CreateCredentialResult

        The model defined in huaweicloud sdk

        :param create_time: 创建访问密钥时间。
        :type create_time: str
        :param access: 创建的AK。
        :type access: str
        :param secret: 创建的SK。
        :type secret: str
        :param status: 访问密钥状态。
        :type status: str
        :param user_id: IAM用户ID。
        :type user_id: str
        :param description: 访问密钥描述信息。
        :type description: str
        """
        
        

        self._create_time = None
        self._access = None
        self._secret = None
        self._status = None
        self._user_id = None
        self._description = None
        self.discriminator = None

        self.create_time = create_time
        self.access = access
        self.secret = secret
        self.status = status
        self.user_id = user_id
        self.description = description

    @property
    def create_time(self):
        """Gets the create_time of this CreateCredentialResult.

        创建访问密钥时间。

        :return: The create_time of this CreateCredentialResult.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CreateCredentialResult.

        创建访问密钥时间。

        :param create_time: The create_time of this CreateCredentialResult.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def access(self):
        """Gets the access of this CreateCredentialResult.

        创建的AK。

        :return: The access of this CreateCredentialResult.
        :rtype: str
        """
        return self._access

    @access.setter
    def access(self, access):
        """Sets the access of this CreateCredentialResult.

        创建的AK。

        :param access: The access of this CreateCredentialResult.
        :type access: str
        """
        self._access = access

    @property
    def secret(self):
        """Gets the secret of this CreateCredentialResult.

        创建的SK。

        :return: The secret of this CreateCredentialResult.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this CreateCredentialResult.

        创建的SK。

        :param secret: The secret of this CreateCredentialResult.
        :type secret: str
        """
        self._secret = secret

    @property
    def status(self):
        """Gets the status of this CreateCredentialResult.

        访问密钥状态。

        :return: The status of this CreateCredentialResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateCredentialResult.

        访问密钥状态。

        :param status: The status of this CreateCredentialResult.
        :type status: str
        """
        self._status = status

    @property
    def user_id(self):
        """Gets the user_id of this CreateCredentialResult.

        IAM用户ID。

        :return: The user_id of this CreateCredentialResult.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this CreateCredentialResult.

        IAM用户ID。

        :param user_id: The user_id of this CreateCredentialResult.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def description(self):
        """Gets the description of this CreateCredentialResult.

        访问密钥描述信息。

        :return: The description of this CreateCredentialResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateCredentialResult.

        访问密钥描述信息。

        :param description: The description of this CreateCredentialResult.
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
        if not isinstance(other, CreateCredentialResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
