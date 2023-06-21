# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PubDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pub_id': 'str',
        'oper_time': 'str',
        'state': 'int',
        'online_time': 'str',
        'company_name': 'str',
        'pub_name': 'str',
        'logo_img': 'str',
        'logo_url': 'str',
        'authorization_files': 'dict(str, str)',
        'auto_get_port': 'int',
        'industry': 'int',
        'pub_abstract': 'str',
        'signs_for_auto_get_port': 'list[str]',
        'company_id': 'str',
        'pub_remark': 'str'
    }

    attribute_map = {
        'pub_id': 'pub_id',
        'oper_time': 'oper_time',
        'state': 'state',
        'online_time': 'online_time',
        'company_name': 'company_name',
        'pub_name': 'pub_name',
        'logo_img': 'logo_img',
        'logo_url': 'logo_url',
        'authorization_files': 'authorization_files',
        'auto_get_port': 'auto_get_port',
        'industry': 'industry',
        'pub_abstract': 'pub_abstract',
        'signs_for_auto_get_port': 'signs_for_auto_get_port',
        'company_id': 'company_id',
        'pub_remark': 'pub_remark'
    }

    def __init__(self, pub_id=None, oper_time=None, state=None, online_time=None, company_name=None, pub_name=None, logo_img=None, logo_url=None, authorization_files=None, auto_get_port=None, industry=None, pub_abstract=None, signs_for_auto_get_port=None, company_id=None, pub_remark=None):
        """PubDetail

        The model defined in huaweicloud sdk

        :param pub_id: 服务号ID。
        :type pub_id: str
        :param oper_time: 最新操作时间，格式：yyyy-MM-ddTHH:mm:ssZ。
        :type oper_time: str
        :param state: 服务号状态。  - 1：未生效 - 2：已生效 - 3：已失效 - 4：已冻结  
        :type state: int
        :param online_time: 上线时间，格式为：yyyy-MM-ddTHH:mm:ssZ。
        :type online_time: str
        :param company_name: 企业名称。
        :type company_name: str
        :param pub_name: 服务号名称。
        :type pub_name: str
        :param logo_img: 服务号LOGO图片资源ID。
        :type logo_img: str
        :param logo_url: 服务号LOGO图片URL。
        :type logo_url: str
        :param authorization_files: 授权证明图片的OBSURL地址。
        :type authorization_files: dict(str, str)
        :param auto_get_port: 是否授权系统自动收集端口。   - 0：否  - 1：是  
        :type auto_get_port: int
        :param industry: 从事行业，默认取服务号所属商家的行业分类。  - 1：金融理财  - 2：社交通讯  - 3：影音娱乐  - 4：旅游出行  - 5：购物  - 6：本地生活  - 7：运动健康  - 8：教育培训  - 9：新闻阅读  - 10：运营商  - 11：其他  
        :type industry: int
        :param pub_abstract: 服务号简介。
        :type pub_abstract: str
        :param signs_for_auto_get_port: 自动收集端口使用的签名列表。  &gt; auto_get_port为1时，该字段为必填，每个签名长度为2-18个字符，每个服务号签名不可以重复。 
        :type signs_for_auto_get_port: list[str]
        :param company_id: 企业ID。
        :type company_id: str
        :param pub_remark: 服务号备注。
        :type pub_remark: str
        """
        
        

        self._pub_id = None
        self._oper_time = None
        self._state = None
        self._online_time = None
        self._company_name = None
        self._pub_name = None
        self._logo_img = None
        self._logo_url = None
        self._authorization_files = None
        self._auto_get_port = None
        self._industry = None
        self._pub_abstract = None
        self._signs_for_auto_get_port = None
        self._company_id = None
        self._pub_remark = None
        self.discriminator = None

        if pub_id is not None:
            self.pub_id = pub_id
        if oper_time is not None:
            self.oper_time = oper_time
        if state is not None:
            self.state = state
        if online_time is not None:
            self.online_time = online_time
        if company_name is not None:
            self.company_name = company_name
        if pub_name is not None:
            self.pub_name = pub_name
        if logo_img is not None:
            self.logo_img = logo_img
        if logo_url is not None:
            self.logo_url = logo_url
        if authorization_files is not None:
            self.authorization_files = authorization_files
        if auto_get_port is not None:
            self.auto_get_port = auto_get_port
        if industry is not None:
            self.industry = industry
        if pub_abstract is not None:
            self.pub_abstract = pub_abstract
        if signs_for_auto_get_port is not None:
            self.signs_for_auto_get_port = signs_for_auto_get_port
        if company_id is not None:
            self.company_id = company_id
        if pub_remark is not None:
            self.pub_remark = pub_remark

    @property
    def pub_id(self):
        """Gets the pub_id of this PubDetail.

        服务号ID。

        :return: The pub_id of this PubDetail.
        :rtype: str
        """
        return self._pub_id

    @pub_id.setter
    def pub_id(self, pub_id):
        """Sets the pub_id of this PubDetail.

        服务号ID。

        :param pub_id: The pub_id of this PubDetail.
        :type pub_id: str
        """
        self._pub_id = pub_id

    @property
    def oper_time(self):
        """Gets the oper_time of this PubDetail.

        最新操作时间，格式：yyyy-MM-ddTHH:mm:ssZ。

        :return: The oper_time of this PubDetail.
        :rtype: str
        """
        return self._oper_time

    @oper_time.setter
    def oper_time(self, oper_time):
        """Sets the oper_time of this PubDetail.

        最新操作时间，格式：yyyy-MM-ddTHH:mm:ssZ。

        :param oper_time: The oper_time of this PubDetail.
        :type oper_time: str
        """
        self._oper_time = oper_time

    @property
    def state(self):
        """Gets the state of this PubDetail.

        服务号状态。  - 1：未生效 - 2：已生效 - 3：已失效 - 4：已冻结  

        :return: The state of this PubDetail.
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PubDetail.

        服务号状态。  - 1：未生效 - 2：已生效 - 3：已失效 - 4：已冻结  

        :param state: The state of this PubDetail.
        :type state: int
        """
        self._state = state

    @property
    def online_time(self):
        """Gets the online_time of this PubDetail.

        上线时间，格式为：yyyy-MM-ddTHH:mm:ssZ。

        :return: The online_time of this PubDetail.
        :rtype: str
        """
        return self._online_time

    @online_time.setter
    def online_time(self, online_time):
        """Sets the online_time of this PubDetail.

        上线时间，格式为：yyyy-MM-ddTHH:mm:ssZ。

        :param online_time: The online_time of this PubDetail.
        :type online_time: str
        """
        self._online_time = online_time

    @property
    def company_name(self):
        """Gets the company_name of this PubDetail.

        企业名称。

        :return: The company_name of this PubDetail.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this PubDetail.

        企业名称。

        :param company_name: The company_name of this PubDetail.
        :type company_name: str
        """
        self._company_name = company_name

    @property
    def pub_name(self):
        """Gets the pub_name of this PubDetail.

        服务号名称。

        :return: The pub_name of this PubDetail.
        :rtype: str
        """
        return self._pub_name

    @pub_name.setter
    def pub_name(self, pub_name):
        """Sets the pub_name of this PubDetail.

        服务号名称。

        :param pub_name: The pub_name of this PubDetail.
        :type pub_name: str
        """
        self._pub_name = pub_name

    @property
    def logo_img(self):
        """Gets the logo_img of this PubDetail.

        服务号LOGO图片资源ID。

        :return: The logo_img of this PubDetail.
        :rtype: str
        """
        return self._logo_img

    @logo_img.setter
    def logo_img(self, logo_img):
        """Sets the logo_img of this PubDetail.

        服务号LOGO图片资源ID。

        :param logo_img: The logo_img of this PubDetail.
        :type logo_img: str
        """
        self._logo_img = logo_img

    @property
    def logo_url(self):
        """Gets the logo_url of this PubDetail.

        服务号LOGO图片URL。

        :return: The logo_url of this PubDetail.
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        """Sets the logo_url of this PubDetail.

        服务号LOGO图片URL。

        :param logo_url: The logo_url of this PubDetail.
        :type logo_url: str
        """
        self._logo_url = logo_url

    @property
    def authorization_files(self):
        """Gets the authorization_files of this PubDetail.

        授权证明图片的OBSURL地址。

        :return: The authorization_files of this PubDetail.
        :rtype: dict(str, str)
        """
        return self._authorization_files

    @authorization_files.setter
    def authorization_files(self, authorization_files):
        """Sets the authorization_files of this PubDetail.

        授权证明图片的OBSURL地址。

        :param authorization_files: The authorization_files of this PubDetail.
        :type authorization_files: dict(str, str)
        """
        self._authorization_files = authorization_files

    @property
    def auto_get_port(self):
        """Gets the auto_get_port of this PubDetail.

        是否授权系统自动收集端口。   - 0：否  - 1：是  

        :return: The auto_get_port of this PubDetail.
        :rtype: int
        """
        return self._auto_get_port

    @auto_get_port.setter
    def auto_get_port(self, auto_get_port):
        """Sets the auto_get_port of this PubDetail.

        是否授权系统自动收集端口。   - 0：否  - 1：是  

        :param auto_get_port: The auto_get_port of this PubDetail.
        :type auto_get_port: int
        """
        self._auto_get_port = auto_get_port

    @property
    def industry(self):
        """Gets the industry of this PubDetail.

        从事行业，默认取服务号所属商家的行业分类。  - 1：金融理财  - 2：社交通讯  - 3：影音娱乐  - 4：旅游出行  - 5：购物  - 6：本地生活  - 7：运动健康  - 8：教育培训  - 9：新闻阅读  - 10：运营商  - 11：其他  

        :return: The industry of this PubDetail.
        :rtype: int
        """
        return self._industry

    @industry.setter
    def industry(self, industry):
        """Sets the industry of this PubDetail.

        从事行业，默认取服务号所属商家的行业分类。  - 1：金融理财  - 2：社交通讯  - 3：影音娱乐  - 4：旅游出行  - 5：购物  - 6：本地生活  - 7：运动健康  - 8：教育培训  - 9：新闻阅读  - 10：运营商  - 11：其他  

        :param industry: The industry of this PubDetail.
        :type industry: int
        """
        self._industry = industry

    @property
    def pub_abstract(self):
        """Gets the pub_abstract of this PubDetail.

        服务号简介。

        :return: The pub_abstract of this PubDetail.
        :rtype: str
        """
        return self._pub_abstract

    @pub_abstract.setter
    def pub_abstract(self, pub_abstract):
        """Sets the pub_abstract of this PubDetail.

        服务号简介。

        :param pub_abstract: The pub_abstract of this PubDetail.
        :type pub_abstract: str
        """
        self._pub_abstract = pub_abstract

    @property
    def signs_for_auto_get_port(self):
        """Gets the signs_for_auto_get_port of this PubDetail.

        自动收集端口使用的签名列表。  > auto_get_port为1时，该字段为必填，每个签名长度为2-18个字符，每个服务号签名不可以重复。 

        :return: The signs_for_auto_get_port of this PubDetail.
        :rtype: list[str]
        """
        return self._signs_for_auto_get_port

    @signs_for_auto_get_port.setter
    def signs_for_auto_get_port(self, signs_for_auto_get_port):
        """Sets the signs_for_auto_get_port of this PubDetail.

        自动收集端口使用的签名列表。  > auto_get_port为1时，该字段为必填，每个签名长度为2-18个字符，每个服务号签名不可以重复。 

        :param signs_for_auto_get_port: The signs_for_auto_get_port of this PubDetail.
        :type signs_for_auto_get_port: list[str]
        """
        self._signs_for_auto_get_port = signs_for_auto_get_port

    @property
    def company_id(self):
        """Gets the company_id of this PubDetail.

        企业ID。

        :return: The company_id of this PubDetail.
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this PubDetail.

        企业ID。

        :param company_id: The company_id of this PubDetail.
        :type company_id: str
        """
        self._company_id = company_id

    @property
    def pub_remark(self):
        """Gets the pub_remark of this PubDetail.

        服务号备注。

        :return: The pub_remark of this PubDetail.
        :rtype: str
        """
        return self._pub_remark

    @pub_remark.setter
    def pub_remark(self, pub_remark):
        """Sets the pub_remark of this PubDetail.

        服务号备注。

        :param pub_remark: The pub_remark of this PubDetail.
        :type pub_remark: str
        """
        self._pub_remark = pub_remark

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
        if not isinstance(other, PubDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
