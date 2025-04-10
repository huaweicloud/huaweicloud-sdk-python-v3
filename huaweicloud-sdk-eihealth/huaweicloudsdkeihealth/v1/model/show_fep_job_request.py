# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFepJobRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eihealth_project_id': 'str',
        'job_id': 'str'
    }

    attribute_map = {
        'eihealth_project_id': 'eihealth_project_id',
        'job_id': 'job_id'
    }

    def __init__(self, eihealth_project_id=None, job_id=None):
        r"""ShowFepJobRequest

        The model defined in huaweicloud sdk

        :param eihealth_project_id: 平台项目ID。
        :type eihealth_project_id: str
        :param job_id: 作业id
        :type job_id: str
        """
        
        

        self._eihealth_project_id = None
        self._job_id = None
        self.discriminator = None

        self.eihealth_project_id = eihealth_project_id
        self.job_id = job_id

    @property
    def eihealth_project_id(self):
        r"""Gets the eihealth_project_id of this ShowFepJobRequest.

        平台项目ID。

        :return: The eihealth_project_id of this ShowFepJobRequest.
        :rtype: str
        """
        return self._eihealth_project_id

    @eihealth_project_id.setter
    def eihealth_project_id(self, eihealth_project_id):
        r"""Sets the eihealth_project_id of this ShowFepJobRequest.

        平台项目ID。

        :param eihealth_project_id: The eihealth_project_id of this ShowFepJobRequest.
        :type eihealth_project_id: str
        """
        self._eihealth_project_id = eihealth_project_id

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowFepJobRequest.

        作业id

        :return: The job_id of this ShowFepJobRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowFepJobRequest.

        作业id

        :param job_id: The job_id of this ShowFepJobRequest.
        :type job_id: str
        """
        self._job_id = job_id

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
        if not isinstance(other, ShowFepJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
