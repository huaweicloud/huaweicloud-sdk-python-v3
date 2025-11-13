# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateShortJobResponse(SdkResponse):

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
        'data_uploading_url': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'data_uploading_url': 'data_uploading_url'
    }

    def __init__(self, job_id=None, data_uploading_url=None):
        r"""CreateShortJobResponse

        The model defined in huaweicloud sdk

        :param job_id: 任务id。
        :type job_id: str
        :param data_uploading_url: 上传训练数据的地址。训练数据需打包成zip文件后，上传至该url。 &gt; 通过该obs地址上传时，需设置content-type为application/zip。
        :type data_uploading_url: str
        """
        
        super().__init__()

        self._job_id = None
        self._data_uploading_url = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if data_uploading_url is not None:
            self.data_uploading_url = data_uploading_url

    @property
    def job_id(self):
        r"""Gets the job_id of this CreateShortJobResponse.

        任务id。

        :return: The job_id of this CreateShortJobResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this CreateShortJobResponse.

        任务id。

        :param job_id: The job_id of this CreateShortJobResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def data_uploading_url(self):
        r"""Gets the data_uploading_url of this CreateShortJobResponse.

        上传训练数据的地址。训练数据需打包成zip文件后，上传至该url。 > 通过该obs地址上传时，需设置content-type为application/zip。

        :return: The data_uploading_url of this CreateShortJobResponse.
        :rtype: str
        """
        return self._data_uploading_url

    @data_uploading_url.setter
    def data_uploading_url(self, data_uploading_url):
        r"""Sets the data_uploading_url of this CreateShortJobResponse.

        上传训练数据的地址。训练数据需打包成zip文件后，上传至该url。 > 通过该obs地址上传时，需设置content-type为application/zip。

        :param data_uploading_url: The data_uploading_url of this CreateShortJobResponse.
        :type data_uploading_url: str
        """
        self._data_uploading_url = data_uploading_url

    def to_dict(self):
        import warnings
        warnings.warn("CreateShortJobResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateShortJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
