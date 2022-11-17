# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppRules:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_time': 'str',
        'enable': 'bool',
        'event_name': 'str',
        'hostid': 'list[str]',
        'id': 'str',
        'name': 'str',
        'projectid': 'str',
        'spec': 'AppRulesSpec'
    }

    attribute_map = {
        'create_time': 'createTime',
        'enable': 'enable',
        'event_name': 'eventName',
        'hostid': 'hostid',
        'id': 'id',
        'name': 'name',
        'projectid': 'projectid',
        'spec': 'spec'
    }

    def __init__(self, create_time=None, enable=None, event_name=None, hostid=None, id=None, name=None, projectid=None, spec=None):
        """AppRules

        The model defined in huaweicloud sdk

        :param create_time: 规则创建时间(创建时不传,修改时传查询返回的createTime)。
        :type create_time: str
        :param enable: true、false 规则是否启用。
        :type enable: bool
        :param event_name: aom_inventory_rules_event 规则事件名称,对于服务发现固定 为\&quot;aom_inventory_rules_event\&quot;。
        :type event_name: str
        :param hostid: 主机ID(暂不使用,传空即可)。
        :type hostid: list[str]
        :param id: 创建时填空，修改时填规则ID。
        :type id: str
        :param name: 规则名称。 字符长度小于64位,以小写字母(a-z)开头,只能包含0-9/a-z/-,不能以-结尾。
        :type name: str
        :param projectid: 租户从IAM申请到的projectid,一般为32位字符串。
        :type projectid: str
        :param spec: 
        :type spec: :class:`huaweicloudsdkaom.v2.AppRulesSpec`
        """
        
        

        self._create_time = None
        self._enable = None
        self._event_name = None
        self._hostid = None
        self._id = None
        self._name = None
        self._projectid = None
        self._spec = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        self.enable = enable
        self.event_name = event_name
        if hostid is not None:
            self.hostid = hostid
        self.id = id
        self.name = name
        self.projectid = projectid
        self.spec = spec

    @property
    def create_time(self):
        """Gets the create_time of this AppRules.

        规则创建时间(创建时不传,修改时传查询返回的createTime)。

        :return: The create_time of this AppRules.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this AppRules.

        规则创建时间(创建时不传,修改时传查询返回的createTime)。

        :param create_time: The create_time of this AppRules.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def enable(self):
        """Gets the enable of this AppRules.

        true、false 规则是否启用。

        :return: The enable of this AppRules.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this AppRules.

        true、false 规则是否启用。

        :param enable: The enable of this AppRules.
        :type enable: bool
        """
        self._enable = enable

    @property
    def event_name(self):
        """Gets the event_name of this AppRules.

        aom_inventory_rules_event 规则事件名称,对于服务发现固定 为\"aom_inventory_rules_event\"。

        :return: The event_name of this AppRules.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this AppRules.

        aom_inventory_rules_event 规则事件名称,对于服务发现固定 为\"aom_inventory_rules_event\"。

        :param event_name: The event_name of this AppRules.
        :type event_name: str
        """
        self._event_name = event_name

    @property
    def hostid(self):
        """Gets the hostid of this AppRules.

        主机ID(暂不使用,传空即可)。

        :return: The hostid of this AppRules.
        :rtype: list[str]
        """
        return self._hostid

    @hostid.setter
    def hostid(self, hostid):
        """Sets the hostid of this AppRules.

        主机ID(暂不使用,传空即可)。

        :param hostid: The hostid of this AppRules.
        :type hostid: list[str]
        """
        self._hostid = hostid

    @property
    def id(self):
        """Gets the id of this AppRules.

        创建时填空，修改时填规则ID。

        :return: The id of this AppRules.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AppRules.

        创建时填空，修改时填规则ID。

        :param id: The id of this AppRules.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this AppRules.

        规则名称。 字符长度小于64位,以小写字母(a-z)开头,只能包含0-9/a-z/-,不能以-结尾。

        :return: The name of this AppRules.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AppRules.

        规则名称。 字符长度小于64位,以小写字母(a-z)开头,只能包含0-9/a-z/-,不能以-结尾。

        :param name: The name of this AppRules.
        :type name: str
        """
        self._name = name

    @property
    def projectid(self):
        """Gets the projectid of this AppRules.

        租户从IAM申请到的projectid,一般为32位字符串。

        :return: The projectid of this AppRules.
        :rtype: str
        """
        return self._projectid

    @projectid.setter
    def projectid(self, projectid):
        """Sets the projectid of this AppRules.

        租户从IAM申请到的projectid,一般为32位字符串。

        :param projectid: The projectid of this AppRules.
        :type projectid: str
        """
        self._projectid = projectid

    @property
    def spec(self):
        """Gets the spec of this AppRules.

        :return: The spec of this AppRules.
        :rtype: :class:`huaweicloudsdkaom.v2.AppRulesSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this AppRules.

        :param spec: The spec of this AppRules.
        :type spec: :class:`huaweicloudsdkaom.v2.AppRulesSpec`
        """
        self._spec = spec

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
        if not isinstance(other, AppRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
