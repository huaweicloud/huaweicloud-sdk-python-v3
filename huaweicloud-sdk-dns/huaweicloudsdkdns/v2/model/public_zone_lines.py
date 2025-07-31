# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublicZoneLines:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'line': 'str',
        'line_name': 'str',
        'create_time': 'str'
    }

    attribute_map = {
        'line': 'line',
        'line_name': 'line_name',
        'create_time': 'create_time'
    }

    def __init__(self, line=None, line_name=None, create_time=None):
        r"""PublicZoneLines

        The model defined in huaweicloud sdk

        :param line: **参数解释：** 线路ID。 **取值范围：** 不涉及。
        :type line: str
        :param line_name: **参数解释：** 线路名称。 **取值范围：** 不涉及。
        :type line_name: str
        :param create_time: **参数解释：** 创建时间。 格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS。 **取值范围：** 不涉及。
        :type create_time: str
        """
        
        

        self._line = None
        self._line_name = None
        self._create_time = None
        self.discriminator = None

        if line is not None:
            self.line = line
        if line_name is not None:
            self.line_name = line_name
        if create_time is not None:
            self.create_time = create_time

    @property
    def line(self):
        r"""Gets the line of this PublicZoneLines.

        **参数解释：** 线路ID。 **取值范围：** 不涉及。

        :return: The line of this PublicZoneLines.
        :rtype: str
        """
        return self._line

    @line.setter
    def line(self, line):
        r"""Sets the line of this PublicZoneLines.

        **参数解释：** 线路ID。 **取值范围：** 不涉及。

        :param line: The line of this PublicZoneLines.
        :type line: str
        """
        self._line = line

    @property
    def line_name(self):
        r"""Gets the line_name of this PublicZoneLines.

        **参数解释：** 线路名称。 **取值范围：** 不涉及。

        :return: The line_name of this PublicZoneLines.
        :rtype: str
        """
        return self._line_name

    @line_name.setter
    def line_name(self, line_name):
        r"""Sets the line_name of this PublicZoneLines.

        **参数解释：** 线路名称。 **取值范围：** 不涉及。

        :param line_name: The line_name of this PublicZoneLines.
        :type line_name: str
        """
        self._line_name = line_name

    @property
    def create_time(self):
        r"""Gets the create_time of this PublicZoneLines.

        **参数解释：** 创建时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。 **取值范围：** 不涉及。

        :return: The create_time of this PublicZoneLines.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this PublicZoneLines.

        **参数解释：** 创建时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。 **取值范围：** 不涉及。

        :param create_time: The create_time of this PublicZoneLines.
        :type create_time: str
        """
        self._create_time = create_time

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
        if not isinstance(other, PublicZoneLines):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
