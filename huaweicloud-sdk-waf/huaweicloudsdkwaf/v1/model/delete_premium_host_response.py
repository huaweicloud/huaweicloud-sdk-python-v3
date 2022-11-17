# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeletePremiumHostResponse(SdkResponse):

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
        'hostname': 'str',
        'extend': 'dict(str, str)',
        'region': 'str',
        'flag': 'Flag',
        'description': 'str',
        'policyid': 'str',
        'protect_status': 'int',
        'access_status': 'int',
        'web_tag': 'str',
        'host_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'hostname': 'hostname',
        'extend': 'extend',
        'region': 'region',
        'flag': 'flag',
        'description': 'description',
        'policyid': 'policyid',
        'protect_status': 'protect_status',
        'access_status': 'access_status',
        'web_tag': 'web_tag',
        'host_id': 'host_id'
    }

    def __init__(self, id=None, hostname=None, extend=None, region=None, flag=None, description=None, policyid=None, protect_status=None, access_status=None, web_tag=None, host_id=None):
        """DeletePremiumHostResponse

        The model defined in huaweicloud sdk

        :param id: 域名id
        :type id: str
        :param hostname: 域名
        :type hostname: str
        :param extend: 扩展字段，用于保存防护域名的一些配置信息。
        :type extend: dict(str, str)
        :param region: 华为云区域ID，控制台创建的域名会携带此参数，api调用创建的域名此参数为空，可以通过华为云上地区和终端节点文档查询区域ID对应的中文名称
        :type region: str
        :param flag: 
        :type flag: :class:`huaweicloudsdkwaf.v1.Flag`
        :param description: 域名描述
        :type description: str
        :param policyid: 防护域名初始绑定的防护策略ID,可以通过策略名称调用查询防护策略列表（ListPolicy）接口查询到对应的策略id
        :type policyid: str
        :param protect_status: 域名防护状态：  - -1：bypass，该域名的请求直接到达其后端服务器，不再经过WAF  - 0：暂停防护，WAF只转发该域名的请求，不做攻击检测  - 1：开启防护，WAF根据您配置的策略进行攻击检测
        :type protect_status: int
        :param access_status: 域名接入状态，0表示未接入，1表示已接入
        :type access_status: int
        :param web_tag: 网站名称，对应WAF控制台域名详情中的网站名称
        :type web_tag: str
        :param host_id: 域名id，和id的值是一样的，属于冗余字段
        :type host_id: str
        """
        
        super(DeletePremiumHostResponse, self).__init__()

        self._id = None
        self._hostname = None
        self._extend = None
        self._region = None
        self._flag = None
        self._description = None
        self._policyid = None
        self._protect_status = None
        self._access_status = None
        self._web_tag = None
        self._host_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if hostname is not None:
            self.hostname = hostname
        if extend is not None:
            self.extend = extend
        if region is not None:
            self.region = region
        if flag is not None:
            self.flag = flag
        if description is not None:
            self.description = description
        if policyid is not None:
            self.policyid = policyid
        if protect_status is not None:
            self.protect_status = protect_status
        if access_status is not None:
            self.access_status = access_status
        if web_tag is not None:
            self.web_tag = web_tag
        if host_id is not None:
            self.host_id = host_id

    @property
    def id(self):
        """Gets the id of this DeletePremiumHostResponse.

        域名id

        :return: The id of this DeletePremiumHostResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeletePremiumHostResponse.

        域名id

        :param id: The id of this DeletePremiumHostResponse.
        :type id: str
        """
        self._id = id

    @property
    def hostname(self):
        """Gets the hostname of this DeletePremiumHostResponse.

        域名

        :return: The hostname of this DeletePremiumHostResponse.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this DeletePremiumHostResponse.

        域名

        :param hostname: The hostname of this DeletePremiumHostResponse.
        :type hostname: str
        """
        self._hostname = hostname

    @property
    def extend(self):
        """Gets the extend of this DeletePremiumHostResponse.

        扩展字段，用于保存防护域名的一些配置信息。

        :return: The extend of this DeletePremiumHostResponse.
        :rtype: dict(str, str)
        """
        return self._extend

    @extend.setter
    def extend(self, extend):
        """Sets the extend of this DeletePremiumHostResponse.

        扩展字段，用于保存防护域名的一些配置信息。

        :param extend: The extend of this DeletePremiumHostResponse.
        :type extend: dict(str, str)
        """
        self._extend = extend

    @property
    def region(self):
        """Gets the region of this DeletePremiumHostResponse.

        华为云区域ID，控制台创建的域名会携带此参数，api调用创建的域名此参数为空，可以通过华为云上地区和终端节点文档查询区域ID对应的中文名称

        :return: The region of this DeletePremiumHostResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this DeletePremiumHostResponse.

        华为云区域ID，控制台创建的域名会携带此参数，api调用创建的域名此参数为空，可以通过华为云上地区和终端节点文档查询区域ID对应的中文名称

        :param region: The region of this DeletePremiumHostResponse.
        :type region: str
        """
        self._region = region

    @property
    def flag(self):
        """Gets the flag of this DeletePremiumHostResponse.

        :return: The flag of this DeletePremiumHostResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.Flag`
        """
        return self._flag

    @flag.setter
    def flag(self, flag):
        """Sets the flag of this DeletePremiumHostResponse.

        :param flag: The flag of this DeletePremiumHostResponse.
        :type flag: :class:`huaweicloudsdkwaf.v1.Flag`
        """
        self._flag = flag

    @property
    def description(self):
        """Gets the description of this DeletePremiumHostResponse.

        域名描述

        :return: The description of this DeletePremiumHostResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeletePremiumHostResponse.

        域名描述

        :param description: The description of this DeletePremiumHostResponse.
        :type description: str
        """
        self._description = description

    @property
    def policyid(self):
        """Gets the policyid of this DeletePremiumHostResponse.

        防护域名初始绑定的防护策略ID,可以通过策略名称调用查询防护策略列表（ListPolicy）接口查询到对应的策略id

        :return: The policyid of this DeletePremiumHostResponse.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        """Sets the policyid of this DeletePremiumHostResponse.

        防护域名初始绑定的防护策略ID,可以通过策略名称调用查询防护策略列表（ListPolicy）接口查询到对应的策略id

        :param policyid: The policyid of this DeletePremiumHostResponse.
        :type policyid: str
        """
        self._policyid = policyid

    @property
    def protect_status(self):
        """Gets the protect_status of this DeletePremiumHostResponse.

        域名防护状态：  - -1：bypass，该域名的请求直接到达其后端服务器，不再经过WAF  - 0：暂停防护，WAF只转发该域名的请求，不做攻击检测  - 1：开启防护，WAF根据您配置的策略进行攻击检测

        :return: The protect_status of this DeletePremiumHostResponse.
        :rtype: int
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        """Sets the protect_status of this DeletePremiumHostResponse.

        域名防护状态：  - -1：bypass，该域名的请求直接到达其后端服务器，不再经过WAF  - 0：暂停防护，WAF只转发该域名的请求，不做攻击检测  - 1：开启防护，WAF根据您配置的策略进行攻击检测

        :param protect_status: The protect_status of this DeletePremiumHostResponse.
        :type protect_status: int
        """
        self._protect_status = protect_status

    @property
    def access_status(self):
        """Gets the access_status of this DeletePremiumHostResponse.

        域名接入状态，0表示未接入，1表示已接入

        :return: The access_status of this DeletePremiumHostResponse.
        :rtype: int
        """
        return self._access_status

    @access_status.setter
    def access_status(self, access_status):
        """Sets the access_status of this DeletePremiumHostResponse.

        域名接入状态，0表示未接入，1表示已接入

        :param access_status: The access_status of this DeletePremiumHostResponse.
        :type access_status: int
        """
        self._access_status = access_status

    @property
    def web_tag(self):
        """Gets the web_tag of this DeletePremiumHostResponse.

        网站名称，对应WAF控制台域名详情中的网站名称

        :return: The web_tag of this DeletePremiumHostResponse.
        :rtype: str
        """
        return self._web_tag

    @web_tag.setter
    def web_tag(self, web_tag):
        """Sets the web_tag of this DeletePremiumHostResponse.

        网站名称，对应WAF控制台域名详情中的网站名称

        :param web_tag: The web_tag of this DeletePremiumHostResponse.
        :type web_tag: str
        """
        self._web_tag = web_tag

    @property
    def host_id(self):
        """Gets the host_id of this DeletePremiumHostResponse.

        域名id，和id的值是一样的，属于冗余字段

        :return: The host_id of this DeletePremiumHostResponse.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this DeletePremiumHostResponse.

        域名id，和id的值是一样的，属于冗余字段

        :param host_id: The host_id of this DeletePremiumHostResponse.
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
        if not isinstance(other, DeletePremiumHostResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
