# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MotionItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'timestamp': 'float',
        'root': 'list[float]',
        'joints': 'list[float]',
        'eyes': 'list[float]'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'root': 'root',
        'joints': 'joints',
        'eyes': 'eyes'
    }

    def __init__(self, timestamp=None, root=None, joints=None, eyes=None):
        """MotionItem

        The model defined in huaweicloud sdk

        :param timestamp: 时间戳，相对时间戳。  单位秒。  保留3位小数。
        :type timestamp: float
        :param root: root 3维坐标。
        :type root: list[float]
        :param joints: 75个关节点，四元数。
        :type joints: list[float]
        :param eyes: 眼动数据
        :type eyes: list[float]
        """
        
        

        self._timestamp = None
        self._root = None
        self._joints = None
        self._eyes = None
        self.discriminator = None

        if timestamp is not None:
            self.timestamp = timestamp
        if root is not None:
            self.root = root
        if joints is not None:
            self.joints = joints
        if eyes is not None:
            self.eyes = eyes

    @property
    def timestamp(self):
        """Gets the timestamp of this MotionItem.

        时间戳，相对时间戳。  单位秒。  保留3位小数。

        :return: The timestamp of this MotionItem.
        :rtype: float
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this MotionItem.

        时间戳，相对时间戳。  单位秒。  保留3位小数。

        :param timestamp: The timestamp of this MotionItem.
        :type timestamp: float
        """
        self._timestamp = timestamp

    @property
    def root(self):
        """Gets the root of this MotionItem.

        root 3维坐标。

        :return: The root of this MotionItem.
        :rtype: list[float]
        """
        return self._root

    @root.setter
    def root(self, root):
        """Sets the root of this MotionItem.

        root 3维坐标。

        :param root: The root of this MotionItem.
        :type root: list[float]
        """
        self._root = root

    @property
    def joints(self):
        """Gets the joints of this MotionItem.

        75个关节点，四元数。

        :return: The joints of this MotionItem.
        :rtype: list[float]
        """
        return self._joints

    @joints.setter
    def joints(self, joints):
        """Sets the joints of this MotionItem.

        75个关节点，四元数。

        :param joints: The joints of this MotionItem.
        :type joints: list[float]
        """
        self._joints = joints

    @property
    def eyes(self):
        """Gets the eyes of this MotionItem.

        眼动数据

        :return: The eyes of this MotionItem.
        :rtype: list[float]
        """
        return self._eyes

    @eyes.setter
    def eyes(self, eyes):
        """Sets the eyes of this MotionItem.

        眼动数据

        :param eyes: The eyes of this MotionItem.
        :type eyes: list[float]
        """
        self._eyes = eyes

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
        if not isinstance(other, MotionItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
