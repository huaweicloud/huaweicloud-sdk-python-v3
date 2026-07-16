# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAutoSearchParamsAnalysisRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'training_job_id': 'str'
    }

    attribute_map = {
        'training_job_id': 'training_job_id'
    }

    def __init__(self, training_job_id=None):
        r"""ShowAutoSearchParamsAnalysisRequest

        The model defined in huaweicloud sdk

        :param training_job_id: 训练作业ID。获取方法请参见[查询训练作业列表](ListTrainingJobs.xml)。
        :type training_job_id: str
        """
        
        

        self._training_job_id = None
        self.discriminator = None

        self.training_job_id = training_job_id

    @property
    def training_job_id(self):
        r"""Gets the training_job_id of this ShowAutoSearchParamsAnalysisRequest.

        训练作业ID。获取方法请参见[查询训练作业列表](ListTrainingJobs.xml)。

        :return: The training_job_id of this ShowAutoSearchParamsAnalysisRequest.
        :rtype: str
        """
        return self._training_job_id

    @training_job_id.setter
    def training_job_id(self, training_job_id):
        r"""Sets the training_job_id of this ShowAutoSearchParamsAnalysisRequest.

        训练作业ID。获取方法请参见[查询训练作业列表](ListTrainingJobs.xml)。

        :param training_job_id: The training_job_id of this ShowAutoSearchParamsAnalysisRequest.
        :type training_job_id: str
        """
        self._training_job_id = training_job_id

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
        if not isinstance(other, ShowAutoSearchParamsAnalysisRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
