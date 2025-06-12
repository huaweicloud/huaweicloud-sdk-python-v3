# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJunitCoverageSummaryResultUnitSummaryList:

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
        'build_no': 'int',
        'stage_name': 'str',
        'root_id': 'str',
        'region': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'build_no': 'build_no',
        'stage_name': 'stage_name',
        'root_id': 'root_id',
        'region': 'region'
    }

    def __init__(self, job_id=None, build_no=None, stage_name=None, root_id=None, region=None):
        r"""ListJunitCoverageSummaryResultUnitSummaryList

        The model defined in huaweicloud sdk

        :param job_id: 任务ID
        :type job_id: str
        :param build_no: 构建任务的构建编号，从1开始，每次构建递增1
        :type build_no: int
        :param stage_name: stage名称
        :type stage_name: str
        :param root_id: 资源ID，下载覆盖率报告时使用
        :type root_id: str
        :param region: 租户所在region
        :type region: str
        """
        
        

        self._job_id = None
        self._build_no = None
        self._stage_name = None
        self._root_id = None
        self._region = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if build_no is not None:
            self.build_no = build_no
        if stage_name is not None:
            self.stage_name = stage_name
        if root_id is not None:
            self.root_id = root_id
        if region is not None:
            self.region = region

    @property
    def job_id(self):
        r"""Gets the job_id of this ListJunitCoverageSummaryResultUnitSummaryList.

        任务ID

        :return: The job_id of this ListJunitCoverageSummaryResultUnitSummaryList.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ListJunitCoverageSummaryResultUnitSummaryList.

        任务ID

        :param job_id: The job_id of this ListJunitCoverageSummaryResultUnitSummaryList.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def build_no(self):
        r"""Gets the build_no of this ListJunitCoverageSummaryResultUnitSummaryList.

        构建任务的构建编号，从1开始，每次构建递增1

        :return: The build_no of this ListJunitCoverageSummaryResultUnitSummaryList.
        :rtype: int
        """
        return self._build_no

    @build_no.setter
    def build_no(self, build_no):
        r"""Sets the build_no of this ListJunitCoverageSummaryResultUnitSummaryList.

        构建任务的构建编号，从1开始，每次构建递增1

        :param build_no: The build_no of this ListJunitCoverageSummaryResultUnitSummaryList.
        :type build_no: int
        """
        self._build_no = build_no

    @property
    def stage_name(self):
        r"""Gets the stage_name of this ListJunitCoverageSummaryResultUnitSummaryList.

        stage名称

        :return: The stage_name of this ListJunitCoverageSummaryResultUnitSummaryList.
        :rtype: str
        """
        return self._stage_name

    @stage_name.setter
    def stage_name(self, stage_name):
        r"""Sets the stage_name of this ListJunitCoverageSummaryResultUnitSummaryList.

        stage名称

        :param stage_name: The stage_name of this ListJunitCoverageSummaryResultUnitSummaryList.
        :type stage_name: str
        """
        self._stage_name = stage_name

    @property
    def root_id(self):
        r"""Gets the root_id of this ListJunitCoverageSummaryResultUnitSummaryList.

        资源ID，下载覆盖率报告时使用

        :return: The root_id of this ListJunitCoverageSummaryResultUnitSummaryList.
        :rtype: str
        """
        return self._root_id

    @root_id.setter
    def root_id(self, root_id):
        r"""Sets the root_id of this ListJunitCoverageSummaryResultUnitSummaryList.

        资源ID，下载覆盖率报告时使用

        :param root_id: The root_id of this ListJunitCoverageSummaryResultUnitSummaryList.
        :type root_id: str
        """
        self._root_id = root_id

    @property
    def region(self):
        r"""Gets the region of this ListJunitCoverageSummaryResultUnitSummaryList.

        租户所在region

        :return: The region of this ListJunitCoverageSummaryResultUnitSummaryList.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListJunitCoverageSummaryResultUnitSummaryList.

        租户所在region

        :param region: The region of this ListJunitCoverageSummaryResultUnitSummaryList.
        :type region: str
        """
        self._region = region

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
        if not isinstance(other, ListJunitCoverageSummaryResultUnitSummaryList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
