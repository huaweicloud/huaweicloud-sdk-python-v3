# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueueSrcAssignUpdateDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'queue_attr': 'int',
        'description': 'str'
    }

    attribute_map = {
        'queue_attr': 'queue_attr',
        'description': 'description'
    }

    def __init__(self, queue_attr=None, description=None):
        r"""QueueSrcAssignUpdateDTO

        The model defined in huaweicloud sdk

        :param queue_attr: 队列属性(0:默认,1:实时队列,2:离线队列), 当前只有yarn队列涉及。
        :type queue_attr: int
        :param description: 当前空间分配资源附加的描述信息。
        :type description: str
        """
        
        

        self._queue_attr = None
        self._description = None
        self.discriminator = None

        if queue_attr is not None:
            self.queue_attr = queue_attr
        if description is not None:
            self.description = description

    @property
    def queue_attr(self):
        r"""Gets the queue_attr of this QueueSrcAssignUpdateDTO.

        队列属性(0:默认,1:实时队列,2:离线队列), 当前只有yarn队列涉及。

        :return: The queue_attr of this QueueSrcAssignUpdateDTO.
        :rtype: int
        """
        return self._queue_attr

    @queue_attr.setter
    def queue_attr(self, queue_attr):
        r"""Sets the queue_attr of this QueueSrcAssignUpdateDTO.

        队列属性(0:默认,1:实时队列,2:离线队列), 当前只有yarn队列涉及。

        :param queue_attr: The queue_attr of this QueueSrcAssignUpdateDTO.
        :type queue_attr: int
        """
        self._queue_attr = queue_attr

    @property
    def description(self):
        r"""Gets the description of this QueueSrcAssignUpdateDTO.

        当前空间分配资源附加的描述信息。

        :return: The description of this QueueSrcAssignUpdateDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this QueueSrcAssignUpdateDTO.

        当前空间分配资源附加的描述信息。

        :param description: The description of this QueueSrcAssignUpdateDTO.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, QueueSrcAssignUpdateDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
