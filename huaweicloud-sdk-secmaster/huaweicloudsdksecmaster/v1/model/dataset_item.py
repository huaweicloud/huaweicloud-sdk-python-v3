# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatasetItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alert': 'bool',
        'allow_alert': 'bool',
        'allow_lts': 'bool',
        'create_time': 'int',
        'domain_id': 'str',
        'enable': 'str',
        'project_id': 'str',
        'region': 'bool',
        'region_id': 'str',
        'success': 'bool',
        'total': 'int',
        'update_time': 'int',
        'workspace_id': 'str'
    }

    attribute_map = {
        'alert': 'alert',
        'allow_alert': 'allow_alert',
        'allow_lts': 'allow_lts',
        'create_time': 'create_time',
        'domain_id': 'domain_id',
        'enable': 'enable',
        'project_id': 'project_id',
        'region': 'region',
        'region_id': 'region_id',
        'success': 'success',
        'total': 'total',
        'update_time': 'update_time',
        'workspace_id': 'workspace_id'
    }

    def __init__(self, alert=None, allow_alert=None, allow_lts=None, create_time=None, domain_id=None, enable=None, project_id=None, region=None, region_id=None, success=None, total=None, update_time=None, workspace_id=None):
        r"""DatasetItem

        The model defined in huaweicloud sdk

        :param alert: 是否触发告警
        :type alert: bool
        :param allow_alert: 是否允许告警
        :type allow_alert: bool
        :param allow_lts: 是否允许长期存储
        :type allow_lts: bool
        :param create_time: 创建时间，单位为毫秒的时间戳
        :type create_time: int
        :param domain_id: 租户ID，唯一标识
        :type domain_id: str
        :param enable: 启用状态，例如 \&quot;active\&quot; 表示启用
        :type enable: str
        :param project_id: 项目ID，唯一标识
        :type project_id: str
        :param region: 是否是区域级数据
        :type region: bool
        :param region_id: 区域ID，表示当前区域
        :type region_id: str
        :param success: 操作是否成功
        :type success: bool
        :param total: 总记录数
        :type total: int
        :param update_time: 更新时间，单位为毫秒的时间戳
        :type update_time: int
        :param workspace_id: 工作空间ID，唯一标识
        :type workspace_id: str
        """
        
        

        self._alert = None
        self._allow_alert = None
        self._allow_lts = None
        self._create_time = None
        self._domain_id = None
        self._enable = None
        self._project_id = None
        self._region = None
        self._region_id = None
        self._success = None
        self._total = None
        self._update_time = None
        self._workspace_id = None
        self.discriminator = None

        self.alert = alert
        self.allow_alert = allow_alert
        self.allow_lts = allow_lts
        self.create_time = create_time
        self.domain_id = domain_id
        self.enable = enable
        self.project_id = project_id
        self.region = region
        self.region_id = region_id
        self.success = success
        self.total = total
        self.update_time = update_time
        self.workspace_id = workspace_id

    @property
    def alert(self):
        r"""Gets the alert of this DatasetItem.

        是否触发告警

        :return: The alert of this DatasetItem.
        :rtype: bool
        """
        return self._alert

    @alert.setter
    def alert(self, alert):
        r"""Sets the alert of this DatasetItem.

        是否触发告警

        :param alert: The alert of this DatasetItem.
        :type alert: bool
        """
        self._alert = alert

    @property
    def allow_alert(self):
        r"""Gets the allow_alert of this DatasetItem.

        是否允许告警

        :return: The allow_alert of this DatasetItem.
        :rtype: bool
        """
        return self._allow_alert

    @allow_alert.setter
    def allow_alert(self, allow_alert):
        r"""Sets the allow_alert of this DatasetItem.

        是否允许告警

        :param allow_alert: The allow_alert of this DatasetItem.
        :type allow_alert: bool
        """
        self._allow_alert = allow_alert

    @property
    def allow_lts(self):
        r"""Gets the allow_lts of this DatasetItem.

        是否允许长期存储

        :return: The allow_lts of this DatasetItem.
        :rtype: bool
        """
        return self._allow_lts

    @allow_lts.setter
    def allow_lts(self, allow_lts):
        r"""Sets the allow_lts of this DatasetItem.

        是否允许长期存储

        :param allow_lts: The allow_lts of this DatasetItem.
        :type allow_lts: bool
        """
        self._allow_lts = allow_lts

    @property
    def create_time(self):
        r"""Gets the create_time of this DatasetItem.

        创建时间，单位为毫秒的时间戳

        :return: The create_time of this DatasetItem.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this DatasetItem.

        创建时间，单位为毫秒的时间戳

        :param create_time: The create_time of this DatasetItem.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def domain_id(self):
        r"""Gets the domain_id of this DatasetItem.

        租户ID，唯一标识

        :return: The domain_id of this DatasetItem.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this DatasetItem.

        租户ID，唯一标识

        :param domain_id: The domain_id of this DatasetItem.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def enable(self):
        r"""Gets the enable of this DatasetItem.

        启用状态，例如 \"active\" 表示启用

        :return: The enable of this DatasetItem.
        :rtype: str
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this DatasetItem.

        启用状态，例如 \"active\" 表示启用

        :param enable: The enable of this DatasetItem.
        :type enable: str
        """
        self._enable = enable

    @property
    def project_id(self):
        r"""Gets the project_id of this DatasetItem.

        项目ID，唯一标识

        :return: The project_id of this DatasetItem.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this DatasetItem.

        项目ID，唯一标识

        :param project_id: The project_id of this DatasetItem.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def region(self):
        r"""Gets the region of this DatasetItem.

        是否是区域级数据

        :return: The region of this DatasetItem.
        :rtype: bool
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this DatasetItem.

        是否是区域级数据

        :param region: The region of this DatasetItem.
        :type region: bool
        """
        self._region = region

    @property
    def region_id(self):
        r"""Gets the region_id of this DatasetItem.

        区域ID，表示当前区域

        :return: The region_id of this DatasetItem.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this DatasetItem.

        区域ID，表示当前区域

        :param region_id: The region_id of this DatasetItem.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def success(self):
        r"""Gets the success of this DatasetItem.

        操作是否成功

        :return: The success of this DatasetItem.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this DatasetItem.

        操作是否成功

        :param success: The success of this DatasetItem.
        :type success: bool
        """
        self._success = success

    @property
    def total(self):
        r"""Gets the total of this DatasetItem.

        总记录数

        :return: The total of this DatasetItem.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this DatasetItem.

        总记录数

        :param total: The total of this DatasetItem.
        :type total: int
        """
        self._total = total

    @property
    def update_time(self):
        r"""Gets the update_time of this DatasetItem.

        更新时间，单位为毫秒的时间戳

        :return: The update_time of this DatasetItem.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this DatasetItem.

        更新时间，单位为毫秒的时间戳

        :param update_time: The update_time of this DatasetItem.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this DatasetItem.

        工作空间ID，唯一标识

        :return: The workspace_id of this DatasetItem.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this DatasetItem.

        工作空间ID，唯一标识

        :param workspace_id: The workspace_id of this DatasetItem.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

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
        if not isinstance(other, DatasetItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
