# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchSearchMetricHitsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'workspace_id': 'str',
        'timespan': 'str',
        'cache': 'bool',
        'body': 'BatchSearchMetricHitsRequestBody'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'timespan': 'timespan',
        'cache': 'cache',
        'body': 'body'
    }

    def __init__(self, project_id=None, workspace_id=None, timespan=None, cache=None, body=None):
        r"""BatchSearchMetricHitsRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目ID
        :type project_id: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param timespan: 查询指标的时间范围，ISO8601格式，例如：2007-03-01T13:00:00Z/2008-05-11T15:30:00Z或2007-03-01T13:00:00Z/P1Y2M10DT2H30M或P1Y2M10DT2H30M/2008-05-11T15:30:00Z
        :type timespan: str
        :param cache: 是否启用缓存，默认true, 禁用缓存 false
        :type cache: bool
        :param body: Body of the BatchSearchMetricHitsRequest
        :type body: :class:`huaweicloudsdksecmaster.v2.BatchSearchMetricHitsRequestBody`
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._timespan = None
        self._cache = None
        self._body = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        if timespan is not None:
            self.timespan = timespan
        if cache is not None:
            self.cache = cache
        if body is not None:
            self.body = body

    @property
    def project_id(self):
        r"""Gets the project_id of this BatchSearchMetricHitsRequest.

        项目ID

        :return: The project_id of this BatchSearchMetricHitsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this BatchSearchMetricHitsRequest.

        项目ID

        :param project_id: The project_id of this BatchSearchMetricHitsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this BatchSearchMetricHitsRequest.

        工作空间ID

        :return: The workspace_id of this BatchSearchMetricHitsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this BatchSearchMetricHitsRequest.

        工作空间ID

        :param workspace_id: The workspace_id of this BatchSearchMetricHitsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def timespan(self):
        r"""Gets the timespan of this BatchSearchMetricHitsRequest.

        查询指标的时间范围，ISO8601格式，例如：2007-03-01T13:00:00Z/2008-05-11T15:30:00Z或2007-03-01T13:00:00Z/P1Y2M10DT2H30M或P1Y2M10DT2H30M/2008-05-11T15:30:00Z

        :return: The timespan of this BatchSearchMetricHitsRequest.
        :rtype: str
        """
        return self._timespan

    @timespan.setter
    def timespan(self, timespan):
        r"""Sets the timespan of this BatchSearchMetricHitsRequest.

        查询指标的时间范围，ISO8601格式，例如：2007-03-01T13:00:00Z/2008-05-11T15:30:00Z或2007-03-01T13:00:00Z/P1Y2M10DT2H30M或P1Y2M10DT2H30M/2008-05-11T15:30:00Z

        :param timespan: The timespan of this BatchSearchMetricHitsRequest.
        :type timespan: str
        """
        self._timespan = timespan

    @property
    def cache(self):
        r"""Gets the cache of this BatchSearchMetricHitsRequest.

        是否启用缓存，默认true, 禁用缓存 false

        :return: The cache of this BatchSearchMetricHitsRequest.
        :rtype: bool
        """
        return self._cache

    @cache.setter
    def cache(self, cache):
        r"""Sets the cache of this BatchSearchMetricHitsRequest.

        是否启用缓存，默认true, 禁用缓存 false

        :param cache: The cache of this BatchSearchMetricHitsRequest.
        :type cache: bool
        """
        self._cache = cache

    @property
    def body(self):
        r"""Gets the body of this BatchSearchMetricHitsRequest.

        :return: The body of this BatchSearchMetricHitsRequest.
        :rtype: :class:`huaweicloudsdksecmaster.v2.BatchSearchMetricHitsRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this BatchSearchMetricHitsRequest.

        :param body: The body of this BatchSearchMetricHitsRequest.
        :type body: :class:`huaweicloudsdksecmaster.v2.BatchSearchMetricHitsRequestBody`
        """
        self._body = body

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
        if not isinstance(other, BatchSearchMetricHitsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
