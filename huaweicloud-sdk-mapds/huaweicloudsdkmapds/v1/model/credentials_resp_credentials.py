# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CredentialsRespCredentials:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uuid': 'str',
        'key': 'str',
        'create_time': 'str',
        'description': 'str',
        'status': 'str'
    }

    attribute_map = {
        'uuid': 'uuid',
        'key': 'key',
        'create_time': 'create_time',
        'description': 'description',
        'status': 'status'
    }

    def __init__(self, uuid=None, key=None, create_time=None, description=None, status=None):
        """CredentialsRespCredentials

        The model defined in huaweicloud sdk

        :param uuid: 凭证id
        :type uuid: str
        :param key: 凭证value
        :type key: str
        :param create_time: 凭证创建时间
        :type create_time: str
        :param description: 凭证描述
        :type description: str
        :param status: 凭证状态
        :type status: str
        """
        
        

        self._uuid = None
        self._key = None
        self._create_time = None
        self._description = None
        self._status = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if key is not None:
            self.key = key
        if create_time is not None:
            self.create_time = create_time
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status

    @property
    def uuid(self):
        """Gets the uuid of this CredentialsRespCredentials.

        凭证id

        :return: The uuid of this CredentialsRespCredentials.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this CredentialsRespCredentials.

        凭证id

        :param uuid: The uuid of this CredentialsRespCredentials.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def key(self):
        """Gets the key of this CredentialsRespCredentials.

        凭证value

        :return: The key of this CredentialsRespCredentials.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CredentialsRespCredentials.

        凭证value

        :param key: The key of this CredentialsRespCredentials.
        :type key: str
        """
        self._key = key

    @property
    def create_time(self):
        """Gets the create_time of this CredentialsRespCredentials.

        凭证创建时间

        :return: The create_time of this CredentialsRespCredentials.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CredentialsRespCredentials.

        凭证创建时间

        :param create_time: The create_time of this CredentialsRespCredentials.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def description(self):
        """Gets the description of this CredentialsRespCredentials.

        凭证描述

        :return: The description of this CredentialsRespCredentials.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CredentialsRespCredentials.

        凭证描述

        :param description: The description of this CredentialsRespCredentials.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this CredentialsRespCredentials.

        凭证状态

        :return: The status of this CredentialsRespCredentials.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CredentialsRespCredentials.

        凭证状态

        :param status: The status of this CredentialsRespCredentials.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, CredentialsRespCredentials):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
