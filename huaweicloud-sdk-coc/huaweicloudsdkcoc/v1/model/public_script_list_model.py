# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublicScriptListModel:

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
        'name': 'str',
        'type': 'str',
        'gmt_created': 'int',
        'description': 'str',
        'properties': 'PublicScriptPropertiesModel'
    }

    attribute_map = {
        'id': 'id',
        'script_uuid': 'script_uuid',
        'name': 'name',
        'type': 'type',
        'gmt_created': 'gmt_created',
        'description': 'description',
        'properties': 'properties'
    }

    def __init__(self, id=None, script_uuid=None, name=None, type=None, gmt_created=None, description=None, properties=None):
        r"""PublicScriptListModel

        The model defined in huaweicloud sdk

        :param id: 脚本自增id
        :type id: int
        :param script_uuid: 脚本uuid
        :type script_uuid: str
        :param name: 脚本名称
        :type name: str
        :param type: 脚本类型 SHELL:shell脚本 PYTHON:python脚本 BAT:bat脚本
        :type type: str
        :param gmt_created: 创建时间
        :type gmt_created: int
        :param description: 脚本描述： 根据X-Language(X-Language) 进行国际化
        :type description: str
        :param properties: 
        :type properties: :class:`huaweicloudsdkcoc.v1.PublicScriptPropertiesModel`
        """
        
        

        self._id = None
        self._script_uuid = None
        self._name = None
        self._type = None
        self._gmt_created = None
        self._description = None
        self._properties = None
        self.discriminator = None

        self.id = id
        self.script_uuid = script_uuid
        self.name = name
        self.type = type
        self.gmt_created = gmt_created
        self.description = description
        self.properties = properties

    @property
    def id(self):
        r"""Gets the id of this PublicScriptListModel.

        脚本自增id

        :return: The id of this PublicScriptListModel.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PublicScriptListModel.

        脚本自增id

        :param id: The id of this PublicScriptListModel.
        :type id: int
        """
        self._id = id

    @property
    def script_uuid(self):
        r"""Gets the script_uuid of this PublicScriptListModel.

        脚本uuid

        :return: The script_uuid of this PublicScriptListModel.
        :rtype: str
        """
        return self._script_uuid

    @script_uuid.setter
    def script_uuid(self, script_uuid):
        r"""Sets the script_uuid of this PublicScriptListModel.

        脚本uuid

        :param script_uuid: The script_uuid of this PublicScriptListModel.
        :type script_uuid: str
        """
        self._script_uuid = script_uuid

    @property
    def name(self):
        r"""Gets the name of this PublicScriptListModel.

        脚本名称

        :return: The name of this PublicScriptListModel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PublicScriptListModel.

        脚本名称

        :param name: The name of this PublicScriptListModel.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this PublicScriptListModel.

        脚本类型 SHELL:shell脚本 PYTHON:python脚本 BAT:bat脚本

        :return: The type of this PublicScriptListModel.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this PublicScriptListModel.

        脚本类型 SHELL:shell脚本 PYTHON:python脚本 BAT:bat脚本

        :param type: The type of this PublicScriptListModel.
        :type type: str
        """
        self._type = type

    @property
    def gmt_created(self):
        r"""Gets the gmt_created of this PublicScriptListModel.

        创建时间

        :return: The gmt_created of this PublicScriptListModel.
        :rtype: int
        """
        return self._gmt_created

    @gmt_created.setter
    def gmt_created(self, gmt_created):
        r"""Sets the gmt_created of this PublicScriptListModel.

        创建时间

        :param gmt_created: The gmt_created of this PublicScriptListModel.
        :type gmt_created: int
        """
        self._gmt_created = gmt_created

    @property
    def description(self):
        r"""Gets the description of this PublicScriptListModel.

        脚本描述： 根据X-Language(X-Language) 进行国际化

        :return: The description of this PublicScriptListModel.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PublicScriptListModel.

        脚本描述： 根据X-Language(X-Language) 进行国际化

        :param description: The description of this PublicScriptListModel.
        :type description: str
        """
        self._description = description

    @property
    def properties(self):
        r"""Gets the properties of this PublicScriptListModel.

        :return: The properties of this PublicScriptListModel.
        :rtype: :class:`huaweicloudsdkcoc.v1.PublicScriptPropertiesModel`
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this PublicScriptListModel.

        :param properties: The properties of this PublicScriptListModel.
        :type properties: :class:`huaweicloudsdkcoc.v1.PublicScriptPropertiesModel`
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
        if not isinstance(other, PublicScriptListModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
