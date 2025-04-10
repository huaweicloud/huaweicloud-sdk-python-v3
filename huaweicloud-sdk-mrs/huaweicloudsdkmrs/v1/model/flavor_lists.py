# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlavorLists:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'master': 'list[str]',
        'core': 'list[str]',
        'task': 'list[str]'
    }

    attribute_map = {
        'master': 'master',
        'core': 'core',
        'task': 'task'
    }

    def __init__(self, master=None, core=None, task=None):
        r"""FlavorLists

        The model defined in huaweicloud sdk

        :param master: master节点支持的规格列表
        :type master: list[str]
        :param core: core节点支持的规格列表
        :type core: list[str]
        :param task: task节点支持的规格列表
        :type task: list[str]
        """
        
        

        self._master = None
        self._core = None
        self._task = None
        self.discriminator = None

        if master is not None:
            self.master = master
        if core is not None:
            self.core = core
        if task is not None:
            self.task = task

    @property
    def master(self):
        r"""Gets the master of this FlavorLists.

        master节点支持的规格列表

        :return: The master of this FlavorLists.
        :rtype: list[str]
        """
        return self._master

    @master.setter
    def master(self, master):
        r"""Sets the master of this FlavorLists.

        master节点支持的规格列表

        :param master: The master of this FlavorLists.
        :type master: list[str]
        """
        self._master = master

    @property
    def core(self):
        r"""Gets the core of this FlavorLists.

        core节点支持的规格列表

        :return: The core of this FlavorLists.
        :rtype: list[str]
        """
        return self._core

    @core.setter
    def core(self, core):
        r"""Sets the core of this FlavorLists.

        core节点支持的规格列表

        :param core: The core of this FlavorLists.
        :type core: list[str]
        """
        self._core = core

    @property
    def task(self):
        r"""Gets the task of this FlavorLists.

        task节点支持的规格列表

        :return: The task of this FlavorLists.
        :rtype: list[str]
        """
        return self._task

    @task.setter
    def task(self, task):
        r"""Sets the task of this FlavorLists.

        task节点支持的规格列表

        :param task: The task of this FlavorLists.
        :type task: list[str]
        """
        self._task = task

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
        if not isinstance(other, FlavorLists):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
