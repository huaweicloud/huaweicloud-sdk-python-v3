# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DomainsWithPort:

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
        'business_type': 'str',
        'domain_status': 'str',
        'cname': 'str',
        'sources': 'list[SourcesConfig]',
        'https_status': 'int',
        'create_time': 'int',
        'update_time': 'int',
        'disabled': 'int',
        'locked': 'int',
        'service_area': 'str',
        'banned_reason': 'str',
        'locked_reason': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'business_type': 'business_type',
        'domain_status': 'domain_status',
        'cname': 'cname',
        'sources': 'sources',
        'https_status': 'https_status',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'disabled': 'disabled',
        'locked': 'locked',
        'service_area': 'service_area',
        'banned_reason': 'banned_reason',
        'locked_reason': 'locked_reason',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, id=None, business_type=None, domain_status=None, cname=None, sources=None, https_status=None, create_time=None, update_time=None, disabled=None, locked=None, service_area=None, banned_reason=None, locked_reason=None, enterprise_project_id=None):
        """DomainsWithPort

        The model defined in huaweicloud sdk

        :param id: 加速域名ID。
        :type id: str
        :param business_type: 域名业务类型，若为web，则表示类型为网站加速；若为download，则表示业务类型为文件下载加速；若为video，则表示业务类型为点播加速；若为wholeSite，则表示类型为全站加速。
        :type business_type: str
        :param domain_status: 加速域名状态。取值意义： - online表示“已开启” - offline表示“已停用” - configuring表示“配置中” - configure_failed表示“配置失败” - checking表示“审核中” - check_failed表示“审核未通过” - deleting表示“删除中”。
        :type domain_status: str
        :param cname: 加速域名对应的CNAME。
        :type cname: str
        :param sources: 源站域名或源站IP，源站为IP类型时，仅支持IPv4，如需传入多个源站IP，以多个源站对象传入，除IP其他参数请保持一致，主源站最多支持15个源站IP对象，备源站最多支持15个源站IP对象；源站为域名类型时仅支持1个源站对象。不支持IP源站和域名源站混用。
        :type sources: list[:class:`huaweicloudsdkcdn.v2.SourcesConfig`]
        :param https_status: 是否开启HTTPS加速。 0：代表未开启HTTPS加速； 1：代表开启HTTPS加速，且回源方式为协议跟随； 2：代表开启HTTPS加速，且回源方式为HTTP； 3：代表开启HTTPS加速，且回源方式为HTTPS。
        :type https_status: int
        :param create_time: 域名创建时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。
        :type create_time: int
        :param update_time: 域名修改时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。
        :type update_time: int
        :param disabled: 封禁状态（0代表未禁用；1代表禁用）。
        :type disabled: int
        :param locked: 锁定状态（0代表未锁定；1代表锁定）。
        :type locked: int
        :param service_area: 华为云CDN提供的加速服务范围，包含：mainland_china中国大陆、outside_mainland_china中国大陆境外、global全球。
        :type service_area: str
        :param banned_reason: 域名禁用原因。 1：该域名涉嫌违规内容（涉黄/涉赌/涉毒/涉政）已被禁用； 2：该域名因备案失效已被禁用； 3：该域名遭受攻击，已被禁用； 150：该域名涉嫌违规内容涉黄已被禁用； 151：该域名涉嫌违规内容涉政已被禁用； 152：该域名涉嫌违规内容涉暴已被禁用； 153：该域名涉嫌违规内容涉赌已被禁用。
        :type banned_reason: str
        :param locked_reason: 域名锁定原因（Changing the config, please wait）。
        :type locked_reason: str
        :param enterprise_project_id: 当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，不传表示查询默认项目。注意：当使用子帐号调用接口时，该参数必传。  您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。       
        :type enterprise_project_id: str
        """
        
        

        self._id = None
        self._business_type = None
        self._domain_status = None
        self._cname = None
        self._sources = None
        self._https_status = None
        self._create_time = None
        self._update_time = None
        self._disabled = None
        self._locked = None
        self._service_area = None
        self._banned_reason = None
        self._locked_reason = None
        self._enterprise_project_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if business_type is not None:
            self.business_type = business_type
        if domain_status is not None:
            self.domain_status = domain_status
        if cname is not None:
            self.cname = cname
        if sources is not None:
            self.sources = sources
        if https_status is not None:
            self.https_status = https_status
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if disabled is not None:
            self.disabled = disabled
        if locked is not None:
            self.locked = locked
        if service_area is not None:
            self.service_area = service_area
        if banned_reason is not None:
            self.banned_reason = banned_reason
        if locked_reason is not None:
            self.locked_reason = locked_reason
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        """Gets the id of this DomainsWithPort.

        加速域名ID。

        :return: The id of this DomainsWithPort.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DomainsWithPort.

        加速域名ID。

        :param id: The id of this DomainsWithPort.
        :type id: str
        """
        self._id = id

    @property
    def business_type(self):
        """Gets the business_type of this DomainsWithPort.

        域名业务类型，若为web，则表示类型为网站加速；若为download，则表示业务类型为文件下载加速；若为video，则表示业务类型为点播加速；若为wholeSite，则表示类型为全站加速。

        :return: The business_type of this DomainsWithPort.
        :rtype: str
        """
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        """Sets the business_type of this DomainsWithPort.

        域名业务类型，若为web，则表示类型为网站加速；若为download，则表示业务类型为文件下载加速；若为video，则表示业务类型为点播加速；若为wholeSite，则表示类型为全站加速。

        :param business_type: The business_type of this DomainsWithPort.
        :type business_type: str
        """
        self._business_type = business_type

    @property
    def domain_status(self):
        """Gets the domain_status of this DomainsWithPort.

        加速域名状态。取值意义： - online表示“已开启” - offline表示“已停用” - configuring表示“配置中” - configure_failed表示“配置失败” - checking表示“审核中” - check_failed表示“审核未通过” - deleting表示“删除中”。

        :return: The domain_status of this DomainsWithPort.
        :rtype: str
        """
        return self._domain_status

    @domain_status.setter
    def domain_status(self, domain_status):
        """Sets the domain_status of this DomainsWithPort.

        加速域名状态。取值意义： - online表示“已开启” - offline表示“已停用” - configuring表示“配置中” - configure_failed表示“配置失败” - checking表示“审核中” - check_failed表示“审核未通过” - deleting表示“删除中”。

        :param domain_status: The domain_status of this DomainsWithPort.
        :type domain_status: str
        """
        self._domain_status = domain_status

    @property
    def cname(self):
        """Gets the cname of this DomainsWithPort.

        加速域名对应的CNAME。

        :return: The cname of this DomainsWithPort.
        :rtype: str
        """
        return self._cname

    @cname.setter
    def cname(self, cname):
        """Sets the cname of this DomainsWithPort.

        加速域名对应的CNAME。

        :param cname: The cname of this DomainsWithPort.
        :type cname: str
        """
        self._cname = cname

    @property
    def sources(self):
        """Gets the sources of this DomainsWithPort.

        源站域名或源站IP，源站为IP类型时，仅支持IPv4，如需传入多个源站IP，以多个源站对象传入，除IP其他参数请保持一致，主源站最多支持15个源站IP对象，备源站最多支持15个源站IP对象；源站为域名类型时仅支持1个源站对象。不支持IP源站和域名源站混用。

        :return: The sources of this DomainsWithPort.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.SourcesConfig`]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this DomainsWithPort.

        源站域名或源站IP，源站为IP类型时，仅支持IPv4，如需传入多个源站IP，以多个源站对象传入，除IP其他参数请保持一致，主源站最多支持15个源站IP对象，备源站最多支持15个源站IP对象；源站为域名类型时仅支持1个源站对象。不支持IP源站和域名源站混用。

        :param sources: The sources of this DomainsWithPort.
        :type sources: list[:class:`huaweicloudsdkcdn.v2.SourcesConfig`]
        """
        self._sources = sources

    @property
    def https_status(self):
        """Gets the https_status of this DomainsWithPort.

        是否开启HTTPS加速。 0：代表未开启HTTPS加速； 1：代表开启HTTPS加速，且回源方式为协议跟随； 2：代表开启HTTPS加速，且回源方式为HTTP； 3：代表开启HTTPS加速，且回源方式为HTTPS。

        :return: The https_status of this DomainsWithPort.
        :rtype: int
        """
        return self._https_status

    @https_status.setter
    def https_status(self, https_status):
        """Sets the https_status of this DomainsWithPort.

        是否开启HTTPS加速。 0：代表未开启HTTPS加速； 1：代表开启HTTPS加速，且回源方式为协议跟随； 2：代表开启HTTPS加速，且回源方式为HTTP； 3：代表开启HTTPS加速，且回源方式为HTTPS。

        :param https_status: The https_status of this DomainsWithPort.
        :type https_status: int
        """
        self._https_status = https_status

    @property
    def create_time(self):
        """Gets the create_time of this DomainsWithPort.

        域名创建时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。

        :return: The create_time of this DomainsWithPort.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this DomainsWithPort.

        域名创建时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。

        :param create_time: The create_time of this DomainsWithPort.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this DomainsWithPort.

        域名修改时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。

        :return: The update_time of this DomainsWithPort.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this DomainsWithPort.

        域名修改时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。

        :param update_time: The update_time of this DomainsWithPort.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def disabled(self):
        """Gets the disabled of this DomainsWithPort.

        封禁状态（0代表未禁用；1代表禁用）。

        :return: The disabled of this DomainsWithPort.
        :rtype: int
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this DomainsWithPort.

        封禁状态（0代表未禁用；1代表禁用）。

        :param disabled: The disabled of this DomainsWithPort.
        :type disabled: int
        """
        self._disabled = disabled

    @property
    def locked(self):
        """Gets the locked of this DomainsWithPort.

        锁定状态（0代表未锁定；1代表锁定）。

        :return: The locked of this DomainsWithPort.
        :rtype: int
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this DomainsWithPort.

        锁定状态（0代表未锁定；1代表锁定）。

        :param locked: The locked of this DomainsWithPort.
        :type locked: int
        """
        self._locked = locked

    @property
    def service_area(self):
        """Gets the service_area of this DomainsWithPort.

        华为云CDN提供的加速服务范围，包含：mainland_china中国大陆、outside_mainland_china中国大陆境外、global全球。

        :return: The service_area of this DomainsWithPort.
        :rtype: str
        """
        return self._service_area

    @service_area.setter
    def service_area(self, service_area):
        """Sets the service_area of this DomainsWithPort.

        华为云CDN提供的加速服务范围，包含：mainland_china中国大陆、outside_mainland_china中国大陆境外、global全球。

        :param service_area: The service_area of this DomainsWithPort.
        :type service_area: str
        """
        self._service_area = service_area

    @property
    def banned_reason(self):
        """Gets the banned_reason of this DomainsWithPort.

        域名禁用原因。 1：该域名涉嫌违规内容（涉黄/涉赌/涉毒/涉政）已被禁用； 2：该域名因备案失效已被禁用； 3：该域名遭受攻击，已被禁用； 150：该域名涉嫌违规内容涉黄已被禁用； 151：该域名涉嫌违规内容涉政已被禁用； 152：该域名涉嫌违规内容涉暴已被禁用； 153：该域名涉嫌违规内容涉赌已被禁用。

        :return: The banned_reason of this DomainsWithPort.
        :rtype: str
        """
        return self._banned_reason

    @banned_reason.setter
    def banned_reason(self, banned_reason):
        """Sets the banned_reason of this DomainsWithPort.

        域名禁用原因。 1：该域名涉嫌违规内容（涉黄/涉赌/涉毒/涉政）已被禁用； 2：该域名因备案失效已被禁用； 3：该域名遭受攻击，已被禁用； 150：该域名涉嫌违规内容涉黄已被禁用； 151：该域名涉嫌违规内容涉政已被禁用； 152：该域名涉嫌违规内容涉暴已被禁用； 153：该域名涉嫌违规内容涉赌已被禁用。

        :param banned_reason: The banned_reason of this DomainsWithPort.
        :type banned_reason: str
        """
        self._banned_reason = banned_reason

    @property
    def locked_reason(self):
        """Gets the locked_reason of this DomainsWithPort.

        域名锁定原因（Changing the config, please wait）。

        :return: The locked_reason of this DomainsWithPort.
        :rtype: str
        """
        return self._locked_reason

    @locked_reason.setter
    def locked_reason(self, locked_reason):
        """Sets the locked_reason of this DomainsWithPort.

        域名锁定原因（Changing the config, please wait）。

        :param locked_reason: The locked_reason of this DomainsWithPort.
        :type locked_reason: str
        """
        self._locked_reason = locked_reason

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this DomainsWithPort.

        当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，不传表示查询默认项目。注意：当使用子帐号调用接口时，该参数必传。  您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。       

        :return: The enterprise_project_id of this DomainsWithPort.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this DomainsWithPort.

        当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，不传表示查询默认项目。注意：当使用子帐号调用接口时，该参数必传。  您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。       

        :param enterprise_project_id: The enterprise_project_id of this DomainsWithPort.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, DomainsWithPort):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other