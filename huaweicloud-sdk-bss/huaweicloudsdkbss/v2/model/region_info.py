# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RegionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region_code': 'str',
        'region_name': 'str'
    }

    attribute_map = {
        'region_code': 'region_code',
        'region_name': 'region_name'
    }

    def __init__(self, region_code=None, region_name=None):
        r"""RegionInfo

        The model defined in huaweicloud sdk

        :param region_code: 云服务区编码
        :type region_code: str
        :param region_name: 云服务区名称
        :type region_name: str
        """
        
        

        self._region_code = None
        self._region_name = None
        self.discriminator = None

        if region_code is not None:
            self.region_code = region_code
        if region_name is not None:
            self.region_name = region_name

    @property
    def region_code(self):
        r"""Gets the region_code of this RegionInfo.

        云服务区编码

        :return: The region_code of this RegionInfo.
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        r"""Sets the region_code of this RegionInfo.

        云服务区编码

        :param region_code: The region_code of this RegionInfo.
        :type region_code: str
        """
        self._region_code = region_code

    @property
    def region_name(self):
        r"""Gets the region_name of this RegionInfo.

        云服务区名称

        :return: The region_name of this RegionInfo.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        r"""Sets the region_name of this RegionInfo.

        云服务区名称

        :param region_name: The region_name of this RegionInfo.
        :type region_name: str
        """
        self._region_name = region_name

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
        if not isinstance(other, RegionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
