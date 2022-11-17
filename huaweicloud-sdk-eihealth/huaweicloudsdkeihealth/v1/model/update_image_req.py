# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateImageReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'ImageType',
        'description': 'str',
        'chip_type': 'ImageChipType'
    }

    attribute_map = {
        'type': 'type',
        'description': 'description',
        'chip_type': 'chip_type'
    }

    def __init__(self, type=None, description=None, chip_type=None):
        """UpdateImageReq

        The model defined in huaweicloud sdk

        :param type: 
        :type type: :class:`huaweicloudsdkeihealth.v1.ImageType`
        :param description: 描述信息
        :type description: str
        :param chip_type: 
        :type chip_type: :class:`huaweicloudsdkeihealth.v1.ImageChipType`
        """
        
        

        self._type = None
        self._description = None
        self._chip_type = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if chip_type is not None:
            self.chip_type = chip_type

    @property
    def type(self):
        """Gets the type of this UpdateImageReq.

        :return: The type of this UpdateImageReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ImageType`
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpdateImageReq.

        :param type: The type of this UpdateImageReq.
        :type type: :class:`huaweicloudsdkeihealth.v1.ImageType`
        """
        self._type = type

    @property
    def description(self):
        """Gets the description of this UpdateImageReq.

        描述信息

        :return: The description of this UpdateImageReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateImageReq.

        描述信息

        :param description: The description of this UpdateImageReq.
        :type description: str
        """
        self._description = description

    @property
    def chip_type(self):
        """Gets the chip_type of this UpdateImageReq.

        :return: The chip_type of this UpdateImageReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ImageChipType`
        """
        return self._chip_type

    @chip_type.setter
    def chip_type(self, chip_type):
        """Sets the chip_type of this UpdateImageReq.

        :param chip_type: The chip_type of this UpdateImageReq.
        :type chip_type: :class:`huaweicloudsdkeihealth.v1.ImageChipType`
        """
        self._chip_type = chip_type

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
        if not isinstance(other, UpdateImageReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
