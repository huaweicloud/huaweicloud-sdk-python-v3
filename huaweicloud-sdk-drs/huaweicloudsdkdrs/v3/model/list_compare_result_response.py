# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCompareResultResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'object_level_compare_results': 'ObjectCompareResult',
        'line_compare_results': 'LineCompareResult',
        'content_compare_results': 'ContentCompareResult',
        'compare_task_list_results': 'CompareTaskListResult',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'object_level_compare_results': 'object_level_compare_results',
        'line_compare_results': 'line_compare_results',
        'content_compare_results': 'content_compare_results',
        'compare_task_list_results': 'compare_task_list_results',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, job_id=None, object_level_compare_results=None, line_compare_results=None, content_compare_results=None, compare_task_list_results=None, error_code=None, error_msg=None):
        """ListCompareResultResponse

        The model defined in huaweicloud sdk

        :param job_id: 任务id。
        :type job_id: str
        :param object_level_compare_results: 
        :type object_level_compare_results: :class:`huaweicloudsdkdrs.v3.ObjectCompareResult`
        :param line_compare_results: 
        :type line_compare_results: :class:`huaweicloudsdkdrs.v3.LineCompareResult`
        :param content_compare_results: 
        :type content_compare_results: :class:`huaweicloudsdkdrs.v3.ContentCompareResult`
        :param compare_task_list_results: 
        :type compare_task_list_results: :class:`huaweicloudsdkdrs.v3.CompareTaskListResult`
        :param error_code: 错误码。
        :type error_code: str
        :param error_msg: 错误信息。
        :type error_msg: str
        """
        
        super(ListCompareResultResponse, self).__init__()

        self._job_id = None
        self._object_level_compare_results = None
        self._line_compare_results = None
        self._content_compare_results = None
        self._compare_task_list_results = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if object_level_compare_results is not None:
            self.object_level_compare_results = object_level_compare_results
        if line_compare_results is not None:
            self.line_compare_results = line_compare_results
        if content_compare_results is not None:
            self.content_compare_results = content_compare_results
        if compare_task_list_results is not None:
            self.compare_task_list_results = compare_task_list_results
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def job_id(self):
        """Gets the job_id of this ListCompareResultResponse.

        任务id。

        :return: The job_id of this ListCompareResultResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ListCompareResultResponse.

        任务id。

        :param job_id: The job_id of this ListCompareResultResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def object_level_compare_results(self):
        """Gets the object_level_compare_results of this ListCompareResultResponse.


        :return: The object_level_compare_results of this ListCompareResultResponse.
        :rtype: :class:`huaweicloudsdkdrs.v3.ObjectCompareResult`
        """
        return self._object_level_compare_results

    @object_level_compare_results.setter
    def object_level_compare_results(self, object_level_compare_results):
        """Sets the object_level_compare_results of this ListCompareResultResponse.


        :param object_level_compare_results: The object_level_compare_results of this ListCompareResultResponse.
        :type object_level_compare_results: :class:`huaweicloudsdkdrs.v3.ObjectCompareResult`
        """
        self._object_level_compare_results = object_level_compare_results

    @property
    def line_compare_results(self):
        """Gets the line_compare_results of this ListCompareResultResponse.


        :return: The line_compare_results of this ListCompareResultResponse.
        :rtype: :class:`huaweicloudsdkdrs.v3.LineCompareResult`
        """
        return self._line_compare_results

    @line_compare_results.setter
    def line_compare_results(self, line_compare_results):
        """Sets the line_compare_results of this ListCompareResultResponse.


        :param line_compare_results: The line_compare_results of this ListCompareResultResponse.
        :type line_compare_results: :class:`huaweicloudsdkdrs.v3.LineCompareResult`
        """
        self._line_compare_results = line_compare_results

    @property
    def content_compare_results(self):
        """Gets the content_compare_results of this ListCompareResultResponse.


        :return: The content_compare_results of this ListCompareResultResponse.
        :rtype: :class:`huaweicloudsdkdrs.v3.ContentCompareResult`
        """
        return self._content_compare_results

    @content_compare_results.setter
    def content_compare_results(self, content_compare_results):
        """Sets the content_compare_results of this ListCompareResultResponse.


        :param content_compare_results: The content_compare_results of this ListCompareResultResponse.
        :type content_compare_results: :class:`huaweicloudsdkdrs.v3.ContentCompareResult`
        """
        self._content_compare_results = content_compare_results

    @property
    def compare_task_list_results(self):
        """Gets the compare_task_list_results of this ListCompareResultResponse.


        :return: The compare_task_list_results of this ListCompareResultResponse.
        :rtype: :class:`huaweicloudsdkdrs.v3.CompareTaskListResult`
        """
        return self._compare_task_list_results

    @compare_task_list_results.setter
    def compare_task_list_results(self, compare_task_list_results):
        """Sets the compare_task_list_results of this ListCompareResultResponse.


        :param compare_task_list_results: The compare_task_list_results of this ListCompareResultResponse.
        :type compare_task_list_results: :class:`huaweicloudsdkdrs.v3.CompareTaskListResult`
        """
        self._compare_task_list_results = compare_task_list_results

    @property
    def error_code(self):
        """Gets the error_code of this ListCompareResultResponse.

        错误码。

        :return: The error_code of this ListCompareResultResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ListCompareResultResponse.

        错误码。

        :param error_code: The error_code of this ListCompareResultResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this ListCompareResultResponse.

        错误信息。

        :return: The error_msg of this ListCompareResultResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this ListCompareResultResponse.

        错误信息。

        :param error_msg: The error_msg of this ListCompareResultResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, ListCompareResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
