# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunCodehubTemplateJobResponse(SdkResponse):

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
        'file_list': 'list[FileTreeNode]'
    }

    attribute_map = {
        'job_id': 'job_id',
        'file_list': 'file_list'
    }

    def __init__(self, job_id=None, file_list=None):
        r"""RunCodehubTemplateJobResponse

        The model defined in huaweicloud sdk

        :param job_id: 任务id。
        :type job_id: str
        :param file_list: 文件列表。
        :type file_list: list[:class:`huaweicloudsdkdevstar.v1.FileTreeNode`]
        """
        
        super(RunCodehubTemplateJobResponse, self).__init__()

        self._job_id = None
        self._file_list = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if file_list is not None:
            self.file_list = file_list

    @property
    def job_id(self):
        r"""Gets the job_id of this RunCodehubTemplateJobResponse.

        任务id。

        :return: The job_id of this RunCodehubTemplateJobResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this RunCodehubTemplateJobResponse.

        任务id。

        :param job_id: The job_id of this RunCodehubTemplateJobResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def file_list(self):
        r"""Gets the file_list of this RunCodehubTemplateJobResponse.

        文件列表。

        :return: The file_list of this RunCodehubTemplateJobResponse.
        :rtype: list[:class:`huaweicloudsdkdevstar.v1.FileTreeNode`]
        """
        return self._file_list

    @file_list.setter
    def file_list(self, file_list):
        r"""Sets the file_list of this RunCodehubTemplateJobResponse.

        文件列表。

        :param file_list: The file_list of this RunCodehubTemplateJobResponse.
        :type file_list: list[:class:`huaweicloudsdkdevstar.v1.FileTreeNode`]
        """
        self._file_list = file_list

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
        if not isinstance(other, RunCodehubTemplateJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
