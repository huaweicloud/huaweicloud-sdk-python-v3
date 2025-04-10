# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TagRecordVO:

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
        'tag_id': 'str',
        'tag_name': 'str',
        'biz_id': 'str',
        'biz_type': 'BizTypeEnum',
        'create_by': 'str',
        'update_by': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'tag_id': 'tag_id',
        'tag_name': 'tag_name',
        'biz_id': 'biz_id',
        'biz_type': 'biz_type',
        'create_by': 'create_by',
        'update_by': 'update_by',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, tag_id=None, tag_name=None, biz_id=None, biz_type=None, create_by=None, update_by=None, create_time=None, update_time=None):
        r"""TagRecordVO

        The model defined in huaweicloud sdk

        :param id: 编码，ID字符串。
        :type id: str
        :param tag_id: 标签ID，ID字符串。
        :type tag_id: str
        :param tag_name: 标签名称。
        :type tag_name: str
        :param biz_id: 实体ID，ID字符串。
        :type biz_id: str
        :param biz_type: 
        :type biz_type: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        :param create_by: 创建人。
        :type create_by: str
        :param update_by: 更新人。
        :type update_by: str
        :param create_time: 创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type create_time: datetime
        :param update_time: 更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type update_time: datetime
        """
        
        

        self._id = None
        self._tag_id = None
        self._tag_name = None
        self._biz_id = None
        self._biz_type = None
        self._create_by = None
        self._update_by = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.tag_id = tag_id
        if tag_name is not None:
            self.tag_name = tag_name
        self.biz_id = biz_id
        self.biz_type = biz_type
        if create_by is not None:
            self.create_by = create_by
        if update_by is not None:
            self.update_by = update_by
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this TagRecordVO.

        编码，ID字符串。

        :return: The id of this TagRecordVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TagRecordVO.

        编码，ID字符串。

        :param id: The id of this TagRecordVO.
        :type id: str
        """
        self._id = id

    @property
    def tag_id(self):
        r"""Gets the tag_id of this TagRecordVO.

        标签ID，ID字符串。

        :return: The tag_id of this TagRecordVO.
        :rtype: str
        """
        return self._tag_id

    @tag_id.setter
    def tag_id(self, tag_id):
        r"""Sets the tag_id of this TagRecordVO.

        标签ID，ID字符串。

        :param tag_id: The tag_id of this TagRecordVO.
        :type tag_id: str
        """
        self._tag_id = tag_id

    @property
    def tag_name(self):
        r"""Gets the tag_name of this TagRecordVO.

        标签名称。

        :return: The tag_name of this TagRecordVO.
        :rtype: str
        """
        return self._tag_name

    @tag_name.setter
    def tag_name(self, tag_name):
        r"""Sets the tag_name of this TagRecordVO.

        标签名称。

        :param tag_name: The tag_name of this TagRecordVO.
        :type tag_name: str
        """
        self._tag_name = tag_name

    @property
    def biz_id(self):
        r"""Gets the biz_id of this TagRecordVO.

        实体ID，ID字符串。

        :return: The biz_id of this TagRecordVO.
        :rtype: str
        """
        return self._biz_id

    @biz_id.setter
    def biz_id(self, biz_id):
        r"""Sets the biz_id of this TagRecordVO.

        实体ID，ID字符串。

        :param biz_id: The biz_id of this TagRecordVO.
        :type biz_id: str
        """
        self._biz_id = biz_id

    @property
    def biz_type(self):
        r"""Gets the biz_type of this TagRecordVO.

        :return: The biz_type of this TagRecordVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        """
        return self._biz_type

    @biz_type.setter
    def biz_type(self, biz_type):
        r"""Sets the biz_type of this TagRecordVO.

        :param biz_type: The biz_type of this TagRecordVO.
        :type biz_type: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        """
        self._biz_type = biz_type

    @property
    def create_by(self):
        r"""Gets the create_by of this TagRecordVO.

        创建人。

        :return: The create_by of this TagRecordVO.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this TagRecordVO.

        创建人。

        :param create_by: The create_by of this TagRecordVO.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def update_by(self):
        r"""Gets the update_by of this TagRecordVO.

        更新人。

        :return: The update_by of this TagRecordVO.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        r"""Sets the update_by of this TagRecordVO.

        更新人。

        :param update_by: The update_by of this TagRecordVO.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def create_time(self):
        r"""Gets the create_time of this TagRecordVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The create_time of this TagRecordVO.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this TagRecordVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param create_time: The create_time of this TagRecordVO.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this TagRecordVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The update_time of this TagRecordVO.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this TagRecordVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param update_time: The update_time of this TagRecordVO.
        :type update_time: datetime
        """
        self._update_time = update_time

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
        if not isinstance(other, TagRecordVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
