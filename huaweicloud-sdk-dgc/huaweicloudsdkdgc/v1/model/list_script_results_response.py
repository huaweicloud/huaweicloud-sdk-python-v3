# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScriptResultsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'results': 'list[Result]',
        'message': 'str'
    }

    attribute_map = {
        'status': 'status',
        'results': 'results',
        'message': 'message'
    }

    def __init__(self, status=None, results=None, message=None):
        """ListScriptResultsResponse

        The model defined in huaweicloud sdk

        :param status: 执行状态。 - LAUNCHING ：提交中 - RUNNING ： 运行中 - FINISHED：执行成功 - FAILED：执行失败
        :type status: str
        :param results: 执行结果
        :type results: list[:class:`huaweicloudsdkdgc.v1.Result`]
        :param message: 执行失败消息
        :type message: str
        """
        
        super(ListScriptResultsResponse, self).__init__()

        self._status = None
        self._results = None
        self._message = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if results is not None:
            self.results = results
        if message is not None:
            self.message = message

    @property
    def status(self):
        """Gets the status of this ListScriptResultsResponse.

        执行状态。 - LAUNCHING ：提交中 - RUNNING ： 运行中 - FINISHED：执行成功 - FAILED：执行失败

        :return: The status of this ListScriptResultsResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListScriptResultsResponse.

        执行状态。 - LAUNCHING ：提交中 - RUNNING ： 运行中 - FINISHED：执行成功 - FAILED：执行失败

        :param status: The status of this ListScriptResultsResponse.
        :type status: str
        """
        self._status = status

    @property
    def results(self):
        """Gets the results of this ListScriptResultsResponse.

        执行结果

        :return: The results of this ListScriptResultsResponse.
        :rtype: list[:class:`huaweicloudsdkdgc.v1.Result`]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this ListScriptResultsResponse.

        执行结果

        :param results: The results of this ListScriptResultsResponse.
        :type results: list[:class:`huaweicloudsdkdgc.v1.Result`]
        """
        self._results = results

    @property
    def message(self):
        """Gets the message of this ListScriptResultsResponse.

        执行失败消息

        :return: The message of this ListScriptResultsResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ListScriptResultsResponse.

        执行失败消息

        :param message: The message of this ListScriptResultsResponse.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, ListScriptResultsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
