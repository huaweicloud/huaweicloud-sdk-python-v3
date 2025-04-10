# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AtlasClassificationInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'entity_guid': 'str',
        'propagate': 'bool',
        'validity_periods': 'list[TimeBoundary]',
        'type_name': 'str',
        'attributes': 'object'
    }

    attribute_map = {
        'entity_guid': 'entity_guid',
        'propagate': 'propagate',
        'validity_periods': 'validity_periods',
        'type_name': 'type_name',
        'attributes': 'attributes'
    }

    def __init__(self, entity_guid=None, propagate=None, validity_periods=None, type_name=None, attributes=None):
        r"""AtlasClassificationInfo

        The model defined in huaweicloud sdk

        :param entity_guid: guid
        :type entity_guid: str
        :param propagate: 是否传播
        :type propagate: bool
        :param validity_periods: 时间信息
        :type validity_periods: list[:class:`huaweicloudsdkdataartsstudio.v1.TimeBoundary`]
        :param type_name: 类型名称
        :type type_name: str
        :param attributes: 实体map Map&lt;String, Object&gt;
        :type attributes: object
        """
        
        

        self._entity_guid = None
        self._propagate = None
        self._validity_periods = None
        self._type_name = None
        self._attributes = None
        self.discriminator = None

        if entity_guid is not None:
            self.entity_guid = entity_guid
        if propagate is not None:
            self.propagate = propagate
        if validity_periods is not None:
            self.validity_periods = validity_periods
        if type_name is not None:
            self.type_name = type_name
        if attributes is not None:
            self.attributes = attributes

    @property
    def entity_guid(self):
        r"""Gets the entity_guid of this AtlasClassificationInfo.

        guid

        :return: The entity_guid of this AtlasClassificationInfo.
        :rtype: str
        """
        return self._entity_guid

    @entity_guid.setter
    def entity_guid(self, entity_guid):
        r"""Sets the entity_guid of this AtlasClassificationInfo.

        guid

        :param entity_guid: The entity_guid of this AtlasClassificationInfo.
        :type entity_guid: str
        """
        self._entity_guid = entity_guid

    @property
    def propagate(self):
        r"""Gets the propagate of this AtlasClassificationInfo.

        是否传播

        :return: The propagate of this AtlasClassificationInfo.
        :rtype: bool
        """
        return self._propagate

    @propagate.setter
    def propagate(self, propagate):
        r"""Sets the propagate of this AtlasClassificationInfo.

        是否传播

        :param propagate: The propagate of this AtlasClassificationInfo.
        :type propagate: bool
        """
        self._propagate = propagate

    @property
    def validity_periods(self):
        r"""Gets the validity_periods of this AtlasClassificationInfo.

        时间信息

        :return: The validity_periods of this AtlasClassificationInfo.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.TimeBoundary`]
        """
        return self._validity_periods

    @validity_periods.setter
    def validity_periods(self, validity_periods):
        r"""Sets the validity_periods of this AtlasClassificationInfo.

        时间信息

        :param validity_periods: The validity_periods of this AtlasClassificationInfo.
        :type validity_periods: list[:class:`huaweicloudsdkdataartsstudio.v1.TimeBoundary`]
        """
        self._validity_periods = validity_periods

    @property
    def type_name(self):
        r"""Gets the type_name of this AtlasClassificationInfo.

        类型名称

        :return: The type_name of this AtlasClassificationInfo.
        :rtype: str
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        r"""Sets the type_name of this AtlasClassificationInfo.

        类型名称

        :param type_name: The type_name of this AtlasClassificationInfo.
        :type type_name: str
        """
        self._type_name = type_name

    @property
    def attributes(self):
        r"""Gets the attributes of this AtlasClassificationInfo.

        实体map Map<String, Object>

        :return: The attributes of this AtlasClassificationInfo.
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        r"""Sets the attributes of this AtlasClassificationInfo.

        实体map Map<String, Object>

        :param attributes: The attributes of this AtlasClassificationInfo.
        :type attributes: object
        """
        self._attributes = attributes

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
        if not isinstance(other, AtlasClassificationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
