# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupTriggerInfo:

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
        'type': 'str',
        'properties': 'BackupTriggerPropertiesInfo'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'properties': 'properties'
    }

    def __init__(self, id=None, name=None, type=None, properties=None):
        r"""BackupTriggerInfo

        The model defined in huaweicloud sdk

        :param id: **参数解释**: 调度器id **取值范围**: 字符长度0-256 
        :type id: str
        :param name: **参数解释**: 调度器名称 **取值范围**: 字符长度0-256 
        :type name: str
        :param type: **参数解释**: 调度器类型，目前只支持time，定时调度。 **取值范围**: 字符长度0-256 
        :type type: str
        :param properties: 
        :type properties: :class:`huaweicloudsdkhss.v5.BackupTriggerPropertiesInfo`
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._properties = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if properties is not None:
            self.properties = properties

    @property
    def id(self):
        r"""Gets the id of this BackupTriggerInfo.

        **参数解释**: 调度器id **取值范围**: 字符长度0-256 

        :return: The id of this BackupTriggerInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BackupTriggerInfo.

        **参数解释**: 调度器id **取值范围**: 字符长度0-256 

        :param id: The id of this BackupTriggerInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this BackupTriggerInfo.

        **参数解释**: 调度器名称 **取值范围**: 字符长度0-256 

        :return: The name of this BackupTriggerInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BackupTriggerInfo.

        **参数解释**: 调度器名称 **取值范围**: 字符长度0-256 

        :param name: The name of this BackupTriggerInfo.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this BackupTriggerInfo.

        **参数解释**: 调度器类型，目前只支持time，定时调度。 **取值范围**: 字符长度0-256 

        :return: The type of this BackupTriggerInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this BackupTriggerInfo.

        **参数解释**: 调度器类型，目前只支持time，定时调度。 **取值范围**: 字符长度0-256 

        :param type: The type of this BackupTriggerInfo.
        :type type: str
        """
        self._type = type

    @property
    def properties(self):
        r"""Gets the properties of this BackupTriggerInfo.

        :return: The properties of this BackupTriggerInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.BackupTriggerPropertiesInfo`
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this BackupTriggerInfo.

        :param properties: The properties of this BackupTriggerInfo.
        :type properties: :class:`huaweicloudsdkhss.v5.BackupTriggerPropertiesInfo`
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
        if not isinstance(other, BackupTriggerInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
