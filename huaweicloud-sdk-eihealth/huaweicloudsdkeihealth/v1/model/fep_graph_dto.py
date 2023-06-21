# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FepGraphDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'center_id': 'str',
        'pairs': 'list[SimilarityDto]'
    }

    attribute_map = {
        'center_id': 'center_id',
        'pairs': 'pairs'
    }

    def __init__(self, center_id=None, pairs=None):
        """FepGraphDto

        The model defined in huaweicloud sdk

        :param center_id: 中心配体名称
        :type center_id: str
        :param pairs: 配体对列表
        :type pairs: list[:class:`huaweicloudsdkeihealth.v1.SimilarityDto`]
        """
        
        

        self._center_id = None
        self._pairs = None
        self.discriminator = None

        self.center_id = center_id
        self.pairs = pairs

    @property
    def center_id(self):
        """Gets the center_id of this FepGraphDto.

        中心配体名称

        :return: The center_id of this FepGraphDto.
        :rtype: str
        """
        return self._center_id

    @center_id.setter
    def center_id(self, center_id):
        """Sets the center_id of this FepGraphDto.

        中心配体名称

        :param center_id: The center_id of this FepGraphDto.
        :type center_id: str
        """
        self._center_id = center_id

    @property
    def pairs(self):
        """Gets the pairs of this FepGraphDto.

        配体对列表

        :return: The pairs of this FepGraphDto.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.SimilarityDto`]
        """
        return self._pairs

    @pairs.setter
    def pairs(self, pairs):
        """Sets the pairs of this FepGraphDto.

        配体对列表

        :param pairs: The pairs of this FepGraphDto.
        :type pairs: list[:class:`huaweicloudsdkeihealth.v1.SimilarityDto`]
        """
        self._pairs = pairs

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
        if not isinstance(other, FepGraphDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
