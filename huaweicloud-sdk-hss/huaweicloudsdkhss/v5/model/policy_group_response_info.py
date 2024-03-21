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
        'deletable': 'bool',
        'host_num': 'int',
        'default_group': 'bool',
        'support_os': 'str',
        'support_version': 'str'
    }

    attribute_map = {
        'group_name': 'group_name',
        'group_id': 'group_id',
        'description': 'description',
        'deletable': 'deletable',
        'host_num': 'host_num',
        'default_group': 'default_group',
        'support_os': 'support_os',
        'support_version': 'support_version'
    }

    def __init__(self, group_name=None, group_id=None, description=None, deletable=None, host_num=None, default_group=None, support_os=None, support_version=None):
        """PolicyGroupResponseInfo

        The model defined in huaweicloud sdk

        :param group_name: 策略组名
        :type group_name: str
        :param group_id: 策略组ID
        :type group_id: str
        :param description: 策略组的描述信息
        :type description: str
        :param deletable: 是否允许删除该策略组
        :type deletable: bool
        :param host_num: 关联服务器数
        :type host_num: int
        :param default_group: 是否是默认策略组
        :type default_group: bool
        :param support_os: 支持的操作系统，包含如下:   - Linux ：支持Linux系统   - Windows : 支持Windows系统
        :type support_os: str
        :param support_version: 支持的版本，包含如下:   - hss.version.basic ：基础版策略组   - hss.version.advanced : 专业版策略组   - hss.version.enterprise : 企业版策略组   - hss.version.premium : 旗舰版策略组   - hss.version.wtp : 网页防篡改版策略组   - hss.version.container.enterprise : 容器版策略组
        :type support_version: str
        """
        
        

        self._group_name = None
        self._group_id = None
        self._description = None
        self._deletable = None
        self._host_num = None
        self._default_group = None
        self._support_os = None
        self._support_version = None
        self.discriminator = None

        if group_name is not None:
            self.group_name = group_name
        if group_id is not None:
            self.group_id = group_id
        if description is not None:
            self.description = description
        if deletable is not None:
            self.deletable = deletable
        if host_num is not None:
            self.host_num = host_num
        if default_group is not None:
            self.default_group = default_group
        if support_os is not None:
            self.support_os = support_os
        if support_version is not None:
            self.support_version = support_version

    @property
    def group_name(self):
        """Gets the group_name of this PolicyGroupResponseInfo.

        策略组名

        :return: The group_name of this PolicyGroupResponseInfo.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this PolicyGroupResponseInfo.

        策略组名

        :param group_name: The group_name of this PolicyGroupResponseInfo.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def group_id(self):
        """Gets the group_id of this PolicyGroupResponseInfo.

        策略组ID

        :return: The group_id of this PolicyGroupResponseInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this PolicyGroupResponseInfo.

        策略组ID

        :param group_id: The group_id of this PolicyGroupResponseInfo.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def description(self):
        """Gets the description of this PolicyGroupResponseInfo.

        策略组的描述信息

        :return: The description of this PolicyGroupResponseInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PolicyGroupResponseInfo.

        策略组的描述信息

        :param description: The description of this PolicyGroupResponseInfo.
        :type description: str
        """
        self._description = description

    @property
    def deletable(self):
        """Gets the deletable of this PolicyGroupResponseInfo.

        是否允许删除该策略组

        :return: The deletable of this PolicyGroupResponseInfo.
        :rtype: bool
        """
        return self._deletable

    @deletable.setter
    def deletable(self, deletable):
        """Sets the deletable of this PolicyGroupResponseInfo.

        是否允许删除该策略组

        :param deletable: The deletable of this PolicyGroupResponseInfo.
        :type deletable: bool
        """
        self._deletable = deletable

    @property
    def host_num(self):
        """Gets the host_num of this PolicyGroupResponseInfo.

        关联服务器数

        :return: The host_num of this PolicyGroupResponseInfo.
        :rtype: int
        """
        return self._host_num

    @host_num.setter
    def host_num(self, host_num):
        """Sets the host_num of this PolicyGroupResponseInfo.

        关联服务器数

        :param host_num: The host_num of this PolicyGroupResponseInfo.
        :type host_num: int
        """
        self._host_num = host_num

    @property
    def default_group(self):
        """Gets the default_group of this PolicyGroupResponseInfo.

        是否是默认策略组

        :return: The default_group of this PolicyGroupResponseInfo.
        :rtype: bool
        """
        return self._default_group

    @default_group.setter
    def default_group(self, default_group):
        """Sets the default_group of this PolicyGroupResponseInfo.

        是否是默认策略组

        :param default_group: The default_group of this PolicyGroupResponseInfo.
        :type default_group: bool
        """
        self._default_group = default_group

    @property
    def support_os(self):
        """Gets the support_os of this PolicyGroupResponseInfo.

        支持的操作系统，包含如下:   - Linux ：支持Linux系统   - Windows : 支持Windows系统

        :return: The support_os of this PolicyGroupResponseInfo.
        :rtype: str
        """
        return self._support_os

    @support_os.setter
    def support_os(self, support_os):
        """Sets the support_os of this PolicyGroupResponseInfo.

        支持的操作系统，包含如下:   - Linux ：支持Linux系统   - Windows : 支持Windows系统

        :param support_os: The support_os of this PolicyGroupResponseInfo.
        :type support_os: str
        """
        self._support_os = support_os

    @property
    def support_version(self):
        """Gets the support_version of this PolicyGroupResponseInfo.

        支持的版本，包含如下:   - hss.version.basic ：基础版策略组   - hss.version.advanced : 专业版策略组   - hss.version.enterprise : 企业版策略组   - hss.version.premium : 旗舰版策略组   - hss.version.wtp : 网页防篡改版策略组   - hss.version.container.enterprise : 容器版策略组

        :return: The support_version of this PolicyGroupResponseInfo.
        :rtype: str
        """
        return self._support_version

    @support_version.setter
    def support_version(self, support_version):
        """Sets the support_version of this PolicyGroupResponseInfo.

        支持的版本，包含如下:   - hss.version.basic ：基础版策略组   - hss.version.advanced : 专业版策略组   - hss.version.enterprise : 企业版策略组   - hss.version.premium : 旗舰版策略组   - hss.version.wtp : 网页防篡改版策略组   - hss.version.container.enterprise : 容器版策略组

        :param support_version: The support_version of this PolicyGroupResponseInfo.
        :type support_version: str
        """
        self._support_version = support_version

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
