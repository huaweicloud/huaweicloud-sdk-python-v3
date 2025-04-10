# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchEnvTopologyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_list': 'list[TopoNode]',
        'line_list': 'list[TopoLine]',
        'collector_config': 'dict(str, CollectorConfigModel)',
        'real_start_time': 'int',
        'real_end_time': 'int'
    }

    attribute_map = {
        'node_list': 'node_list',
        'line_list': 'line_list',
        'collector_config': 'collector_config',
        'real_start_time': 'real_start_time',
        'real_end_time': 'real_end_time'
    }

    def __init__(self, node_list=None, line_list=None, collector_config=None, real_start_time=None, real_end_time=None):
        r"""SearchEnvTopologyResponse

        The model defined in huaweicloud sdk

        :param node_list: 组件节点列表。
        :type node_list: list[:class:`huaweicloudsdkapm.v1.TopoNode`]
        :param line_list: 组件之间调用指向线列表。
        :type line_list: list[:class:`huaweicloudsdkapm.v1.TopoLine`]
        :param collector_config: 采集器配置。
        :type collector_config: dict(str, CollectorConfigModel)
        :param real_start_time: 开始时间。
        :type real_start_time: int
        :param real_end_time: 结束时间。
        :type real_end_time: int
        """
        
        super(SearchEnvTopologyResponse, self).__init__()

        self._node_list = None
        self._line_list = None
        self._collector_config = None
        self._real_start_time = None
        self._real_end_time = None
        self.discriminator = None

        if node_list is not None:
            self.node_list = node_list
        if line_list is not None:
            self.line_list = line_list
        if collector_config is not None:
            self.collector_config = collector_config
        if real_start_time is not None:
            self.real_start_time = real_start_time
        if real_end_time is not None:
            self.real_end_time = real_end_time

    @property
    def node_list(self):
        r"""Gets the node_list of this SearchEnvTopologyResponse.

        组件节点列表。

        :return: The node_list of this SearchEnvTopologyResponse.
        :rtype: list[:class:`huaweicloudsdkapm.v1.TopoNode`]
        """
        return self._node_list

    @node_list.setter
    def node_list(self, node_list):
        r"""Sets the node_list of this SearchEnvTopologyResponse.

        组件节点列表。

        :param node_list: The node_list of this SearchEnvTopologyResponse.
        :type node_list: list[:class:`huaweicloudsdkapm.v1.TopoNode`]
        """
        self._node_list = node_list

    @property
    def line_list(self):
        r"""Gets the line_list of this SearchEnvTopologyResponse.

        组件之间调用指向线列表。

        :return: The line_list of this SearchEnvTopologyResponse.
        :rtype: list[:class:`huaweicloudsdkapm.v1.TopoLine`]
        """
        return self._line_list

    @line_list.setter
    def line_list(self, line_list):
        r"""Sets the line_list of this SearchEnvTopologyResponse.

        组件之间调用指向线列表。

        :param line_list: The line_list of this SearchEnvTopologyResponse.
        :type line_list: list[:class:`huaweicloudsdkapm.v1.TopoLine`]
        """
        self._line_list = line_list

    @property
    def collector_config(self):
        r"""Gets the collector_config of this SearchEnvTopologyResponse.

        采集器配置。

        :return: The collector_config of this SearchEnvTopologyResponse.
        :rtype: dict(str, CollectorConfigModel)
        """
        return self._collector_config

    @collector_config.setter
    def collector_config(self, collector_config):
        r"""Sets the collector_config of this SearchEnvTopologyResponse.

        采集器配置。

        :param collector_config: The collector_config of this SearchEnvTopologyResponse.
        :type collector_config: dict(str, CollectorConfigModel)
        """
        self._collector_config = collector_config

    @property
    def real_start_time(self):
        r"""Gets the real_start_time of this SearchEnvTopologyResponse.

        开始时间。

        :return: The real_start_time of this SearchEnvTopologyResponse.
        :rtype: int
        """
        return self._real_start_time

    @real_start_time.setter
    def real_start_time(self, real_start_time):
        r"""Sets the real_start_time of this SearchEnvTopologyResponse.

        开始时间。

        :param real_start_time: The real_start_time of this SearchEnvTopologyResponse.
        :type real_start_time: int
        """
        self._real_start_time = real_start_time

    @property
    def real_end_time(self):
        r"""Gets the real_end_time of this SearchEnvTopologyResponse.

        结束时间。

        :return: The real_end_time of this SearchEnvTopologyResponse.
        :rtype: int
        """
        return self._real_end_time

    @real_end_time.setter
    def real_end_time(self, real_end_time):
        r"""Sets the real_end_time of this SearchEnvTopologyResponse.

        结束时间。

        :param real_end_time: The real_end_time of this SearchEnvTopologyResponse.
        :type real_end_time: int
        """
        self._real_end_time = real_end_time

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
        if not isinstance(other, SearchEnvTopologyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
