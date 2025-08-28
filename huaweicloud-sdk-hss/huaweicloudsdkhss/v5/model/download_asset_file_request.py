# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadAssetFileRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'asset_type': 'str',
        'category': 'str',
        'body': 'DownloadAssetFileRequestBody'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'asset_type': 'asset_type',
        'category': 'category',
        'body': 'body'
    }

    def __init__(self, enterprise_project_id=None, asset_type=None, category=None, body=None):
        r"""DownloadAssetFileRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param asset_type: **参数解释**: 资产指纹类型 **约束限制**: 不涉及 **取值范围**: - users         ：账号 - auto_launch   ：自启动项 - database      ：数据库 - jar_package   ：中间件 - port          ：开放端口 - process       ：进程 - web_cms       ：web应用 - web_framework ：web框架 - web_service   ：web服务 - web_site      ：web站点 - app           ：软件 - kernel_module ：内核模块  **默认取值**: 不涉及 
        :type asset_type: str
        :param category: **参数解释**: 类别 **约束限制**: 不涉及 **取值范围**: - host     ：主机 - container：容器  **默认取值**: host 
        :type category: str
        :param body: Body of the DownloadAssetFileRequest
        :type body: :class:`huaweicloudsdkhss.v5.DownloadAssetFileRequestBody`
        """
        
        

        self._enterprise_project_id = None
        self._asset_type = None
        self._category = None
        self._body = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.asset_type = asset_type
        self.category = category
        if body is not None:
            self.body = body

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this DownloadAssetFileRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this DownloadAssetFileRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this DownloadAssetFileRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this DownloadAssetFileRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def asset_type(self):
        r"""Gets the asset_type of this DownloadAssetFileRequest.

        **参数解释**: 资产指纹类型 **约束限制**: 不涉及 **取值范围**: - users         ：账号 - auto_launch   ：自启动项 - database      ：数据库 - jar_package   ：中间件 - port          ：开放端口 - process       ：进程 - web_cms       ：web应用 - web_framework ：web框架 - web_service   ：web服务 - web_site      ：web站点 - app           ：软件 - kernel_module ：内核模块  **默认取值**: 不涉及 

        :return: The asset_type of this DownloadAssetFileRequest.
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        r"""Sets the asset_type of this DownloadAssetFileRequest.

        **参数解释**: 资产指纹类型 **约束限制**: 不涉及 **取值范围**: - users         ：账号 - auto_launch   ：自启动项 - database      ：数据库 - jar_package   ：中间件 - port          ：开放端口 - process       ：进程 - web_cms       ：web应用 - web_framework ：web框架 - web_service   ：web服务 - web_site      ：web站点 - app           ：软件 - kernel_module ：内核模块  **默认取值**: 不涉及 

        :param asset_type: The asset_type of this DownloadAssetFileRequest.
        :type asset_type: str
        """
        self._asset_type = asset_type

    @property
    def category(self):
        r"""Gets the category of this DownloadAssetFileRequest.

        **参数解释**: 类别 **约束限制**: 不涉及 **取值范围**: - host     ：主机 - container：容器  **默认取值**: host 

        :return: The category of this DownloadAssetFileRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this DownloadAssetFileRequest.

        **参数解释**: 类别 **约束限制**: 不涉及 **取值范围**: - host     ：主机 - container：容器  **默认取值**: host 

        :param category: The category of this DownloadAssetFileRequest.
        :type category: str
        """
        self._category = category

    @property
    def body(self):
        r"""Gets the body of this DownloadAssetFileRequest.

        :return: The body of this DownloadAssetFileRequest.
        :rtype: :class:`huaweicloudsdkhss.v5.DownloadAssetFileRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this DownloadAssetFileRequest.

        :param body: The body of this DownloadAssetFileRequest.
        :type body: :class:`huaweicloudsdkhss.v5.DownloadAssetFileRequestBody`
        """
        self._body = body

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
        if not isinstance(other, DownloadAssetFileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
