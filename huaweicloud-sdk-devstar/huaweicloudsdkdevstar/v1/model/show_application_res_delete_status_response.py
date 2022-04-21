# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowApplicationResDeleteStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'repo_status': 'str',
        'pipeline_status': 'list[PipelineDeleteStatus]'
    }

    attribute_map = {
        'repo_status': 'repo_status',
        'pipeline_status': 'pipeline_status'
    }

    def __init__(self, repo_status=None, pipeline_status=None):
        """ShowApplicationResDeleteStatusResponse

        The model defined in huaweicloud sdk

        :param repo_status: 代码仓删除状态,deleted:删除成功,failed:删除失败,going:正在删除中
        :type repo_status: str
        :param pipeline_status: 流水线删除状态
        :type pipeline_status: list[:class:`huaweicloudsdkdevstar.v1.PipelineDeleteStatus`]
        """
        
        super(ShowApplicationResDeleteStatusResponse, self).__init__()

        self._repo_status = None
        self._pipeline_status = None
        self.discriminator = None

        if repo_status is not None:
            self.repo_status = repo_status
        if pipeline_status is not None:
            self.pipeline_status = pipeline_status

    @property
    def repo_status(self):
        """Gets the repo_status of this ShowApplicationResDeleteStatusResponse.

        代码仓删除状态,deleted:删除成功,failed:删除失败,going:正在删除中

        :return: The repo_status of this ShowApplicationResDeleteStatusResponse.
        :rtype: str
        """
        return self._repo_status

    @repo_status.setter
    def repo_status(self, repo_status):
        """Sets the repo_status of this ShowApplicationResDeleteStatusResponse.

        代码仓删除状态,deleted:删除成功,failed:删除失败,going:正在删除中

        :param repo_status: The repo_status of this ShowApplicationResDeleteStatusResponse.
        :type repo_status: str
        """
        self._repo_status = repo_status

    @property
    def pipeline_status(self):
        """Gets the pipeline_status of this ShowApplicationResDeleteStatusResponse.

        流水线删除状态

        :return: The pipeline_status of this ShowApplicationResDeleteStatusResponse.
        :rtype: list[:class:`huaweicloudsdkdevstar.v1.PipelineDeleteStatus`]
        """
        return self._pipeline_status

    @pipeline_status.setter
    def pipeline_status(self, pipeline_status):
        """Sets the pipeline_status of this ShowApplicationResDeleteStatusResponse.

        流水线删除状态

        :param pipeline_status: The pipeline_status of this ShowApplicationResDeleteStatusResponse.
        :type pipeline_status: list[:class:`huaweicloudsdkdevstar.v1.PipelineDeleteStatus`]
        """
        self._pipeline_status = pipeline_status

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
        if not isinstance(other, ShowApplicationResDeleteStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
