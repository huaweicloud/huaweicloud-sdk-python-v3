# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiskAutoExpansionPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'threshold': 'int',
        'step': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'threshold': 'threshold',
        'step': 'step'
    }

    def __init__(self, instance_id=None, threshold=None, step=None):
        r"""DiskAutoExpansionPolicy

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param threshold: 触发自动扩容阈值，只支持输入80、85和90。默认阈值为90，即当已使用存储空间达到总存储空间的90%时就会触发扩容。集群实例的自动扩容阈值指的是每个shard。
        :type threshold: int
        :param step: 扩容步长（s%），默认为10，支持输入10、15和20。当触发自动扩容的时候，自动扩容当前存储空间的s%（非10倍数向上取整。小数点后四舍五入，默认一次最小10G，账户余额不足时，会导致包年包月实例扩容失败）。
        :type step: int
        """
        
        

        self._instance_id = None
        self._threshold = None
        self._step = None
        self.discriminator = None

        self.instance_id = instance_id
        if threshold is not None:
            self.threshold = threshold
        if step is not None:
            self.step = step

    @property
    def instance_id(self):
        r"""Gets the instance_id of this DiskAutoExpansionPolicy.

        实例ID。

        :return: The instance_id of this DiskAutoExpansionPolicy.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this DiskAutoExpansionPolicy.

        实例ID。

        :param instance_id: The instance_id of this DiskAutoExpansionPolicy.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def threshold(self):
        r"""Gets the threshold of this DiskAutoExpansionPolicy.

        触发自动扩容阈值，只支持输入80、85和90。默认阈值为90，即当已使用存储空间达到总存储空间的90%时就会触发扩容。集群实例的自动扩容阈值指的是每个shard。

        :return: The threshold of this DiskAutoExpansionPolicy.
        :rtype: int
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        r"""Sets the threshold of this DiskAutoExpansionPolicy.

        触发自动扩容阈值，只支持输入80、85和90。默认阈值为90，即当已使用存储空间达到总存储空间的90%时就会触发扩容。集群实例的自动扩容阈值指的是每个shard。

        :param threshold: The threshold of this DiskAutoExpansionPolicy.
        :type threshold: int
        """
        self._threshold = threshold

    @property
    def step(self):
        r"""Gets the step of this DiskAutoExpansionPolicy.

        扩容步长（s%），默认为10，支持输入10、15和20。当触发自动扩容的时候，自动扩容当前存储空间的s%（非10倍数向上取整。小数点后四舍五入，默认一次最小10G，账户余额不足时，会导致包年包月实例扩容失败）。

        :return: The step of this DiskAutoExpansionPolicy.
        :rtype: int
        """
        return self._step

    @step.setter
    def step(self, step):
        r"""Sets the step of this DiskAutoExpansionPolicy.

        扩容步长（s%），默认为10，支持输入10、15和20。当触发自动扩容的时候，自动扩容当前存储空间的s%（非10倍数向上取整。小数点后四舍五入，默认一次最小10G，账户余额不足时，会导致包年包月实例扩容失败）。

        :param step: The step of this DiskAutoExpansionPolicy.
        :type step: int
        """
        self._step = step

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
        if not isinstance(other, DiskAutoExpansionPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
