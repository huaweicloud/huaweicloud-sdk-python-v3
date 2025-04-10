# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Review:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'charger': 'str',
        'create_time': 'str',
        'creator': 'str',
        'deleted': 'str',
        'description': 'str',
        'id': 'str',
        'mindmap_id': 'str',
        'node_id': 'str',
        'node_value': 'str',
        'status': 'str',
        'type': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'charger': 'charger',
        'create_time': 'create_time',
        'creator': 'creator',
        'deleted': 'deleted',
        'description': 'description',
        'id': 'id',
        'mindmap_id': 'mindmap_id',
        'node_id': 'node_id',
        'node_value': 'node_value',
        'status': 'status',
        'type': 'type',
        'update_time': 'update_time'
    }

    def __init__(self, charger=None, create_time=None, creator=None, deleted=None, description=None, id=None, mindmap_id=None, node_id=None, node_value=None, status=None, type=None, update_time=None):
        r"""Review

        The model defined in huaweicloud sdk

        :param charger: 名称
        :type charger: str
        :param create_time: 创建时间
        :type create_time: str
        :param creator: 创建人
        :type creator: str
        :param deleted: 是否删除
        :type deleted: str
        :param description: 描述
        :type description: str
        :param id: id 主键
        :type id: str
        :param mindmap_id: 脑图id
        :type mindmap_id: str
        :param node_id: 节点id
        :type node_id: str
        :param node_value: 节点值
        :type node_value: str
        :param status: 状态
        :type status: str
        :param type: 类型
        :type type: str
        :param update_time: 更新时间
        :type update_time: str
        """
        
        

        self._charger = None
        self._create_time = None
        self._creator = None
        self._deleted = None
        self._description = None
        self._id = None
        self._mindmap_id = None
        self._node_id = None
        self._node_value = None
        self._status = None
        self._type = None
        self._update_time = None
        self.discriminator = None

        if charger is not None:
            self.charger = charger
        if create_time is not None:
            self.create_time = create_time
        if creator is not None:
            self.creator = creator
        if deleted is not None:
            self.deleted = deleted
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if mindmap_id is not None:
            self.mindmap_id = mindmap_id
        if node_id is not None:
            self.node_id = node_id
        if node_value is not None:
            self.node_value = node_value
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if update_time is not None:
            self.update_time = update_time

    @property
    def charger(self):
        r"""Gets the charger of this Review.

        名称

        :return: The charger of this Review.
        :rtype: str
        """
        return self._charger

    @charger.setter
    def charger(self, charger):
        r"""Sets the charger of this Review.

        名称

        :param charger: The charger of this Review.
        :type charger: str
        """
        self._charger = charger

    @property
    def create_time(self):
        r"""Gets the create_time of this Review.

        创建时间

        :return: The create_time of this Review.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this Review.

        创建时间

        :param create_time: The create_time of this Review.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def creator(self):
        r"""Gets the creator of this Review.

        创建人

        :return: The creator of this Review.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this Review.

        创建人

        :param creator: The creator of this Review.
        :type creator: str
        """
        self._creator = creator

    @property
    def deleted(self):
        r"""Gets the deleted of this Review.

        是否删除

        :return: The deleted of this Review.
        :rtype: str
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        r"""Sets the deleted of this Review.

        是否删除

        :param deleted: The deleted of this Review.
        :type deleted: str
        """
        self._deleted = deleted

    @property
    def description(self):
        r"""Gets the description of this Review.

        描述

        :return: The description of this Review.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Review.

        描述

        :param description: The description of this Review.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        r"""Gets the id of this Review.

        id 主键

        :return: The id of this Review.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Review.

        id 主键

        :param id: The id of this Review.
        :type id: str
        """
        self._id = id

    @property
    def mindmap_id(self):
        r"""Gets the mindmap_id of this Review.

        脑图id

        :return: The mindmap_id of this Review.
        :rtype: str
        """
        return self._mindmap_id

    @mindmap_id.setter
    def mindmap_id(self, mindmap_id):
        r"""Sets the mindmap_id of this Review.

        脑图id

        :param mindmap_id: The mindmap_id of this Review.
        :type mindmap_id: str
        """
        self._mindmap_id = mindmap_id

    @property
    def node_id(self):
        r"""Gets the node_id of this Review.

        节点id

        :return: The node_id of this Review.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this Review.

        节点id

        :param node_id: The node_id of this Review.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def node_value(self):
        r"""Gets the node_value of this Review.

        节点值

        :return: The node_value of this Review.
        :rtype: str
        """
        return self._node_value

    @node_value.setter
    def node_value(self, node_value):
        r"""Sets the node_value of this Review.

        节点值

        :param node_value: The node_value of this Review.
        :type node_value: str
        """
        self._node_value = node_value

    @property
    def status(self):
        r"""Gets the status of this Review.

        状态

        :return: The status of this Review.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Review.

        状态

        :param status: The status of this Review.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        r"""Gets the type of this Review.

        类型

        :return: The type of this Review.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Review.

        类型

        :param type: The type of this Review.
        :type type: str
        """
        self._type = type

    @property
    def update_time(self):
        r"""Gets the update_time of this Review.

        更新时间

        :return: The update_time of this Review.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this Review.

        更新时间

        :param update_time: The update_time of this Review.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, Review):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
