# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachShareFilesystemResponseBody200Jobs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_id': 'str',
        'job_id': 'str'
    }

    attribute_map = {
        'server_id': 'server_id',
        'job_id': 'job_id'
    }

    def __init__(self, server_id=None, job_id=None):
        r"""AttachShareFilesystemResponseBody200Jobs

        The model defined in huaweicloud sdk

        :param server_id: 云手机服务器的唯一标识ID，云手机服务器相关任务包含此字段。
        :type server_id: str
        :param job_id: 任务的唯一标识。
        :type job_id: str
        """
        
        

        self._server_id = None
        self._job_id = None
        self.discriminator = None

        if server_id is not None:
            self.server_id = server_id
        if job_id is not None:
            self.job_id = job_id

    @property
    def server_id(self):
        r"""Gets the server_id of this AttachShareFilesystemResponseBody200Jobs.

        云手机服务器的唯一标识ID，云手机服务器相关任务包含此字段。

        :return: The server_id of this AttachShareFilesystemResponseBody200Jobs.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this AttachShareFilesystemResponseBody200Jobs.

        云手机服务器的唯一标识ID，云手机服务器相关任务包含此字段。

        :param server_id: The server_id of this AttachShareFilesystemResponseBody200Jobs.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def job_id(self):
        r"""Gets the job_id of this AttachShareFilesystemResponseBody200Jobs.

        任务的唯一标识。

        :return: The job_id of this AttachShareFilesystemResponseBody200Jobs.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this AttachShareFilesystemResponseBody200Jobs.

        任务的唯一标识。

        :param job_id: The job_id of this AttachShareFilesystemResponseBody200Jobs.
        :type job_id: str
        """
        self._job_id = job_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AttachShareFilesystemResponseBody200Jobs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
