# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtDataSourceReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_source_id': 'str',
        'type': 'str',
        'data_source_name': 'str',
        'user_name': 'str',
        'user_pwd': 'str',
        'description': 'str',
        'reboot': 'bool',
        'connect_info': 'str'
    }

    attribute_map = {
        'data_source_id': 'data_source_id',
        'type': 'type',
        'data_source_name': 'data_source_name',
        'user_name': 'user_name',
        'user_pwd': 'user_pwd',
        'description': 'description',
        'reboot': 'reboot',
        'connect_info': 'connect_info'
    }

    def __init__(self, data_source_id=None, type=None, data_source_name=None, user_name=None, user_pwd=None, description=None, reboot=None, connect_info=None):
        r"""ExtDataSourceReq

        The model defined in huaweicloud sdk

        :param data_source_id: **参数解释**： 外部数据源ID。当数据源为MRS时为必选字段。 **取值范围**： 不涉及。
        :type data_source_id: str
        :param type: **参数解释**： 数据源类型。 **取值范围**： 不涉及。
        :type type: str
        :param data_source_name: **参数解释**： 外部数据源名称。 **取值范围**： 仅可包含大小写字母、数字、下划线，1到64个字符。
        :type data_source_name: str
        :param user_name: **参数解释**： 用户名。数据源类型为OBS时，传对应OBS委托名称。 **取值范围**： 仅可包含大小写字母、数字、下划线，3到20个字符。
        :type user_name: str
        :param user_pwd: **参数解释**： 密码。当数据源为MRS时为必选字段。 **取值范围**： 不涉及。
        :type user_pwd: str
        :param description: **参数解释**： 描述。 **取值范围**： 除!&lt;&gt;&#39;&#x3D;&amp;等特殊字符外的字符。长度256个字符以内。
        :type description: str
        :param reboot: **参数解释**： 是否重启集群。 **取值范围**： 不涉及。
        :type reboot: bool
        :param connect_info: **参数解释**： 连接的数据库。当数据源为OBS时为必选字段。 **取值范围**： 不涉及。
        :type connect_info: str
        """
        
        

        self._data_source_id = None
        self._type = None
        self._data_source_name = None
        self._user_name = None
        self._user_pwd = None
        self._description = None
        self._reboot = None
        self._connect_info = None
        self.discriminator = None

        if data_source_id is not None:
            self.data_source_id = data_source_id
        self.type = type
        self.data_source_name = data_source_name
        self.user_name = user_name
        if user_pwd is not None:
            self.user_pwd = user_pwd
        if description is not None:
            self.description = description
        if reboot is not None:
            self.reboot = reboot
        if connect_info is not None:
            self.connect_info = connect_info

    @property
    def data_source_id(self):
        r"""Gets the data_source_id of this ExtDataSourceReq.

        **参数解释**： 外部数据源ID。当数据源为MRS时为必选字段。 **取值范围**： 不涉及。

        :return: The data_source_id of this ExtDataSourceReq.
        :rtype: str
        """
        return self._data_source_id

    @data_source_id.setter
    def data_source_id(self, data_source_id):
        r"""Sets the data_source_id of this ExtDataSourceReq.

        **参数解释**： 外部数据源ID。当数据源为MRS时为必选字段。 **取值范围**： 不涉及。

        :param data_source_id: The data_source_id of this ExtDataSourceReq.
        :type data_source_id: str
        """
        self._data_source_id = data_source_id

    @property
    def type(self):
        r"""Gets the type of this ExtDataSourceReq.

        **参数解释**： 数据源类型。 **取值范围**： 不涉及。

        :return: The type of this ExtDataSourceReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ExtDataSourceReq.

        **参数解释**： 数据源类型。 **取值范围**： 不涉及。

        :param type: The type of this ExtDataSourceReq.
        :type type: str
        """
        self._type = type

    @property
    def data_source_name(self):
        r"""Gets the data_source_name of this ExtDataSourceReq.

        **参数解释**： 外部数据源名称。 **取值范围**： 仅可包含大小写字母、数字、下划线，1到64个字符。

        :return: The data_source_name of this ExtDataSourceReq.
        :rtype: str
        """
        return self._data_source_name

    @data_source_name.setter
    def data_source_name(self, data_source_name):
        r"""Sets the data_source_name of this ExtDataSourceReq.

        **参数解释**： 外部数据源名称。 **取值范围**： 仅可包含大小写字母、数字、下划线，1到64个字符。

        :param data_source_name: The data_source_name of this ExtDataSourceReq.
        :type data_source_name: str
        """
        self._data_source_name = data_source_name

    @property
    def user_name(self):
        r"""Gets the user_name of this ExtDataSourceReq.

        **参数解释**： 用户名。数据源类型为OBS时，传对应OBS委托名称。 **取值范围**： 仅可包含大小写字母、数字、下划线，3到20个字符。

        :return: The user_name of this ExtDataSourceReq.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ExtDataSourceReq.

        **参数解释**： 用户名。数据源类型为OBS时，传对应OBS委托名称。 **取值范围**： 仅可包含大小写字母、数字、下划线，3到20个字符。

        :param user_name: The user_name of this ExtDataSourceReq.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_pwd(self):
        r"""Gets the user_pwd of this ExtDataSourceReq.

        **参数解释**： 密码。当数据源为MRS时为必选字段。 **取值范围**： 不涉及。

        :return: The user_pwd of this ExtDataSourceReq.
        :rtype: str
        """
        return self._user_pwd

    @user_pwd.setter
    def user_pwd(self, user_pwd):
        r"""Sets the user_pwd of this ExtDataSourceReq.

        **参数解释**： 密码。当数据源为MRS时为必选字段。 **取值范围**： 不涉及。

        :param user_pwd: The user_pwd of this ExtDataSourceReq.
        :type user_pwd: str
        """
        self._user_pwd = user_pwd

    @property
    def description(self):
        r"""Gets the description of this ExtDataSourceReq.

        **参数解释**： 描述。 **取值范围**： 除!<>'=&等特殊字符外的字符。长度256个字符以内。

        :return: The description of this ExtDataSourceReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ExtDataSourceReq.

        **参数解释**： 描述。 **取值范围**： 除!<>'=&等特殊字符外的字符。长度256个字符以内。

        :param description: The description of this ExtDataSourceReq.
        :type description: str
        """
        self._description = description

    @property
    def reboot(self):
        r"""Gets the reboot of this ExtDataSourceReq.

        **参数解释**： 是否重启集群。 **取值范围**： 不涉及。

        :return: The reboot of this ExtDataSourceReq.
        :rtype: bool
        """
        return self._reboot

    @reboot.setter
    def reboot(self, reboot):
        r"""Sets the reboot of this ExtDataSourceReq.

        **参数解释**： 是否重启集群。 **取值范围**： 不涉及。

        :param reboot: The reboot of this ExtDataSourceReq.
        :type reboot: bool
        """
        self._reboot = reboot

    @property
    def connect_info(self):
        r"""Gets the connect_info of this ExtDataSourceReq.

        **参数解释**： 连接的数据库。当数据源为OBS时为必选字段。 **取值范围**： 不涉及。

        :return: The connect_info of this ExtDataSourceReq.
        :rtype: str
        """
        return self._connect_info

    @connect_info.setter
    def connect_info(self, connect_info):
        r"""Sets the connect_info of this ExtDataSourceReq.

        **参数解释**： 连接的数据库。当数据源为OBS时为必选字段。 **取值范围**： 不涉及。

        :param connect_info: The connect_info of this ExtDataSourceReq.
        :type connect_info: str
        """
        self._connect_info = connect_info

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
        if not isinstance(other, ExtDataSourceReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
