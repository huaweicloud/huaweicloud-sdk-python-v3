# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScriptListModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'script_uuid': 'str',
        'enterprise_project_id': 'str',
        'name': 'str',
        'type': 'str',
        'status': 'str',
        'gmt_created': 'int',
        'gmt_modified': 'int',
        'creator': 'str',
        'creator_id': 'str',
        'operator': 'str',
        'properties': 'ScriptPropertiesModel'
    }

    attribute_map = {
        'id': 'id',
        'script_uuid': 'script_uuid',
        'enterprise_project_id': 'enterprise_project_id',
        'name': 'name',
        'type': 'type',
        'status': 'status',
        'gmt_created': 'gmt_created',
        'gmt_modified': 'gmt_modified',
        'creator': 'creator',
        'creator_id': 'creator_id',
        'operator': 'operator',
        'properties': 'properties'
    }

    def __init__(self, id=None, script_uuid=None, enterprise_project_id=None, name=None, type=None, status=None, gmt_created=None, gmt_modified=None, creator=None, creator_id=None, operator=None, properties=None):
        r"""ScriptListModel

        The model defined in huaweicloud sdk

        :param id: 脚本自增id
        :type id: int
        :param script_uuid: 脚本uuid
        :type script_uuid: str
        :param enterprise_project_id: 企业项目ID，默认为：0
        :type enterprise_project_id: str
        :param name: 脚本名称
        :type name: str
        :param type: 脚本类型 SHELL:shell脚本 PYTHON:python脚本 BAT:bat脚本
        :type type: str
        :param status: 脚本状态 PENDING_APPROVE:待审批 APPROVED：正常（审批通过） REJECTED：驳回（审批人，驳回该脚本
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
        """
        
        

        self._id = None
        self._script_uuid = None
        self._enterprise_project_id = None
        self._name = None
        self._type = None
        self._status = None
        self._gmt_created = None
        self._gmt_modified = None
        self._creator = None
        self._creator_id = None
        self._operator = None
        self._properties = None
        self.discriminator = None

        self.id = id
        self.script_uuid = script_uuid
        self.enterprise_project_id = enterprise_project_id
        self.name = name
        self.type = type
        self.status = status
        self.gmt_created = gmt_created
        if gmt_modified is not None:
            self.gmt_modified = gmt_modified
        self.creator = creator
        self.creator_id = creator_id
        if operator is not None:
            self.operator = operator
        self.properties = properties

    @property
    def id(self):
        r"""Gets the id of this ScriptListModel.

        脚本自增id

        :return: The id of this ScriptListModel.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ScriptListModel.

        脚本自增id

        :param id: The id of this ScriptListModel.
        :type id: int
        """
        self._id = id

    @property
    def script_uuid(self):
        r"""Gets the script_uuid of this ScriptListModel.

        脚本uuid

        :return: The script_uuid of this ScriptListModel.
        :rtype: str
        """
        return self._script_uuid

    @script_uuid.setter
    def script_uuid(self, script_uuid):
        r"""Sets the script_uuid of this ScriptListModel.

        脚本uuid

        :param script_uuid: The script_uuid of this ScriptListModel.
        :type script_uuid: str
        """
        self._script_uuid = script_uuid

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ScriptListModel.

        企业项目ID，默认为：0

        :return: The enterprise_project_id of this ScriptListModel.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ScriptListModel.

        企业项目ID，默认为：0

        :param enterprise_project_id: The enterprise_project_id of this ScriptListModel.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def name(self):
        r"""Gets the name of this ScriptListModel.

        脚本名称

        :return: The name of this ScriptListModel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ScriptListModel.

        脚本名称

        :param name: The name of this ScriptListModel.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this ScriptListModel.

        脚本类型 SHELL:shell脚本 PYTHON:python脚本 BAT:bat脚本

        :return: The type of this ScriptListModel.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ScriptListModel.

        脚本类型 SHELL:shell脚本 PYTHON:python脚本 BAT:bat脚本

        :param type: The type of this ScriptListModel.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this ScriptListModel.

        脚本状态 PENDING_APPROVE:待审批 APPROVED：正常（审批通过） REJECTED：驳回（审批人，驳回该脚本

        :return: The status of this ScriptListModel.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ScriptListModel.

        脚本状态 PENDING_APPROVE:待审批 APPROVED：正常（审批通过） REJECTED：驳回（审批人，驳回该脚本

        :param status: The status of this ScriptListModel.
        :type status: str
        """
        self._status = status

    @property
    def gmt_created(self):
        r"""Gets the gmt_created of this ScriptListModel.

        创建时间

        :return: The gmt_created of this ScriptListModel.
        :rtype: int
        """
        return self._gmt_created

    @gmt_created.setter
    def gmt_created(self, gmt_created):
        r"""Sets the gmt_created of this ScriptListModel.

        创建时间

        :param gmt_created: The gmt_created of this ScriptListModel.
        :type gmt_created: int
        """
        self._gmt_created = gmt_created

    @property
    def gmt_modified(self):
        r"""Gets the gmt_modified of this ScriptListModel.

        修改时间

        :return: The gmt_modified of this ScriptListModel.
        :rtype: int
        """
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, gmt_modified):
        r"""Sets the gmt_modified of this ScriptListModel.

        修改时间

        :param gmt_modified: The gmt_modified of this ScriptListModel.
        :type gmt_modified: int
        """
        self._gmt_modified = gmt_modified

    @property
    def creator(self):
        r"""Gets the creator of this ScriptListModel.

        创建人

        :return: The creator of this ScriptListModel.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this ScriptListModel.

        创建人

        :param creator: The creator of this ScriptListModel.
        :type creator: str
        """
        self._creator = creator

    @property
    def creator_id(self):
        r"""Gets the creator_id of this ScriptListModel.

        创建人Id

        :return: The creator_id of this ScriptListModel.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        r"""Sets the creator_id of this ScriptListModel.

        创建人Id

        :param creator_id: The creator_id of this ScriptListModel.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def operator(self):
        r"""Gets the operator of this ScriptListModel.

        修改人

        :return: The operator of this ScriptListModel.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this ScriptListModel.

        修改人

        :param operator: The operator of this ScriptListModel.
        :type operator: str
        """
        self._operator = operator

    @property
    def properties(self):
        r"""Gets the properties of this ScriptListModel.

        :return: The properties of this ScriptListModel.
        :rtype: :class:`huaweicloudsdkcoc.v1.ScriptPropertiesModel`
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this ScriptListModel.

        :param properties: The properties of this ScriptListModel.
        :type properties: :class:`huaweicloudsdkcoc.v1.ScriptPropertiesModel`
        """
        self._properties = properties

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
        if not isinstance(other, ScriptListModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
