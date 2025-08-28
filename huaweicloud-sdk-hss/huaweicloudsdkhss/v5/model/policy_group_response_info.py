# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyGroupResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_name': 'str',
        'group_id': 'str',
        'description': 'str',
        'host_num': 'int',
        'default_group': 'bool',
        'deletable': 'bool',
        'support_os': 'str',
        'support_version': 'str',
        'protect_mode': 'str'
    }

    attribute_map = {
        'group_name': 'group_name',
        'group_id': 'group_id',
        'description': 'description',
        'host_num': 'host_num',
        'default_group': 'default_group',
        'deletable': 'deletable',
        'support_os': 'support_os',
        'support_version': 'support_version',
        'protect_mode': 'protect_mode'
    }

    def __init__(self, group_name=None, group_id=None, description=None, host_num=None, default_group=None, deletable=None, support_os=None, support_version=None, protect_mode=None):
        r"""PolicyGroupResponseInfo

        The model defined in huaweicloud sdk

        :param group_name: **参数解释**: 策略组名称 **取值范围**: 字符长度1-256位 
        :type group_name: str
        :param group_id: **参数解释**: 策略组ID **取值范围**: 字符长度1-256位 
        :type group_id: str
        :param description: **参数解释**: 策略组描述 **取值范围**: 字符长度0-64位 
        :type description: str
        :param host_num: **参数解释**: 关联服务器数 **取值范围**: 取值0-1000000 
        :type host_num: int
        :param default_group: **参数解释**: 是否是默认策略组 **取值范围**: - true: 是默认策略组。 - false: 不是默认策略组。 
        :type default_group: bool
        :param deletable: **参数解释**: 是否可以删除，只有default_group为false且host_num为0时可以删除 **取值范围**: - true: 可以删除。 - false: 不可以删除。 
        :type deletable: bool
        :param support_os: **参数解释**: 支持的操作系统 **取值范围**: - Linux: 支持Linux操作系统。 - Windows: 支持Windows操作系统。 
        :type support_os: str
        :param support_version: **参数解释**: 支持的版本 **取值范围**: - hss.version.advanced: 专业版。 - hss.version.enterprise: 企业版。 - hss.version.premium: 旗舰版。 - hss.version.wtp: 网页防篡改版。 - hss.version.container.enterprise: 容器版。 
        :type support_version: str
        :param protect_mode: **参数解释**: 防护模式 **取值范围**: - high_detection: 高检出模式。 - equalization: 均衡模式。 
        :type protect_mode: str
        """
        
        

        self._group_name = None
        self._group_id = None
        self._description = None
        self._host_num = None
        self._default_group = None
        self._deletable = None
        self._support_os = None
        self._support_version = None
        self._protect_mode = None
        self.discriminator = None

        if group_name is not None:
            self.group_name = group_name
        if group_id is not None:
            self.group_id = group_id
        if description is not None:
            self.description = description
        if host_num is not None:
            self.host_num = host_num
        if default_group is not None:
            self.default_group = default_group
        if deletable is not None:
            self.deletable = deletable
        if support_os is not None:
            self.support_os = support_os
        if support_version is not None:
            self.support_version = support_version
        if protect_mode is not None:
            self.protect_mode = protect_mode

    @property
    def group_name(self):
        r"""Gets the group_name of this PolicyGroupResponseInfo.

        **参数解释**: 策略组名称 **取值范围**: 字符长度1-256位 

        :return: The group_name of this PolicyGroupResponseInfo.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this PolicyGroupResponseInfo.

        **参数解释**: 策略组名称 **取值范围**: 字符长度1-256位 

        :param group_name: The group_name of this PolicyGroupResponseInfo.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def group_id(self):
        r"""Gets the group_id of this PolicyGroupResponseInfo.

        **参数解释**: 策略组ID **取值范围**: 字符长度1-256位 

        :return: The group_id of this PolicyGroupResponseInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this PolicyGroupResponseInfo.

        **参数解释**: 策略组ID **取值范围**: 字符长度1-256位 

        :param group_id: The group_id of this PolicyGroupResponseInfo.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def description(self):
        r"""Gets the description of this PolicyGroupResponseInfo.

        **参数解释**: 策略组描述 **取值范围**: 字符长度0-64位 

        :return: The description of this PolicyGroupResponseInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PolicyGroupResponseInfo.

        **参数解释**: 策略组描述 **取值范围**: 字符长度0-64位 

        :param description: The description of this PolicyGroupResponseInfo.
        :type description: str
        """
        self._description = description

    @property
    def host_num(self):
        r"""Gets the host_num of this PolicyGroupResponseInfo.

        **参数解释**: 关联服务器数 **取值范围**: 取值0-1000000 

        :return: The host_num of this PolicyGroupResponseInfo.
        :rtype: int
        """
        return self._host_num

    @host_num.setter
    def host_num(self, host_num):
        r"""Sets the host_num of this PolicyGroupResponseInfo.

        **参数解释**: 关联服务器数 **取值范围**: 取值0-1000000 

        :param host_num: The host_num of this PolicyGroupResponseInfo.
        :type host_num: int
        """
        self._host_num = host_num

    @property
    def default_group(self):
        r"""Gets the default_group of this PolicyGroupResponseInfo.

        **参数解释**: 是否是默认策略组 **取值范围**: - true: 是默认策略组。 - false: 不是默认策略组。 

        :return: The default_group of this PolicyGroupResponseInfo.
        :rtype: bool
        """
        return self._default_group

    @default_group.setter
    def default_group(self, default_group):
        r"""Sets the default_group of this PolicyGroupResponseInfo.

        **参数解释**: 是否是默认策略组 **取值范围**: - true: 是默认策略组。 - false: 不是默认策略组。 

        :param default_group: The default_group of this PolicyGroupResponseInfo.
        :type default_group: bool
        """
        self._default_group = default_group

    @property
    def deletable(self):
        r"""Gets the deletable of this PolicyGroupResponseInfo.

        **参数解释**: 是否可以删除，只有default_group为false且host_num为0时可以删除 **取值范围**: - true: 可以删除。 - false: 不可以删除。 

        :return: The deletable of this PolicyGroupResponseInfo.
        :rtype: bool
        """
        return self._deletable

    @deletable.setter
    def deletable(self, deletable):
        r"""Sets the deletable of this PolicyGroupResponseInfo.

        **参数解释**: 是否可以删除，只有default_group为false且host_num为0时可以删除 **取值范围**: - true: 可以删除。 - false: 不可以删除。 

        :param deletable: The deletable of this PolicyGroupResponseInfo.
        :type deletable: bool
        """
        self._deletable = deletable

    @property
    def support_os(self):
        r"""Gets the support_os of this PolicyGroupResponseInfo.

        **参数解释**: 支持的操作系统 **取值范围**: - Linux: 支持Linux操作系统。 - Windows: 支持Windows操作系统。 

        :return: The support_os of this PolicyGroupResponseInfo.
        :rtype: str
        """
        return self._support_os

    @support_os.setter
    def support_os(self, support_os):
        r"""Sets the support_os of this PolicyGroupResponseInfo.

        **参数解释**: 支持的操作系统 **取值范围**: - Linux: 支持Linux操作系统。 - Windows: 支持Windows操作系统。 

        :param support_os: The support_os of this PolicyGroupResponseInfo.
        :type support_os: str
        """
        self._support_os = support_os

    @property
    def support_version(self):
        r"""Gets the support_version of this PolicyGroupResponseInfo.

        **参数解释**: 支持的版本 **取值范围**: - hss.version.advanced: 专业版。 - hss.version.enterprise: 企业版。 - hss.version.premium: 旗舰版。 - hss.version.wtp: 网页防篡改版。 - hss.version.container.enterprise: 容器版。 

        :return: The support_version of this PolicyGroupResponseInfo.
        :rtype: str
        """
        return self._support_version

    @support_version.setter
    def support_version(self, support_version):
        r"""Sets the support_version of this PolicyGroupResponseInfo.

        **参数解释**: 支持的版本 **取值范围**: - hss.version.advanced: 专业版。 - hss.version.enterprise: 企业版。 - hss.version.premium: 旗舰版。 - hss.version.wtp: 网页防篡改版。 - hss.version.container.enterprise: 容器版。 

        :param support_version: The support_version of this PolicyGroupResponseInfo.
        :type support_version: str
        """
        self._support_version = support_version

    @property
    def protect_mode(self):
        r"""Gets the protect_mode of this PolicyGroupResponseInfo.

        **参数解释**: 防护模式 **取值范围**: - high_detection: 高检出模式。 - equalization: 均衡模式。 

        :return: The protect_mode of this PolicyGroupResponseInfo.
        :rtype: str
        """
        return self._protect_mode

    @protect_mode.setter
    def protect_mode(self, protect_mode):
        r"""Sets the protect_mode of this PolicyGroupResponseInfo.

        **参数解释**: 防护模式 **取值范围**: - high_detection: 高检出模式。 - equalization: 均衡模式。 

        :param protect_mode: The protect_mode of this PolicyGroupResponseInfo.
        :type protect_mode: str
        """
        self._protect_mode = protect_mode

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
        if not isinstance(other, PolicyGroupResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
