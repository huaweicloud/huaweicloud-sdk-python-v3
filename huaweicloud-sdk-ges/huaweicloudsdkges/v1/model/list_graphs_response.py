# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGraphsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'graph_count': 'int',
        'graphs': 'list[Graph1]',
        'error_message': 'str',
        'error_code': 'str'
    }

    attribute_map = {
        'graph_count': 'graphCount',
        'graphs': 'graphs',
        'error_message': 'errorMessage',
        'error_code': 'errorCode'
    }

    def __init__(self, graph_count=None, graphs=None, error_message=None, error_code=None):
        """ListGraphsResponse

        The model defined in huaweicloud sdk

        :param graph_count: 图总个数。请求失败时为空。
        :type graph_count: int
        :param graphs: 图列表。请求失败时为空。
        :type graphs: list[:class:`huaweicloudsdkges.v1.Graph1`]
        :param error_message: 系统提示信息，执行成功时，字段可能为空。执行失败时，用于显示错误信息。
        :type error_message: str
        :param error_code: 系统提示信息，执行成功时，字段可能为空。执行失败时，用于显示错误码。
        :type error_code: str
        """
        
        super(ListGraphsResponse, self).__init__()

        self._graph_count = None
        self._graphs = None
        self._error_message = None
        self._error_code = None
        self.discriminator = None

        if graph_count is not None:
            self.graph_count = graph_count
        if graphs is not None:
            self.graphs = graphs
        if error_message is not None:
            self.error_message = error_message
        if error_code is not None:
            self.error_code = error_code

    @property
    def graph_count(self):
        """Gets the graph_count of this ListGraphsResponse.

        图总个数。请求失败时为空。

        :return: The graph_count of this ListGraphsResponse.
        :rtype: int
        """
        return self._graph_count

    @graph_count.setter
    def graph_count(self, graph_count):
        """Sets the graph_count of this ListGraphsResponse.

        图总个数。请求失败时为空。

        :param graph_count: The graph_count of this ListGraphsResponse.
        :type graph_count: int
        """
        self._graph_count = graph_count

    @property
    def graphs(self):
        """Gets the graphs of this ListGraphsResponse.

        图列表。请求失败时为空。

        :return: The graphs of this ListGraphsResponse.
        :rtype: list[:class:`huaweicloudsdkges.v1.Graph1`]
        """
        return self._graphs

    @graphs.setter
    def graphs(self, graphs):
        """Sets the graphs of this ListGraphsResponse.

        图列表。请求失败时为空。

        :param graphs: The graphs of this ListGraphsResponse.
        :type graphs: list[:class:`huaweicloudsdkges.v1.Graph1`]
        """
        self._graphs = graphs

    @property
    def error_message(self):
        """Gets the error_message of this ListGraphsResponse.

        系统提示信息，执行成功时，字段可能为空。执行失败时，用于显示错误信息。

        :return: The error_message of this ListGraphsResponse.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this ListGraphsResponse.

        系统提示信息，执行成功时，字段可能为空。执行失败时，用于显示错误信息。

        :param error_message: The error_message of this ListGraphsResponse.
        :type error_message: str
        """
        self._error_message = error_message

    @property
    def error_code(self):
        """Gets the error_code of this ListGraphsResponse.

        系统提示信息，执行成功时，字段可能为空。执行失败时，用于显示错误码。

        :return: The error_code of this ListGraphsResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ListGraphsResponse.

        系统提示信息，执行成功时，字段可能为空。执行失败时，用于显示错误码。

        :param error_code: The error_code of this ListGraphsResponse.
        :type error_code: str
        """
        self._error_code = error_code

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
        if not isinstance(other, ListGraphsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
