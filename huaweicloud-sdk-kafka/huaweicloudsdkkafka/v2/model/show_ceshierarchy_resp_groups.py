# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCeshierarchyRespGroups:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'queues': 'list[ShowCeshierarchyRespQueues1]'
    }

    attribute_map = {
        'name': 'name',
        'queues': 'queues'
    }

    def __init__(self, name=None, queues=None):
        r"""ShowCeshierarchyRespGroups

        The model defined in huaweicloud sdk

        :param name: 消费组名称。
        :type name: str
        :param queues: Topic信息。
        :type queues: list[:class:`huaweicloudsdkkafka.v2.ShowCeshierarchyRespQueues1`]
        """
        
        

        self._name = None
        self._queues = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if queues is not None:
            self.queues = queues

    @property
    def name(self):
        r"""Gets the name of this ShowCeshierarchyRespGroups.

        消费组名称。

        :return: The name of this ShowCeshierarchyRespGroups.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowCeshierarchyRespGroups.

        消费组名称。

        :param name: The name of this ShowCeshierarchyRespGroups.
        :type name: str
        """
        self._name = name

    @property
    def queues(self):
        r"""Gets the queues of this ShowCeshierarchyRespGroups.

        Topic信息。

        :return: The queues of this ShowCeshierarchyRespGroups.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.ShowCeshierarchyRespQueues1`]
        """
        return self._queues

    @queues.setter
    def queues(self, queues):
        r"""Sets the queues of this ShowCeshierarchyRespGroups.

        Topic信息。

        :param queues: The queues of this ShowCeshierarchyRespGroups.
        :type queues: list[:class:`huaweicloudsdkkafka.v2.ShowCeshierarchyRespQueues1`]
        """
        self._queues = queues

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
        if not isinstance(other, ShowCeshierarchyRespGroups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
