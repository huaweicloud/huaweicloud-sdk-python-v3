# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDdsSlowLogTrendRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'int',
        'end_time': 'int',
        'node_ids': 'list[str]'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'node_ids': 'node_ids'
    }

    def __init__(self, start_time=None, end_time=None, node_ids=None):
        r"""ShowDdsSlowLogTrendRequestBody

        The model defined in huaweicloud sdk

        :param start_time: 开始时间
        :type start_time: int
        :param end_time: 结束时间
        :type end_time: int
        :param node_ids: 节点ID列表
        :type node_ids: list[str]
        """
        
        

        self._start_time = None
        self._end_time = None
        self._node_ids = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        if node_ids is not None:
            self.node_ids = node_ids

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowDdsSlowLogTrendRequestBody.

        开始时间

        :return: The start_time of this ShowDdsSlowLogTrendRequestBody.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowDdsSlowLogTrendRequestBody.

        开始时间

        :param start_time: The start_time of this ShowDdsSlowLogTrendRequestBody.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowDdsSlowLogTrendRequestBody.

        结束时间

        :return: The end_time of this ShowDdsSlowLogTrendRequestBody.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowDdsSlowLogTrendRequestBody.

        结束时间

        :param end_time: The end_time of this ShowDdsSlowLogTrendRequestBody.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def node_ids(self):
        r"""Gets the node_ids of this ShowDdsSlowLogTrendRequestBody.

        节点ID列表

        :return: The node_ids of this ShowDdsSlowLogTrendRequestBody.
        :rtype: list[str]
        """
        return self._node_ids

    @node_ids.setter
    def node_ids(self, node_ids):
        r"""Sets the node_ids of this ShowDdsSlowLogTrendRequestBody.

        节点ID列表

        :param node_ids: The node_ids of this ShowDdsSlowLogTrendRequestBody.
        :type node_ids: list[str]
        """
        self._node_ids = node_ids

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowDdsSlowLogTrendRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
