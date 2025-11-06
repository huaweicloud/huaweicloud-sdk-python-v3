# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDashBoardRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dashboard_id': 'str',
        'enterprise_project_id': 'str',
        'version': 'str'
    }

    attribute_map = {
        'dashboard_id': 'dashboard_id',
        'enterprise_project_id': 'Enterprise-Project-Id',
        'version': 'version'
    }

    def __init__(self, dashboard_id=None, enterprise_project_id=None, version=None):
        r"""ShowDashBoardRequest

        The model defined in huaweicloud sdk

        :param dashboard_id: 仪表盘id。
        :type dashboard_id: str
        :param enterprise_project_id: 企业项目id。获取方式请参见：[获取企业项目ID](aom_04_0024.xml)。  -  查询单个企业项目下实例，填写企业项目id。  -  查询所有企业项目下实例，填写“all_granted_eps”。
        :type enterprise_project_id: str
        :param version: 仪表盘版本号。
        :type version: str
        """
        
        

        self._dashboard_id = None
        self._enterprise_project_id = None
        self._version = None
        self.discriminator = None

        self.dashboard_id = dashboard_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.version = version

    @property
    def dashboard_id(self):
        r"""Gets the dashboard_id of this ShowDashBoardRequest.

        仪表盘id。

        :return: The dashboard_id of this ShowDashBoardRequest.
        :rtype: str
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        r"""Sets the dashboard_id of this ShowDashBoardRequest.

        仪表盘id。

        :param dashboard_id: The dashboard_id of this ShowDashBoardRequest.
        :type dashboard_id: str
        """
        self._dashboard_id = dashboard_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowDashBoardRequest.

        企业项目id。获取方式请参见：[获取企业项目ID](aom_04_0024.xml)。  -  查询单个企业项目下实例，填写企业项目id。  -  查询所有企业项目下实例，填写“all_granted_eps”。

        :return: The enterprise_project_id of this ShowDashBoardRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowDashBoardRequest.

        企业项目id。获取方式请参见：[获取企业项目ID](aom_04_0024.xml)。  -  查询单个企业项目下实例，填写企业项目id。  -  查询所有企业项目下实例，填写“all_granted_eps”。

        :param enterprise_project_id: The enterprise_project_id of this ShowDashBoardRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def version(self):
        r"""Gets the version of this ShowDashBoardRequest.

        仪表盘版本号。

        :return: The version of this ShowDashBoardRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ShowDashBoardRequest.

        仪表盘版本号。

        :param version: The version of this ShowDashBoardRequest.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, ShowDashBoardRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
