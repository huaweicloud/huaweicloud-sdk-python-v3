# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOperationLogsByVaultNameRequest:

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
        'status': 'str',
        'resource_name': 'str',
        'offset': 'int',
        'limit': 'int',
        'last_days': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'status': 'status',
        'resource_name': 'resource_name',
        'offset': 'offset',
        'limit': 'limit',
        'last_days': 'last_days'
    }

    def __init__(self, enterprise_project_id=None, status=None, resource_name=None, offset=None, limit=None, last_days=None):
        r"""ListOperationLogsByVaultNameRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param status: 恢复状态，包含如下：   - success : 成功   - skipped : 跳过   - failed : 失败   - running : 正在运行   - timeout : 超时   - waiting : 等待
        :type status: str
        :param resource_name: 服务器名称
        :type resource_name: str
        :param offset: 查询起始点
        :type offset: int
        :param limit: 每页显示个数
        :type limit: int
        :param last_days: 查询时间范围
        :type last_days: int
        """
        
        

        self._enterprise_project_id = None
        self._status = None
        self._resource_name = None
        self._offset = None
        self._limit = None
        self._last_days = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if status is not None:
            self.status = status
        if resource_name is not None:
            self.resource_name = resource_name
        self.offset = offset
        self.limit = limit
        if last_days is not None:
            self.last_days = last_days

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListOperationLogsByVaultNameRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListOperationLogsByVaultNameRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListOperationLogsByVaultNameRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListOperationLogsByVaultNameRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def status(self):
        r"""Gets the status of this ListOperationLogsByVaultNameRequest.

        恢复状态，包含如下：   - success : 成功   - skipped : 跳过   - failed : 失败   - running : 正在运行   - timeout : 超时   - waiting : 等待

        :return: The status of this ListOperationLogsByVaultNameRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListOperationLogsByVaultNameRequest.

        恢复状态，包含如下：   - success : 成功   - skipped : 跳过   - failed : 失败   - running : 正在运行   - timeout : 超时   - waiting : 等待

        :param status: The status of this ListOperationLogsByVaultNameRequest.
        :type status: str
        """
        self._status = status

    @property
    def resource_name(self):
        r"""Gets the resource_name of this ListOperationLogsByVaultNameRequest.

        服务器名称

        :return: The resource_name of this ListOperationLogsByVaultNameRequest.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this ListOperationLogsByVaultNameRequest.

        服务器名称

        :param resource_name: The resource_name of this ListOperationLogsByVaultNameRequest.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def offset(self):
        r"""Gets the offset of this ListOperationLogsByVaultNameRequest.

        查询起始点

        :return: The offset of this ListOperationLogsByVaultNameRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListOperationLogsByVaultNameRequest.

        查询起始点

        :param offset: The offset of this ListOperationLogsByVaultNameRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListOperationLogsByVaultNameRequest.

        每页显示个数

        :return: The limit of this ListOperationLogsByVaultNameRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListOperationLogsByVaultNameRequest.

        每页显示个数

        :param limit: The limit of this ListOperationLogsByVaultNameRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def last_days(self):
        r"""Gets the last_days of this ListOperationLogsByVaultNameRequest.

        查询时间范围

        :return: The last_days of this ListOperationLogsByVaultNameRequest.
        :rtype: int
        """
        return self._last_days

    @last_days.setter
    def last_days(self, last_days):
        r"""Sets the last_days of this ListOperationLogsByVaultNameRequest.

        查询时间范围

        :param last_days: The last_days of this ListOperationLogsByVaultNameRequest.
        :type last_days: int
        """
        self._last_days = last_days

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
        if not isinstance(other, ListOperationLogsByVaultNameRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
