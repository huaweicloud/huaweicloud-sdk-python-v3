# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFlowLogsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flow_logs': 'list[FlowLog]',
        'request_id': 'str',
        'total_count': 'int',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'flow_logs': 'flow_logs',
        'request_id': 'request_id',
        'total_count': 'total_count',
        'page_info': 'page_info'
    }

    def __init__(self, flow_logs=None, request_id=None, total_count=None, page_info=None):
        r"""ListFlowLogsResponse

        The model defined in huaweicloud sdk

        :param flow_logs: 
        :type flow_logs: list[:class:`huaweicloudsdker.v3.FlowLog`]
        :param request_id: 请求ID
        :type request_id: str
        :param total_count: 总计数量
        :type total_count: int
        :param page_info: 
        :type page_info: :class:`huaweicloudsdker.v3.PageInfo`
        """
        
        super(ListFlowLogsResponse, self).__init__()

        self._flow_logs = None
        self._request_id = None
        self._total_count = None
        self._page_info = None
        self.discriminator = None

        if flow_logs is not None:
            self.flow_logs = flow_logs
        if request_id is not None:
            self.request_id = request_id
        if total_count is not None:
            self.total_count = total_count
        if page_info is not None:
            self.page_info = page_info

    @property
    def flow_logs(self):
        r"""Gets the flow_logs of this ListFlowLogsResponse.

        :return: The flow_logs of this ListFlowLogsResponse.
        :rtype: list[:class:`huaweicloudsdker.v3.FlowLog`]
        """
        return self._flow_logs

    @flow_logs.setter
    def flow_logs(self, flow_logs):
        r"""Sets the flow_logs of this ListFlowLogsResponse.

        :param flow_logs: The flow_logs of this ListFlowLogsResponse.
        :type flow_logs: list[:class:`huaweicloudsdker.v3.FlowLog`]
        """
        self._flow_logs = flow_logs

    @property
    def request_id(self):
        r"""Gets the request_id of this ListFlowLogsResponse.

        请求ID

        :return: The request_id of this ListFlowLogsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListFlowLogsResponse.

        请求ID

        :param request_id: The request_id of this ListFlowLogsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def total_count(self):
        r"""Gets the total_count of this ListFlowLogsResponse.

        总计数量

        :return: The total_count of this ListFlowLogsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListFlowLogsResponse.

        总计数量

        :param total_count: The total_count of this ListFlowLogsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def page_info(self):
        r"""Gets the page_info of this ListFlowLogsResponse.

        :return: The page_info of this ListFlowLogsResponse.
        :rtype: :class:`huaweicloudsdker.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListFlowLogsResponse.

        :param page_info: The page_info of this ListFlowLogsResponse.
        :type page_info: :class:`huaweicloudsdker.v3.PageInfo`
        """
        self._page_info = page_info

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
        if not isinstance(other, ListFlowLogsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
