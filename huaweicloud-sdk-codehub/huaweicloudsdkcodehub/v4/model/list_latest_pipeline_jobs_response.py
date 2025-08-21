# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLatestPipelineJobsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'status': 'str',
        'stages': 'list[PipelineStageJobDto]'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'stages': 'stages'
    }

    def __init__(self, id=None, status=None, stages=None):
        r"""ListLatestPipelineJobsResponse

        The model defined in huaweicloud sdk

        :param id: 流水线ID
        :type id: int
        :param status: 流水线状态，pending为排队，running为运行中，success为成功，failed为失败，canceled为取消，skipped为跳过，timedout为超时
        :type status: str
        :param stages: 
        :type stages: list[:class:`huaweicloudsdkcodehub.v4.PipelineStageJobDto`]
        """
        
        super(ListLatestPipelineJobsResponse, self).__init__()

        self._id = None
        self._status = None
        self._stages = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if stages is not None:
            self.stages = stages

    @property
    def id(self):
        r"""Gets the id of this ListLatestPipelineJobsResponse.

        流水线ID

        :return: The id of this ListLatestPipelineJobsResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListLatestPipelineJobsResponse.

        流水线ID

        :param id: The id of this ListLatestPipelineJobsResponse.
        :type id: int
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this ListLatestPipelineJobsResponse.

        流水线状态，pending为排队，running为运行中，success为成功，failed为失败，canceled为取消，skipped为跳过，timedout为超时

        :return: The status of this ListLatestPipelineJobsResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListLatestPipelineJobsResponse.

        流水线状态，pending为排队，running为运行中，success为成功，failed为失败，canceled为取消，skipped为跳过，timedout为超时

        :param status: The status of this ListLatestPipelineJobsResponse.
        :type status: str
        """
        self._status = status

    @property
    def stages(self):
        r"""Gets the stages of this ListLatestPipelineJobsResponse.

        :return: The stages of this ListLatestPipelineJobsResponse.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.PipelineStageJobDto`]
        """
        return self._stages

    @stages.setter
    def stages(self, stages):
        r"""Sets the stages of this ListLatestPipelineJobsResponse.

        :param stages: The stages of this ListLatestPipelineJobsResponse.
        :type stages: list[:class:`huaweicloudsdkcodehub.v4.PipelineStageJobDto`]
        """
        self._stages = stages

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
        if not isinstance(other, ListLatestPipelineJobsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
