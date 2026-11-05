# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SupabaseSpecFlavorInfo:

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
        'mode': 'str',
        'version': 'str',
        'vcpus': 'int',
        'ram': 'int',
        'spec_code': 'str',
        'group_type': 'str',
        'availability_zones': 'list[SupabaseSpecFlavorInfoAvailabilityZones]'
    }

    attribute_map = {
        'id': 'id',
        'mode': 'mode',
        'version': 'version',
        'vcpus': 'vcpus',
        'ram': 'ram',
        'spec_code': 'spec_code',
        'group_type': 'group_type',
        'availability_zones': 'availability_zones'
    }

    def __init__(self, id=None, mode=None, version=None, vcpus=None, ram=None, spec_code=None, group_type=None, availability_zones=None):
        r"""SupabaseSpecFlavorInfo

        The model defined in huaweicloud sdk

        :param id: 
        :type id: str
        :param mode: 
        :type mode: str
        :param version: 
        :type version: str
        :param vcpus: 
        :type vcpus: int
        :param ram: 
        :type ram: int
        :param spec_code: 
        :type spec_code: str
        :param group_type: 
        :type group_type: str
        :param availability_zones: 
        :type availability_zones: list[:class:`huaweicloudsdkrds.v3.SupabaseSpecFlavorInfoAvailabilityZones`]
        """
        
        

        self._id = None
        self._mode = None
        self._version = None
        self._vcpus = None
        self._ram = None
        self._spec_code = None
        self._group_type = None
        self._availability_zones = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if mode is not None:
            self.mode = mode
        if version is not None:
            self.version = version
        if vcpus is not None:
            self.vcpus = vcpus
        if ram is not None:
            self.ram = ram
        if spec_code is not None:
            self.spec_code = spec_code
        if group_type is not None:
            self.group_type = group_type
        if availability_zones is not None:
            self.availability_zones = availability_zones

    @property
    def id(self):
        r"""Gets the id of this SupabaseSpecFlavorInfo.

        :return: The id of this SupabaseSpecFlavorInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SupabaseSpecFlavorInfo.

        :param id: The id of this SupabaseSpecFlavorInfo.
        :type id: str
        """
        self._id = id

    @property
    def mode(self):
        r"""Gets the mode of this SupabaseSpecFlavorInfo.

        :return: The mode of this SupabaseSpecFlavorInfo.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this SupabaseSpecFlavorInfo.

        :param mode: The mode of this SupabaseSpecFlavorInfo.
        :type mode: str
        """
        self._mode = mode

    @property
    def version(self):
        r"""Gets the version of this SupabaseSpecFlavorInfo.

        :return: The version of this SupabaseSpecFlavorInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this SupabaseSpecFlavorInfo.

        :param version: The version of this SupabaseSpecFlavorInfo.
        :type version: str
        """
        self._version = version

    @property
    def vcpus(self):
        r"""Gets the vcpus of this SupabaseSpecFlavorInfo.

        :return: The vcpus of this SupabaseSpecFlavorInfo.
        :rtype: int
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        r"""Sets the vcpus of this SupabaseSpecFlavorInfo.

        :param vcpus: The vcpus of this SupabaseSpecFlavorInfo.
        :type vcpus: int
        """
        self._vcpus = vcpus

    @property
    def ram(self):
        r"""Gets the ram of this SupabaseSpecFlavorInfo.

        :return: The ram of this SupabaseSpecFlavorInfo.
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        r"""Sets the ram of this SupabaseSpecFlavorInfo.

        :param ram: The ram of this SupabaseSpecFlavorInfo.
        :type ram: int
        """
        self._ram = ram

    @property
    def spec_code(self):
        r"""Gets the spec_code of this SupabaseSpecFlavorInfo.

        :return: The spec_code of this SupabaseSpecFlavorInfo.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this SupabaseSpecFlavorInfo.

        :param spec_code: The spec_code of this SupabaseSpecFlavorInfo.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def group_type(self):
        r"""Gets the group_type of this SupabaseSpecFlavorInfo.

        :return: The group_type of this SupabaseSpecFlavorInfo.
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        r"""Sets the group_type of this SupabaseSpecFlavorInfo.

        :param group_type: The group_type of this SupabaseSpecFlavorInfo.
        :type group_type: str
        """
        self._group_type = group_type

    @property
    def availability_zones(self):
        r"""Gets the availability_zones of this SupabaseSpecFlavorInfo.

        :return: The availability_zones of this SupabaseSpecFlavorInfo.
        :rtype: list[:class:`huaweicloudsdkrds.v3.SupabaseSpecFlavorInfoAvailabilityZones`]
        """
        return self._availability_zones

    @availability_zones.setter
    def availability_zones(self, availability_zones):
        r"""Sets the availability_zones of this SupabaseSpecFlavorInfo.

        :param availability_zones: The availability_zones of this SupabaseSpecFlavorInfo.
        :type availability_zones: list[:class:`huaweicloudsdkrds.v3.SupabaseSpecFlavorInfoAvailabilityZones`]
        """
        self._availability_zones = availability_zones

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
        if not isinstance(other, SupabaseSpecFlavorInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
