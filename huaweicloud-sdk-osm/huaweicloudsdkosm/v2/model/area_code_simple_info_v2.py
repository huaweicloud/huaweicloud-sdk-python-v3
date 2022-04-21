# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AreaCodeSimpleInfoV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'area_code': 'str',
        'area_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'area_code': 'area_code',
        'area_name': 'area_name'
    }

    def __init__(self, id=None, area_code=None, area_name=None):
        """AreaCodeSimpleInfoV2

        The model defined in huaweicloud sdk

        :param id: 唯一id
        :type id: int
        :param area_code: 国家码
        :type area_code: str
        :param area_name: 国家名称
        :type area_name: str
        """
        
        

        self._id = None
        self._area_code = None
        self._area_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if area_code is not None:
            self.area_code = area_code
        if area_name is not None:
            self.area_name = area_name

    @property
    def id(self):
        """Gets the id of this AreaCodeSimpleInfoV2.

        唯一id

        :return: The id of this AreaCodeSimpleInfoV2.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AreaCodeSimpleInfoV2.

        唯一id

        :param id: The id of this AreaCodeSimpleInfoV2.
        :type id: int
        """
        self._id = id

    @property
    def area_code(self):
        """Gets the area_code of this AreaCodeSimpleInfoV2.

        国家码

        :return: The area_code of this AreaCodeSimpleInfoV2.
        :rtype: str
        """
        return self._area_code

    @area_code.setter
    def area_code(self, area_code):
        """Sets the area_code of this AreaCodeSimpleInfoV2.

        国家码

        :param area_code: The area_code of this AreaCodeSimpleInfoV2.
        :type area_code: str
        """
        self._area_code = area_code

    @property
    def area_name(self):
        """Gets the area_name of this AreaCodeSimpleInfoV2.

        国家名称

        :return: The area_name of this AreaCodeSimpleInfoV2.
        :rtype: str
        """
        return self._area_name

    @area_name.setter
    def area_name(self, area_name):
        """Sets the area_name of this AreaCodeSimpleInfoV2.

        国家名称

        :param area_name: The area_name of this AreaCodeSimpleInfoV2.
        :type area_name: str
        """
        self._area_name = area_name

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
        if not isinstance(other, AreaCodeSimpleInfoV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
