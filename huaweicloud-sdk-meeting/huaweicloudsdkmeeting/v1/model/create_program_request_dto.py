# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateProgramRequestDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'program_name': 'str',
        'program_item_list': 'list[ProgramItemRequestBase]'
    }

    attribute_map = {
        'program_name': 'programName',
        'program_item_list': 'programItemList'
    }

    def __init__(self, program_name=None, program_item_list=None):
        r"""CreateProgramRequestDTO

        The model defined in huaweicloud sdk

        :param program_name: 节目名称。
        :type program_name: str
        :param program_item_list: 节目素材列表。
        :type program_item_list: list[:class:`huaweicloudsdkmeeting.v1.ProgramItemRequestBase`]
        """
        
        

        self._program_name = None
        self._program_item_list = None
        self.discriminator = None

        self.program_name = program_name
        if program_item_list is not None:
            self.program_item_list = program_item_list

    @property
    def program_name(self):
        r"""Gets the program_name of this CreateProgramRequestDTO.

        节目名称。

        :return: The program_name of this CreateProgramRequestDTO.
        :rtype: str
        """
        return self._program_name

    @program_name.setter
    def program_name(self, program_name):
        r"""Sets the program_name of this CreateProgramRequestDTO.

        节目名称。

        :param program_name: The program_name of this CreateProgramRequestDTO.
        :type program_name: str
        """
        self._program_name = program_name

    @property
    def program_item_list(self):
        r"""Gets the program_item_list of this CreateProgramRequestDTO.

        节目素材列表。

        :return: The program_item_list of this CreateProgramRequestDTO.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.ProgramItemRequestBase`]
        """
        return self._program_item_list

    @program_item_list.setter
    def program_item_list(self, program_item_list):
        r"""Sets the program_item_list of this CreateProgramRequestDTO.

        节目素材列表。

        :param program_item_list: The program_item_list of this CreateProgramRequestDTO.
        :type program_item_list: list[:class:`huaweicloudsdkmeeting.v1.ProgramItemRequestBase`]
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
        if not isinstance(other, CreateProgramRequestDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
