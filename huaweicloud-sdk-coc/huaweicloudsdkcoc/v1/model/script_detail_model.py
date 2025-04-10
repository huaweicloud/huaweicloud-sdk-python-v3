# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScriptDetailModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'script_uuid': 'str',
        'name': 'str',
        'version': 'str',
        'description': 'str',
        'type': 'str',
        'content': 'str',
        'script_params': 'list[ScriptParamDefine]',
        'status': 'str',
        'gmt_created': 'int',
        'gmt_modified': 'int',
        'creator': 'str',
        'creator_id': 'str',
        'operator': 'str',
        'properties': 'ScriptPropertiesModel',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'script_uuid': 'script_uuid',
        'name': 'name',
        'version': 'version',
        'description': 'description',
        'type': 'type',
        'content': 'content',
        'script_params': 'script_params',
        'status': 'status',
        'gmt_created': 'gmt_created',
        'gmt_modified': 'gmt_modified',
        'creator': 'creator',
        'creator_id': 'creator_id',
        'operator': 'operator',
        'properties': 'properties',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, script_uuid=None, name=None, version=None, description=None, type=None, content=None, script_params=None, status=None, gmt_created=None, gmt_modified=None, creator=None, creator_id=None, operator=None, properties=None, enterprise_project_id=None):
        r"""ScriptDetailModel

        The model defined in huaweicloud sdk

        :param script_uuid: 脚本uuid
        :type script_uuid: str
        :param name: 脚本名称
        :type name: str
        :param version: 脚本版本号 约束条件  后期废除，不建议使用
        :type version: str
        :param description: 脚本描述
        :type description: str
        :param type: 脚本类型 SHELL:shell脚本， PYTHON:Python脚本， BAT:Bat脚本，
        :type type: str
        :param content: 脚本内容
        :type content: str
        :param script_params: 脚本入参
        :type script_params: list[:class:`huaweicloudsdkcoc.v1.ScriptParamDefine`]
        :param status: 脚本状态 PENDING_APPROVE:待审批 APPROVED：正常（审批通过） REJECTED：驳回（审批人，驳回该脚本）
        :type status: str
        :param gmt_created: 创建时间
        :type gmt_created: int
        :param gmt_modified: 修改时间
        :type gmt_modified: int
        :param creator: 创建人
        :type creator: str
        :param creator_id: 创建人Id
        :type creator_id: str
        :param operator: 修改人
        :type operator: str
        :param properties: 
        :type properties: :class:`huaweicloudsdkcoc.v1.ScriptPropertiesModel`
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        """
        
        

        self._script_uuid = None
        self._name = None
        self._version = None
        self._description = None
        self._type = None
        self._content = None
        self._script_params = None
        self._status = None
        self._gmt_created = None
        self._gmt_modified = None
        self._creator = None
        self._creator_id = None
        self._operator = None
        self._properties = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.script_uuid = script_uuid
        self.name = name
        if version is not None:
            self.version = version
        self.description = description
        self.type = type
        self.content = content
        if script_params is not None:
            self.script_params = script_params
        self.status = status
        self.gmt_created = gmt_created
        if gmt_modified is not None:
            self.gmt_modified = gmt_modified
        self.creator = creator
        self.creator_id = creator_id
        if operator is not None:
            self.operator = operator
        self.properties = properties
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def script_uuid(self):
        r"""Gets the script_uuid of this ScriptDetailModel.

        脚本uuid

        :return: The script_uuid of this ScriptDetailModel.
        :rtype: str
        """
        return self._script_uuid

    @script_uuid.setter
    def script_uuid(self, script_uuid):
        r"""Sets the script_uuid of this ScriptDetailModel.

        脚本uuid

        :param script_uuid: The script_uuid of this ScriptDetailModel.
        :type script_uuid: str
        """
        self._script_uuid = script_uuid

    @property
    def name(self):
        r"""Gets the name of this ScriptDetailModel.

        脚本名称

        :return: The name of this ScriptDetailModel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ScriptDetailModel.

        脚本名称

        :param name: The name of this ScriptDetailModel.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        r"""Gets the version of this ScriptDetailModel.

        脚本版本号 约束条件  后期废除，不建议使用

        :return: The version of this ScriptDetailModel.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ScriptDetailModel.

        脚本版本号 约束条件  后期废除，不建议使用

        :param version: The version of this ScriptDetailModel.
        :type version: str
        """
        self._version = version

    @property
    def description(self):
        r"""Gets the description of this ScriptDetailModel.

        脚本描述

        :return: The description of this ScriptDetailModel.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ScriptDetailModel.

        脚本描述

        :param description: The description of this ScriptDetailModel.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        r"""Gets the type of this ScriptDetailModel.

        脚本类型 SHELL:shell脚本， PYTHON:Python脚本， BAT:Bat脚本，

        :return: The type of this ScriptDetailModel.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ScriptDetailModel.

        脚本类型 SHELL:shell脚本， PYTHON:Python脚本， BAT:Bat脚本，

        :param type: The type of this ScriptDetailModel.
        :type type: str
        """
        self._type = type

    @property
    def content(self):
        r"""Gets the content of this ScriptDetailModel.

        脚本内容

        :return: The content of this ScriptDetailModel.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this ScriptDetailModel.

        脚本内容

        :param content: The content of this ScriptDetailModel.
        :type content: str
        """
        self._content = content

    @property
    def script_params(self):
        r"""Gets the script_params of this ScriptDetailModel.

        脚本入参

        :return: The script_params of this ScriptDetailModel.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.ScriptParamDefine`]
        """
        return self._script_params

    @script_params.setter
    def script_params(self, script_params):
        r"""Sets the script_params of this ScriptDetailModel.

        脚本入参

        :param script_params: The script_params of this ScriptDetailModel.
        :type script_params: list[:class:`huaweicloudsdkcoc.v1.ScriptParamDefine`]
        """
        self._script_params = script_params

    @property
    def status(self):
        r"""Gets the status of this ScriptDetailModel.

        脚本状态 PENDING_APPROVE:待审批 APPROVED：正常（审批通过） REJECTED：驳回（审批人，驳回该脚本）

        :return: The status of this ScriptDetailModel.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ScriptDetailModel.

        脚本状态 PENDING_APPROVE:待审批 APPROVED：正常（审批通过） REJECTED：驳回（审批人，驳回该脚本）

        :param status: The status of this ScriptDetailModel.
        :type status: str
        """
        self._status = status

    @property
    def gmt_created(self):
        r"""Gets the gmt_created of this ScriptDetailModel.

        创建时间

        :return: The gmt_created of this ScriptDetailModel.
        :rtype: int
        """
        return self._gmt_created

    @gmt_created.setter
    def gmt_created(self, gmt_created):
        r"""Sets the gmt_created of this ScriptDetailModel.

        创建时间

        :param gmt_created: The gmt_created of this ScriptDetailModel.
        :type gmt_created: int
        """
        self._gmt_created = gmt_created

    @property
    def gmt_modified(self):
        r"""Gets the gmt_modified of this ScriptDetailModel.

        修改时间

        :return: The gmt_modified of this ScriptDetailModel.
        :rtype: int
        """
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, gmt_modified):
        r"""Sets the gmt_modified of this ScriptDetailModel.

        修改时间

        :param gmt_modified: The gmt_modified of this ScriptDetailModel.
        :type gmt_modified: int
        """
        self._gmt_modified = gmt_modified

    @property
    def creator(self):
        r"""Gets the creator of this ScriptDetailModel.

        创建人

        :return: The creator of this ScriptDetailModel.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this ScriptDetailModel.

        创建人

        :param creator: The creator of this ScriptDetailModel.
        :type creator: str
        """
        self._creator = creator

    @property
    def creator_id(self):
        r"""Gets the creator_id of this ScriptDetailModel.

        创建人Id

        :return: The creator_id of this ScriptDetailModel.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        r"""Sets the creator_id of this ScriptDetailModel.

        创建人Id

        :param creator_id: The creator_id of this ScriptDetailModel.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def operator(self):
        r"""Gets the operator of this ScriptDetailModel.

        修改人

        :return: The operator of this ScriptDetailModel.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this ScriptDetailModel.

        修改人

        :param operator: The operator of this ScriptDetailModel.
        :type operator: str
        """
        self._operator = operator

    @property
    def properties(self):
        r"""Gets the properties of this ScriptDetailModel.

        :return: The properties of this ScriptDetailModel.
        :rtype: :class:`huaweicloudsdkcoc.v1.ScriptPropertiesModel`
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this ScriptDetailModel.

        :param properties: The properties of this ScriptDetailModel.
        :type properties: :class:`huaweicloudsdkcoc.v1.ScriptPropertiesModel`
        """
        self._properties = properties

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ScriptDetailModel.

        企业项目id

        :return: The enterprise_project_id of this ScriptDetailModel.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ScriptDetailModel.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ScriptDetailModel.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ScriptDetailModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
