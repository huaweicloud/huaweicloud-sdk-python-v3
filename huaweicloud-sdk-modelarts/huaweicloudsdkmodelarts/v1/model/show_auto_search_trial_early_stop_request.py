# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAutoSearchTrialEarlyStopRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'training_job_id': 'str',
        'trial_id': 'str'
    }

    attribute_map = {
        'training_job_id': 'training_job_id',
        'trial_id': 'trial_id'
    }

    def __init__(self, training_job_id=None, trial_id=None):
        r"""ShowAutoSearchTrialEarlyStopRequest

        The model defined in huaweicloud sdk

        :param training_job_id: 训练作业ID。获取方法请参见[查询训练作业列表](ListTrainingJobs.xml)。
        :type training_job_id: str
        :param trial_id: 超参搜索的trial_id。
        :type trial_id: str
        """
        
        

        self._training_job_id = None
        self._trial_id = None
        self.discriminator = None

        self.training_job_id = training_job_id
        self.trial_id = trial_id

    @property
    def training_job_id(self):
        r"""Gets the training_job_id of this ShowAutoSearchTrialEarlyStopRequest.

        训练作业ID。获取方法请参见[查询训练作业列表](ListTrainingJobs.xml)。

        :return: The training_job_id of this ShowAutoSearchTrialEarlyStopRequest.
        :rtype: str
        """
        return self._training_job_id

    @training_job_id.setter
    def training_job_id(self, training_job_id):
        r"""Sets the training_job_id of this ShowAutoSearchTrialEarlyStopRequest.

        训练作业ID。获取方法请参见[查询训练作业列表](ListTrainingJobs.xml)。

        :param training_job_id: The training_job_id of this ShowAutoSearchTrialEarlyStopRequest.
        :type training_job_id: str
        """
        self._training_job_id = training_job_id

    @property
    def trial_id(self):
        r"""Gets the trial_id of this ShowAutoSearchTrialEarlyStopRequest.

        超参搜索的trial_id。

        :return: The trial_id of this ShowAutoSearchTrialEarlyStopRequest.
        :rtype: str
        """
        return self._trial_id

    @trial_id.setter
    def trial_id(self, trial_id):
        r"""Sets the trial_id of this ShowAutoSearchTrialEarlyStopRequest.

        超参搜索的trial_id。

        :param trial_id: The trial_id of this ShowAutoSearchTrialEarlyStopRequest.
        :type trial_id: str
        """
        self._trial_id = trial_id

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
        if not isinstance(other, ShowAutoSearchTrialEarlyStopRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
