# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRaspServerDetailRequest:

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
        'limit': 'int',
        'offset': 'int',
        'host_id': 'str',
        'keyword': 'str',
        'app_protect_status': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'limit': 'limit',
        'offset': 'offset',
        'host_id': 'host_id',
        'keyword': 'keyword',
        'app_protect_status': 'app_protect_status'
    }

    def __init__(self, enterprise_project_id=None, limit=None, offset=None, host_id=None, keyword=None, app_protect_status=None):
        r"""ShowRaspServerDetailRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 
        :type offset: int
        :param host_id: 服务器ID
        :type host_id: str
        :param keyword: 搜索关键词
        :type keyword: str
        :param app_protect_status: java单个应用防护状态，包含如下3种。 - 0 ：未防护。 - 1 ：防护失败。 - 2 ：防护成功。
        :type app_protect_status: int
        """
        
        

        self._enterprise_project_id = None
        self._limit = None
        self._offset = None
        self._host_id = None
        self._keyword = None
        self._app_protect_status = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.limit = limit
        self.offset = offset
        self.host_id = host_id
        if keyword is not None:
            self.keyword = keyword
        if app_protect_status is not None:
            self.app_protect_status = app_protect_status

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowRaspServerDetailRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ShowRaspServerDetailRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowRaspServerDetailRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ShowRaspServerDetailRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def limit(self):
        r"""Gets the limit of this ShowRaspServerDetailRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ShowRaspServerDetailRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowRaspServerDetailRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ShowRaspServerDetailRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowRaspServerDetailRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :return: The offset of this ShowRaspServerDetailRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowRaspServerDetailRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :param offset: The offset of this ShowRaspServerDetailRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def host_id(self):
        r"""Gets the host_id of this ShowRaspServerDetailRequest.

        服务器ID

        :return: The host_id of this ShowRaspServerDetailRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ShowRaspServerDetailRequest.

        服务器ID

        :param host_id: The host_id of this ShowRaspServerDetailRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def keyword(self):
        r"""Gets the keyword of this ShowRaspServerDetailRequest.

        搜索关键词

        :return: The keyword of this ShowRaspServerDetailRequest.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        r"""Sets the keyword of this ShowRaspServerDetailRequest.

        搜索关键词

        :param keyword: The keyword of this ShowRaspServerDetailRequest.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def app_protect_status(self):
        r"""Gets the app_protect_status of this ShowRaspServerDetailRequest.

        java单个应用防护状态，包含如下3种。 - 0 ：未防护。 - 1 ：防护失败。 - 2 ：防护成功。

        :return: The app_protect_status of this ShowRaspServerDetailRequest.
        :rtype: int
        """
        return self._app_protect_status

    @app_protect_status.setter
    def app_protect_status(self, app_protect_status):
        r"""Sets the app_protect_status of this ShowRaspServerDetailRequest.

        java单个应用防护状态，包含如下3种。 - 0 ：未防护。 - 1 ：防护失败。 - 2 ：防护成功。

        :param app_protect_status: The app_protect_status of this ShowRaspServerDetailRequest.
        :type app_protect_status: int
        """
        self._app_protect_status = app_protect_status

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
        if not isinstance(other, ShowRaspServerDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
