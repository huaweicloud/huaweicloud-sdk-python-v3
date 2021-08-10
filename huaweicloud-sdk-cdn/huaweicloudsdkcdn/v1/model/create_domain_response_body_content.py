# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDomainResponseBodyContent:


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
        'domain_name': 'str',
        'business_type': 'str',
        'service_area': 'str',
        'user_domain_id': 'str',
        'domain_status': 'str',
        'cname': 'str',
        'sources': 'list[Sources]',
        'domain_origin_host': 'DomainOriginHost',
        'https_status': 'int',
        'create_time': 'int',
        'modify_time': 'int',
        'disabled': 'int',
        'locked': 'int'
    }

    attribute_map = {
        'id': 'id',
        'domain_name': 'domain_name',
        'business_type': 'business_type',
        'service_area': 'service_area',
        'user_domain_id': 'user_domain_id',
        'domain_status': 'domain_status',
        'cname': 'cname',
        'sources': 'sources',
        'domain_origin_host': 'domain_origin_host',
        'https_status': 'https_status',
        'create_time': 'create_time',
        'modify_time': 'modify_time',
        'disabled': 'disabled',
        'locked': 'locked'
    }

    def __init__(self, id=None, domain_name=None, business_type=None, service_area=None, user_domain_id=None, domain_status=None, cname=None, sources=None, domain_origin_host=None, https_status=None, create_time=None, modify_time=None, disabled=None, locked=None):
        """CreateDomainResponseBodyContent - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._domain_name = None
        self._business_type = None
        self._service_area = None
        self._user_domain_id = None
        self._domain_status = None
        self._cname = None
        self._sources = None
        self._domain_origin_host = None
        self._https_status = None
        self._create_time = None
        self._modify_time = None
        self._disabled = None
        self._locked = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if domain_name is not None:
            self.domain_name = domain_name
        if business_type is not None:
            self.business_type = business_type
        if service_area is not None:
            self.service_area = service_area
        if user_domain_id is not None:
            self.user_domain_id = user_domain_id
        if domain_status is not None:
            self.domain_status = domain_status
        if cname is not None:
            self.cname = cname
        if sources is not None:
            self.sources = sources
        if domain_origin_host is not None:
            self.domain_origin_host = domain_origin_host
        if https_status is not None:
            self.https_status = https_status
        if create_time is not None:
            self.create_time = create_time
        if modify_time is not None:
            self.modify_time = modify_time
        if disabled is not None:
            self.disabled = disabled
        if locked is not None:
            self.locked = locked

    @property
    def id(self):
        """Gets the id of this CreateDomainResponseBodyContent.

        加速域名ID。

        :return: The id of this CreateDomainResponseBodyContent.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateDomainResponseBodyContent.

        加速域名ID。

        :param id: The id of this CreateDomainResponseBodyContent.
        :type: str
        """
        self._id = id

    @property
    def domain_name(self):
        """Gets the domain_name of this CreateDomainResponseBodyContent.

        加速域名。

        :return: The domain_name of this CreateDomainResponseBodyContent.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this CreateDomainResponseBodyContent.

        加速域名。

        :param domain_name: The domain_name of this CreateDomainResponseBodyContent.
        :type: str
        """
        self._domain_name = domain_name

    @property
    def business_type(self):
        """Gets the business_type of this CreateDomainResponseBodyContent.

        域名业务类型:-web:静态加速；-download:下载加速；-video:流媒体加速；-wholeSite:全站加速。

        :return: The business_type of this CreateDomainResponseBodyContent.
        :rtype: str
        """
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        """Sets the business_type of this CreateDomainResponseBodyContent.

        域名业务类型:-web:静态加速；-download:下载加速；-video:流媒体加速；-wholeSite:全站加速。

        :param business_type: The business_type of this CreateDomainResponseBodyContent.
        :type: str
        """
        self._business_type = business_type

    @property
    def service_area(self):
        """Gets the service_area of this CreateDomainResponseBodyContent.

        域名服务范围，若为mainland_china，则表示服务范围为中国大陆；若为outside_mainland_china，则表示服务范围为中国大陆境外；若为global，则表示服务范围为全球。

        :return: The service_area of this CreateDomainResponseBodyContent.
        :rtype: str
        """
        return self._service_area

    @service_area.setter
    def service_area(self, service_area):
        """Sets the service_area of this CreateDomainResponseBodyContent.

        域名服务范围，若为mainland_china，则表示服务范围为中国大陆；若为outside_mainland_china，则表示服务范围为中国大陆境外；若为global，则表示服务范围为全球。

        :param service_area: The service_area of this CreateDomainResponseBodyContent.
        :type: str
        """
        self._service_area = service_area

    @property
    def user_domain_id(self):
        """Gets the user_domain_id of this CreateDomainResponseBodyContent.

        域名所属用户的domain_id。

        :return: The user_domain_id of this CreateDomainResponseBodyContent.
        :rtype: str
        """
        return self._user_domain_id

    @user_domain_id.setter
    def user_domain_id(self, user_domain_id):
        """Sets the user_domain_id of this CreateDomainResponseBodyContent.

        域名所属用户的domain_id。

        :param user_domain_id: The user_domain_id of this CreateDomainResponseBodyContent.
        :type: str
        """
        self._user_domain_id = user_domain_id

    @property
    def domain_status(self):
        """Gets the domain_status of this CreateDomainResponseBodyContent.

        加速域名状态。取值意义：online表示“已开启”、offline表示“已停用”、configuring表示“配置中”、configure_failed表示“配置失败”、checking表示“审核中”、check_failed表示“审核失败”、deleting表示“删除中”。

        :return: The domain_status of this CreateDomainResponseBodyContent.
        :rtype: str
        """
        return self._domain_status

    @domain_status.setter
    def domain_status(self, domain_status):
        """Sets the domain_status of this CreateDomainResponseBodyContent.

        加速域名状态。取值意义：online表示“已开启”、offline表示“已停用”、configuring表示“配置中”、configure_failed表示“配置失败”、checking表示“审核中”、check_failed表示“审核失败”、deleting表示“删除中”。

        :param domain_status: The domain_status of this CreateDomainResponseBodyContent.
        :type: str
        """
        self._domain_status = domain_status

    @property
    def cname(self):
        """Gets the cname of this CreateDomainResponseBodyContent.

        加速域名对应的CNAME。

        :return: The cname of this CreateDomainResponseBodyContent.
        :rtype: str
        """
        return self._cname

    @cname.setter
    def cname(self, cname):
        """Sets the cname of this CreateDomainResponseBodyContent.

        加速域名对应的CNAME。

        :param cname: The cname of this CreateDomainResponseBodyContent.
        :type: str
        """
        self._cname = cname

    @property
    def sources(self):
        """Gets the sources of this CreateDomainResponseBodyContent.

        源站信息

        :return: The sources of this CreateDomainResponseBodyContent.
        :rtype: list[Sources]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this CreateDomainResponseBodyContent.

        源站信息

        :param sources: The sources of this CreateDomainResponseBodyContent.
        :type: list[Sources]
        """
        self._sources = sources

    @property
    def domain_origin_host(self):
        """Gets the domain_origin_host of this CreateDomainResponseBodyContent.


        :return: The domain_origin_host of this CreateDomainResponseBodyContent.
        :rtype: DomainOriginHost
        """
        return self._domain_origin_host

    @domain_origin_host.setter
    def domain_origin_host(self, domain_origin_host):
        """Sets the domain_origin_host of this CreateDomainResponseBodyContent.


        :param domain_origin_host: The domain_origin_host of this CreateDomainResponseBodyContent.
        :type: DomainOriginHost
        """
        self._domain_origin_host = domain_origin_host

    @property
    def https_status(self):
        """Gets the https_status of this CreateDomainResponseBodyContent.

        是否开启HTTPS加速。

        :return: The https_status of this CreateDomainResponseBodyContent.
        :rtype: int
        """
        return self._https_status

    @https_status.setter
    def https_status(self, https_status):
        """Sets the https_status of this CreateDomainResponseBodyContent.

        是否开启HTTPS加速。

        :param https_status: The https_status of this CreateDomainResponseBodyContent.
        :type: int
        """
        self._https_status = https_status

    @property
    def create_time(self):
        """Gets the create_time of this CreateDomainResponseBodyContent.

        域名创建时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。

        :return: The create_time of this CreateDomainResponseBodyContent.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CreateDomainResponseBodyContent.

        域名创建时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。

        :param create_time: The create_time of this CreateDomainResponseBodyContent.
        :type: int
        """
        self._create_time = create_time

    @property
    def modify_time(self):
        """Gets the modify_time of this CreateDomainResponseBodyContent.

        域名修改时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。

        :return: The modify_time of this CreateDomainResponseBodyContent.
        :rtype: int
        """
        return self._modify_time

    @modify_time.setter
    def modify_time(self, modify_time):
        """Sets the modify_time of this CreateDomainResponseBodyContent.

        域名修改时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。

        :param modify_time: The modify_time of this CreateDomainResponseBodyContent.
        :type: int
        """
        self._modify_time = modify_time

    @property
    def disabled(self):
        """Gets the disabled of this CreateDomainResponseBodyContent.

        封禁状态（0代表未禁用；1代表禁用）。

        :return: The disabled of this CreateDomainResponseBodyContent.
        :rtype: int
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this CreateDomainResponseBodyContent.

        封禁状态（0代表未禁用；1代表禁用）。

        :param disabled: The disabled of this CreateDomainResponseBodyContent.
        :type: int
        """
        self._disabled = disabled

    @property
    def locked(self):
        """Gets the locked of this CreateDomainResponseBodyContent.

        锁定状态（0代表未锁定；1代表锁定）。

        :return: The locked of this CreateDomainResponseBodyContent.
        :rtype: int
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this CreateDomainResponseBodyContent.

        锁定状态（0代表未锁定；1代表锁定）。

        :param locked: The locked of this CreateDomainResponseBodyContent.
        :type: int
        """
        self._locked = locked

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
        if not isinstance(other, CreateDomainResponseBodyContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
