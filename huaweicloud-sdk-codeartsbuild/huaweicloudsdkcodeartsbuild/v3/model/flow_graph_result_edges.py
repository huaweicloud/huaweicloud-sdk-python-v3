# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlowGraphResultEdges:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        '_from': 'str',
        'to': 'str'
    }

    attribute_map = {
        '_from': 'from',
        'to': 'to'
    }

    def __init__(self, _from=None, to=None):
        """FlowGraphResultEdges

        The model defined in huaweicloud sdk

        :param _from: 依赖子任务ID
        :type _from: str
        :param to: 被依赖的子任务ID
        :type to: str
        """
        
        

        self.__from = None
        self._to = None
        self.discriminator = None

        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to

    @property
    def _from(self):
        """Gets the _from of this FlowGraphResultEdges.

        依赖子任务ID

        :return: The _from of this FlowGraphResultEdges.
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this FlowGraphResultEdges.

        依赖子任务ID

        :param _from: The _from of this FlowGraphResultEdges.
        :type _from: str
        """
        self.__from = _from

    @property
    def to(self):
        """Gets the to of this FlowGraphResultEdges.

        被依赖的子任务ID

        :return: The to of this FlowGraphResultEdges.
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this FlowGraphResultEdges.

        被依赖的子任务ID

        :param to: The to of this FlowGraphResultEdges.
        :type to: str
        """
        self._to = to

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
        if not isinstance(other, FlowGraphResultEdges):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
