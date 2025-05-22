# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResizeInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_node_num': 'int',
        'origin_node_num': 'int',
        'resize_status': 'str',
        'start_time': 'str'
    }

    attribute_map = {
        'target_node_num': 'target_node_num',
        'origin_node_num': 'origin_node_num',
        'resize_status': 'resize_status',
        'start_time': 'start_time'
    }

    def __init__(self, target_node_num=None, origin_node_num=None, resize_status=None, start_time=None):
        r"""ResizeInfo

        The model defined in huaweicloud sdk

        :param target_node_num: **参数解释**： 扩容后的节点数量。 **取值范围**： 不涉及。
        :type target_node_num: int
        :param origin_node_num: **参数解释**： 扩容前的节点数量。 **取值范围**： 不涉及。
        :type origin_node_num: int
        :param resize_status: **参数解释**： 扩容状态。 **取值范围**： - GROWING：扩容中 - RESIZE_FAILURE：扩容失败。
        :type resize_status: str
        :param start_time: **参数解释**： 扩容开始时间，格式为ISO8601：YYYY-MM-DDThh:mm:ss **取值范围**： 不涉及。
        :type start_time: str
        """
        
        

        self._target_node_num = None
        self._origin_node_num = None
        self._resize_status = None
        self._start_time = None
        self.discriminator = None

        if target_node_num is not None:
            self.target_node_num = target_node_num
        if origin_node_num is not None:
            self.origin_node_num = origin_node_num
        if resize_status is not None:
            self.resize_status = resize_status
        if start_time is not None:
            self.start_time = start_time

    @property
    def target_node_num(self):
        r"""Gets the target_node_num of this ResizeInfo.

        **参数解释**： 扩容后的节点数量。 **取值范围**： 不涉及。

        :return: The target_node_num of this ResizeInfo.
        :rtype: int
        """
        return self._target_node_num

    @target_node_num.setter
    def target_node_num(self, target_node_num):
        r"""Sets the target_node_num of this ResizeInfo.

        **参数解释**： 扩容后的节点数量。 **取值范围**： 不涉及。

        :param target_node_num: The target_node_num of this ResizeInfo.
        :type target_node_num: int
        """
        self._target_node_num = target_node_num

    @property
    def origin_node_num(self):
        r"""Gets the origin_node_num of this ResizeInfo.

        **参数解释**： 扩容前的节点数量。 **取值范围**： 不涉及。

        :return: The origin_node_num of this ResizeInfo.
        :rtype: int
        """
        return self._origin_node_num

    @origin_node_num.setter
    def origin_node_num(self, origin_node_num):
        r"""Sets the origin_node_num of this ResizeInfo.

        **参数解释**： 扩容前的节点数量。 **取值范围**： 不涉及。

        :param origin_node_num: The origin_node_num of this ResizeInfo.
        :type origin_node_num: int
        """
        self._origin_node_num = origin_node_num

    @property
    def resize_status(self):
        r"""Gets the resize_status of this ResizeInfo.

        **参数解释**： 扩容状态。 **取值范围**： - GROWING：扩容中 - RESIZE_FAILURE：扩容失败。

        :return: The resize_status of this ResizeInfo.
        :rtype: str
        """
        return self._resize_status

    @resize_status.setter
    def resize_status(self, resize_status):
        r"""Sets the resize_status of this ResizeInfo.

        **参数解释**： 扩容状态。 **取值范围**： - GROWING：扩容中 - RESIZE_FAILURE：扩容失败。

        :param resize_status: The resize_status of this ResizeInfo.
        :type resize_status: str
        """
        self._resize_status = resize_status

    @property
    def start_time(self):
        r"""Gets the start_time of this ResizeInfo.

        **参数解释**： 扩容开始时间，格式为ISO8601：YYYY-MM-DDThh:mm:ss **取值范围**： 不涉及。

        :return: The start_time of this ResizeInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ResizeInfo.

        **参数解释**： 扩容开始时间，格式为ISO8601：YYYY-MM-DDThh:mm:ss **取值范围**： 不涉及。

        :param start_time: The start_time of this ResizeInfo.
        :type start_time: str
        """
        self._start_time = start_time

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
        if not isinstance(other, ResizeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
