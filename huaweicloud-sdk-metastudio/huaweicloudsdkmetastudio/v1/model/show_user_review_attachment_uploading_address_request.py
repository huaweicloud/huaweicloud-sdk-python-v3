# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowUserReviewAttachmentUploadingAddressRequest:

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
        'start_number': 'int',
        'end_number': 'int'
    }

    attribute_map = {
        'job_id': 'job_id',
        'start_number': 'start_number',
        'end_number': 'end_number'
    }

    def __init__(self, job_id=None, start_number=None, end_number=None):
        r"""ShowUserReviewAttachmentUploadingAddressRequest

        The model defined in huaweicloud sdk

        :param job_id: 任务id
        :type job_id: str
        :param start_number: 起始序号
        :type start_number: int
        :param end_number: 结束序号
        :type end_number: int
        """
        
        

        self._job_id = None
        self._start_number = None
        self._end_number = None
        self.discriminator = None

        self.job_id = job_id
        if start_number is not None:
            self.start_number = start_number
        if end_number is not None:
            self.end_number = end_number

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowUserReviewAttachmentUploadingAddressRequest.

        任务id

        :return: The job_id of this ShowUserReviewAttachmentUploadingAddressRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowUserReviewAttachmentUploadingAddressRequest.

        任务id

        :param job_id: The job_id of this ShowUserReviewAttachmentUploadingAddressRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def start_number(self):
        r"""Gets the start_number of this ShowUserReviewAttachmentUploadingAddressRequest.

        起始序号

        :return: The start_number of this ShowUserReviewAttachmentUploadingAddressRequest.
        :rtype: int
        """
        return self._start_number

    @start_number.setter
    def start_number(self, start_number):
        r"""Sets the start_number of this ShowUserReviewAttachmentUploadingAddressRequest.

        起始序号

        :param start_number: The start_number of this ShowUserReviewAttachmentUploadingAddressRequest.
        :type start_number: int
        """
        self._start_number = start_number

    @property
    def end_number(self):
        r"""Gets the end_number of this ShowUserReviewAttachmentUploadingAddressRequest.

        结束序号

        :return: The end_number of this ShowUserReviewAttachmentUploadingAddressRequest.
        :rtype: int
        """
        return self._end_number

    @end_number.setter
    def end_number(self, end_number):
        r"""Sets the end_number of this ShowUserReviewAttachmentUploadingAddressRequest.

        结束序号

        :param end_number: The end_number of this ShowUserReviewAttachmentUploadingAddressRequest.
        :type end_number: int
        """
        self._end_number = end_number

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
        if not isinstance(other, ShowUserReviewAttachmentUploadingAddressRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
