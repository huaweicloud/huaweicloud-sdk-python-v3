# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnumDataInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'current_cloud_service_id': 'str',
        'description': 'str',
        'level_id': 'str',
        'mtm_region': 'str',
        'mtm_type': 'str',
        'source_id': 'str',
        'title': 'str',
        'is_change_event': 'bool',
        'is_service_interrupt': 'bool',
        'is_deleted': 'bool',
        'match_type': 'str',
        'ticket_id': 'str',
        'name_zh': 'str',
        'name_en': 'str',
        'user_name': 'str',
        'full_name_zh': 'str',
        'full_name_en': 'str',
        'name_zh_path': 'str',
        'name_en_path': 'str',
        'status': 'str',
        'biz_id': 'str',
        'prop_id': 'str',
        'model_id': 'str',
        'enum_type_id': 'str'
    }

    attribute_map = {
        'current_cloud_service_id': 'current_cloud_service_id',
        'description': 'description',
        'level_id': 'level_id',
        'mtm_region': 'mtm_region',
        'mtm_type': 'mtm_type',
        'source_id': 'source_id',
        'title': 'title',
        'is_change_event': 'is_change_event',
        'is_service_interrupt': 'is_service_interrupt',
        'is_deleted': 'is_deleted',
        'match_type': 'match_type',
        'ticket_id': 'ticket_id',
        'name_zh': 'name_zh',
        'name_en': 'name_en',
        'user_name': 'user_name',
        'full_name_zh': 'full_name_zh',
        'full_name_en': 'full_name_en',
        'name_zh_path': 'name_zh_path',
        'name_en_path': 'name_en_path',
        'status': 'status',
        'biz_id': 'biz_id',
        'prop_id': 'prop_id',
        'model_id': 'model_id',
        'enum_type_id': 'enum_type_id'
    }

    def __init__(self, current_cloud_service_id=None, description=None, level_id=None, mtm_region=None, mtm_type=None, source_id=None, title=None, is_change_event=None, is_service_interrupt=None, is_deleted=None, match_type=None, ticket_id=None, name_zh=None, name_en=None, user_name=None, full_name_zh=None, full_name_en=None, name_zh_path=None, name_en_path=None, status=None, biz_id=None, prop_id=None, model_id=None, enum_type_id=None):
        r"""EnumDataInfo

        The model defined in huaweicloud sdk

        :param current_cloud_service_id: 扩展字段
        :type current_cloud_service_id: str
        :param description: 扩展字段
        :type description: str
        :param level_id: 扩展字段
        :type level_id: str
        :param mtm_region: 扩展字段
        :type mtm_region: str
        :param mtm_type: 扩展字段
        :type mtm_type: str
        :param source_id: 扩展字段
        :type source_id: str
        :param title: 扩展字段
        :type title: str
        :param is_change_event: 是否变更事件
        :type is_change_event: bool
        :param is_service_interrupt: 是否变更事件
        :type is_service_interrupt: bool
        :param is_deleted: 是否删除
        :type is_deleted: bool
        :param match_type: 匹配类型
        :type match_type: str
        :param ticket_id: 所属单号
        :type ticket_id: str
        :param name_zh: 中文名
        :type name_zh: str
        :param name_en: 英文名
        :type name_en: str
        :param user_name: 工号
        :type user_name: str
        :param full_name_zh: 中文名
        :type full_name_zh: str
        :param full_name_en: 英文名
        :type full_name_en: str
        :param name_zh_path: 中文名路径
        :type name_zh_path: str
        :param name_en_path: 中文名路径
        :type name_en_path: str
        :param status: status
        :type status: str
        :param biz_id: 唯一id
        :type biz_id: str
        :param prop_id: 字段id
        :type prop_id: str
        :param model_id: 模型id
        :type model_id: str
        :param enum_type_id: 枚举类型
        :type enum_type_id: str
        """
        
        

        self._current_cloud_service_id = None
        self._description = None
        self._level_id = None
        self._mtm_region = None
        self._mtm_type = None
        self._source_id = None
        self._title = None
        self._is_change_event = None
        self._is_service_interrupt = None
        self._is_deleted = None
        self._match_type = None
        self._ticket_id = None
        self._name_zh = None
        self._name_en = None
        self._user_name = None
        self._full_name_zh = None
        self._full_name_en = None
        self._name_zh_path = None
        self._name_en_path = None
        self._status = None
        self._biz_id = None
        self._prop_id = None
        self._model_id = None
        self._enum_type_id = None
        self.discriminator = None

        if current_cloud_service_id is not None:
            self.current_cloud_service_id = current_cloud_service_id
        if description is not None:
            self.description = description
        if level_id is not None:
            self.level_id = level_id
        if mtm_region is not None:
            self.mtm_region = mtm_region
        if mtm_type is not None:
            self.mtm_type = mtm_type
        if source_id is not None:
            self.source_id = source_id
        if title is not None:
            self.title = title
        if is_change_event is not None:
            self.is_change_event = is_change_event
        if is_service_interrupt is not None:
            self.is_service_interrupt = is_service_interrupt
        if is_deleted is not None:
            self.is_deleted = is_deleted
        if match_type is not None:
            self.match_type = match_type
        if ticket_id is not None:
            self.ticket_id = ticket_id
        if name_zh is not None:
            self.name_zh = name_zh
        if name_en is not None:
            self.name_en = name_en
        if user_name is not None:
            self.user_name = user_name
        if full_name_zh is not None:
            self.full_name_zh = full_name_zh
        if full_name_en is not None:
            self.full_name_en = full_name_en
        if name_zh_path is not None:
            self.name_zh_path = name_zh_path
        if name_en_path is not None:
            self.name_en_path = name_en_path
        if status is not None:
            self.status = status
        if biz_id is not None:
            self.biz_id = biz_id
        if prop_id is not None:
            self.prop_id = prop_id
        if model_id is not None:
            self.model_id = model_id
        if enum_type_id is not None:
            self.enum_type_id = enum_type_id

    @property
    def current_cloud_service_id(self):
        r"""Gets the current_cloud_service_id of this EnumDataInfo.

        扩展字段

        :return: The current_cloud_service_id of this EnumDataInfo.
        :rtype: str
        """
        return self._current_cloud_service_id

    @current_cloud_service_id.setter
    def current_cloud_service_id(self, current_cloud_service_id):
        r"""Sets the current_cloud_service_id of this EnumDataInfo.

        扩展字段

        :param current_cloud_service_id: The current_cloud_service_id of this EnumDataInfo.
        :type current_cloud_service_id: str
        """
        self._current_cloud_service_id = current_cloud_service_id

    @property
    def description(self):
        r"""Gets the description of this EnumDataInfo.

        扩展字段

        :return: The description of this EnumDataInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this EnumDataInfo.

        扩展字段

        :param description: The description of this EnumDataInfo.
        :type description: str
        """
        self._description = description

    @property
    def level_id(self):
        r"""Gets the level_id of this EnumDataInfo.

        扩展字段

        :return: The level_id of this EnumDataInfo.
        :rtype: str
        """
        return self._level_id

    @level_id.setter
    def level_id(self, level_id):
        r"""Sets the level_id of this EnumDataInfo.

        扩展字段

        :param level_id: The level_id of this EnumDataInfo.
        :type level_id: str
        """
        self._level_id = level_id

    @property
    def mtm_region(self):
        r"""Gets the mtm_region of this EnumDataInfo.

        扩展字段

        :return: The mtm_region of this EnumDataInfo.
        :rtype: str
        """
        return self._mtm_region

    @mtm_region.setter
    def mtm_region(self, mtm_region):
        r"""Sets the mtm_region of this EnumDataInfo.

        扩展字段

        :param mtm_region: The mtm_region of this EnumDataInfo.
        :type mtm_region: str
        """
        self._mtm_region = mtm_region

    @property
    def mtm_type(self):
        r"""Gets the mtm_type of this EnumDataInfo.

        扩展字段

        :return: The mtm_type of this EnumDataInfo.
        :rtype: str
        """
        return self._mtm_type

    @mtm_type.setter
    def mtm_type(self, mtm_type):
        r"""Sets the mtm_type of this EnumDataInfo.

        扩展字段

        :param mtm_type: The mtm_type of this EnumDataInfo.
        :type mtm_type: str
        """
        self._mtm_type = mtm_type

    @property
    def source_id(self):
        r"""Gets the source_id of this EnumDataInfo.

        扩展字段

        :return: The source_id of this EnumDataInfo.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        r"""Sets the source_id of this EnumDataInfo.

        扩展字段

        :param source_id: The source_id of this EnumDataInfo.
        :type source_id: str
        """
        self._source_id = source_id

    @property
    def title(self):
        r"""Gets the title of this EnumDataInfo.

        扩展字段

        :return: The title of this EnumDataInfo.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this EnumDataInfo.

        扩展字段

        :param title: The title of this EnumDataInfo.
        :type title: str
        """
        self._title = title

    @property
    def is_change_event(self):
        r"""Gets the is_change_event of this EnumDataInfo.

        是否变更事件

        :return: The is_change_event of this EnumDataInfo.
        :rtype: bool
        """
        return self._is_change_event

    @is_change_event.setter
    def is_change_event(self, is_change_event):
        r"""Sets the is_change_event of this EnumDataInfo.

        是否变更事件

        :param is_change_event: The is_change_event of this EnumDataInfo.
        :type is_change_event: bool
        """
        self._is_change_event = is_change_event

    @property
    def is_service_interrupt(self):
        r"""Gets the is_service_interrupt of this EnumDataInfo.

        是否变更事件

        :return: The is_service_interrupt of this EnumDataInfo.
        :rtype: bool
        """
        return self._is_service_interrupt

    @is_service_interrupt.setter
    def is_service_interrupt(self, is_service_interrupt):
        r"""Sets the is_service_interrupt of this EnumDataInfo.

        是否变更事件

        :param is_service_interrupt: The is_service_interrupt of this EnumDataInfo.
        :type is_service_interrupt: bool
        """
        self._is_service_interrupt = is_service_interrupt

    @property
    def is_deleted(self):
        r"""Gets the is_deleted of this EnumDataInfo.

        是否删除

        :return: The is_deleted of this EnumDataInfo.
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        r"""Sets the is_deleted of this EnumDataInfo.

        是否删除

        :param is_deleted: The is_deleted of this EnumDataInfo.
        :type is_deleted: bool
        """
        self._is_deleted = is_deleted

    @property
    def match_type(self):
        r"""Gets the match_type of this EnumDataInfo.

        匹配类型

        :return: The match_type of this EnumDataInfo.
        :rtype: str
        """
        return self._match_type

    @match_type.setter
    def match_type(self, match_type):
        r"""Sets the match_type of this EnumDataInfo.

        匹配类型

        :param match_type: The match_type of this EnumDataInfo.
        :type match_type: str
        """
        self._match_type = match_type

    @property
    def ticket_id(self):
        r"""Gets the ticket_id of this EnumDataInfo.

        所属单号

        :return: The ticket_id of this EnumDataInfo.
        :rtype: str
        """
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, ticket_id):
        r"""Sets the ticket_id of this EnumDataInfo.

        所属单号

        :param ticket_id: The ticket_id of this EnumDataInfo.
        :type ticket_id: str
        """
        self._ticket_id = ticket_id

    @property
    def name_zh(self):
        r"""Gets the name_zh of this EnumDataInfo.

        中文名

        :return: The name_zh of this EnumDataInfo.
        :rtype: str
        """
        return self._name_zh

    @name_zh.setter
    def name_zh(self, name_zh):
        r"""Sets the name_zh of this EnumDataInfo.

        中文名

        :param name_zh: The name_zh of this EnumDataInfo.
        :type name_zh: str
        """
        self._name_zh = name_zh

    @property
    def name_en(self):
        r"""Gets the name_en of this EnumDataInfo.

        英文名

        :return: The name_en of this EnumDataInfo.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        r"""Sets the name_en of this EnumDataInfo.

        英文名

        :param name_en: The name_en of this EnumDataInfo.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def user_name(self):
        r"""Gets the user_name of this EnumDataInfo.

        工号

        :return: The user_name of this EnumDataInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this EnumDataInfo.

        工号

        :param user_name: The user_name of this EnumDataInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def full_name_zh(self):
        r"""Gets the full_name_zh of this EnumDataInfo.

        中文名

        :return: The full_name_zh of this EnumDataInfo.
        :rtype: str
        """
        return self._full_name_zh

    @full_name_zh.setter
    def full_name_zh(self, full_name_zh):
        r"""Sets the full_name_zh of this EnumDataInfo.

        中文名

        :param full_name_zh: The full_name_zh of this EnumDataInfo.
        :type full_name_zh: str
        """
        self._full_name_zh = full_name_zh

    @property
    def full_name_en(self):
        r"""Gets the full_name_en of this EnumDataInfo.

        英文名

        :return: The full_name_en of this EnumDataInfo.
        :rtype: str
        """
        return self._full_name_en

    @full_name_en.setter
    def full_name_en(self, full_name_en):
        r"""Sets the full_name_en of this EnumDataInfo.

        英文名

        :param full_name_en: The full_name_en of this EnumDataInfo.
        :type full_name_en: str
        """
        self._full_name_en = full_name_en

    @property
    def name_zh_path(self):
        r"""Gets the name_zh_path of this EnumDataInfo.

        中文名路径

        :return: The name_zh_path of this EnumDataInfo.
        :rtype: str
        """
        return self._name_zh_path

    @name_zh_path.setter
    def name_zh_path(self, name_zh_path):
        r"""Sets the name_zh_path of this EnumDataInfo.

        中文名路径

        :param name_zh_path: The name_zh_path of this EnumDataInfo.
        :type name_zh_path: str
        """
        self._name_zh_path = name_zh_path

    @property
    def name_en_path(self):
        r"""Gets the name_en_path of this EnumDataInfo.

        中文名路径

        :return: The name_en_path of this EnumDataInfo.
        :rtype: str
        """
        return self._name_en_path

    @name_en_path.setter
    def name_en_path(self, name_en_path):
        r"""Sets the name_en_path of this EnumDataInfo.

        中文名路径

        :param name_en_path: The name_en_path of this EnumDataInfo.
        :type name_en_path: str
        """
        self._name_en_path = name_en_path

    @property
    def status(self):
        r"""Gets the status of this EnumDataInfo.

        status

        :return: The status of this EnumDataInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this EnumDataInfo.

        status

        :param status: The status of this EnumDataInfo.
        :type status: str
        """
        self._status = status

    @property
    def biz_id(self):
        r"""Gets the biz_id of this EnumDataInfo.

        唯一id

        :return: The biz_id of this EnumDataInfo.
        :rtype: str
        """
        return self._biz_id

    @biz_id.setter
    def biz_id(self, biz_id):
        r"""Sets the biz_id of this EnumDataInfo.

        唯一id

        :param biz_id: The biz_id of this EnumDataInfo.
        :type biz_id: str
        """
        self._biz_id = biz_id

    @property
    def prop_id(self):
        r"""Gets the prop_id of this EnumDataInfo.

        字段id

        :return: The prop_id of this EnumDataInfo.
        :rtype: str
        """
        return self._prop_id

    @prop_id.setter
    def prop_id(self, prop_id):
        r"""Sets the prop_id of this EnumDataInfo.

        字段id

        :param prop_id: The prop_id of this EnumDataInfo.
        :type prop_id: str
        """
        self._prop_id = prop_id

    @property
    def model_id(self):
        r"""Gets the model_id of this EnumDataInfo.

        模型id

        :return: The model_id of this EnumDataInfo.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        r"""Sets the model_id of this EnumDataInfo.

        模型id

        :param model_id: The model_id of this EnumDataInfo.
        :type model_id: str
        """
        self._model_id = model_id

    @property
    def enum_type_id(self):
        r"""Gets the enum_type_id of this EnumDataInfo.

        枚举类型

        :return: The enum_type_id of this EnumDataInfo.
        :rtype: str
        """
        return self._enum_type_id

    @enum_type_id.setter
    def enum_type_id(self, enum_type_id):
        r"""Sets the enum_type_id of this EnumDataInfo.

        枚举类型

        :param enum_type_id: The enum_type_id of this EnumDataInfo.
        :type enum_type_id: str
        """
        self._enum_type_id = enum_type_id

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
        if not isinstance(other, EnumDataInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
