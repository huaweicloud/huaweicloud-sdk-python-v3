# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AzFlavors:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'az_code': 'str',
        'az_name': 'str',
        'master': 'list[Flavor]',
        'core': 'list[Flavor]',
        'task': 'list[Flavor]'
    }

    attribute_map = {
        'az_code': 'az_code',
        'az_name': 'az_name',
        'master': 'master',
        'core': 'core',
        'task': 'task'
    }

    def __init__(self, az_code=None, az_name=None, master=None, core=None, task=None):
        r"""AzFlavors

        The model defined in huaweicloud sdk

        :param az_code: 可用区code
        :type az_code: str
        :param az_name: 可用区名称
        :type az_name: str
        :param master: master节点支持的规格列表
        :type master: list[:class:`huaweicloudsdkmrs.v2.Flavor`]
        :param core: core节点支持的规格列表
        :type core: list[:class:`huaweicloudsdkmrs.v2.Flavor`]
        :param task: task节点支持的规格列表
        :type task: list[:class:`huaweicloudsdkmrs.v2.Flavor`]
        """
        
        

        self._az_code = None
        self._az_name = None
        self._master = None
        self._core = None
        self._task = None
        self.discriminator = None

        if az_code is not None:
            self.az_code = az_code
        if az_name is not None:
            self.az_name = az_name
        if master is not None:
            self.master = master
        if core is not None:
            self.core = core
        if task is not None:
            self.task = task

    @property
    def az_code(self):
        r"""Gets the az_code of this AzFlavors.

        可用区code

        :return: The az_code of this AzFlavors.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        r"""Sets the az_code of this AzFlavors.

        可用区code

        :param az_code: The az_code of this AzFlavors.
        :type az_code: str
        """
        self._az_code = az_code

    @property
    def az_name(self):
        r"""Gets the az_name of this AzFlavors.

        可用区名称

        :return: The az_name of this AzFlavors.
        :rtype: str
        """
        return self._az_name

    @az_name.setter
    def az_name(self, az_name):
        r"""Sets the az_name of this AzFlavors.

        可用区名称

        :param az_name: The az_name of this AzFlavors.
        :type az_name: str
        """
        self._az_name = az_name

    @property
    def master(self):
        r"""Gets the master of this AzFlavors.

        master节点支持的规格列表

        :return: The master of this AzFlavors.
        :rtype: list[:class:`huaweicloudsdkmrs.v2.Flavor`]
        """
        return self._master

    @master.setter
    def master(self, master):
        r"""Sets the master of this AzFlavors.

        master节点支持的规格列表

        :param master: The master of this AzFlavors.
        :type master: list[:class:`huaweicloudsdkmrs.v2.Flavor`]
        """
        self._master = master

    @property
    def core(self):
        r"""Gets the core of this AzFlavors.

        core节点支持的规格列表

        :return: The core of this AzFlavors.
        :rtype: list[:class:`huaweicloudsdkmrs.v2.Flavor`]
        """
        return self._core

    @core.setter
    def core(self, core):
        r"""Sets the core of this AzFlavors.

        core节点支持的规格列表

        :param core: The core of this AzFlavors.
        :type core: list[:class:`huaweicloudsdkmrs.v2.Flavor`]
        """
        self._core = core

    @property
    def task(self):
        r"""Gets the task of this AzFlavors.

        task节点支持的规格列表

        :return: The task of this AzFlavors.
        :rtype: list[:class:`huaweicloudsdkmrs.v2.Flavor`]
        """
        return self._task

    @task.setter
    def task(self, task):
        r"""Sets the task of this AzFlavors.

        task节点支持的规格列表

        :param task: The task of this AzFlavors.
        :type task: list[:class:`huaweicloudsdkmrs.v2.Flavor`]
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
        if not isinstance(other, AzFlavors):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
