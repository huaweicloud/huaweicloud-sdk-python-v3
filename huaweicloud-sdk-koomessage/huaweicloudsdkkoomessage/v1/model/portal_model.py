# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PortalModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'portal_id': 'str',
        'company_id': 'str',
        'company_name': 'str',
        'pub_id': 'str',
        'pub_name': 'str',
        'background_img': 'str',
        'background_img_url': 'str',
        'summary': 'str',
        'tels': 'str',
        'fastapps': 'str',
        'state': 'int',
        'approve_state': 'int',
        'online_time': 'datetime',
        'creator': 'str',
        'create_time': 'datetime',
        'change_reason': 'str'
    }

    attribute_map = {
        'portal_id': 'portal_id',
        'company_id': 'company_id',
        'company_name': 'company_name',
        'pub_id': 'pub_id',
        'pub_name': 'pub_name',
        'background_img': 'background_img',
        'background_img_url': 'background_img_url',
        'summary': 'summary',
        'tels': 'tels',
        'fastapps': 'fastapps',
        'state': 'state',
        'approve_state': 'approve_state',
        'online_time': 'online_time',
        'creator': 'creator',
        'create_time': 'create_time',
        'change_reason': 'change_reason'
    }

    def __init__(self, portal_id=None, company_id=None, company_name=None, pub_id=None, pub_name=None, background_img=None, background_img_url=None, summary=None, tels=None, fastapps=None, state=None, approve_state=None, online_time=None, creator=None, create_time=None, change_reason=None):
        """PortalModel

        The model defined in huaweicloud sdk

        :param portal_id: 主页ID。
        :type portal_id: str
        :param company_id: 企业ID。
        :type company_id: str
        :param company_name: 企业名称。
        :type company_name: str
        :param pub_id: 服务号ID。
        :type pub_id: str
        :param pub_name: 服务号名称。
        :type pub_name: str
        :param background_img: 主页背景图片资源ID。
        :type background_img: str
        :param background_img_url: 背景图片URL。
        :type background_img_url: str
        :param summary: 简介。
        :type summary: str
        :param tels: 热线号列表。  &gt; 以JSON列表返回，格式： &gt; {\&quot;tel\&quot;: \&quot;400-800-8800\&quot;, \&quot;usage\&quot;: \&quot;官方服务电话\&quot;}。 
        :type tels: str
        :param fastapps: 快应用列表。  &gt; 以JSON列表返回，格式： &gt; {\&quot;name\&quot;: \&quot;快应用名称\&quot;,\&quot;logo_img\&quot;: \&quot;快应用LOGO图片资源ID\&quot;, \&quot;logo_img_url\&quot;: \&quot;快应用LOGO图片资源URL\&quot;, \&quot;description\&quot;: \&quot;快应用描述\&quot;,\&quot;deeplink\&quot;: \&quot;hap://app/fastapp\&quot;,\&quot;depend_engine_version\&quot;: \&quot;1040\&quot;}。 
        :type fastapps: str
        :param state: 资源状态。  - 1：未生效  - 2：已生效  - 3：已失效  - 4：已冻结 
        :type state: int
        :param approve_state: 审核状态。  - 1：待审核  - 2：通过  - 3：驳回 
        :type approve_state: int
        :param online_time: 上线时间。
        :type online_time: datetime
        :param creator: 创建人。
        :type creator: str
        :param create_time: 创建时间。
        :type create_time: datetime
        :param change_reason: 修改原因。
        :type change_reason: str
        """
        
        

        self._portal_id = None
        self._company_id = None
        self._company_name = None
        self._pub_id = None
        self._pub_name = None
        self._background_img = None
        self._background_img_url = None
        self._summary = None
        self._tels = None
        self._fastapps = None
        self._state = None
        self._approve_state = None
        self._online_time = None
        self._creator = None
        self._create_time = None
        self._change_reason = None
        self.discriminator = None

        self.portal_id = portal_id
        if company_id is not None:
            self.company_id = company_id
        self.company_name = company_name
        self.pub_id = pub_id
        self.pub_name = pub_name
        self.background_img = background_img
        if background_img_url is not None:
            self.background_img_url = background_img_url
        self.summary = summary
        self.tels = tels
        self.fastapps = fastapps
        self.state = state
        self.approve_state = approve_state
        self.online_time = online_time
        self.creator = creator
        self.create_time = create_time
        self.change_reason = change_reason

    @property
    def portal_id(self):
        """Gets the portal_id of this PortalModel.

        主页ID。

        :return: The portal_id of this PortalModel.
        :rtype: str
        """
        return self._portal_id

    @portal_id.setter
    def portal_id(self, portal_id):
        """Sets the portal_id of this PortalModel.

        主页ID。

        :param portal_id: The portal_id of this PortalModel.
        :type portal_id: str
        """
        self._portal_id = portal_id

    @property
    def company_id(self):
        """Gets the company_id of this PortalModel.

        企业ID。

        :return: The company_id of this PortalModel.
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this PortalModel.

        企业ID。

        :param company_id: The company_id of this PortalModel.
        :type company_id: str
        """
        self._company_id = company_id

    @property
    def company_name(self):
        """Gets the company_name of this PortalModel.

        企业名称。

        :return: The company_name of this PortalModel.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this PortalModel.

        企业名称。

        :param company_name: The company_name of this PortalModel.
        :type company_name: str
        """
        self._company_name = company_name

    @property
    def pub_id(self):
        """Gets the pub_id of this PortalModel.

        服务号ID。

        :return: The pub_id of this PortalModel.
        :rtype: str
        """
        return self._pub_id

    @pub_id.setter
    def pub_id(self, pub_id):
        """Sets the pub_id of this PortalModel.

        服务号ID。

        :param pub_id: The pub_id of this PortalModel.
        :type pub_id: str
        """
        self._pub_id = pub_id

    @property
    def pub_name(self):
        """Gets the pub_name of this PortalModel.

        服务号名称。

        :return: The pub_name of this PortalModel.
        :rtype: str
        """
        return self._pub_name

    @pub_name.setter
    def pub_name(self, pub_name):
        """Sets the pub_name of this PortalModel.

        服务号名称。

        :param pub_name: The pub_name of this PortalModel.
        :type pub_name: str
        """
        self._pub_name = pub_name

    @property
    def background_img(self):
        """Gets the background_img of this PortalModel.

        主页背景图片资源ID。

        :return: The background_img of this PortalModel.
        :rtype: str
        """
        return self._background_img

    @background_img.setter
    def background_img(self, background_img):
        """Sets the background_img of this PortalModel.

        主页背景图片资源ID。

        :param background_img: The background_img of this PortalModel.
        :type background_img: str
        """
        self._background_img = background_img

    @property
    def background_img_url(self):
        """Gets the background_img_url of this PortalModel.

        背景图片URL。

        :return: The background_img_url of this PortalModel.
        :rtype: str
        """
        return self._background_img_url

    @background_img_url.setter
    def background_img_url(self, background_img_url):
        """Sets the background_img_url of this PortalModel.

        背景图片URL。

        :param background_img_url: The background_img_url of this PortalModel.
        :type background_img_url: str
        """
        self._background_img_url = background_img_url

    @property
    def summary(self):
        """Gets the summary of this PortalModel.

        简介。

        :return: The summary of this PortalModel.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this PortalModel.

        简介。

        :param summary: The summary of this PortalModel.
        :type summary: str
        """
        self._summary = summary

    @property
    def tels(self):
        """Gets the tels of this PortalModel.

        热线号列表。  > 以JSON列表返回，格式： > {\"tel\": \"400-800-8800\", \"usage\": \"官方服务电话\"}。 

        :return: The tels of this PortalModel.
        :rtype: str
        """
        return self._tels

    @tels.setter
    def tels(self, tels):
        """Sets the tels of this PortalModel.

        热线号列表。  > 以JSON列表返回，格式： > {\"tel\": \"400-800-8800\", \"usage\": \"官方服务电话\"}。 

        :param tels: The tels of this PortalModel.
        :type tels: str
        """
        self._tels = tels

    @property
    def fastapps(self):
        """Gets the fastapps of this PortalModel.

        快应用列表。  > 以JSON列表返回，格式： > {\"name\": \"快应用名称\",\"logo_img\": \"快应用LOGO图片资源ID\", \"logo_img_url\": \"快应用LOGO图片资源URL\", \"description\": \"快应用描述\",\"deeplink\": \"hap://app/fastapp\",\"depend_engine_version\": \"1040\"}。 

        :return: The fastapps of this PortalModel.
        :rtype: str
        """
        return self._fastapps

    @fastapps.setter
    def fastapps(self, fastapps):
        """Sets the fastapps of this PortalModel.

        快应用列表。  > 以JSON列表返回，格式： > {\"name\": \"快应用名称\",\"logo_img\": \"快应用LOGO图片资源ID\", \"logo_img_url\": \"快应用LOGO图片资源URL\", \"description\": \"快应用描述\",\"deeplink\": \"hap://app/fastapp\",\"depend_engine_version\": \"1040\"}。 

        :param fastapps: The fastapps of this PortalModel.
        :type fastapps: str
        """
        self._fastapps = fastapps

    @property
    def state(self):
        """Gets the state of this PortalModel.

        资源状态。  - 1：未生效  - 2：已生效  - 3：已失效  - 4：已冻结 

        :return: The state of this PortalModel.
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PortalModel.

        资源状态。  - 1：未生效  - 2：已生效  - 3：已失效  - 4：已冻结 

        :param state: The state of this PortalModel.
        :type state: int
        """
        self._state = state

    @property
    def approve_state(self):
        """Gets the approve_state of this PortalModel.

        审核状态。  - 1：待审核  - 2：通过  - 3：驳回 

        :return: The approve_state of this PortalModel.
        :rtype: int
        """
        return self._approve_state

    @approve_state.setter
    def approve_state(self, approve_state):
        """Sets the approve_state of this PortalModel.

        审核状态。  - 1：待审核  - 2：通过  - 3：驳回 

        :param approve_state: The approve_state of this PortalModel.
        :type approve_state: int
        """
        self._approve_state = approve_state

    @property
    def online_time(self):
        """Gets the online_time of this PortalModel.

        上线时间。

        :return: The online_time of this PortalModel.
        :rtype: datetime
        """
        return self._online_time

    @online_time.setter
    def online_time(self, online_time):
        """Sets the online_time of this PortalModel.

        上线时间。

        :param online_time: The online_time of this PortalModel.
        :type online_time: datetime
        """
        self._online_time = online_time

    @property
    def creator(self):
        """Gets the creator of this PortalModel.

        创建人。

        :return: The creator of this PortalModel.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this PortalModel.

        创建人。

        :param creator: The creator of this PortalModel.
        :type creator: str
        """
        self._creator = creator

    @property
    def create_time(self):
        """Gets the create_time of this PortalModel.

        创建时间。

        :return: The create_time of this PortalModel.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this PortalModel.

        创建时间。

        :param create_time: The create_time of this PortalModel.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def change_reason(self):
        """Gets the change_reason of this PortalModel.

        修改原因。

        :return: The change_reason of this PortalModel.
        :rtype: str
        """
        return self._change_reason

    @change_reason.setter
    def change_reason(self, change_reason):
        """Sets the change_reason of this PortalModel.

        修改原因。

        :param change_reason: The change_reason of this PortalModel.
        :type change_reason: str
        """
        self._change_reason = change_reason

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
        if not isinstance(other, PortalModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
