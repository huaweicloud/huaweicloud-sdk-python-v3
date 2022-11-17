# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProgramResponse(SdkResponse):

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
        'play_time': 'int',
        'program_item_list': 'list[ProgramItemResponseBase]'
    }

    attribute_map = {
        'id': 'id',
        'last_updated_by': 'lastUpdatedBy',
        'update_time': 'updateTime',
        'program_name': 'programName',
        'material_size_str': 'materialSizeStr',
        'play_time': 'playTime',
        'program_item_list': 'programItemList'
    }

    def __init__(self, id=None, last_updated_by=None, update_time=None, program_name=None, material_size_str=None, play_time=None, program_item_list=None):
        """ShowProgramResponse

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
        :param program_item_list: 节目素材列表。
        :type program_item_list: list[:class:`huaweicloudsdkmeeting.v1.ProgramItemResponseBase`]
        """
        
        super(ShowProgramResponse, self).__init__()

        self._id = None
        self._last_updated_by = None
        self._update_time = None
        self._program_name = None
        self._material_size_str = None
        self._play_time = None
        self._program_item_list = None
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
        if program_item_list is not None:
            self.program_item_list = program_item_list

    @property
    def id(self):
        """Gets the id of this ShowProgramResponse.

        节目ID。

        :return: The id of this ShowProgramResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowProgramResponse.

        节目ID。

        :param id: The id of this ShowProgramResponse.
        :type id: str
        """
        self._id = id

    @property
    def last_updated_by(self):
        """Gets the last_updated_by of this ShowProgramResponse.

        更新者。

        :return: The last_updated_by of this ShowProgramResponse.
        :rtype: str
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, last_updated_by):
        """Sets the last_updated_by of this ShowProgramResponse.

        更新者。

        :param last_updated_by: The last_updated_by of this ShowProgramResponse.
        :type last_updated_by: str
        """
        self._last_updated_by = last_updated_by

    @property
    def update_time(self):
        """Gets the update_time of this ShowProgramResponse.

        更新时间。

        :return: The update_time of this ShowProgramResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowProgramResponse.

        更新时间。

        :param update_time: The update_time of this ShowProgramResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def program_name(self):
        """Gets the program_name of this ShowProgramResponse.

        节目名称。

        :return: The program_name of this ShowProgramResponse.
        :rtype: str
        """
        return self._program_name

    @program_name.setter
    def program_name(self, program_name):
        """Sets the program_name of this ShowProgramResponse.

        节目名称。

        :param program_name: The program_name of this ShowProgramResponse.
        :type program_name: str
        """
        self._program_name = program_name

    @property
    def material_size_str(self):
        """Gets the material_size_str of this ShowProgramResponse.

        节目的总素材大小（含单位）。

        :return: The material_size_str of this ShowProgramResponse.
        :rtype: str
        """
        return self._material_size_str

    @material_size_str.setter
    def material_size_str(self, material_size_str):
        """Sets the material_size_str of this ShowProgramResponse.

        节目的总素材大小（含单位）。

        :param material_size_str: The material_size_str of this ShowProgramResponse.
        :type material_size_str: str
        """
        self._material_size_str = material_size_str

    @property
    def play_time(self):
        """Gets the play_time of this ShowProgramResponse.

        节目的总播放时长，单位秒。

        :return: The play_time of this ShowProgramResponse.
        :rtype: int
        """
        return self._play_time

    @play_time.setter
    def play_time(self, play_time):
        """Sets the play_time of this ShowProgramResponse.

        节目的总播放时长，单位秒。

        :param play_time: The play_time of this ShowProgramResponse.
        :type play_time: int
        """
        self._play_time = play_time

    @property
    def program_item_list(self):
        """Gets the program_item_list of this ShowProgramResponse.

        节目素材列表。

        :return: The program_item_list of this ShowProgramResponse.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.ProgramItemResponseBase`]
        """
        return self._program_item_list

    @program_item_list.setter
    def program_item_list(self, program_item_list):
        """Sets the program_item_list of this ShowProgramResponse.

        节目素材列表。

        :param program_item_list: The program_item_list of this ShowProgramResponse.
        :type program_item_list: list[:class:`huaweicloudsdkmeeting.v1.ProgramItemResponseBase`]
        """
        self._program_item_list = program_item_list

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
        if not isinstance(other, ShowProgramResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
