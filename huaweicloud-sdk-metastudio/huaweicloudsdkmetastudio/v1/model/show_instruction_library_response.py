# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstructionLibraryResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instruction_library_id': 'str',
        'name': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'instruction_library_id': 'instruction_library_id',
        'name': 'name',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, instruction_library_id=None, name=None, create_time=None, update_time=None, x_request_id=None):
        r"""ShowInstructionLibraryResponse

        The model defined in huaweicloud sdk

        :param instruction_library_id: 指令集ID。
        :type instruction_library_id: str
        :param name: 指令集名称。
        :type name: str
        :param create_time: 创建时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type create_time: str
        :param update_time: 更新时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type update_time: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowInstructionLibraryResponse, self).__init__()

        self._instruction_library_id = None
        self._name = None
        self._create_time = None
        self._update_time = None
        self._x_request_id = None
        self.discriminator = None

        if instruction_library_id is not None:
            self.instruction_library_id = instruction_library_id
        if name is not None:
            self.name = name
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def instruction_library_id(self):
        r"""Gets the instruction_library_id of this ShowInstructionLibraryResponse.

        指令集ID。

        :return: The instruction_library_id of this ShowInstructionLibraryResponse.
        :rtype: str
        """
        return self._instruction_library_id

    @instruction_library_id.setter
    def instruction_library_id(self, instruction_library_id):
        r"""Sets the instruction_library_id of this ShowInstructionLibraryResponse.

        指令集ID。

        :param instruction_library_id: The instruction_library_id of this ShowInstructionLibraryResponse.
        :type instruction_library_id: str
        """
        self._instruction_library_id = instruction_library_id

    @property
    def name(self):
        r"""Gets the name of this ShowInstructionLibraryResponse.

        指令集名称。

        :return: The name of this ShowInstructionLibraryResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowInstructionLibraryResponse.

        指令集名称。

        :param name: The name of this ShowInstructionLibraryResponse.
        :type name: str
        """
        self._name = name

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowInstructionLibraryResponse.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The create_time of this ShowInstructionLibraryResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowInstructionLibraryResponse.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param create_time: The create_time of this ShowInstructionLibraryResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowInstructionLibraryResponse.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The update_time of this ShowInstructionLibraryResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowInstructionLibraryResponse.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param update_time: The update_time of this ShowInstructionLibraryResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowInstructionLibraryResponse.

        :return: The x_request_id of this ShowInstructionLibraryResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowInstructionLibraryResponse.

        :param x_request_id: The x_request_id of this ShowInstructionLibraryResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ShowInstructionLibraryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
