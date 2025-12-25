# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LocalAreaId:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'local_area_id': 'str'
    }

    attribute_map = {
        'local_area_id': 'local_area_id'
    }

    def __init__(self, local_area_id=None):
        r"""LocalAreaId

        The model defined in huaweicloud sdk

        :param local_area_id: 本端大区。云连接支持的大区有： - Chinese-Mainland（中国大陆） - Asia-Pacific（亚太） - Africa（非洲） - Western-Latin-America（拉美西） - Eastern-Latin-America（拉美东） - Northern-Latin-America（拉美北）
        :type local_area_id: str
        """
        
        

        self._local_area_id = None
        self.discriminator = None

        self.local_area_id = local_area_id

    @property
    def local_area_id(self):
        r"""Gets the local_area_id of this LocalAreaId.

        本端大区。云连接支持的大区有： - Chinese-Mainland（中国大陆） - Asia-Pacific（亚太） - Africa（非洲） - Western-Latin-America（拉美西） - Eastern-Latin-America（拉美东） - Northern-Latin-America（拉美北）

        :return: The local_area_id of this LocalAreaId.
        :rtype: str
        """
        return self._local_area_id

    @local_area_id.setter
    def local_area_id(self, local_area_id):
        r"""Sets the local_area_id of this LocalAreaId.

        本端大区。云连接支持的大区有： - Chinese-Mainland（中国大陆） - Asia-Pacific（亚太） - Africa（非洲） - Western-Latin-America（拉美西） - Eastern-Latin-America（拉美东） - Northern-Latin-America（拉美北）

        :param local_area_id: The local_area_id of this LocalAreaId.
        :type local_area_id: str
        """
        self._local_area_id = local_area_id

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
        if not isinstance(other, LocalAreaId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
