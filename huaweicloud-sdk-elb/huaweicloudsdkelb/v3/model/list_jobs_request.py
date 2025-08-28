# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJobsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'page_reverse': 'bool',
        'job_id': 'str',
        'job_type': 'str',
        'status': 'str',
        'error_code': 'str',
        'resource_id': 'str',
        'begin_time': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'page_reverse': 'page_reverse',
        'job_id': 'job_id',
        'job_type': 'job_type',
        'status': 'status',
        'error_code': 'error_code',
        'resource_id': 'resource_id',
        'begin_time': 'begin_time'
    }

    def __init__(self, limit=None, marker=None, page_reverse=None, job_id=None, job_type=None, status=None, error_code=None, resource_id=None, begin_time=None):
        r"""ListJobsRequest

        The model defined in huaweicloud sdk

        :param limit: **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000
        :type limit: int
        :param marker: **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及
        :type marker: str
        :param page_reverse: **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse&#x3D;true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false
        :type page_reverse: bool
        :param job_id: **参数解释**：任务ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type job_id: str
        :param job_type: **参数解释**：任务类型。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type job_type: str
        :param status: **参数解释**：任务状态。  **约束限制**：不涉及  **取值范围**：INIT,RUNNING,FAIL,SUCCESS,ROLLBACKING,COMPLETE,ROLLBACK_FAIL,CANCEL  **默认取值**：不涉及
        :type status: str
        :param error_code: **参数解释**：任务的错误码。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type error_code: str
        :param resource_id: **参数解释**：资源ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type resource_id: str
        :param begin_time: **参数解释**：查询任务的开始时间大于等于传入时间的任务。格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type begin_time: str
        """
        
        

        self._limit = None
        self._marker = None
        self._page_reverse = None
        self._job_id = None
        self._job_type = None
        self._status = None
        self._error_code = None
        self._resource_id = None
        self._begin_time = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if job_id is not None:
            self.job_id = job_id
        if job_type is not None:
            self.job_type = job_type
        if status is not None:
            self.status = status
        if error_code is not None:
            self.error_code = error_code
        if resource_id is not None:
            self.resource_id = resource_id
        if begin_time is not None:
            self.begin_time = begin_time

    @property
    def limit(self):
        r"""Gets the limit of this ListJobsRequest.

        **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000

        :return: The limit of this ListJobsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListJobsRequest.

        **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000

        :param limit: The limit of this ListJobsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListJobsRequest.

        **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The marker of this ListJobsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListJobsRequest.

        **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及

        :param marker: The marker of this ListJobsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        r"""Gets the page_reverse of this ListJobsRequest.

        **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false

        :return: The page_reverse of this ListJobsRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        r"""Sets the page_reverse of this ListJobsRequest.

        **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false

        :param page_reverse: The page_reverse of this ListJobsRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def job_id(self):
        r"""Gets the job_id of this ListJobsRequest.

        **参数解释**：任务ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The job_id of this ListJobsRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ListJobsRequest.

        **参数解释**：任务ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param job_id: The job_id of this ListJobsRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_type(self):
        r"""Gets the job_type of this ListJobsRequest.

        **参数解释**：任务类型。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The job_type of this ListJobsRequest.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this ListJobsRequest.

        **参数解释**：任务类型。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param job_type: The job_type of this ListJobsRequest.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def status(self):
        r"""Gets the status of this ListJobsRequest.

        **参数解释**：任务状态。  **约束限制**：不涉及  **取值范围**：INIT,RUNNING,FAIL,SUCCESS,ROLLBACKING,COMPLETE,ROLLBACK_FAIL,CANCEL  **默认取值**：不涉及

        :return: The status of this ListJobsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListJobsRequest.

        **参数解释**：任务状态。  **约束限制**：不涉及  **取值范围**：INIT,RUNNING,FAIL,SUCCESS,ROLLBACKING,COMPLETE,ROLLBACK_FAIL,CANCEL  **默认取值**：不涉及

        :param status: The status of this ListJobsRequest.
        :type status: str
        """
        self._status = status

    @property
    def error_code(self):
        r"""Gets the error_code of this ListJobsRequest.

        **参数解释**：任务的错误码。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The error_code of this ListJobsRequest.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ListJobsRequest.

        **参数解释**：任务的错误码。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param error_code: The error_code of this ListJobsRequest.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ListJobsRequest.

        **参数解释**：资源ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The resource_id of this ListJobsRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ListJobsRequest.

        **参数解释**：资源ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param resource_id: The resource_id of this ListJobsRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ListJobsRequest.

        **参数解释**：查询任务的开始时间大于等于传入时间的任务。格式：yyyy-MM-dd'T'HH:mm:ss  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The begin_time of this ListJobsRequest.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ListJobsRequest.

        **参数解释**：查询任务的开始时间大于等于传入时间的任务。格式：yyyy-MM-dd'T'HH:mm:ss  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param begin_time: The begin_time of this ListJobsRequest.
        :type begin_time: str
        """
        self._begin_time = begin_time

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
        if not isinstance(other, ListJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
