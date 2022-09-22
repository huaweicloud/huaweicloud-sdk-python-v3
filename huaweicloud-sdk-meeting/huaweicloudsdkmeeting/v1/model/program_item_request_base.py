# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProgramItemRequestBase:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'material_id': 'str',
        'play_time': 'int'
    }

    attribute_map = {
        'material_id': 'materialId',
        'play_time': 'playTime'
    }

    def __init__(self, material_id=None, play_time=None):
        """ProgramItemRequestBase

        The model defined in huaweicloud sdk

        :param material_id: 素材ID。
        :type material_id: str
        :param play_time: 播放时长。
        :type play_time: int
        """
        
        

        self._material_id = None
        self._play_time = None
        self.discriminator = None

        self.material_id = material_id
        self.play_time = play_time

    @property
    def material_id(self):
        """Gets the material_id of this ProgramItemRequestBase.

        素材ID。

        :return: The material_id of this ProgramItemRequestBase.
        :rtype: str
        """
        return self._material_id

    @material_id.setter
    def material_id(self, material_id):
        """Sets the material_id of this ProgramItemRequestBase.

        素材ID。

        :param material_id: The material_id of this ProgramItemRequestBase.
        :type material_id: str
        """
        self._material_id = material_id

    @property
    def play_time(self):
        """Gets the play_time of this ProgramItemRequestBase.

        播放时长。

        :return: The play_time of this ProgramItemRequestBase.
        :rtype: int
        """
        return self._play_time

    @play_time.setter
    def play_time(self, play_time):
        """Sets the play_time of this ProgramItemRequestBase.

        播放时长。

        :param play_time: The play_time of this ProgramItemRequestBase.
        :type play_time: int
        """
        self._play_time = play_time

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
        if not isinstance(other, ProgramItemRequestBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
