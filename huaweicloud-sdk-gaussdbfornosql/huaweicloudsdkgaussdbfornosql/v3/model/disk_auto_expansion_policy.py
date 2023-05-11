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
        'threshold': 'int',
        'step': 'int',
        'size': 'int'
    }

    attribute_map = {
        'threshold': 'threshold',
        'step': 'step',
        'size': 'size'
    }

    def __init__(self, threshold=None, step=None, size=None):
        """DiskAutoExpansionPolicy

        The model defined in huaweicloud sdk

        :param threshold: 触发自动扩容阈值，只支持输入80、85和90。默认阈值为90，即当已使用存储空间达到总存储空间的90%或者可用空间小于10GB时就会触发扩容。
        :type threshold: int
        :param step: 扩容步长（s%），默认为10，支持输入10、15和20。当触发自动扩容的时候，自动扩容当前存储空间的s%（非10倍数向上取整。小数点后四舍五入，默认一次最小100G，账户余额不足时，会导致包年包月实例扩容失败）
        :type step: int
        :param size: 实例通过自动扩容所能达到的存储空间上限,单位：GB。需要大于等于实例购买的存储空间大小，且最大上限不能超过实例当前规格支持的最大存储容量。批量自动扩容时，不支持自定义存储自动扩容上限，默认扩容至所选实例对应的最大存储空间。
        :type size: int
        """
        
        

        self._threshold = None
        self._step = None
        self._size = None
        self.discriminator = None

        if threshold is not None:
            self.threshold = threshold
        if step is not None:
            self.step = step
        if size is not None:
            self.size = size

    @property
    def threshold(self):
        """Gets the threshold of this DiskAutoExpansionPolicy.

        触发自动扩容阈值，只支持输入80、85和90。默认阈值为90，即当已使用存储空间达到总存储空间的90%或者可用空间小于10GB时就会触发扩容。

        :return: The threshold of this DiskAutoExpansionPolicy.
        :rtype: int
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this DiskAutoExpansionPolicy.

        触发自动扩容阈值，只支持输入80、85和90。默认阈值为90，即当已使用存储空间达到总存储空间的90%或者可用空间小于10GB时就会触发扩容。

        :param threshold: The threshold of this DiskAutoExpansionPolicy.
        :type threshold: int
        """
        self._threshold = threshold

    @property
    def step(self):
        """Gets the step of this DiskAutoExpansionPolicy.

        扩容步长（s%），默认为10，支持输入10、15和20。当触发自动扩容的时候，自动扩容当前存储空间的s%（非10倍数向上取整。小数点后四舍五入，默认一次最小100G，账户余额不足时，会导致包年包月实例扩容失败）

        :return: The step of this DiskAutoExpansionPolicy.
        :rtype: int
        """
        return self._step

    @step.setter
    def step(self, step):
        """Sets the step of this DiskAutoExpansionPolicy.

        扩容步长（s%），默认为10，支持输入10、15和20。当触发自动扩容的时候，自动扩容当前存储空间的s%（非10倍数向上取整。小数点后四舍五入，默认一次最小100G，账户余额不足时，会导致包年包月实例扩容失败）

        :param step: The step of this DiskAutoExpansionPolicy.
        :type step: int
        """
        self._step = step

    @property
    def size(self):
        """Gets the size of this DiskAutoExpansionPolicy.

        实例通过自动扩容所能达到的存储空间上限,单位：GB。需要大于等于实例购买的存储空间大小，且最大上限不能超过实例当前规格支持的最大存储容量。批量自动扩容时，不支持自定义存储自动扩容上限，默认扩容至所选实例对应的最大存储空间。

        :return: The size of this DiskAutoExpansionPolicy.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this DiskAutoExpansionPolicy.

        实例通过自动扩容所能达到的存储空间上限,单位：GB。需要大于等于实例购买的存储空间大小，且最大上限不能超过实例当前规格支持的最大存储容量。批量自动扩容时，不支持自定义存储自动扩容上限，默认扩容至所选实例对应的最大存储空间。

        :param size: The size of this DiskAutoExpansionPolicy.
        :type size: int
        """
        self._size = size

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
