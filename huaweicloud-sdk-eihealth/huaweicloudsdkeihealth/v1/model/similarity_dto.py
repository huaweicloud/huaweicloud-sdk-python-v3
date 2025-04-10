# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SimilarityDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ligand_ids': 'list[str]'
    }

    attribute_map = {
        'ligand_ids': 'ligand_ids'
    }

    def __init__(self, ligand_ids=None):
        r"""SimilarityDto

        The model defined in huaweicloud sdk

        :param ligand_ids: 配体对
        :type ligand_ids: list[str]
        """
        
        

        self._ligand_ids = None
        self.discriminator = None

        self.ligand_ids = ligand_ids

    @property
    def ligand_ids(self):
        r"""Gets the ligand_ids of this SimilarityDto.

        配体对

        :return: The ligand_ids of this SimilarityDto.
        :rtype: list[str]
        """
        return self._ligand_ids

    @ligand_ids.setter
    def ligand_ids(self, ligand_ids):
        r"""Sets the ligand_ids of this SimilarityDto.

        配体对

        :param ligand_ids: The ligand_ids of this SimilarityDto.
        :type ligand_ids: list[str]
        """
        self._ligand_ids = ligand_ids

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
        if not isinstance(other, SimilarityDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
