# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AiguardAtlasBatchDeleteBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'atlas_ids': 'list[str]'
    }

    attribute_map = {
        'atlas_ids': 'atlas_ids'
    }

    def __init__(self, atlas_ids=None):
        r"""AiguardAtlasBatchDeleteBody

        The model defined in huaweicloud sdk

        :param atlas_ids: 图库ID列表
        :type atlas_ids: list[str]
        """
        
        

        self._atlas_ids = None
        self.discriminator = None

        self.atlas_ids = atlas_ids

    @property
    def atlas_ids(self):
        r"""Gets the atlas_ids of this AiguardAtlasBatchDeleteBody.

        图库ID列表

        :return: The atlas_ids of this AiguardAtlasBatchDeleteBody.
        :rtype: list[str]
        """
        return self._atlas_ids

    @atlas_ids.setter
    def atlas_ids(self, atlas_ids):
        r"""Sets the atlas_ids of this AiguardAtlasBatchDeleteBody.

        图库ID列表

        :param atlas_ids: The atlas_ids of this AiguardAtlasBatchDeleteBody.
        :type atlas_ids: list[str]
        """
        self._atlas_ids = atlas_ids

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
        if not isinstance(other, AiguardAtlasBatchDeleteBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
