# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmTemplates:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_id': 'str',
        'template_name': 'str',
        'template_type': 'TemplateType',
        'create_time': 'datetime',
        'template_description': 'str',
        'association_alarm_total': 'int',
        'policy_total': 'int',
        'policy_statistics': 'list[PolicyStatistics]',
        'association_resource_groups': 'list[AssociationResourceGroup]'
    }

    attribute_map = {
        'template_id': 'template_id',
        'template_name': 'template_name',
        'template_type': 'template_type',
        'create_time': 'create_time',
        'template_description': 'template_description',
        'association_alarm_total': 'association_alarm_total',
        'policy_total': 'policy_total',
        'policy_statistics': 'policy_statistics',
        'association_resource_groups': 'association_resource_groups'
    }

    def __init__(self, template_id=None, template_name=None, template_type=None, create_time=None, template_description=None, association_alarm_total=None, policy_total=None, policy_statistics=None, association_resource_groups=None):
        """AlarmTemplates

        The model defined in huaweicloud sdk

        :param template_id: 告警模板的ID，以at开头，后跟字母、数字，长度最长为64
        :type template_id: str
        :param template_name: 告警模板的名称，以字母或汉字开头，可包含字母、数字、汉字、_、-，长度范围[1,128]
        :type template_name: str
        :param template_type: 
        :type template_type: :class:`huaweicloudsdkces.v2.TemplateType`
        :param create_time: 告警模板的创建时间
        :type create_time: datetime
        :param template_description: 告警模板的描述，长度范围[0,256]，该字段默认值为空字符串
        :type template_description: str
        :param association_alarm_total: 告警模板关联的告警规则数目
        :type association_alarm_total: int
        :param policy_total: 告警模板的告警策略总数
        :type policy_total: int
        :param policy_statistics: 服务列表告警策略数目统计
        :type policy_statistics: list[:class:`huaweicloudsdkces.v2.PolicyStatistics`]
        :param association_resource_groups: 关联的资源分组
        :type association_resource_groups: list[:class:`huaweicloudsdkces.v2.AssociationResourceGroup`]
        """
        
        

        self._template_id = None
        self._template_name = None
        self._template_type = None
        self._create_time = None
        self._template_description = None
        self._association_alarm_total = None
        self._policy_total = None
        self._policy_statistics = None
        self._association_resource_groups = None
        self.discriminator = None

        self.template_id = template_id
        self.template_name = template_name
        self.template_type = template_type
        self.create_time = create_time
        self.template_description = template_description
        if association_alarm_total is not None:
            self.association_alarm_total = association_alarm_total
        self.policy_total = policy_total
        self.policy_statistics = policy_statistics
        if association_resource_groups is not None:
            self.association_resource_groups = association_resource_groups

    @property
    def template_id(self):
        """Gets the template_id of this AlarmTemplates.

        告警模板的ID，以at开头，后跟字母、数字，长度最长为64

        :return: The template_id of this AlarmTemplates.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this AlarmTemplates.

        告警模板的ID，以at开头，后跟字母、数字，长度最长为64

        :param template_id: The template_id of this AlarmTemplates.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def template_name(self):
        """Gets the template_name of this AlarmTemplates.

        告警模板的名称，以字母或汉字开头，可包含字母、数字、汉字、_、-，长度范围[1,128]

        :return: The template_name of this AlarmTemplates.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this AlarmTemplates.

        告警模板的名称，以字母或汉字开头，可包含字母、数字、汉字、_、-，长度范围[1,128]

        :param template_name: The template_name of this AlarmTemplates.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def template_type(self):
        """Gets the template_type of this AlarmTemplates.

        :return: The template_type of this AlarmTemplates.
        :rtype: :class:`huaweicloudsdkces.v2.TemplateType`
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        """Sets the template_type of this AlarmTemplates.

        :param template_type: The template_type of this AlarmTemplates.
        :type template_type: :class:`huaweicloudsdkces.v2.TemplateType`
        """
        self._template_type = template_type

    @property
    def create_time(self):
        """Gets the create_time of this AlarmTemplates.

        告警模板的创建时间

        :return: The create_time of this AlarmTemplates.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this AlarmTemplates.

        告警模板的创建时间

        :param create_time: The create_time of this AlarmTemplates.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def template_description(self):
        """Gets the template_description of this AlarmTemplates.

        告警模板的描述，长度范围[0,256]，该字段默认值为空字符串

        :return: The template_description of this AlarmTemplates.
        :rtype: str
        """
        return self._template_description

    @template_description.setter
    def template_description(self, template_description):
        """Sets the template_description of this AlarmTemplates.

        告警模板的描述，长度范围[0,256]，该字段默认值为空字符串

        :param template_description: The template_description of this AlarmTemplates.
        :type template_description: str
        """
        self._template_description = template_description

    @property
    def association_alarm_total(self):
        """Gets the association_alarm_total of this AlarmTemplates.

        告警模板关联的告警规则数目

        :return: The association_alarm_total of this AlarmTemplates.
        :rtype: int
        """
        return self._association_alarm_total

    @association_alarm_total.setter
    def association_alarm_total(self, association_alarm_total):
        """Sets the association_alarm_total of this AlarmTemplates.

        告警模板关联的告警规则数目

        :param association_alarm_total: The association_alarm_total of this AlarmTemplates.
        :type association_alarm_total: int
        """
        self._association_alarm_total = association_alarm_total

    @property
    def policy_total(self):
        """Gets the policy_total of this AlarmTemplates.

        告警模板的告警策略总数

        :return: The policy_total of this AlarmTemplates.
        :rtype: int
        """
        return self._policy_total

    @policy_total.setter
    def policy_total(self, policy_total):
        """Sets the policy_total of this AlarmTemplates.

        告警模板的告警策略总数

        :param policy_total: The policy_total of this AlarmTemplates.
        :type policy_total: int
        """
        self._policy_total = policy_total

    @property
    def policy_statistics(self):
        """Gets the policy_statistics of this AlarmTemplates.

        服务列表告警策略数目统计

        :return: The policy_statistics of this AlarmTemplates.
        :rtype: list[:class:`huaweicloudsdkces.v2.PolicyStatistics`]
        """
        return self._policy_statistics

    @policy_statistics.setter
    def policy_statistics(self, policy_statistics):
        """Sets the policy_statistics of this AlarmTemplates.

        服务列表告警策略数目统计

        :param policy_statistics: The policy_statistics of this AlarmTemplates.
        :type policy_statistics: list[:class:`huaweicloudsdkces.v2.PolicyStatistics`]
        """
        self._policy_statistics = policy_statistics

    @property
    def association_resource_groups(self):
        """Gets the association_resource_groups of this AlarmTemplates.

        关联的资源分组

        :return: The association_resource_groups of this AlarmTemplates.
        :rtype: list[:class:`huaweicloudsdkces.v2.AssociationResourceGroup`]
        """
        return self._association_resource_groups

    @association_resource_groups.setter
    def association_resource_groups(self, association_resource_groups):
        """Sets the association_resource_groups of this AlarmTemplates.

        关联的资源分组

        :param association_resource_groups: The association_resource_groups of this AlarmTemplates.
        :type association_resource_groups: list[:class:`huaweicloudsdkces.v2.AssociationResourceGroup`]
        """
        self._association_resource_groups = association_resource_groups

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
        if not isinstance(other, AlarmTemplates):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
