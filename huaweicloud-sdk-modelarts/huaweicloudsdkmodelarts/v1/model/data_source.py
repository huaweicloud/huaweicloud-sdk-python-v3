# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataSource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job': 'JobSummary',
        'nfs': 'NFSSummary'
    }

    attribute_map = {
        'job': 'job',
        'nfs': 'nfs'
    }

    def __init__(self, job=None, nfs=None):
        r"""DataSource

        The model defined in huaweicloud sdk

        :param job: 
        :type job: :class:`huaweicloudsdkmodelarts.v1.JobSummary`
        :param nfs: 
        :type nfs: :class:`huaweicloudsdkmodelarts.v1.NFSSummary`
        """
        
        

        self._job = None
        self._nfs = None
        self.discriminator = None

        self.job = job
        if nfs is not None:
            self.nfs = nfs

    @property
    def job(self):
        r"""Gets the job of this DataSource.

        :return: The job of this DataSource.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.JobSummary`
        """
        return self._job

    @job.setter
    def job(self, job):
        r"""Sets the job of this DataSource.

        :param job: The job of this DataSource.
        :type job: :class:`huaweicloudsdkmodelarts.v1.JobSummary`
        """
        self._job = job

    @property
    def nfs(self):
        r"""Gets the nfs of this DataSource.

        :return: The nfs of this DataSource.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.NFSSummary`
        """
        return self._nfs

    @nfs.setter
    def nfs(self, nfs):
        r"""Sets the nfs of this DataSource.

        :param nfs: The nfs of this DataSource.
        :type nfs: :class:`huaweicloudsdkmodelarts.v1.NFSSummary`
        """
        self._nfs = nfs

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
        if not isinstance(other, DataSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
