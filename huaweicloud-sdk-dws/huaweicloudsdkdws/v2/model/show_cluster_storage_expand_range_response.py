# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClusterStorageExpandRangeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'min_size': 'int',
        'max_size': 'int',
        'current_size': 'int',
        'step': 'int'
    }

    attribute_map = {
        'min_size': 'min_size',
        'max_size': 'max_size',
        'current_size': 'current_size',
        'step': 'step'
    }

    def __init__(self, min_size=None, max_size=None, current_size=None, step=None):
        r"""ShowClusterStorageExpandRangeResponse

        The model defined in huaweicloud sdk

        :param min_size: **参数解释**： 扩容后单节点磁盘最小值（单位GB）。 **取值范围**： 不涉及。
        :type min_size: int
        :param max_size: **参数解释**： 扩容后单节点磁盘最大值（单位GB）。 **取值范围**： 不涉及。
        :type max_size: int
        :param current_size: **参数解释**： 磁盘当前值（单位GB）。 **取值范围**： 不涉及。
        :type current_size: int
        :param step: **参数解释**： 磁盘步长大小（单位GB）。比如当前单节点磁盘20GB，步长为20，则扩容后单节点磁盘大小至少为40GB。 **取值范围**： 大于等于10。
        :type step: int
        """
        
        super(ShowClusterStorageExpandRangeResponse, self).__init__()

        self._min_size = None
        self._max_size = None
        self._current_size = None
        self._step = None
        self.discriminator = None

        if min_size is not None:
            self.min_size = min_size
        if max_size is not None:
            self.max_size = max_size
        if current_size is not None:
            self.current_size = current_size
        if step is not None:
            self.step = step

    @property
    def min_size(self):
        r"""Gets the min_size of this ShowClusterStorageExpandRangeResponse.

        **参数解释**： 扩容后单节点磁盘最小值（单位GB）。 **取值范围**： 不涉及。

        :return: The min_size of this ShowClusterStorageExpandRangeResponse.
        :rtype: int
        """
        return self._min_size

    @min_size.setter
    def min_size(self, min_size):
        r"""Sets the min_size of this ShowClusterStorageExpandRangeResponse.

        **参数解释**： 扩容后单节点磁盘最小值（单位GB）。 **取值范围**： 不涉及。

        :param min_size: The min_size of this ShowClusterStorageExpandRangeResponse.
        :type min_size: int
        """
        self._min_size = min_size

    @property
    def max_size(self):
        r"""Gets the max_size of this ShowClusterStorageExpandRangeResponse.

        **参数解释**： 扩容后单节点磁盘最大值（单位GB）。 **取值范围**： 不涉及。

        :return: The max_size of this ShowClusterStorageExpandRangeResponse.
        :rtype: int
        """
        return self._max_size

    @max_size.setter
    def max_size(self, max_size):
        r"""Sets the max_size of this ShowClusterStorageExpandRangeResponse.

        **参数解释**： 扩容后单节点磁盘最大值（单位GB）。 **取值范围**： 不涉及。

        :param max_size: The max_size of this ShowClusterStorageExpandRangeResponse.
        :type max_size: int
        """
        self._max_size = max_size

    @property
    def current_size(self):
        r"""Gets the current_size of this ShowClusterStorageExpandRangeResponse.

        **参数解释**： 磁盘当前值（单位GB）。 **取值范围**： 不涉及。

        :return: The current_size of this ShowClusterStorageExpandRangeResponse.
        :rtype: int
        """
        return self._current_size

    @current_size.setter
    def current_size(self, current_size):
        r"""Sets the current_size of this ShowClusterStorageExpandRangeResponse.

        **参数解释**： 磁盘当前值（单位GB）。 **取值范围**： 不涉及。

        :param current_size: The current_size of this ShowClusterStorageExpandRangeResponse.
        :type current_size: int
        """
        self._current_size = current_size

    @property
    def step(self):
        r"""Gets the step of this ShowClusterStorageExpandRangeResponse.

        **参数解释**： 磁盘步长大小（单位GB）。比如当前单节点磁盘20GB，步长为20，则扩容后单节点磁盘大小至少为40GB。 **取值范围**： 大于等于10。

        :return: The step of this ShowClusterStorageExpandRangeResponse.
        :rtype: int
        """
        return self._step

    @step.setter
    def step(self, step):
        r"""Sets the step of this ShowClusterStorageExpandRangeResponse.

        **参数解释**： 磁盘步长大小（单位GB）。比如当前单节点磁盘20GB，步长为20，则扩容后单节点磁盘大小至少为40GB。 **取值范围**： 大于等于10。

        :param step: The step of this ShowClusterStorageExpandRangeResponse.
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
        if not isinstance(other, ShowClusterStorageExpandRangeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
