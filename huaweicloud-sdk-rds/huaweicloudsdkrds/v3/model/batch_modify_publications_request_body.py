# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchModifyPublicationsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publication_ids': 'list[str]',
        'job_schedule': 'OperateUsedJobSchedule'
    }

    attribute_map = {
        'publication_ids': 'publication_ids',
        'job_schedule': 'job_schedule'
    }

    def __init__(self, publication_ids=None, job_schedule=None):
        r"""BatchModifyPublicationsRequestBody

        The model defined in huaweicloud sdk

        :param publication_ids: 修改的发布id列表。
        :type publication_ids: list[str]
        :param job_schedule: 
        :type job_schedule: :class:`huaweicloudsdkrds.v3.OperateUsedJobSchedule`
        """
        
        

        self._publication_ids = None
        self._job_schedule = None
        self.discriminator = None

        self.publication_ids = publication_ids
        self.job_schedule = job_schedule

    @property
    def publication_ids(self):
        r"""Gets the publication_ids of this BatchModifyPublicationsRequestBody.

        修改的发布id列表。

        :return: The publication_ids of this BatchModifyPublicationsRequestBody.
        :rtype: list[str]
        """
        return self._publication_ids

    @publication_ids.setter
    def publication_ids(self, publication_ids):
        r"""Sets the publication_ids of this BatchModifyPublicationsRequestBody.

        修改的发布id列表。

        :param publication_ids: The publication_ids of this BatchModifyPublicationsRequestBody.
        :type publication_ids: list[str]
        """
        self._publication_ids = publication_ids

    @property
    def job_schedule(self):
        r"""Gets the job_schedule of this BatchModifyPublicationsRequestBody.

        :return: The job_schedule of this BatchModifyPublicationsRequestBody.
        :rtype: :class:`huaweicloudsdkrds.v3.OperateUsedJobSchedule`
        """
        return self._job_schedule

    @job_schedule.setter
    def job_schedule(self, job_schedule):
        r"""Sets the job_schedule of this BatchModifyPublicationsRequestBody.

        :param job_schedule: The job_schedule of this BatchModifyPublicationsRequestBody.
        :type job_schedule: :class:`huaweicloudsdkrds.v3.OperateUsedJobSchedule`
        """
        self._job_schedule = job_schedule

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
        if not isinstance(other, BatchModifyPublicationsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
