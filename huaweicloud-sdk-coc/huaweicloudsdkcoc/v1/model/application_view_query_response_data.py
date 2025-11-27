# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplicationViewQueryResponseData:

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
        'name': 'str',
        'code': 'str',
        'type': 'str',
        'parent_id': 'str',
        'component_id': 'str',
        'application_id': 'str',
        'path': 'str',
        'vendor': 'str',
        'related_domain_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'code': 'code',
        'type': 'type',
        'parent_id': 'parent_id',
        'component_id': 'component_id',
        'application_id': 'application_id',
        'path': 'path',
        'vendor': 'vendor',
        'related_domain_id': 'related_domain_id'
    }

    def __init__(self, id=None, name=None, code=None, type=None, parent_id=None, component_id=None, application_id=None, path=None, vendor=None, related_domain_id=None):
        r"""ApplicationViewQueryResponseData

        The model defined in huaweicloud sdk

        :param id: **参数解释：** CMDB分配的uuid。 **取值范围：** 不涉及。
        :type id: str
        :param name: **参数解释：** 应用或分组或组件的名称。 **取值范围：** 字符串，长度在[3,50]之间。
        :type name: str
        :param code: **参数解释：** 应用或分组或组件code。 **取值范围：** 字符串，长度在[3,50]之间。
        :type code: str
        :param type: **参数解释：** 应用或分组或组件。 **取值范围：** 不涉及。
        :type type: str
        :param parent_id: **参数解释：** 父节点id，即查询结果所在路径的父节点id。 **取值范围：** 字符串，长度24。
        :type parent_id: str
        :param component_id: **参数解释：** 组件id。 **取值范围：** 字符串，长度24。
        :type component_id: str
        :param application_id: **参数解释：** 应用id。 **取值范围：** 字符串，长度24。
        :type application_id: str
        :param path: **参数解释：** 节点所在路径，由应用，组件，分组等id组成。 **取值范围：** 不涉及。
        :type path: str
        :param vendor: **参数解释：** 云厂商信息。 **取值范围：** - RMS：华为云厂商。 - ALI：阿里云厂商。 - OTHER：其他厂商。
        :type vendor: str
        :param related_domain_id: **参数解释：** 跨账号资源所属的domainId。 **取值范围：** 不涉及。
        :type related_domain_id: str
        """
        
        

        self._id = None
        self._name = None
        self._code = None
        self._type = None
        self._parent_id = None
        self._component_id = None
        self._application_id = None
        self._path = None
        self._vendor = None
        self._related_domain_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if code is not None:
            self.code = code
        if type is not None:
            self.type = type
        if parent_id is not None:
            self.parent_id = parent_id
        if component_id is not None:
            self.component_id = component_id
        if application_id is not None:
            self.application_id = application_id
        if path is not None:
            self.path = path
        if vendor is not None:
            self.vendor = vendor
        if related_domain_id is not None:
            self.related_domain_id = related_domain_id

    @property
    def id(self):
        r"""Gets the id of this ApplicationViewQueryResponseData.

        **参数解释：** CMDB分配的uuid。 **取值范围：** 不涉及。

        :return: The id of this ApplicationViewQueryResponseData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ApplicationViewQueryResponseData.

        **参数解释：** CMDB分配的uuid。 **取值范围：** 不涉及。

        :param id: The id of this ApplicationViewQueryResponseData.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ApplicationViewQueryResponseData.

        **参数解释：** 应用或分组或组件的名称。 **取值范围：** 字符串，长度在[3,50]之间。

        :return: The name of this ApplicationViewQueryResponseData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ApplicationViewQueryResponseData.

        **参数解释：** 应用或分组或组件的名称。 **取值范围：** 字符串，长度在[3,50]之间。

        :param name: The name of this ApplicationViewQueryResponseData.
        :type name: str
        """
        self._name = name

    @property
    def code(self):
        r"""Gets the code of this ApplicationViewQueryResponseData.

        **参数解释：** 应用或分组或组件code。 **取值范围：** 字符串，长度在[3,50]之间。

        :return: The code of this ApplicationViewQueryResponseData.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ApplicationViewQueryResponseData.

        **参数解释：** 应用或分组或组件code。 **取值范围：** 字符串，长度在[3,50]之间。

        :param code: The code of this ApplicationViewQueryResponseData.
        :type code: str
        """
        self._code = code

    @property
    def type(self):
        r"""Gets the type of this ApplicationViewQueryResponseData.

        **参数解释：** 应用或分组或组件。 **取值范围：** 不涉及。

        :return: The type of this ApplicationViewQueryResponseData.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ApplicationViewQueryResponseData.

        **参数解释：** 应用或分组或组件。 **取值范围：** 不涉及。

        :param type: The type of this ApplicationViewQueryResponseData.
        :type type: str
        """
        self._type = type

    @property
    def parent_id(self):
        r"""Gets the parent_id of this ApplicationViewQueryResponseData.

        **参数解释：** 父节点id，即查询结果所在路径的父节点id。 **取值范围：** 字符串，长度24。

        :return: The parent_id of this ApplicationViewQueryResponseData.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this ApplicationViewQueryResponseData.

        **参数解释：** 父节点id，即查询结果所在路径的父节点id。 **取值范围：** 字符串，长度24。

        :param parent_id: The parent_id of this ApplicationViewQueryResponseData.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def component_id(self):
        r"""Gets the component_id of this ApplicationViewQueryResponseData.

        **参数解释：** 组件id。 **取值范围：** 字符串，长度24。

        :return: The component_id of this ApplicationViewQueryResponseData.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        r"""Sets the component_id of this ApplicationViewQueryResponseData.

        **参数解释：** 组件id。 **取值范围：** 字符串，长度24。

        :param component_id: The component_id of this ApplicationViewQueryResponseData.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def application_id(self):
        r"""Gets the application_id of this ApplicationViewQueryResponseData.

        **参数解释：** 应用id。 **取值范围：** 字符串，长度24。

        :return: The application_id of this ApplicationViewQueryResponseData.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        r"""Sets the application_id of this ApplicationViewQueryResponseData.

        **参数解释：** 应用id。 **取值范围：** 字符串，长度24。

        :param application_id: The application_id of this ApplicationViewQueryResponseData.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def path(self):
        r"""Gets the path of this ApplicationViewQueryResponseData.

        **参数解释：** 节点所在路径，由应用，组件，分组等id组成。 **取值范围：** 不涉及。

        :return: The path of this ApplicationViewQueryResponseData.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this ApplicationViewQueryResponseData.

        **参数解释：** 节点所在路径，由应用，组件，分组等id组成。 **取值范围：** 不涉及。

        :param path: The path of this ApplicationViewQueryResponseData.
        :type path: str
        """
        self._path = path

    @property
    def vendor(self):
        r"""Gets the vendor of this ApplicationViewQueryResponseData.

        **参数解释：** 云厂商信息。 **取值范围：** - RMS：华为云厂商。 - ALI：阿里云厂商。 - OTHER：其他厂商。

        :return: The vendor of this ApplicationViewQueryResponseData.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        r"""Sets the vendor of this ApplicationViewQueryResponseData.

        **参数解释：** 云厂商信息。 **取值范围：** - RMS：华为云厂商。 - ALI：阿里云厂商。 - OTHER：其他厂商。

        :param vendor: The vendor of this ApplicationViewQueryResponseData.
        :type vendor: str
        """
        self._vendor = vendor

    @property
    def related_domain_id(self):
        r"""Gets the related_domain_id of this ApplicationViewQueryResponseData.

        **参数解释：** 跨账号资源所属的domainId。 **取值范围：** 不涉及。

        :return: The related_domain_id of this ApplicationViewQueryResponseData.
        :rtype: str
        """
        return self._related_domain_id

    @related_domain_id.setter
    def related_domain_id(self, related_domain_id):
        r"""Sets the related_domain_id of this ApplicationViewQueryResponseData.

        **参数解释：** 跨账号资源所属的domainId。 **取值范围：** 不涉及。

        :param related_domain_id: The related_domain_id of this ApplicationViewQueryResponseData.
        :type related_domain_id: str
        """
        self._related_domain_id = related_domain_id

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
        if not isinstance(other, ApplicationViewQueryResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
