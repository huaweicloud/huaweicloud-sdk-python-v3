# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataClassTypeDetailInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'parent_name': 'str',
        'parent_business_code': 'str',
        'name': 'str',
        'business_code': 'str',
        'description': 'str',
        'workspace_id': 'str',
        'project_id': 'str',
        'enabled': 'bool',
        'is_built_in': 'bool',
        'layout_id': 'str',
        'layout_name': 'str',
        'dataclass_id': 'str',
        'sla': 'int'
    }

    attribute_map = {
        'id': 'id',
        'parent_name': 'parent_name',
        'parent_business_code': 'parent_business_code',
        'name': 'name',
        'business_code': 'business_code',
        'description': 'description',
        'workspace_id': 'workspace_id',
        'project_id': 'project_id',
        'enabled': 'enabled',
        'is_built_in': 'is_built_in',
        'layout_id': 'layout_id',
        'layout_name': 'layout_name',
        'dataclass_id': 'dataclass_id',
        'sla': 'sla'
    }

    def __init__(self, id=None, parent_name=None, parent_business_code=None, name=None, business_code=None, description=None, workspace_id=None, project_id=None, enabled=None, is_built_in=None, layout_id=None, layout_name=None, dataclass_id=None, sla=None):
        """DataClassTypeDetailInfo

        The model defined in huaweicloud sdk

        :param id: Id value
        :type id: str
        :param parent_name: The name, display only
        :type parent_name: str
        :param parent_business_code: 类型标识码
        :type parent_business_code: str
        :param name: The name, display only
        :type name: str
        :param business_code: 类型标识码
        :type business_code: str
        :param description: The description, display only
        :type description: str
        :param workspace_id: workspace id
        :type workspace_id: str
        :param project_id: Project id value
        :type project_id: str
        :param enabled: If is enabled, false for disenabled, true for enabled
        :type enabled: bool
        :param is_built_in: 是否内置
        :type is_built_in: bool
        :param layout_id: 布局ID
        :type layout_id: str
        :param layout_name: The name, display only
        :type layout_name: str
        :param dataclass_id: dataclass id.
        :type dataclass_id: str
        :param sla: sla
        :type sla: int
        """
        
        

        self._id = None
        self._parent_name = None
        self._parent_business_code = None
        self._name = None
        self._business_code = None
        self._description = None
        self._workspace_id = None
        self._project_id = None
        self._enabled = None
        self._is_built_in = None
        self._layout_id = None
        self._layout_name = None
        self._dataclass_id = None
        self._sla = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if parent_name is not None:
            self.parent_name = parent_name
        if parent_business_code is not None:
            self.parent_business_code = parent_business_code
        if name is not None:
            self.name = name
        if business_code is not None:
            self.business_code = business_code
        if description is not None:
            self.description = description
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if project_id is not None:
            self.project_id = project_id
        if enabled is not None:
            self.enabled = enabled
        if is_built_in is not None:
            self.is_built_in = is_built_in
        if layout_id is not None:
            self.layout_id = layout_id
        if layout_name is not None:
            self.layout_name = layout_name
        if dataclass_id is not None:
            self.dataclass_id = dataclass_id
        if sla is not None:
            self.sla = sla

    @property
    def id(self):
        """Gets the id of this DataClassTypeDetailInfo.

        Id value

        :return: The id of this DataClassTypeDetailInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataClassTypeDetailInfo.

        Id value

        :param id: The id of this DataClassTypeDetailInfo.
        :type id: str
        """
        self._id = id

    @property
    def parent_name(self):
        """Gets the parent_name of this DataClassTypeDetailInfo.

        The name, display only

        :return: The parent_name of this DataClassTypeDetailInfo.
        :rtype: str
        """
        return self._parent_name

    @parent_name.setter
    def parent_name(self, parent_name):
        """Sets the parent_name of this DataClassTypeDetailInfo.

        The name, display only

        :param parent_name: The parent_name of this DataClassTypeDetailInfo.
        :type parent_name: str
        """
        self._parent_name = parent_name

    @property
    def parent_business_code(self):
        """Gets the parent_business_code of this DataClassTypeDetailInfo.

        类型标识码

        :return: The parent_business_code of this DataClassTypeDetailInfo.
        :rtype: str
        """
        return self._parent_business_code

    @parent_business_code.setter
    def parent_business_code(self, parent_business_code):
        """Sets the parent_business_code of this DataClassTypeDetailInfo.

        类型标识码

        :param parent_business_code: The parent_business_code of this DataClassTypeDetailInfo.
        :type parent_business_code: str
        """
        self._parent_business_code = parent_business_code

    @property
    def name(self):
        """Gets the name of this DataClassTypeDetailInfo.

        The name, display only

        :return: The name of this DataClassTypeDetailInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DataClassTypeDetailInfo.

        The name, display only

        :param name: The name of this DataClassTypeDetailInfo.
        :type name: str
        """
        self._name = name

    @property
    def business_code(self):
        """Gets the business_code of this DataClassTypeDetailInfo.

        类型标识码

        :return: The business_code of this DataClassTypeDetailInfo.
        :rtype: str
        """
        return self._business_code

    @business_code.setter
    def business_code(self, business_code):
        """Sets the business_code of this DataClassTypeDetailInfo.

        类型标识码

        :param business_code: The business_code of this DataClassTypeDetailInfo.
        :type business_code: str
        """
        self._business_code = business_code

    @property
    def description(self):
        """Gets the description of this DataClassTypeDetailInfo.

        The description, display only

        :return: The description of this DataClassTypeDetailInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DataClassTypeDetailInfo.

        The description, display only

        :param description: The description of this DataClassTypeDetailInfo.
        :type description: str
        """
        self._description = description

    @property
    def workspace_id(self):
        """Gets the workspace_id of this DataClassTypeDetailInfo.

        workspace id

        :return: The workspace_id of this DataClassTypeDetailInfo.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this DataClassTypeDetailInfo.

        workspace id

        :param workspace_id: The workspace_id of this DataClassTypeDetailInfo.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def project_id(self):
        """Gets the project_id of this DataClassTypeDetailInfo.

        Project id value

        :return: The project_id of this DataClassTypeDetailInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this DataClassTypeDetailInfo.

        Project id value

        :param project_id: The project_id of this DataClassTypeDetailInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def enabled(self):
        """Gets the enabled of this DataClassTypeDetailInfo.

        If is enabled, false for disenabled, true for enabled

        :return: The enabled of this DataClassTypeDetailInfo.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this DataClassTypeDetailInfo.

        If is enabled, false for disenabled, true for enabled

        :param enabled: The enabled of this DataClassTypeDetailInfo.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def is_built_in(self):
        """Gets the is_built_in of this DataClassTypeDetailInfo.

        是否内置

        :return: The is_built_in of this DataClassTypeDetailInfo.
        :rtype: bool
        """
        return self._is_built_in

    @is_built_in.setter
    def is_built_in(self, is_built_in):
        """Sets the is_built_in of this DataClassTypeDetailInfo.

        是否内置

        :param is_built_in: The is_built_in of this DataClassTypeDetailInfo.
        :type is_built_in: bool
        """
        self._is_built_in = is_built_in

    @property
    def layout_id(self):
        """Gets the layout_id of this DataClassTypeDetailInfo.

        布局ID

        :return: The layout_id of this DataClassTypeDetailInfo.
        :rtype: str
        """
        return self._layout_id

    @layout_id.setter
    def layout_id(self, layout_id):
        """Sets the layout_id of this DataClassTypeDetailInfo.

        布局ID

        :param layout_id: The layout_id of this DataClassTypeDetailInfo.
        :type layout_id: str
        """
        self._layout_id = layout_id

    @property
    def layout_name(self):
        """Gets the layout_name of this DataClassTypeDetailInfo.

        The name, display only

        :return: The layout_name of this DataClassTypeDetailInfo.
        :rtype: str
        """
        return self._layout_name

    @layout_name.setter
    def layout_name(self, layout_name):
        """Sets the layout_name of this DataClassTypeDetailInfo.

        The name, display only

        :param layout_name: The layout_name of this DataClassTypeDetailInfo.
        :type layout_name: str
        """
        self._layout_name = layout_name

    @property
    def dataclass_id(self):
        """Gets the dataclass_id of this DataClassTypeDetailInfo.

        dataclass id.

        :return: The dataclass_id of this DataClassTypeDetailInfo.
        :rtype: str
        """
        return self._dataclass_id

    @dataclass_id.setter
    def dataclass_id(self, dataclass_id):
        """Sets the dataclass_id of this DataClassTypeDetailInfo.

        dataclass id.

        :param dataclass_id: The dataclass_id of this DataClassTypeDetailInfo.
        :type dataclass_id: str
        """
        self._dataclass_id = dataclass_id

    @property
    def sla(self):
        """Gets the sla of this DataClassTypeDetailInfo.

        sla

        :return: The sla of this DataClassTypeDetailInfo.
        :rtype: int
        """
        return self._sla

    @sla.setter
    def sla(self, sla):
        """Sets the sla of this DataClassTypeDetailInfo.

        sla

        :param sla: The sla of this DataClassTypeDetailInfo.
        :type sla: int
        """
        self._sla = sla

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
        if not isinstance(other, DataClassTypeDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
