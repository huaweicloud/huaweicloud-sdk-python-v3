# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssetModelResp:

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
        'version': 'str',
        'location': 'str',
        'desc': 'str',
        'series': 'str',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'code': 'code',
        'version': 'version',
        'location': 'location',
        'desc': 'desc',
        'series': 'series',
        'type': 'type'
    }

    def __init__(self, id=None, name=None, code=None, version=None, location=None, desc=None, series=None, type=None):
        r"""AssetModelResp

        The model defined in huaweicloud sdk

        :param id: **参数解释**：模型id。 **取值范围**：不涉及。
        :type id: str
        :param name: **参数解释**：模型名称。 **取值范围**：不涉及。
        :type name: str
        :param code: **参数解释**：模型名称。 **取值范围**：不涉及。
        :type code: str
        :param version: **参数解释**：模型发布版本。 **取值范围**：不涉及。
        :type version: str
        :param location: **参数解释**：模型发布地址。 **取值范围**：不涉及。
        :type location: str
        :param desc: **参数解释**：模型描述。 **取值范围**：不涉及。
        :type desc: str
        :param series: **参数解释**：模型品牌。 **取值范围**：不涉及。
        :type series: str
        :param type: **参数解释**：模型类型。 **取值范围**：不涉及。
        :type type: str
        """
        
        

        self._id = None
        self._name = None
        self._code = None
        self._version = None
        self._location = None
        self._desc = None
        self._series = None
        self._type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if code is not None:
            self.code = code
        self.version = version
        if location is not None:
            self.location = location
        if desc is not None:
            self.desc = desc
        if series is not None:
            self.series = series
        self.type = type

    @property
    def id(self):
        r"""Gets the id of this AssetModelResp.

        **参数解释**：模型id。 **取值范围**：不涉及。

        :return: The id of this AssetModelResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AssetModelResp.

        **参数解释**：模型id。 **取值范围**：不涉及。

        :param id: The id of this AssetModelResp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this AssetModelResp.

        **参数解释**：模型名称。 **取值范围**：不涉及。

        :return: The name of this AssetModelResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AssetModelResp.

        **参数解释**：模型名称。 **取值范围**：不涉及。

        :param name: The name of this AssetModelResp.
        :type name: str
        """
        self._name = name

    @property
    def code(self):
        r"""Gets the code of this AssetModelResp.

        **参数解释**：模型名称。 **取值范围**：不涉及。

        :return: The code of this AssetModelResp.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this AssetModelResp.

        **参数解释**：模型名称。 **取值范围**：不涉及。

        :param code: The code of this AssetModelResp.
        :type code: str
        """
        self._code = code

    @property
    def version(self):
        r"""Gets the version of this AssetModelResp.

        **参数解释**：模型发布版本。 **取值范围**：不涉及。

        :return: The version of this AssetModelResp.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this AssetModelResp.

        **参数解释**：模型发布版本。 **取值范围**：不涉及。

        :param version: The version of this AssetModelResp.
        :type version: str
        """
        self._version = version

    @property
    def location(self):
        r"""Gets the location of this AssetModelResp.

        **参数解释**：模型发布地址。 **取值范围**：不涉及。

        :return: The location of this AssetModelResp.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this AssetModelResp.

        **参数解释**：模型发布地址。 **取值范围**：不涉及。

        :param location: The location of this AssetModelResp.
        :type location: str
        """
        self._location = location

    @property
    def desc(self):
        r"""Gets the desc of this AssetModelResp.

        **参数解释**：模型描述。 **取值范围**：不涉及。

        :return: The desc of this AssetModelResp.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this AssetModelResp.

        **参数解释**：模型描述。 **取值范围**：不涉及。

        :param desc: The desc of this AssetModelResp.
        :type desc: str
        """
        self._desc = desc

    @property
    def series(self):
        r"""Gets the series of this AssetModelResp.

        **参数解释**：模型品牌。 **取值范围**：不涉及。

        :return: The series of this AssetModelResp.
        :rtype: str
        """
        return self._series

    @series.setter
    def series(self, series):
        r"""Sets the series of this AssetModelResp.

        **参数解释**：模型品牌。 **取值范围**：不涉及。

        :param series: The series of this AssetModelResp.
        :type series: str
        """
        self._series = series

    @property
    def type(self):
        r"""Gets the type of this AssetModelResp.

        **参数解释**：模型类型。 **取值范围**：不涉及。

        :return: The type of this AssetModelResp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AssetModelResp.

        **参数解释**：模型类型。 **取值范围**：不涉及。

        :param type: The type of this AssetModelResp.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, AssetModelResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
