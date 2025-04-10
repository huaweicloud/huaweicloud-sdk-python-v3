# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MultiViewModelCreateDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'item': 'ObjectReferenceParamDTO',
        'branch': 'VersionModelBranchCreateDTO',
        'check_out_time': 'str',
        'check_out_user_name': 'str',
        'create_time': 'str',
        'creator': 'str',
        'description': 'str',
        'id': 'str',
        'kiaguid': 'str',
        'last_update_time': 'str',
        'master': 'VersionModelMasterCreateDTO',
        'modifier': 'str',
        'name': 'str',
        'rdm_extension_type': 'str',
        'security_level': 'str',
        'tenant': 'ObjectReferenceParamDTO',
        'working_copy': 'bool'
    }

    attribute_map = {
        'item': 'item',
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
        'rdm_extension_type': 'rdmExtensionType',
        'security_level': 'securityLevel',
        'tenant': 'tenant',
        'working_copy': 'workingCopy'
    }

    def __init__(self, item=None, branch=None, check_out_time=None, check_out_user_name=None, create_time=None, creator=None, description=None, id=None, kiaguid=None, last_update_time=None, master=None, modifier=None, name=None, rdm_extension_type=None, security_level=None, tenant=None, working_copy=None):
        r"""MultiViewModelCreateDTO

        The model defined in huaweicloud sdk

        :param item: 
        :type item: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        :param branch: 
        :type branch: :class:`huaweicloudsdkidmeclassicapi.v1.VersionModelBranchCreateDTO`
        :param check_out_time: 检出时间。
        :type check_out_time: str
        :param check_out_user_name: 检出人。
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
        :type master: :class:`huaweicloudsdkidmeclassicapi.v1.VersionModelMasterCreateDTO`
        :param modifier: 修改人。
        :type modifier: str
        :param name: 中文名称。
        :type name: str
        :param rdm_extension_type: 扩展类型。
        :type rdm_extension_type: str
        :param security_level: 安全密级。 - INTERNAL：内部公开。 - SECRET：秘密。 - CONFIDENTIAL：机密。 - TOP_SECRET：绝密。
        :type security_level: str
        :param tenant: 
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        :param working_copy: 是否已检出。 - true：已检出。 - false：未检出。
        :type working_copy: bool
        """
        
        

        self._item = None
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
        self._rdm_extension_type = None
        self._security_level = None
        self._tenant = None
        self._working_copy = None
        self.discriminator = None

        if item is not None:
            self.item = item
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
        if rdm_extension_type is not None:
            self.rdm_extension_type = rdm_extension_type
        if security_level is not None:
            self.security_level = security_level
        if tenant is not None:
            self.tenant = tenant
        if working_copy is not None:
            self.working_copy = working_copy

    @property
    def item(self):
        r"""Gets the item of this MultiViewModelCreateDTO.

        :return: The item of this MultiViewModelCreateDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        """
        return self._item

    @item.setter
    def item(self, item):
        r"""Sets the item of this MultiViewModelCreateDTO.

        :param item: The item of this MultiViewModelCreateDTO.
        :type item: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        """
        self._item = item

    @property
    def branch(self):
        r"""Gets the branch of this MultiViewModelCreateDTO.

        :return: The branch of this MultiViewModelCreateDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.VersionModelBranchCreateDTO`
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        r"""Sets the branch of this MultiViewModelCreateDTO.

        :param branch: The branch of this MultiViewModelCreateDTO.
        :type branch: :class:`huaweicloudsdkidmeclassicapi.v1.VersionModelBranchCreateDTO`
        """
        self._branch = branch

    @property
    def check_out_time(self):
        r"""Gets the check_out_time of this MultiViewModelCreateDTO.

        检出时间。

        :return: The check_out_time of this MultiViewModelCreateDTO.
        :rtype: str
        """
        return self._check_out_time

    @check_out_time.setter
    def check_out_time(self, check_out_time):
        r"""Sets the check_out_time of this MultiViewModelCreateDTO.

        检出时间。

        :param check_out_time: The check_out_time of this MultiViewModelCreateDTO.
        :type check_out_time: str
        """
        self._check_out_time = check_out_time

    @property
    def check_out_user_name(self):
        r"""Gets the check_out_user_name of this MultiViewModelCreateDTO.

        检出人。

        :return: The check_out_user_name of this MultiViewModelCreateDTO.
        :rtype: str
        """
        return self._check_out_user_name

    @check_out_user_name.setter
    def check_out_user_name(self, check_out_user_name):
        r"""Sets the check_out_user_name of this MultiViewModelCreateDTO.

        检出人。

        :param check_out_user_name: The check_out_user_name of this MultiViewModelCreateDTO.
        :type check_out_user_name: str
        """
        self._check_out_user_name = check_out_user_name

    @property
    def create_time(self):
        r"""Gets the create_time of this MultiViewModelCreateDTO.

        创建时间。

        :return: The create_time of this MultiViewModelCreateDTO.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this MultiViewModelCreateDTO.

        创建时间。

        :param create_time: The create_time of this MultiViewModelCreateDTO.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def creator(self):
        r"""Gets the creator of this MultiViewModelCreateDTO.

        创建者。

        :return: The creator of this MultiViewModelCreateDTO.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this MultiViewModelCreateDTO.

        创建者。

        :param creator: The creator of this MultiViewModelCreateDTO.
        :type creator: str
        """
        self._creator = creator

    @property
    def description(self):
        r"""Gets the description of this MultiViewModelCreateDTO.

        描述信息。

        :return: The description of this MultiViewModelCreateDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this MultiViewModelCreateDTO.

        描述信息。

        :param description: The description of this MultiViewModelCreateDTO.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        r"""Gets the id of this MultiViewModelCreateDTO.

        唯一标识。

        :return: The id of this MultiViewModelCreateDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this MultiViewModelCreateDTO.

        唯一标识。

        :param id: The id of this MultiViewModelCreateDTO.
        :type id: str
        """
        self._id = id

    @property
    def kiaguid(self):
        r"""Gets the kiaguid of this MultiViewModelCreateDTO.

        关键信息资产ID。

        :return: The kiaguid of this MultiViewModelCreateDTO.
        :rtype: str
        """
        return self._kiaguid

    @kiaguid.setter
    def kiaguid(self, kiaguid):
        r"""Sets the kiaguid of this MultiViewModelCreateDTO.

        关键信息资产ID。

        :param kiaguid: The kiaguid of this MultiViewModelCreateDTO.
        :type kiaguid: str
        """
        self._kiaguid = kiaguid

    @property
    def last_update_time(self):
        r"""Gets the last_update_time of this MultiViewModelCreateDTO.

        最后更新时间。

        :return: The last_update_time of this MultiViewModelCreateDTO.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        r"""Sets the last_update_time of this MultiViewModelCreateDTO.

        最后更新时间。

        :param last_update_time: The last_update_time of this MultiViewModelCreateDTO.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def master(self):
        r"""Gets the master of this MultiViewModelCreateDTO.

        :return: The master of this MultiViewModelCreateDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.VersionModelMasterCreateDTO`
        """
        return self._master

    @master.setter
    def master(self, master):
        r"""Sets the master of this MultiViewModelCreateDTO.

        :param master: The master of this MultiViewModelCreateDTO.
        :type master: :class:`huaweicloudsdkidmeclassicapi.v1.VersionModelMasterCreateDTO`
        """
        self._master = master

    @property
    def modifier(self):
        r"""Gets the modifier of this MultiViewModelCreateDTO.

        修改人。

        :return: The modifier of this MultiViewModelCreateDTO.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        r"""Sets the modifier of this MultiViewModelCreateDTO.

        修改人。

        :param modifier: The modifier of this MultiViewModelCreateDTO.
        :type modifier: str
        """
        self._modifier = modifier

    @property
    def name(self):
        r"""Gets the name of this MultiViewModelCreateDTO.

        中文名称。

        :return: The name of this MultiViewModelCreateDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this MultiViewModelCreateDTO.

        中文名称。

        :param name: The name of this MultiViewModelCreateDTO.
        :type name: str
        """
        self._name = name

    @property
    def rdm_extension_type(self):
        r"""Gets the rdm_extension_type of this MultiViewModelCreateDTO.

        扩展类型。

        :return: The rdm_extension_type of this MultiViewModelCreateDTO.
        :rtype: str
        """
        return self._rdm_extension_type

    @rdm_extension_type.setter
    def rdm_extension_type(self, rdm_extension_type):
        r"""Sets the rdm_extension_type of this MultiViewModelCreateDTO.

        扩展类型。

        :param rdm_extension_type: The rdm_extension_type of this MultiViewModelCreateDTO.
        :type rdm_extension_type: str
        """
        self._rdm_extension_type = rdm_extension_type

    @property
    def security_level(self):
        r"""Gets the security_level of this MultiViewModelCreateDTO.

        安全密级。 - INTERNAL：内部公开。 - SECRET：秘密。 - CONFIDENTIAL：机密。 - TOP_SECRET：绝密。

        :return: The security_level of this MultiViewModelCreateDTO.
        :rtype: str
        """
        return self._security_level

    @security_level.setter
    def security_level(self, security_level):
        r"""Sets the security_level of this MultiViewModelCreateDTO.

        安全密级。 - INTERNAL：内部公开。 - SECRET：秘密。 - CONFIDENTIAL：机密。 - TOP_SECRET：绝密。

        :param security_level: The security_level of this MultiViewModelCreateDTO.
        :type security_level: str
        """
        self._security_level = security_level

    @property
    def tenant(self):
        r"""Gets the tenant of this MultiViewModelCreateDTO.

        :return: The tenant of this MultiViewModelCreateDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        r"""Sets the tenant of this MultiViewModelCreateDTO.

        :param tenant: The tenant of this MultiViewModelCreateDTO.
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        """
        self._tenant = tenant

    @property
    def working_copy(self):
        r"""Gets the working_copy of this MultiViewModelCreateDTO.

        是否已检出。 - true：已检出。 - false：未检出。

        :return: The working_copy of this MultiViewModelCreateDTO.
        :rtype: bool
        """
        return self._working_copy

    @working_copy.setter
    def working_copy(self, working_copy):
        r"""Sets the working_copy of this MultiViewModelCreateDTO.

        是否已检出。 - true：已检出。 - false：未检出。

        :param working_copy: The working_copy of this MultiViewModelCreateDTO.
        :type working_copy: bool
        """
        self._working_copy = working_copy

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
        if not isinstance(other, MultiViewModelCreateDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
