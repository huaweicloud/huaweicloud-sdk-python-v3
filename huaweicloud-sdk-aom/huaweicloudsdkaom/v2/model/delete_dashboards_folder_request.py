# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteDashboardsFolderRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'folder_id': 'str',
        'enterprise_project_id': 'str',
        'delete_all': 'bool'
    }

    attribute_map = {
        'folder_id': 'folder_id',
        'enterprise_project_id': 'Enterprise-Project-Id',
        'delete_all': 'delete_all'
    }

    def __init__(self, folder_id=None, enterprise_project_id=None, delete_all=None):
        r"""DeleteDashboardsFolderRequest

        The model defined in huaweicloud sdk

        :param folder_id: 仪表盘分组id。
        :type folder_id: str
        :param enterprise_project_id: 企业项目id。获取方式请参见：[获取企业项目ID](aom_04_0024.xml)。  - 删除单个企业项目下实例，填写企业项目id。  - 不填时，默认删除企业项目id为0的企业项目下实例。
        :type enterprise_project_id: str
        :param delete_all: 是否删除仪表盘分组下的仪表盘。
        :type delete_all: bool
        """
        
        

        self._folder_id = None
        self._enterprise_project_id = None
        self._delete_all = None
        self.discriminator = None

        self.folder_id = folder_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.delete_all = delete_all

    @property
    def folder_id(self):
        r"""Gets the folder_id of this DeleteDashboardsFolderRequest.

        仪表盘分组id。

        :return: The folder_id of this DeleteDashboardsFolderRequest.
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        r"""Sets the folder_id of this DeleteDashboardsFolderRequest.

        仪表盘分组id。

        :param folder_id: The folder_id of this DeleteDashboardsFolderRequest.
        :type folder_id: str
        """
        self._folder_id = folder_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this DeleteDashboardsFolderRequest.

        企业项目id。获取方式请参见：[获取企业项目ID](aom_04_0024.xml)。  - 删除单个企业项目下实例，填写企业项目id。  - 不填时，默认删除企业项目id为0的企业项目下实例。

        :return: The enterprise_project_id of this DeleteDashboardsFolderRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this DeleteDashboardsFolderRequest.

        企业项目id。获取方式请参见：[获取企业项目ID](aom_04_0024.xml)。  - 删除单个企业项目下实例，填写企业项目id。  - 不填时，默认删除企业项目id为0的企业项目下实例。

        :param enterprise_project_id: The enterprise_project_id of this DeleteDashboardsFolderRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def delete_all(self):
        r"""Gets the delete_all of this DeleteDashboardsFolderRequest.

        是否删除仪表盘分组下的仪表盘。

        :return: The delete_all of this DeleteDashboardsFolderRequest.
        :rtype: bool
        """
        return self._delete_all

    @delete_all.setter
    def delete_all(self, delete_all):
        r"""Sets the delete_all of this DeleteDashboardsFolderRequest.

        是否删除仪表盘分组下的仪表盘。

        :param delete_all: The delete_all of this DeleteDashboardsFolderRequest.
        :type delete_all: bool
        """
        self._delete_all = delete_all

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
        if not isinstance(other, DeleteDashboardsFolderRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
