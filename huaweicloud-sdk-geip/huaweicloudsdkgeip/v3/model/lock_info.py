# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LockInfo:

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
        'resource_type': 'str',
        'resource_id': 'str',
        'scene': 'str',
        'source_type': 'str',
        'source_id': 'str',
        'check_url': 'str',
        'action': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'resource_type': 'resource_type',
        'resource_id': 'resource_id',
        'scene': 'scene',
        'source_type': 'source_type',
        'source_id': 'source_id',
        'check_url': 'check_url',
        'action': 'action',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, resource_type=None, resource_id=None, scene=None, source_type=None, source_id=None, check_url=None, action=None, created_at=None, updated_at=None):
        r"""LockInfo

        The model defined in huaweicloud sdk

        :param id: 锁id
        :type id: str
        :param resource_type: 资源类型
        :type resource_type: str
        :param resource_id: 资源id
        :type resource_id: str
        :param scene: 场景类型
        :type scene: str
        :param source_type: 源类型
        :type source_type: str
        :param source_id: 源id
        :type source_id: str
        :param check_url: check地址
        :type check_url: str
        :param action: 动作类型
        :type action: str
        :param created_at: 创建时间
        :type created_at: datetime
        :param updated_at: 更新时间
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._resource_type = None
        self._resource_id = None
        self._scene = None
        self._source_type = None
        self._source_id = None
        self._check_url = None
        self._action = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_id is not None:
            self.resource_id = resource_id
        if scene is not None:
            self.scene = scene
        if source_type is not None:
            self.source_type = source_type
        if source_id is not None:
            self.source_id = source_id
        if check_url is not None:
            self.check_url = check_url
        if action is not None:
            self.action = action
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this LockInfo.

        锁id

        :return: The id of this LockInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this LockInfo.

        锁id

        :param id: The id of this LockInfo.
        :type id: str
        """
        self._id = id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this LockInfo.

        资源类型

        :return: The resource_type of this LockInfo.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this LockInfo.

        资源类型

        :param resource_type: The resource_type of this LockInfo.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_id(self):
        r"""Gets the resource_id of this LockInfo.

        资源id

        :return: The resource_id of this LockInfo.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this LockInfo.

        资源id

        :param resource_id: The resource_id of this LockInfo.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def scene(self):
        r"""Gets the scene of this LockInfo.

        场景类型

        :return: The scene of this LockInfo.
        :rtype: str
        """
        return self._scene

    @scene.setter
    def scene(self, scene):
        r"""Sets the scene of this LockInfo.

        场景类型

        :param scene: The scene of this LockInfo.
        :type scene: str
        """
        self._scene = scene

    @property
    def source_type(self):
        r"""Gets the source_type of this LockInfo.

        源类型

        :return: The source_type of this LockInfo.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        r"""Sets the source_type of this LockInfo.

        源类型

        :param source_type: The source_type of this LockInfo.
        :type source_type: str
        """
        self._source_type = source_type

    @property
    def source_id(self):
        r"""Gets the source_id of this LockInfo.

        源id

        :return: The source_id of this LockInfo.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        r"""Sets the source_id of this LockInfo.

        源id

        :param source_id: The source_id of this LockInfo.
        :type source_id: str
        """
        self._source_id = source_id

    @property
    def check_url(self):
        r"""Gets the check_url of this LockInfo.

        check地址

        :return: The check_url of this LockInfo.
        :rtype: str
        """
        return self._check_url

    @check_url.setter
    def check_url(self, check_url):
        r"""Sets the check_url of this LockInfo.

        check地址

        :param check_url: The check_url of this LockInfo.
        :type check_url: str
        """
        self._check_url = check_url

    @property
    def action(self):
        r"""Gets the action of this LockInfo.

        动作类型

        :return: The action of this LockInfo.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this LockInfo.

        动作类型

        :param action: The action of this LockInfo.
        :type action: str
        """
        self._action = action

    @property
    def created_at(self):
        r"""Gets the created_at of this LockInfo.

        创建时间

        :return: The created_at of this LockInfo.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this LockInfo.

        创建时间

        :param created_at: The created_at of this LockInfo.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this LockInfo.

        更新时间

        :return: The updated_at of this LockInfo.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this LockInfo.

        更新时间

        :param updated_at: The updated_at of this LockInfo.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, LockInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
