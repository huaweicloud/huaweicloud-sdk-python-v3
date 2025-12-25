# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AreaId:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'area_id': 'str'
    }

    attribute_map = {
        'area_id': 'area_id'
    }

    def __init__(self, area_id=None):
        r"""AreaId

        The model defined in huaweicloud sdk

        :param area_id: 大区。云连接支持的大区有： - Chinese-Mainland（中国大陆） - Asia-Pacific（亚太） - Africa（非洲） - Western-Latin-America（拉美西） - Eastern-Latin-America（拉美东） - Northern-Latin-America（拉美北）
        :type area_id: str
        """
        
        

        self._area_id = None
        self.discriminator = None

        self.area_id = area_id

    @property
    def area_id(self):
        r"""Gets the area_id of this AreaId.

        大区。云连接支持的大区有： - Chinese-Mainland（中国大陆） - Asia-Pacific（亚太） - Africa（非洲） - Western-Latin-America（拉美西） - Eastern-Latin-America（拉美东） - Northern-Latin-America（拉美北）

        :return: The area_id of this AreaId.
        :rtype: str
        """
        return self._area_id

    @area_id.setter
    def area_id(self, area_id):
        r"""Sets the area_id of this AreaId.

        大区。云连接支持的大区有： - Chinese-Mainland（中国大陆） - Asia-Pacific（亚太） - Africa（非洲） - Western-Latin-America（拉美西） - Eastern-Latin-America（拉美东） - Northern-Latin-America（拉美北）

        :param area_id: The area_id of this AreaId.
        :type area_id: str
        """
        self._area_id = area_id

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
        if not isinstance(other, AreaId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
