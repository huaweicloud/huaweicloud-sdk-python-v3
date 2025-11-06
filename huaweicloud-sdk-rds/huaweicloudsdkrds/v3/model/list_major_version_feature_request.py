# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMajorVersionFeatureRequest:

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
        'single': 'bool'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'version': 'version',
        'single': 'single'
    }

    def __init__(self, x_language=None, version=None, single=None):
        r"""ListMajorVersionFeatureRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言。
        :type x_language: str
        :param version: 版本，例如：2022_SE, 2022_EE, 2022_WEB。
        :type version: str
        :param single: 是否是单机版。
        :type single: bool
        """
        
        

        self._x_language = None
        self._version = None
        self._single = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.version = version
        self.single = single

    @property
    def x_language(self):
        r"""Gets the x_language of this ListMajorVersionFeatureRequest.

        语言。

        :return: The x_language of this ListMajorVersionFeatureRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListMajorVersionFeatureRequest.

        语言。

        :param x_language: The x_language of this ListMajorVersionFeatureRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def version(self):
        r"""Gets the version of this ListMajorVersionFeatureRequest.

        版本，例如：2022_SE, 2022_EE, 2022_WEB。

        :return: The version of this ListMajorVersionFeatureRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ListMajorVersionFeatureRequest.

        版本，例如：2022_SE, 2022_EE, 2022_WEB。

        :param version: The version of this ListMajorVersionFeatureRequest.
        :type version: str
        """
        self._version = version

    @property
    def single(self):
        r"""Gets the single of this ListMajorVersionFeatureRequest.

        是否是单机版。

        :return: The single of this ListMajorVersionFeatureRequest.
        :rtype: bool
        """
        return self._single

    @single.setter
    def single(self, single):
        r"""Sets the single of this ListMajorVersionFeatureRequest.

        是否是单机版。

        :param single: The single of this ListMajorVersionFeatureRequest.
        :type single: bool
        """
        self._single = single

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
        if not isinstance(other, ListMajorVersionFeatureRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
