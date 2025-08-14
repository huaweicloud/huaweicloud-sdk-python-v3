# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeBaselineWhiteListRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'rule_type': 'str',
        'host_id_list': 'list[str]',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'rule_type': 'rule_type',
        'host_id_list': 'host_id_list',
        'description': 'description'
    }

    def __init__(self, id=None, rule_type=None, host_id_list=None, description=None):
        r"""ChangeBaselineWhiteListRequestBody

        The model defined in huaweicloud sdk

        :param id: 被修改的白名单id
        :type id: str
        :param rule_type: 基线检查白名单的规则范围 - specific_host：部分主机 - all_host：全部主机
        :type rule_type: str
        :param host_id_list: rule_type为specific_host时，该字段为待修改的白名单主机id列表，rule_type为all_host时无该字段
        :type host_id_list: list[str]
        :param description: 基线白名单备注
        :type description: str
        """
        
        

        self._id = None
        self._rule_type = None
        self._host_id_list = None
        self._description = None
        self.discriminator = None

        self.id = id
        self.rule_type = rule_type
        if host_id_list is not None:
            self.host_id_list = host_id_list
        if description is not None:
            self.description = description

    @property
    def id(self):
        r"""Gets the id of this ChangeBaselineWhiteListRequestBody.

        被修改的白名单id

        :return: The id of this ChangeBaselineWhiteListRequestBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ChangeBaselineWhiteListRequestBody.

        被修改的白名单id

        :param id: The id of this ChangeBaselineWhiteListRequestBody.
        :type id: str
        """
        self._id = id

    @property
    def rule_type(self):
        r"""Gets the rule_type of this ChangeBaselineWhiteListRequestBody.

        基线检查白名单的规则范围 - specific_host：部分主机 - all_host：全部主机

        :return: The rule_type of this ChangeBaselineWhiteListRequestBody.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        r"""Sets the rule_type of this ChangeBaselineWhiteListRequestBody.

        基线检查白名单的规则范围 - specific_host：部分主机 - all_host：全部主机

        :param rule_type: The rule_type of this ChangeBaselineWhiteListRequestBody.
        :type rule_type: str
        """
        self._rule_type = rule_type

    @property
    def host_id_list(self):
        r"""Gets the host_id_list of this ChangeBaselineWhiteListRequestBody.

        rule_type为specific_host时，该字段为待修改的白名单主机id列表，rule_type为all_host时无该字段

        :return: The host_id_list of this ChangeBaselineWhiteListRequestBody.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        r"""Sets the host_id_list of this ChangeBaselineWhiteListRequestBody.

        rule_type为specific_host时，该字段为待修改的白名单主机id列表，rule_type为all_host时无该字段

        :param host_id_list: The host_id_list of this ChangeBaselineWhiteListRequestBody.
        :type host_id_list: list[str]
        """
        self._host_id_list = host_id_list

    @property
    def description(self):
        r"""Gets the description of this ChangeBaselineWhiteListRequestBody.

        基线白名单备注

        :return: The description of this ChangeBaselineWhiteListRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ChangeBaselineWhiteListRequestBody.

        基线白名单备注

        :param description: The description of this ChangeBaselineWhiteListRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, ChangeBaselineWhiteListRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
