# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SpecCheckitemModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'checkitem_uuid': 'str',
        'create_time': 'str',
        'language': 'str',
        'name': 'str',
        'remove_time': 'str',
        'specification_uuid': 'str',
        'uuid': 'str'
    }

    attribute_map = {
        'checkitem_uuid': 'checkitem_uuid',
        'create_time': 'create_time',
        'language': 'language',
        'name': 'name',
        'remove_time': 'remove_time',
        'specification_uuid': 'specification_uuid',
        'uuid': 'uuid'
    }

    def __init__(self, checkitem_uuid=None, create_time=None, language=None, name=None, remove_time=None, specification_uuid=None, uuid=None):
        r"""SpecCheckitemModel

        The model defined in huaweicloud sdk

        :param checkitem_uuid: 检查项的uuid
        :type checkitem_uuid: str
        :param create_time: 遵从包创建时间戳
        :type create_time: str
        :param language: 遵从包创建的语言环境
        :type language: str
        :param name: 遵从包名称
        :type name: str
        :param remove_time: 遵从包删除时间戳
        :type remove_time: str
        :param specification_uuid: 遵从包的uuid
        :type specification_uuid: str
        :param uuid: uuid
        :type uuid: str
        """
        
        

        self._checkitem_uuid = None
        self._create_time = None
        self._language = None
        self._name = None
        self._remove_time = None
        self._specification_uuid = None
        self._uuid = None
        self.discriminator = None

        if checkitem_uuid is not None:
            self.checkitem_uuid = checkitem_uuid
        if create_time is not None:
            self.create_time = create_time
        if language is not None:
            self.language = language
        if name is not None:
            self.name = name
        if remove_time is not None:
            self.remove_time = remove_time
        if specification_uuid is not None:
            self.specification_uuid = specification_uuid
        if uuid is not None:
            self.uuid = uuid

    @property
    def checkitem_uuid(self):
        r"""Gets the checkitem_uuid of this SpecCheckitemModel.

        检查项的uuid

        :return: The checkitem_uuid of this SpecCheckitemModel.
        :rtype: str
        """
        return self._checkitem_uuid

    @checkitem_uuid.setter
    def checkitem_uuid(self, checkitem_uuid):
        r"""Sets the checkitem_uuid of this SpecCheckitemModel.

        检查项的uuid

        :param checkitem_uuid: The checkitem_uuid of this SpecCheckitemModel.
        :type checkitem_uuid: str
        """
        self._checkitem_uuid = checkitem_uuid

    @property
    def create_time(self):
        r"""Gets the create_time of this SpecCheckitemModel.

        遵从包创建时间戳

        :return: The create_time of this SpecCheckitemModel.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this SpecCheckitemModel.

        遵从包创建时间戳

        :param create_time: The create_time of this SpecCheckitemModel.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def language(self):
        r"""Gets the language of this SpecCheckitemModel.

        遵从包创建的语言环境

        :return: The language of this SpecCheckitemModel.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this SpecCheckitemModel.

        遵从包创建的语言环境

        :param language: The language of this SpecCheckitemModel.
        :type language: str
        """
        self._language = language

    @property
    def name(self):
        r"""Gets the name of this SpecCheckitemModel.

        遵从包名称

        :return: The name of this SpecCheckitemModel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SpecCheckitemModel.

        遵从包名称

        :param name: The name of this SpecCheckitemModel.
        :type name: str
        """
        self._name = name

    @property
    def remove_time(self):
        r"""Gets the remove_time of this SpecCheckitemModel.

        遵从包删除时间戳

        :return: The remove_time of this SpecCheckitemModel.
        :rtype: str
        """
        return self._remove_time

    @remove_time.setter
    def remove_time(self, remove_time):
        r"""Sets the remove_time of this SpecCheckitemModel.

        遵从包删除时间戳

        :param remove_time: The remove_time of this SpecCheckitemModel.
        :type remove_time: str
        """
        self._remove_time = remove_time

    @property
    def specification_uuid(self):
        r"""Gets the specification_uuid of this SpecCheckitemModel.

        遵从包的uuid

        :return: The specification_uuid of this SpecCheckitemModel.
        :rtype: str
        """
        return self._specification_uuid

    @specification_uuid.setter
    def specification_uuid(self, specification_uuid):
        r"""Sets the specification_uuid of this SpecCheckitemModel.

        遵从包的uuid

        :param specification_uuid: The specification_uuid of this SpecCheckitemModel.
        :type specification_uuid: str
        """
        self._specification_uuid = specification_uuid

    @property
    def uuid(self):
        r"""Gets the uuid of this SpecCheckitemModel.

        uuid

        :return: The uuid of this SpecCheckitemModel.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        r"""Sets the uuid of this SpecCheckitemModel.

        uuid

        :param uuid: The uuid of this SpecCheckitemModel.
        :type uuid: str
        """
        self._uuid = uuid

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
        if not isinstance(other, SpecCheckitemModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
