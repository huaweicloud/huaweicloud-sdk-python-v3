# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TestPoint:

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
        'group_id': 'str',
        'id': 'str',
        'mindmap_id': 'str',
        'name': 'str',
        'node_id': 'str',
        'requirement_id': 'str',
        'requirement_name': 'str',
        'service_id': 'str',
        'status': 'str',
        'status_type': 'str',
        'tc_counts': 'str',
        'test_cases': 'str',
        'update_name': 'str',
        'update_num': 'str',
        'update_time': 'str',
        'version': 'str'
    }

    attribute_map = {
        'app': 'app',
        'create_time': 'create_time',
        'creator_name': 'creator_name',
        'creator_num': 'creator_num',
        'delete_time': 'delete_time',
        'deleted': 'deleted',
        'group_id': 'group_id',
        'id': 'id',
        'mindmap_id': 'mindmap_id',
        'name': 'name',
        'node_id': 'node_id',
        'requirement_id': 'requirement_id',
        'requirement_name': 'requirement_name',
        'service_id': 'service_id',
        'status': 'status',
        'status_type': 'status_type',
        'tc_counts': 'tc_counts',
        'test_cases': 'test_cases',
        'update_name': 'update_name',
        'update_num': 'update_num',
        'update_time': 'update_time',
        'version': 'version'
    }

    def __init__(self, app=None, create_time=None, creator_name=None, creator_num=None, delete_time=None, deleted=None, group_id=None, id=None, mindmap_id=None, name=None, node_id=None, requirement_id=None, requirement_name=None, service_id=None, status=None, status_type=None, tc_counts=None, test_cases=None, update_name=None, update_num=None, update_time=None, version=None):
        r"""TestPoint

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
        :param deleted: 逻辑删除字段
        :type deleted: str
        :param group_id: 分组id
        :type group_id: str
        :param id: id 主键
        :type id: str
        :param mindmap_id: 脑图id
        :type mindmap_id: str
        :param name: 名称
        :type name: str
        :param node_id: 节点id
        :type node_id: str
        :param requirement_id: 需求id
        :type requirement_id: str
        :param requirement_name: 需求名称
        :type requirement_name: str
        :param service_id: 服务id
        :type service_id: str
        :param status: 状态
        :type status: str
        :param status_type: 状体类型
        :type status_type: str
        :param tc_counts: tc数量
        :type tc_counts: str
        :param test_cases: 测试用例
        :type test_cases: str
        :param update_name: 更新人名称
        :type update_name: str
        :param update_num: 更新人工号
        :type update_num: str
        :param update_time: 更新时间
        :type update_time: str
        :param version: 版本
        :type version: str
        """
        
        

        self._app = None
        self._create_time = None
        self._creator_name = None
        self._creator_num = None
        self._delete_time = None
        self._deleted = None
        self._group_id = None
        self._id = None
        self._mindmap_id = None
        self._name = None
        self._node_id = None
        self._requirement_id = None
        self._requirement_name = None
        self._service_id = None
        self._status = None
        self._status_type = None
        self._tc_counts = None
        self._test_cases = None
        self._update_name = None
        self._update_num = None
        self._update_time = None
        self._version = None
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
        if group_id is not None:
            self.group_id = group_id
        if id is not None:
            self.id = id
        if mindmap_id is not None:
            self.mindmap_id = mindmap_id
        if name is not None:
            self.name = name
        if node_id is not None:
            self.node_id = node_id
        if requirement_id is not None:
            self.requirement_id = requirement_id
        if requirement_name is not None:
            self.requirement_name = requirement_name
        if service_id is not None:
            self.service_id = service_id
        if status is not None:
            self.status = status
        if status_type is not None:
            self.status_type = status_type
        if tc_counts is not None:
            self.tc_counts = tc_counts
        if test_cases is not None:
            self.test_cases = test_cases
        if update_name is not None:
            self.update_name = update_name
        if update_num is not None:
            self.update_num = update_num
        if update_time is not None:
            self.update_time = update_time
        if version is not None:
            self.version = version

    @property
    def app(self):
        r"""Gets the app of this TestPoint.

        app

        :return: The app of this TestPoint.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        r"""Sets the app of this TestPoint.

        app

        :param app: The app of this TestPoint.
        :type app: str
        """
        self._app = app

    @property
    def create_time(self):
        r"""Gets the create_time of this TestPoint.

        创建时间

        :return: The create_time of this TestPoint.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this TestPoint.

        创建时间

        :param create_time: The create_time of this TestPoint.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def creator_name(self):
        r"""Gets the creator_name of this TestPoint.

        创建人名称

        :return: The creator_name of this TestPoint.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        r"""Sets the creator_name of this TestPoint.

        创建人名称

        :param creator_name: The creator_name of this TestPoint.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def creator_num(self):
        r"""Gets the creator_num of this TestPoint.

        创建人工号

        :return: The creator_num of this TestPoint.
        :rtype: str
        """
        return self._creator_num

    @creator_num.setter
    def creator_num(self, creator_num):
        r"""Sets the creator_num of this TestPoint.

        创建人工号

        :param creator_num: The creator_num of this TestPoint.
        :type creator_num: str
        """
        self._creator_num = creator_num

    @property
    def delete_time(self):
        r"""Gets the delete_time of this TestPoint.

        删除时间

        :return: The delete_time of this TestPoint.
        :rtype: str
        """
        return self._delete_time

    @delete_time.setter
    def delete_time(self, delete_time):
        r"""Sets the delete_time of this TestPoint.

        删除时间

        :param delete_time: The delete_time of this TestPoint.
        :type delete_time: str
        """
        self._delete_time = delete_time

    @property
    def deleted(self):
        r"""Gets the deleted of this TestPoint.

        逻辑删除字段

        :return: The deleted of this TestPoint.
        :rtype: str
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        r"""Sets the deleted of this TestPoint.

        逻辑删除字段

        :param deleted: The deleted of this TestPoint.
        :type deleted: str
        """
        self._deleted = deleted

    @property
    def group_id(self):
        r"""Gets the group_id of this TestPoint.

        分组id

        :return: The group_id of this TestPoint.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this TestPoint.

        分组id

        :param group_id: The group_id of this TestPoint.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def id(self):
        r"""Gets the id of this TestPoint.

        id 主键

        :return: The id of this TestPoint.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TestPoint.

        id 主键

        :param id: The id of this TestPoint.
        :type id: str
        """
        self._id = id

    @property
    def mindmap_id(self):
        r"""Gets the mindmap_id of this TestPoint.

        脑图id

        :return: The mindmap_id of this TestPoint.
        :rtype: str
        """
        return self._mindmap_id

    @mindmap_id.setter
    def mindmap_id(self, mindmap_id):
        r"""Sets the mindmap_id of this TestPoint.

        脑图id

        :param mindmap_id: The mindmap_id of this TestPoint.
        :type mindmap_id: str
        """
        self._mindmap_id = mindmap_id

    @property
    def name(self):
        r"""Gets the name of this TestPoint.

        名称

        :return: The name of this TestPoint.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TestPoint.

        名称

        :param name: The name of this TestPoint.
        :type name: str
        """
        self._name = name

    @property
    def node_id(self):
        r"""Gets the node_id of this TestPoint.

        节点id

        :return: The node_id of this TestPoint.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this TestPoint.

        节点id

        :param node_id: The node_id of this TestPoint.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def requirement_id(self):
        r"""Gets the requirement_id of this TestPoint.

        需求id

        :return: The requirement_id of this TestPoint.
        :rtype: str
        """
        return self._requirement_id

    @requirement_id.setter
    def requirement_id(self, requirement_id):
        r"""Sets the requirement_id of this TestPoint.

        需求id

        :param requirement_id: The requirement_id of this TestPoint.
        :type requirement_id: str
        """
        self._requirement_id = requirement_id

    @property
    def requirement_name(self):
        r"""Gets the requirement_name of this TestPoint.

        需求名称

        :return: The requirement_name of this TestPoint.
        :rtype: str
        """
        return self._requirement_name

    @requirement_name.setter
    def requirement_name(self, requirement_name):
        r"""Sets the requirement_name of this TestPoint.

        需求名称

        :param requirement_name: The requirement_name of this TestPoint.
        :type requirement_name: str
        """
        self._requirement_name = requirement_name

    @property
    def service_id(self):
        r"""Gets the service_id of this TestPoint.

        服务id

        :return: The service_id of this TestPoint.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        r"""Sets the service_id of this TestPoint.

        服务id

        :param service_id: The service_id of this TestPoint.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def status(self):
        r"""Gets the status of this TestPoint.

        状态

        :return: The status of this TestPoint.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this TestPoint.

        状态

        :param status: The status of this TestPoint.
        :type status: str
        """
        self._status = status

    @property
    def status_type(self):
        r"""Gets the status_type of this TestPoint.

        状体类型

        :return: The status_type of this TestPoint.
        :rtype: str
        """
        return self._status_type

    @status_type.setter
    def status_type(self, status_type):
        r"""Sets the status_type of this TestPoint.

        状体类型

        :param status_type: The status_type of this TestPoint.
        :type status_type: str
        """
        self._status_type = status_type

    @property
    def tc_counts(self):
        r"""Gets the tc_counts of this TestPoint.

        tc数量

        :return: The tc_counts of this TestPoint.
        :rtype: str
        """
        return self._tc_counts

    @tc_counts.setter
    def tc_counts(self, tc_counts):
        r"""Sets the tc_counts of this TestPoint.

        tc数量

        :param tc_counts: The tc_counts of this TestPoint.
        :type tc_counts: str
        """
        self._tc_counts = tc_counts

    @property
    def test_cases(self):
        r"""Gets the test_cases of this TestPoint.

        测试用例

        :return: The test_cases of this TestPoint.
        :rtype: str
        """
        return self._test_cases

    @test_cases.setter
    def test_cases(self, test_cases):
        r"""Sets the test_cases of this TestPoint.

        测试用例

        :param test_cases: The test_cases of this TestPoint.
        :type test_cases: str
        """
        self._test_cases = test_cases

    @property
    def update_name(self):
        r"""Gets the update_name of this TestPoint.

        更新人名称

        :return: The update_name of this TestPoint.
        :rtype: str
        """
        return self._update_name

    @update_name.setter
    def update_name(self, update_name):
        r"""Sets the update_name of this TestPoint.

        更新人名称

        :param update_name: The update_name of this TestPoint.
        :type update_name: str
        """
        self._update_name = update_name

    @property
    def update_num(self):
        r"""Gets the update_num of this TestPoint.

        更新人工号

        :return: The update_num of this TestPoint.
        :rtype: str
        """
        return self._update_num

    @update_num.setter
    def update_num(self, update_num):
        r"""Sets the update_num of this TestPoint.

        更新人工号

        :param update_num: The update_num of this TestPoint.
        :type update_num: str
        """
        self._update_num = update_num

    @property
    def update_time(self):
        r"""Gets the update_time of this TestPoint.

        更新时间

        :return: The update_time of this TestPoint.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this TestPoint.

        更新时间

        :param update_time: The update_time of this TestPoint.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def version(self):
        r"""Gets the version of this TestPoint.

        版本

        :return: The version of this TestPoint.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this TestPoint.

        版本

        :param version: The version of this TestPoint.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, TestPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
