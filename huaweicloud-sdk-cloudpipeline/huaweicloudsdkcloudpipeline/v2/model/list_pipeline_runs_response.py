# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPipelineRunsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'total': 'int',
        'pipeline_runs': 'list[ListPipelineRunsPagePipelineRuns]'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'total': 'total',
        'pipeline_runs': 'pipeline_runs'
    }

    def __init__(self, offset=None, limit=None, total=None, pipeline_runs=None):
        """ListPipelineRunsResponse

        The model defined in huaweicloud sdk

        :param offset: 起始偏移
        :type offset: int
        :param limit: 查询大小
        :type limit: int
        :param total: 总数
        :type total: int
        :param pipeline_runs: 流水线运行信息
        :type pipeline_runs: list[:class:`huaweicloudsdkcloudpipeline.v2.ListPipelineRunsPagePipelineRuns`]
        """
        
        super(ListPipelineRunsResponse, self).__init__()

        self._offset = None
        self._limit = None
        self._total = None
        self._pipeline_runs = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if total is not None:
            self.total = total
        if pipeline_runs is not None:
            self.pipeline_runs = pipeline_runs

    @property
    def offset(self):
        """Gets the offset of this ListPipelineRunsResponse.

        起始偏移

        :return: The offset of this ListPipelineRunsResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPipelineRunsResponse.

        起始偏移

        :param offset: The offset of this ListPipelineRunsResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListPipelineRunsResponse.

        查询大小

        :return: The limit of this ListPipelineRunsResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPipelineRunsResponse.

        查询大小

        :param limit: The limit of this ListPipelineRunsResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def total(self):
        """Gets the total of this ListPipelineRunsResponse.

        总数

        :return: The total of this ListPipelineRunsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListPipelineRunsResponse.

        总数

        :param total: The total of this ListPipelineRunsResponse.
        :type total: int
        """
        self._total = total

    @property
    def pipeline_runs(self):
        """Gets the pipeline_runs of this ListPipelineRunsResponse.

        流水线运行信息

        :return: The pipeline_runs of this ListPipelineRunsResponse.
        :rtype: list[:class:`huaweicloudsdkcloudpipeline.v2.ListPipelineRunsPagePipelineRuns`]
        """
        return self._pipeline_runs

    @pipeline_runs.setter
    def pipeline_runs(self, pipeline_runs):
        """Sets the pipeline_runs of this ListPipelineRunsResponse.

        流水线运行信息

        :param pipeline_runs: The pipeline_runs of this ListPipelineRunsResponse.
        :type pipeline_runs: list[:class:`huaweicloudsdkcloudpipeline.v2.ListPipelineRunsPagePipelineRuns`]
        """
        self._pipeline_runs = pipeline_runs

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
        if not isinstance(other, ListPipelineRunsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
