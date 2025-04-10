# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecordJob:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sequence': 'int',
        'deploy_type': 'str',
        'job_id': 'str',
        'job_info': 'RecordJobInfo'
    }

    attribute_map = {
        'sequence': 'sequence',
        'deploy_type': 'deploy_type',
        'job_id': 'job_id',
        'job_info': 'job_info'
    }

    def __init__(self, sequence=None, deploy_type=None, job_id=None, job_info=None):
        r"""RecordJob

        The model defined in huaweicloud sdk

        :param sequence: 
        :type sequence: int
        :param deploy_type: 
        :type deploy_type: str
        :param job_id: 
        :type job_id: str
        :param job_info: 
        :type job_info: :class:`huaweicloudsdkservicestage.v3.RecordJobInfo`
        """
        
        

        self._sequence = None
        self._deploy_type = None
        self._job_id = None
        self._job_info = None
        self.discriminator = None

        if sequence is not None:
            self.sequence = sequence
        if deploy_type is not None:
            self.deploy_type = deploy_type
        if job_id is not None:
            self.job_id = job_id
        if job_info is not None:
            self.job_info = job_info

    @property
    def sequence(self):
        r"""Gets the sequence of this RecordJob.

        :return: The sequence of this RecordJob.
        :rtype: int
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        r"""Sets the sequence of this RecordJob.

        :param sequence: The sequence of this RecordJob.
        :type sequence: int
        """
        self._sequence = sequence

    @property
    def deploy_type(self):
        r"""Gets the deploy_type of this RecordJob.

        :return: The deploy_type of this RecordJob.
        :rtype: str
        """
        return self._deploy_type

    @deploy_type.setter
    def deploy_type(self, deploy_type):
        r"""Sets the deploy_type of this RecordJob.

        :param deploy_type: The deploy_type of this RecordJob.
        :type deploy_type: str
        """
        self._deploy_type = deploy_type

    @property
    def job_id(self):
        r"""Gets the job_id of this RecordJob.

        :return: The job_id of this RecordJob.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this RecordJob.

        :param job_id: The job_id of this RecordJob.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_info(self):
        r"""Gets the job_info of this RecordJob.

        :return: The job_info of this RecordJob.
        :rtype: :class:`huaweicloudsdkservicestage.v3.RecordJobInfo`
        """
        return self._job_info

    @job_info.setter
    def job_info(self, job_info):
        r"""Sets the job_info of this RecordJob.

        :param job_info: The job_info of this RecordJob.
        :type job_info: :class:`huaweicloudsdkservicestage.v3.RecordJobInfo`
        """
        self._job_info = job_info

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
        if not isinstance(other, RecordJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
