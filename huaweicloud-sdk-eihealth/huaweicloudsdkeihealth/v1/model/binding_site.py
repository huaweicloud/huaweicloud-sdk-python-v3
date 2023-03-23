# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BindingSite:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protein': 'str',
        'bounding_box': 'BoundingBox'
    }

    attribute_map = {
        'protein': 'protein',
        'bounding_box': 'bounding_box'
    }

    def __init__(self, protein=None, bounding_box=None):
        """BindingSite

        The model defined in huaweicloud sdk

        :param protein: 蛋白质3D结构，使用gzip压缩然后转base64格式
        :type protein: str
        :param bounding_box: 
        :type bounding_box: :class:`huaweicloudsdkeihealth.v1.BoundingBox`
        """
        
        

        self._protein = None
        self._bounding_box = None
        self.discriminator = None

        if protein is not None:
            self.protein = protein
        if bounding_box is not None:
            self.bounding_box = bounding_box

    @property
    def protein(self):
        """Gets the protein of this BindingSite.

        蛋白质3D结构，使用gzip压缩然后转base64格式

        :return: The protein of this BindingSite.
        :rtype: str
        """
        return self._protein

    @protein.setter
    def protein(self, protein):
        """Sets the protein of this BindingSite.

        蛋白质3D结构，使用gzip压缩然后转base64格式

        :param protein: The protein of this BindingSite.
        :type protein: str
        """
        self._protein = protein

    @property
    def bounding_box(self):
        """Gets the bounding_box of this BindingSite.

        :return: The bounding_box of this BindingSite.
        :rtype: :class:`huaweicloudsdkeihealth.v1.BoundingBox`
        """
        return self._bounding_box

    @bounding_box.setter
    def bounding_box(self, bounding_box):
        """Sets the bounding_box of this BindingSite.

        :param bounding_box: The bounding_box of this BindingSite.
        :type bounding_box: :class:`huaweicloudsdkeihealth.v1.BoundingBox`
        """
        self._bounding_box = bounding_box

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
        if not isinstance(other, BindingSite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
