# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventDump:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source': 'str',
        'state': 'str',
        'description': 'str',
        'id': 'str',
        'filename': 'str',
        'obsname': 'str',
        'tenantid': 'str',
        'start': 'int',
        'end': 'int',
        'total': 'int',
        'url': 'str',
        'urltimestamp': 'int',
        'timestamp': 'int'
    }

    attribute_map = {
        'source': 'source',
        'state': 'state',
        'description': 'description',
        'id': 'id',
        'filename': 'filename',
        'obsname': 'obsname',
        'tenantid': 'tenantid',
        'start': 'start',
        'end': 'end',
        'total': 'total',
        'url': 'url',
        'urltimestamp': 'urltimestamp',
        'timestamp': 'timestamp'
    }

    def __init__(self, source=None, state=None, description=None, id=None, filename=None, obsname=None, tenantid=None, start=None, end=None, total=None, url=None, urltimestamp=None, timestamp=None):
        r"""EventDump

        The model defined in huaweicloud sdk

        :param source: 文件来源
        :type source: str
        :param state: 文件状态
        :type state: str
        :param description: 事件描述
        :type description: str
        :param id: 文件id
        :type id: str
        :param filename: 文件名
        :type filename: str
        :param obsname: 文件obs名
        :type obsname: str
        :param tenantid: 租户id
        :type tenantid: str
        :param start: 统计开始时间
        :type start: int
        :param end: 统计截止时间
        :type end: int
        :param total: 总计事件数
        :type total: int
        :param url: 链接
        :type url: str
        :param urltimestamp: 更新url时间戳
        :type urltimestamp: int
        :param timestamp: 文件生成时间戳
        :type timestamp: int
        """
        
        

        self._source = None
        self._state = None
        self._description = None
        self._id = None
        self._filename = None
        self._obsname = None
        self._tenantid = None
        self._start = None
        self._end = None
        self._total = None
        self._url = None
        self._urltimestamp = None
        self._timestamp = None
        self.discriminator = None

        if source is not None:
            self.source = source
        if state is not None:
            self.state = state
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if filename is not None:
            self.filename = filename
        if obsname is not None:
            self.obsname = obsname
        if tenantid is not None:
            self.tenantid = tenantid
        if start is not None:
            self.start = start
        if end is not None:
            self.end = end
        if total is not None:
            self.total = total
        if url is not None:
            self.url = url
        if urltimestamp is not None:
            self.urltimestamp = urltimestamp
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def source(self):
        r"""Gets the source of this EventDump.

        文件来源

        :return: The source of this EventDump.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this EventDump.

        文件来源

        :param source: The source of this EventDump.
        :type source: str
        """
        self._source = source

    @property
    def state(self):
        r"""Gets the state of this EventDump.

        文件状态

        :return: The state of this EventDump.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this EventDump.

        文件状态

        :param state: The state of this EventDump.
        :type state: str
        """
        self._state = state

    @property
    def description(self):
        r"""Gets the description of this EventDump.

        事件描述

        :return: The description of this EventDump.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this EventDump.

        事件描述

        :param description: The description of this EventDump.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        r"""Gets the id of this EventDump.

        文件id

        :return: The id of this EventDump.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this EventDump.

        文件id

        :param id: The id of this EventDump.
        :type id: str
        """
        self._id = id

    @property
    def filename(self):
        r"""Gets the filename of this EventDump.

        文件名

        :return: The filename of this EventDump.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        r"""Sets the filename of this EventDump.

        文件名

        :param filename: The filename of this EventDump.
        :type filename: str
        """
        self._filename = filename

    @property
    def obsname(self):
        r"""Gets the obsname of this EventDump.

        文件obs名

        :return: The obsname of this EventDump.
        :rtype: str
        """
        return self._obsname

    @obsname.setter
    def obsname(self, obsname):
        r"""Sets the obsname of this EventDump.

        文件obs名

        :param obsname: The obsname of this EventDump.
        :type obsname: str
        """
        self._obsname = obsname

    @property
    def tenantid(self):
        r"""Gets the tenantid of this EventDump.

        租户id

        :return: The tenantid of this EventDump.
        :rtype: str
        """
        return self._tenantid

    @tenantid.setter
    def tenantid(self, tenantid):
        r"""Sets the tenantid of this EventDump.

        租户id

        :param tenantid: The tenantid of this EventDump.
        :type tenantid: str
        """
        self._tenantid = tenantid

    @property
    def start(self):
        r"""Gets the start of this EventDump.

        统计开始时间

        :return: The start of this EventDump.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        r"""Sets the start of this EventDump.

        统计开始时间

        :param start: The start of this EventDump.
        :type start: int
        """
        self._start = start

    @property
    def end(self):
        r"""Gets the end of this EventDump.

        统计截止时间

        :return: The end of this EventDump.
        :rtype: int
        """
        return self._end

    @end.setter
    def end(self, end):
        r"""Sets the end of this EventDump.

        统计截止时间

        :param end: The end of this EventDump.
        :type end: int
        """
        self._end = end

    @property
    def total(self):
        r"""Gets the total of this EventDump.

        总计事件数

        :return: The total of this EventDump.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this EventDump.

        总计事件数

        :param total: The total of this EventDump.
        :type total: int
        """
        self._total = total

    @property
    def url(self):
        r"""Gets the url of this EventDump.

        链接

        :return: The url of this EventDump.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this EventDump.

        链接

        :param url: The url of this EventDump.
        :type url: str
        """
        self._url = url

    @property
    def urltimestamp(self):
        r"""Gets the urltimestamp of this EventDump.

        更新url时间戳

        :return: The urltimestamp of this EventDump.
        :rtype: int
        """
        return self._urltimestamp

    @urltimestamp.setter
    def urltimestamp(self, urltimestamp):
        r"""Sets the urltimestamp of this EventDump.

        更新url时间戳

        :param urltimestamp: The urltimestamp of this EventDump.
        :type urltimestamp: int
        """
        self._urltimestamp = urltimestamp

    @property
    def timestamp(self):
        r"""Gets the timestamp of this EventDump.

        文件生成时间戳

        :return: The timestamp of this EventDump.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this EventDump.

        文件生成时间戳

        :param timestamp: The timestamp of this EventDump.
        :type timestamp: int
        """
        self._timestamp = timestamp

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
        if not isinstance(other, EventDump):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
