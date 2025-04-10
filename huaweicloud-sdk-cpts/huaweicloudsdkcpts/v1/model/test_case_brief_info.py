# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TestCaseBriefInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'name': 'str',
        'status': 'int',
        'create_time': 'str',
        'update_time': 'str',
        'parent_id': 'int',
        'type': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'parent_id': 'parent_id',
        'type': 'type'
    }

    def __init__(self, id=None, name=None, status=None, create_time=None, update_time=None, parent_id=None, type=None):
        r"""TestCaseBriefInfo

        The model defined in huaweicloud sdk

        :param id: 用例id
        :type id: int
        :param name: 用例名称
        :type name: str
        :param status: 状态（0-已删除；1-启用；2-停用；）
        :type status: int
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 更新时间
        :type update_time: str
        :param parent_id: 所属目录id
        :type parent_id: int
        :param type: 类型（1-目录；2-用例；）
        :type type: int
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._create_time = None
        self._update_time = None
        self._parent_id = None
        self._type = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.status = status
        self.create_time = create_time
        self.update_time = update_time
        self.parent_id = parent_id
        self.type = type

    @property
    def id(self):
        r"""Gets the id of this TestCaseBriefInfo.

        用例id

        :return: The id of this TestCaseBriefInfo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TestCaseBriefInfo.

        用例id

        :param id: The id of this TestCaseBriefInfo.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this TestCaseBriefInfo.

        用例名称

        :return: The name of this TestCaseBriefInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TestCaseBriefInfo.

        用例名称

        :param name: The name of this TestCaseBriefInfo.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this TestCaseBriefInfo.

        状态（0-已删除；1-启用；2-停用；）

        :return: The status of this TestCaseBriefInfo.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this TestCaseBriefInfo.

        状态（0-已删除；1-启用；2-停用；）

        :param status: The status of this TestCaseBriefInfo.
        :type status: int
        """
        self._status = status

    @property
    def create_time(self):
        r"""Gets the create_time of this TestCaseBriefInfo.

        创建时间

        :return: The create_time of this TestCaseBriefInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this TestCaseBriefInfo.

        创建时间

        :param create_time: The create_time of this TestCaseBriefInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this TestCaseBriefInfo.

        更新时间

        :return: The update_time of this TestCaseBriefInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this TestCaseBriefInfo.

        更新时间

        :param update_time: The update_time of this TestCaseBriefInfo.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def parent_id(self):
        r"""Gets the parent_id of this TestCaseBriefInfo.

        所属目录id

        :return: The parent_id of this TestCaseBriefInfo.
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this TestCaseBriefInfo.

        所属目录id

        :param parent_id: The parent_id of this TestCaseBriefInfo.
        :type parent_id: int
        """
        self._parent_id = parent_id

    @property
    def type(self):
        r"""Gets the type of this TestCaseBriefInfo.

        类型（1-目录；2-用例；）

        :return: The type of this TestCaseBriefInfo.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this TestCaseBriefInfo.

        类型（1-目录；2-用例；）

        :param type: The type of this TestCaseBriefInfo.
        :type type: int
        """
        self._type = type

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
        if not isinstance(other, TestCaseBriefInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
