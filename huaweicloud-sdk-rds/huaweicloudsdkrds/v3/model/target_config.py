# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TargetConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor': 'str',
        'cpu': 'str',
        'mem': 'str'
    }

    attribute_map = {
        'flavor': 'flavor',
        'cpu': 'cpu',
        'mem': 'mem'
    }

    def __init__(self, flavor=None, cpu=None, mem=None):
        r"""TargetConfig

        The model defined in huaweicloud sdk

        :param flavor: 当name&#x3D;RESIZE_FLAVOR时，表示规格变更任务的目标规格。
        :type flavor: str
        :param cpu: 当name&#x3D;RESIZE_FLAVOR时，表示规格变更任务的的目标cpu。
        :type cpu: str
        :param mem: 当name&#x3D;RESIZE_FLAVOR时，表示规格变更任务的目标内存。
        :type mem: str
        """
        
        

        self._flavor = None
        self._cpu = None
        self._mem = None
        self.discriminator = None

        if flavor is not None:
            self.flavor = flavor
        if cpu is not None:
            self.cpu = cpu
        if mem is not None:
            self.mem = mem

    @property
    def flavor(self):
        r"""Gets the flavor of this TargetConfig.

        当name=RESIZE_FLAVOR时，表示规格变更任务的目标规格。

        :return: The flavor of this TargetConfig.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this TargetConfig.

        当name=RESIZE_FLAVOR时，表示规格变更任务的目标规格。

        :param flavor: The flavor of this TargetConfig.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def cpu(self):
        r"""Gets the cpu of this TargetConfig.

        当name=RESIZE_FLAVOR时，表示规格变更任务的的目标cpu。

        :return: The cpu of this TargetConfig.
        :rtype: str
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this TargetConfig.

        当name=RESIZE_FLAVOR时，表示规格变更任务的的目标cpu。

        :param cpu: The cpu of this TargetConfig.
        :type cpu: str
        """
        self._cpu = cpu

    @property
    def mem(self):
        r"""Gets the mem of this TargetConfig.

        当name=RESIZE_FLAVOR时，表示规格变更任务的目标内存。

        :return: The mem of this TargetConfig.
        :rtype: str
        """
        return self._mem

    @mem.setter
    def mem(self, mem):
        r"""Sets the mem of this TargetConfig.

        当name=RESIZE_FLAVOR时，表示规格变更任务的目标内存。

        :param mem: The mem of this TargetConfig.
        :type mem: str
        """
        self._mem = mem

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
        if not isinstance(other, TargetConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
