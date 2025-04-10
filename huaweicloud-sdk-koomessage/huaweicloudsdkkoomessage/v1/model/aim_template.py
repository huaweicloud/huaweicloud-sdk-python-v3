# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AIMTemplate:

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
        'tpl_name': 'str',
        'scene': 'str',
        'tpl_state': 'int',
        'disable_desc': 'str',
        'disable_time': 'str',
        'audit_state': 'int',
        'audit_desc': 'str',
        'description': 'str',
        'creation_time': 'str',
        'update_time': 'str',
        'pages': 'str',
        'params': 'list[AIMTemplateParams]',
        'factory_info': 'list[FactoryInfo]',
        'match_type': 'int',
        'card_id': 'str',
        'sub_type': 'int',
        'preview_url': 'str'
    }

    attribute_map = {
        'tpl_id': 'tpl_id',
        'tpl_name': 'tpl_name',
        'scene': 'scene',
        'tpl_state': 'tpl_state',
        'disable_desc': 'disable_desc',
        'disable_time': 'disable_time',
        'audit_state': 'audit_state',
        'audit_desc': 'audit_desc',
        'description': 'description',
        'creation_time': 'creation_time',
        'update_time': 'update_time',
        'pages': 'pages',
        'params': 'params',
        'factory_info': 'factory_info',
        'match_type': 'match_type',
        'card_id': 'card_id',
        'sub_type': 'sub_type',
        'preview_url': 'preview_url'
    }

    def __init__(self, tpl_id=None, tpl_name=None, scene=None, tpl_state=None, disable_desc=None, disable_time=None, audit_state=None, audit_desc=None, description=None, creation_time=None, update_time=None, pages=None, params=None, factory_info=None, match_type=None, card_id=None, sub_type=None, preview_url=None):
        r"""AIMTemplate

        The model defined in huaweicloud sdk

        :param tpl_id: 智能信息模板ID。  &gt; 智能信息平台生成的模板ID，由9位数字组成。 
        :type tpl_id: str
        :param tpl_name: 智能信息模板名称。
        :type tpl_name: str
        :param scene: 场景类型。 
        :type scene: str
        :param tpl_state: 模板状态。  - 0：禁用 - 1：启用 
        :type tpl_state: int
        :param disable_desc: 禁用原因。
        :type disable_desc: str
        :param disable_time: 禁用时间。样例：1970-01-01T00:00 :00Z。
        :type disable_time: str
        :param audit_state: 审核状态。 - 0：未提交  - 1：审核中  - 2：审核通过  - 3：审核失败 
        :type audit_state: int
        :param audit_desc: 审批信息。
        :type audit_desc: str
        :param description: 短信示例。  &gt;对应创建个人模板API中的入参sms_example。 
        :type description: str
        :param creation_time: 创建时间。样例为：1970-01-01T00:00:00Z。
        :type creation_time: str
        :param update_time: 更新时间。样例为：1970-01-01T00:00:00Z。
        :type update_time: str
        :param pages: 模板页面HTML，JSON格式。
        :type pages: str
        :param params: 模板动态参数列表。
        :type params: list[:class:`huaweicloudsdkkoomessage.v1.AIMTemplateParams`]
        :param factory_info: 支持厂商列表。
        :type factory_info: list[:class:`huaweicloudsdkkoomessage.v1.FactoryInfo`]
        :param match_type: 审核状态。 - 1：短链解析模板 - 2：文本识别模板 - 4：一体化模板 
        :type match_type: int
        :param card_id: 布局类型。
        :type card_id: str
        :param sub_type: sub_type。
        :type sub_type: int
        :param preview_url: 模板二维码预览地址。
        :type preview_url: str
        """
        
        

        self._tpl_id = None
        self._tpl_name = None
        self._scene = None
        self._tpl_state = None
        self._disable_desc = None
        self._disable_time = None
        self._audit_state = None
        self._audit_desc = None
        self._description = None
        self._creation_time = None
        self._update_time = None
        self._pages = None
        self._params = None
        self._factory_info = None
        self._match_type = None
        self._card_id = None
        self._sub_type = None
        self._preview_url = None
        self.discriminator = None

        if tpl_id is not None:
            self.tpl_id = tpl_id
        if tpl_name is not None:
            self.tpl_name = tpl_name
        if scene is not None:
            self.scene = scene
        if tpl_state is not None:
            self.tpl_state = tpl_state
        if disable_desc is not None:
            self.disable_desc = disable_desc
        if disable_time is not None:
            self.disable_time = disable_time
        if audit_state is not None:
            self.audit_state = audit_state
        if audit_desc is not None:
            self.audit_desc = audit_desc
        if description is not None:
            self.description = description
        if creation_time is not None:
            self.creation_time = creation_time
        if update_time is not None:
            self.update_time = update_time
        if pages is not None:
            self.pages = pages
        if params is not None:
            self.params = params
        if factory_info is not None:
            self.factory_info = factory_info
        if match_type is not None:
            self.match_type = match_type
        if card_id is not None:
            self.card_id = card_id
        if sub_type is not None:
            self.sub_type = sub_type
        if preview_url is not None:
            self.preview_url = preview_url

    @property
    def tpl_id(self):
        r"""Gets the tpl_id of this AIMTemplate.

        智能信息模板ID。  > 智能信息平台生成的模板ID，由9位数字组成。 

        :return: The tpl_id of this AIMTemplate.
        :rtype: str
        """
        return self._tpl_id

    @tpl_id.setter
    def tpl_id(self, tpl_id):
        r"""Sets the tpl_id of this AIMTemplate.

        智能信息模板ID。  > 智能信息平台生成的模板ID，由9位数字组成。 

        :param tpl_id: The tpl_id of this AIMTemplate.
        :type tpl_id: str
        """
        self._tpl_id = tpl_id

    @property
    def tpl_name(self):
        r"""Gets the tpl_name of this AIMTemplate.

        智能信息模板名称。

        :return: The tpl_name of this AIMTemplate.
        :rtype: str
        """
        return self._tpl_name

    @tpl_name.setter
    def tpl_name(self, tpl_name):
        r"""Sets the tpl_name of this AIMTemplate.

        智能信息模板名称。

        :param tpl_name: The tpl_name of this AIMTemplate.
        :type tpl_name: str
        """
        self._tpl_name = tpl_name

    @property
    def scene(self):
        r"""Gets the scene of this AIMTemplate.

        场景类型。 

        :return: The scene of this AIMTemplate.
        :rtype: str
        """
        return self._scene

    @scene.setter
    def scene(self, scene):
        r"""Sets the scene of this AIMTemplate.

        场景类型。 

        :param scene: The scene of this AIMTemplate.
        :type scene: str
        """
        self._scene = scene

    @property
    def tpl_state(self):
        r"""Gets the tpl_state of this AIMTemplate.

        模板状态。  - 0：禁用 - 1：启用 

        :return: The tpl_state of this AIMTemplate.
        :rtype: int
        """
        return self._tpl_state

    @tpl_state.setter
    def tpl_state(self, tpl_state):
        r"""Sets the tpl_state of this AIMTemplate.

        模板状态。  - 0：禁用 - 1：启用 

        :param tpl_state: The tpl_state of this AIMTemplate.
        :type tpl_state: int
        """
        self._tpl_state = tpl_state

    @property
    def disable_desc(self):
        r"""Gets the disable_desc of this AIMTemplate.

        禁用原因。

        :return: The disable_desc of this AIMTemplate.
        :rtype: str
        """
        return self._disable_desc

    @disable_desc.setter
    def disable_desc(self, disable_desc):
        r"""Sets the disable_desc of this AIMTemplate.

        禁用原因。

        :param disable_desc: The disable_desc of this AIMTemplate.
        :type disable_desc: str
        """
        self._disable_desc = disable_desc

    @property
    def disable_time(self):
        r"""Gets the disable_time of this AIMTemplate.

        禁用时间。样例：1970-01-01T00:00 :00Z。

        :return: The disable_time of this AIMTemplate.
        :rtype: str
        """
        return self._disable_time

    @disable_time.setter
    def disable_time(self, disable_time):
        r"""Sets the disable_time of this AIMTemplate.

        禁用时间。样例：1970-01-01T00:00 :00Z。

        :param disable_time: The disable_time of this AIMTemplate.
        :type disable_time: str
        """
        self._disable_time = disable_time

    @property
    def audit_state(self):
        r"""Gets the audit_state of this AIMTemplate.

        审核状态。 - 0：未提交  - 1：审核中  - 2：审核通过  - 3：审核失败 

        :return: The audit_state of this AIMTemplate.
        :rtype: int
        """
        return self._audit_state

    @audit_state.setter
    def audit_state(self, audit_state):
        r"""Sets the audit_state of this AIMTemplate.

        审核状态。 - 0：未提交  - 1：审核中  - 2：审核通过  - 3：审核失败 

        :param audit_state: The audit_state of this AIMTemplate.
        :type audit_state: int
        """
        self._audit_state = audit_state

    @property
    def audit_desc(self):
        r"""Gets the audit_desc of this AIMTemplate.

        审批信息。

        :return: The audit_desc of this AIMTemplate.
        :rtype: str
        """
        return self._audit_desc

    @audit_desc.setter
    def audit_desc(self, audit_desc):
        r"""Sets the audit_desc of this AIMTemplate.

        审批信息。

        :param audit_desc: The audit_desc of this AIMTemplate.
        :type audit_desc: str
        """
        self._audit_desc = audit_desc

    @property
    def description(self):
        r"""Gets the description of this AIMTemplate.

        短信示例。  >对应创建个人模板API中的入参sms_example。 

        :return: The description of this AIMTemplate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AIMTemplate.

        短信示例。  >对应创建个人模板API中的入参sms_example。 

        :param description: The description of this AIMTemplate.
        :type description: str
        """
        self._description = description

    @property
    def creation_time(self):
        r"""Gets the creation_time of this AIMTemplate.

        创建时间。样例为：1970-01-01T00:00:00Z。

        :return: The creation_time of this AIMTemplate.
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        r"""Sets the creation_time of this AIMTemplate.

        创建时间。样例为：1970-01-01T00:00:00Z。

        :param creation_time: The creation_time of this AIMTemplate.
        :type creation_time: str
        """
        self._creation_time = creation_time

    @property
    def update_time(self):
        r"""Gets the update_time of this AIMTemplate.

        更新时间。样例为：1970-01-01T00:00:00Z。

        :return: The update_time of this AIMTemplate.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this AIMTemplate.

        更新时间。样例为：1970-01-01T00:00:00Z。

        :param update_time: The update_time of this AIMTemplate.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def pages(self):
        r"""Gets the pages of this AIMTemplate.

        模板页面HTML，JSON格式。

        :return: The pages of this AIMTemplate.
        :rtype: str
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        r"""Sets the pages of this AIMTemplate.

        模板页面HTML，JSON格式。

        :param pages: The pages of this AIMTemplate.
        :type pages: str
        """
        self._pages = pages

    @property
    def params(self):
        r"""Gets the params of this AIMTemplate.

        模板动态参数列表。

        :return: The params of this AIMTemplate.
        :rtype: list[:class:`huaweicloudsdkkoomessage.v1.AIMTemplateParams`]
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this AIMTemplate.

        模板动态参数列表。

        :param params: The params of this AIMTemplate.
        :type params: list[:class:`huaweicloudsdkkoomessage.v1.AIMTemplateParams`]
        """
        self._params = params

    @property
    def factory_info(self):
        r"""Gets the factory_info of this AIMTemplate.

        支持厂商列表。

        :return: The factory_info of this AIMTemplate.
        :rtype: list[:class:`huaweicloudsdkkoomessage.v1.FactoryInfo`]
        """
        return self._factory_info

    @factory_info.setter
    def factory_info(self, factory_info):
        r"""Sets the factory_info of this AIMTemplate.

        支持厂商列表。

        :param factory_info: The factory_info of this AIMTemplate.
        :type factory_info: list[:class:`huaweicloudsdkkoomessage.v1.FactoryInfo`]
        """
        self._factory_info = factory_info

    @property
    def match_type(self):
        r"""Gets the match_type of this AIMTemplate.

        审核状态。 - 1：短链解析模板 - 2：文本识别模板 - 4：一体化模板 

        :return: The match_type of this AIMTemplate.
        :rtype: int
        """
        return self._match_type

    @match_type.setter
    def match_type(self, match_type):
        r"""Sets the match_type of this AIMTemplate.

        审核状态。 - 1：短链解析模板 - 2：文本识别模板 - 4：一体化模板 

        :param match_type: The match_type of this AIMTemplate.
        :type match_type: int
        """
        self._match_type = match_type

    @property
    def card_id(self):
        r"""Gets the card_id of this AIMTemplate.

        布局类型。

        :return: The card_id of this AIMTemplate.
        :rtype: str
        """
        return self._card_id

    @card_id.setter
    def card_id(self, card_id):
        r"""Sets the card_id of this AIMTemplate.

        布局类型。

        :param card_id: The card_id of this AIMTemplate.
        :type card_id: str
        """
        self._card_id = card_id

    @property
    def sub_type(self):
        r"""Gets the sub_type of this AIMTemplate.

        sub_type。

        :return: The sub_type of this AIMTemplate.
        :rtype: int
        """
        return self._sub_type

    @sub_type.setter
    def sub_type(self, sub_type):
        r"""Sets the sub_type of this AIMTemplate.

        sub_type。

        :param sub_type: The sub_type of this AIMTemplate.
        :type sub_type: int
        """
        self._sub_type = sub_type

    @property
    def preview_url(self):
        r"""Gets the preview_url of this AIMTemplate.

        模板二维码预览地址。

        :return: The preview_url of this AIMTemplate.
        :rtype: str
        """
        return self._preview_url

    @preview_url.setter
    def preview_url(self, preview_url):
        r"""Sets the preview_url of this AIMTemplate.

        模板二维码预览地址。

        :param preview_url: The preview_url of this AIMTemplate.
        :type preview_url: str
        """
        self._preview_url = preview_url

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
        if not isinstance(other, AIMTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
