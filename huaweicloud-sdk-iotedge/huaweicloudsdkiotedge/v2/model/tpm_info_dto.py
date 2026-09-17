# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TPMInfoDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'manufacture_id': 'str',
        'spec_version': 'str'
    }

    attribute_map = {
        'manufacture_id': 'manufacture_id',
        'spec_version': 'spec_version'
    }

    def __init__(self, manufacture_id=None, spec_version=None):
        r"""TPMInfoDTO

        The model defined in huaweicloud sdk

        :param manufacture_id: 厂商信息
        :type manufacture_id: str
        :param spec_version: 协议版本
        :type spec_version: str
        """
        
        

        self._manufacture_id = None
        self._spec_version = None
        self.discriminator = None

        if manufacture_id is not None:
            self.manufacture_id = manufacture_id
        if spec_version is not None:
            self.spec_version = spec_version

    @property
    def manufacture_id(self):
        r"""Gets the manufacture_id of this TPMInfoDTO.

        厂商信息

        :return: The manufacture_id of this TPMInfoDTO.
        :rtype: str
        """
        return self._manufacture_id

    @manufacture_id.setter
    def manufacture_id(self, manufacture_id):
        r"""Sets the manufacture_id of this TPMInfoDTO.

        厂商信息

        :param manufacture_id: The manufacture_id of this TPMInfoDTO.
        :type manufacture_id: str
        """
        self._manufacture_id = manufacture_id

    @property
    def spec_version(self):
        r"""Gets the spec_version of this TPMInfoDTO.

        协议版本

        :return: The spec_version of this TPMInfoDTO.
        :rtype: str
        """
        return self._spec_version

    @spec_version.setter
    def spec_version(self, spec_version):
        r"""Sets the spec_version of this TPMInfoDTO.

        协议版本

        :param spec_version: The spec_version of this TPMInfoDTO.
        :type spec_version: str
        """
        self._spec_version = spec_version

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
        if not isinstance(other, TPMInfoDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
