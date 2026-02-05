# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigSqlBlacklistReqV3VO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sql_black_list_full_check': 'str',
        'request_id': 'str',
        'project_id': 'str',
        'instance_id': 'str',
        'logic_db_name': 'str',
        'sql_black_list_prefix_check': 'str',
        'sql_black_list_regex_check': 'str'
    }

    attribute_map = {
        'sql_black_list_full_check': 'sql_black_list_full_check',
        'request_id': 'request_id',
        'project_id': 'project_id',
        'instance_id': 'instance_id',
        'logic_db_name': 'logic_db_name',
        'sql_black_list_prefix_check': 'sql_black_list_prefix_check',
        'sql_black_list_regex_check': 'sql_black_list_regex_check'
    }

    def __init__(self, sql_black_list_full_check=None, request_id=None, project_id=None, instance_id=None, logic_db_name=None, sql_black_list_prefix_check=None, sql_black_list_regex_check=None):
        r"""ConfigSqlBlacklistReqV3VO

        The model defined in huaweicloud sdk

        :param sql_black_list_full_check: **参数解释**：  全量匹配sql黑名单。  **约束限制**：  不涉及  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type sql_black_list_full_check: str
        :param request_id: **参数解释**：  请求ID。  **约束限制**：  不涉及  **取值范围**：  只能由英文字母、数字组成。  **默认取值**：  不涉及。
        :type request_id: str
        :param project_id: **参数解释**：  租户在某一Region下的project ID。  获取方法请参见[获取项目ID](https://support.huaweicloud.com/api-ddm/ddm_api_01_0063.html)。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，且长度为32个字符。  **默认取值**：  不涉及。 
        :type project_id: str
        :param instance_id: **参数解释**：  实例ID，此参数是实例的唯一标识。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in09，长度为36个字符。  **默认取值**：  不涉及。
        :type instance_id: str
        :param logic_db_name: **参数解释**：  逻辑库名称。  **约束限制**：  不涉及  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type logic_db_name: str
        :param sql_black_list_prefix_check: **参数解释**：  前缀匹配sql黑名单。  **约束限制**：  不涉及  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type sql_black_list_prefix_check: str
        :param sql_black_list_regex_check: **参数解释**：  正则匹配sql黑名单。  **约束限制**：  不涉及  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type sql_black_list_regex_check: str
        """
        
        

        self._sql_black_list_full_check = None
        self._request_id = None
        self._project_id = None
        self._instance_id = None
        self._logic_db_name = None
        self._sql_black_list_prefix_check = None
        self._sql_black_list_regex_check = None
        self.discriminator = None

        if sql_black_list_full_check is not None:
            self.sql_black_list_full_check = sql_black_list_full_check
        if request_id is not None:
            self.request_id = request_id
        if project_id is not None:
            self.project_id = project_id
        if instance_id is not None:
            self.instance_id = instance_id
        if logic_db_name is not None:
            self.logic_db_name = logic_db_name
        if sql_black_list_prefix_check is not None:
            self.sql_black_list_prefix_check = sql_black_list_prefix_check
        if sql_black_list_regex_check is not None:
            self.sql_black_list_regex_check = sql_black_list_regex_check

    @property
    def sql_black_list_full_check(self):
        r"""Gets the sql_black_list_full_check of this ConfigSqlBlacklistReqV3VO.

        **参数解释**：  全量匹配sql黑名单。  **约束限制**：  不涉及  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The sql_black_list_full_check of this ConfigSqlBlacklistReqV3VO.
        :rtype: str
        """
        return self._sql_black_list_full_check

    @sql_black_list_full_check.setter
    def sql_black_list_full_check(self, sql_black_list_full_check):
        r"""Sets the sql_black_list_full_check of this ConfigSqlBlacklistReqV3VO.

        **参数解释**：  全量匹配sql黑名单。  **约束限制**：  不涉及  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param sql_black_list_full_check: The sql_black_list_full_check of this ConfigSqlBlacklistReqV3VO.
        :type sql_black_list_full_check: str
        """
        self._sql_black_list_full_check = sql_black_list_full_check

    @property
    def request_id(self):
        r"""Gets the request_id of this ConfigSqlBlacklistReqV3VO.

        **参数解释**：  请求ID。  **约束限制**：  不涉及  **取值范围**：  只能由英文字母、数字组成。  **默认取值**：  不涉及。

        :return: The request_id of this ConfigSqlBlacklistReqV3VO.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ConfigSqlBlacklistReqV3VO.

        **参数解释**：  请求ID。  **约束限制**：  不涉及  **取值范围**：  只能由英文字母、数字组成。  **默认取值**：  不涉及。

        :param request_id: The request_id of this ConfigSqlBlacklistReqV3VO.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ConfigSqlBlacklistReqV3VO.

        **参数解释**：  租户在某一Region下的project ID。  获取方法请参见[获取项目ID](https://support.huaweicloud.com/api-ddm/ddm_api_01_0063.html)。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，且长度为32个字符。  **默认取值**：  不涉及。 

        :return: The project_id of this ConfigSqlBlacklistReqV3VO.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ConfigSqlBlacklistReqV3VO.

        **参数解释**：  租户在某一Region下的project ID。  获取方法请参见[获取项目ID](https://support.huaweicloud.com/api-ddm/ddm_api_01_0063.html)。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，且长度为32个字符。  **默认取值**：  不涉及。 

        :param project_id: The project_id of this ConfigSqlBlacklistReqV3VO.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ConfigSqlBlacklistReqV3VO.

        **参数解释**：  实例ID，此参数是实例的唯一标识。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in09，长度为36个字符。  **默认取值**：  不涉及。

        :return: The instance_id of this ConfigSqlBlacklistReqV3VO.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ConfigSqlBlacklistReqV3VO.

        **参数解释**：  实例ID，此参数是实例的唯一标识。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in09，长度为36个字符。  **默认取值**：  不涉及。

        :param instance_id: The instance_id of this ConfigSqlBlacklistReqV3VO.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def logic_db_name(self):
        r"""Gets the logic_db_name of this ConfigSqlBlacklistReqV3VO.

        **参数解释**：  逻辑库名称。  **约束限制**：  不涉及  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The logic_db_name of this ConfigSqlBlacklistReqV3VO.
        :rtype: str
        """
        return self._logic_db_name

    @logic_db_name.setter
    def logic_db_name(self, logic_db_name):
        r"""Sets the logic_db_name of this ConfigSqlBlacklistReqV3VO.

        **参数解释**：  逻辑库名称。  **约束限制**：  不涉及  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param logic_db_name: The logic_db_name of this ConfigSqlBlacklistReqV3VO.
        :type logic_db_name: str
        """
        self._logic_db_name = logic_db_name

    @property
    def sql_black_list_prefix_check(self):
        r"""Gets the sql_black_list_prefix_check of this ConfigSqlBlacklistReqV3VO.

        **参数解释**：  前缀匹配sql黑名单。  **约束限制**：  不涉及  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The sql_black_list_prefix_check of this ConfigSqlBlacklistReqV3VO.
        :rtype: str
        """
        return self._sql_black_list_prefix_check

    @sql_black_list_prefix_check.setter
    def sql_black_list_prefix_check(self, sql_black_list_prefix_check):
        r"""Sets the sql_black_list_prefix_check of this ConfigSqlBlacklistReqV3VO.

        **参数解释**：  前缀匹配sql黑名单。  **约束限制**：  不涉及  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param sql_black_list_prefix_check: The sql_black_list_prefix_check of this ConfigSqlBlacklistReqV3VO.
        :type sql_black_list_prefix_check: str
        """
        self._sql_black_list_prefix_check = sql_black_list_prefix_check

    @property
    def sql_black_list_regex_check(self):
        r"""Gets the sql_black_list_regex_check of this ConfigSqlBlacklistReqV3VO.

        **参数解释**：  正则匹配sql黑名单。  **约束限制**：  不涉及  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The sql_black_list_regex_check of this ConfigSqlBlacklistReqV3VO.
        :rtype: str
        """
        return self._sql_black_list_regex_check

    @sql_black_list_regex_check.setter
    def sql_black_list_regex_check(self, sql_black_list_regex_check):
        r"""Sets the sql_black_list_regex_check of this ConfigSqlBlacklistReqV3VO.

        **参数解释**：  正则匹配sql黑名单。  **约束限制**：  不涉及  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param sql_black_list_regex_check: The sql_black_list_regex_check of this ConfigSqlBlacklistReqV3VO.
        :type sql_black_list_regex_check: str
        """
        self._sql_black_list_regex_check = sql_black_list_regex_check

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
        if not isinstance(other, ConfigSqlBlacklistReqV3VO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
