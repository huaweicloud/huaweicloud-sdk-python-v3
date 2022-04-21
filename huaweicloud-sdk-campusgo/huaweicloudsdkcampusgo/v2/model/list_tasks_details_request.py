# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTasksDetailsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'service_name': 'str',
        'service_version': 'str',
        'state': 'str',
        'name_like': 'str',
        'id_like': 'str',
        'created_since': 'int',
        'created_until': 'int',
        'order': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'service_name': 'service_name',
        'service_version': 'service_version',
        'state': 'state',
        'name_like': 'name_like',
        'id_like': 'id_like',
        'created_since': 'created_since',
        'created_until': 'created_until',
        'order': 'order',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, service_name=None, service_version=None, state=None, name_like=None, id_like=None, created_since=None, created_until=None, order=None, offset=None, limit=None):
        """ListTasksDetailsRequest

        The model defined in huaweicloud sdk

        :param service_name: 服务名称
        :type service_name: str
        :param service_version: 目标服务作业对应的服务版本号
        :type service_version: str
        :param state: 目标服务作业的状态，分别为PENDING（等待中），RECOVERING（恢复中），STARTING（启动中），UPGRADING（升级中），CREATE_FAILED（创建失败），START_FAILED（启动失败），RUNNING（运行中），STOPPING（停止中），STOPPED（已停止），ABNORMAL（异常），SUCCEEDED（运行成功），FAILED（运行失败），DELETING（删除中），FREEZING（冻结中），FROZEN（已冻结）
        :type state: str
        :param name_like: 目标服务作业的名称，支持模糊匹配
        :type name_like: str
        :param id_like: 目标服务作业的ID，支持模糊匹配
        :type id_like: str
        :param created_since: 目标服务作业的创建起始时间
        :type created_since: int
        :param created_until: 目标服务作业的创建截止时间
        :type created_until: int
        :param order: 展示服务作业时的排序字段和顺序，分别为name:ASC（按名称顺序排序），name:DESC（按名称倒序排序），created_at:ASC（按创建时间正序排序），created_at:DESC（按创建时间倒序排序），updated_at:ASC（按更新时间正序排序），updated_at:DESC（按更新时间倒序排序）
        :type order: str
        :param offset: 首个展示的服务作业的偏移量
        :type offset: int
        :param limit: 展示服务作业的数量
        :type limit: int
        """
        
        

        self._service_name = None
        self._service_version = None
        self._state = None
        self._name_like = None
        self._id_like = None
        self._created_since = None
        self._created_until = None
        self._order = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.service_name = service_name
        if service_version is not None:
            self.service_version = service_version
        if state is not None:
            self.state = state
        if name_like is not None:
            self.name_like = name_like
        if id_like is not None:
            self.id_like = id_like
        if created_since is not None:
            self.created_since = created_since
        if created_until is not None:
            self.created_until = created_until
        if order is not None:
            self.order = order
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def service_name(self):
        """Gets the service_name of this ListTasksDetailsRequest.

        服务名称

        :return: The service_name of this ListTasksDetailsRequest.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this ListTasksDetailsRequest.

        服务名称

        :param service_name: The service_name of this ListTasksDetailsRequest.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def service_version(self):
        """Gets the service_version of this ListTasksDetailsRequest.

        目标服务作业对应的服务版本号

        :return: The service_version of this ListTasksDetailsRequest.
        :rtype: str
        """
        return self._service_version

    @service_version.setter
    def service_version(self, service_version):
        """Sets the service_version of this ListTasksDetailsRequest.

        目标服务作业对应的服务版本号

        :param service_version: The service_version of this ListTasksDetailsRequest.
        :type service_version: str
        """
        self._service_version = service_version

    @property
    def state(self):
        """Gets the state of this ListTasksDetailsRequest.

        目标服务作业的状态，分别为PENDING（等待中），RECOVERING（恢复中），STARTING（启动中），UPGRADING（升级中），CREATE_FAILED（创建失败），START_FAILED（启动失败），RUNNING（运行中），STOPPING（停止中），STOPPED（已停止），ABNORMAL（异常），SUCCEEDED（运行成功），FAILED（运行失败），DELETING（删除中），FREEZING（冻结中），FROZEN（已冻结）

        :return: The state of this ListTasksDetailsRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ListTasksDetailsRequest.

        目标服务作业的状态，分别为PENDING（等待中），RECOVERING（恢复中），STARTING（启动中），UPGRADING（升级中），CREATE_FAILED（创建失败），START_FAILED（启动失败），RUNNING（运行中），STOPPING（停止中），STOPPED（已停止），ABNORMAL（异常），SUCCEEDED（运行成功），FAILED（运行失败），DELETING（删除中），FREEZING（冻结中），FROZEN（已冻结）

        :param state: The state of this ListTasksDetailsRequest.
        :type state: str
        """
        self._state = state

    @property
    def name_like(self):
        """Gets the name_like of this ListTasksDetailsRequest.

        目标服务作业的名称，支持模糊匹配

        :return: The name_like of this ListTasksDetailsRequest.
        :rtype: str
        """
        return self._name_like

    @name_like.setter
    def name_like(self, name_like):
        """Sets the name_like of this ListTasksDetailsRequest.

        目标服务作业的名称，支持模糊匹配

        :param name_like: The name_like of this ListTasksDetailsRequest.
        :type name_like: str
        """
        self._name_like = name_like

    @property
    def id_like(self):
        """Gets the id_like of this ListTasksDetailsRequest.

        目标服务作业的ID，支持模糊匹配

        :return: The id_like of this ListTasksDetailsRequest.
        :rtype: str
        """
        return self._id_like

    @id_like.setter
    def id_like(self, id_like):
        """Sets the id_like of this ListTasksDetailsRequest.

        目标服务作业的ID，支持模糊匹配

        :param id_like: The id_like of this ListTasksDetailsRequest.
        :type id_like: str
        """
        self._id_like = id_like

    @property
    def created_since(self):
        """Gets the created_since of this ListTasksDetailsRequest.

        目标服务作业的创建起始时间

        :return: The created_since of this ListTasksDetailsRequest.
        :rtype: int
        """
        return self._created_since

    @created_since.setter
    def created_since(self, created_since):
        """Sets the created_since of this ListTasksDetailsRequest.

        目标服务作业的创建起始时间

        :param created_since: The created_since of this ListTasksDetailsRequest.
        :type created_since: int
        """
        self._created_since = created_since

    @property
    def created_until(self):
        """Gets the created_until of this ListTasksDetailsRequest.

        目标服务作业的创建截止时间

        :return: The created_until of this ListTasksDetailsRequest.
        :rtype: int
        """
        return self._created_until

    @created_until.setter
    def created_until(self, created_until):
        """Sets the created_until of this ListTasksDetailsRequest.

        目标服务作业的创建截止时间

        :param created_until: The created_until of this ListTasksDetailsRequest.
        :type created_until: int
        """
        self._created_until = created_until

    @property
    def order(self):
        """Gets the order of this ListTasksDetailsRequest.

        展示服务作业时的排序字段和顺序，分别为name:ASC（按名称顺序排序），name:DESC（按名称倒序排序），created_at:ASC（按创建时间正序排序），created_at:DESC（按创建时间倒序排序），updated_at:ASC（按更新时间正序排序），updated_at:DESC（按更新时间倒序排序）

        :return: The order of this ListTasksDetailsRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ListTasksDetailsRequest.

        展示服务作业时的排序字段和顺序，分别为name:ASC（按名称顺序排序），name:DESC（按名称倒序排序），created_at:ASC（按创建时间正序排序），created_at:DESC（按创建时间倒序排序），updated_at:ASC（按更新时间正序排序），updated_at:DESC（按更新时间倒序排序）

        :param order: The order of this ListTasksDetailsRequest.
        :type order: str
        """
        self._order = order

    @property
    def offset(self):
        """Gets the offset of this ListTasksDetailsRequest.

        首个展示的服务作业的偏移量

        :return: The offset of this ListTasksDetailsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListTasksDetailsRequest.

        首个展示的服务作业的偏移量

        :param offset: The offset of this ListTasksDetailsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListTasksDetailsRequest.

        展示服务作业的数量

        :return: The limit of this ListTasksDetailsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListTasksDetailsRequest.

        展示服务作业的数量

        :param limit: The limit of this ListTasksDetailsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListTasksDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
