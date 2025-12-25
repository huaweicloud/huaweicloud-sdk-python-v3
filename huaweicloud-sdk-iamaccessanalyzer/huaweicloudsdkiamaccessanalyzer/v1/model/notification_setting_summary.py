# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NotificationSettingSummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('analyzer_name')

    openapi_types = {
        'id': 'str',
        'urn': 'str',
        'analyzer_id': 'str',
        'analyzer_name': 'str',
        'analyzer_type': 'str',
        'mc_switch': 'bool',
        'smn_topic_urns': 'list[str]',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'urn': 'urn',
        'analyzer_id': 'analyzer_id',
        'analyzer_name': 'analyzer_name',
        'analyzer_type': 'analyzer_type',
        'mc_switch': 'mc_switch',
        'smn_topic_urns': 'smn_topic_urns',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, urn=None, analyzer_id=None, analyzer_name=None, analyzer_type=None, mc_switch=None, smn_topic_urns=None, created_at=None, updated_at=None):
        r"""NotificationSettingSummary

        The model defined in huaweicloud sdk

        :param id: 消息通知配置的唯一标识符。
        :type id: str
        :param urn: 消息通知配置的唯一资源标识符。
        :type urn: str
        :param analyzer_id: 分析器的唯一标识符。
        :type analyzer_id: str
        :param analyzer_name: 分析器的名称。
        :type analyzer_name: str
        :param analyzer_type: 分析器的类型。 - account: 账号级外部访问分析器 - organization：组织级外部访问分析器 - account_unused_access：账号级未使用访问分析器 - organization_unused_access：组织级未使用访问分析器 - account_privilege_escalation：账号级提权访问分析器 - account_iam_best_practice：账号级IAM最佳实践分析器 
        :type analyzer_type: str
        :param mc_switch: 是否开启消息中心通知开关。
        :type mc_switch: bool
        :param smn_topic_urns: 消息通知配置的SMN主题URN列表。
        :type smn_topic_urns: list[str]
        :param created_at: 创建消息通知配置的时间。
        :type created_at: datetime
        :param updated_at: 上次更新消息通知配置的时间。
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._urn = None
        self._analyzer_id = None
        self._analyzer_name = None
        self._analyzer_type = None
        self._mc_switch = None
        self._smn_topic_urns = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        self.urn = urn
        self.analyzer_id = analyzer_id
        self.analyzer_name = analyzer_name
        self.analyzer_type = analyzer_type
        self.mc_switch = mc_switch
        self.smn_topic_urns = smn_topic_urns
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this NotificationSettingSummary.

        消息通知配置的唯一标识符。

        :return: The id of this NotificationSettingSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this NotificationSettingSummary.

        消息通知配置的唯一标识符。

        :param id: The id of this NotificationSettingSummary.
        :type id: str
        """
        self._id = id

    @property
    def urn(self):
        r"""Gets the urn of this NotificationSettingSummary.

        消息通知配置的唯一资源标识符。

        :return: The urn of this NotificationSettingSummary.
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        r"""Sets the urn of this NotificationSettingSummary.

        消息通知配置的唯一资源标识符。

        :param urn: The urn of this NotificationSettingSummary.
        :type urn: str
        """
        self._urn = urn

    @property
    def analyzer_id(self):
        r"""Gets the analyzer_id of this NotificationSettingSummary.

        分析器的唯一标识符。

        :return: The analyzer_id of this NotificationSettingSummary.
        :rtype: str
        """
        return self._analyzer_id

    @analyzer_id.setter
    def analyzer_id(self, analyzer_id):
        r"""Sets the analyzer_id of this NotificationSettingSummary.

        分析器的唯一标识符。

        :param analyzer_id: The analyzer_id of this NotificationSettingSummary.
        :type analyzer_id: str
        """
        self._analyzer_id = analyzer_id

    @property
    def analyzer_name(self):
        r"""Gets the analyzer_name of this NotificationSettingSummary.

        分析器的名称。

        :return: The analyzer_name of this NotificationSettingSummary.
        :rtype: str
        """
        return self._analyzer_name

    @analyzer_name.setter
    def analyzer_name(self, analyzer_name):
        r"""Sets the analyzer_name of this NotificationSettingSummary.

        分析器的名称。

        :param analyzer_name: The analyzer_name of this NotificationSettingSummary.
        :type analyzer_name: str
        """
        self._analyzer_name = analyzer_name

    @property
    def analyzer_type(self):
        r"""Gets the analyzer_type of this NotificationSettingSummary.

        分析器的类型。 - account: 账号级外部访问分析器 - organization：组织级外部访问分析器 - account_unused_access：账号级未使用访问分析器 - organization_unused_access：组织级未使用访问分析器 - account_privilege_escalation：账号级提权访问分析器 - account_iam_best_practice：账号级IAM最佳实践分析器 

        :return: The analyzer_type of this NotificationSettingSummary.
        :rtype: str
        """
        return self._analyzer_type

    @analyzer_type.setter
    def analyzer_type(self, analyzer_type):
        r"""Sets the analyzer_type of this NotificationSettingSummary.

        分析器的类型。 - account: 账号级外部访问分析器 - organization：组织级外部访问分析器 - account_unused_access：账号级未使用访问分析器 - organization_unused_access：组织级未使用访问分析器 - account_privilege_escalation：账号级提权访问分析器 - account_iam_best_practice：账号级IAM最佳实践分析器 

        :param analyzer_type: The analyzer_type of this NotificationSettingSummary.
        :type analyzer_type: str
        """
        self._analyzer_type = analyzer_type

    @property
    def mc_switch(self):
        r"""Gets the mc_switch of this NotificationSettingSummary.

        是否开启消息中心通知开关。

        :return: The mc_switch of this NotificationSettingSummary.
        :rtype: bool
        """
        return self._mc_switch

    @mc_switch.setter
    def mc_switch(self, mc_switch):
        r"""Sets the mc_switch of this NotificationSettingSummary.

        是否开启消息中心通知开关。

        :param mc_switch: The mc_switch of this NotificationSettingSummary.
        :type mc_switch: bool
        """
        self._mc_switch = mc_switch

    @property
    def smn_topic_urns(self):
        r"""Gets the smn_topic_urns of this NotificationSettingSummary.

        消息通知配置的SMN主题URN列表。

        :return: The smn_topic_urns of this NotificationSettingSummary.
        :rtype: list[str]
        """
        return self._smn_topic_urns

    @smn_topic_urns.setter
    def smn_topic_urns(self, smn_topic_urns):
        r"""Sets the smn_topic_urns of this NotificationSettingSummary.

        消息通知配置的SMN主题URN列表。

        :param smn_topic_urns: The smn_topic_urns of this NotificationSettingSummary.
        :type smn_topic_urns: list[str]
        """
        self._smn_topic_urns = smn_topic_urns

    @property
    def created_at(self):
        r"""Gets the created_at of this NotificationSettingSummary.

        创建消息通知配置的时间。

        :return: The created_at of this NotificationSettingSummary.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this NotificationSettingSummary.

        创建消息通知配置的时间。

        :param created_at: The created_at of this NotificationSettingSummary.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this NotificationSettingSummary.

        上次更新消息通知配置的时间。

        :return: The updated_at of this NotificationSettingSummary.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this NotificationSettingSummary.

        上次更新消息通知配置的时间。

        :param updated_at: The updated_at of this NotificationSettingSummary.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, NotificationSettingSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
