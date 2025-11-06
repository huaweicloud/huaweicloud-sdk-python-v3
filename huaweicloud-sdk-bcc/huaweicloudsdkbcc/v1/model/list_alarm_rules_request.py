# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlarmRulesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'namespace': 'str',
        'region_id': 'str',
        'alarm_rule_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'namespace': 'namespace',
        'region_id': 'region_id',
        'alarm_rule_id': 'alarm_rule_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, domain_id=None, namespace=None, region_id=None, alarm_rule_id=None, offset=None, limit=None):
        r"""ListAlarmRulesRequest

        The model defined in huaweicloud sdk

        :param domain_id: 账号ID
        :type domain_id: str
        :param namespace: 告警命名空间，取值范围：SYS.CBR,SYS.RDS,SYS.GaussDB
        :type namespace: str
        :param region_id: RegionID
        :type region_id: str
        :param alarm_rule_id: 告警规则ID
        :type alarm_rule_id: str
        :param offset: 分页起始值，默认值为0。
        :type offset: int
        :param limit: 单次查询的条数限制,取值范围(0,100]，默认值为100，用于限制结果数据条数。
        :type limit: int
        """
        
        

        self._domain_id = None
        self._namespace = None
        self._region_id = None
        self._alarm_rule_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.domain_id = domain_id
        if namespace is not None:
            self.namespace = namespace
        if region_id is not None:
            self.region_id = region_id
        if alarm_rule_id is not None:
            self.alarm_rule_id = alarm_rule_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ListAlarmRulesRequest.

        账号ID

        :return: The domain_id of this ListAlarmRulesRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ListAlarmRulesRequest.

        账号ID

        :param domain_id: The domain_id of this ListAlarmRulesRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def namespace(self):
        r"""Gets the namespace of this ListAlarmRulesRequest.

        告警命名空间，取值范围：SYS.CBR,SYS.RDS,SYS.GaussDB

        :return: The namespace of this ListAlarmRulesRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ListAlarmRulesRequest.

        告警命名空间，取值范围：SYS.CBR,SYS.RDS,SYS.GaussDB

        :param namespace: The namespace of this ListAlarmRulesRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def region_id(self):
        r"""Gets the region_id of this ListAlarmRulesRequest.

        RegionID

        :return: The region_id of this ListAlarmRulesRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ListAlarmRulesRequest.

        RegionID

        :param region_id: The region_id of this ListAlarmRulesRequest.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def alarm_rule_id(self):
        r"""Gets the alarm_rule_id of this ListAlarmRulesRequest.

        告警规则ID

        :return: The alarm_rule_id of this ListAlarmRulesRequest.
        :rtype: str
        """
        return self._alarm_rule_id

    @alarm_rule_id.setter
    def alarm_rule_id(self, alarm_rule_id):
        r"""Sets the alarm_rule_id of this ListAlarmRulesRequest.

        告警规则ID

        :param alarm_rule_id: The alarm_rule_id of this ListAlarmRulesRequest.
        :type alarm_rule_id: str
        """
        self._alarm_rule_id = alarm_rule_id

    @property
    def offset(self):
        r"""Gets the offset of this ListAlarmRulesRequest.

        分页起始值，默认值为0。

        :return: The offset of this ListAlarmRulesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAlarmRulesRequest.

        分页起始值，默认值为0。

        :param offset: The offset of this ListAlarmRulesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListAlarmRulesRequest.

        单次查询的条数限制,取值范围(0,100]，默认值为100，用于限制结果数据条数。

        :return: The limit of this ListAlarmRulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAlarmRulesRequest.

        单次查询的条数限制,取值范围(0,100]，默认值为100，用于限制结果数据条数。

        :param limit: The limit of this ListAlarmRulesRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListAlarmRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
