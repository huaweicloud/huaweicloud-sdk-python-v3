# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCloudLogResourcesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'datasets': 'list[DatasetItem]',
        'exist': 'bool',
        'workspaces': 'list[str]'
    }

    attribute_map = {
        'datasets': 'datasets',
        'exist': 'exist',
        'workspaces': 'workspaces'
    }

    def __init__(self, datasets=None, exist=None, workspaces=None):
        r"""ListCloudLogResourcesResponse

        The model defined in huaweicloud sdk

        :param datasets: 数据集列表
        :type datasets: list[:class:`huaweicloudsdksecmaster.v1.DatasetItem`]
        :param exist: 表示资源是否存在
        :type exist: bool
        :param workspaces: 工作空间列表
        :type workspaces: list[str]
        """
        
        super().__init__()

        self._datasets = None
        self._exist = None
        self._workspaces = None
        self.discriminator = None

        if datasets is not None:
            self.datasets = datasets
        if exist is not None:
            self.exist = exist
        if workspaces is not None:
            self.workspaces = workspaces

    @property
    def datasets(self):
        r"""Gets the datasets of this ListCloudLogResourcesResponse.

        数据集列表

        :return: The datasets of this ListCloudLogResourcesResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.DatasetItem`]
        """
        return self._datasets

    @datasets.setter
    def datasets(self, datasets):
        r"""Sets the datasets of this ListCloudLogResourcesResponse.

        数据集列表

        :param datasets: The datasets of this ListCloudLogResourcesResponse.
        :type datasets: list[:class:`huaweicloudsdksecmaster.v1.DatasetItem`]
        """
        self._datasets = datasets

    @property
    def exist(self):
        r"""Gets the exist of this ListCloudLogResourcesResponse.

        表示资源是否存在

        :return: The exist of this ListCloudLogResourcesResponse.
        :rtype: bool
        """
        return self._exist

    @exist.setter
    def exist(self, exist):
        r"""Sets the exist of this ListCloudLogResourcesResponse.

        表示资源是否存在

        :param exist: The exist of this ListCloudLogResourcesResponse.
        :type exist: bool
        """
        self._exist = exist

    @property
    def workspaces(self):
        r"""Gets the workspaces of this ListCloudLogResourcesResponse.

        工作空间列表

        :return: The workspaces of this ListCloudLogResourcesResponse.
        :rtype: list[str]
        """
        return self._workspaces

    @workspaces.setter
    def workspaces(self, workspaces):
        r"""Sets the workspaces of this ListCloudLogResourcesResponse.

        工作空间列表

        :param workspaces: The workspaces of this ListCloudLogResourcesResponse.
        :type workspaces: list[str]
        """
        self._workspaces = workspaces

    def to_dict(self):
        import warnings
        warnings.warn("ListCloudLogResourcesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListCloudLogResourcesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
