# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSignatureResponse(SdkResponse):

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
        'create_time': 'str',
        'update_time': 'str',
        'customer_id': 'str',
        'tenant': 'TenantBasic',
        'signature_name': 'str',
        'signature_id': 'str',
        'signature_type': 'str',
        'app_name': 'str',
        'apply_desc': 'str',
        'channel_num': 'str',
        'review_desc': 'str',
        'file_id': 'str',
        'status': 'str',
        'site': 'str',
        'signature_source': 'int',
        'is_involved_third': 'str',
        'power_attorney_file_id': 'str',
        'urge_status': 'str',
        'urge_time': 'str',
        'urge_desc': 'str',
        'app_key': 'str',
        'source_title_content': 'str',
        'signature_usage': 'str',
        'qualification_id': 'str',
        'qualification_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'customer_id': 'customer_id',
        'tenant': 'tenant',
        'signature_name': 'signature_name',
        'signature_id': 'signature_id',
        'signature_type': 'signature_type',
        'app_name': 'app_name',
        'apply_desc': 'apply_desc',
        'channel_num': 'channel_num',
        'review_desc': 'review_desc',
        'file_id': 'file_id',
        'status': 'status',
        'site': 'site',
        'signature_source': 'signature_source',
        'is_involved_third': 'is_involved_third',
        'power_attorney_file_id': 'power_attorney_file_id',
        'urge_status': 'urge_status',
        'urge_time': 'urge_time',
        'urge_desc': 'urge_desc',
        'app_key': 'app_key',
        'source_title_content': 'source_title_content',
        'signature_usage': 'signature_usage',
        'qualification_id': 'qualification_id',
        'qualification_name': 'qualification_name'
    }

    def __init__(self, id=None, create_time=None, update_time=None, customer_id=None, tenant=None, signature_name=None, signature_id=None, signature_type=None, app_name=None, apply_desc=None, channel_num=None, review_desc=None, file_id=None, status=None, site=None, signature_source=None, is_involved_third=None, power_attorney_file_id=None, urge_status=None, urge_time=None, urge_desc=None, app_key=None, source_title_content=None, signature_usage=None, qualification_id=None, qualification_name=None):
        r"""ShowSignatureResponse

        The model defined in huaweicloud sdk

        :param id: 签名主键id，用于获取、修改、删除、申请激活签名的唯一标识
        :type id: str
        :param create_time: 创建时间[yyyy-MM-dd HH:mm:ss]
        :type create_time: str
        :param update_time: 更新时间[yyyy-MM-dd HH:mm:ss]
        :type update_time: str
        :param customer_id: 租户customer id
        :type customer_id: str
        :param tenant: 
        :type tenant: :class:`huaweicloudsdkmsgsms.v2.TenantBasic`
        :param signature_name: 签名名称
        :type signature_name: str
        :param signature_id: 签名id
        :type signature_id: str
        :param signature_type: 签名类型
        :type signature_type: str
        :param app_name: 应用名称
        :type app_name: str
        :param apply_desc: 申请描述
        :type apply_desc: str
        :param channel_num: 国内短信通道号，仅当签名审核成功，运营人员配置完成后返回。
        :type channel_num: str
        :param review_desc: 审核意见
        :type review_desc: str
        :param file_id: 文件id
        :type file_id: str
        :param status: 签名状态
        :type status: str
        :param site: 站点
        :type site: str
        :param signature_source: 签名来源
        :type signature_source: int
        :param is_involved_third: 是否涉及第三方权益
        :type is_involved_third: str
        :param power_attorney_file_id: 授权委托书文件ID
        :type power_attorney_file_id: str
        :param urge_status: 催审状态
        :type urge_status: str
        :param urge_time: 催审时间
        :type urge_time: str
        :param urge_desc: 催审描述
        :type urge_desc: str
        :param app_key: 应用key
        :type app_key: str
        :param source_title_content: 标题内容
        :type source_title_content: str
        :param signature_usage: 签名用途
        :type signature_usage: str
        :param qualification_id: 资质ID
        :type qualification_id: str
        :param qualification_name: 资质名
        :type qualification_name: str
        """
        
        super(ShowSignatureResponse, self).__init__()

        self._id = None
        self._create_time = None
        self._update_time = None
        self._customer_id = None
        self._tenant = None
        self._signature_name = None
        self._signature_id = None
        self._signature_type = None
        self._app_name = None
        self._apply_desc = None
        self._channel_num = None
        self._review_desc = None
        self._file_id = None
        self._status = None
        self._site = None
        self._signature_source = None
        self._is_involved_third = None
        self._power_attorney_file_id = None
        self._urge_status = None
        self._urge_time = None
        self._urge_desc = None
        self._app_key = None
        self._source_title_content = None
        self._signature_usage = None
        self._qualification_id = None
        self._qualification_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if customer_id is not None:
            self.customer_id = customer_id
        if tenant is not None:
            self.tenant = tenant
        if signature_name is not None:
            self.signature_name = signature_name
        if signature_id is not None:
            self.signature_id = signature_id
        if signature_type is not None:
            self.signature_type = signature_type
        if app_name is not None:
            self.app_name = app_name
        if apply_desc is not None:
            self.apply_desc = apply_desc
        if channel_num is not None:
            self.channel_num = channel_num
        if review_desc is not None:
            self.review_desc = review_desc
        if file_id is not None:
            self.file_id = file_id
        if status is not None:
            self.status = status
        if site is not None:
            self.site = site
        if signature_source is not None:
            self.signature_source = signature_source
        if is_involved_third is not None:
            self.is_involved_third = is_involved_third
        if power_attorney_file_id is not None:
            self.power_attorney_file_id = power_attorney_file_id
        if urge_status is not None:
            self.urge_status = urge_status
        if urge_time is not None:
            self.urge_time = urge_time
        if urge_desc is not None:
            self.urge_desc = urge_desc
        if app_key is not None:
            self.app_key = app_key
        if source_title_content is not None:
            self.source_title_content = source_title_content
        if signature_usage is not None:
            self.signature_usage = signature_usage
        if qualification_id is not None:
            self.qualification_id = qualification_id
        if qualification_name is not None:
            self.qualification_name = qualification_name

    @property
    def id(self):
        r"""Gets the id of this ShowSignatureResponse.

        签名主键id，用于获取、修改、删除、申请激活签名的唯一标识

        :return: The id of this ShowSignatureResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowSignatureResponse.

        签名主键id，用于获取、修改、删除、申请激活签名的唯一标识

        :param id: The id of this ShowSignatureResponse.
        :type id: str
        """
        self._id = id

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowSignatureResponse.

        创建时间[yyyy-MM-dd HH:mm:ss]

        :return: The create_time of this ShowSignatureResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowSignatureResponse.

        创建时间[yyyy-MM-dd HH:mm:ss]

        :param create_time: The create_time of this ShowSignatureResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowSignatureResponse.

        更新时间[yyyy-MM-dd HH:mm:ss]

        :return: The update_time of this ShowSignatureResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowSignatureResponse.

        更新时间[yyyy-MM-dd HH:mm:ss]

        :param update_time: The update_time of this ShowSignatureResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def customer_id(self):
        r"""Gets the customer_id of this ShowSignatureResponse.

        租户customer id

        :return: The customer_id of this ShowSignatureResponse.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        r"""Sets the customer_id of this ShowSignatureResponse.

        租户customer id

        :param customer_id: The customer_id of this ShowSignatureResponse.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def tenant(self):
        r"""Gets the tenant of this ShowSignatureResponse.

        :return: The tenant of this ShowSignatureResponse.
        :rtype: :class:`huaweicloudsdkmsgsms.v2.TenantBasic`
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        r"""Sets the tenant of this ShowSignatureResponse.

        :param tenant: The tenant of this ShowSignatureResponse.
        :type tenant: :class:`huaweicloudsdkmsgsms.v2.TenantBasic`
        """
        self._tenant = tenant

    @property
    def signature_name(self):
        r"""Gets the signature_name of this ShowSignatureResponse.

        签名名称

        :return: The signature_name of this ShowSignatureResponse.
        :rtype: str
        """
        return self._signature_name

    @signature_name.setter
    def signature_name(self, signature_name):
        r"""Sets the signature_name of this ShowSignatureResponse.

        签名名称

        :param signature_name: The signature_name of this ShowSignatureResponse.
        :type signature_name: str
        """
        self._signature_name = signature_name

    @property
    def signature_id(self):
        r"""Gets the signature_id of this ShowSignatureResponse.

        签名id

        :return: The signature_id of this ShowSignatureResponse.
        :rtype: str
        """
        return self._signature_id

    @signature_id.setter
    def signature_id(self, signature_id):
        r"""Sets the signature_id of this ShowSignatureResponse.

        签名id

        :param signature_id: The signature_id of this ShowSignatureResponse.
        :type signature_id: str
        """
        self._signature_id = signature_id

    @property
    def signature_type(self):
        r"""Gets the signature_type of this ShowSignatureResponse.

        签名类型

        :return: The signature_type of this ShowSignatureResponse.
        :rtype: str
        """
        return self._signature_type

    @signature_type.setter
    def signature_type(self, signature_type):
        r"""Sets the signature_type of this ShowSignatureResponse.

        签名类型

        :param signature_type: The signature_type of this ShowSignatureResponse.
        :type signature_type: str
        """
        self._signature_type = signature_type

    @property
    def app_name(self):
        r"""Gets the app_name of this ShowSignatureResponse.

        应用名称

        :return: The app_name of this ShowSignatureResponse.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ShowSignatureResponse.

        应用名称

        :param app_name: The app_name of this ShowSignatureResponse.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def apply_desc(self):
        r"""Gets the apply_desc of this ShowSignatureResponse.

        申请描述

        :return: The apply_desc of this ShowSignatureResponse.
        :rtype: str
        """
        return self._apply_desc

    @apply_desc.setter
    def apply_desc(self, apply_desc):
        r"""Sets the apply_desc of this ShowSignatureResponse.

        申请描述

        :param apply_desc: The apply_desc of this ShowSignatureResponse.
        :type apply_desc: str
        """
        self._apply_desc = apply_desc

    @property
    def channel_num(self):
        r"""Gets the channel_num of this ShowSignatureResponse.

        国内短信通道号，仅当签名审核成功，运营人员配置完成后返回。

        :return: The channel_num of this ShowSignatureResponse.
        :rtype: str
        """
        return self._channel_num

    @channel_num.setter
    def channel_num(self, channel_num):
        r"""Sets the channel_num of this ShowSignatureResponse.

        国内短信通道号，仅当签名审核成功，运营人员配置完成后返回。

        :param channel_num: The channel_num of this ShowSignatureResponse.
        :type channel_num: str
        """
        self._channel_num = channel_num

    @property
    def review_desc(self):
        r"""Gets the review_desc of this ShowSignatureResponse.

        审核意见

        :return: The review_desc of this ShowSignatureResponse.
        :rtype: str
        """
        return self._review_desc

    @review_desc.setter
    def review_desc(self, review_desc):
        r"""Sets the review_desc of this ShowSignatureResponse.

        审核意见

        :param review_desc: The review_desc of this ShowSignatureResponse.
        :type review_desc: str
        """
        self._review_desc = review_desc

    @property
    def file_id(self):
        r"""Gets the file_id of this ShowSignatureResponse.

        文件id

        :return: The file_id of this ShowSignatureResponse.
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        r"""Sets the file_id of this ShowSignatureResponse.

        文件id

        :param file_id: The file_id of this ShowSignatureResponse.
        :type file_id: str
        """
        self._file_id = file_id

    @property
    def status(self):
        r"""Gets the status of this ShowSignatureResponse.

        签名状态

        :return: The status of this ShowSignatureResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowSignatureResponse.

        签名状态

        :param status: The status of this ShowSignatureResponse.
        :type status: str
        """
        self._status = status

    @property
    def site(self):
        r"""Gets the site of this ShowSignatureResponse.

        站点

        :return: The site of this ShowSignatureResponse.
        :rtype: str
        """
        return self._site

    @site.setter
    def site(self, site):
        r"""Sets the site of this ShowSignatureResponse.

        站点

        :param site: The site of this ShowSignatureResponse.
        :type site: str
        """
        self._site = site

    @property
    def signature_source(self):
        r"""Gets the signature_source of this ShowSignatureResponse.

        签名来源

        :return: The signature_source of this ShowSignatureResponse.
        :rtype: int
        """
        return self._signature_source

    @signature_source.setter
    def signature_source(self, signature_source):
        r"""Sets the signature_source of this ShowSignatureResponse.

        签名来源

        :param signature_source: The signature_source of this ShowSignatureResponse.
        :type signature_source: int
        """
        self._signature_source = signature_source

    @property
    def is_involved_third(self):
        r"""Gets the is_involved_third of this ShowSignatureResponse.

        是否涉及第三方权益

        :return: The is_involved_third of this ShowSignatureResponse.
        :rtype: str
        """
        return self._is_involved_third

    @is_involved_third.setter
    def is_involved_third(self, is_involved_third):
        r"""Sets the is_involved_third of this ShowSignatureResponse.

        是否涉及第三方权益

        :param is_involved_third: The is_involved_third of this ShowSignatureResponse.
        :type is_involved_third: str
        """
        self._is_involved_third = is_involved_third

    @property
    def power_attorney_file_id(self):
        r"""Gets the power_attorney_file_id of this ShowSignatureResponse.

        授权委托书文件ID

        :return: The power_attorney_file_id of this ShowSignatureResponse.
        :rtype: str
        """
        return self._power_attorney_file_id

    @power_attorney_file_id.setter
    def power_attorney_file_id(self, power_attorney_file_id):
        r"""Sets the power_attorney_file_id of this ShowSignatureResponse.

        授权委托书文件ID

        :param power_attorney_file_id: The power_attorney_file_id of this ShowSignatureResponse.
        :type power_attorney_file_id: str
        """
        self._power_attorney_file_id = power_attorney_file_id

    @property
    def urge_status(self):
        r"""Gets the urge_status of this ShowSignatureResponse.

        催审状态

        :return: The urge_status of this ShowSignatureResponse.
        :rtype: str
        """
        return self._urge_status

    @urge_status.setter
    def urge_status(self, urge_status):
        r"""Sets the urge_status of this ShowSignatureResponse.

        催审状态

        :param urge_status: The urge_status of this ShowSignatureResponse.
        :type urge_status: str
        """
        self._urge_status = urge_status

    @property
    def urge_time(self):
        r"""Gets the urge_time of this ShowSignatureResponse.

        催审时间

        :return: The urge_time of this ShowSignatureResponse.
        :rtype: str
        """
        return self._urge_time

    @urge_time.setter
    def urge_time(self, urge_time):
        r"""Sets the urge_time of this ShowSignatureResponse.

        催审时间

        :param urge_time: The urge_time of this ShowSignatureResponse.
        :type urge_time: str
        """
        self._urge_time = urge_time

    @property
    def urge_desc(self):
        r"""Gets the urge_desc of this ShowSignatureResponse.

        催审描述

        :return: The urge_desc of this ShowSignatureResponse.
        :rtype: str
        """
        return self._urge_desc

    @urge_desc.setter
    def urge_desc(self, urge_desc):
        r"""Sets the urge_desc of this ShowSignatureResponse.

        催审描述

        :param urge_desc: The urge_desc of this ShowSignatureResponse.
        :type urge_desc: str
        """
        self._urge_desc = urge_desc

    @property
    def app_key(self):
        r"""Gets the app_key of this ShowSignatureResponse.

        应用key

        :return: The app_key of this ShowSignatureResponse.
        :rtype: str
        """
        return self._app_key

    @app_key.setter
    def app_key(self, app_key):
        r"""Sets the app_key of this ShowSignatureResponse.

        应用key

        :param app_key: The app_key of this ShowSignatureResponse.
        :type app_key: str
        """
        self._app_key = app_key

    @property
    def source_title_content(self):
        r"""Gets the source_title_content of this ShowSignatureResponse.

        标题内容

        :return: The source_title_content of this ShowSignatureResponse.
        :rtype: str
        """
        return self._source_title_content

    @source_title_content.setter
    def source_title_content(self, source_title_content):
        r"""Sets the source_title_content of this ShowSignatureResponse.

        标题内容

        :param source_title_content: The source_title_content of this ShowSignatureResponse.
        :type source_title_content: str
        """
        self._source_title_content = source_title_content

    @property
    def signature_usage(self):
        r"""Gets the signature_usage of this ShowSignatureResponse.

        签名用途

        :return: The signature_usage of this ShowSignatureResponse.
        :rtype: str
        """
        return self._signature_usage

    @signature_usage.setter
    def signature_usage(self, signature_usage):
        r"""Sets the signature_usage of this ShowSignatureResponse.

        签名用途

        :param signature_usage: The signature_usage of this ShowSignatureResponse.
        :type signature_usage: str
        """
        self._signature_usage = signature_usage

    @property
    def qualification_id(self):
        r"""Gets the qualification_id of this ShowSignatureResponse.

        资质ID

        :return: The qualification_id of this ShowSignatureResponse.
        :rtype: str
        """
        return self._qualification_id

    @qualification_id.setter
    def qualification_id(self, qualification_id):
        r"""Sets the qualification_id of this ShowSignatureResponse.

        资质ID

        :param qualification_id: The qualification_id of this ShowSignatureResponse.
        :type qualification_id: str
        """
        self._qualification_id = qualification_id

    @property
    def qualification_name(self):
        r"""Gets the qualification_name of this ShowSignatureResponse.

        资质名

        :return: The qualification_name of this ShowSignatureResponse.
        :rtype: str
        """
        return self._qualification_name

    @qualification_name.setter
    def qualification_name(self, qualification_name):
        r"""Sets the qualification_name of this ShowSignatureResponse.

        资质名

        :param qualification_name: The qualification_name of this ShowSignatureResponse.
        :type qualification_name: str
        """
        self._qualification_name = qualification_name

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
        if not isinstance(other, ShowSignatureResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
