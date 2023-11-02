# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PocketMolDesignReceptorDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file': 'ReceptorDrugFile',
        'bounding_box': 'BoundingBoxDto',
        'remove_water': 'bool',
        'remove_ion': 'bool'
    }

    attribute_map = {
        'file': 'file',
        'bounding_box': 'bounding_box',
        'remove_water': 'remove_water',
        'remove_ion': 'remove_ion'
    }

    def __init__(self, file=None, bounding_box=None, remove_water=None, remove_ion=None):
        """PocketMolDesignReceptorDto

        The model defined in huaweicloud sdk

        :param file: 
        :type file: :class:`huaweicloudsdkeihealth.v1.ReceptorDrugFile`
        :param bounding_box: 
        :type bounding_box: :class:`huaweicloudsdkeihealth.v1.BoundingBoxDto`
        :param remove_water: 去水
        :type remove_water: bool
        :param remove_ion: 去离子
        :type remove_ion: bool
        """
        
        

        self._file = None
        self._bounding_box = None
        self._remove_water = None
        self._remove_ion = None
        self.discriminator = None

        self.file = file
        if bounding_box is not None:
            self.bounding_box = bounding_box
        if remove_water is not None:
            self.remove_water = remove_water
        if remove_ion is not None:
            self.remove_ion = remove_ion

    @property
    def file(self):
        """Gets the file of this PocketMolDesignReceptorDto.

        :return: The file of this PocketMolDesignReceptorDto.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ReceptorDrugFile`
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this PocketMolDesignReceptorDto.

        :param file: The file of this PocketMolDesignReceptorDto.
        :type file: :class:`huaweicloudsdkeihealth.v1.ReceptorDrugFile`
        """
        self._file = file

    @property
    def bounding_box(self):
        """Gets the bounding_box of this PocketMolDesignReceptorDto.

        :return: The bounding_box of this PocketMolDesignReceptorDto.
        :rtype: :class:`huaweicloudsdkeihealth.v1.BoundingBoxDto`
        """
        return self._bounding_box

    @bounding_box.setter
    def bounding_box(self, bounding_box):
        """Sets the bounding_box of this PocketMolDesignReceptorDto.

        :param bounding_box: The bounding_box of this PocketMolDesignReceptorDto.
        :type bounding_box: :class:`huaweicloudsdkeihealth.v1.BoundingBoxDto`
        """
        self._bounding_box = bounding_box

    @property
    def remove_water(self):
        """Gets the remove_water of this PocketMolDesignReceptorDto.

        去水

        :return: The remove_water of this PocketMolDesignReceptorDto.
        :rtype: bool
        """
        return self._remove_water

    @remove_water.setter
    def remove_water(self, remove_water):
        """Sets the remove_water of this PocketMolDesignReceptorDto.

        去水

        :param remove_water: The remove_water of this PocketMolDesignReceptorDto.
        :type remove_water: bool
        """
        self._remove_water = remove_water

    @property
    def remove_ion(self):
        """Gets the remove_ion of this PocketMolDesignReceptorDto.

        去离子

        :return: The remove_ion of this PocketMolDesignReceptorDto.
        :rtype: bool
        """
        return self._remove_ion

    @remove_ion.setter
    def remove_ion(self, remove_ion):
        """Sets the remove_ion of this PocketMolDesignReceptorDto.

        去离子

        :param remove_ion: The remove_ion of this PocketMolDesignReceptorDto.
        :type remove_ion: bool
        """
        self._remove_ion = remove_ion

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
        if not isinstance(other, PocketMolDesignReceptorDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
