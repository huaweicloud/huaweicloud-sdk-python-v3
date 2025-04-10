# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VmsTemplateStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tpl_id': 'str',
        'audit_state': 'int',
        'audit_desc': 'str',
        'tpl_size': 'int',
        'valid_time': 'str',
        'status_detail': 'list[StatusDetail]',
        'preview_url': 'str',
        'tpl_name': 'str',
        'title': 'str',
        'tpl_sign': 'str',
        'create_time': 'str',
        'var_info': 'list[VarInfo]',
        'restags': 'str'
    }

    attribute_map = {
        'tpl_id': 'tpl_id',
        'audit_state': 'audit_state',
        'audit_desc': 'audit_desc',
        'tpl_size': 'tpl_size',
        'valid_time': 'valid_time',
        'status_detail': 'status_detail',
        'preview_url': 'preview_url',
        'tpl_name': 'tpl_name',
        'title': 'title',
        'tpl_sign': 'tpl_sign',
        'create_time': 'create_time',
        'var_info': 'var_info',
        'restags': 'restags'
    }

    def __init__(self, tpl_id=None, audit_state=None, audit_desc=None, tpl_size=None, valid_time=None, status_detail=None, preview_url=None, tpl_name=None, title=None, tpl_sign=None, create_time=None, var_info=None, restags=None):
        r"""VmsTemplateStatus

        The model defined in huaweicloud sdk

        :param tpl_id: 智能信息基础版模板ID。
        :type tpl_id: str
        :param audit_state: 智能信息基础版审核状态。 - 0：正常可用 - 1：审核中 - 2：审核不通过 - 3：模板已禁用 - 4：模板不存在 - 5：模板已过期 
        :type audit_state: int
        :param audit_desc: 智能信息基础版模板状态的描述，若状态是审核不通过或被禁用，描述表示的是不通过或禁用的原因。 &gt; 长度不超过 1024 字。 
        :type audit_desc: str
        :param tpl_size: 智能信息基础版模板的大小。  &gt;  单位：字节。 
        :type tpl_size: int
        :param valid_time: 模板截止有效日期，格式：yyyy-MM-ddTHH:mm:ssZ，0：表示永久有效。样例：2020-01-31T23:59:59Z。
        :type valid_time: str
        :param status_detail: 运营商的模板状态详情。
        :type status_detail: list[:class:`huaweicloudsdkkoomessage.v1.StatusDetail`]
        :param preview_url: 智能信息基础版模板预览地址。
        :type preview_url: str
        :param tpl_name: 智能信息基础版模板名称。
        :type tpl_name: str
        :param title: 智能信息基础版模板主题。
        :type title: str
        :param tpl_sign: 智能信息基础版模板签名。
        :type tpl_sign: str
        :param create_time: 智能信息基础版模板创建时间，格式：yyyy-MM-ddTHH:mm:ssZ。
        :type create_time: str
        :param var_info: 智能信息基础版模板动参信息，静态模板没有动参，该字段填空。
        :type var_info: list[:class:`huaweicloudsdkkoomessage.v1.VarInfo`]
        :param restags: 资源分配标签，取值如下： - 三网一般 - 三网抗诉 - 单网一般 - 单网抗诉 
        :type restags: str
        """
        
        

        self._tpl_id = None
        self._audit_state = None
        self._audit_desc = None
        self._tpl_size = None
        self._valid_time = None
        self._status_detail = None
        self._preview_url = None
        self._tpl_name = None
        self._title = None
        self._tpl_sign = None
        self._create_time = None
        self._var_info = None
        self._restags = None
        self.discriminator = None

        if tpl_id is not None:
            self.tpl_id = tpl_id
        if audit_state is not None:
            self.audit_state = audit_state
        if audit_desc is not None:
            self.audit_desc = audit_desc
        if tpl_size is not None:
            self.tpl_size = tpl_size
        if valid_time is not None:
            self.valid_time = valid_time
        if status_detail is not None:
            self.status_detail = status_detail
        if preview_url is not None:
            self.preview_url = preview_url
        if tpl_name is not None:
            self.tpl_name = tpl_name
        if title is not None:
            self.title = title
        if tpl_sign is not None:
            self.tpl_sign = tpl_sign
        if create_time is not None:
            self.create_time = create_time
        if var_info is not None:
            self.var_info = var_info
        if restags is not None:
            self.restags = restags

    @property
    def tpl_id(self):
        r"""Gets the tpl_id of this VmsTemplateStatus.

        智能信息基础版模板ID。

        :return: The tpl_id of this VmsTemplateStatus.
        :rtype: str
        """
        return self._tpl_id

    @tpl_id.setter
    def tpl_id(self, tpl_id):
        r"""Sets the tpl_id of this VmsTemplateStatus.

        智能信息基础版模板ID。

        :param tpl_id: The tpl_id of this VmsTemplateStatus.
        :type tpl_id: str
        """
        self._tpl_id = tpl_id

    @property
    def audit_state(self):
        r"""Gets the audit_state of this VmsTemplateStatus.

        智能信息基础版审核状态。 - 0：正常可用 - 1：审核中 - 2：审核不通过 - 3：模板已禁用 - 4：模板不存在 - 5：模板已过期 

        :return: The audit_state of this VmsTemplateStatus.
        :rtype: int
        """
        return self._audit_state

    @audit_state.setter
    def audit_state(self, audit_state):
        r"""Sets the audit_state of this VmsTemplateStatus.

        智能信息基础版审核状态。 - 0：正常可用 - 1：审核中 - 2：审核不通过 - 3：模板已禁用 - 4：模板不存在 - 5：模板已过期 

        :param audit_state: The audit_state of this VmsTemplateStatus.
        :type audit_state: int
        """
        self._audit_state = audit_state

    @property
    def audit_desc(self):
        r"""Gets the audit_desc of this VmsTemplateStatus.

        智能信息基础版模板状态的描述，若状态是审核不通过或被禁用，描述表示的是不通过或禁用的原因。 > 长度不超过 1024 字。 

        :return: The audit_desc of this VmsTemplateStatus.
        :rtype: str
        """
        return self._audit_desc

    @audit_desc.setter
    def audit_desc(self, audit_desc):
        r"""Sets the audit_desc of this VmsTemplateStatus.

        智能信息基础版模板状态的描述，若状态是审核不通过或被禁用，描述表示的是不通过或禁用的原因。 > 长度不超过 1024 字。 

        :param audit_desc: The audit_desc of this VmsTemplateStatus.
        :type audit_desc: str
        """
        self._audit_desc = audit_desc

    @property
    def tpl_size(self):
        r"""Gets the tpl_size of this VmsTemplateStatus.

        智能信息基础版模板的大小。  >  单位：字节。 

        :return: The tpl_size of this VmsTemplateStatus.
        :rtype: int
        """
        return self._tpl_size

    @tpl_size.setter
    def tpl_size(self, tpl_size):
        r"""Sets the tpl_size of this VmsTemplateStatus.

        智能信息基础版模板的大小。  >  单位：字节。 

        :param tpl_size: The tpl_size of this VmsTemplateStatus.
        :type tpl_size: int
        """
        self._tpl_size = tpl_size

    @property
    def valid_time(self):
        r"""Gets the valid_time of this VmsTemplateStatus.

        模板截止有效日期，格式：yyyy-MM-ddTHH:mm:ssZ，0：表示永久有效。样例：2020-01-31T23:59:59Z。

        :return: The valid_time of this VmsTemplateStatus.
        :rtype: str
        """
        return self._valid_time

    @valid_time.setter
    def valid_time(self, valid_time):
        r"""Sets the valid_time of this VmsTemplateStatus.

        模板截止有效日期，格式：yyyy-MM-ddTHH:mm:ssZ，0：表示永久有效。样例：2020-01-31T23:59:59Z。

        :param valid_time: The valid_time of this VmsTemplateStatus.
        :type valid_time: str
        """
        self._valid_time = valid_time

    @property
    def status_detail(self):
        r"""Gets the status_detail of this VmsTemplateStatus.

        运营商的模板状态详情。

        :return: The status_detail of this VmsTemplateStatus.
        :rtype: list[:class:`huaweicloudsdkkoomessage.v1.StatusDetail`]
        """
        return self._status_detail

    @status_detail.setter
    def status_detail(self, status_detail):
        r"""Sets the status_detail of this VmsTemplateStatus.

        运营商的模板状态详情。

        :param status_detail: The status_detail of this VmsTemplateStatus.
        :type status_detail: list[:class:`huaweicloudsdkkoomessage.v1.StatusDetail`]
        """
        self._status_detail = status_detail

    @property
    def preview_url(self):
        r"""Gets the preview_url of this VmsTemplateStatus.

        智能信息基础版模板预览地址。

        :return: The preview_url of this VmsTemplateStatus.
        :rtype: str
        """
        return self._preview_url

    @preview_url.setter
    def preview_url(self, preview_url):
        r"""Sets the preview_url of this VmsTemplateStatus.

        智能信息基础版模板预览地址。

        :param preview_url: The preview_url of this VmsTemplateStatus.
        :type preview_url: str
        """
        self._preview_url = preview_url

    @property
    def tpl_name(self):
        r"""Gets the tpl_name of this VmsTemplateStatus.

        智能信息基础版模板名称。

        :return: The tpl_name of this VmsTemplateStatus.
        :rtype: str
        """
        return self._tpl_name

    @tpl_name.setter
    def tpl_name(self, tpl_name):
        r"""Sets the tpl_name of this VmsTemplateStatus.

        智能信息基础版模板名称。

        :param tpl_name: The tpl_name of this VmsTemplateStatus.
        :type tpl_name: str
        """
        self._tpl_name = tpl_name

    @property
    def title(self):
        r"""Gets the title of this VmsTemplateStatus.

        智能信息基础版模板主题。

        :return: The title of this VmsTemplateStatus.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this VmsTemplateStatus.

        智能信息基础版模板主题。

        :param title: The title of this VmsTemplateStatus.
        :type title: str
        """
        self._title = title

    @property
    def tpl_sign(self):
        r"""Gets the tpl_sign of this VmsTemplateStatus.

        智能信息基础版模板签名。

        :return: The tpl_sign of this VmsTemplateStatus.
        :rtype: str
        """
        return self._tpl_sign

    @tpl_sign.setter
    def tpl_sign(self, tpl_sign):
        r"""Sets the tpl_sign of this VmsTemplateStatus.

        智能信息基础版模板签名。

        :param tpl_sign: The tpl_sign of this VmsTemplateStatus.
        :type tpl_sign: str
        """
        self._tpl_sign = tpl_sign

    @property
    def create_time(self):
        r"""Gets the create_time of this VmsTemplateStatus.

        智能信息基础版模板创建时间，格式：yyyy-MM-ddTHH:mm:ssZ。

        :return: The create_time of this VmsTemplateStatus.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this VmsTemplateStatus.

        智能信息基础版模板创建时间，格式：yyyy-MM-ddTHH:mm:ssZ。

        :param create_time: The create_time of this VmsTemplateStatus.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def var_info(self):
        r"""Gets the var_info of this VmsTemplateStatus.

        智能信息基础版模板动参信息，静态模板没有动参，该字段填空。

        :return: The var_info of this VmsTemplateStatus.
        :rtype: list[:class:`huaweicloudsdkkoomessage.v1.VarInfo`]
        """
        return self._var_info

    @var_info.setter
    def var_info(self, var_info):
        r"""Sets the var_info of this VmsTemplateStatus.

        智能信息基础版模板动参信息，静态模板没有动参，该字段填空。

        :param var_info: The var_info of this VmsTemplateStatus.
        :type var_info: list[:class:`huaweicloudsdkkoomessage.v1.VarInfo`]
        """
        self._var_info = var_info

    @property
    def restags(self):
        r"""Gets the restags of this VmsTemplateStatus.

        资源分配标签，取值如下： - 三网一般 - 三网抗诉 - 单网一般 - 单网抗诉 

        :return: The restags of this VmsTemplateStatus.
        :rtype: str
        """
        return self._restags

    @restags.setter
    def restags(self, restags):
        r"""Sets the restags of this VmsTemplateStatus.

        资源分配标签，取值如下： - 三网一般 - 三网抗诉 - 单网一般 - 单网抗诉 

        :param restags: The restags of this VmsTemplateStatus.
        :type restags: str
        """
        self._restags = restags

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
        if not isinstance(other, VmsTemplateStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
