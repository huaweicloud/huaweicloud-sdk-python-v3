# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCollectConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'all_vendors': 'list[ListCollectConfigResponseBodyAllVendors]',
        'cofing_statistics': 'ListCollectConfigResponseBodyCofingStatistics',
        'data_list': 'list[ListCollectConfigResponseBodyDataList]',
        'datasets': 'list[DatasetInfo]',
        'dataspace_id': 'str',
        'dataspace_name': 'str',
        'domain_id': 'str',
        'lts_sets': 'list[LtsResponseVo]',
        'project_id': 'str',
        'region_id': 'str',
        'workspace_id': 'str'
    }

    attribute_map = {
        'all_vendors': 'all_vendors',
        'cofing_statistics': 'cofing_statistics',
        'data_list': 'data_list',
        'datasets': 'datasets',
        'dataspace_id': 'dataspace_id',
        'dataspace_name': 'dataspace_name',
        'domain_id': 'domain_id',
        'lts_sets': 'lts_sets',
        'project_id': 'project_id',
        'region_id': 'region_id',
        'workspace_id': 'workspace_id'
    }

    def __init__(self, all_vendors=None, cofing_statistics=None, data_list=None, datasets=None, dataspace_id=None, dataspace_name=None, domain_id=None, lts_sets=None, project_id=None, region_id=None, workspace_id=None):
        r"""ListCollectConfigResponse

        The model defined in huaweicloud sdk

        :param all_vendors: 所有的云厂商、云产品和日志
        :type all_vendors: list[:class:`huaweicloudsdksecmaster.v1.ListCollectConfigResponseBodyAllVendors`]
        :param cofing_statistics: 
        :type cofing_statistics: :class:`huaweicloudsdksecmaster.v1.ListCollectConfigResponseBodyCofingStatistics`
        :param data_list: 数据
        :type data_list: list[:class:`huaweicloudsdksecmaster.v1.ListCollectConfigResponseBodyDataList`]
        :param datasets: 数据集列表
        :type datasets: list[:class:`huaweicloudsdksecmaster.v1.DatasetInfo`]
        :param dataspace_id: 数据空间ID
        :type dataspace_id: str
        :param dataspace_name: 数据空间名称
        :type dataspace_name: str
        :param domain_id: 账号ID
        :type domain_id: str
        :param lts_sets: lts日志配置
        :type lts_sets: list[:class:`huaweicloudsdksecmaster.v1.LtsResponseVo`]
        :param project_id: 项目ID
        :type project_id: str
        :param region_id: 所属region
        :type region_id: str
        :param workspace_id: 工作空间 id
        :type workspace_id: str
        """
        
        super().__init__()

        self._all_vendors = None
        self._cofing_statistics = None
        self._data_list = None
        self._datasets = None
        self._dataspace_id = None
        self._dataspace_name = None
        self._domain_id = None
        self._lts_sets = None
        self._project_id = None
        self._region_id = None
        self._workspace_id = None
        self.discriminator = None

        if all_vendors is not None:
            self.all_vendors = all_vendors
        if cofing_statistics is not None:
            self.cofing_statistics = cofing_statistics
        if data_list is not None:
            self.data_list = data_list
        if datasets is not None:
            self.datasets = datasets
        if dataspace_id is not None:
            self.dataspace_id = dataspace_id
        if dataspace_name is not None:
            self.dataspace_name = dataspace_name
        if domain_id is not None:
            self.domain_id = domain_id
        if lts_sets is not None:
            self.lts_sets = lts_sets
        if project_id is not None:
            self.project_id = project_id
        if region_id is not None:
            self.region_id = region_id
        if workspace_id is not None:
            self.workspace_id = workspace_id

    @property
    def all_vendors(self):
        r"""Gets the all_vendors of this ListCollectConfigResponse.

        所有的云厂商、云产品和日志

        :return: The all_vendors of this ListCollectConfigResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.ListCollectConfigResponseBodyAllVendors`]
        """
        return self._all_vendors

    @all_vendors.setter
    def all_vendors(self, all_vendors):
        r"""Sets the all_vendors of this ListCollectConfigResponse.

        所有的云厂商、云产品和日志

        :param all_vendors: The all_vendors of this ListCollectConfigResponse.
        :type all_vendors: list[:class:`huaweicloudsdksecmaster.v1.ListCollectConfigResponseBodyAllVendors`]
        """
        self._all_vendors = all_vendors

    @property
    def cofing_statistics(self):
        r"""Gets the cofing_statistics of this ListCollectConfigResponse.

        :return: The cofing_statistics of this ListCollectConfigResponse.
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListCollectConfigResponseBodyCofingStatistics`
        """
        return self._cofing_statistics

    @cofing_statistics.setter
    def cofing_statistics(self, cofing_statistics):
        r"""Sets the cofing_statistics of this ListCollectConfigResponse.

        :param cofing_statistics: The cofing_statistics of this ListCollectConfigResponse.
        :type cofing_statistics: :class:`huaweicloudsdksecmaster.v1.ListCollectConfigResponseBodyCofingStatistics`
        """
        self._cofing_statistics = cofing_statistics

    @property
    def data_list(self):
        r"""Gets the data_list of this ListCollectConfigResponse.

        数据

        :return: The data_list of this ListCollectConfigResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.ListCollectConfigResponseBodyDataList`]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        r"""Sets the data_list of this ListCollectConfigResponse.

        数据

        :param data_list: The data_list of this ListCollectConfigResponse.
        :type data_list: list[:class:`huaweicloudsdksecmaster.v1.ListCollectConfigResponseBodyDataList`]
        """
        self._data_list = data_list

    @property
    def datasets(self):
        r"""Gets the datasets of this ListCollectConfigResponse.

        数据集列表

        :return: The datasets of this ListCollectConfigResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.DatasetInfo`]
        """
        return self._datasets

    @datasets.setter
    def datasets(self, datasets):
        r"""Sets the datasets of this ListCollectConfigResponse.

        数据集列表

        :param datasets: The datasets of this ListCollectConfigResponse.
        :type datasets: list[:class:`huaweicloudsdksecmaster.v1.DatasetInfo`]
        """
        self._datasets = datasets

    @property
    def dataspace_id(self):
        r"""Gets the dataspace_id of this ListCollectConfigResponse.

        数据空间ID

        :return: The dataspace_id of this ListCollectConfigResponse.
        :rtype: str
        """
        return self._dataspace_id

    @dataspace_id.setter
    def dataspace_id(self, dataspace_id):
        r"""Sets the dataspace_id of this ListCollectConfigResponse.

        数据空间ID

        :param dataspace_id: The dataspace_id of this ListCollectConfigResponse.
        :type dataspace_id: str
        """
        self._dataspace_id = dataspace_id

    @property
    def dataspace_name(self):
        r"""Gets the dataspace_name of this ListCollectConfigResponse.

        数据空间名称

        :return: The dataspace_name of this ListCollectConfigResponse.
        :rtype: str
        """
        return self._dataspace_name

    @dataspace_name.setter
    def dataspace_name(self, dataspace_name):
        r"""Sets the dataspace_name of this ListCollectConfigResponse.

        数据空间名称

        :param dataspace_name: The dataspace_name of this ListCollectConfigResponse.
        :type dataspace_name: str
        """
        self._dataspace_name = dataspace_name

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ListCollectConfigResponse.

        账号ID

        :return: The domain_id of this ListCollectConfigResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ListCollectConfigResponse.

        账号ID

        :param domain_id: The domain_id of this ListCollectConfigResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def lts_sets(self):
        r"""Gets the lts_sets of this ListCollectConfigResponse.

        lts日志配置

        :return: The lts_sets of this ListCollectConfigResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.LtsResponseVo`]
        """
        return self._lts_sets

    @lts_sets.setter
    def lts_sets(self, lts_sets):
        r"""Sets the lts_sets of this ListCollectConfigResponse.

        lts日志配置

        :param lts_sets: The lts_sets of this ListCollectConfigResponse.
        :type lts_sets: list[:class:`huaweicloudsdksecmaster.v1.LtsResponseVo`]
        """
        self._lts_sets = lts_sets

    @property
    def project_id(self):
        r"""Gets the project_id of this ListCollectConfigResponse.

        项目ID

        :return: The project_id of this ListCollectConfigResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListCollectConfigResponse.

        项目ID

        :param project_id: The project_id of this ListCollectConfigResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def region_id(self):
        r"""Gets the region_id of this ListCollectConfigResponse.

        所属region

        :return: The region_id of this ListCollectConfigResponse.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ListCollectConfigResponse.

        所属region

        :param region_id: The region_id of this ListCollectConfigResponse.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListCollectConfigResponse.

        工作空间 id

        :return: The workspace_id of this ListCollectConfigResponse.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListCollectConfigResponse.

        工作空间 id

        :param workspace_id: The workspace_id of this ListCollectConfigResponse.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    def to_dict(self):
        import warnings
        warnings.warn("ListCollectConfigResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListCollectConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
