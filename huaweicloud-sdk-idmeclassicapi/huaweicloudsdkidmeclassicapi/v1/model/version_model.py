# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VersionModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'branch': 'VersionModelBranch',
        'check_out_time': 'str',
        'check_out_user_name': 'str',
        'create_time': 'str',
        'creator': 'str',
        'description': 'str',
        'id': 'str',
        'kiaguid': 'str',
        'last_update_time': 'str',
        'master': 'VersionModelMaster',
        'modifier': 'str',
        'name': 'str',
        'need_set_null_attrs': 'list[str]',
        'rdm_extension_type': 'str',
        'security_level': 'str'
    }

    attribute_map = {
        'branch': 'branch',
        'check_out_time': 'checkOutTime',
        'check_out_user_name': 'checkOutUserName',
        'create_time': 'createTime',
        'creator': 'creator',
        'description': 'description',
        'id': 'id',
        'kiaguid': 'kiaguid',
        'last_update_time': 'lastUpdateTime',
        'master': 'master',
        'modifier': 'modifier',
        'name': 'name',
        'need_set_null_attrs': 'needSetNullAttrs',
        'rdm_extension_type': 'rdmExtensionType',
        'security_level': 'securityLevel'
    }

    def __init__(self, branch=None, check_out_time=None, check_out_user_name=None, create_time=None, creator=None, description=None, id=None, kiaguid=None, last_update_time=None, master=None, modifier=None, name=None, need_set_null_attrs=None, rdm_extension_type=None, security_level=None):
        """VersionModel

        The model defined in huaweicloud sdk

        :param branch: 
        :type branch: :class:`huaweicloudsdkidmeclassicapi.v1.VersionModelBranch`
        :param check_out_time: 检出时间。
        :type check_out_time: str
        :param check_out_user_name: 检出用户名称。
        :type check_out_user_name: str
        :param create_time: 创建时间。
        :type create_time: str
        :param creator: 创建者。
        :type creator: str
        :param description: 描述信息。
        :type description: str
        :param id: 唯一标识。
        :type id: str
        :param kiaguid: 关键信息资产ID。
        :type kiaguid: str
        :param last_update_time: 最后更新时间。
        :type last_update_time: str
        :param master: 
        :type master: :class:`huaweicloudsdkidmeclassicapi.v1.VersionModelMaster`
        :param modifier: 更新者。
        :type modifier: str
        :param name: 中文名称。
        :type name: str
        :param need_set_null_attrs: 设置NULL值的属性名称。
        :type need_set_null_attrs: list[str]
        :param rdm_extension_type: 扩展类型。
        :type rdm_extension_type: str
        :param security_level: 安全密级。 - INTERNAL：内部公开。 - SECRET：秘密。 - CONFIDENTIAL：机密。 - TOP_SECRET：绝密。
        :type security_level: str
        """
        
        

        self._branch = None
        self._check_out_time = None
        self._check_out_user_name = None
        self._create_time = None
        self._creator = None
        self._description = None
        self._id = None
        self._kiaguid = None
        self._last_update_time = None
        self._master = None
        self._modifier = None
        self._name = None
        self._need_set_null_attrs = None
        self._rdm_extension_type = None
        self._security_level = None
        self.discriminator = None

        if branch is not None:
            self.branch = branch
        if check_out_time is not None:
            self.check_out_time = check_out_time
        if check_out_user_name is not None:
            self.check_out_user_name = check_out_user_name
        if create_time is not None:
            self.create_time = create_time
        if creator is not None:
            self.creator = creator
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if kiaguid is not None:
            self.kiaguid = kiaguid
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if master is not None:
            self.master = master
        if modifier is not None:
            self.modifier = modifier
        if name is not None:
            self.name = name
        if need_set_null_attrs is not None:
            self.need_set_null_attrs = need_set_null_attrs
        if rdm_extension_type is not None:
            self.rdm_extension_type = rdm_extension_type
        if security_level is not None:
            self.security_level = security_level

    @property
    def branch(self):
        """Gets the branch of this VersionModel.

        :return: The branch of this VersionModel.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.VersionModelBranch`
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this VersionModel.

        :param branch: The branch of this VersionModel.
        :type branch: :class:`huaweicloudsdkidmeclassicapi.v1.VersionModelBranch`
        """
        self._branch = branch

    @property
    def check_out_time(self):
        """Gets the check_out_time of this VersionModel.

        检出时间。

        :return: The check_out_time of this VersionModel.
        :rtype: str
        """
        return self._check_out_time

    @check_out_time.setter
    def check_out_time(self, check_out_time):
        """Sets the check_out_time of this VersionModel.

        检出时间。

        :param check_out_time: The check_out_time of this VersionModel.
        :type check_out_time: str
        """
        self._check_out_time = check_out_time

    @property
    def check_out_user_name(self):
        """Gets the check_out_user_name of this VersionModel.

        检出用户名称。

        :return: The check_out_user_name of this VersionModel.
        :rtype: str
        """
        return self._check_out_user_name

    @check_out_user_name.setter
    def check_out_user_name(self, check_out_user_name):
        """Sets the check_out_user_name of this VersionModel.

        检出用户名称。

        :param check_out_user_name: The check_out_user_name of this VersionModel.
        :type check_out_user_name: str
        """
        self._check_out_user_name = check_out_user_name

    @property
    def create_time(self):
        """Gets the create_time of this VersionModel.

        创建时间。

        :return: The create_time of this VersionModel.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this VersionModel.

        创建时间。

        :param create_time: The create_time of this VersionModel.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def creator(self):
        """Gets the creator of this VersionModel.

        创建者。

        :return: The creator of this VersionModel.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this VersionModel.

        创建者。

        :param creator: The creator of this VersionModel.
        :type creator: str
        """
        self._creator = creator

    @property
    def description(self):
        """Gets the description of this VersionModel.

        描述信息。

        :return: The description of this VersionModel.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VersionModel.

        描述信息。

        :param description: The description of this VersionModel.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        """Gets the id of this VersionModel.

        唯一标识。

        :return: The id of this VersionModel.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VersionModel.

        唯一标识。

        :param id: The id of this VersionModel.
        :type id: str
        """
        self._id = id

    @property
    def kiaguid(self):
        """Gets the kiaguid of this VersionModel.

        关键信息资产ID。

        :return: The kiaguid of this VersionModel.
        :rtype: str
        """
        return self._kiaguid

    @kiaguid.setter
    def kiaguid(self, kiaguid):
        """Sets the kiaguid of this VersionModel.

        关键信息资产ID。

        :param kiaguid: The kiaguid of this VersionModel.
        :type kiaguid: str
        """
        self._kiaguid = kiaguid

    @property
    def last_update_time(self):
        """Gets the last_update_time of this VersionModel.

        最后更新时间。

        :return: The last_update_time of this VersionModel.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """Sets the last_update_time of this VersionModel.

        最后更新时间。

        :param last_update_time: The last_update_time of this VersionModel.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def master(self):
        """Gets the master of this VersionModel.

        :return: The master of this VersionModel.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.VersionModelMaster`
        """
        return self._master

    @master.setter
    def master(self, master):
        """Sets the master of this VersionModel.

        :param master: The master of this VersionModel.
        :type master: :class:`huaweicloudsdkidmeclassicapi.v1.VersionModelMaster`
        """
        self._master = master

    @property
    def modifier(self):
        """Gets the modifier of this VersionModel.

        更新者。

        :return: The modifier of this VersionModel.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        """Sets the modifier of this VersionModel.

        更新者。

        :param modifier: The modifier of this VersionModel.
        :type modifier: str
        """
        self._modifier = modifier

    @property
    def name(self):
        """Gets the name of this VersionModel.

        中文名称。

        :return: The name of this VersionModel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VersionModel.

        中文名称。

        :param name: The name of this VersionModel.
        :type name: str
        """
        self._name = name

    @property
    def need_set_null_attrs(self):
        """Gets the need_set_null_attrs of this VersionModel.

        设置NULL值的属性名称。

        :return: The need_set_null_attrs of this VersionModel.
        :rtype: list[str]
        """
        return self._need_set_null_attrs

    @need_set_null_attrs.setter
    def need_set_null_attrs(self, need_set_null_attrs):
        """Sets the need_set_null_attrs of this VersionModel.

        设置NULL值的属性名称。

        :param need_set_null_attrs: The need_set_null_attrs of this VersionModel.
        :type need_set_null_attrs: list[str]
        """
        self._need_set_null_attrs = need_set_null_attrs

    @property
    def rdm_extension_type(self):
        """Gets the rdm_extension_type of this VersionModel.

        扩展类型。

        :return: The rdm_extension_type of this VersionModel.
        :rtype: str
        """
        return self._rdm_extension_type

    @rdm_extension_type.setter
    def rdm_extension_type(self, rdm_extension_type):
        """Sets the rdm_extension_type of this VersionModel.

        扩展类型。

        :param rdm_extension_type: The rdm_extension_type of this VersionModel.
        :type rdm_extension_type: str
        """
        self._rdm_extension_type = rdm_extension_type

    @property
    def security_level(self):
        """Gets the security_level of this VersionModel.

        安全密级。 - INTERNAL：内部公开。 - SECRET：秘密。 - CONFIDENTIAL：机密。 - TOP_SECRET：绝密。

        :return: The security_level of this VersionModel.
        :rtype: str
        """
        return self._security_level

    @security_level.setter
    def security_level(self, security_level):
        """Sets the security_level of this VersionModel.

        安全密级。 - INTERNAL：内部公开。 - SECRET：秘密。 - CONFIDENTIAL：机密。 - TOP_SECRET：绝密。

        :param security_level: The security_level of this VersionModel.
        :type security_level: str
        """
        self._security_level = security_level

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
        if not isinstance(other, VersionModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
