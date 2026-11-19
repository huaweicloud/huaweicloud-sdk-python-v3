# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DelegatedAccountResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parent_id': 'str',
        'parent_name': 'str',
        'id': 'str',
        'urn': 'str',
        'name': 'str',
        'org_type': 'str'
    }

    attribute_map = {
        'parent_id': 'parent_id',
        'parent_name': 'parent_name',
        'id': 'id',
        'urn': 'urn',
        'name': 'name',
        'org_type': 'org_type'
    }

    def __init__(self, parent_id=None, parent_name=None, id=None, urn=None, name=None, org_type=None):
        r"""DelegatedAccountResponseInfo

        The model defined in huaweicloud sdk

        :param parent_id: **参数解释** 父节点的ID **取值范围** 字符长度1-64位 
        :type parent_id: str
        :param parent_name: **参数解释** 父节点名称 **取值范围** 字符长度0-64位 
        :type parent_name: str
        :param id: **参数解释** 账号ID **取值范围** 字符长度1-64位 
        :type id: str
        :param urn: **参数解释** 账号的统一资源名称 **取值范围** 字符长度0-2048位 
        :type urn: str
        :param name: **参数解释** 账号名称 **取值范围** 字符长度1-64位 
        :type name: str
        :param org_type: **参数解释** 节点类型 **取值范围** - unit：组织 - account：账号 - project：项目 
        :type org_type: str
        """
        
        

        self._parent_id = None
        self._parent_name = None
        self._id = None
        self._urn = None
        self._name = None
        self._org_type = None
        self.discriminator = None

        if parent_id is not None:
            self.parent_id = parent_id
        if parent_name is not None:
            self.parent_name = parent_name
        if id is not None:
            self.id = id
        if urn is not None:
            self.urn = urn
        if name is not None:
            self.name = name
        if org_type is not None:
            self.org_type = org_type

    @property
    def parent_id(self):
        r"""Gets the parent_id of this DelegatedAccountResponseInfo.

        **参数解释** 父节点的ID **取值范围** 字符长度1-64位 

        :return: The parent_id of this DelegatedAccountResponseInfo.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this DelegatedAccountResponseInfo.

        **参数解释** 父节点的ID **取值范围** 字符长度1-64位 

        :param parent_id: The parent_id of this DelegatedAccountResponseInfo.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def parent_name(self):
        r"""Gets the parent_name of this DelegatedAccountResponseInfo.

        **参数解释** 父节点名称 **取值范围** 字符长度0-64位 

        :return: The parent_name of this DelegatedAccountResponseInfo.
        :rtype: str
        """
        return self._parent_name

    @parent_name.setter
    def parent_name(self, parent_name):
        r"""Sets the parent_name of this DelegatedAccountResponseInfo.

        **参数解释** 父节点名称 **取值范围** 字符长度0-64位 

        :param parent_name: The parent_name of this DelegatedAccountResponseInfo.
        :type parent_name: str
        """
        self._parent_name = parent_name

    @property
    def id(self):
        r"""Gets the id of this DelegatedAccountResponseInfo.

        **参数解释** 账号ID **取值范围** 字符长度1-64位 

        :return: The id of this DelegatedAccountResponseInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DelegatedAccountResponseInfo.

        **参数解释** 账号ID **取值范围** 字符长度1-64位 

        :param id: The id of this DelegatedAccountResponseInfo.
        :type id: str
        """
        self._id = id

    @property
    def urn(self):
        r"""Gets the urn of this DelegatedAccountResponseInfo.

        **参数解释** 账号的统一资源名称 **取值范围** 字符长度0-2048位 

        :return: The urn of this DelegatedAccountResponseInfo.
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        r"""Sets the urn of this DelegatedAccountResponseInfo.

        **参数解释** 账号的统一资源名称 **取值范围** 字符长度0-2048位 

        :param urn: The urn of this DelegatedAccountResponseInfo.
        :type urn: str
        """
        self._urn = urn

    @property
    def name(self):
        r"""Gets the name of this DelegatedAccountResponseInfo.

        **参数解释** 账号名称 **取值范围** 字符长度1-64位 

        :return: The name of this DelegatedAccountResponseInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DelegatedAccountResponseInfo.

        **参数解释** 账号名称 **取值范围** 字符长度1-64位 

        :param name: The name of this DelegatedAccountResponseInfo.
        :type name: str
        """
        self._name = name

    @property
    def org_type(self):
        r"""Gets the org_type of this DelegatedAccountResponseInfo.

        **参数解释** 节点类型 **取值范围** - unit：组织 - account：账号 - project：项目 

        :return: The org_type of this DelegatedAccountResponseInfo.
        :rtype: str
        """
        return self._org_type

    @org_type.setter
    def org_type(self, org_type):
        r"""Sets the org_type of this DelegatedAccountResponseInfo.

        **参数解释** 节点类型 **取值范围** - unit：组织 - account：账号 - project：项目 

        :param org_type: The org_type of this DelegatedAccountResponseInfo.
        :type org_type: str
        """
        self._org_type = org_type

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DelegatedAccountResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
