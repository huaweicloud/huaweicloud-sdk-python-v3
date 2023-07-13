# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Path:

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
        'status': 'str',
        'agent_id': 'str',
        'dir_path': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'agent_id': 'agent_id',
        'dir_path': 'dir_path'
    }

    def __init__(self, id=None, status=None, agent_id=None, dir_path=None):
        """Path

        The model defined in huaweicloud sdk

        :param id: 路径ID
        :type id: str
        :param status: 路径状态，有available和remove两种状态
        :type status: str
        :param agent_id: 该路径所属于的客户端ID
        :type agent_id: str
        :param dir_path: 路径详情
        :type dir_path: str
        """
        
        

        self._id = None
        self._status = None
        self._agent_id = None
        self._dir_path = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if agent_id is not None:
            self.agent_id = agent_id
        if dir_path is not None:
            self.dir_path = dir_path

    @property
    def id(self):
        """Gets the id of this Path.

        路径ID

        :return: The id of this Path.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Path.

        路径ID

        :param id: The id of this Path.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this Path.

        路径状态，有available和remove两种状态

        :return: The status of this Path.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Path.

        路径状态，有available和remove两种状态

        :param status: The status of this Path.
        :type status: str
        """
        self._status = status

    @property
    def agent_id(self):
        """Gets the agent_id of this Path.

        该路径所属于的客户端ID

        :return: The agent_id of this Path.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this Path.

        该路径所属于的客户端ID

        :param agent_id: The agent_id of this Path.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def dir_path(self):
        """Gets the dir_path of this Path.

        路径详情

        :return: The dir_path of this Path.
        :rtype: str
        """
        return self._dir_path

    @dir_path.setter
    def dir_path(self, dir_path):
        """Sets the dir_path of this Path.

        路径详情

        :param dir_path: The dir_path of this Path.
        :type dir_path: str
        """
        self._dir_path = dir_path

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
        if not isinstance(other, Path):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
