# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProgramItemResponseBase:

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
        'material_name': 'str',
        'file_path': 'str',
        'play_time': 'int'
    }

    attribute_map = {
        'material_id': 'materialId',
        'material_name': 'materialName',
        'file_path': 'filePath',
        'play_time': 'playTime'
    }

    def __init__(self, material_id=None, material_name=None, file_path=None, play_time=None):
        """ProgramItemResponseBase

        The model defined in huaweicloud sdk

        :param material_id: 素材ID。
        :type material_id: str
        :param material_name: 素材名称。
        :type material_name: str
        :param file_path: 素材云盘文件下载路径。
        :type file_path: str
        :param play_time: 播放时长。
        :type play_time: int
        """
        
        

        self._material_id = None
        self._material_name = None
        self._file_path = None
        self._play_time = None
        self.discriminator = None

        if material_id is not None:
            self.material_id = material_id
        if material_name is not None:
            self.material_name = material_name
        if file_path is not None:
            self.file_path = file_path
        if play_time is not None:
            self.play_time = play_time

    @property
    def material_id(self):
        """Gets the material_id of this ProgramItemResponseBase.

        素材ID。

        :return: The material_id of this ProgramItemResponseBase.
        :rtype: str
        """
        return self._material_id

    @material_id.setter
    def material_id(self, material_id):
        """Sets the material_id of this ProgramItemResponseBase.

        素材ID。

        :param material_id: The material_id of this ProgramItemResponseBase.
        :type material_id: str
        """
        self._material_id = material_id

    @property
    def material_name(self):
        """Gets the material_name of this ProgramItemResponseBase.

        素材名称。

        :return: The material_name of this ProgramItemResponseBase.
        :rtype: str
        """
        return self._material_name

    @material_name.setter
    def material_name(self, material_name):
        """Sets the material_name of this ProgramItemResponseBase.

        素材名称。

        :param material_name: The material_name of this ProgramItemResponseBase.
        :type material_name: str
        """
        self._material_name = material_name

    @property
    def file_path(self):
        """Gets the file_path of this ProgramItemResponseBase.

        素材云盘文件下载路径。

        :return: The file_path of this ProgramItemResponseBase.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """Sets the file_path of this ProgramItemResponseBase.

        素材云盘文件下载路径。

        :param file_path: The file_path of this ProgramItemResponseBase.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def play_time(self):
        """Gets the play_time of this ProgramItemResponseBase.

        播放时长。

        :return: The play_time of this ProgramItemResponseBase.
        :rtype: int
        """
        return self._play_time

    @play_time.setter
    def play_time(self, play_time):
        """Sets the play_time of this ProgramItemResponseBase.

        播放时长。

        :param play_time: The play_time of this ProgramItemResponseBase.
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
        if not isinstance(other, ProgramItemResponseBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
