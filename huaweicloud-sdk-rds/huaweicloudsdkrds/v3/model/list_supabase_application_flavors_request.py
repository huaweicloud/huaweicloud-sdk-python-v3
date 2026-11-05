# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSupabaseApplicationFlavorsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'version': 'str',
        'spec_code': 'str',
        'az_code': 'str',
        'is_free': 'bool',
        'mode': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'version': 'version',
        'spec_code': 'spec_code',
        'az_code': 'az_code',
        'is_free': 'is_free',
        'mode': 'mode'
    }

    def __init__(self, x_language=None, version=None, spec_code=None, az_code=None, is_free=None, mode=None):
        r"""ListSupabaseApplicationFlavorsRequest

        The model defined in huaweicloud sdk

        :param x_language: 
        :type x_language: str
        :param version: 
        :type version: str
        :param spec_code: 
        :type spec_code: str
        :param az_code: 
        :type az_code: str
        :param is_free: 
        :type is_free: bool
        :param mode: 
        :type mode: str
        """
        
        

        self._x_language = None
        self._version = None
        self._spec_code = None
        self._az_code = None
        self._is_free = None
        self._mode = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if version is not None:
            self.version = version
        if spec_code is not None:
            self.spec_code = spec_code
        if az_code is not None:
            self.az_code = az_code
        if is_free is not None:
            self.is_free = is_free
        if mode is not None:
            self.mode = mode

    @property
    def x_language(self):
        r"""Gets the x_language of this ListSupabaseApplicationFlavorsRequest.

        :return: The x_language of this ListSupabaseApplicationFlavorsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListSupabaseApplicationFlavorsRequest.

        :param x_language: The x_language of this ListSupabaseApplicationFlavorsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def version(self):
        r"""Gets the version of this ListSupabaseApplicationFlavorsRequest.

        :return: The version of this ListSupabaseApplicationFlavorsRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ListSupabaseApplicationFlavorsRequest.

        :param version: The version of this ListSupabaseApplicationFlavorsRequest.
        :type version: str
        """
        self._version = version

    @property
    def spec_code(self):
        r"""Gets the spec_code of this ListSupabaseApplicationFlavorsRequest.

        :return: The spec_code of this ListSupabaseApplicationFlavorsRequest.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this ListSupabaseApplicationFlavorsRequest.

        :param spec_code: The spec_code of this ListSupabaseApplicationFlavorsRequest.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def az_code(self):
        r"""Gets the az_code of this ListSupabaseApplicationFlavorsRequest.

        :return: The az_code of this ListSupabaseApplicationFlavorsRequest.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        r"""Sets the az_code of this ListSupabaseApplicationFlavorsRequest.

        :param az_code: The az_code of this ListSupabaseApplicationFlavorsRequest.
        :type az_code: str
        """
        self._az_code = az_code

    @property
    def is_free(self):
        r"""Gets the is_free of this ListSupabaseApplicationFlavorsRequest.

        :return: The is_free of this ListSupabaseApplicationFlavorsRequest.
        :rtype: bool
        """
        return self._is_free

    @is_free.setter
    def is_free(self, is_free):
        r"""Sets the is_free of this ListSupabaseApplicationFlavorsRequest.

        :param is_free: The is_free of this ListSupabaseApplicationFlavorsRequest.
        :type is_free: bool
        """
        self._is_free = is_free

    @property
    def mode(self):
        r"""Gets the mode of this ListSupabaseApplicationFlavorsRequest.

        :return: The mode of this ListSupabaseApplicationFlavorsRequest.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this ListSupabaseApplicationFlavorsRequest.

        :param mode: The mode of this ListSupabaseApplicationFlavorsRequest.
        :type mode: str
        """
        self._mode = mode

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
        if not isinstance(other, ListSupabaseApplicationFlavorsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
