# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTopIoTrafficsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'instance_id': 'str',
        'node_id': 'str',
        'component_id': 'str',
        'top_io_num': 'int',
        'sort_condition': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'node_id': 'node_id',
        'component_id': 'component_id',
        'top_io_num': 'top_io_num',
        'sort_condition': 'sort_condition'
    }

    def __init__(self, x_language=None, instance_id=None, node_id=None, component_id=None, top_io_num=None, sort_condition=None):
        """ListTopIoTrafficsRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言
        :type x_language: str
        :param instance_id: 实例ID，严格匹配UUID规则。
        :type instance_id: str
        :param node_id: 节点ID。节点应为CN或者非日志角色的DN节点，并且节点状态为正常。
        :type node_id: str
        :param component_id: 组件ID。组件应为CN或者非日志角色的DN组件。 DN：Data Node，和CN对应的概念。负责实际执行表数据的存储、查询操作。 CN：Coordinator Node，负责数据库系统元数据存储、查询任务的分解和部分执行，以及将DN中查询结果汇聚在一起。
        :type component_id: str
        :param top_io_num: 期望查询数据库进程下TOP IO线程数（默认值为20）。接口返回TOP IO线程与会话信息关联后的结果，数量最大不超过该值。
        :type top_io_num: int
        :param sort_condition: TOP IO排序条件
        :type sort_condition: str
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._node_id = None
        self._component_id = None
        self._top_io_num = None
        self._sort_condition = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        self.node_id = node_id
        self.component_id = component_id
        if top_io_num is not None:
            self.top_io_num = top_io_num
        if sort_condition is not None:
            self.sort_condition = sort_condition

    @property
    def x_language(self):
        """Gets the x_language of this ListTopIoTrafficsRequest.

        语言

        :return: The x_language of this ListTopIoTrafficsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListTopIoTrafficsRequest.

        语言

        :param x_language: The x_language of this ListTopIoTrafficsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        """Gets the instance_id of this ListTopIoTrafficsRequest.

        实例ID，严格匹配UUID规则。

        :return: The instance_id of this ListTopIoTrafficsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListTopIoTrafficsRequest.

        实例ID，严格匹配UUID规则。

        :param instance_id: The instance_id of this ListTopIoTrafficsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def node_id(self):
        """Gets the node_id of this ListTopIoTrafficsRequest.

        节点ID。节点应为CN或者非日志角色的DN节点，并且节点状态为正常。

        :return: The node_id of this ListTopIoTrafficsRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this ListTopIoTrafficsRequest.

        节点ID。节点应为CN或者非日志角色的DN节点，并且节点状态为正常。

        :param node_id: The node_id of this ListTopIoTrafficsRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def component_id(self):
        """Gets the component_id of this ListTopIoTrafficsRequest.

        组件ID。组件应为CN或者非日志角色的DN组件。 DN：Data Node，和CN对应的概念。负责实际执行表数据的存储、查询操作。 CN：Coordinator Node，负责数据库系统元数据存储、查询任务的分解和部分执行，以及将DN中查询结果汇聚在一起。

        :return: The component_id of this ListTopIoTrafficsRequest.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        """Sets the component_id of this ListTopIoTrafficsRequest.

        组件ID。组件应为CN或者非日志角色的DN组件。 DN：Data Node，和CN对应的概念。负责实际执行表数据的存储、查询操作。 CN：Coordinator Node，负责数据库系统元数据存储、查询任务的分解和部分执行，以及将DN中查询结果汇聚在一起。

        :param component_id: The component_id of this ListTopIoTrafficsRequest.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def top_io_num(self):
        """Gets the top_io_num of this ListTopIoTrafficsRequest.

        期望查询数据库进程下TOP IO线程数（默认值为20）。接口返回TOP IO线程与会话信息关联后的结果，数量最大不超过该值。

        :return: The top_io_num of this ListTopIoTrafficsRequest.
        :rtype: int
        """
        return self._top_io_num

    @top_io_num.setter
    def top_io_num(self, top_io_num):
        """Sets the top_io_num of this ListTopIoTrafficsRequest.

        期望查询数据库进程下TOP IO线程数（默认值为20）。接口返回TOP IO线程与会话信息关联后的结果，数量最大不超过该值。

        :param top_io_num: The top_io_num of this ListTopIoTrafficsRequest.
        :type top_io_num: int
        """
        self._top_io_num = top_io_num

    @property
    def sort_condition(self):
        """Gets the sort_condition of this ListTopIoTrafficsRequest.

        TOP IO排序条件

        :return: The sort_condition of this ListTopIoTrafficsRequest.
        :rtype: str
        """
        return self._sort_condition

    @sort_condition.setter
    def sort_condition(self, sort_condition):
        """Sets the sort_condition of this ListTopIoTrafficsRequest.

        TOP IO排序条件

        :param sort_condition: The sort_condition of this ListTopIoTrafficsRequest.
        :type sort_condition: str
        """
        self._sort_condition = sort_condition

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
        if not isinstance(other, ListTopIoTrafficsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
