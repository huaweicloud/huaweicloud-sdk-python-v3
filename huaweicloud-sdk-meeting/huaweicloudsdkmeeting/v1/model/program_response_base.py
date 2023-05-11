# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProgramResponseBase:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'last_updated_by': 'str',
        'update_time': 'int',
        'program_name': 'str',
        'material_size_str': 'str',
        'play_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'last_updated_by': 'lastUpdatedBy',
        'update_time': 'updateTime',
        'program_name': 'programName',
        'material_size_str': 'materialSizeStr',
        'play_time': 'playTime'
    }

    def __init__(self, id=None, last_updated_by=None, update_time=None, program_name=None, material_size_str=None, play_time=None):
        """ProgramResponseBase

        The model defined in huaweicloud sdk

        :param id: 节目ID。
        :type id: str
        :param last_updated_by: 更新者。
        :type last_updated_by: str
        :param update_time: 更新时间。
        :type update_time: int
        :param program_name: 节目名称。
        :type program_name: str
        :param material_size_str: 节目的总素材大小（含单位）。
        :type material_size_str: str
        :param play_time: 节目的总播放时长，单位秒。
        :type play_time: int
        """
        
        

        self._id = None
        self._last_updated_by = None
        self._update_time = None
        self._program_name = None
        self._material_size_str = None
        self._play_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if last_updated_by is not None:
            self.last_updated_by = last_updated_by
        if update_time is not None:
            self.update_time = update_time
        if program_name is not None:
            self.program_name = program_name
        if material_size_str is not None:
            self.material_size_str = material_size_str
        if play_time is not None:
            self.play_time = play_time

    @property
    def id(self):
        """Gets the id of this ProgramResponseBase.

        节目ID。

        :return: The id of this ProgramResponseBase.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProgramResponseBase.

        节目ID。

        :param id: The id of this ProgramResponseBase.
        :type id: str
        """
        self._id = id

    @property
    def last_updated_by(self):
        """Gets the last_updated_by of this ProgramResponseBase.

        更新者。

        :return: The last_updated_by of this ProgramResponseBase.
        :rtype: str
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, last_updated_by):
        """Sets the last_updated_by of this ProgramResponseBase.

        更新者。

        :param last_updated_by: The last_updated_by of this ProgramResponseBase.
        :type last_updated_by: str
        """
        self._last_updated_by = last_updated_by

    @property
    def update_time(self):
        """Gets the update_time of this ProgramResponseBase.

        更新时间。

        :return: The update_time of this ProgramResponseBase.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ProgramResponseBase.

        更新时间。

        :param update_time: The update_time of this ProgramResponseBase.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def program_name(self):
        """Gets the program_name of this ProgramResponseBase.

        节目名称。

        :return: The program_name of this ProgramResponseBase.
        :rtype: str
        """
        return self._program_name

    @program_name.setter
    def program_name(self, program_name):
        """Sets the program_name of this ProgramResponseBase.

        节目名称。

        :param program_name: The program_name of this ProgramResponseBase.
        :type program_name: str
        """
        self._program_name = program_name

    @property
    def material_size_str(self):
        """Gets the material_size_str of this ProgramResponseBase.

        节目的总素材大小（含单位）。

        :return: The material_size_str of this ProgramResponseBase.
        :rtype: str
        """
        return self._material_size_str

    @material_size_str.setter
    def material_size_str(self, material_size_str):
        """Sets the material_size_str of this ProgramResponseBase.

        节目的总素材大小（含单位）。

        :param material_size_str: The material_size_str of this ProgramResponseBase.
        :type material_size_str: str
        """
        self._material_size_str = material_size_str

    @property
    def play_time(self):
        """Gets the play_time of this ProgramResponseBase.

        节目的总播放时长，单位秒。

        :return: The play_time of this ProgramResponseBase.
        :rtype: int
        """
        return self._play_time

    @play_time.setter
    def play_time(self, play_time):
        """Sets the play_time of this ProgramResponseBase.

        节目的总播放时长，单位秒。

        :param play_time: The play_time of this ProgramResponseBase.
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
        if not isinstance(other, ProgramResponseBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
