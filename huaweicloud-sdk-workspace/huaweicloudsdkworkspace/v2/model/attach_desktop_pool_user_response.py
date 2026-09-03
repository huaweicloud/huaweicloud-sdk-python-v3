# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachDesktopPoolUserResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'job_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'job_id': 'job_id'
    }

    def __init__(self, type=None, job_id=None):
        r"""AttachDesktopPoolUserResponse

        The model defined in huaweicloud sdk

        :param type: CREATING：桌面创建中；WAITING：动态池排队等待；EXCEEDED：静态池已达最大值；ASSIGNING：有空闲桌面，分配中；RESETTING 重置中。
        :type type: str
        :param job_id: 任务ID。
        :type job_id: str
        """
        
        super().__init__()

        self._type = None
        self._job_id = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if job_id is not None:
            self.job_id = job_id

    @property
    def type(self):
        r"""Gets the type of this AttachDesktopPoolUserResponse.

        CREATING：桌面创建中；WAITING：动态池排队等待；EXCEEDED：静态池已达最大值；ASSIGNING：有空闲桌面，分配中；RESETTING 重置中。

        :return: The type of this AttachDesktopPoolUserResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AttachDesktopPoolUserResponse.

        CREATING：桌面创建中；WAITING：动态池排队等待；EXCEEDED：静态池已达最大值；ASSIGNING：有空闲桌面，分配中；RESETTING 重置中。

        :param type: The type of this AttachDesktopPoolUserResponse.
        :type type: str
        """
        self._type = type

    @property
    def job_id(self):
        r"""Gets the job_id of this AttachDesktopPoolUserResponse.

        任务ID。

        :return: The job_id of this AttachDesktopPoolUserResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this AttachDesktopPoolUserResponse.

        任务ID。

        :param job_id: The job_id of this AttachDesktopPoolUserResponse.
        :type job_id: str
        """
        self._job_id = job_id

    def to_dict(self):
        import warnings
        warnings.warn("AttachDesktopPoolUserResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, AttachDesktopPoolUserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
