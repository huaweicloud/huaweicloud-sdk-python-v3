# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Flavor:

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
        'spec_code': 'str',
        'vcpus': 'str',
        'ram': 'str',
        'az_infos': 'list[AvailableZone]'
    }

    attribute_map = {
        'id': 'id',
        'spec_code': 'spec_code',
        'vcpus': 'vcpus',
        'ram': 'ram',
        'az_infos': 'az_infos'
    }

    def __init__(self, id=None, spec_code=None, vcpus=None, ram=None, az_infos=None):
        r"""Flavor

        The model defined in huaweicloud sdk

        :param id: 规格id。
        :type id: str
        :param spec_code: 资源规格编码。
        :type spec_code: str
        :param vcpus: CPU大小。例如：1表示1U。
        :type vcpus: str
        :param ram: 内存大小，单位:GB。
        :type ram: str
        :param az_infos: 可用区信息  normal：在售。 unsupported：暂不支持该规格。 sellout：售罄。
        :type az_infos: list[:class:`huaweicloudsdkddm.v1.AvailableZone`]
        """
        
        

        self._id = None
        self._spec_code = None
        self._vcpus = None
        self._ram = None
        self._az_infos = None
        self.discriminator = None

        self.id = id
        self.spec_code = spec_code
        self.vcpus = vcpus
        self.ram = ram
        self.az_infos = az_infos

    @property
    def id(self):
        r"""Gets the id of this Flavor.

        规格id。

        :return: The id of this Flavor.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Flavor.

        规格id。

        :param id: The id of this Flavor.
        :type id: str
        """
        self._id = id

    @property
    def spec_code(self):
        r"""Gets the spec_code of this Flavor.

        资源规格编码。

        :return: The spec_code of this Flavor.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this Flavor.

        资源规格编码。

        :param spec_code: The spec_code of this Flavor.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def vcpus(self):
        r"""Gets the vcpus of this Flavor.

        CPU大小。例如：1表示1U。

        :return: The vcpus of this Flavor.
        :rtype: str
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        r"""Sets the vcpus of this Flavor.

        CPU大小。例如：1表示1U。

        :param vcpus: The vcpus of this Flavor.
        :type vcpus: str
        """
        self._vcpus = vcpus

    @property
    def ram(self):
        r"""Gets the ram of this Flavor.

        内存大小，单位:GB。

        :return: The ram of this Flavor.
        :rtype: str
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        r"""Sets the ram of this Flavor.

        内存大小，单位:GB。

        :param ram: The ram of this Flavor.
        :type ram: str
        """
        self._ram = ram

    @property
    def az_infos(self):
        r"""Gets the az_infos of this Flavor.

        可用区信息  normal：在售。 unsupported：暂不支持该规格。 sellout：售罄。

        :return: The az_infos of this Flavor.
        :rtype: list[:class:`huaweicloudsdkddm.v1.AvailableZone`]
        """
        return self._az_infos

    @az_infos.setter
    def az_infos(self, az_infos):
        r"""Sets the az_infos of this Flavor.

        可用区信息  normal：在售。 unsupported：暂不支持该规格。 sellout：售罄。

        :param az_infos: The az_infos of this Flavor.
        :type az_infos: list[:class:`huaweicloudsdkddm.v1.AvailableZone`]
        """
        self._az_infos = az_infos

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
        if not isinstance(other, Flavor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
