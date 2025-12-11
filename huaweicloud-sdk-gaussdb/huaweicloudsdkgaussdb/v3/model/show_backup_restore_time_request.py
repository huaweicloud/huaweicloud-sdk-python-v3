# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBackupRestoreTimeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'instance_id': 'str',
        'date': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'date': 'date',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, x_language=None, instance_id=None, date=None, start_time=None, end_time=None):
        r"""ShowBackupRestoreTimeRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言。
        :type x_language: str
        :param instance_id: 租户在某一project下的实例ID。
        :type instance_id: str
        :param date: **参数解释**：  所需查询的日期。  **约束限制**：  不涉及。  **取值范围**：  yyyy-mm-dd字符串格式，时区为UTC。  **默认取值**：  不涉及。
        :type date: str
        :param start_time: **参数解释**：  所需查询的起始时间戳。  **约束限制**：  - “start_time”有值时，“end_time”必选。 - “date”有值时，“start_time”失效。  **取值范围**：  格式为UNIX时间戳，单位是毫秒，时区为UTC标准时区。传参时需要将对应时区的时间转为标准时区对应的时间戳，比如，北京时区的时间点需要-8h后再转为时间戳。  **默认取值**：  不涉及。
        :type start_time: str
        :param end_time: **参数解释**：  所需查询的结束时间戳。  **约束限制**：  - “end_time”有值时，“start_time”必选。 - “date”有值时，“end_time”失效。  **取值范围**：  格式为UNIX时间戳，单位是毫秒，时区为UTC标准时区。传参时需要将对应时区的时间转为标准时区对应的时间戳，比如，北京时区的时间点需要-8h后再转为时间戳。  **默认取值**：  不涉及。
        :type end_time: str
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._date = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        if date is not None:
            self.date = date
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowBackupRestoreTimeRequest.

        语言。

        :return: The x_language of this ShowBackupRestoreTimeRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowBackupRestoreTimeRequest.

        语言。

        :param x_language: The x_language of this ShowBackupRestoreTimeRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowBackupRestoreTimeRequest.

        租户在某一project下的实例ID。

        :return: The instance_id of this ShowBackupRestoreTimeRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowBackupRestoreTimeRequest.

        租户在某一project下的实例ID。

        :param instance_id: The instance_id of this ShowBackupRestoreTimeRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def date(self):
        r"""Gets the date of this ShowBackupRestoreTimeRequest.

        **参数解释**：  所需查询的日期。  **约束限制**：  不涉及。  **取值范围**：  yyyy-mm-dd字符串格式，时区为UTC。  **默认取值**：  不涉及。

        :return: The date of this ShowBackupRestoreTimeRequest.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this ShowBackupRestoreTimeRequest.

        **参数解释**：  所需查询的日期。  **约束限制**：  不涉及。  **取值范围**：  yyyy-mm-dd字符串格式，时区为UTC。  **默认取值**：  不涉及。

        :param date: The date of this ShowBackupRestoreTimeRequest.
        :type date: str
        """
        self._date = date

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowBackupRestoreTimeRequest.

        **参数解释**：  所需查询的起始时间戳。  **约束限制**：  - “start_time”有值时，“end_time”必选。 - “date”有值时，“start_time”失效。  **取值范围**：  格式为UNIX时间戳，单位是毫秒，时区为UTC标准时区。传参时需要将对应时区的时间转为标准时区对应的时间戳，比如，北京时区的时间点需要-8h后再转为时间戳。  **默认取值**：  不涉及。

        :return: The start_time of this ShowBackupRestoreTimeRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowBackupRestoreTimeRequest.

        **参数解释**：  所需查询的起始时间戳。  **约束限制**：  - “start_time”有值时，“end_time”必选。 - “date”有值时，“start_time”失效。  **取值范围**：  格式为UNIX时间戳，单位是毫秒，时区为UTC标准时区。传参时需要将对应时区的时间转为标准时区对应的时间戳，比如，北京时区的时间点需要-8h后再转为时间戳。  **默认取值**：  不涉及。

        :param start_time: The start_time of this ShowBackupRestoreTimeRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowBackupRestoreTimeRequest.

        **参数解释**：  所需查询的结束时间戳。  **约束限制**：  - “end_time”有值时，“start_time”必选。 - “date”有值时，“end_time”失效。  **取值范围**：  格式为UNIX时间戳，单位是毫秒，时区为UTC标准时区。传参时需要将对应时区的时间转为标准时区对应的时间戳，比如，北京时区的时间点需要-8h后再转为时间戳。  **默认取值**：  不涉及。

        :return: The end_time of this ShowBackupRestoreTimeRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowBackupRestoreTimeRequest.

        **参数解释**：  所需查询的结束时间戳。  **约束限制**：  - “end_time”有值时，“start_time”必选。 - “date”有值时，“end_time”失效。  **取值范围**：  格式为UNIX时间戳，单位是毫秒，时区为UTC标准时区。传参时需要将对应时区的时间转为标准时区对应的时间戳，比如，北京时区的时间点需要-8h后再转为时间戳。  **默认取值**：  不涉及。

        :param end_time: The end_time of this ShowBackupRestoreTimeRequest.
        :type end_time: str
        """
        self._end_time = end_time

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowBackupRestoreTimeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
