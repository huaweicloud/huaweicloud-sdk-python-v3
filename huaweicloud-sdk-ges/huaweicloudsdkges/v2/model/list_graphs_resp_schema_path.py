# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGraphsRespSchemaPath:

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
        'path': 'str',
        'status': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'path': 'path',
        'status': 'status'
    }

    def __init__(self, job_id=None, path=None, status=None):
        r"""ListGraphsRespSchemaPath

        The model defined in huaweicloud sdk

        :param job_id: 导入OBS文件对应的jobId。
        :type job_id: str
        :param path: OBS存储路径，不包含OBS Endpoint。
        :type path: str
        :param status: OBS文件导入状态。  - success：完全导入成功 - partiallyFailed：部分失败 - failed：完全导入失败
        :type status: str
        """
        
        

        self._job_id = None
        self._path = None
        self._status = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if path is not None:
            self.path = path
        if status is not None:
            self.status = status

    @property
    def job_id(self):
        r"""Gets the job_id of this ListGraphsRespSchemaPath.

        导入OBS文件对应的jobId。

        :return: The job_id of this ListGraphsRespSchemaPath.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ListGraphsRespSchemaPath.

        导入OBS文件对应的jobId。

        :param job_id: The job_id of this ListGraphsRespSchemaPath.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def path(self):
        r"""Gets the path of this ListGraphsRespSchemaPath.

        OBS存储路径，不包含OBS Endpoint。

        :return: The path of this ListGraphsRespSchemaPath.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this ListGraphsRespSchemaPath.

        OBS存储路径，不包含OBS Endpoint。

        :param path: The path of this ListGraphsRespSchemaPath.
        :type path: str
        """
        self._path = path

    @property
    def status(self):
        r"""Gets the status of this ListGraphsRespSchemaPath.

        OBS文件导入状态。  - success：完全导入成功 - partiallyFailed：部分失败 - failed：完全导入失败

        :return: The status of this ListGraphsRespSchemaPath.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListGraphsRespSchemaPath.

        OBS文件导入状态。  - success：完全导入成功 - partiallyFailed：部分失败 - failed：完全导入失败

        :param status: The status of this ListGraphsRespSchemaPath.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ListGraphsRespSchemaPath):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
