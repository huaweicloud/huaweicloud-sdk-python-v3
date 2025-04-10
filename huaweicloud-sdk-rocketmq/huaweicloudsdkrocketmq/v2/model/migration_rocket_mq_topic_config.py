# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MigrationRocketMqTopicConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topic_name': 'str',
        'order': 'bool',
        'perm': 'int',
        'read_queue_nums': 'int',
        'write_queue_nums': 'int',
        'topic_filter_type': 'str',
        'topic_sys_flag': 'int'
    }

    attribute_map = {
        'topic_name': 'topicName',
        'order': 'order',
        'perm': 'perm',
        'read_queue_nums': 'readQueueNums',
        'write_queue_nums': 'writeQueueNums',
        'topic_filter_type': 'topicFilterType',
        'topic_sys_flag': 'topicSysFlag'
    }

    def __init__(self, topic_name=None, order=None, perm=None, read_queue_nums=None, write_queue_nums=None, topic_filter_type=None, topic_sys_flag=None):
        r"""MigrationRocketMqTopicConfig

        The model defined in huaweicloud sdk

        :param topic_name: Topic名称。
        :type topic_name: str
        :param order: 是否有序消息。
        :type order: bool
        :param perm: Topic权限。
        :type perm: int
        :param read_queue_nums: 读队列个数。
        :type read_queue_nums: int
        :param write_queue_nums: 写队列个数。
        :type write_queue_nums: int
        :param topic_filter_type: Topic过滤类型。   - SINGLE_TAG：单标签   - MULTI_TAG：多标签
        :type topic_filter_type: str
        :param topic_sys_flag: Topic系统标志位。
        :type topic_sys_flag: int
        """
        
        

        self._topic_name = None
        self._order = None
        self._perm = None
        self._read_queue_nums = None
        self._write_queue_nums = None
        self._topic_filter_type = None
        self._topic_sys_flag = None
        self.discriminator = None

        if topic_name is not None:
            self.topic_name = topic_name
        if order is not None:
            self.order = order
        if perm is not None:
            self.perm = perm
        if read_queue_nums is not None:
            self.read_queue_nums = read_queue_nums
        if write_queue_nums is not None:
            self.write_queue_nums = write_queue_nums
        if topic_filter_type is not None:
            self.topic_filter_type = topic_filter_type
        if topic_sys_flag is not None:
            self.topic_sys_flag = topic_sys_flag

    @property
    def topic_name(self):
        r"""Gets the topic_name of this MigrationRocketMqTopicConfig.

        Topic名称。

        :return: The topic_name of this MigrationRocketMqTopicConfig.
        :rtype: str
        """
        return self._topic_name

    @topic_name.setter
    def topic_name(self, topic_name):
        r"""Sets the topic_name of this MigrationRocketMqTopicConfig.

        Topic名称。

        :param topic_name: The topic_name of this MigrationRocketMqTopicConfig.
        :type topic_name: str
        """
        self._topic_name = topic_name

    @property
    def order(self):
        r"""Gets the order of this MigrationRocketMqTopicConfig.

        是否有序消息。

        :return: The order of this MigrationRocketMqTopicConfig.
        :rtype: bool
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this MigrationRocketMqTopicConfig.

        是否有序消息。

        :param order: The order of this MigrationRocketMqTopicConfig.
        :type order: bool
        """
        self._order = order

    @property
    def perm(self):
        r"""Gets the perm of this MigrationRocketMqTopicConfig.

        Topic权限。

        :return: The perm of this MigrationRocketMqTopicConfig.
        :rtype: int
        """
        return self._perm

    @perm.setter
    def perm(self, perm):
        r"""Sets the perm of this MigrationRocketMqTopicConfig.

        Topic权限。

        :param perm: The perm of this MigrationRocketMqTopicConfig.
        :type perm: int
        """
        self._perm = perm

    @property
    def read_queue_nums(self):
        r"""Gets the read_queue_nums of this MigrationRocketMqTopicConfig.

        读队列个数。

        :return: The read_queue_nums of this MigrationRocketMqTopicConfig.
        :rtype: int
        """
        return self._read_queue_nums

    @read_queue_nums.setter
    def read_queue_nums(self, read_queue_nums):
        r"""Sets the read_queue_nums of this MigrationRocketMqTopicConfig.

        读队列个数。

        :param read_queue_nums: The read_queue_nums of this MigrationRocketMqTopicConfig.
        :type read_queue_nums: int
        """
        self._read_queue_nums = read_queue_nums

    @property
    def write_queue_nums(self):
        r"""Gets the write_queue_nums of this MigrationRocketMqTopicConfig.

        写队列个数。

        :return: The write_queue_nums of this MigrationRocketMqTopicConfig.
        :rtype: int
        """
        return self._write_queue_nums

    @write_queue_nums.setter
    def write_queue_nums(self, write_queue_nums):
        r"""Sets the write_queue_nums of this MigrationRocketMqTopicConfig.

        写队列个数。

        :param write_queue_nums: The write_queue_nums of this MigrationRocketMqTopicConfig.
        :type write_queue_nums: int
        """
        self._write_queue_nums = write_queue_nums

    @property
    def topic_filter_type(self):
        r"""Gets the topic_filter_type of this MigrationRocketMqTopicConfig.

        Topic过滤类型。   - SINGLE_TAG：单标签   - MULTI_TAG：多标签

        :return: The topic_filter_type of this MigrationRocketMqTopicConfig.
        :rtype: str
        """
        return self._topic_filter_type

    @topic_filter_type.setter
    def topic_filter_type(self, topic_filter_type):
        r"""Sets the topic_filter_type of this MigrationRocketMqTopicConfig.

        Topic过滤类型。   - SINGLE_TAG：单标签   - MULTI_TAG：多标签

        :param topic_filter_type: The topic_filter_type of this MigrationRocketMqTopicConfig.
        :type topic_filter_type: str
        """
        self._topic_filter_type = topic_filter_type

    @property
    def topic_sys_flag(self):
        r"""Gets the topic_sys_flag of this MigrationRocketMqTopicConfig.

        Topic系统标志位。

        :return: The topic_sys_flag of this MigrationRocketMqTopicConfig.
        :rtype: int
        """
        return self._topic_sys_flag

    @topic_sys_flag.setter
    def topic_sys_flag(self, topic_sys_flag):
        r"""Sets the topic_sys_flag of this MigrationRocketMqTopicConfig.

        Topic系统标志位。

        :param topic_sys_flag: The topic_sys_flag of this MigrationRocketMqTopicConfig.
        :type topic_sys_flag: int
        """
        self._topic_sys_flag = topic_sys_flag

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
        if not isinstance(other, MigrationRocketMqTopicConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
