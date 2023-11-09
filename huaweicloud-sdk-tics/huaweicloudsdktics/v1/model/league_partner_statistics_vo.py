# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LeaguePartnerStatisticsVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'partner_access_cnt': 'int',
        'partner_domain_alias': 'str',
        'partner_domain_name': 'str',
        'partner_job_cnt': 'int',
        'partner_job_ins_cnt': 'int',
        'partner_job_ins_fail_cnt': 'int',
        'partner_job_ins_intercept_cnt': 'int',
        'partner_job_ins_success_cnt': 'int'
    }

    attribute_map = {
        'partner_access_cnt': 'partner_access_cnt',
        'partner_domain_alias': 'partner_domain_alias',
        'partner_domain_name': 'partner_domain_name',
        'partner_job_cnt': 'partner_job_cnt',
        'partner_job_ins_cnt': 'partner_job_ins_cnt',
        'partner_job_ins_fail_cnt': 'partner_job_ins_fail_cnt',
        'partner_job_ins_intercept_cnt': 'partner_job_ins_intercept_cnt',
        'partner_job_ins_success_cnt': 'partner_job_ins_success_cnt'
    }

    def __init__(self, partner_access_cnt=None, partner_domain_alias=None, partner_domain_name=None, partner_job_cnt=None, partner_job_ins_cnt=None, partner_job_ins_fail_cnt=None, partner_job_ins_intercept_cnt=None, partner_job_ins_success_cnt=None):
        """LeaguePartnerStatisticsVo

        The model defined in huaweicloud sdk

        :param partner_access_cnt: 合作方访问次数
        :type partner_access_cnt: int
        :param partner_domain_alias: 租户别名
        :type partner_domain_alias: str
        :param partner_domain_name: 租户名
        :type partner_domain_name: str
        :param partner_job_cnt: 作业总数
        :type partner_job_cnt: int
        :param partner_job_ins_cnt: 实例总数
        :type partner_job_ins_cnt: int
        :param partner_job_ins_fail_cnt: 实例失败数
        :type partner_job_ins_fail_cnt: int
        :param partner_job_ins_intercept_cnt: 实例拦截数
        :type partner_job_ins_intercept_cnt: int
        :param partner_job_ins_success_cnt: 实例成功数
        :type partner_job_ins_success_cnt: int
        """
        
        

        self._partner_access_cnt = None
        self._partner_domain_alias = None
        self._partner_domain_name = None
        self._partner_job_cnt = None
        self._partner_job_ins_cnt = None
        self._partner_job_ins_fail_cnt = None
        self._partner_job_ins_intercept_cnt = None
        self._partner_job_ins_success_cnt = None
        self.discriminator = None

        if partner_access_cnt is not None:
            self.partner_access_cnt = partner_access_cnt
        if partner_domain_alias is not None:
            self.partner_domain_alias = partner_domain_alias
        if partner_domain_name is not None:
            self.partner_domain_name = partner_domain_name
        if partner_job_cnt is not None:
            self.partner_job_cnt = partner_job_cnt
        if partner_job_ins_cnt is not None:
            self.partner_job_ins_cnt = partner_job_ins_cnt
        if partner_job_ins_fail_cnt is not None:
            self.partner_job_ins_fail_cnt = partner_job_ins_fail_cnt
        if partner_job_ins_intercept_cnt is not None:
            self.partner_job_ins_intercept_cnt = partner_job_ins_intercept_cnt
        if partner_job_ins_success_cnt is not None:
            self.partner_job_ins_success_cnt = partner_job_ins_success_cnt

    @property
    def partner_access_cnt(self):
        """Gets the partner_access_cnt of this LeaguePartnerStatisticsVo.

        合作方访问次数

        :return: The partner_access_cnt of this LeaguePartnerStatisticsVo.
        :rtype: int
        """
        return self._partner_access_cnt

    @partner_access_cnt.setter
    def partner_access_cnt(self, partner_access_cnt):
        """Sets the partner_access_cnt of this LeaguePartnerStatisticsVo.

        合作方访问次数

        :param partner_access_cnt: The partner_access_cnt of this LeaguePartnerStatisticsVo.
        :type partner_access_cnt: int
        """
        self._partner_access_cnt = partner_access_cnt

    @property
    def partner_domain_alias(self):
        """Gets the partner_domain_alias of this LeaguePartnerStatisticsVo.

        租户别名

        :return: The partner_domain_alias of this LeaguePartnerStatisticsVo.
        :rtype: str
        """
        return self._partner_domain_alias

    @partner_domain_alias.setter
    def partner_domain_alias(self, partner_domain_alias):
        """Sets the partner_domain_alias of this LeaguePartnerStatisticsVo.

        租户别名

        :param partner_domain_alias: The partner_domain_alias of this LeaguePartnerStatisticsVo.
        :type partner_domain_alias: str
        """
        self._partner_domain_alias = partner_domain_alias

    @property
    def partner_domain_name(self):
        """Gets the partner_domain_name of this LeaguePartnerStatisticsVo.

        租户名

        :return: The partner_domain_name of this LeaguePartnerStatisticsVo.
        :rtype: str
        """
        return self._partner_domain_name

    @partner_domain_name.setter
    def partner_domain_name(self, partner_domain_name):
        """Sets the partner_domain_name of this LeaguePartnerStatisticsVo.

        租户名

        :param partner_domain_name: The partner_domain_name of this LeaguePartnerStatisticsVo.
        :type partner_domain_name: str
        """
        self._partner_domain_name = partner_domain_name

    @property
    def partner_job_cnt(self):
        """Gets the partner_job_cnt of this LeaguePartnerStatisticsVo.

        作业总数

        :return: The partner_job_cnt of this LeaguePartnerStatisticsVo.
        :rtype: int
        """
        return self._partner_job_cnt

    @partner_job_cnt.setter
    def partner_job_cnt(self, partner_job_cnt):
        """Sets the partner_job_cnt of this LeaguePartnerStatisticsVo.

        作业总数

        :param partner_job_cnt: The partner_job_cnt of this LeaguePartnerStatisticsVo.
        :type partner_job_cnt: int
        """
        self._partner_job_cnt = partner_job_cnt

    @property
    def partner_job_ins_cnt(self):
        """Gets the partner_job_ins_cnt of this LeaguePartnerStatisticsVo.

        实例总数

        :return: The partner_job_ins_cnt of this LeaguePartnerStatisticsVo.
        :rtype: int
        """
        return self._partner_job_ins_cnt

    @partner_job_ins_cnt.setter
    def partner_job_ins_cnt(self, partner_job_ins_cnt):
        """Sets the partner_job_ins_cnt of this LeaguePartnerStatisticsVo.

        实例总数

        :param partner_job_ins_cnt: The partner_job_ins_cnt of this LeaguePartnerStatisticsVo.
        :type partner_job_ins_cnt: int
        """
        self._partner_job_ins_cnt = partner_job_ins_cnt

    @property
    def partner_job_ins_fail_cnt(self):
        """Gets the partner_job_ins_fail_cnt of this LeaguePartnerStatisticsVo.

        实例失败数

        :return: The partner_job_ins_fail_cnt of this LeaguePartnerStatisticsVo.
        :rtype: int
        """
        return self._partner_job_ins_fail_cnt

    @partner_job_ins_fail_cnt.setter
    def partner_job_ins_fail_cnt(self, partner_job_ins_fail_cnt):
        """Sets the partner_job_ins_fail_cnt of this LeaguePartnerStatisticsVo.

        实例失败数

        :param partner_job_ins_fail_cnt: The partner_job_ins_fail_cnt of this LeaguePartnerStatisticsVo.
        :type partner_job_ins_fail_cnt: int
        """
        self._partner_job_ins_fail_cnt = partner_job_ins_fail_cnt

    @property
    def partner_job_ins_intercept_cnt(self):
        """Gets the partner_job_ins_intercept_cnt of this LeaguePartnerStatisticsVo.

        实例拦截数

        :return: The partner_job_ins_intercept_cnt of this LeaguePartnerStatisticsVo.
        :rtype: int
        """
        return self._partner_job_ins_intercept_cnt

    @partner_job_ins_intercept_cnt.setter
    def partner_job_ins_intercept_cnt(self, partner_job_ins_intercept_cnt):
        """Sets the partner_job_ins_intercept_cnt of this LeaguePartnerStatisticsVo.

        实例拦截数

        :param partner_job_ins_intercept_cnt: The partner_job_ins_intercept_cnt of this LeaguePartnerStatisticsVo.
        :type partner_job_ins_intercept_cnt: int
        """
        self._partner_job_ins_intercept_cnt = partner_job_ins_intercept_cnt

    @property
    def partner_job_ins_success_cnt(self):
        """Gets the partner_job_ins_success_cnt of this LeaguePartnerStatisticsVo.

        实例成功数

        :return: The partner_job_ins_success_cnt of this LeaguePartnerStatisticsVo.
        :rtype: int
        """
        return self._partner_job_ins_success_cnt

    @partner_job_ins_success_cnt.setter
    def partner_job_ins_success_cnt(self, partner_job_ins_success_cnt):
        """Sets the partner_job_ins_success_cnt of this LeaguePartnerStatisticsVo.

        实例成功数

        :param partner_job_ins_success_cnt: The partner_job_ins_success_cnt of this LeaguePartnerStatisticsVo.
        :type partner_job_ins_success_cnt: int
        """
        self._partner_job_ins_success_cnt = partner_job_ins_success_cnt

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
        if not isinstance(other, LeaguePartnerStatisticsVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
