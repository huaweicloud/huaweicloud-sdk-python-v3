# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowResourceCopiesSummaryResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eps_id': 'str',
        'region_id': 'str',
        'resource_type': 'str',
        'copy_type': 'str',
        'total_copy_counts': 'int',
        'completed_copy_counts': 'int',
        'failed_copy_counts': 'int',
        'summary': 'list[GetResourceCopySummaryResponseSummary]'
    }

    attribute_map = {
        'eps_id': 'eps_id',
        'region_id': 'region_id',
        'resource_type': 'resource_type',
        'copy_type': 'copy_type',
        'total_copy_counts': 'total_copy_counts',
        'completed_copy_counts': 'completed_copy_counts',
        'failed_copy_counts': 'failed_copy_counts',
        'summary': 'summary'
    }

    def __init__(self, eps_id=None, region_id=None, resource_type=None, copy_type=None, total_copy_counts=None, completed_copy_counts=None, failed_copy_counts=None, summary=None):
        r"""ShowResourceCopiesSummaryResponse

        The model defined in huaweicloud sdk

        :param eps_id: 企业项目ID
        :type eps_id: str
        :param region_id: 区域ID
        :type region_id: str
        :param resource_type: 资源类型：Server-云服务器，Volume-云硬盘，Sfs-Turbo-高性能文件存储，Workspace-云桌面，MySQL-MySQL，PostgreSQL-PostgreSQL，SQLServer-SQLServer，MariaDB-MariaDB，GaussDB-GaussDB
        :type resource_type: str
        :param copy_type: 副本类型
        :type copy_type: str
        :param total_copy_counts: 总副本数
        :type total_copy_counts: int
        :param completed_copy_counts: 完成的备份总数, key -&gt; ResourceCopyStatisticsKeyEnum.COMPLETED.getValue()
        :type completed_copy_counts: int
        :param failed_copy_counts: 失败的备份总数, key -&gt; ResourceCopyStatisticsKeyEnum.FAILED.getValue()
        :type failed_copy_counts: int
        :param summary: 统计信息
        :type summary: list[:class:`huaweicloudsdkbcc.v1.GetResourceCopySummaryResponseSummary`]
        """
        
        super().__init__()

        self._eps_id = None
        self._region_id = None
        self._resource_type = None
        self._copy_type = None
        self._total_copy_counts = None
        self._completed_copy_counts = None
        self._failed_copy_counts = None
        self._summary = None
        self.discriminator = None

        if eps_id is not None:
            self.eps_id = eps_id
        if region_id is not None:
            self.region_id = region_id
        if resource_type is not None:
            self.resource_type = resource_type
        if copy_type is not None:
            self.copy_type = copy_type
        if total_copy_counts is not None:
            self.total_copy_counts = total_copy_counts
        if completed_copy_counts is not None:
            self.completed_copy_counts = completed_copy_counts
        if failed_copy_counts is not None:
            self.failed_copy_counts = failed_copy_counts
        if summary is not None:
            self.summary = summary

    @property
    def eps_id(self):
        r"""Gets the eps_id of this ShowResourceCopiesSummaryResponse.

        企业项目ID

        :return: The eps_id of this ShowResourceCopiesSummaryResponse.
        :rtype: str
        """
        return self._eps_id

    @eps_id.setter
    def eps_id(self, eps_id):
        r"""Sets the eps_id of this ShowResourceCopiesSummaryResponse.

        企业项目ID

        :param eps_id: The eps_id of this ShowResourceCopiesSummaryResponse.
        :type eps_id: str
        """
        self._eps_id = eps_id

    @property
    def region_id(self):
        r"""Gets the region_id of this ShowResourceCopiesSummaryResponse.

        区域ID

        :return: The region_id of this ShowResourceCopiesSummaryResponse.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ShowResourceCopiesSummaryResponse.

        区域ID

        :param region_id: The region_id of this ShowResourceCopiesSummaryResponse.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ShowResourceCopiesSummaryResponse.

        资源类型：Server-云服务器，Volume-云硬盘，Sfs-Turbo-高性能文件存储，Workspace-云桌面，MySQL-MySQL，PostgreSQL-PostgreSQL，SQLServer-SQLServer，MariaDB-MariaDB，GaussDB-GaussDB

        :return: The resource_type of this ShowResourceCopiesSummaryResponse.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ShowResourceCopiesSummaryResponse.

        资源类型：Server-云服务器，Volume-云硬盘，Sfs-Turbo-高性能文件存储，Workspace-云桌面，MySQL-MySQL，PostgreSQL-PostgreSQL，SQLServer-SQLServer，MariaDB-MariaDB，GaussDB-GaussDB

        :param resource_type: The resource_type of this ShowResourceCopiesSummaryResponse.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def copy_type(self):
        r"""Gets the copy_type of this ShowResourceCopiesSummaryResponse.

        副本类型

        :return: The copy_type of this ShowResourceCopiesSummaryResponse.
        :rtype: str
        """
        return self._copy_type

    @copy_type.setter
    def copy_type(self, copy_type):
        r"""Sets the copy_type of this ShowResourceCopiesSummaryResponse.

        副本类型

        :param copy_type: The copy_type of this ShowResourceCopiesSummaryResponse.
        :type copy_type: str
        """
        self._copy_type = copy_type

    @property
    def total_copy_counts(self):
        r"""Gets the total_copy_counts of this ShowResourceCopiesSummaryResponse.

        总副本数

        :return: The total_copy_counts of this ShowResourceCopiesSummaryResponse.
        :rtype: int
        """
        return self._total_copy_counts

    @total_copy_counts.setter
    def total_copy_counts(self, total_copy_counts):
        r"""Sets the total_copy_counts of this ShowResourceCopiesSummaryResponse.

        总副本数

        :param total_copy_counts: The total_copy_counts of this ShowResourceCopiesSummaryResponse.
        :type total_copy_counts: int
        """
        self._total_copy_counts = total_copy_counts

    @property
    def completed_copy_counts(self):
        r"""Gets the completed_copy_counts of this ShowResourceCopiesSummaryResponse.

        完成的备份总数, key -> ResourceCopyStatisticsKeyEnum.COMPLETED.getValue()

        :return: The completed_copy_counts of this ShowResourceCopiesSummaryResponse.
        :rtype: int
        """
        return self._completed_copy_counts

    @completed_copy_counts.setter
    def completed_copy_counts(self, completed_copy_counts):
        r"""Sets the completed_copy_counts of this ShowResourceCopiesSummaryResponse.

        完成的备份总数, key -> ResourceCopyStatisticsKeyEnum.COMPLETED.getValue()

        :param completed_copy_counts: The completed_copy_counts of this ShowResourceCopiesSummaryResponse.
        :type completed_copy_counts: int
        """
        self._completed_copy_counts = completed_copy_counts

    @property
    def failed_copy_counts(self):
        r"""Gets the failed_copy_counts of this ShowResourceCopiesSummaryResponse.

        失败的备份总数, key -> ResourceCopyStatisticsKeyEnum.FAILED.getValue()

        :return: The failed_copy_counts of this ShowResourceCopiesSummaryResponse.
        :rtype: int
        """
        return self._failed_copy_counts

    @failed_copy_counts.setter
    def failed_copy_counts(self, failed_copy_counts):
        r"""Sets the failed_copy_counts of this ShowResourceCopiesSummaryResponse.

        失败的备份总数, key -> ResourceCopyStatisticsKeyEnum.FAILED.getValue()

        :param failed_copy_counts: The failed_copy_counts of this ShowResourceCopiesSummaryResponse.
        :type failed_copy_counts: int
        """
        self._failed_copy_counts = failed_copy_counts

    @property
    def summary(self):
        r"""Gets the summary of this ShowResourceCopiesSummaryResponse.

        统计信息

        :return: The summary of this ShowResourceCopiesSummaryResponse.
        :rtype: list[:class:`huaweicloudsdkbcc.v1.GetResourceCopySummaryResponseSummary`]
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        r"""Sets the summary of this ShowResourceCopiesSummaryResponse.

        统计信息

        :param summary: The summary of this ShowResourceCopiesSummaryResponse.
        :type summary: list[:class:`huaweicloudsdkbcc.v1.GetResourceCopySummaryResponseSummary`]
        """
        self._summary = summary

    def to_dict(self):
        import warnings
        warnings.warn("ShowResourceCopiesSummaryResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowResourceCopiesSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
