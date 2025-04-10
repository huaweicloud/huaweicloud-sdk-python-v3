# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CdmRandomCreateAndStartJobJsonReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'jobs': 'list[Job]',
        'clusters': 'list[str]'
    }

    attribute_map = {
        'jobs': 'jobs',
        'clusters': 'clusters'
    }

    def __init__(self, jobs=None, clusters=None):
        r"""CdmRandomCreateAndStartJobJsonReq

        The model defined in huaweicloud sdk

        :param jobs: 作业列表，请参见jobs数据结构说明。
        :type jobs: list[:class:`huaweicloudsdkcdm.v1.Job`]
        :param clusters: CDM集群ID列表，系统会从里面随机选择一个开机状态的集群，在该集群中创建作业并执行作业。
        :type clusters: list[str]
        """
        
        

        self._jobs = None
        self._clusters = None
        self.discriminator = None

        self.jobs = jobs
        self.clusters = clusters

    @property
    def jobs(self):
        r"""Gets the jobs of this CdmRandomCreateAndStartJobJsonReq.

        作业列表，请参见jobs数据结构说明。

        :return: The jobs of this CdmRandomCreateAndStartJobJsonReq.
        :rtype: list[:class:`huaweicloudsdkcdm.v1.Job`]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        r"""Sets the jobs of this CdmRandomCreateAndStartJobJsonReq.

        作业列表，请参见jobs数据结构说明。

        :param jobs: The jobs of this CdmRandomCreateAndStartJobJsonReq.
        :type jobs: list[:class:`huaweicloudsdkcdm.v1.Job`]
        """
        self._jobs = jobs

    @property
    def clusters(self):
        r"""Gets the clusters of this CdmRandomCreateAndStartJobJsonReq.

        CDM集群ID列表，系统会从里面随机选择一个开机状态的集群，在该集群中创建作业并执行作业。

        :return: The clusters of this CdmRandomCreateAndStartJobJsonReq.
        :rtype: list[str]
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        r"""Sets the clusters of this CdmRandomCreateAndStartJobJsonReq.

        CDM集群ID列表，系统会从里面随机选择一个开机状态的集群，在该集群中创建作业并执行作业。

        :param clusters: The clusters of this CdmRandomCreateAndStartJobJsonReq.
        :type clusters: list[str]
        """
        self._clusters = clusters

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
        if not isinstance(other, CdmRandomCreateAndStartJobJsonReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
