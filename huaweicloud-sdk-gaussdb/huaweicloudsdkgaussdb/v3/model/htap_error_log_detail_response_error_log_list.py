# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HtapErrorLogDetailResponseErrorLogList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'time': 'str',
        'level': 'str',
        'content': 'str',
        'line_num': 'str'
    }

    attribute_map = {
        'node_id': 'node_id',
        'time': 'time',
        'level': 'level',
        'content': 'content',
        'line_num': 'line_num'
    }

    def __init__(self, node_id=None, time=None, level=None, content=None, line_num=None):
        r"""HtapErrorLogDetailResponseErrorLogList

        The model defined in huaweicloud sdk

        :param node_id: **参数解释**： HTAP标准版实例节点ID。  **取值范围**：  不涉及。
        :type node_id: str
        :param time: **参数解释**： 日志时间。  **取值范围**：  不涉及。
        :type time: str
        :param level: **参数解释**： 日志级别。  **取值范围**：  不涉及。
        :type level: str
        :param content: **参数解释**： 日志内容。  **取值范围**：  不涉及。
        :type content: str
        :param line_num: **参数解释**： 日志单行序列号，第一次查询时不需要此参数，后续分页查询时需要使用，可从上次查询的返回信息中获取。  **取值范围**：  不涉及。
        :type line_num: str
        """
        
        

        self._node_id = None
        self._time = None
        self._level = None
        self._content = None
        self._line_num = None
        self.discriminator = None

        self.node_id = node_id
        self.time = time
        self.level = level
        self.content = content
        self.line_num = line_num

    @property
    def node_id(self):
        r"""Gets the node_id of this HtapErrorLogDetailResponseErrorLogList.

        **参数解释**： HTAP标准版实例节点ID。  **取值范围**：  不涉及。

        :return: The node_id of this HtapErrorLogDetailResponseErrorLogList.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this HtapErrorLogDetailResponseErrorLogList.

        **参数解释**： HTAP标准版实例节点ID。  **取值范围**：  不涉及。

        :param node_id: The node_id of this HtapErrorLogDetailResponseErrorLogList.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def time(self):
        r"""Gets the time of this HtapErrorLogDetailResponseErrorLogList.

        **参数解释**： 日志时间。  **取值范围**：  不涉及。

        :return: The time of this HtapErrorLogDetailResponseErrorLogList.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this HtapErrorLogDetailResponseErrorLogList.

        **参数解释**： 日志时间。  **取值范围**：  不涉及。

        :param time: The time of this HtapErrorLogDetailResponseErrorLogList.
        :type time: str
        """
        self._time = time

    @property
    def level(self):
        r"""Gets the level of this HtapErrorLogDetailResponseErrorLogList.

        **参数解释**： 日志级别。  **取值范围**：  不涉及。

        :return: The level of this HtapErrorLogDetailResponseErrorLogList.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this HtapErrorLogDetailResponseErrorLogList.

        **参数解释**： 日志级别。  **取值范围**：  不涉及。

        :param level: The level of this HtapErrorLogDetailResponseErrorLogList.
        :type level: str
        """
        self._level = level

    @property
    def content(self):
        r"""Gets the content of this HtapErrorLogDetailResponseErrorLogList.

        **参数解释**： 日志内容。  **取值范围**：  不涉及。

        :return: The content of this HtapErrorLogDetailResponseErrorLogList.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this HtapErrorLogDetailResponseErrorLogList.

        **参数解释**： 日志内容。  **取值范围**：  不涉及。

        :param content: The content of this HtapErrorLogDetailResponseErrorLogList.
        :type content: str
        """
        self._content = content

    @property
    def line_num(self):
        r"""Gets the line_num of this HtapErrorLogDetailResponseErrorLogList.

        **参数解释**： 日志单行序列号，第一次查询时不需要此参数，后续分页查询时需要使用，可从上次查询的返回信息中获取。  **取值范围**：  不涉及。

        :return: The line_num of this HtapErrorLogDetailResponseErrorLogList.
        :rtype: str
        """
        return self._line_num

    @line_num.setter
    def line_num(self, line_num):
        r"""Sets the line_num of this HtapErrorLogDetailResponseErrorLogList.

        **参数解释**： 日志单行序列号，第一次查询时不需要此参数，后续分页查询时需要使用，可从上次查询的返回信息中获取。  **取值范围**：  不涉及。

        :param line_num: The line_num of this HtapErrorLogDetailResponseErrorLogList.
        :type line_num: str
        """
        self._line_num = line_num

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
        if not isinstance(other, HtapErrorLogDetailResponseErrorLogList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
