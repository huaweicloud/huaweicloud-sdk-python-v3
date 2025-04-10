# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VolumeType:

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
        'extra_specs': 'VolumeTypeExtraSpecs',
        'description': 'str',
        'qos_specs_id': 'str',
        'is_public': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'extra_specs': 'extra_specs',
        'description': 'description',
        'qos_specs_id': 'qos_specs_id',
        'is_public': 'is_public'
    }

    def __init__(self, id=None, name=None, extra_specs=None, description=None, qos_specs_id=None, is_public=None):
        r"""VolumeType

        The model defined in huaweicloud sdk

        :param id: 云硬盘类型的ID。
        :type id: str
        :param name: 云硬盘类型名称。
        :type name: str
        :param extra_specs: 
        :type extra_specs: :class:`huaweicloudsdkevs.v2.VolumeTypeExtraSpecs`
        :param description: 云硬盘类型的描述信息。
        :type description: str
        :param qos_specs_id: 预留属性。
        :type qos_specs_id: str
        :param is_public: 预留属性。
        :type is_public: bool
        """
        
        

        self._id = None
        self._name = None
        self._extra_specs = None
        self._description = None
        self._qos_specs_id = None
        self._is_public = None
        self.discriminator = None

        self.id = id
        self.name = name
        if extra_specs is not None:
            self.extra_specs = extra_specs
        if description is not None:
            self.description = description
        if qos_specs_id is not None:
            self.qos_specs_id = qos_specs_id
        if is_public is not None:
            self.is_public = is_public

    @property
    def id(self):
        r"""Gets the id of this VolumeType.

        云硬盘类型的ID。

        :return: The id of this VolumeType.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this VolumeType.

        云硬盘类型的ID。

        :param id: The id of this VolumeType.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this VolumeType.

        云硬盘类型名称。

        :return: The name of this VolumeType.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this VolumeType.

        云硬盘类型名称。

        :param name: The name of this VolumeType.
        :type name: str
        """
        self._name = name

    @property
    def extra_specs(self):
        r"""Gets the extra_specs of this VolumeType.

        :return: The extra_specs of this VolumeType.
        :rtype: :class:`huaweicloudsdkevs.v2.VolumeTypeExtraSpecs`
        """
        return self._extra_specs

    @extra_specs.setter
    def extra_specs(self, extra_specs):
        r"""Sets the extra_specs of this VolumeType.

        :param extra_specs: The extra_specs of this VolumeType.
        :type extra_specs: :class:`huaweicloudsdkevs.v2.VolumeTypeExtraSpecs`
        """
        self._extra_specs = extra_specs

    @property
    def description(self):
        r"""Gets the description of this VolumeType.

        云硬盘类型的描述信息。

        :return: The description of this VolumeType.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this VolumeType.

        云硬盘类型的描述信息。

        :param description: The description of this VolumeType.
        :type description: str
        """
        self._description = description

    @property
    def qos_specs_id(self):
        r"""Gets the qos_specs_id of this VolumeType.

        预留属性。

        :return: The qos_specs_id of this VolumeType.
        :rtype: str
        """
        return self._qos_specs_id

    @qos_specs_id.setter
    def qos_specs_id(self, qos_specs_id):
        r"""Sets the qos_specs_id of this VolumeType.

        预留属性。

        :param qos_specs_id: The qos_specs_id of this VolumeType.
        :type qos_specs_id: str
        """
        self._qos_specs_id = qos_specs_id

    @property
    def is_public(self):
        r"""Gets the is_public of this VolumeType.

        预留属性。

        :return: The is_public of this VolumeType.
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        r"""Sets the is_public of this VolumeType.

        预留属性。

        :param is_public: The is_public of this VolumeType.
        :type is_public: bool
        """
        self._is_public = is_public

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
        if not isinstance(other, VolumeType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
