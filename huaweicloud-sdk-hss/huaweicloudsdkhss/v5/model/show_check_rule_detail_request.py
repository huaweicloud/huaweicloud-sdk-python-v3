# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCheckRuleDetailRequest:

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
        'check_name': 'str',
        'check_type': 'str',
        'check_rule_id': 'str',
        'standard': 'str',
        'host_id': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'check_name': 'check_name',
        'check_type': 'check_type',
        'check_rule_id': 'check_rule_id',
        'standard': 'standard',
        'host_id': 'host_id'
    }

    def __init__(self, enterprise_project_id=None, check_name=None, check_type=None, check_rule_id=None, standard=None, host_id=None):
        """ShowCheckRuleDetailRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 企业项目ID，查询所有企业项目时填写：all_granted_eps
        :type enterprise_project_id: str
        :param check_name: 基线名称
        :type check_name: str
        :param check_type: 基线类型
        :type check_type: str
        :param check_rule_id: 检查项ID
        :type check_rule_id: str
        :param standard: 标准类型，包含如下:   - cn_standard : 等保合规标准   - hw_standard : 华为标准   - qt_standard : 青腾标准
        :type standard: str
        :param host_id: 主机ID
        :type host_id: str
        """
        
        

        self._enterprise_project_id = None
        self._check_name = None
        self._check_type = None
        self._check_rule_id = None
        self._standard = None
        self._host_id = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.check_name = check_name
        self.check_type = check_type
        self.check_rule_id = check_rule_id
        self.standard = standard
        if host_id is not None:
            self.host_id = host_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowCheckRuleDetailRequest.

        企业项目ID，查询所有企业项目时填写：all_granted_eps

        :return: The enterprise_project_id of this ShowCheckRuleDetailRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowCheckRuleDetailRequest.

        企业项目ID，查询所有企业项目时填写：all_granted_eps

        :param enterprise_project_id: The enterprise_project_id of this ShowCheckRuleDetailRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def check_name(self):
        """Gets the check_name of this ShowCheckRuleDetailRequest.

        基线名称

        :return: The check_name of this ShowCheckRuleDetailRequest.
        :rtype: str
        """
        return self._check_name

    @check_name.setter
    def check_name(self, check_name):
        """Sets the check_name of this ShowCheckRuleDetailRequest.

        基线名称

        :param check_name: The check_name of this ShowCheckRuleDetailRequest.
        :type check_name: str
        """
        self._check_name = check_name

    @property
    def check_type(self):
        """Gets the check_type of this ShowCheckRuleDetailRequest.

        基线类型

        :return: The check_type of this ShowCheckRuleDetailRequest.
        :rtype: str
        """
        return self._check_type

    @check_type.setter
    def check_type(self, check_type):
        """Sets the check_type of this ShowCheckRuleDetailRequest.

        基线类型

        :param check_type: The check_type of this ShowCheckRuleDetailRequest.
        :type check_type: str
        """
        self._check_type = check_type

    @property
    def check_rule_id(self):
        """Gets the check_rule_id of this ShowCheckRuleDetailRequest.

        检查项ID

        :return: The check_rule_id of this ShowCheckRuleDetailRequest.
        :rtype: str
        """
        return self._check_rule_id

    @check_rule_id.setter
    def check_rule_id(self, check_rule_id):
        """Sets the check_rule_id of this ShowCheckRuleDetailRequest.

        检查项ID

        :param check_rule_id: The check_rule_id of this ShowCheckRuleDetailRequest.
        :type check_rule_id: str
        """
        self._check_rule_id = check_rule_id

    @property
    def standard(self):
        """Gets the standard of this ShowCheckRuleDetailRequest.

        标准类型，包含如下:   - cn_standard : 等保合规标准   - hw_standard : 华为标准   - qt_standard : 青腾标准

        :return: The standard of this ShowCheckRuleDetailRequest.
        :rtype: str
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        """Sets the standard of this ShowCheckRuleDetailRequest.

        标准类型，包含如下:   - cn_standard : 等保合规标准   - hw_standard : 华为标准   - qt_standard : 青腾标准

        :param standard: The standard of this ShowCheckRuleDetailRequest.
        :type standard: str
        """
        self._standard = standard

    @property
    def host_id(self):
        """Gets the host_id of this ShowCheckRuleDetailRequest.

        主机ID

        :return: The host_id of this ShowCheckRuleDetailRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this ShowCheckRuleDetailRequest.

        主机ID

        :param host_id: The host_id of this ShowCheckRuleDetailRequest.
        :type host_id: str
        """
        self._host_id = host_id

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
        if not isinstance(other, ShowCheckRuleDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
