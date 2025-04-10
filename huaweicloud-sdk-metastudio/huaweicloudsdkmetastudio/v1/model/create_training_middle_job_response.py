# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTrainingMiddleJobResponse(SdkResponse):

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
        'training_data_uploading_url': 'str',
        'segment_uploading_url': 'CreateTrainingJobRspSegmentUploadingUrl',
        'authorization_letter_uploading_url': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'training_data_uploading_url': 'training_data_uploading_url',
        'segment_uploading_url': 'segment_uploading_url',
        'authorization_letter_uploading_url': 'authorization_letter_uploading_url'
    }

    def __init__(self, job_id=None, training_data_uploading_url=None, segment_uploading_url=None, authorization_letter_uploading_url=None):
        r"""CreateTrainingMiddleJobResponse

        The model defined in huaweicloud sdk

        :param job_id: 任务id。
        :type job_id: str
        :param training_data_uploading_url: 上传训练数据的地址。训练数据需打包成zip文件后，上传至该url。  create_type取值为package时设置。 &gt; 通过该obs地址上传时，需设置content-type为application/zip。
        :type training_data_uploading_url: str
        :param segment_uploading_url: 
        :type segment_uploading_url: :class:`huaweicloudsdkmetastudio.v1.CreateTrainingJobRspSegmentUploadingUrl`
        :param authorization_letter_uploading_url: 授权书的上传地址。
        :type authorization_letter_uploading_url: str
        """
        
        super(CreateTrainingMiddleJobResponse, self).__init__()

        self._job_id = None
        self._training_data_uploading_url = None
        self._segment_uploading_url = None
        self._authorization_letter_uploading_url = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if training_data_uploading_url is not None:
            self.training_data_uploading_url = training_data_uploading_url
        if segment_uploading_url is not None:
            self.segment_uploading_url = segment_uploading_url
        if authorization_letter_uploading_url is not None:
            self.authorization_letter_uploading_url = authorization_letter_uploading_url

    @property
    def job_id(self):
        r"""Gets the job_id of this CreateTrainingMiddleJobResponse.

        任务id。

        :return: The job_id of this CreateTrainingMiddleJobResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this CreateTrainingMiddleJobResponse.

        任务id。

        :param job_id: The job_id of this CreateTrainingMiddleJobResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def training_data_uploading_url(self):
        r"""Gets the training_data_uploading_url of this CreateTrainingMiddleJobResponse.

        上传训练数据的地址。训练数据需打包成zip文件后，上传至该url。  create_type取值为package时设置。 > 通过该obs地址上传时，需设置content-type为application/zip。

        :return: The training_data_uploading_url of this CreateTrainingMiddleJobResponse.
        :rtype: str
        """
        return self._training_data_uploading_url

    @training_data_uploading_url.setter
    def training_data_uploading_url(self, training_data_uploading_url):
        r"""Sets the training_data_uploading_url of this CreateTrainingMiddleJobResponse.

        上传训练数据的地址。训练数据需打包成zip文件后，上传至该url。  create_type取值为package时设置。 > 通过该obs地址上传时，需设置content-type为application/zip。

        :param training_data_uploading_url: The training_data_uploading_url of this CreateTrainingMiddleJobResponse.
        :type training_data_uploading_url: str
        """
        self._training_data_uploading_url = training_data_uploading_url

    @property
    def segment_uploading_url(self):
        r"""Gets the segment_uploading_url of this CreateTrainingMiddleJobResponse.

        :return: The segment_uploading_url of this CreateTrainingMiddleJobResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateTrainingJobRspSegmentUploadingUrl`
        """
        return self._segment_uploading_url

    @segment_uploading_url.setter
    def segment_uploading_url(self, segment_uploading_url):
        r"""Sets the segment_uploading_url of this CreateTrainingMiddleJobResponse.

        :param segment_uploading_url: The segment_uploading_url of this CreateTrainingMiddleJobResponse.
        :type segment_uploading_url: :class:`huaweicloudsdkmetastudio.v1.CreateTrainingJobRspSegmentUploadingUrl`
        """
        self._segment_uploading_url = segment_uploading_url

    @property
    def authorization_letter_uploading_url(self):
        r"""Gets the authorization_letter_uploading_url of this CreateTrainingMiddleJobResponse.

        授权书的上传地址。

        :return: The authorization_letter_uploading_url of this CreateTrainingMiddleJobResponse.
        :rtype: str
        """
        return self._authorization_letter_uploading_url

    @authorization_letter_uploading_url.setter
    def authorization_letter_uploading_url(self, authorization_letter_uploading_url):
        r"""Sets the authorization_letter_uploading_url of this CreateTrainingMiddleJobResponse.

        授权书的上传地址。

        :param authorization_letter_uploading_url: The authorization_letter_uploading_url of this CreateTrainingMiddleJobResponse.
        :type authorization_letter_uploading_url: str
        """
        self._authorization_letter_uploading_url = authorization_letter_uploading_url

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
        if not isinstance(other, CreateTrainingMiddleJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
