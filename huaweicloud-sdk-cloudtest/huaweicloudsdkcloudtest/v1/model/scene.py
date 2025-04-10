# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Scene:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app': 'str',
        'create_time': 'str',
        'creator_name': 'str',
        'creator_num': 'str',
        'delete_time': 'str',
        'deleted': 'str',
        'id': 'str',
        'mindmap_id': 'str',
        'name': 'str',
        'node_id': 'str',
        'status': 'str',
        'status_type': 'str',
        'tc_counts': 'str',
        'test_cases': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'app': 'app',
        'create_time': 'create_time',
        'creator_name': 'creator_name',
        'creator_num': 'creator_num',
        'delete_time': 'delete_time',
        'deleted': 'deleted',
        'id': 'id',
        'mindmap_id': 'mindmap_id',
        'name': 'name',
        'node_id': 'node_id',
        'status': 'status',
        'status_type': 'status_type',
        'tc_counts': 'tc_counts',
        'test_cases': 'test_cases',
        'update_time': 'update_time'
    }

    def __init__(self, app=None, create_time=None, creator_name=None, creator_num=None, delete_time=None, deleted=None, id=None, mindmap_id=None, name=None, node_id=None, status=None, status_type=None, tc_counts=None, test_cases=None, update_time=None):
        r"""Scene

        The model defined in huaweicloud sdk

        :param app: app
        :type app: str
        :param create_time: 创建时间
        :type create_time: str
        :param creator_name: 创建人名称
        :type creator_name: str
        :param creator_num: 创建人工号
        :type creator_num: str
        :param delete_time: 删除时间
        :type delete_time: str
        :param deleted: 是否删除
        :type deleted: str
        :param id: id 主键
        :type id: str
        :param mindmap_id: 脑图id
        :type mindmap_id: str
        :param name: 名称
        :type name: str
        :param node_id: 节点id
        :type node_id: str
        :param status: 状态
        :type status: str
        :param status_type: 状态类型
        :type status_type: str
        :param tc_counts: tc数量
        :type tc_counts: str
        :param test_cases: 测试用例
        :type test_cases: str
        :param update_time: 更新时间
        :type update_time: str
        """
        
        

        self._app = None
        self._create_time = None
        self._creator_name = None
        self._creator_num = None
        self._delete_time = None
        self._deleted = None
        self._id = None
        self._mindmap_id = None
        self._name = None
        self._node_id = None
        self._status = None
        self._status_type = None
        self._tc_counts = None
        self._test_cases = None
        self._update_time = None
        self.discriminator = None

        if app is not None:
            self.app = app
        if create_time is not None:
            self.create_time = create_time
        if creator_name is not None:
            self.creator_name = creator_name
        if creator_num is not None:
            self.creator_num = creator_num
        if delete_time is not None:
            self.delete_time = delete_time
        if deleted is not None:
            self.deleted = deleted
        if id is not None:
            self.id = id
        if mindmap_id is not None:
            self.mindmap_id = mindmap_id
        if name is not None:
            self.name = name
        if node_id is not None:
            self.node_id = node_id
        if status is not None:
            self.status = status
        if status_type is not None:
            self.status_type = status_type
        if tc_counts is not None:
            self.tc_counts = tc_counts
        if test_cases is not None:
            self.test_cases = test_cases
        if update_time is not None:
            self.update_time = update_time

    @property
    def app(self):
        r"""Gets the app of this Scene.

        app

        :return: The app of this Scene.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        r"""Sets the app of this Scene.

        app

        :param app: The app of this Scene.
        :type app: str
        """
        self._app = app

    @property
    def create_time(self):
        r"""Gets the create_time of this Scene.

        创建时间

        :return: The create_time of this Scene.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this Scene.

        创建时间

        :param create_time: The create_time of this Scene.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def creator_name(self):
        r"""Gets the creator_name of this Scene.

        创建人名称

        :return: The creator_name of this Scene.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        r"""Sets the creator_name of this Scene.

        创建人名称

        :param creator_name: The creator_name of this Scene.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def creator_num(self):
        r"""Gets the creator_num of this Scene.

        创建人工号

        :return: The creator_num of this Scene.
        :rtype: str
        """
        return self._creator_num

    @creator_num.setter
    def creator_num(self, creator_num):
        r"""Sets the creator_num of this Scene.

        创建人工号

        :param creator_num: The creator_num of this Scene.
        :type creator_num: str
        """
        self._creator_num = creator_num

    @property
    def delete_time(self):
        r"""Gets the delete_time of this Scene.

        删除时间

        :return: The delete_time of this Scene.
        :rtype: str
        """
        return self._delete_time

    @delete_time.setter
    def delete_time(self, delete_time):
        r"""Sets the delete_time of this Scene.

        删除时间

        :param delete_time: The delete_time of this Scene.
        :type delete_time: str
        """
        self._delete_time = delete_time

    @property
    def deleted(self):
        r"""Gets the deleted of this Scene.

        是否删除

        :return: The deleted of this Scene.
        :rtype: str
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        r"""Sets the deleted of this Scene.

        是否删除

        :param deleted: The deleted of this Scene.
        :type deleted: str
        """
        self._deleted = deleted

    @property
    def id(self):
        r"""Gets the id of this Scene.

        id 主键

        :return: The id of this Scene.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Scene.

        id 主键

        :param id: The id of this Scene.
        :type id: str
        """
        self._id = id

    @property
    def mindmap_id(self):
        r"""Gets the mindmap_id of this Scene.

        脑图id

        :return: The mindmap_id of this Scene.
        :rtype: str
        """
        return self._mindmap_id

    @mindmap_id.setter
    def mindmap_id(self, mindmap_id):
        r"""Sets the mindmap_id of this Scene.

        脑图id

        :param mindmap_id: The mindmap_id of this Scene.
        :type mindmap_id: str
        """
        self._mindmap_id = mindmap_id

    @property
    def name(self):
        r"""Gets the name of this Scene.

        名称

        :return: The name of this Scene.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Scene.

        名称

        :param name: The name of this Scene.
        :type name: str
        """
        self._name = name

    @property
    def node_id(self):
        r"""Gets the node_id of this Scene.

        节点id

        :return: The node_id of this Scene.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this Scene.

        节点id

        :param node_id: The node_id of this Scene.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def status(self):
        r"""Gets the status of this Scene.

        状态

        :return: The status of this Scene.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Scene.

        状态

        :param status: The status of this Scene.
        :type status: str
        """
        self._status = status

    @property
    def status_type(self):
        r"""Gets the status_type of this Scene.

        状态类型

        :return: The status_type of this Scene.
        :rtype: str
        """
        return self._status_type

    @status_type.setter
    def status_type(self, status_type):
        r"""Sets the status_type of this Scene.

        状态类型

        :param status_type: The status_type of this Scene.
        :type status_type: str
        """
        self._status_type = status_type

    @property
    def tc_counts(self):
        r"""Gets the tc_counts of this Scene.

        tc数量

        :return: The tc_counts of this Scene.
        :rtype: str
        """
        return self._tc_counts

    @tc_counts.setter
    def tc_counts(self, tc_counts):
        r"""Sets the tc_counts of this Scene.

        tc数量

        :param tc_counts: The tc_counts of this Scene.
        :type tc_counts: str
        """
        self._tc_counts = tc_counts

    @property
    def test_cases(self):
        r"""Gets the test_cases of this Scene.

        测试用例

        :return: The test_cases of this Scene.
        :rtype: str
        """
        return self._test_cases

    @test_cases.setter
    def test_cases(self, test_cases):
        r"""Sets the test_cases of this Scene.

        测试用例

        :param test_cases: The test_cases of this Scene.
        :type test_cases: str
        """
        self._test_cases = test_cases

    @property
    def update_time(self):
        r"""Gets the update_time of this Scene.

        更新时间

        :return: The update_time of this Scene.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this Scene.

        更新时间

        :param update_time: The update_time of this Scene.
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
        if not isinstance(other, Scene):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
