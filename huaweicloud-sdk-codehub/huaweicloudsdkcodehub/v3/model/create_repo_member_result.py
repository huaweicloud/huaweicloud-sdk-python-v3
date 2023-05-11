# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRepoMemberResult:

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
        'message': 'str',
        'name': 'str',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'message': 'message',
        'name': 'name',
        'status': 'status'
    }

    def __init__(self, id=None, message=None, name=None, status=None):
        """CreateRepoMemberResult

        The model defined in huaweicloud sdk

        :param id: 用户id
        :type id: str
        :param message: 创建仓库成员信息
        :type message: str
        :param name: 用户名
        :type name: str
        :param status: 创建仓库成员状态
        :type status: str
        """
        
        

        self._id = None
        self._message = None
        self._name = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if message is not None:
            self.message = message
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this CreateRepoMemberResult.

        用户id

        :return: The id of this CreateRepoMemberResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateRepoMemberResult.

        用户id

        :param id: The id of this CreateRepoMemberResult.
        :type id: str
        """
        self._id = id

    @property
    def message(self):
        """Gets the message of this CreateRepoMemberResult.

        创建仓库成员信息

        :return: The message of this CreateRepoMemberResult.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CreateRepoMemberResult.

        创建仓库成员信息

        :param message: The message of this CreateRepoMemberResult.
        :type message: str
        """
        self._message = message

    @property
    def name(self):
        """Gets the name of this CreateRepoMemberResult.

        用户名

        :return: The name of this CreateRepoMemberResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateRepoMemberResult.

        用户名

        :param name: The name of this CreateRepoMemberResult.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this CreateRepoMemberResult.

        创建仓库成员状态

        :return: The status of this CreateRepoMemberResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateRepoMemberResult.

        创建仓库成员状态

        :param status: The status of this CreateRepoMemberResult.
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
        if not isinstance(other, CreateRepoMemberResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
