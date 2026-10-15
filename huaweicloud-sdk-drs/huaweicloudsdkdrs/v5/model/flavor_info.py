# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlavorInfo:

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
        'cloud_service_type': 'str',
        'spec_type_code': 'str',
        'spec_code': 'str'
    }

    attribute_map = {
        'id': 'id',
        'cloud_service_type': 'cloud_service_type',
        'spec_type_code': 'spec_type_code',
        'spec_code': 'spec_code'
    }

    def __init__(self, id=None, cloud_service_type=None, spec_type_code=None, spec_code=None):
        r"""FlavorInfo

        The model defined in huaweicloud sdk

        :param id: 规格id
        :type id: str
        :param cloud_service_type: 云服务类型
        :type cloud_service_type: str
        :param spec_type_code: 规格类型码
        :type spec_type_code: str
        :param spec_code: 规格码
        :type spec_code: str
        """
        
        

        self._id = None
        self._cloud_service_type = None
        self._spec_type_code = None
        self._spec_code = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if cloud_service_type is not None:
            self.cloud_service_type = cloud_service_type
        if spec_type_code is not None:
            self.spec_type_code = spec_type_code
        if spec_code is not None:
            self.spec_code = spec_code

    @property
    def id(self):
        r"""Gets the id of this FlavorInfo.

        规格id

        :return: The id of this FlavorInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this FlavorInfo.

        规格id

        :param id: The id of this FlavorInfo.
        :type id: str
        """
        self._id = id

    @property
    def cloud_service_type(self):
        r"""Gets the cloud_service_type of this FlavorInfo.

        云服务类型

        :return: The cloud_service_type of this FlavorInfo.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        r"""Sets the cloud_service_type of this FlavorInfo.

        云服务类型

        :param cloud_service_type: The cloud_service_type of this FlavorInfo.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def spec_type_code(self):
        r"""Gets the spec_type_code of this FlavorInfo.

        规格类型码

        :return: The spec_type_code of this FlavorInfo.
        :rtype: str
        """
        return self._spec_type_code

    @spec_type_code.setter
    def spec_type_code(self, spec_type_code):
        r"""Sets the spec_type_code of this FlavorInfo.

        规格类型码

        :param spec_type_code: The spec_type_code of this FlavorInfo.
        :type spec_type_code: str
        """
        self._spec_type_code = spec_type_code

    @property
    def spec_code(self):
        r"""Gets the spec_code of this FlavorInfo.

        规格码

        :return: The spec_code of this FlavorInfo.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this FlavorInfo.

        规格码

        :param spec_code: The spec_code of this FlavorInfo.
        :type spec_code: str
        """
        self._spec_code = spec_code

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
        if not isinstance(other, FlavorInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
