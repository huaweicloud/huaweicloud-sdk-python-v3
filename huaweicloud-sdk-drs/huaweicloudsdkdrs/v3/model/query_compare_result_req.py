# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryCompareResultReq:

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
        'object_level_compare_id': 'str',
        'line_compare_id': 'str',
        'content_compare_id': 'str',
        'current_page': 'int',
        'per_page': 'int'
    }

    attribute_map = {
        'job_id': 'job_id',
        'object_level_compare_id': 'object_level_compare_id',
        'line_compare_id': 'line_compare_id',
        'content_compare_id': 'content_compare_id',
        'current_page': 'current_page',
        'per_page': 'per_page'
    }

    def __init__(self, job_id=None, object_level_compare_id=None, line_compare_id=None, content_compare_id=None, current_page=None, per_page=None):
        """QueryCompareResultReq

        The model defined in huaweicloud sdk

        :param job_id: 任务id。
        :type job_id: str
        :param object_level_compare_id: 请求查询结果的对象级对比任务id。
        :type object_level_compare_id: str
        :param line_compare_id: 请求查询结果的行对比任务id。
        :type line_compare_id: str
        :param content_compare_id: 请求查询结果的内容对比任务id。
        :type content_compare_id: str
        :param current_page: 分页查询的当前页码，对查询对比任务的结果生效。
        :type current_page: int
        :param per_page: 分页查询的每页个数，对查询对比任务的结果生效。
        :type per_page: int
        """
        
        

        self._job_id = None
        self._object_level_compare_id = None
        self._line_compare_id = None
        self._content_compare_id = None
        self._current_page = None
        self._per_page = None
        self.discriminator = None

        self.job_id = job_id
        if object_level_compare_id is not None:
            self.object_level_compare_id = object_level_compare_id
        if line_compare_id is not None:
            self.line_compare_id = line_compare_id
        if content_compare_id is not None:
            self.content_compare_id = content_compare_id
        self.current_page = current_page
        self.per_page = per_page

    @property
    def job_id(self):
        """Gets the job_id of this QueryCompareResultReq.

        任务id。

        :return: The job_id of this QueryCompareResultReq.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this QueryCompareResultReq.

        任务id。

        :param job_id: The job_id of this QueryCompareResultReq.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def object_level_compare_id(self):
        """Gets the object_level_compare_id of this QueryCompareResultReq.

        请求查询结果的对象级对比任务id。

        :return: The object_level_compare_id of this QueryCompareResultReq.
        :rtype: str
        """
        return self._object_level_compare_id

    @object_level_compare_id.setter
    def object_level_compare_id(self, object_level_compare_id):
        """Sets the object_level_compare_id of this QueryCompareResultReq.

        请求查询结果的对象级对比任务id。

        :param object_level_compare_id: The object_level_compare_id of this QueryCompareResultReq.
        :type object_level_compare_id: str
        """
        self._object_level_compare_id = object_level_compare_id

    @property
    def line_compare_id(self):
        """Gets the line_compare_id of this QueryCompareResultReq.

        请求查询结果的行对比任务id。

        :return: The line_compare_id of this QueryCompareResultReq.
        :rtype: str
        """
        return self._line_compare_id

    @line_compare_id.setter
    def line_compare_id(self, line_compare_id):
        """Sets the line_compare_id of this QueryCompareResultReq.

        请求查询结果的行对比任务id。

        :param line_compare_id: The line_compare_id of this QueryCompareResultReq.
        :type line_compare_id: str
        """
        self._line_compare_id = line_compare_id

    @property
    def content_compare_id(self):
        """Gets the content_compare_id of this QueryCompareResultReq.

        请求查询结果的内容对比任务id。

        :return: The content_compare_id of this QueryCompareResultReq.
        :rtype: str
        """
        return self._content_compare_id

    @content_compare_id.setter
    def content_compare_id(self, content_compare_id):
        """Sets the content_compare_id of this QueryCompareResultReq.

        请求查询结果的内容对比任务id。

        :param content_compare_id: The content_compare_id of this QueryCompareResultReq.
        :type content_compare_id: str
        """
        self._content_compare_id = content_compare_id

    @property
    def current_page(self):
        """Gets the current_page of this QueryCompareResultReq.

        分页查询的当前页码，对查询对比任务的结果生效。

        :return: The current_page of this QueryCompareResultReq.
        :rtype: int
        """
        return self._current_page

    @current_page.setter
    def current_page(self, current_page):
        """Sets the current_page of this QueryCompareResultReq.

        分页查询的当前页码，对查询对比任务的结果生效。

        :param current_page: The current_page of this QueryCompareResultReq.
        :type current_page: int
        """
        self._current_page = current_page

    @property
    def per_page(self):
        """Gets the per_page of this QueryCompareResultReq.

        分页查询的每页个数，对查询对比任务的结果生效。

        :return: The per_page of this QueryCompareResultReq.
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        """Sets the per_page of this QueryCompareResultReq.

        分页查询的每页个数，对查询对比任务的结果生效。

        :param per_page: The per_page of this QueryCompareResultReq.
        :type per_page: int
        """
        self._per_page = per_page

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
        if not isinstance(other, QueryCompareResultReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
