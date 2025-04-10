# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeConstraints:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'other': 'dict(str, object)',
        'master': 'NodeConstraint',
        'core': 'NodeConstraint',
        'task': 'NodeConstraint',
        'core_separate': 'NodeConstraint',
        'core_combine': 'NodeConstraint',
        'task_separate': 'NodeConstraint',
        'task_combine': 'NodeConstraint',
        'node_group_task': 'NodeConstraint'
    }

    attribute_map = {
        'other': 'other',
        'master': 'master',
        'core': 'core',
        'task': 'task',
        'core_separate': 'core_separate',
        'core_combine': 'core_combine',
        'task_separate': 'task_separate',
        'task_combine': 'task_combine',
        'node_group_task': 'node_group_task'
    }

    def __init__(self, other=None, master=None, core=None, task=None, core_separate=None, core_combine=None, task_separate=None, task_combine=None, node_group_task=None):
        r"""NodeConstraints

        The model defined in huaweicloud sdk

        :param other: 其他节点限制
        :type other: dict(str, object)
        :param master: 
        :type master: :class:`huaweicloudsdkmrs.v1.NodeConstraint`
        :param core: 
        :type core: :class:`huaweicloudsdkmrs.v1.NodeConstraint`
        :param task: 
        :type task: :class:`huaweicloudsdkmrs.v1.NodeConstraint`
        :param core_separate: 
        :type core_separate: :class:`huaweicloudsdkmrs.v1.NodeConstraint`
        :param core_combine: 
        :type core_combine: :class:`huaweicloudsdkmrs.v1.NodeConstraint`
        :param task_separate: 
        :type task_separate: :class:`huaweicloudsdkmrs.v1.NodeConstraint`
        :param task_combine: 
        :type task_combine: :class:`huaweicloudsdkmrs.v1.NodeConstraint`
        :param node_group_task: 
        :type node_group_task: :class:`huaweicloudsdkmrs.v1.NodeConstraint`
        """
        
        

        self._other = None
        self._master = None
        self._core = None
        self._task = None
        self._core_separate = None
        self._core_combine = None
        self._task_separate = None
        self._task_combine = None
        self._node_group_task = None
        self.discriminator = None

        if other is not None:
            self.other = other
        if master is not None:
            self.master = master
        if core is not None:
            self.core = core
        if task is not None:
            self.task = task
        if core_separate is not None:
            self.core_separate = core_separate
        if core_combine is not None:
            self.core_combine = core_combine
        if task_separate is not None:
            self.task_separate = task_separate
        if task_combine is not None:
            self.task_combine = task_combine
        if node_group_task is not None:
            self.node_group_task = node_group_task

    @property
    def other(self):
        r"""Gets the other of this NodeConstraints.

        其他节点限制

        :return: The other of this NodeConstraints.
        :rtype: dict(str, object)
        """
        return self._other

    @other.setter
    def other(self, other):
        r"""Sets the other of this NodeConstraints.

        其他节点限制

        :param other: The other of this NodeConstraints.
        :type other: dict(str, object)
        """
        self._other = other

    @property
    def master(self):
        r"""Gets the master of this NodeConstraints.

        :return: The master of this NodeConstraints.
        :rtype: :class:`huaweicloudsdkmrs.v1.NodeConstraint`
        """
        return self._master

    @master.setter
    def master(self, master):
        r"""Sets the master of this NodeConstraints.

        :param master: The master of this NodeConstraints.
        :type master: :class:`huaweicloudsdkmrs.v1.NodeConstraint`
        """
        self._master = master

    @property
    def core(self):
        r"""Gets the core of this NodeConstraints.

        :return: The core of this NodeConstraints.
        :rtype: :class:`huaweicloudsdkmrs.v1.NodeConstraint`
        """
        return self._core

    @core.setter
    def core(self, core):
        r"""Sets the core of this NodeConstraints.

        :param core: The core of this NodeConstraints.
        :type core: :class:`huaweicloudsdkmrs.v1.NodeConstraint`
        """
        self._core = core

    @property
    def task(self):
        r"""Gets the task of this NodeConstraints.

        :return: The task of this NodeConstraints.
        :rtype: :class:`huaweicloudsdkmrs.v1.NodeConstraint`
        """
        return self._task

    @task.setter
    def task(self, task):
        r"""Sets the task of this NodeConstraints.

        :param task: The task of this NodeConstraints.
        :type task: :class:`huaweicloudsdkmrs.v1.NodeConstraint`
        """
        self._task = task

    @property
    def core_separate(self):
        r"""Gets the core_separate of this NodeConstraints.

        :return: The core_separate of this NodeConstraints.
        :rtype: :class:`huaweicloudsdkmrs.v1.NodeConstraint`
        """
        return self._core_separate

    @core_separate.setter
    def core_separate(self, core_separate):
        r"""Sets the core_separate of this NodeConstraints.

        :param core_separate: The core_separate of this NodeConstraints.
        :type core_separate: :class:`huaweicloudsdkmrs.v1.NodeConstraint`
        """
        self._core_separate = core_separate

    @property
    def core_combine(self):
        r"""Gets the core_combine of this NodeConstraints.

        :return: The core_combine of this NodeConstraints.
        :rtype: :class:`huaweicloudsdkmrs.v1.NodeConstraint`
        """
        return self._core_combine

    @core_combine.setter
    def core_combine(self, core_combine):
        r"""Sets the core_combine of this NodeConstraints.

        :param core_combine: The core_combine of this NodeConstraints.
        :type core_combine: :class:`huaweicloudsdkmrs.v1.NodeConstraint`
        """
        self._core_combine = core_combine

    @property
    def task_separate(self):
        r"""Gets the task_separate of this NodeConstraints.

        :return: The task_separate of this NodeConstraints.
        :rtype: :class:`huaweicloudsdkmrs.v1.NodeConstraint`
        """
        return self._task_separate

    @task_separate.setter
    def task_separate(self, task_separate):
        r"""Sets the task_separate of this NodeConstraints.

        :param task_separate: The task_separate of this NodeConstraints.
        :type task_separate: :class:`huaweicloudsdkmrs.v1.NodeConstraint`
        """
        self._task_separate = task_separate

    @property
    def task_combine(self):
        r"""Gets the task_combine of this NodeConstraints.

        :return: The task_combine of this NodeConstraints.
        :rtype: :class:`huaweicloudsdkmrs.v1.NodeConstraint`
        """
        return self._task_combine

    @task_combine.setter
    def task_combine(self, task_combine):
        r"""Sets the task_combine of this NodeConstraints.

        :param task_combine: The task_combine of this NodeConstraints.
        :type task_combine: :class:`huaweicloudsdkmrs.v1.NodeConstraint`
        """
        self._task_combine = task_combine

    @property
    def node_group_task(self):
        r"""Gets the node_group_task of this NodeConstraints.

        :return: The node_group_task of this NodeConstraints.
        :rtype: :class:`huaweicloudsdkmrs.v1.NodeConstraint`
        """
        return self._node_group_task

    @node_group_task.setter
    def node_group_task(self, node_group_task):
        r"""Sets the node_group_task of this NodeConstraints.

        :param node_group_task: The node_group_task of this NodeConstraints.
        :type node_group_task: :class:`huaweicloudsdkmrs.v1.NodeConstraint`
        """
        self._node_group_task = node_group_task

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
        if not isinstance(other, NodeConstraints):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
